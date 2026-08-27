# CQRS — Command and Query Responsibility Segregation

Olá pessoal, tudo bem? Este é mais um vídeo da nossa série de System Design, e hoje falaremos sobre CQRS, ou Command and Query Responsibility Segregation, que se traduz para "segregação de responsabilidade entre comando e consulta". Esse padrão é muito utilizado por empresas que têm alta volumetria em suas APIs, e hoje nós vamos entender qual problema ele vem resolver e como é o desenho desse padrão.

## O problema que o CQRS resolve

Antes de entendermos todas as peças envolvidas na construção de uma arquitetura CQRS, precisamos entender qual é o problema que ele quer resolver. Esse problema passa principalmente por dois pontos centrais: **volume** (quantidade de acessos) e **modelo/assinatura**.

Num serviço normal, ou um microsserviço, temos basicamente duas operações que podem acontecer: eu posso ter **leitura**, em que leio a informação de alguma base de dados, algum data source ou de outra API, e posso ter **escrita**, em que pego uma informação e quero persistir em algum lugar.

Dependendo do tipo de software, a proporção entre leitura e escrita muda:

- Um **serviço de logs**, por exemplo, tem escrita muito maior que leitura — está o tempo todo gerando informações de logs.
- Um **sistema IoT**, um sistema embarcado que fica o tempo todo gerando informações em séries temporais (time series), também é intenso em escrita.
- Por outro lado, uma **busca textual num e-commerce** — a quantidade de pessoas buscando produtos é muito maior do que as atualizações que acontecem no descritivo do produto. Um e-commerce é um sistema muito mais intenso em leitura do que em escrita.

Essa distinção de volumetria é, na minha visão, o principal motivo que justificaria a adoção do CQRS: se eu tenho leituras e escritas em volumes muito diferentes, eu posso querer escalar de forma independente. Faz sentido separar o software em dois blocos — um bloco responsável somente pela escrita (comando) e outro responsável somente pela leitura (query).

O segundo motivo que justificaria a separação entre escrita e leitura é quando eu tenho **modelos ou assinaturas** (payload de request e response) muito diferentes. Se eu tiver um modelo de escrita muito baseado em eventos, no caso de um event sourcing, por exemplo, a fonte da verdade acaba sendo uma fila ou um tópico — e aí eu não consigo fazer agregações de forma trivial. Preciso ou consumir uma certa quantidade de informação, ou ter réplicas de leitura, que é o caso do CQRS. O CQRS também é muito utilizado em cenários em que escritas são feitas via eventos e leituras via HTTP, ou escritas via HTTP e leituras via GraphQL, para permitir mais flexibilidade.

Na minha opinião pessoal: se estou só expondo modelos diferentes e minha intensidade de escrita e leitura é parecida, o CQRS acaba sendo demais — complica porque você tem que manter dois deployments diferentes, duas bases etc. Mas em alguns cenários, quando você combina diferença de volume **e** de modelo/assinatura, aí faz bastante sentido.

## Como funciona o CQRS

Vamos pensar no seguinte cenário: um usuário acessa um frontend, que faz chamadas POST/GET/PUT/PATCH via RESTful. O **API Gateway** é o responsável por segmentar, com base na rota e no método, para qual serviço ele vai mandar a requisição.

No modelo de CQRS, eu tenho dois deployments diferentes (ou dois conjuntos de deployments — pode ser mais de um microsserviço em cada lado): um ecossistema responsável pela escrita e um ecossistema responsável pela leitura. Por isso o nome "Command and Query": tenho o comando que escreve e a query que lê.

Normalmente, no CQRS, a **fonte da verdade é onde se escreve** — o serviço de escrita é o responsável por fazer as validações, verificar que não está gerando inconsistência no estado, e garantir que o que foi escrito é verdadeiro. Um exemplo comum: base relacional na escrita e base documental na leitura.

Fluxo de atualização: frontend → API Gateway → identifica POST → redireciona para o serviço de escrita → validações → salva no banco. Fluxo de consulta: frontend → API Gateway → identifica GET → redireciona para o serviço de leitura.

Existem duas formas comuns de implementar isso:

1. **Mesmo código-fonte, deployments diferentes** — o código-fonte tem exatamente as mesmas APIs; a única coisa que muda é o tipo de deployment. Por exemplo, o serviço A é deployado 30 vezes (30 pods/máquinas) para escrita, enquanto o serviço B (mesmo código) tem só 3 réplicas para leitura. O API Gateway roteia com base no método (POST/PUT vai para um conjunto, GET vai para outro). Vantagem: única fonte de código para gerenciar, mas ainda consigo escalar de forma independente.
2. **Serviços exclusivos diferentes** — um serviço exclusivo para escrita e outro exclusivo para leitura, principalmente quando as bases de dados são diferentes ou a forma de escrita é diferente da forma de leitura (ex: escrita via eventos, leitura via GraphQL). Normalmente é o que acontece na prática, especialmente quando os serviços ganham corpo.

O CQRS não força você a ter código-fonte diferente — você pode, no mesmo código-fonte, ter deployments com réplicas ou gatilhos de escalabilidade diferentes, e isso já é suficiente para ter divisão de responsabilidade entre consulta e comando. Mas normalmente, na prática, até o código-fonte acaba sendo diferente.

## O principal desafio: sincronização

Se a base de escrita é a fonte da verdade, eu preciso sincronizar a informação entre uma base e outra. Aqui começa o desafio real do CQRS. Construir serviços/ecossistemas diferentes é tranquilo (é só duplicar o serviço e ajustar as APIs); o grande desafio é que estou escrevendo num lugar e lendo de outro, e preciso manter os dois sincronizados.

Os dois principais contras do CQRS, na minha visão:

1. Manter código e infraestrutura duplicados — um para leitura, outro para escrita.
2. O desafio de manter **consistência** entre os dados escritos e os lidos.

Existem algumas opções para garantir essa consistência, divididas em **consistência forte** e **consistência eventual**.

### Consistência forte

Não é muito comum em CQRS, mas vale conhecer as opções — às vezes a primeira etapa da migração de um serviço normal para CQRS é simplesmente fazer dois microsserviços/deployments usarem a mesma base de dados (não é recomendado em microsserviços compartilhar base, mas é uma opção na mesa).

**1. Mesma base de dados (views/materialized views)** — o comando dá um UPDATE na tabela, e a leitura faz um SELECT FROM uma view ou materialized view. É uma forma simples de conseguir um "CQRS-like service": separação entre tabelas e views. Chamo de "CQRS-like" porque ainda temos o gargalo da base — o grande trunfo do CQRS é separar volume e escalar a escrita independentemente da leitura; se ambos compartilham a mesma base, mesmo escalando muito a escrita, você acaba impactando a base e, por consequência, a leitura também.

**2. Escrita dentro da mesma transação nas duas bases** — o serviço de escrita salva na sua base e, na mesma transação (ou dá um comando), escreve também na base do serviço de leitura. Na minha opinião não faz muito sentido, porque o serviço de query acaba virando também um serviço de escrita — quebra a separação "um só escreve, o outro só consome". A vantagem que ainda existe: mesmo escrevendo no serviço de query, ele ainda tem um modelo específico para consulta. Não resolve o problema de volume/escalabilidade independente (read e write levam o mesmo impacto), mas ao menos a API de consulta tem um formato dedicado.

**3. Composição de API (API Composition)** — cenário menos comum. A escrita não escreve só na própria base: ela propaga escritas para outros serviços downstream ("em cascata"). O query service deixa de ter base de dados própria e passa a ter só um **cache**. Quando recebe uma consulta, verifica o cache; se não tiver o dado, propaga chamadas para os serviços que têm aquela informação, agrega tudo, compõe a resposta e salva no cache. Por isso "API Composition" — o query service é composto por chamadas de API, sem estado próprio; bate nas fontes de verdade, aglutina a informação, compõe um payload específico para consulta e devolve ao cliente. É parecido com o que faria um BFF (Backend for Frontend). Vantagem: tem cache e modelo específico, então ainda reduz carga e permite escalar os dois lados de forma independente (ex: aumentando o cache ou o TTL conforme cresce a leitura).

Cada uma dessas três formas resolve bem ou o problema de **volume**, ou o de **modelo**, mas não ambos: mesma base resolve bem modelo mas não volume (mesma base = mesmo gargalo).

### Consistência eventual

É onde normalmente vejo o CQRS implementado de forma plena — os times confiam na consistência eventual e em réplicas de leitura. A fonte da verdade continua sendo a base de escrita, mas a consulta se faz através de réplicas.

**1. Réplicas de banco de dados (read replicas)** — a mesma base de dados, só que com um main node (recebe o comando, controla a transação) e réplicas de leitura (acessadas pelo serviço de leitura). Bases cloud (ex: Aurora) já fazem essa sincronização automaticamente; ou pode-se construir esse cluster manualmente (ex: Postgres). O query service bate nas réplicas. O grande trunfo: separação clara entre a base que recebe carga de escrita e as que recebem carga de leitura, escalando de forma independente.

**2. Eventos (event broker)** — Kafka, RabbitMQ, Pub/Sub, SNS/SQS etc. O serviço de escrita escreve na base e posta um evento (escrita dupla — base + tópico). É preciso garantir consistência entre a base e o evento, senão gera-se uma inconsistência entre o que foi salvo e o que foi lido: o **bug da escrita dupla** (dual write problem). O query service consome o evento e atualiza sua própria base — podendo transformar a informação no formato final que quiser (ex: base relacional na escrita, Elasticsearch/Lucene/Solr na leitura, para indexação e busca semântica/facetada, que não é performática no Postgres). Essa é a abordagem que mais vejo no mercado na prática.

**3. Polling** — parecido com eventos, mas sem a camada de broker. O query service, periodicamente (via polling ou job), bate no serviço de escrita (ou em algum lugar onde o serviço de escrita depositou as mudanças, como um bucket S3 com logs/JSON) para pegar todas as transformações que aconteceram, e atualiza sua própria base. Pode ser via arquivos EDI, tabela temporária exposta via API, ou até um integrador de mercado fazendo essa ponte periodicamente.

## Resumo

No CQRS, tenho escala/modelo de dados diferentes entre escrita e leitura, e quero escalar cada lado de forma independente. Separo em ecossistemas de serviços diferentes: toda escrita vai para o ecossistema de escrita (com sua base, fonte da verdade); toda consulta vai para o ecossistema de consulta (com seu próprio modelo de dados).

Para manter consistência entre as duas bases, tenho opções de **consistência forte** (mesma base — não recomendado; transação dentro do mesmo boundary escrevendo nos dois lados — perde o trunfo de separar volume; composição de API) e de **consistência eventual** (réplicas de leitura; eventos, com atenção ao bug da escrita dupla; ou polling/job).

O CQRS adiciona bastante complexidade ao sistema: código-fonte diferente, deployments diferentes, duas coisas para monitorar, gerenciamento do API Gateway para não sobrecarregar o frontend com a responsabilidade de saber qual host chamar (recomendo deixar essa segmentação no próprio Gateway), e a responsabilidade de garantir consistência (senão a leitura mostra informação "stale", desatualizada). Em troca, resolve os problemas de escala — mais volume, possivelmente infraestrutura mais barata, porque escalando de forma independente dá para fazer um ajuste fino muito melhor na quantidade de réplicas de leitura e de escrita.

Command and Query Responsibility Segregation tem seus objetivos e sua função, mas sempre faça a pergunta: vale a pena? Como toda pergunta boa de system design.
