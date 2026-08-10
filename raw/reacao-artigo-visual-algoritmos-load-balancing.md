# Reação a artigo visual interativo sobre algoritmos de Load Balancing

Transcrição de vídeo (fala espontânea, com trechos de tradução simultânea de um artigo em inglês sobre balanceamento de carga com simulações visuais animadas). Limpo de repetições e cacoetes de fala, mantendo o conteúdo técnico e os comentários do apresentador.

## Contexto

O apresentador lê e comenta, em tempo real, um artigo interativo (em inglês) sobre load balancing. O artigo usa simulações animadas — bolinhas representando requisições sendo enviadas a servidores, encolhendo enquanto são processadas — para demonstrar visualmente o comportamento de diferentes algoritmos de balanceamento de carga sob variação de capacidade de servidor e custo de requisição.

## O problema visualizado

Depois de um certo ponto, uma aplicação web cresce a ponto de o deploy em servidor único não bastar. As empresas precisam aumentar disponibilidade, escalabilidade, ou os dois — então fazem deploy da aplicação em múltiplos servidores e usam um load balancer na frente para distribuir as chamadas. Grandes empresas podem ter centenas ou milhares de servidores rodando uma única aplicação para lidar com a carga.

**Simulação 1 — um único servidor:** um load balancer manda requisições a um único servidor a uma taxa de 1 requisição por segundo (rps). Cada requisição é representada por uma bolinha que encolhe enquanto o servidor processa — o tempo até a bolinha desaparecer é o tempo da requisição. Para muitos servidores esse setup funciona bem, mas servidores modernos lidam com múltiplas requisições simultâneas, e mesmo assim há um limite.

**Simulação 2 — servidor sobrecarregado:** com uma taxa de 3 rps, o servidor não consegue processar tudo. Se uma requisição chega enquanto outra está sendo processada e o servidor não tem capacidade, ele **dropa** a requisição — o resultado disso é um erro mostrado ao usuário, algo que se quer evitar.

**Simulação 3 — adicionando um segundo servidor:** com dois servidores atrás do load balancer, a mesma taxa de 3 rps passa a ser atendida sem drops. A estratégia usada pelo load balancer aqui é enviar uma requisição para cada servidor, alternadamente, em sua vez — **Round Robin**.

## Round Robin

Round Robin é uma das formas mais simples de fazer balanceamento de carga: distribui uma requisição por vez, ciclicamente, entre os servidores disponíveis. Funciona bem quando os servidores têm potência equilibrada entre si e as requisições têm custo de processamento equivalente. É o algoritmo padrão do Nginx quando usado como load balancer HTTP.

No mundo real, porém, é raro que os servidores tenham potência equalizada e que as requisições tenham o mesmo custo — mesmo em servidores idênticos, requisições diferentes exigem quantidades de processamento diferentes.

**Simulação 4 — custo de requisição variado:** com requisições de custos diferentes (algumas demoram mais para "encolher" do que outras), o Round Robin continua distribuindo como se todas as requisições e servidores fossem iguais. Resultado: mesmo com a maioria das requisições sendo atendidas com sucesso, algumas acabam sendo dropadas, porque o algoritmo ignora a variação real de custo.

### Mitigação: fila de requisições

Uma forma comum de mitigar o problema de drops é adicionar uma **fila de requisições** na frente de cada servidor (na prática, implementada com filas de mensagens como Redis ou RabbitMQ). A requisição só é dropada se a fila também estiver cheia.

Isso é um trade-off (uma "faca de dois gumes"): reduz o número de requisições dropadas, mas ao custo de latência maior para algumas requisições, que ficam esperando na fila. Além disso, com custo de requisição variado, o servidor começa a perder o balanço — as filas tendem a se acumular de forma desigual entre os servidores.

## Weighted Round Robin

Combinando variação de custo de requisição **e** variação de potência entre servidores (alguns mais potentes, outros menos), o Round Robin simples se mostra fraco: servidores mais fracos derrubam requisições mais rápido enquanto servidores mais potentes ficam ociosos.

A correção é dar um "peso" (weight) a cada servidor, proporcional à sua capacidade — servidores mais potentes recebem proporcionalmente mais requisições. É o **Weighted Round Robin**: um Round Robin ponderado, análogo a uma média ponderada, em que o peso funciona como um multiplicador de quantas requisições por segundo aquele servidor recebe.

**Limitação:** colocar um peso manualmente em cada servidor não escala na prática. Chegar a um peso correto exigiria testes de carga com dados reais para saber a capacidade real de cada servidor — algo raramente feito. E mesmo que o peso do servidor esteja calibrado, o peso "ideal" de uma requisição individual (o quão cara ela é) não é conhecido de antemão.

## Weighted Round Robin Dinâmico (baseado em latência)

Uma variante do Weighted Round Robin calcula os pesos **dinamicamente**, usando a latência observada como métrica proxy: um servidor que respondeu 3 requisições mais rápido que outro, na mesma janela, deveria proporcionalmente receber cerca de 3x mais requisições que o outro.

Na prática: o algoritmo guarda a média de latência das últimas N requisições servidas por cada servidor e decide a próxima distribuição com base na diferença entre essas latências — sem que ninguém precise especificar um peso manualmente. É o **Dynamic Weighted Round Robin**. Ele se adapta continuamente à performance observada de cada servidor durante a execução.

Em cenários de alta variância (servidores com potências muito diferentes e requisições com custos muito diferentes), o Dynamic Weighted Round Robin ainda dropa alguma requisição ocasionalmente, mas se ajusta bem à variação ao longo do tempo.

## Least Connections

Um algoritmo mais forte parte de uma observação simples: o load balancer está posicionado entre o usuário e os servidores, então ele pode manter um registro exato de quantas requisições estão em andamento (não finalizadas) em cada servidor. Quando uma nova requisição chega, o load balancer escolhe o servidor com **menos conexões em aberto** no momento — **Least Connections**.

Esse algoritmo performa extremamente bem independentemente da variação de potência de servidor ou custo de requisição, porque elimina a incerteza: ao invés de estimar ou inferir, ele sabe com precisão qual servidor está menos ocupado.

**Analogia do apresentador:** o comportamento do Least Connections é comparado a um gerente de microgerenciamento constante — sempre de olho em quem está com menos trabalho, mandando mais tarefas para quem está livre. "Ele é um baita otário, mas ele faz o trabalho ser feito" — e a vantagem adicional é a simplicidade de implementação.

**Limitação:** mesmo o Least Connections não é imune a drops — a diferença é que ele só deixa uma requisição cair quando **todas** as filas de todos os servidores já estão completamente cheias, ou seja, quando não há mais capacidade de processamento em lugar nenhum do sistema. Ainda assim, não otimiza diretamente para latência.

## Otimizando latência: combinando os dois mundos

O artigo propõe uma pergunta natural: e se for possível combinar a adaptação dinâmica do Weighted Round Robin (baseada em latência) com a resiliência do Least Connections (baseada em conexões abertas)? O algoritmo citado para isso é o **PEWMA — Pick Exponentially Weighted Moving Average** (ou EWMA), que combina latência ponderada por média móvel exponencial com o monitoramento de carga em tempo real, buscando o melhor dos dois algoritmos anteriores: baixa latência com alta resiliência a drops.

## Conclusão do artigo (segundo o apresentador)

O artigo termina com um disclaimer importante: qualquer conclusão tirada de simulações genéricas deve ser validada com **benchmark contra a carga real do seu próprio sistema**, e não apenas copiada de dicas encontradas na internet. A recomendação final é sempre testar você mesmo antes de escolher um algoritmo de balanceamento de carga para produção.

## Observações do apresentador (fora do artigo)

- O apresentador reflete sobre como equipes de plataforma/observabilidade em empresas maiores dedicam pessoas especificamente a ajustar e manter esse tipo de balanceamento em produção, ao invés de dividir a responsabilidade em muitos times diferentes.
- Comentário lateral sobre a dificuldade de tradução simultânea de termos técnicos em inglês (availability, request, drop, benchmark, tradeoff, vanilla) para português, com a decisão de traduzir "requisição" para request e manter "benchmark" sem tradução (termo sem equivalente direto consagrado).
