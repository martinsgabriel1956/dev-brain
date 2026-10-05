# RabbitMQ: como funciona, para que serve e quando usar (com simulador)

Fonte: transcrição automática de vídeo do YouTube, colada pelo usuário em 2026-10-05. Autor/canal não identificados na transcrição (o único nome citado é "Rafael", dito por um interlocutor imaginário no meio do vídeo). Já em português — sem tradução. Foram adicionados apenas pontuação, parágrafos e títulos; erros de reconhecimento foram corrigidos por contexto.

Termos corrigidos (reconhecimento automático): "Rabit MQ / Rabbit Mkill / Rabbit MQill" → RabbitMQ; "Prodchange" → Producer → Exchange; "Team Kill / kill" → fila (queue); "Fenout / fun / Fen" → Fanout; "Poraders / headers" → Headers; "decknolge / deck" → ack (acknowledgment); "Cafk / Kafka" → Kafka; "M Transit" → MassTransit; "lacat pay" → AbacatePay (grafia incerta); "pag seguro" → PagSeguro; "pro Dnet" → para .NET; "rejex" → regex; "jogo da velha" → `#` (cerquilha); "asterístico" → `*`; "HTP" → HTTP; "pub sub" → pub/sub; "page de pagamentos" → parte de pagamentos; "paid" mantido como routing key `order.paid`.

---

## Abertura

RabbitMQ é uma daquelas ferramentas que muita gente usa, mas poucos sabem o que acontece "no meio". A maioria dos devs aprende que é "um lugar onde você manda uma mensagem que outro sistema vai consumir". O problema: sem entender o modelo mental do RabbitMQ — ou o problema que ele resolve — você o usa de forma errada, ou o usa quando nem precisava (o que é pior). O vídeo promete ensinar como funciona, para que serve, como usar, e mostrar cenários reais num simulador que o autor construiu para o vídeo.

## O problema: uma loja e o fluxo síncrono

Imagine uma loja. O usuário faz um pedido. Depois disso o sistema precisa: registrar o pedido, processar o pagamento, emitir a nota fiscal, alterar o estoque e enviar e-mail de confirmação.

- Processar pagamento depende de um sistema externo (PagSeguro, Stripe, AbacatePay...).
- Emitir nota depende de sistema externo (governo/Receita Federal ou um gateway intermediário).
- Enviar e-mail também depende de sistema externo.

Imagine o usuário esperando todos esses processamentos externos para só então receber a resposta de que o pedido deu certo (ou errado). Pior: se no meio do caminho der problema ao alterar o estoque ou emitir a nota, é preciso desfazer todo o processo.

## Por que RabbitMQ e não requests HTTP entre serviços

Muita gente acha que só quebrar um serviço em microsserviços já resolve tudo. Na prática, com HTTP: a UI faz request para Pedidos → Pedidos chama Pagamentos e espera → depois chama Nota Fiscal e espera → depois chama Estoque e espera → depois chama E-mail e espera → só então responde ao usuário. Se o sistema de nota fiscal cair, o governo ficar fora do ar ou demorar, houver alta demanda, ou o sistema de pagamentos cair (como aconteceu com a AbacatePay), tudo trava — você fica dependente de todos.

> "Microsserviços que têm dependências fora do microsserviço deles não são microsserviços de verdade; são monolitos distribuídos."

### A solução com mensageria

Pedidos, em vez de chamar Pagamentos e esperar, publica uma mensagem no RabbitMQ: "pedido criado". O usuário já pode receber a resposta nesse ponto. Todos os serviços interessados leem a mensagem e agem por conta própria:

- Pagamentos consome "pedido criado", tenta o pagamento e publica "pagamento aprovado" ou "reprovado".
- E-mail consome essa mensagem e manda e-mail de confirmação ou de falha.

RabbitMQ é um **message broker**: recebe mensagens, faz a transmissão entre os sistemas e gerencia essas operações de forma assíncrona.

## O modelo mental: Producer → Exchange → Fila → Consumer

O simulador mostra quatro peças:

1. **Producer (produtor):** pode ser uma API, um console app, um processo em background.
2. **Exchange:** o produtor **não manda mensagem direto para a fila — manda para uma exchange**, que decide para qual(is) fila(s) a mensagem vai. "Se você for guardar alguma informação desse vídeo, guarda isso: Producer → Exchange, e não para a fila. Quem pensa é a exchange."
3. **Fila (queue):** FIFO — primeiro a entrar, primeiro a sair.
4. **Consumer (consumidor):** pode ser um serviço, uma API, ou até o mesmo serviço que publicou.

O "pulo do gato" da configuração está na exchange. Existem quatro tipos: **direct, fanout, topic e headers**. O simulador tem documentação própria sobre RabbitMQ.

## Tipos de exchange

### Direct

Roteamento exato por **binding key / routing key**: a exchange entrega a mensagem para a fila cuja binding key é igual à routing key da mensagem.

Exemplo no simulador: `order-service` (producer) → exchange direct → fila com binding `order.created` → `payment-service` (consumer). Ao enviar `order.created`, a mensagem bate na exchange, vai para a fila e o serviço de pagamento consome. Dá para criar outras filas com bindings `order.canceled` e `order.error`, cada uma com seu consumidor; cada mensagem vai só para a fila com a chave correspondente. "Simples, fácil, direto."

### Fanout

**Ignora a routing key.** Funciona como broadcast: a mensagem vai para **todas** as filas ligadas à exchange. Exemplo: fila 1 (payment-service) e fila 2 (estoque) ligadas a uma exchange fanout; ao enviar `order.created`, as duas filas recebem. Poderia haver também uma fila do serviço de notificações. É útil para "o pedido foi criado e muita gente precisa saber"; segundo o autor, é **o tipo mais usado, pela simplicidade**. Objeção comum — "se alguém não deve receber, é só não estar na exchange" — mas para filtrar existe o topic.

### Topic

Respeita a binding key como se fosse um padrão (parecido com regex), com dois curingas:

- `*` (asterisco) = **exatamente uma palavra**.
- `#` ("jogo da velha") = **zero ou mais palavras**.

Exemplo: fila de pagamentos com binding `order.created`; fila de estoque com `order.paid` (só reduz estoque quando o pedido é pago); fila de notificações com `order.*` (quer ser avisada de qualquer evento de pedido: criado, pago, erro). Mensagem `order.created` vai para pagamentos e notificações; `order.paid` vai para estoque e notificações.

Diferença entre `*` e `#`: com binding `order.*`, uma mensagem `order.paid.toerx` (várias palavras) **não** casa; com `order.#` casa. Para um sistema de **audit log** que deve receber toda e qualquer mensagem, usa-se só `#`. O autor diz: quando você começa a usar topic, é sinal de que o sistema está escalando e sendo organizado direito.

### Headers

Roteia pelo **cabeçalho da mensagem** em vez da routing key (que é ignorada). Ex.: `país = Brasil` — a fila só consome eventos originados no Brasil; ou idioma, localidade, horário. É menos usado, mas bibliotecas como **MassTransit** (pub/sub para .NET) usam bastante headers. O autor percebeu durante a gravação que **esqueceu de implementar a exchange headers no simulador** e disse que provavelmente já estaria corrigido quando o vídeo fosse publicado.

## Quem sabe usar RabbitMQ e quem perde mensagem em produção: ack

Existe um mecanismo de **ack (acknowledgment)**. Quando o consumidor consome a mensagem, ela precisa sair da fila — mas só depois de confirmada. Se o serviço cair no meio do processamento, a mensagem **volta para a fila** e continua lá, parada. Muita gente acha que isso é bug; é uma funcionalidade excelente, porque **garante que a mensagem não se perde**.

## RabbitMQ vs Kafka

Kafka também é pub/sub, mas o RabbitMQ tenta **garantir que a mensagem seja lida** e a **remove depois de lida**. O Kafka tem a intenção de **manter um histórico de eventos** que pode ser lido quando e quantas vezes você quiser.

> "RabbitMQ é tarefa; Kafka é stream de eventos." Tentar usar um no lugar do outro é pedir para arrumar problema.

## Quando usar e quando não usar

- **Use** para: desacoplar o sistema, processamento em background, lidar com erros/falhas e retentativas.
- **Não use** se o sistema é simples, tem poucos processos externos e não depende de muitos serviços de fora: nesse caso, HTTP resolve.

Fechamento: não é complicado nem "um monstro de sete cabeças"; quem entendeu Producer → Exchange → Fila → Consumer já entende melhor do que muita gente que usa em produção. O autor deixa o link do simulador na descrição (com documentação e link do GitHub, aceita sugestões e pull requests), e indica vídeos seus sobre arquitetura síncrona e sobre deploy.
