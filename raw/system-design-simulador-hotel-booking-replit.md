# System Design na Prática: Construindo um Simulador e Desenhando um Sistema de Hotel Booking com Replit

## Por que system design importa mesmo para quem não programa

Hoje o assunto é system design — algo bem técnico, explicado para quem não é técnico. A tese é a seguinte: no mundo em que a inteligência artificial está escrevendo cada vez mais código, a maior contribuição de um programador (ou de alguém que está "vibe codando" um projeto) na construção de um software é saber desenhar o sistema.

O gatilho para esse vídeo foi uma pergunta recebida nos últimos dias: vale a pena aprender LeetCode e system design para entrevista de emprego? A resposta foi um simples "sim", com o seguinte argumento: esse conhecimento — estudar system design, estudar LeetCode — é hoje basicamente a única coisa que não é impactada pela inteligência artificial.

## O que separa um software bom de um software ruim

No final do dia, a diferença entre um software bom e um ruim se resume a isto: o quão lento ele é, quantos erros ele joga na cara do usuário, e se — quando alguém faz uma modificação no sistema — essa modificação de fato se propaga em todas as camadas do sistema.

A coisa mais irritante que pode acontecer com um usuário é: ele modificar algo numa tela, voltar para outra tela, e aquela informação não estar lá. Ou clicar num botão, o sistema ser tão lento que ele clica de novo, e o sistema ser burro o suficiente para disparar duas requisições, cancelando a anterior — cada clique repetido é, na prática, um passo para trás.

Não é a linguagem de programação que a IA escolheu para o projeto. Não é se a pessoa escreveu o código à mão ou deixou a IA escrever via prompt. No final do dia o que importa é se a pessoa sabe desenhar o sistema — porque para escalar o sistema e ter uma arquitetura bem feita (do tipo que "dá orgulho pra mãe"), é preciso saber o que é um CDN, o que é caching, o que é uma fila de processamento (queueing), o que é rate limiting, e várias outras coisas que só se aprendem resolvendo problemas de system design.

Para guardar informação, é preciso pensar em data retention, em padrões de escrita e leitura, em SQL ou NoSQL, e na diferença entre OLAP e OLTP:

- **OLTP** (Online Transaction Processing): sistema voltado a registrar operações rápidas do dia a dia — muitas escritas e leituras pequenas.
- **OLAP** (Online Analytical Processing): arquitetura voltada a consultar, agregar e explorar grandes volumes de dados.

## A ideia de produto: um simulador de system design

A proposta do vídeo é colocar isso em prática: desenhar um sistema junto e simular o que aconteceria se ele fosse colocado em produção. No processo, surgiu uma nova ideia de SaaS — um simulador de system design — construída usando o Replit.

O raciocínio por trás da ideia: system design é importante não só para quem programa, mas para quem está "vibe codando" agora e nem quer aprender a programar de fato. Só que, para o software final ser bom, antes de escrever código é preciso saber desenhar o sistema. Logo, as pessoas precisam de um playground para isso — um playground que tenha (1) um simulador para testar se o desenho funciona e (2) uma IA revisando se o que foi desenhado faz sentido.

O processo de criação começou jogando essa ideia para o agente do Replit. O método de trabalho costuma ser: começar com uma única funcionalidade, pensar nos dados de entrada e saída do sistema, e depois pensar no fluxo — se o usuário vai usar aquilo o suficiente para pagar pela solução.

Um princípio reforçado (já mencionado em vídeos anteriores do canal): em 2026, se a intenção é criar um projeto, ele deve ser lançado desde o dia um já com monetização — seja por assinatura, seja por pagamento único. E deve ser lançado com uma única funcionalidade: aquela pela qual as pessoas pagariam para usar. Nesse caso, a funcionalidade única seria o simulador — não apenas um lugar para desenhar o diagrama de system design (isso qualquer ferramenta tipo Excalidraw já resolve de graça), mas o simulador funcionando de fato.

### Auto-crítica sobre o escopo do produto

O projeto ganhou, no primeiro prompt, quatro problemas de exemplo para resolver, uma tela de componentes, um simulador de caos (o que acontece se o data center cair, se a availability zone cair) e uma funcionalidade de pontuação via IA do desenho feito. Em retrospecto, a avaliação foi que a funcionalidade de simulador de caos foi um erro de escopo nesse estágio — o ideal teria sido focar exclusivamente em criar o simulador como o produto pago, deixando o resto para depois, mas o entusiasmo no prompt inicial levou a abraçar funcionalidade demais de uma vez.

Outra lacuna identificada: falta um tutorial. A sugestão foi criar um primeiro problema — mais fácil — que funcione como tutorial, levando o usuário para a tela do simulador e fazendo highlight, passo a passo, de quais elementos incluir no playground, como conectar um componente a outro, e como rodar o simulador. O prompt usado para pedir isso ao agente foi (em inglês, como escrito originalmente):

> "Let's create a simple problem as a tutorial. For instance, give me three ideas, and when the user selects this problem we navigate the user to the simulator, and there we highlight step by step what elements the user should include in the playground, and a tip when they need to connect one component to another. And after that, how to run the simulator. We should first implement, step by step, a simple user flow — how system design impacts performance, etc."

## Os quatro exercícios base de system design

O produto foi lançado com quatro exemplos de exercícios de system design, escolhidos por serem clássicos de entrevista e por cobrirem praticamente todos os tópicos que um programador precisa saber hoje (e que muitos projetos "vibe codados" também precisam resolver):

1. **URL shortener** — um site que reduz o tamanho de uma URL, tipo um bit.ly.
2. **Feed do Twitter/X**.
3. **Uber** — como encontrar motoristas com mais de 1 milhão de requisições por segundo.
4. **Plataforma de mensageria em tempo real**, tipo Slack.

## Fluxo de trabalho com os agentes do Replit

A tela de componentes precisou de um prompt específico, listando todos os componentes lembrados de um system design: client, mobile, DNS, CDN, load balancer, WAF, API Gateway, entre outros.

O fluxo de trabalho descrito com o Replit: normalmente há uma sessão principal fazendo algo maior (uma refatoração, um problema maior), e subtarefas menores são criadas em paralelo, sem conflitar com a sessão principal — o próprio Replit resolve os conflitos e faz o merge de tudo de volta para a sessão principal. Essas execuções paralelas aparecem como "workers" na interface, sugerindo que o Replit usa git worktrees por baixo dos panos.

Nesse processo, duas tarefas paralelas foram criadas: (1) ajustar o estilo de cores, que estava inconsistente entre o dashboard e a tela de sessão, e (2) implementar um efeito "liquid glass" (glass morphism, similar ao "liquid glass" da Apple, mas para a web) no header da homepage, usando uma biblioteca vista recentemente.

Rodar duas tarefas em paralelo no plano usado exigiu upgrade para o plano "Replit Core" — parcialmente motivado por ter convidado um colaborador (Augusto Galego) como editor do projeto, para vibe codar em conjunto. Com múltiplas pessoas, o taskboard (semelhante a um Kanban) passa a fazer mais sentido, permitindo ver a evolução de várias tarefas paralelas criadas por diferentes pessoas para os agentes.

O plano Replit Core mencionado oferece: $10 de crédito de bônus na assinatura, 20 dólares/mês em créditos, convite de até cinco colaboradores, trabalho em paralelo com até dois agentes, publicação de projetos em qualquer região, e múltiplos workspaces.

### Testes end-to-end automáticos

Um destaque do harness do Replit: ao implementar algo, o agente escreve um teste, roda esse teste do início ao fim (end-to-end), analisa se o resultado do teste corresponde ao que foi pedido, e fica em loop resolvendo os problemas encontrados até o teste passar. Isso dá confiança de que, quando o agente termina uma tarefa, ele já testou o sistema. O vídeo é patrocinado pelo Replit, mas essa avaliação sobre a qualidade do harness é apresentada como observação genuína, anterior à parceria comercial.

## Exercício prático: desenhando um sistema de reserva de hotel (Hotel Booking)

Com o tutorial pronto, o problema escolhido para demonstração foi "Build a Hotel Booking Page". O sistema descreve o cenário: busca e reserva de quartos de hóspedes é um problema clássico de aplicação com leitura pesada. A proposta é construir uma versão simples, rodar para identificar os gargalos (bottlenecks), e depois corrigir.

### Passo a passo do desenho

1. **Client**: adicionado ao canvas — representa os hóspedes visitando o site.
2. **App Server**: adicionado e conectado ao client.
3. **SQL Database**: adicionado para verificar disponibilidade de quartos e armazenar as reservas; conectado ao app server.
4. **Rodar o simulador**: o fluxo simulado mostra uma requisição do cliente chegando ao servidor de aplicação, que consulta o SQL database.

### Primeiro gargalo identificado

O simulador aponta o SQL database piscando em vermelho — na capacidade máxima. Qualquer acesso à página de reserva vai direto ao banco de dados. O simulador mostra métricas em tempo real de alta latência e sinaliza o gargalo (bottleneck flag). A disponibilidade (availability) do sistema cai para 55%. Aumentar o tráfego simulado sobrecarrega ainda mais o app server.

O próprio simulador sugere a correção: a maioria dos hóspedes vê os mesmos quartos populares repetidamente — um cache pode atender essas leituras repetidas.

### Correção 1 — Cache

Um componente de cache é adicionado e conectado ao app server. O resultado no simulador: sem o cache, o bottleneck do SQL database estava em 115%; com o cache conectado, o uso do banco de dados cai significativamente para o mesmo volume de tráfego — demonstração direta do poder do caching em sistemas de leitura intensa (read-heavy).

### Correção 2 — Load Balancer

Em seguida, um load balancer é inserido entre o client e o app server (client → load balancer → app server). O ponto levantado: numa entrevista, é preciso justificar o algoritmo de balanceamento escolhido — round robin, least connections, ou outro método — cada um com vantagens diferentes. Nesse momento do exercício, porém, o foco escolhido foi reduzir a carga no banco de dados SQL via escalabilidade horizontal, e não aprofundar no algoritmo do load balancer.

### Correção 3 — Escalabilidade horizontal do banco de dados (réplicas)

O simulador limita a quantidade de instâncias (réplicas) do banco de dados. Escalar horizontalmente significa adicionar novas instâncias do banco para distribuir a carga de leitura. Ao aumentar o número de réplicas, o alerta de bottleneck no banco desaparece — mas o gargalo se desloca: aumentar réplicas de banco de dados sem tratar a camada de aplicação eventualmente empurra o gargalo para o app server. Nesse ponto, seria necessário introduzir novos componentes e técnicas como sharding (charge/shard database) para aprofundar ainda mais a camada de dados.

### Correção 4 — Fila de mensageria (Message Queue)

Para aliviar o app server, a solução discutida foi adicionar uma fila de processamento (message queue). O simulador oferece opções: Kafka, EventBridge/Event Sub, entre outras. A escolha depende do critério que se está priorizando — e numa entrevista, essa é justamente uma pergunta importante a se fazer ao entrevistador: o critério é capacidade de lidar com grandes volumes de dados, facilidade de integração com o sistema atual, ou necessidade de alta disponibilidade?

Nesse cenário, o critério escolhido foi capacidade de lidar com grandes volumes de dados — o que leva à escolha do Kafka.

**Kafka**: definido no vídeo como uma plataforma de streaming de eventos distribuídos, reconhecidamente complexa — potencialmente over-engineering para um sistema de reserva de hotel, mas usada aqui como exercício. O app server foi conectado ao Kafka, reduzindo o acesso direto do app server à base de dados. Isso, por sua vez, levanta a necessidade de ter algo consumindo as mensagens gerenciadas pelo Kafka (quem consome essas mensagens?) — pergunta deixada em aberto no exercício.

Componentes adicionais também podem ser incluídos no desenho, como métricas e logs.

### Pontuação final da IA

O sistema de duas IAs avaliadoras (que chegam a um consenso entre si) deu nota **58 de 100** ao desenho final. Ambas concordaram que os acertos foram: load balancer, cache e database. Como pontos faltantes, apontaram: réplicas de SQL, invalidação de cache (cache invalidation), e observaram que Kafka, logs e métricas foram introduzidos sem uma justificativa clara — avaliação correta, já que esses componentes foram adicionados ao canvas sem que nada estivesse de fato consumindo ou processando as mensagens/logs no desenho.

## Conclusão

A prática de exercícios de system design como este permite não só entender melhor a arquitetura de sistemas distribuídos, mas também "vibe codar" melhor a própria solução — e, para quem programa, esse tipo de conhecimento macro é apontado como algo que não pode ser delegado para a IA.

O vídeo encerra com o link do simulador e o link de convite do Replit (upgrade para o Replit Core garante crédito de bônus).
