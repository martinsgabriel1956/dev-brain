# Pub/Sub, Message Queue e BullMQ na Prática

Presta atenção: hoje vamos falar sobre três conceitos importantíssimos aqui — na verdade dois conceitos e uma aplicação na prática. Um dos conceitos é **Pub/Sub**, ou seja, publisher/subscriber. O outro conceito é **message queue** — filas de mensagem, mensageria. E o terceiro é o **BullMQ**, que a gente vai ver na prática, no código mesmo, como implementar uma message queue. Vou te mostrar aqui o codezinho, mostrar que não é um bicho de sete cabeças, para você entender como é que funciona, ver um pouco de código, ver um pouco da teoria, entender e ver onde isso pode fazer sentido na sua vida, nas aplicações que você trabalha, tá bom.

*(Bloco de patrocínio omitido — ferramenta de IA não relacionada ao conteúdo técnico do vídeo.)*

## Pub/Sub vs. Message Queue: a confusão comum

Primeira coisa: a gente pode ignorar o BullMQ por enquanto, porque o BullMQ é uma ferramenta — vou falar sobre essa ferramenta durante a implementação das nossas message queues. Eu quero te contar o que é Pub/Sub e o que são message queues. Existe uma certa confusão aqui — eu já confundi isso algumas vezes — que é o seguinte:

**Pub/Sub é publisher/subscriber.** Alguém publica e outras pessoas estão inscritas. O modelo mental disso é o modelo mental do YouTube: eu tô publicando um vídeo, vocês estão inscritos, vocês podem assistir esse vídeo ou não.

**Message queue** é uma fila de mensagens que a gente geralmente usa para atribuir unidades de trabalho para workers, para consumidores.

### Qual é a diferença na prática?

**Pub/Sub: eu tô dizendo algo que aconteceu, eu não tô mandando ninguém fazer nada.**

Imagina que você tem um sistema que processa pagamentos. Ao processar um pagamento, eu vou publicar um evento — imagina um JSON: `{ type: "payment_succeeded", id: 123 }`. Publiquei esse evento, joguei ele no ar. Você pode ter sistemas que se inscrevem para ouvir esse evento: meu sistema de estoque ouvindo o evento de pagamento, meu sistema de entregas ouvindo esse evento de pagamento, meu sistema de analytics ouvindo essa publicação. Esses três sistemas podem estar ouvindo a publicação desse evento e podem fazer algo ou não.

Isso é diferente de um comando. Seria outra coisa se o meu sistema de pagamentos apontasse diretamente pro meu sistema de entregas e mandasse uma ordem direta: "sistema de entregas, você precisa fazer essa entrega aqui". Esse é o modelo mental de publisher/subscriber — uma terminologia que a gente usa para dizer que algo foi feito, e existe uma espécie de ramificação a partir dali.

**Message queue: você publica um trabalho a ser feito.**

Exemplo muito comum de message queue que eu utilizo bastante: fazer compressão ou mudar tamanho de imagens. No JSON, a gente pode ter um job `compress_image`, que vai receber a URL da imagem, o nome da imagem, outros metadados. Alguém vai produzir esse job — imagina quando o usuário faz upload dessa imagem pro meu serviço. Meu serviço vai criar esse job e jogar ele numa fila — uma fila de vários jobs. Em algum momento, esse job vai ser consumido pelo meu worker, que vai executar essa tarefa: comprimir a imagem, armazenar em algum lugar, fazer alguma outra coisa com essa informação.

### A distinção do modelo mental

No Pub/Sub eu estou publicando um fato, publicando algo que aconteceu — como se eu tivesse publicando no jornal: "pagamento foi feito com sucesso", publiquei. Se tiver muita gente ouvindo ou se não tiver ninguém ouvindo, eu não ligo muito — o fato tá publicado. Cada subscriber vai receber uma cópia dessa mensagem, vai ser informado uma vez que essa mensagem aconteceu (ou pode ser informado várias vezes, dependendo de como a gente monta o sistema — depende se a gente vai entregar at-least-once, at-most-once ou exactly-once, os padrões de entrega de mensagem).

Já o modelo mental de uma message queue: "você entregou a mensagem, acabou, fechou". Eu publiquei um trabalho, eu tô esperando alguém pegar e executar esse trabalho, para tirar esse trabalho da fila. Você pode ter mais de um worker — 20, 50, 1000 workers, todos podem estar ouvindo essa mesma fila. Mas a ideia é você não ter diversos workers processando o mesmo job. Não faz sentido eu comprimir a mesma imagem três vezes em três workers diferentes — eu quero comprimir ela só uma vez.

### Inversão de dependência

É quase como uma inversão de dependência. Numa message queue, o meu serviço precisa que algo seja executado — quem depende de quem é o meu serviço; meu serviço depende de quem consome a mensagem. No Pub/Sub é meio o inverso: o meu sistema de pagamentos não depende de ninguém, ele tá publicando a mensagem pros outros reagirem. Quem depende, na verdade, é o meu sistema de estoque, que tá mais dependente dessa mensagem chegar.

### Usando os dois juntos

Também é comum usar ambos. Por exemplo: nosso pagamento foi um sucesso. Geralmente, quando um pagamento é sucesso, o cliente recebe um e-mail. Esse serviço de e-mail pode ouvir ativamente esse evento — a mensagem vai chegar no meu sistema de e-mail pelo menos uma vez (ou múltiplas vezes), e depois eu vou jogar isso numa fila. Essa fila vai garantir que o e-mail é enviado pelo menos uma vez (ou apenas uma vez), e aí eu ponho um worker para enviar o e-mail.

Às vezes a gente fala desses tópicos e vocês acabam achando que são coisas de outro planeta, muito complexas — mas não necessariamente são. Você nem precisa de infraestrutura diferente para rodar isso.

## Como isso aparece no mundo real

No mundo real: você tem um **service** — pode ser uma máquina, um servidor, uma VPS (por exemplo, da HostGator, parceira do canal). E algum tipo de sistema de entrega de mensagens — você poderia usar, por exemplo, o Simple Queue Service da Amazon (AWS SQS). Os workers podem ser outros servidores em VPS, podem ser lambdas, pode ser o que você quiser. Geralmente são três pedaços de infraestrutura diferentes.

Mas na prática, agora, a gente vai rodar esses três dentro da própria máquina. O que eu vou te mostrar não vai ser um sistema Pub/Sub — vamos mostrar uma **message queue**. O interessante é que tudo isso vai estar rodando dentro do meu próprio PC, usando Node — na verdade vamos usar Bun.

## BullMQ na prática

BullMQ é uma lib, um sistema de filas construído em cima do Redis. Você instala o BullMQ, cria uma queue, adiciona jobs para essa queue, adiciona workers, e depois processa isso.

### Estrutura do exemplo

Repositório simples com dois arquivos: um de **producer** e um de **worker** — duas aplicações diferentes, rodando como dois processos de Bun distintos. Eles não se comunicam por chamada de função direta; a comunicação acontece através da fila.

O pedaço crítico de infraestrutura: um Redis rodando dentro do Docker (Redis dockerizado), porque o BullMQ é construído em cima da tecnologia do Redis. Tanto o producer quanto o worker se conectam nesse mesmo host de Redis, na mesma porta — isso é muito importante, senão não funciona.

### O producer

Uma lista de e-mails. Do BullMQ importamos uma `Queue` e a inicializamos. No exemplo, criamos um job de envio de e-mail: imagine que o usuário criou uma conta, e o serviço principal precisa informar "você precisa enviar um e-mail falando que a criação de conta deu certo". O worker vai ser responsável por enviar esse e-mail, para desafogar o serviço principal — ele não precisa lidar com conexões, envio de e-mail, APIs de terceiros. Isso desacopla e permite escalar de maneiras diferentes — uma técnica bem bacana.

O producer usa um `setInterval` que, a cada 1 segundo, adiciona um e-mail na fila. A cada segundo ele vai enfileirando mais um e-mail. É só isso que essa parte faz.

### O worker

Também conectado no mesmo Redis. Tem o nome do job (`My Job Name`, conforme a documentação) e o nome da fila. O worker é criado em cima da mesma fila. A cada 500ms (meio segundo), ele processa um job e, no exemplo, só dá um `console.log` dizendo que o e-mail foi enviado com sucesso.

A partir daí, é código — você pode fazer o que quiser: chamar uma função, chamar uma API externa, integrar com um serviço tipo Resend.

### Rodando o exemplo

Com o Docker do Redis rodando (Redis Alpine, sem problema nenhum), roda-se `bun run producer` — ele começa a criar jobs e adicionar na fila, que vai enchendo. Depois `bun run worker` — o worker se conecta no mesmo Redis e começa a ler os jobs, a cada meio segundo, processando `email 3`, `email 4`, `email 5`, etc., na ordem em que foram enfileirados.

Se você remove o worker, não tem problema — ele volta depois e continua de onde parou. Se você para o producer, o worker vai processar todos os jobs que já estão na fila e esperar. Quando o producer volta a rodar, o worker continua consumindo a partir do próximo job (por exemplo, retomando do job 84, 85, e assim por diante).

Esse é basicamente o quickstart oficial do BullMQ — o exemplo mais simples possível. A ideia não era fazer nada demais, mas desmistificar a complexidade desses tópicos. Muitas vezes, quando a gente fala de system design, de sistemas mais complexos, dá a entender que é algo de outro mundo — mas as coisas não são tão complexas assim.

*(Bloco final sobre divulgação de curso de system design do canal, omitido — não é conteúdo técnico central do vídeo.)*
