# Rate Limit: estratégias de implementação (fixed window, sliding window, token bucket, leaky bucket) — Bernardo Lobato

Transcrição de vídeo (pt-BR) do canal de Bernardo Lobato; parte 2 da série sobre rate limit (a parte 1 está em `raw/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato.md`). ASR bruto limpo, pontuado e organizado em seções; conteúdo técnico preservado, sem tradução (já estava em português). Pedidos de comentário/audiência omitidos. Termos reconhecidos erroneamente pelo ASR foram corrigidos pelo contexto: "P/PI" = API; "end point/edp" = endpoint; "ratit/rate limito" = rate limit; "Slide Window" = sliding window; "fixed de window/fixa de window" = fixed window; "lick/Lak/leak bucket" = leaky bucket; "Cong" = Kong; "SAS" = SaaS; "APS públicas" = APIs públicas; "birsts" = bursts; "ingresso.com" mantido como citado. Valores corrigidos pelo contexto: "seis requisições" (após zerar o contador) = 100 requisições; "sem requisições nos últimos 60 segundos" = 100 requisições nos últimos 60 segundos; "últimos 6 segundos" (tabela) = últimos 60 segundos; "10 clientes" no caso do token bucket é aproximado ("uns 10 clientes"); "10 tokens 100 tokens por segundo" = 100 tokens por segundo (autor se corrige).

## Abertura

Situação: a API é bombardeada de requisições, mas não dá para simplesmente bloquear, seja por regra de negócio específica, seja porque alguns endpoints são mais importantes que outros. O vídeo apresenta estratégias de implementação de rate limit e casos de aplicação numa arquitetura realista. Na primeira edição o foco foi onde colocar o rate limit, qual contexto precisa conhecer e os desafios de compartilhar o componente em sistemas distribuídos; aqui o foco é nas **estratégias de implementação**.

Ponto de partida: pela análise de volumetria, um cliente pode fazer até **100 requisições por minuto**. Parece simples (um contador por cliente), mas é preciso responder o que significa exatamente "100 por minuto" e como controlar isso. Quatro estratégias mais conhecidas: **fixed window, sliding window, token bucket e leaky bucket**, comparando comportamento e complexidade.

## Fixed window

Divide o tempo em **janelas fixas**: 10:00–10:01, 10:01–10:02, 10:02–10:03 etc. Conta as requisições do cliente na janela; ao chegar a 100, as próximas são bloqueadas até o início da próxima janela, quando o contador zera e libera de novo 100. Muito simples de implementar; funciona bem para política básica.

**Problema (burst na fronteira):** o cliente fica de 10:00:00 a 10:00:59 sem enviar nada e manda as 100 requisições numa rajada de 1 segundo; às 10:01:00 a janela reinicia e ele manda mais 100 em 1 segundo. O sistema deixa passar: **200 requisições em ~2 segundos** sem quebrar nenhuma regra. Se todos os clientes fizerem o mesmo, há um pico perigoso na infraestrutura. Pode ser aceitável em várias situações, mas em outras gera um burst maior do que o desejado.

**Quando faz sentido:**
- **Cota contratual** (X requisições por minuto/hora/dia): o raciocínio é estritamente contratual, sem considerar uso de recursos; subentende-se que o sistema dá conta dos picos na fronteira. Comum em cotas de API dentro de um SaaS ou de um API gateway.
- **APIs públicas / endpoints que não se quer deixar totalmente abertos:** uma barreira contra chamadas excessivas, não exige algoritmo preciso. Endpoints como **login** se beneficiam de uma proteção simples, inclusive contra tentativa de invasão por força bruta.
- Frameworks e gateways de mercado oferecem o modelo. O **Kong** suporta explicitamente limites em janela fixa por consumidor, credencial, IP, serviço, rota etc.

Quando o uso de recursos e a fronteira da janela viram problema maior, o fixed window não resolve tudo.

## Sliding window

Em vez de blocos fixos, olha uma **janela que acompanha o momento atual**: não "10:00 às 10:01", mas "os últimos 60 segundos". Regra: 100 requisições nos últimos 60 segundos; quando chega uma nova, conta quantas o cliente fez nos 60 segundos anteriores. A janela está sempre se deslocando, o que reduz bastante o problema do fixed window: **não há mais fronteira fixa em que o contador é zerado**.

**Custo:** é preciso guardar mais informação sobre as requisições para calcular a janela; um simples contador não resolve. Dependendo da implementação: mais memória, mais operações de I/O no armazenamento, lógica mais complicada, ainda mais se a arquitetura é distribuída. Troca comum de arquitetura: controle mais preciso, pago em complexidade e recursos.

**Quando faz sentido:** quando a fronteira artificial das janelas fixas vira problema; quando a **distribuição** das requisições é tão importante quanto a quantidade (limitação de recursos de infra, adequação dos clientes). A documentação do Kong descreve o cenário: sliding window mantém a taxa dentro do limite configurado, enquanto fixed window pode permitir volume maior na transição entre janelas. Diretriz: não se quer que o cliente tenha pico descontrolado mesmo por poucos segundos.

## Token bucket

E se não for possível evitar a rajada e for preciso ser mais flexível? Já apresentado brevemente no vídeo anterior; recapitulação.

Um **balde (bucket) que recebe tokens ao longo do tempo**; o token é basicamente um número. A ideia de balde explicita que há **limite**: os tokens não são adicionados infinitamente, uma hora o balde transborda. Cada requisição consome X tokens (definido por quem implementa). Enquanto há tokens, o consumo continua; com o balde vazio, a requisição é limitada ou bloqueada; passada a janela de tempo especificada, tokens são repostos e o acesso é liberado.

**Exemplo:** reposição de **100 tokens por segundo**, capacidade do bucket de **200 tokens**, cada requisição consome 1 token. Com poucas requisições os tokens se acumulam até 200; num pico, o cliente consome o acumulado rapidamente: até **200 requisições** com o bucket cheio. Isso permite **bursts (picos) controlados** e trabalha com uma espécie de **média de consumo** por cliente, admitindo picos dentro da capacidade configurada.

**Pesos por endpoint:** se a contabilização é por endpoint, é possível dar pesos diferentes. Um endpoint que consome muito recurso pode ter peso 10, enquanto GETs simples e corriqueiros têm peso 1: uma requisição ao endpoint pesado consome 10 vezes mais tokens. Permite controlar ainda mais os recursos. Por isso o algoritmo aparece bastante em API gateways: limitar consumo sem exigir taxa completamente uniforme.

### Caso real do autor (token bucket com pesos)

Projeto de alguns anos atrás, contado sem detalhar o projeto: cerca de 10 clientes e uma API bem pesada. Cada cliente fazia **sincronização de dados em segundo plano**, várias vezes por dia, chamando um endpoint que devolvia a **diferença de dados desde a última chamada daquele cliente** — um endpoint que pode consumir muito processamento e memória conforme o volume devolvido. Alguns clientes **automatizaram e paralelizaram** a sincronização, gerando consumo muito alto e muitos picos, o que prejudicava a API como um todo: os outros endpoints, os outros clientes e também o **portal front-end**, usado por milhares de pessoas vinculadas aos clientes (endpoints simples do dia a dia).

**Solução:** token bucket como estratégia de rate limit — por exemplo, **10.000 tokens por hora por cliente**; requisição simples do portal pesa **1 token**, requisição de sincronização pesada consome **~1000 tokens**. Resultado: picos controlados **sem mexer no código da API**; o portal consumia os endpoints simples tranquilamente e as sincronizações consumiam só o que fora projetado. Teve até **caráter pedagógico**: alguns clientes ajustaram seus processos para não receber tantos **429**. Para o autor a solução é interessante porque junta a questão contratual de negócio com a técnica, sem mexer em infra, desenho ou regra de negócio específica.

**Conclusão:** token bucket faz sentido quando se quer controlar uma **taxa média de consumo**, sabendo que certos picos são aceitáveis e se quer limitar justamente esses picos. Não trata todo pico como problema: admite a existência do burst e define quanto dele o sistema consegue consumir.

## Leaky bucket

Ideia parecida, comportamento diferente. As requisições **entram em um balde e são processadas ou liberadas a uma taxa determinada**; se muitas entram de uma vez, podem **ficar aguardando** enquanto são liberadas de forma controlada. Token bucket é bom para permitir picos controlados; leaky bucket é bom para **saída previsível** e uso mais controlável da infra — especialmente quando o recurso por trás do rate limit é mais estável e menos elástico, como um **sistema legado**.

**Exemplo:** serviço que processa ~100 requisições por segundo; se chegam 100 de uma vez, pode não ser interessante encaminhar tudo de uma vez. Com leaky bucket, colocam-se numa fila e liberam-se a uma taxa controlada, "a conta-gotas". Transforma uma **entrada potencialmente irregular numa saída previsível**.

O leaky bucket **não precisa estar atrelado ao HTTP**: numa aplicação que recebe solicitações para gerar PDF, processar imagem, enviar e-mail, gerar relatório etc., as solicitações podem entrar num tipo de fila e ser processadas a taxa controlada antes de bloquear qualquer uma. **Ressalva do autor:** fala de "fila" só para facilitar a explicação; **não** é processamento assíncrono nem event sourcing — são estratégias de rate limit.

### Consumo de serviços de terceiros (client rate limit)

Exemplo: aplicação tipo iFood, ou plataforma de venda de ingresso como ingresso.com. Cada uma chama endpoints externos de APIs dos seus clientes/parceiros (restaurantes, redes de cinema). A aplicação pode precisar consumir essas APIs externas **sem conhecer a capacidade real delas**. O controle deve existir (e provavelmente existe) também na API do parceiro, mas não há como validar isso em todas as APIs externas. Daí o **client rate limit**: implementar o controle **do nosso lado**, para garantir que a aplicação não ultrapasse uma taxa de chamadas à API do parceiro, e para evitar inundar os próprios logs com erros. É uma forma de respeitar a infra do parceiro: o usuário final pode gerar centenas de solicitações rapidamente, enquanto o processamento real precisa ocorrer a velocidade menor.

O **Kong** implementa leaky bucket como estratégia avançada de rate limit; a documentação atual lista explicitamente o leaky bucket como algoritmo suportado.

## Qual estratégia usar (tabela do vídeo)

| Estratégia | O que controla |
|---|---|
| Fixed window | Cota por janela de tempo |
| Sliding window | Cota pelos últimos 60 segundos |
| Token bucket | Taxa + pico controlado |
| Leaky bucket | Saída com taxa controlada |

As estratégias **não são versões melhores ou piores** umas das outras; cada uma representa um comportamento que deve ser usado para o problema que se tem. Não há bala de prata na arquitetura de software.

- **Fixed window:** implementação simples; política por intervalos fixos.
- **Sliding window:** visão mais precisa da utilização recente.
- **Token bucket:** taxa média + picos controlados dentro da capacidade configurada.
- **Leaky bucket:** melhor controle da taxa de saída; suaviza picos.

A escolha depende mais do **comportamento que se quer produzir** e do problema em mãos do que de escolher o algoritmo mais sofisticado. É também por isso que a configuração de rate limit muda de cenário para cenário; conhecer ao menos a ideia central de cada estratégia amplia o repertório técnico.

## Fechamento: duas decisões e uma terceira parte

Juntando com o vídeo anterior, há duas decisões: (1) **onde colocar** o rate limit (borda, gateway, load balancer, aplicação); (2) **como controlar o consumo** (fixed window, sliding window, token bucket, leaky bucket). Falta uma terceira, tão importante: colocar tudo para funcionar **em produção numa arquitetura distribuída** — como compartilhar estado entre várias instâncias (onde entram Redis ou cache compartilhado), como lidar com concorrência, o que acontece se o mecanismo de rate limit ficar indisponível. O autor pergunta se há interesse numa terceira parte e pede que os espectadores contem se já implementaram rate limit e qual problema tentavam resolver.
