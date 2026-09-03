# Três Tipos de Módulos numa Arquitetura de Monolito Modular — Valdemar Neto

E aí, hoje eu vou te mostrar os três tipos de módulos mais comuns numa arquitetura de monolito modular. Um deles eu não uso bastante, eu vou explicar por quê. Eu também vou mostrar design de código: como o design de código de uma arquitetura modular se encaixa com padrões de arquitetura como Clean Architecture, e como uma arquitetura modular leva o potencial de qualquer arquitetura, e como tem uma camada a mais que é adicionada por causa da modularização. Então a gente vai entender como arquiteturas tradicionais interagem com arquiteturas modulares, e vocês vão poder aplicar isso no dia a dia de vocês.

Eu sou Valdemar Neto, eu falo sobre conteúdos avançados sobre liderança e desenvolvimento de software. Então se tu não me segue ainda, me segue aí, comenta no vídeo se tiver qualquer dúvida — as dúvidas são úteis para todo mundo nos comentários, eu vou responder todas elas.

## Onde a Arquitetura Modular se Encaixa

Para a gente começar, tem que entender que dois padrões de arquitetura são bem famosos em arquiteturas maiores, arquiteturas enterprise: Hexagonal Architecture e Clean Architecture. Antes disso a gente tem o MVC, arquiteturas mais simples, mas a maioria das pessoas que constrói alguma aplicação de grande porte para grandes empresas segue ou Hexagonal Architecture ou Clean Architecture — normalmente é uma dessas duas. Também tem, como eu falei, o MVC, ainda bem usado em aplicações menores, e tem padrões como Vertical Slice, que algumas pessoas testam, outras não — mas eu vou focar nessas duas.

O que essas arquiteturas têm em comum? Elas têm foco em separação do domínio. No meio a gente tem lógica de negócio, domínio — na Clean Architecture tem Use Case, Entidades. Pensem nisso como a parte de domínio, a parte onde a tua lógica de negócio interage com o mundo externo e com lógica específica do teu negócio. Nas entidades, no Clean Architecture ou no Hexagonal, pode ser no teu Domain Model, pode ter entidades, pode não ter, pode ser um Domain Service, algo do tipo — mas pensem que a tua lógica de negócio tá no meio da tua arquitetura. Tu recebe coisas de fora através de controllers, do que for, através de repositórios de banco de dados, e tu trata isso no meio da tua arquitetura.

Por que que arquiteturas modulares puxam esses limites um pouco mais? Porque, por mais que o Domain-Driven Design fale de Shared Kernel e tal, não se fala muito sobre reuso de infraestrutura, e não se fala muito sobre como separar as coisas para rodar elas separadas — esse módulo vai rodar no processo X, aquele módulo vai rodar no processo Y. Não se fala muito nisso nesse tipo de arquitetura, porque a gente foi de monolitos tradicionais para arquiteturas como microsserviço, onde para esse tipo de arquitetura em si nada mudou: elas ainda ficavam num codebase singular basicamente. Um estava num monolito grandão, onde tu tinha que focar muito em abstração para poder reusar código e não ser muito impactado por mudanças; o microsserviço era muito mais simples, codebase muito menor, mas ainda assim um codebase singular. Com arquiteturas modulares a gente passa um nível adiante: a gente tem o mesmo codebase separado por módulos. Isso é o que muda.

## Como Estruturo o Código Hoje

Como eu vejo a arquitetura, o design de código interno, nos dias de hoje eu ainda sigo muito os princípios dessas arquiteturas — Clean e Hexagonal. Claro que eu vou evoluindo a aplicação até que ela chegue em coisas mais complexas, mas eu sigo alguns princípios que eu quero mostrar aqui: como eu estruturo mais ou menos, e como eu vejo as aplicações nos dias de hoje.

A gente tem a **lógica de negócio** — Business Logic seria o centro das duas arquiteturas, eu chamo de **Core**. Aí tu tem services, se tiver entidades elas vão estar lá, tu tem use cases também, pode ficar aqui.

Depois tu tem a parte que eu chamo de **Supporting Infrastructure** — ou Adapters, ou Gateways, do Clean Architecture, para quem conhece. Pensem que é a coisa que interage com tua lógica de negócio: controllers, GraphQL resolvers, clients para APIs externas, repositórios para banco de dados. Por que essa camada é interessante? Porque ela ainda tem conhecimento específico do contexto em que está — um `IdentityController`, `UserController`, é específico de algo, não é totalmente genérico. A gente fala "infraestrutura" e tal, e eu concordo com a parte de infraestrutura, mas é uma infraestrutura que tem conhecimento do contexto em que está — então ela não é totalmente compartilhável.

Depois a gente tem coisas que são **infraestrutura pura**: lib de database, log, monitoring, config. Essas coisas podem ser simplesmente pegas daqui e movidas para outro lugar — e isso é fundamental para uma arquitetura modular que precisa ser reusável.

Agora vou mostrar no código o que eu falei, para vocês entenderem melhor. E agora vou falar dos três tipos de módulos mais comuns numa arquitetura modular.

## Os Três Tipos de Módulos

Esse código faz parte do meu curso dentro da Tech Leads Club, chamado "Aplicações Enterprise". Não é um curso aberto, porque é um curso avançado, bem nichado para quem já tá nesse nível — mas quem tiver interesse, entra lá. Eu obviamente vou seguir trazendo conteúdo aberto aqui sobre o curso, mas o código completo é lá; qualquer coisa que quiserem perguntar eu vou compartilhando.

No codebase, é um serviço de streaming — o "Fake Flix", como a gente chama lá — usando NestJS. Mas vocês podem seguir isso com Go, com qualquer stack, com módulos no Java, qualquer coisa que tenha módulo vai seguir de forma similar. A gente tem a pasta `source`, tem `modules` e `shared` — aqui já começa a aparecer a importância de coisas compartilhadas.

### 1. Módulos de Domínio

Primeiro e mais importante tipo de módulo numa arquitetura modular: **módulos de domínio**. Eles são abrangentes — como um microsserviço, ou até maior que um microsserviço. No exemplo: `billing` (toda a parte de cobrança de um serviço de streaming), `content` (toda a parte de conteúdo — indexar conteúdo, fazer streaming de conteúdo; dentro dele tem coisas como recomendação, distribuição de conteúdo, e várias outras), `identity` (autenticação e autorização, `user management`). Se tu olhar esse codebase, já sabe: isso aqui são módulos de domínio. A ideia é que esses módulos possam rodar juntos ou também rodar separados, quando estiverem na infraestrutura — AWS, contêineres, o que for.

### 2. Módulos de Infraestrutura Pura

O segundo tipo — e o mais importante depois dos módulos de domínio — são os **módulos de infraestrutura pura**. Lembra que eu mostrei a infraestrutura pura? São esses módulos: módulo de HTTP, módulo de logger, módulo de persistência. A infraestrutura pura de um ORM, por exemplo, é só o setup daquele ORM basicamente, que tu pode pegar e plugar em qualquer outro módulo. Se eu for no meu módulo de `content`, dentro de `persistence`, eu vou estar usando aquele outro módulo — o `DynamoDB persistence module`, ou o `TypeORM persistence module`.

O que acontece aqui: a gente tem módulos de infraestrutura pura compartilhados, que podem ser facilmente compartilhados entre módulos de domínio. Isso te permite reuso, escala, e permite deixar os módulos de domínio focados em coisas de domínio. Se a gente voltar para o módulo de domínio — lembra que eu falei de Supporting Infrastructure — toda a parte HTTP fica dentro do módulo de domínio, a parte de repositório fica dentro do módulo de domínio. Dessa maneira a gente tem essa separação.

### 3. Módulos de Feature

O terceiro tipo de módulo — que é o que eu não gosto muito, que algumas pessoas usam mas eu particularmente não uso bastante, e vou explicar por quê — são os **módulos de feature**. São módulos mais granulares que módulo de domínio: tu pega um domínio e quebra ele em funcionalidades.

Na teoria, se a gente olhar um repositório como o "Ultimate NestJS" — que eu achei como exemplo, um repositório que mostra exemplos de código do NestJS, não é código de produção — dentro de `modules` ele tem módulos granulares como `category`, `auth`, `chat`, `health`.

Qual o problema de módulos puramente de feature? Tu não sabe o contexto deles. Numa aplicação real de monolito modular, tu vai ter vários bounded contexts do teu Domain-Driven Design estratégico, e você tem que mapear isso pro código de alguma maneira. Dessa forma tu não sabe: tipo, `auth` é do quê? Ah, tu vai reusar... mas tem `category`, mais `category` do que quê? Ele acaba sendo granular demais. E outra coisa: compartilhar coisa entre módulos de feature acaba sendo complexo e acaba acoplando eles demais — pô, tem uma entidade, como é que tu compartilha essa entidade entre módulos de feature? Acaba ficando uma abstração desnecessária na maioria dos casos.

Claro, tem casos e casos: às vezes se tu tem um módulo de domínio muito grande, tu pode quebrar ele em duas, três partes — dois ou três submódulos. Também é um caso. Mas granular demais é uma coisa que eu não faço muito.

## Encerramento

Então, galera, era isso: os três tipos de módulos mais comuns, e como estruturar eles — e também o tipo de estrutura que eu uso nas minhas aplicações. Qualquer dúvida, comentem aqui; se gostou, comenta aqui, se não gostou comenta aqui também, dá like, dá dislike, é com vocês. Valeu, até a próxima.

---

*Nota de transcrição: transcrição de fala em português, já em pt-BR (sem necessidade de tradução). Pontuação e quebras de parágrafo foram normalizadas para leitura; repetições e hesitações típicas de fala foram limpas mantendo o conteúdo integral. Nomes próprios como "Fake Flix" (nome do app de exemplo do curso) e "Ultimate NestJS" (repositório de exemplo público, não afiliado ao autor) mantidos como citados no áudio.*
