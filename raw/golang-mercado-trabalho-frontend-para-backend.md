# Golang e o mercado de trabalho: como migrar do frontend para o backend

> Transcrição de vídeo (YouTube) — Lucas Badico. Já em português, sem necessidade de tradução.

E estamos de volta com o primeiro vídeo depois dos 5.000 inscritos. É isso aí, galera, finalmente chegamos naquela marca, e estamos aqui de volta para falar de uma das coisas que eu mais gosto de falar, que é Golang e o mercado de trabalho.

Nesse vídeo eu tô respondendo as perguntas do John Lee, um brother aqui da comunidade que foi lá no meu Instagram e deixou umas perguntas muito boas, que eu não poderia deixar morrer ali — eu tinha que trazer aqui para vocês essas respostas, para voltar a falar de um tema que a gente já fala aqui no canal há bastante tempo, que é empregabilidade e mercado de trabalho para dev júnior em Golang.

Bom, nesse vídeo a gente vai discutir por que Golang é uma escolha sólida, não é uma coisa passageira; qual é a vantagem pro dev em si; e também qual é o cenário do mercado atual, na minha visão, tanto brasileiro quanto internacional. E por fim eu vou te dar uma estratégia matadora para você conseguir migrar do frontend/Node para o Golang.

Você não me conhece: eu sou Lucas Badico, dev, professor, apaixonado por programação, especialmente Golang. E cara, muito obrigado aos 5.000 inscritos, muito obrigado aos meus membros e muito obrigado a essa comunidade fantástica que a gente tá construindo.

## A pergunta do John Lee

> "Oi Lucas, deixa eu te perguntar: no seu ponto de vista, o mercado para Go em São Paulo, como tá? Realmente tem vagas para júnior? Existem empresas em busca desses desenvolvedores? Você acha que é uma linguagem que talvez seja momentânea, ou vem para cravar mesmo? Eu atuo como frontend, gostaria de saber mais desse mundo de back."

Ele fez várias perguntinhas ali. Tem uma parte perguntando especificamente sobre São Paulo, mas falar de São Paulo é falar de uma tendência nacional, e falar de uma tendência nacional é falar de uma tendência mundial — ou, na verdade, algo que é uma tendência mundial que influenciou São Paulo. Então a pergunta dele vale muito pra gente conversar no geral.

Eu já respondi isso em vários outros vídeos, mas é um tema que sempre levanta dúvidas de vocês. Uma coisa muito interessante pra mim é que ele é um cara de frontend — pelo que entendi, ele já atua como frontend e quer saber como seria esse mundo de back. Vou adicionar como eu vejo o modo de pessoas como ele acessarem o mundo do Go.

## Go veio para ficar

Primeira coisa que eu tenho que falar: Go veio para ficar, Go não é momentâneo, Go não é passageiro. Você tem casos de algumas tecnologias que são meio que passageiras, ou muito específicas. Um exemplo: no passado tivemos Ruby/Ruby on Rails. O Ruby on Rails é muito forte ainda em determinadas áreas, mas aqui no Brasil só uma empresa adotou Ruby on Rails de forma relevante — foram algumas consultorias que ganharam dinheiro com isso. Fora isso, você não tem registro de uma adoção em massa ou de uma tendência de crescimento no Ruby on Rails. Teve forte influência no mercado, foi muito importante pra evolução do nosso ecossistema, mas não avançou a ponto de gerar vagas. Tem grandes pessoas que trabalham com Ruby on Rails — o DHH é um deles — mas o ponto é: não existe uma forte tendência de crescimento ali.

Go já é diferente. Primeiro de tudo, o Go se estabeleceu em grandes empresas. Pra citar aqui no Brasil: Mercado Pago e Mercado Livre, no geral, usam Go. A Stone é quase 100% Go também. São várias grandes empresas no Brasil que usam Go.

E tem uma questão intrínseca ao Go que faz dele um forte candidato à adoção em novas empresas: Go é uma linguagem *cloud native*. O que é uma linguagem cloud native? Go foi criado com a cloud em mente, é perfeito para ambientes de cloud. Por exemplo: se eu quero fazer uma aplicação web frontend dinâmica, JavaScript foi criado para isso; se eu quero fazer uma aplicação pro macOS, tem o Swift, que foi criado pra isso. Apesar de cloud ser um negócio heterogêneo — muitas ofertas, muitas empresas, muitas plataformas — o Go atende a todas essas plataformas. O Go é a base da cloud, vamos dizer assim, porque as características do Go, quando ele foi pensado, foram para sustentar a infraestrutura em cloud do Google (não uma cloud aberta ainda, mas a infraestrutura em cloud do Google). Então ele é perfeito pra cloud, o que faz com que qualquer coisa que você for fazer pra web/backend, o Go seja um forte candidato. Ele não é perfeito — não vou dizer aqui que é perfeito — mas ele te dá muita coisa de mão beijada, de forma muito simples.

## Filosofia: Go vs. Rust

Isso foi sobre tecnologia. Agora, sobre filosofia — pra entrar nesse ponto eu quero comparar a filosofia do Rust (tenho vários vídeos aqui no canal sobre isso, vocês sabem que eu gosto, que eu tô estudando e já trabalhei com ele) e do Go, pra vocês entenderem o que o Go fez.

Quando você olha pro Go e pro Rust, a primeira diferença clara é a quantidade de features. O Rust tem inúmeras features, inimagináveis, que o Go nem sonha ter. O Rust é pensado para ser *clever* — pra você fazer coisas inteligentes de maneira relativamente rápida e leve. O Go é pra você fazer coisas de maneira consistente e sólida.

É muito interessante porque eu já fiz vídeo sobre isso: essas duas filosofias entram em contraste. Quando eu quero programar em Go pensando como Rust, não dá certo. Quando eu quero programar em Rust pensando como Go, até dá certo, mas não fica perfeito. É isso que eu quero dizer: quando você aprende Golang, você aprende a ser pragmático a nível de linguagem, porque a linguagem só tem um jeito de fazer as coisas — ela te entrega uma maneira muito clara de comunicação, muito clara sobre o que é um ponteiro, o que é uma referência. É uma linguagem muito pragmática, muito crua. Não quer dizer que você não consiga fazer as coisas com ela — você consegue, só que de uma forma que às vezes não vai parecer bonita, mas vai ser muito funcional.

E isso cria em nós, devs, um "bichinho" que sempre diz: "não precisa ser perfeito, mas eu consigo fazer o bem feito ser tão bom quanto o perfeito, e muito mais fácil de dar manutenção no futuro". É meio abstrato o que eu tô falando, mas esse é o ponto: o Go te torna um programador melhor, não porque o Go é melhor que as outras linguagens, mas porque a filosofia dele te faz entender o que é essencial e o que não é essencial para produzir os teus projetos.

## O cenário de mercado

Dito isso, falei sobre tendência, sobre impacto. O que eu vejo no mercado geral: o que antes era tido como certo que seria feito em Node, hoje eu vejo a galera questionando e possivelmente migrando pra Go. Eu diria que isso tá em 40/60 — 60% continua em Node, 40% vai pra Go. Isso no mercado geral, incluindo startups.

No mercado americano, eu diria que tá 80/20 — 80% vai pra Go, 20% continua em Node, porque eu vejo muita vaga de Go lá, muita startup começando em Go. É muito mais difundido no mercado americano. No mercado europeu é um pouco diferente: você tem uma variedade muito maior de tecnologias, porque cada região tem um tipo de cultura.

## Vagas para júnior existem?

É uma pergunta interessante, porque eu não vejo isso tão comum, mas estão aparecendo cada vez mais. Eu acho que quando a gente aprende uma linguagem como Golang, tem que pensar um pouco diferente de quando se aprende frontend, porque você não deve mirar no júnior — deve mirar no pleno. Você tem que tentar desenvolver algo pra você, ou alguns projetos, que demonstrem que você tá no nível de um pleno, porque vaga para pleno tem.

E uma vez que você tá no nível de um pleno, pode concorrer a essas vagas e dizer, de cara: "não tenho experiência prática, não tenho experiência em times, não tenho experiência em empresa, então eu tô disposto a ganhar menos do que vocês estão oferecendo, pra entrar como júnior — mas eu consigo fazer o que um pleno faz." Tem que ser esse o discurso de vocês, porque assim você abre portas.

É muito mais fácil fazer isso quando você conhece alguém da empresa — daí entra a importância de comunidade e network, que a gente sempre fala aqui. Mas existe um modo de fazer essa transição vindo do frontend, que é atuar como fullstack.

## O caminho: fullstack como ponte

Eu, nesse momento, trabalho numa empresa que segue exatamente esse modelo. Na minha empresa tem oito pessoas: dois não-programadores, e seis programadores (comigo e o CEO), mais quatro programadores fora esse núcleo. Desses quatro, um é de backend e três são frontend — mas esses frontends são fullstack, e todos começaram a mexer com Golang depois que entraram na empresa.

Ou seja: há uma porta pra quem já é do frontend entrar numa empresa como fullstack que mexe no backend, e ganhar essa experiência prática de pleno atuando numa empresa — mesmo que como fullstack. Porque se você estudou pra aprender como um pleno e trabalhou como um pleno (mesmo que fullstack, numa empresa, mexendo no dia a dia no backend), com isso você consegue depois fazer essa migração e atuar como pleno-plus, quase sênior, num outro backend.

Então você tem essa chance, e é isso que eu tenho defendido. A minha intenção com o meu curso é oferecer uma alternativa, uma porta de entrada pra devs que estão na web, no frontend especificamente ou em Node, conseguirem uma vaga de fullstack em empresas que trabalham com Go. Essa é a principal meta do meu curso — se vocês não sabiam, eu dou um curso de Golang, já temos 10 aulas disponíveis, estamos preparando as próximas seis, e em breve vamos voltar com o curso num modelo um pouco diferente, dando sequência.

Mas o ponto é esse: se você é frontend, e em especial se está em São Paulo (como perguntou o John Lee), essa é uma baita oportunidade — veja pessoas que são fullstack em Go, ou seja, que trabalham no frontend mas também com Golang, veja em quais empresas elas trabalham dessa forma, e tente fazer conexões com essas empresas pra conseguir uma posição nelas, já com experiência de frontend.

Pra mim essa é a melhor maneira. Tem sim oportunidade. Vagas puramente de empresas que vão ensinar a pessoa do zero em Go existem, mas são muito poucas — começaram a aparecer, já tem algumas vagas de Golang júnior surgindo. Meus mentorados, no grupo, sempre mandam uma coisa ou outra, e isso é uma tendência interessante de se ver chegar. Espero que daqui a uns dois, três anos eu consiga fazer um vídeo aqui e dizer "olha só a quantidade de vagas de Golang júnior" — não posso fazer isso agora. Então vocês têm que usar essas estratégias que eu comentei.

## Encerramento

Fica aí à disposição de vocês, o meu curso, se vocês gostarem. A gente tá tentando trabalhar pra melhorá-lo. Fica também à disposição vocês mandarem perguntas pra mim, seja aqui nos comentários, seja no meu Instagram, igual o brother John Lee mandou — eu sempre respondo. Esse aqui tinha coisas muito interessantes, falei "vou fazer um vídeo" — então esse vídeo é resposta pro John.

Fica à disposição pra mandarem perguntas, e me digam: vocês que migraram, seja pra Golang ou outra linguagem, mas usaram essa ponte do frontend, contem aí nos comentários a experiência de vocês, e deixem dicas de como a galera pode achar essas empresas que têm vagas de fullstack com Golang.

É isso aí, muito obrigado pela atenção de vocês.
