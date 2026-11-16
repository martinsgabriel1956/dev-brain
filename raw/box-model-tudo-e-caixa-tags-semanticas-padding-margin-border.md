# Box Model: tudo é caixa

Então, pessoal, nós vamos continuar a saga do básico do CSS. Acredito que a gente está trilhando bem legal, bem passo a passo, o que é o CSS, como a gente vincula, como é que funcionam as tags.

## Tags semânticas

Se vocês tiverem um pouco mais de curiosidade de conhecer as tags semânticas do HTML5, eu recomendo fortemente que vocês estudem isso. Se eu não colocar aí na descrição do vídeo, por favor, reclame, eu quero o link para eu colocar para vocês, mas basicamente vocês podem vir aqui no Google e colocar tags semânticas HTML5.

Vocês vão conhecer as principais e eu já destaco desde já a importância de a gente conhecer sobre as tags semânticas, porque elas ajudam a melhor colocar o nosso site nos sites de busca no Google, a gente consegue hierarquizar de forma melhor os nossos sites quando a gente utiliza as tags semânticas.

Mas vocês vão perceber, e principalmente essa aula de box model é para poder deixar isso o mais claro possível, é que todas as tags são caixas. Meio que não faz muita diferença eu criar um header ou criar uma div, não faz diferença nenhuma, absolutamente nenhuma visualmente ou então na prática, desenvolvendo uma aplicação, eu colocar section ao invés de uma div. Não faz absolutamente nenhuma diferença, a diferença está na semântica, por ser isso uma boa prática da programação.

Quando eu coloco header, eu entendo semanticamente que o conteúdo que tem aqui dentro é o conteúdo de algum cabeçalho. Se eu colocar nav é um conteúdo de links, é uma barra de navegação. Se eu colocar uma seção, provavelmente é um trecho de conteúdo do meu site. Se for um artigo é um conteúdo mais relacionado a texto. Se eu colocar figura é uma imagem. Se eu colocar o footer, então é a parte que você está desenhando o rodapé do seu site.

Então essa tag semântica facilita a vida do Google quando você coloca o seu site na internet, então é importante para você conhecer as principais tags e consequentemente saber aplicar eles da melhor forma possível, pois vai te dar um diferencial quando a gente está construindo páginas web, beleza?

## Tudo é caixa

Então o primeiro tópico que a gente vai trabalhar nessa aula, e sempre que eu lembrar de algum conceito eu vou estar lembrando para vocês, é que tudo é caixa, basicamente isso.

Essas regras aqui de box model vocês podem aplicar absolutamente tudo. Todas as tags são caixas, são box, são divs, se é que eu posso dizer assim. Para quem não sabe o que é div, vou demonstrar aqui para vocês: div é uma tag que antes do HTML5 basicamente todo o site era composto por divs. É lógico que tinha o link, que são meio que desde a fundação do HTML tem essas tags principais aqui, parágrafo, título, subtítulo, body, head, mas não tinha essas tags semânticas como section, article, elas vieram todas com o HTML5. Então a gente compunha a interface toda feita com divs e divs é um elemento de caixa, e aí a gente consegue aplicar em elementos de caixa sempre, sempre, sempre essas características aqui.

Width é o quê? A largura, o comprimento, será que eu posso dizer assim, em 2D. Height, a altura da nossa caixa. O padding é o espaçamento do conteúdo com relação à borda da caixa, então se eu aumentar o padding na parte de cima ele vai aumentar esse espaçamento.

Então para todos esses aqui tem variações, porque como é uma caixa tem o quê? Quatro lados. Então tem o margin-top, tem o margin-bottom, tem o margin-left e tem o margin-right. Margin-top é a margem de cima, margin-bottom é a margem de baixo, margin-left é a margem da esquerda, margin-right é a margem da direita. Margin é a distância entre uma caixa e outra que eu coloco para espaçar, como eu coloquei aqui, e essa mesma regrinha se aplica ao padding, isso aqui é o espaçamento interno. Border é a bordinha da nossa caixa, border-radius é para poder arredondar os pontos da nossa caixa, o width é a largura, height é a altura.

E aí a gente vai conhecendo essas outras propriedades, onde você pode aplicar os tamanhos em pixels, em pontos, em rem, e eu vou mostrar que essas duas aqui são medidas relativas, é importante saber disso, em centímetro, em porcentagem, que também é uma medida relativa. Então a gente precisa conhecer quando aplicar o quê, e não necessariamente você vai só aplicar em uma interface medidas fixas, como em pixels. Eles vão ter que aplicar em diversas vezes medidas com porcentagem ou em rem, são medidas relativas que ajudam na construção do nosso layout a responsividade.

## Padding na prática

Então se eu colocar, por exemplo, uma caixinha com a medida dela em 70%, eu vou até mostrar aqui na prática para vocês. Vamos supor que eu venho aqui, já vamos fazer uso da nossa linguagem semântica, e eu vou criar aqui uma seção. Essa seção vai ter um texto lorem ipsum, então vamos lá, o clássico texto de um parágrafo chamado lorem ipsum, vamos dar enter, olha só, já apareceu aqui. O que a gente vai fazer? Como é que a gente vai estilizar?

Está aqui o nosso body, a gente pode vir aqui, section. A primeira coisa que eu quero mudar é o background-color, eu quero deixar ele um pouco em um cinza diferente, ou seja, eu vou aplicar um 2A2020, está aqui ele. Para poder melhorar o espaçamento dele, para eu ter espaçamento interno, o que eu vou fazer? Eu vou dar um padding e olha só as variações. O padding, quando eu digito ele normal, ele é um resumo dos outros paddings.

Vou explicar: quando eu digito padding, o CSS costuma sempre ter isso aqui entre todas as propriedades, existem propriedades que resumem em uma tag só. Por exemplo, eu posso muito bem aplicar o background-color como background, olha só como não vai mudar nada. Por quê? Porque essa aqui é uma tag que engloba a background-color. Background-color é uma das outras propriedades, porque tem a background-color, tem a background-repeat, tem o background-attachment, tem a background-position, tem o background-image. Ele mostra para você todas as subcaracterísticas do background, e tem o background normal, que por si só engloba todas as características.

Násser, como é que eu faço para descobrir qual é a ordem que eu aplico, por exemplo? Meio que você vai pegando com o tempo, você vai estudando com o tempo, mas olha, um site que eu sempre indico é o W3C, que é o órgão que, tipo assim, regulamenta tudo que é da internet web, tudo que é com relação ao web, eles colocam aqui, e você pode colocar tag, tag background. É um ótimo site para você conhecer absolutamente todas as técnicas que a gente está trabalhando aqui. Ele tem vários exemplos, e aqui, try it yourself, ele vai te apresentando vários exemplos para você entender da melhor forma possível as propriedades. Olha só, ele traz esse exemplo aqui, try it yourself, para vocês irem entendendo.

Então, essa parte inicial, use e abuse, e até hoje, não interessa, eu ainda mexo muito nesse site aqui para poder estar conhecendo todas as propriedades, as propriedades que são gigantescas, por isso que precisa de ter um estudo por fora, para vocês evoluírem nessa parte.

A parte de background a gente vai tratar ainda, mas eu estou falando de padding, box model, vamos focar aqui. O padding então: lembra que eu tenho padding-top, ele vai me dar espaçamento na parte de cima. Então, se eu apertar 100 pixels, o que ele vai fazer? Olha só, está vendo que abri uma caixinha aqui? Eu vou deixar ela mais evidente, para todo mundo ver, vou colocar em ciano. Não existe essa cor, voltei aqui, peguei uma cor ciano rapidinho para poder a gente aplicar.

Então está aqui, essa é a nossa caixinha. Eu vou aplicar um padding-top, acabei de aplicar, 100 pixels, olha só, ele deu espaçamento com relação ao espaçamento interno da nossa caixa. Vamos supor que eu queira um espaçamento na parte esquerda, só que de 50 pixels, olha só, o meu conteúdo afastou na parte da esquerda. Se eu quiser aumentar isso aqui para 200, ele afastou ainda mais. Vamos supor que eu queira um padding-bottom, ou seja, na parte de baixo, de 50 pixels, olha só, a minha caixinha deu espaçamento interno e está aqui, meio que administrar o espaço interno.

E tem como eu resumir isso aqui tudo com padding, sendo que é essa ordem: top, right, bottom e left. Sempre começa no topo, e isso aqui se aplica a um monte e um monte de propriedade, dessa regrinha: sempre começa no top e aí gira no sentido horário. Então top, right, bottom, left. Então, para eu aplicar, vamos supor que eu queira 100 pixels na parte de cima, nada na esquerda, 200 na parte de baixo e 500 na esquerda, quando eu aplico, ele vai fazer isso para mim. Está aqui a nossa página com esse padding aplicado.

## Margin

E a mesmíssima coisa dá para fazer com margem, só que o margem, como o próprio nome já diz, não é o espaçamento interno, é a distância de uma caixa para outra. Então ele vai dar a distância com relação ao que está do lado dele, que é esse link aqui e esse body.

Então vamos lá, se eu colocar 50 em cima, posso zerar aqui essa outra parte, 50 em cima, ele deu um espaçamento. Deixa eu colocar um padding aqui, senão fica muito feio, ninguém enxerga nada, um padding de 50 pixels. Se eu aplicar só o padding de 50 pixels, é a mesma coisa de eu escrever 50 pixels, 50 pixels, 50 pixels, ele aplica para todos os lados quando você digita só assim: 50 para cá, 50 para cá, 50 para cá, 50 para cá.

Quando você aplica um margin, 50 em cima, eu quero aumentar, 50, 100, aumentou. Vamos supor que eu quero dar um margin-left, então modifica aqui, coloca 50, ele dá o espaçamento aqui.

## Border e border-radius

O conhecimento de border é muito importante em todo o nosso desenvolvimento do CSS. Vocês entenderam essas propriedades? Deixa eu voltar aqui para a nossa linha, vê se eu esqueci de alguma coisa, acredito que não.

E propriedade de border da mesma forma, o border é uma propriedade que engloba várias outras, deixa eu demonstrar aqui para vocês. Vamos lá, vamos supor que eu queira aplicar uma border, então border 5px solid red. Você percebe que eu apliquei três propriedades aqui dentro de border, e olha só, ele deixou a borda sólida vermelha. Mas eu poderia muito bem escrever isso dessa forma aqui: border-width é 5 pixels, color red, então vai surtir exatamente o mesmo efeito. Se eu colocar aqui 15px, vai mudar isso, se eu vir aqui e mudar para blue, vai mudar.

Se eu colocar um border-radius, eu posso colocar fixo em todos os pontos e, da mesmíssima forma, eu posso colocar 0px, 10px, 0px, 50px, vamos ver como fica a nossa borda. Na verdade é isso, 0, apliquei 0 aqui, 10 aqui, nada aqui e 50 aqui, quando eu quero bordas fixas. Se eu colocar, por exemplo, 50px, vai aplicar para todas.

E se eu quiser que sempre seja uma circunferência, eu faço 50%, eu utilizo em porcentagem, vai virar um elipse. Mas por que não virou um elipse? Porque o width está diferente do height, então vai virar um elipse. Então se eu fixar, por exemplo, em 300px, o width é 300px, o height de 300px, vai virar uma circunferência bonitinha utilizando o border-radius.

E essas propriedades também você vai conhecer com o tempo, e não deixe de fuçar, até não querer mais, o W3C. E eu vou sempre estar explicando essas propriedades, talvez desconhecidas, ao decorrer do curso. Não se preocupe com isso, porque você vai aprendendo com o tempo. Até a próxima.
