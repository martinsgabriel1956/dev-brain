# Básico de CSS: o que é, como criar estilos e as três formas de aplicar

Olá pessoal, agora nós vamos começar literalmente a parte básica, então deixa eu voltar aqui para a aula.

Vamos lá para básico de CSS, então só para deixar muito bem claro que a gente vai passar nos principais tópicos do CSS. É claro que é muito complicado eu resumir um CSS, uma linguagem de marcação tão ampla e com tantas funcionalidades em um módulo só, mas é literalmente passando pelos principais pontos e eventualmente eu vou vir aqui voltar e gravar alguma aula, mas no primeiro momento eu gravei o que é básico, básico, básico para poder a gente estar entendendo e compreendendo as próximas aulas.

Então esse aqui é um módulo de nivelamento para tanto aqueles que não têm um conhecimento muito alto em CSS ou até aqueles que já atuam na área. Eu sempre costumo olhar, mesmo tendo trabalhado há um tempo já com isso, eu sempre procuro verificar se tem alguma coisa que eu ainda não sei e que o outro pode agregar. Então nós vamos passar por algumas propriedades, calma lá que a gente vai chegar lá.

## O que é CSS?

Primeira coisa, o que é CSS? Então vamos começar lá do começo, o que se trata essa linguagem e as suas particularidades.

CSS significa Cascading Style Sheets, ou seja, folhas de estilo. Então o CSS não é uma linguagem de programação, ele é uma linguagem que é mais voltada para marcação, para estilo e aí a gente vai pegando as tags do HTML e aplicando o estilo nessas tags de forma a gente construir o nosso layout.

Mas eu sempre costumo dizer que o CSS detém de três partes que têm propriedades que são mais voltadas à estilização, propriamente dito. A gente vai para a prática, a gente vai codar para vocês entenderem. Tem propriedades que são mais voltadas para layout, que é literalmente construir a estrutura, o esqueleto do nosso site para poder abrigar o conteúdo e fazer com que ele seja responsivo, ou seja, se adapte a qualquer tipo de tela. E tem a parte do CSS que é mais voltada com propriedades de motion, que a gente vai trabalhar as duas principais aqui nesse curso.

Então esse básico do CSS é mais voltado para a gente entender quais são as propriedades de estilo e as propriedades de layout. As propriedades do CSS que são mais voltadas para motion, logicamente, vão estar no curso de motion.

No caso do CSS em particular, são documentos que descrevem a forma que o HTML deve ser apresentado, então meio que o poder está na junção. Se você colocar só HTML puro, você vai ver como é uma página extremamente, mas extremamente arcaica, onde não tem poder de personalização nenhum, é tudo muito básico. Então o CSS se encaixa muito bem com o HTML nesse sentido.

## Como criar estilos?

Como criar estilos? A gente vai demonstrar agora na prática. De basicamente é um elemento que é a tag do HTML, a gente vai trabalhar muitos exemplos para vocês entenderem. Vem a propriedade e vem o valor, então a grande questão está em conhecer essas propriedades, saber como aplica os valores e um exemplo aqui, em uma tag h1, eu estou aplicando a propriedade de color, aplicando o valor green.

## Como aplicar o CSS?

Primeira coisa, como que eu aplico o CSS? Como que eu desenvolvo o CSS? A gente tem basicamente três formas que eu vou mostrar agora para vocês.

Vamos aqui para o nosso VS Code, onde a gente já teve uma aula para configurar ele da melhor forma possível. Posso fechar essa parte aqui e eu apenas criei uma pasta chamada CSS Basics, para poder a gente começar a entender como é que funciona o CSS.

Como eu disse para vocês, tem um plugin que é nativo do próprio VS Code que completa o HTML para a gente, então eu simplesmente vim aqui, cliquei em New File, digitei index.html e criei a nossa primeira página HTML para poder a gente estar observando.

Para quem não sabe por que a gente sempre deixa index.html, é um padrão da internet que quando o browser identifica o arquivo index.html, é meio que a primeira página do seu site, então sempre a página inicial do seu site é sempre colocada como index.html.

Sem mais delongas, vamos lá. HTML, olha só, a gente aperta aqui no 5 e ele já completa nessa estrutura para a gente. Vamos tentar entender aqui, já falando de um pouquinho de HTML5 básico, essa é a estrutura básica de toda e qualquer página web.

Tem a tag HTML que engloba todas as outras tags, tem a tag head que é a tag de cabeçalho, onde vai as tags meta para poder melhorar, definir alguns padrões e melhorar até a visibilidade do seu site pelo Google. Depois eu posso colocar uma aula bônus para vocês entenderem como a gente utiliza essas tags meta.

O title é literalmente o que é escrito na parte da aba do seu website, então eu vou abrir ele com o Live Server para poder a gente visualizar melhor essa página e conforme eu for fazendo alterações aqui no nosso código, vocês vão vendo as alterações aparecendo aqui automaticamente. Se você não sabe como é que eu faço isso, dá uma corrida lá na parte que a gente estruturou, o VS Code, e instalou os plugins para vocês entenderem.

Eu meio que inicializei um servidor onde eu faço qualquer modificação, então teste, só de eu salvar ele já vai aparecer aqui, teste, está muito pequeno, vocês não estão enxergando. Vamos lá, Document, então eu vou colocar aqui aulas básicas CSS, então ele apareceu no título da minha aba aqui no meu documento.

Está aqui o nosso arquivo HTML que a gente precisa vincular ele ao CSS, então como eu disse para vocês, existem três formas de a gente aplicar o CSS.

### Estilo inline

Tem o estilo inline que é aplicado diretamente em qualquer tag e é o tipo de maior prioridade, a maior prioridade é o do tipo inline, eu não estou entendendo nada que você está falando, vamos lá.

Vamos supor que eu coloque aqui uma tag h1, que para quem não sabe é uma tag de título, onde eu vou estabelecer os títulos do meu site, então aqui, meu título, e eu dou um Ctrl+S e ele vai aparecer bem aqui para a gente, deixa eu dar um zoom para vocês visualizarem, está aqui meu título.

Eu posso muito bem vir aqui na própria tag e abrir uma propriedade chamada style e colocar entre aspas o meu conteúdo CSS, então eu aplico o CSS onde ele vai aplicar estritamente para essa tag aqui, se eu tiver uma outra tag h1 aqui embaixo, onde eu coloco o meu segundo título, ele não vai aplicar para essa.

Então, deixa eu colocar aqui, por exemplo, o color: red, essa aqui é a propriedade de cor do texto, essa aqui é a cor em escrito, mas eu poderia muito bem também colocar em hexadecimal ou em RGBA e olha lá, por mais que eu tenha aplicado ao h1, eu estou aplicando o estilo inline.

### Estilo incorporado

Um outro tipo, um outro jeito de a gente incorporar o nosso CSS é colocar a tag style no nosso cabeçalho, então eu venho aqui no nosso head e eu vou abrir a tag style, onde eu vou definir aqui type igual a text barra CSS.

Então, eu vou aplicar o meu CSS aqui dentro utilizando agora seletores, como assim seletores? São literalmente as tags, então vamos supor que eu queira aplicar para o h1, que eu estou fazendo aqui embaixo, eu abro, fecha chaves, é essa sintaxe do HTML, onde eu aplico color: green e aí todos os h1s da minha página vão ficar em verde, está vendo?

Então, quando eu aplico no estilo incorporado, que é colocado no cabeçalho da nossa página HTML, você percebe que ele aplica para a minha página, mas é só para esta página aqui, então você vai percebendo que a grande intenção é eu diminuir o máximo o código, então se eu for colocar uma tag de estilo em cada página e o meu site tem 40 páginas, você está vendo que quando eu precisar, por exemplo, modificar, não quero verde, agora eu quero roxo, então você vai lá e coloca purple, você vai ter que fazer essa modificação em 30 páginas, então você percebe que esses estilos aqui são mais utilizados para poder a gente usar em exceção, então quando você quer aplicar, eu quero nessa página aqui fazer um estilo diferente, aí você pode aplicar o estilo incorporado ou mais específico ainda, quando eu quero em uma tag específica, eu aplico um estilo inline e dá para perceber o que eu acabei de falar aqui, que é quanto mais para baixo, maior a prioridade, o que isso significa?

Você percebe que eu apliquei aqui h1, ou seja, todos os meus h1s na minha página deveriam ficar roxo, mas pelo fato de eu ter um estilo aplicado inline, ele tem maior prioridade e o meu texto continuou vermelho. Beleza?

### Arquivo externo

Então, essa aqui é a última forma e a forma mais utilizada, mais amplamente utilizada é aquela que você literalmente vem aqui, vamos criar aqui uma pastinha chamada CSS e eu vou criar um arquivo style.css aqui dentro dela, onde eu vou estilizar a minha página por meio de um arquivo e por ser um arquivo, eu posso linkar ele em diversas páginas, um só arquivo, eu mando em diversas páginas e como é que eu faço esse link?

Utilizando justamente a tag link, CSS aqui, Emmet Abbreviation, onde eu falo, vai lá na pasta CSS e encontre e leia esse arquivo style.css, então se eu colocar qualquer modificação aqui, calma que esse seletor aqui eu ainda vou explicar para vocês, vamos supor que eu tire o padding, o margin, aplique, sei lá, box-sizing, border-box e eu coloco um background-color na minha página, deixa eu colocar no body, é melhor, aí eu vou abrir aqui a tag body, que é a tag do corpo, onde literalmente eu coloco o conteúdo, eu coloco o background-color e eu vou colocar o meu preto, sempre utilizo nas minhas interfaces, você percebe que quando eu tirei o margin e o padding, meio que o espaçamento entre as tags diminuiu, então olha só, eu estou aplicando o CSS de três formas diferentes, então essa é a primeira aula que eu queria mostrar para vocês, onde eu posso muito bem exemplificar essas coisas e vamos supor que eu coloque o h1 aqui como color: green, vamos ver o que acontece, color: green, ele sobrescreveu esse carinha daqui, então é assim que a gente trabalha com CSS incorporando e aplicando nas nossas páginas HTML, até a próxima aula.
