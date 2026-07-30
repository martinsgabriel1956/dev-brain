# System Design na Prática: Simulação de Entrevista com Reserva de Ingressos de Cinema (draw.io)

> Transcrição de vídeo em português (canal Rocket City), primeiro episódio de uma série semanal de conteúdo técnico. Reescrita como Markdown estruturado em seções temáticas a partir de transcrição corrida sem pontuação, sem cortes de conteúdo. Sem necessidade de tradução — fonte já em português.

## Abertura

Boas-vindas ao nosso primeiro vídeo da série, onde eu vou estar trazendo um conteúdo tech por semana, e você vai poder acompanhar mesmo que você seja uma pessoa experiente ou uma pessoa que esteja iniciando na área. Esse vídeo é para você. Eu vou tentar abordar de forma bem prática como que funcionam os temas, os tópicos que eu vou trazer aqui. E para você não perder, já se inscreve aí no canal da Rocket, que toda semana eu vou estar trazendo esse conteúdo, beleza.

O tema de hoje é system design — então é arquitetura de sistemas — mas não é só isso, é como se dar bem em entrevistas de system design. O meu nome é João, eu trabalho pra gringa já tem 3 anos, eu já passei por bastante experiência, seja aqui no Brasil ou lá fora, de entrevistas de system design. Eu vou tentar trazer hoje para você como que são essas entrevistas e qual a dinâmica que você pode aplicar, e algumas dicas cruciais para você se dar bem nelas.

## Overview: o que é arquitetura de sistemas

Para você que nunca ouviu sobre system design, sobre a arquitetura de sistemas, eu vou tentar dar um overview aqui — vou tentar explicar de uma forma bem abstrata, bem genérica.

A arquitetura de sistemas é a forma que os servidores se conectam. Vamos usar um exemplo prático: você tá acessando o Instagram pelo seu computador. Quando você vai digitar instagram.com no seu browser, por trás dos panos tá acontecendo uma série de coisas até chegar no servidor do Instagram, e o Instagram carregar todas aquelas fotos para você no seu feed. É isso que é a arquitetura de sistemas — é tudo que ocorre ali por trás, debaixo dos panos, nessa interconexão. Nessa conexão que existe entre os servidores do Instagram, o banco de dados, o CDN (que eu também vou explicar para vocês o que que é), até que esse conteúdo chegue a você, até que você veja ele visualmente.

Espero que você goste do vídeo — se você gostar, compartilha na rede, comenta bastante. Esse vídeo vai ser dividido em duas partes: essa parte introdutória que eu tô fazendo agora (onde eu me apresento e explico um pouco sobre o tema/tópico que a gente vai falar hoje) e a segunda parte, que é uma parte prática — vocês vão estar vendo eu mexendo aqui para poder mostrar esse conceito de uma forma dinâmica e prática, porque falar é fácil, mas a gente quer ver na prática.

## Parte Prática: simulando uma entrevista de system design

Tô aqui com o meu draw.io aberto. Draw.io, para quem não sabe, é uma forma de você diagramar sistemas, fazer fluxogramas, diagramas no geral. A gente vai utilizar aqui no vídeo — quando você tá fazendo entrevistas, geralmente eles usam o próprio draw.io ou usam esses públicos mesmo.

### O problema inicial e as follow-up questions

Temos aqui as instruções do nosso sistema. Como é numa entrevista, geralmente a pessoa (o entrevistador) vem com algo bem simples, assim: "fazer um sistema de reserva de ingressos de cinema". E o que que você tem que fazer? Você tem que fazer follow-up questions — que é basicamente você perguntar mais coisas sobre esse sistema. Ele faz isso propositalmente.

Já deixei algumas coisas aqui, como se eu tivesse feito essas perguntas:

- Esse sistema de reserva de ingressos de cinema tem que ter um **seatmap** — para o usuário poder escolher o lugar onde ele vai sentar.
- Ele pode fazer **pesquisas dos filmes por nome**.
- O que é crucial para esse sistema, o que é um requisito funcional que precisa ter: ele **comprar o ingresso e reservar por 15 minutos caso o pagamento não seja realizado**.
- Esse sistema será **acessado via web** — então mobile, desktop, qualquer dispositivo que tenha acesso ao navegador.

São esses tipos de perguntas que você tem que fazer, baseado em um problema simples, para começar a destravar. Uma pergunta boa de início para se fazer é perguntar sobre **autorização, autenticação e login**. Esse sistema vai ter login e autorização, mas o entrevistador costuma falar: "vai ter, mas você não precisa considerar isso, você não precisa desenhar isso, pode assumir que tudo tá sendo autenticado" — isso ajuda a salvar tempo. E por que isso ajuda? Porque quando você começa a fazer pergunta assim, mais básica, começa a pensar em outras coisas — é uma forma de você ganhar tempo para pensar nas perguntas que você precisa fazer.

### Montando a arquitetura

A gente vai ter um **ator**: esse ator é o nosso client, é o nosso front-end. Ele pode ser acessado via mobile, desktop, notebook — enfim, qualquer coisa que tenha navegador. A gente vai ter o nosso sistema aqui, os nossos servidores — vamos dizer assim, **web server**.

Uma boa prática que você pode fazer é pensar em **escalabilidade** — geralmente isso é mais para senioridades mais altas, quando você pensa em escalabilidade. Inclusive perguntas do tipo "quantos usuários tem, quantos acessos por minuto, quantos ingressos são comprados por dia" são boas, mas somente para senioridades mais altas/avançadas. No caso mais simples não precisa. Mas uma coisa de praxe que é bem legal colocar aqui é o **load balancer**.

Load balancer é uma forma de você não onerar, não deixar um servidor que já tá cheio de requisição com mais requisições. Por exemplo, se você tem três servidores (a gente colocou três pro nosso sistema) e um deles tá usando 100% da máquina, a gente tem um load balancer que, baseado em uma série de regras (pode ser por exemplo hardware), vai mandar para outro servidor. A gente tem esse load balancer justamente para fazer esse direcionamento das requisições, e o nosso web server aqui.

Primeira coisa: vou organizar do mais fácil pro mais difícil.

1. **Pesquisar os filmes por nome.** Esse sistema vai ser acessado por web — já tá feito, essa parte já tá feita (client mobile/desktop/notebook + load balancer fazendo o direcionamento das requisições).

### Busca de filmes: `/search` e o banco de dados

Para pesquisar filmes, a gente precisa ter esses filmes guardados — então a gente vai ter um **banco de dados** aqui. Esse banco de dados vai ter os filmes, e os filmes vão ter algumas coisas, como por exemplo um **ID**, um **nome**, e vamos dizer que vai ter uma **categoria**. De início é isso que a nossa tabela de filmes vai ter no nosso banco de dados.

Esse banco de dados geralmente é bom falar qual é — nesse caso pode ser **MySQL**. Por quê MySQL? No meu caso aqui é por meios didáticos, mas se eu tivesse numa entrevista e eu visse que filmes não têm relação com outra coisa, eu poderia criar um banco de dados **não relacional**, já que ele não tem relação com nenhum outro dado — poderia ser MongoDB, enfim, qualquer outro banco não relacional. Mas para deixar mais didático eu coloquei o MySQL aqui, que é o mais comum, imagino que todo mundo que trabalha como dev ou tá iniciando os estudos conhece, e para facilitar serve pra gente.

A gente vai ter os **endpoints** aqui no nosso sistema. O primeiro endpoint vai ser o `/search` — ele vai bater aqui, vai ser um `/search`, ele vai bater no nosso MySQL. Então o nosso sistema tá conversando com o MySQL, a gente vai ter o nosso `/search` por nome, ele vai buscar o filme — fazer uma query no banco de dados — e vai retornar pro nosso usuário. A partir disso, nosso usuário vai ver "ah, esse filme tá disponível", ele vai clicar em "prosseguir".

### Seatmap: API externa

Assim que ele clicar em prosseguir, a gente tem que mostrar o seatmap para ele. A gente vai ter a **API de seatmap** aqui. Por que é uma API externa, por que não é algo que tá dentro da nossa interconexão? Porque geralmente uma API de seatmap lida com bastante coisa — qual o local físico, quais são as salas disponíveis — então tem bastante coisa, é um contexto muito específico, e não faria sentido a gente colocar aqui no nosso sistema de reservas. Então é uma API externa.

Uma coisa boa de também ter uma API de seatmap é: e se outros sites quiserem usar a nossa API para vender os nossos ingressos? Outro site que começou a vender ingressos de cinema e quer usar as nossas APIs — então a gente precisa ter um sistema externo de seatmap, que é o que a gente tá fazendo. O nosso web server vai comunicar com esse seatmap e vai retornar pro nosso usuário os assentos.

Então isso é tudo endpoint: vai ter, por exemplo, um `GET assentos`, vai ter também um `POST` para indisponibilizar assento — a gente pode ter um post para indisponibilizar ou disponibilizar um assento, tipo `commit assento`. Isso quer dizer o quê? Por exemplo, `commit assento` pega aquele assento e indisponibiliza ele, ou, se ele tiver indisponibilizado, disponibiliza — ele faz esse switch.

Então, recapitulando a ordem: primeiro o cliente fez o `search`, buscou o filme, retornou para ele. Depois que retornou, ele vê na page o seatmap, que retorna os assentos disponíveis. Nisso o usuário vai escolher o assento que ele quer, a sala e o assento.

### Pagamentos: outra API externa

Assim que ele escolher a sala e o assento, ele vai pra parte de pagamentos. O nosso web server vai lidar com pagamentos, e pagamentos também vai ter uma **API externa**, porque geralmente a gente utiliza APIs externas para pagamentos — hoje em dia a gente tem diversas APIs que são boas, escaláveis, e se der problema a gente vai conseguir saber. Então é muito bom ter um serviço externo para lidar com isso. A gente vai ter a API de pagamentos, que vai conversar também com o nosso web server.

(Nota do apresentador: as setas do diagrama foram desenhadas de forma unidirecional só para mostrar de onde tá saindo o fluxo — por exemplo, o fluxo sempre inicia pelo cliente e vai até o destino — mas na prática tudo tem idas e vindas: o `search` retorna, pagamentos retorna, seatmap retorna. É uma comunicação bidirecional.)

### Reserva de 15 minutos: Redis como cache

Retomando a lista de requisitos: seatmap ✓, pesquisar filmes por nome ✓, comprar o ingresso ✓ — mas falta "reservar por 15 minutos caso o pagamento não seja realizado". Como fazer isso?

O nosso web server vai ter duas opções: ou ele vai pra pagamentos assim que o usuário for pagar, mas caso o usuário não pague e fique na tela aguardando, vai ter o nosso **banco de dados de cache** — um **Redis** aqui.

O que é o banco de dados de cache: é um banco de dados onde ele vai guardar o nosso assento. A ID — vamos dizer assim, ele vai ter o `seatmapId` e vai ter o `seatId` — então ele vai ter o número da sala do cinema e o número do assento. Ele vai guardar isso por 15 minutos, expira em 15 minutos, porque é a nossa regra de reservar o ingresso por 15 minutos.

Recapitulando o fluxo completo: o cliente bate no filme, faz a query para buscar esse filme, esse filme é retornado. A gente vai pro seatmap, pega os assentos disponíveis, e a gente escolhe um assento. A gente vai pra pagamentos — ou não. Caso a gente não vá pra API de pagamentos, a gente reserva esse filme por 15 minutos: esse assento vai ser reservado no nosso banco de dados de cache. Mas, caso ele deseje realizar o pagamento, ele só vai realizar o pagamento e a gente vai fazer o `POST` do `commit assento` — a gente vai indisponibilizar esse assento porque foi feito um pagamento.

### O problema de consistência entre seatmap e cache

Agora, uma coisa que eu não comentei: quando ele fizer esse `GET assentos`, pode ser que esse assento esteja no nosso banco de dados de cache, porque a API de seatmap não tá lidando com essa questão de reserva — é a gente, o nosso sistema interno, que tá lidando com a reserva. A API de seatmap não. Então pode ocasionar de a gente fazer um `GET assentos` e ele retornar que tá disponível, mas o nosso assento pode não estar disponível de fato, porque ele pode estar no banco de dados de cache.

Como é o nosso sistema interno que tá lidando com a reserva, tem que ter um mecanismo: o assento foi retornado pela API de seatmap como disponível, mas o nosso sistema interno tá indisponível. O que acontece na maioria dos casos que eu já vi — eu não conheço muito bem essa parte da arquitetura, fiz isso de uma forma sem pensar muito, foi uma forma bem simplista — é aquele negócio: quando aparece para você disponível no frontend, você clica, mas aí aparece "esse assento já foi reservado por outro, tá pendente de pagamento".

É isso que vai acontecer aqui: o `GET assentos` retorna pro cliente, o cliente escolhe um assento, mas quando esse assento chega no nosso web server, a gente vai verificar no nosso Redis. Assim que a gente verificar nesse Redis, a gente vai falar "esse assento foi reservado, infelizmente" — então, enquanto mostrou no front que esse assento tava disponível, a gente voltou pro back e viu, pelo Redis, que ele tava reservado por 15 minutos.

Eu não sei se é a melhor das formas — eu concordo que não é — mas quando você tá fazendo uma entrevista dessas de arquitetura é muita conversa, você vai trocar ideia com o entrevistador e vai perguntar as coisas para ele. Isso aqui eu não treinei antes, fiz da cabeça agora — baita rascunho, sei que tem bastante erro aqui, mas o foco é a gente mostrar como funcionaria uma entrevista de system design.

### Fechando os requisitos

Voltando na nossa lista: temos um sistema que vai ser acessado via mobile/desktop, a gente pesquisa os filmes por nome, a gente tem o seatmap, e a gente compra o ingresso e reserva por 15 minutos caso o pagamento não seja realizado. Temos tudo isso aqui, todo esse fluxo tá funcional — a gente consegue ver claramente essas coisas.

Numa entrevista de verdade, você vai destrinchar muito mais essas APIs — vai falar quais são os endpoints delas, quais os JSONs de retorno, tudo. Vai ter muita coisa que você vai precisar fazer. Por exemplo, esse web server que tá conectando com o banco de dados pode ter uma lógica aqui dentro também — se tiver alguma lógica, você tem que deixar explícita. Por exemplo, eu falei que a gente consulta o banco de dados Redis para retornar caso ele esteja reservado — essa é uma lógica que estaria aqui, eu posso explicitar isso na fala, comunicando com o recrutador.

## Encerramento

Espero que isso tenha ajudado, espero que isso tenha dado uma clareada, uma ideia boa de como funciona uma entrevista de system design. Vocês viram que não é algo muito complexo, é algo simples, mas a gente tem que ter muita conversa com a pessoa com quem a gente tá sendo entrevistado. Isso ajuda bastante — como eu falei, isso aqui tá bem simplista, não é alguma coisa muito escalável e nem production ready, mas é alguma coisa que eu tirei agora da minha cabeça, que veio à tona.

É isso, galera, espero que vocês tenham gostado. Não se esqueçam de se inscrever no canal da Rocket City, beleza, e agradeço de coração — agradeço se isso te ajudou, deixa um comentário aí, e estamos junto. Não se esqueça de ver os próximos vídeos ou os vídeos anteriores caso eu já tenha postado. É isso, beleza, tamos junto.
