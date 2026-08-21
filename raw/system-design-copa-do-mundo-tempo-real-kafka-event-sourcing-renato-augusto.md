# System Design: Resultados de Jogos da Copa do Mundo em Tempo Real (Event Sourcing + Kafka)

Transcrição de vídeo (aula de system design). Falado em português do Brasil — sem necessidade de tradução.

## Introdução

No vídeo de hoje a gente vai entrar no clima da Copa do Mundo e vai arquitetar um sistema que traz os resultados dos jogos da Copa em tempo real, exatamente como aquele que você vê no Google. Vamos passar por todos os conceitos, todos os fundamentos e ferramentas. Vamos falar de event sourcing, vamos falar de mensageria com o Apache Kafka e como o Kafka funciona por baixo dos panos. Vamos fugir um pouco dessa arquitetura tradicional que geralmente a gente tá acostumado a ver nos vídeos de system design aqui do canal, e vamos projetar um dos sistemas mais desafiadores que eu já trouxe aqui para você. Então, sem mais enrolação, vamos direto pra tela, porque tem muita coisa pra gente ver e muita coisa para eu te ensinar. Bora lá.

## Requisitos Funcionais e Não Funcionais

Vamos direto ao ponto aqui, direto ao que interessa, porque como você já sabe tem muita coisa pra gente ver. A gente vai começar pelos requisitos funcionais e não funcionais, só que não vamos passar por todas aquelas etapas que a gente já tá acostumado nos vídeos de arquitetura do canal, como escolher o banco de dados, escolher as entidades, fazer o cálculo de estimativa e capacidade — tudo isso a gente vai ver ao longo do percurso conforme formos projetando a arquitetura. Daqui a gente só vai passar pelo endpoint principal da aplicação e já vamos botar a mão na massa para começar a projetar o sistema.

### Requisitos Funcionais

Tudo aquilo que a aplicação tem que ser capaz de fazer. Aqui temos dois requisitos bem simples:

1. **Resultado dos jogos**: os usuários devem ser capazes de visualizar o resultado dos jogos em tempo real e receber atualizações sem necessidade de atualizar a página ou o aplicativo. Aqui a gente vai ter que trabalhar de alguma forma para fazer com que o servidor consiga se comunicar com o front end de maneira assíncrona, sem necessidade de ficar dando F5 na página.
2. **Estatística e histórico**: os usuários devem ser capazes de visualizar dados e estatísticas completas de jogos passados, de times, campeonatos e também de jogadores específicos. Esse requisito é mais relacionado a dados históricos — por exemplo, o resultado das últimas 20 partidas, ou dos últimos 20 anos daquela seleção, daquele time ou daquele jogador.

### Requisitos Não Funcionais

Como a aplicação deve se comportar — como ela tem que conseguir realizar os requisitos funcionais:

1. O sistema deve suportar **10 milhões de usuários ativos simultaneamente** nos dias de grandes jogos.
2. O sistema deve operar em modo de **alta disponibilidade 24x7**.
3. O sistema deve ter **consistência forte** e não pode haver perda de dados (isso vai fazer sentido quando a gente falar de eventing e da timeline de eventos de todo o histórico de eventos que acontecem durante uma partida).

### Endpoint Principal

Antes de botar a mão na massa, vamos só definir um endpoint para começar. Um `GET /matchs/:id`, que recebe o ID da partida que o usuário quer acompanhar. Vão surgir outros endpoints ao longo do caminho, mas isso já é suficiente para começar. Com esse endpoint, o usuário já conseguiria fazer uma requisição do front end pro servidor, e o servidor forneceria a partida escolhida através do ID passado — acompanhando em tempo real o resultado, exatamente como o Google faz. (Exemplo demonstrado ao vivo: uma partida Iraque x Noruega no Google, mostrando placar, minuto do jogo, jogadores que marcaram os gols, atualizando sem dar refresh na página — inclusive aparecendo um gol novo durante a gravação. Geralmente aparecem também cartões amarelos, cartões vermelhos e substituições, além do placar e dos jogadores.)

## Primeiro Elemento da Arquitetura: Data Provider

O primeiro elemento da arquitetura não vai ser o front end fazendo requisição — vamos fugir um pouco do tradicional. O primeiro elemento é o **data provider**: um provedor de dados para fornecer dados em tempo real das partidas que estão acontecendo.

O que são esses data providers? Pode ser gente contratada para ficar dentro dos estádios em todos os jogos, publicando numa parte do sistema o que está acontecendo naquele exato momento (parte da própria empresa), ou pode-se consumir uma API já existente, como uma API da FIFA ou uma "Futebol API". De qualquer forma, isso é um data provider: ou a empresa cria os próprios dados/eventos (com olheiros), ou consome uma API externa.

### Exemplo de Eventos

Isso é só para exemplificar como funciona. Poderíamos ter um evento assim:

- ID da partida (Brasil x Marrocos, dia 13), time A = Brasil, time B = Marrocos, competição = Group Stage (fase de grupos).
- Tipo do evento: `match_started` — a partida começou. Esse é o primeiro evento.
- Sequência: extremamente importante para poder criar toda a timeline, porque vários eventos podem acontecer dentro do mesmo minuto. É essencial para gerenciar a linha do tempo.
- Payload: vazio nesse caso, porque a partida acabou de começar e não há informação adicional relevante.

Outro evento: um gol, no minuto 21, do Ismael Saibari (Marrocos), camisa 11, com um ID único da seleção (ex.: "MAR" — que não se repete entre seleções). O payload aqui é o gol em si. Poderia haver um cartão amarelo, com payload diferente; um escanteio aos 45+1, também com payload diferente. E assim por diante — cartão vermelho, VAR, escanteio, pênalti, falta, substituição, e uma infinidade de outros tipos de evento possíveis. Isso tudo é só exemplo, para você entender como vai funcionar a arquitetura.

## API de Ingestão (Ingest API)

Depois do data provider, precisamos pegar esses eventos criados e criar uma **API de ingestão** (ingest API) — diferente das APIs convencionais que a gente costuma criar, mas nada muito complexo; é só um conceito, uma nomenclatura.

A função da API de ingestão: receber todos os eventos publicados (via webhook, ou os próprios funcionários publicando via algum endpoint) e **modelar esses eventos para um modelo de domínio próprio** — dar vida a esses eventos de uma forma que faça sentido para o negócio. Por exemplo:

- Criar um `event_id` diferente daquele que veio (podendo armazenar o ID original como `external_event_id`).
- Criar o `match_id` da partida — extremamente importante, porque numa partida acontecem vários eventos, mas o ID da partida permanece o mesmo até o final.
- Modelar o evento à vontade, da forma que fizer sentido para o negócio, podendo adicionar mais dados.

A API de ingestão tem uma única finalidade: receber eventos externos, modelar esses eventos de forma que faça sentido para o domínio da aplicação, e depois **publicar esses eventos num tópico do Apache Kafka**, na ordem em que chegaram. (Muita coisa sobre Kafka será explicada mais à frente — o que são os offsets, o que é um tópico, e por que isso não é uma fila convencional como RabbitMQ ou SQS. Por hora, basta imaginar isso como uma fila.)

## Consumer e Banco de Dados

Depois que o evento vai para um tópico do Kafka, precisamos de um **consumer** para pegar esses eventos e processá-los com alguma regra de negócio. Nesse primeiro momento, o consumer pode simplesmente pegar os eventos e armazená-los num banco de dados — a escolha aqui é **PostgreSQL**.

Sobre lidar com JSON dinâmico: o Postgres também consegue lidar com JSON — é uma das funcionalidades dele. Exemplo:

```sql
INSERT INTO matchs (id, data)
VALUES ('<match-id>', '{...}'::jsonb);
```

Não há motivo para escolher um banco não-relacional aqui, até porque há a questão dos IDs e relacionamentos (explicado a seguir) que fazem mais sentido num banco relacional.

O evento completo (com ID da partida, ID do evento, etc.) é separado em uma tabela `match_events` — os eventos de uma partida — relacionada por `match_id` com a tabela `matchs` (a partida em si). Uma partida pode ter vários eventos; um evento específico só pode pertencer a uma partida (relacionamento um-para-muitos).

## Servidor Web (primeira versão, ainda sem funcionar bem)

O próximo elemento é o **servidor web**, que responde as requisições do front end. Nessa primeira versão, ele consulta diretamente o banco de dados. O front end faz `GET /matchs/:id`, o servidor consulta o banco:

```sql
SELECT *
FROM match_events
WHERE match_id = '<id>'
ORDER BY sequence;
```

O resultado é uma lista de eventos ordenados por sequência, cada um com `event_id`, `match_id`, tipo do evento, sequência, payload (em JSON) e outros dados como `received_at` (hora que o evento foi recebido).

## O Conceito de Event Sourcing

Preste atenção nessa sequência de eventos: isso é o que a gente chama de **event sourcing**. O placar de uma partida — por exemplo, "2 a 1" — **não existe** dentro do sistema como um dado armazenado. Não há uma tabelinha "resultado da partida" com "2 a 1" sendo atualizada — isso não faz sentido nesse tipo de arquitetura (embora mais adiante a gente vá fazer algo parecido, mas com finalidade completamente diferente).

O conceito nasce de ter uma **linha de eventos que levaram a um resultado específico**. Se processarmos os eventos em ordem, sabemos que no minuto 21 saiu o primeiro gol, no minuto 37 saiu o segundo, no minuto 90 acabou a partida, e conseguimos **projetar** o resultado (1 a 1, por exemplo). Isso é o conceito filosófico de event sourcing: uma linha do tempo, diferente das arquiteturas tradicionais que consultam o banco e montam uma tabelinha específica. Essa linha do tempo começa no Apache Kafka — todo evento chega na ordem, e é por isso que se trabalha com aquela sequência.

### Isso ainda não resolve o problema

Essa primeira versão da arquitetura tem vários problemas:

1. **Recalcular a timeline a cada requisição.** Toda vez que chega uma requisição, o servidor tem que consultar o banco e recalcular toda a linha do tempo para chegar de novo no resultado — buscar todos os gols, ordenar, interpretar o payload, somar gol por time, considerar gol anulado pelo VAR, e só então montar o placar. Isso não é trivial, e estamos falando de 10 milhões de usuários fazendo requisições — ou seja, 10 milhões de consultas batendo no Postgres para remontar a timeline. Isso derrubaria o servidor ou o banco de dados.
2. **O cliente tem que ficar atualizando a página.** Os dados retornados são estáticos; não há atualização automática. Isso não dá para resolver com HTTP convencional (pelo menos não do jeito comum) — precisa de outra abordagem, e não faz sentido ficar batendo no banco o tempo todo.
3. **Falta de alta disponibilidade.** Se a API de ingestão cair, toda a arquitetura para: param de chegar eventos na fila, no consumer, no banco, e os dados não são mais atualizados. Se qualquer elemento cair (Kafka, consumer, banco, servidor web), toda a arquitetura cai. Precisamos de alta disponibilidade.
4. **O volume de usuários vai travar o servidor e o banco.**
5. **Novo requisito da empresa**: atender todos os campeonatos ao redor do mundo — Champions League, Premier League, Bundesliga, Brasileirão, Libertadores, Super Mundial de Clubes, Liga de Portugal, SPL (Liga Saudita), Euro, Copa América, La Liga, Copa do Brasil, e por aí vai (isso é só uma fração do que existiria na prática — centenas de campeonatos). Ou seja, muitos eventos chegando a todo momento, de fusos horários diferentes, partidas acontecendo em todo canto do mundo o tempo todo, inclusive quando você está dormindo. (Esse requisito foi adicionado deliberadamente para aprofundar a arquitetura, em vez de pensar só no cenário simplificado de Copa do Mundo.)

## Alta Disponibilidade: Escalabilidade Horizontal

O primeiro problema a resolver é a alta disponibilidade, através de **escalabilidade horizontal**. Começamos escalando horizontalmente a API de ingestão.

Ponto importante: muita gente acredita que escalar horizontalmente é só para lidar com altas volumetrias — mas não é sempre o caso. Os data providers não vão produzir milhões de eventos por segundo; na pior das hipóteses, centenas ou milhares, não milhões. Um servidor só já seria suficiente para o volume. Mas como precisamos de alta disponibilidade — sem perda de dados, sem servidor fora do ar — precisamos de **redundância**. Ou seja: escalamos horizontalmente não só para volumetria, mas também para ter segurança/redundância.

Colocamos um **load balancer** na ponta, recebendo todas as requisições e repassando para três instâncias da API de ingestão. Também podemos escalar os consumers: de um consumer para dois consumers. É aqui que começa o problema mais interessante, e onde a arquitetura ganha muito mais profundidade — fundamentos do Kafka.

## Kafka: Tópicos Não São Filas Convencionais

Numa fila convencional (ex.: fila de banco), você chega, é atendido, e sai da fila — todo elemento que chega é consumido e sai. No Kafka, os eventos podem ser **persistidos** — cada evento é armazenado dentro de um **offset** (uma "caixinha": offset 0, 1, 2, 3...). Isso é o que permite trabalhar com event sourcing / fonte de eventos: os eventos ficam armazenados pelo tempo que você determinar, e mesmo que um consumer consuma um dado, ele não sai da fila (a não ser que se configure isso).

### Por que armazenar os eventos: Event Replay

Pensa num exemplo diferente (não futebol): um sistema de operações financeiras, processando valores/pagamentos. Imagine que, alguns meses depois, se descobre um bug na forma como os valores eram calculados (ex.: usar `float` para representar dinheiro, o que nunca deve ser feito — descontando centavos a mais). Ao trabalhar com event sourcing / armazenamento da cronologia de eventos, é possível criar um consumer do zero, com uma regra de negócio nova que resolve o bug, e colocá-lo para processar **desde o primeiro evento**. Essa técnica se chama **event replay**: voltar ao começo da linha temporal e reprocessar um a um, na ordem cronológica em que aconteceram. É assim que se trabalha com esse tipo de arquitetura.

## Consumer Groups

Voltando à alta disponibilidade dos consumers: numa fila convencional, você chega, é atendido, vai embora, e vem o próximo. No Kafka, os eventos são armazenados — não vão embora. O que acontece se criarmos uma réplica do consumer e colocá-la para processar junto com a que já existia?

O Kafka vai pegar o evento (ex.: gol do Marrocos) e **entregar para os dois consumers** (broadcast) — porque nada os diferencia. Se os dois processarem e ambos gravarem no banco, teríamos **dois gols do Marrocos duplicados**, sendo que só houve um. Esse é o problema de trabalhar com múltiplos consumers "soltos" no Kafka.

A solução é o **consumer group**: um grupo de consumers identificado por um `group_id` (ex.: `"event-service"`). Exemplo de código:

```js
const kafka = new Kafka({ clientId: 'consumer-1', brokers: ['...'] });
const consumer = kafka.consumer({ groupId: 'event-service' });

await consumer.connect();
await consumer.subscribe({ topic: 'match-events' });

await consumer.run({
  eachMessage: async ({ message }) => {
    // conectar no banco e salvar a mensagem
  },
});
```

Todos os consumers com o mesmo `group_id` participam do mesmo grupo. Dentro de um consumer group, o Kafka só entrega uma mensagem/evento para **um único consumer** do grupo — justamente para evitar duplicatas, já que a linha temporal precisa ser preservada (não pode haver perda nem duplicidade de dados). O Kafka é referência em lidar com isso, cuidando com maestria dessa questão da linha temporal.

### Offset Commit e Por Que o Segundo Consumer Fica Parado

Um exemplo do fluxo: o Kafka entrega o primeiro evento pro consumer 1, depois o segundo evento (mesma partida) também pro consumer 1, depois um terceiro evento (decisão do VAR, gol cancelado) também pro consumer 1. O consumer 2 fica parado — porque o Kafka funciona diferente do RabbitMQ/SQS, onde você simplesmente sobe vários consumers e o processamento vai sendo paralelizado, cada um pegando uma mensagem.

Isso é uma forma de o Kafka preservar a linha temporal. Se o Kafka entregasse o primeiro evento pro consumer 1 e, ao mesmo tempo, o segundo evento pro consumer 2 (que grava no banco que houve um gol), e depois entregasse o terceiro evento (decisão do VAR cancelando o gol) pro consumer 1 — e esse consumer morresse enquanto processava — essa mensagem seria **perdida para sempre**.

A solução do Kafka: ele só entrega a próxima mensagem depois que o consumer **comitar** (offset commit). O consumer pega o evento, processa (salva no banco, etc.), e depois avisa o Kafka: "esse evento que estava no offset zero eu já processei, me entrega o próximo". Por isso o Kafka não entrega o segundo evento enquanto não tem certeza de que o primeiro foi processado — sem isso, não há como garantir consistência dessa forma.

Muita gente não sabe disso — é fundamento do Kafka. Acaba colocando dois, três, quatro consumers e, no final das contas, só um está de fato trabalhando.

## Partições

Como então conseguir paralelismo real? A resposta é: **partições**. Uma partição é uma subdivisão de um tópico. Para trabalhar com dois consumers, é preciso ter duas partições; com três consumers, três partições; e assim por diante.

### Fluxo completo

1. O data provider produz o dado, que bate no load balancer.
2. O load balancer repassa para as instâncias da API de ingestão.
3. A API de ingestão modela o evento no domínio. A entidade `match` tem um `match_id` **único** — extremamente importante.
4. A API de ingestão produz (`send`) o evento para o tópico `match-events`, usando como **chave de partição** (`key`) o `match_id`. O valor (`value`) é o evento em si.

```js
const kafka = new Kafka({ clientId: 'ingest-api', brokers: ['...'] });
const producer = kafka.producer();
await producer.connect();

await producer.send({
  topic: 'match-events',
  messages: [
    { key: event.match.id, value: JSON.stringify(event) },
  ],
});
```

A chave de partição (`key`) é algo extremamente importante — quem já viu vídeos de banco de dados sobre escalabilidade sabe disso.

### Como o Kafka decide a partição: Murmur Hash

Por baixo dos panos, o Kafka usa o algoritmo **Murmur** (murmur hash). Ele pega o `match_id` (string alfanumérica), aplica o algoritmo de hashing, e transforma isso em um número. A mesma entrada sempre gera a mesma saída.

Depois, exatamente como os bancos de dados fazem para definir partição em escalabilidade horizontal, ele calcula o **módulo** desse número pelo número de partições (`hash % número_de_partições`) — encontrando o resto da divisão. Com duas partições, o resto é 0 ou 1; com três partições, seria 0, 1 ou 2; e assim por diante.

Como o `match_id` pertence a uma partida específica, **todo evento daquela partida vai sempre para a mesma partição** — preservando a ordem/linha temporal por partida.

Exemplo: se Alemanha x Curaçao e Brasil x Marrocos estão acontecendo ao mesmo tempo, o evento de Brasil x Marrocos pode ir para a partição 0, e o de Alemanha x Curaçao para a partição 1. Uma partição só pode pertencer a um consumer (dentro do consumer group) — é assim que se preserva a linha temporal por partida, mesmo com múltiplos consumers processando em paralelo. Continua sendo o mesmo tópico — é como se fosse a mesma fila, só que com "caixas de atendimento" diferentes (partições).

### Criando um tópico com partições (exemplo de CLI)

```bash
kafka-topics.sh --create \
  --topic match-events \
  --partitions 2 \
  --bootstrap-server localhost:9092
```

Isso já diz ao Kafka: "eu vou ter dois consumers". Com intenção de três, quatro consumers, cria-se com três, quatro partições, e assim por diante.

### Rebalanceamento

Se um consumer cair, o Kafka faz o que se chama de **rebalance**: as partições do consumer que caiu são reatribuídas para os consumers restantes. Não há problema em um único consumer ter várias partições — se ele estiver sozinho, o Kafka distribui todas as partições para ele. O que não pode acontecer é uma partição ser consumida por **dois consumers diferentes** ao mesmo tempo (dentro do mesmo consumer group).

## Score Service: Cache com Redis

Depois de resolver escala/disponibilidade com partições, falta resolver o problema de servir os dados sem recalcular a timeline a cada requisição. Não faz sentido o servidor web consultar o banco de dados e remontar toda a linha do tempo a cada requisição. É preciso ter algum lugar rápido, objetivo, já calculado.

Cria-se um **outro grupo de consumers**, chamado `score-service`. Esses consumers pegam as mensagens do tópico e ignoram todos os tipos de evento, exceto: gol, substituição e cartão amarelo/vermelho — que é justamente o que aparece no Google. Não há necessidade de recalcular a linha do tempo inteira — quando chega um evento de gol daquela partida específica, o consumer armazena isso no **Redis**:

```
match_id: <id>
status: live
minute: 67
score: { time_a: 2, time_b: 1 }
goals: [{ player: "Vinícius Júnior", minute: 37, team: "Brasil" }, ...]
cards: [...]
```

Isso já é suficiente para abastecer um front end simples, tipo o do Google — sem precisar de todas as estatísticas com profundidade, apenas o placar já calculado. Ao chegar um evento de gol, o consumer vai no Redis, monta o payload inteiro e armazena. Quando chega o próximo evento (ex.: cartão amarelo), busca o dado do Redis, atualiza, e salva de novo. Isso roda em memória — muito mais rápido do que ir ao banco de dados remontar toda a timeline.

O servidor web agora pode simplesmente se conectar a esse Redis para consultar os dados já montados, em vez de esperar o banco remontar tudo. Conforme os eventos chegam, o `score-service` calcula e atualiza o Redis; quando a requisição chega ao servidor web, ele consulta o Redis e retorna ao front end.

## Tempo Real: SSE e Redis Pub/Sub

Isso ainda não resolve o problema do tempo real — o cliente ainda precisaria dar F5 e consultar o Redis de novo. A solução:

1. **Primeira requisição** (o usuário acabou de entrar na página/app): o servidor consulta o Redis, retorna os dados, o front end renderiza. Fim dessa requisição.
2. O front end, em seguida, abre uma **conexão HTTP que nunca fecha** — o que se chama de **SSE (Server-Sent Events)**.

Para viabilizar isso, entra mais um elemento na arquitetura: o **Redis Pub/Sub** — uma fila de mensageria simples. O mesmo dado que foi armazenado no Redis (cache em memória) pode ser replicado e publicado no Redis Pub/Sub, marcado com o `match_id` como canal/chave. Todo mundo conectado e "ouvindo" esse canal específico recebe a mensagem — o próprio Redis entrega. O servidor web se conecta ao Redis e fica inscrito (`SUBSCRIBE`) nesse canal específico do ID que o usuário está solicitando no endpoint.

### Código do Front End (exemplo)

```js
// primeira requisição
const res = await fetch(`/matchs/${matchId}`);
const data = await res.json();
renderMatch(data);

// conexão SSE
const es = new EventSource(`/matchs/${matchId}/stream`);
es.onmessage = (e) => applyUpdate(JSON.parse(e.data));
```

### Código do Servidor (endpoint SSE, exemplo)

```js
app.get('/matchs/:id/stream', (req, res) => {
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Connection', 'keep-alive');
  // manter a conexão viva (keep-alive) e se inscrever no canal do Redis Pub/Sub
  // referente a req.params.id; a cada mensagem recebida, escrever no response
});
```

O `Content-Type: text/event-stream` é o que caracteriza o stream de eventos, e o keep-alive é o que segura a conexão HTTP aberta indefinidamente. O servidor busca do Redis (cache) na primeira requisição normal, fecha essa conexão; em seguida o front end abre a conexão SSE, e o servidor se inscreve no Redis Pub/Sub no canal daquele `match_id`. Toda vez que chega um evento novo, o `score-service` atualiza o Redis (cache) — para as próximas primeiras requisições de novos usuários — e também publica o mesmo dado no Redis Pub/Sub, que por sua vez notifica os servidores inscritos, que repassam a atualização para os clientes conectados via SSE. O front end aplica as atualizações indefinidamente.

### Como o Servidor Sabe Para Quem Enviar Cada Mensagem

Com 10 milhões de usuários conectados, como o servidor sabe qual conexão SSE pertence a qual partida? Através de um **mapeamento em memória**: para cada conexão, associa-se o `match_id` de interesse.

```
{
  "<match_id_1>": [conexao_A, conexao_B, conexao_C],
  "<match_id_2>": [conexao_D, conexao_E]
}
```

Quando chega uma mensagem no Redis Pub/Sub com um determinado `match_id`, o servidor consulta esse mapa em memória, encontra todas as conexões SSE abertas interessadas naquele ID, e envia a atualização para todas elas de uma vez.

## Endpoints de Histórico e Estatística

Voltando ao segundo requisito funcional (histórico e estatísticas): endpoints como:

- `GET /matchs/:id/stats` — estatísticas de uma partida específica.
- `GET /teams/:id/history` — histórico de um time (ex.: últimos 10, 20 anos).
- `GET /players/:id` — dados de um jogador específico.

Esses endpoints não atendem os 10 milhões de usuários simultâneos em tempo real — são para usuários que clicaram para ver histórico. Aqui, faz sentido consultar o banco de dados diretamente, montar a linha temporal completa (event sourcing "puro", sem necessidade de cache/tempo real) e entregar ao usuário interessado.

## Escalabilidade Final

Por fim, escalar horizontalmente também o Redis (por questões de redundância — um cluster, ficando o código agnóstico da topologia, só conectando no cluster) e o banco de dados (réplicas de leitura, para redundância e não ter perda de dados / falta de disponibilidade). Poderíamos também colocar um load balancer na ponta desses componentes, mas isso já é assunto batido no canal (vídeo anterior sobre load balancer).

Essa é a arquitetura final: data provider → load balancer → API de ingestão (múltiplas instâncias) → tópico Kafka particionado (`match-events`) → dois consumer groups (persistência no Postgres; `score-service` no Redis) → Redis Pub/Sub → servidor web com conexões SSE mapeadas em memória → front end.

## Encerramento

O vídeo menciona, como material relacionado do mesmo autor/canal: um vídeo anterior sobre load balancer, um vídeo sobre Redis, e o produto "Mapa do Arquiteto" — um guia de carreira/mentoria para conduzir do zero até arquiteto de software e arquiteto de soluções, com roadmap de estudos.
