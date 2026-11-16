# Flexbox, prática 1: o layout do YouTube, do grid do design à estrutura HTML

Opa, fala pessoal, tudo certo com vocês? Vamos lá para as aulas práticas do Flexbox, pelas aulas onde eu vou colocar exercícios assim como esse aqui, com um design um pouquinho mais genérico, porque acredito que é mais fácil a gente estar reproduzindo e exercitando toda a teoria que a gente viu.

Então, eu estou propondo aqui o layout do YouTube. Vamos ver as skills, como é que a gente faz para poder analisar e literalmente passar para o código utilizando apenas Flexbox para esse tipo de exercício aqui, tá bom? Então, está aqui o nosso layout: a gente vai fazer a parte do menuzinho e depois a parte do conteúdo. Vamos lá, fechou?

## O grid do design

Primeira coisa, pessoal, é que esse design aqui eu apliquei um grid, um grid de 1440p. O que significa isso? Se você não sabe, dá uma olhadinha nas aulas de grid para você entender por que é importante a gente estabelecer o layout dessa forma aqui, estabelecer alguns padrões que a gente consegue passar para o código de maneira mais fácil, tá bom?

Mas em base, o que eu fiz? Coloquei aqui um grid de, deixa eu ver aqui as informações, 96px, 12 colunas, padrão de desktop, 96px cada coluna, e um gutter, ou seja, um espaço entre as colunas de 24px, e estabeleci a partir daí, tá bom? Isso aqui vai servir para poder a gente definir o container, e a soma da distância de tudo isso aqui dá próximo de 1440px, que é um bom padrão para poder a gente estar utilizando e construindo os nossos layouts, tá bom?

## Desenhando a estrutura de divs: o menu

Então vamos lá, sem mais delongas: como é a estrutura de divs que a gente precisa se atentar quando a gente está codando esse tipo de projeto aqui. Então eu vou pegar aqui uma div vermelhinha e voltar traçando para poder a gente entender como é que vai se dar primeiro a estrutura HTML, para depois a gente codar estilizando da melhor forma possível.

Então eu vou traçar aqui uma div maior, que literalmente pega nessa parte preta. Pode ver que o nosso menu tem um fundinho preto, está vendo? Se é um fundo diferente desse fundo aqui, eu preciso colocar uma div, então literalmente vai ser uma div de ponta a ponta, onde vai estar englobando todos os elementos. Vou colocar aqui dessa forma aqui, tá bom?

Depois a gente vai perceber que dentro a gente tem a estrutura de container, tanto no conteúdo como no menu. Então a gente vai precisar de outra div englobando e alinhando o conteúdo, então vai ficar uma div bem aqui, englobando o conteúdo central, literalmente centralizando o nosso conteúdo. E vai ter outra div filha, que literalmente aí sim ela vai ser uma div para a nossa logo, a nossa estrutura aqui, então vai ter uma div aqui e uma outra div aqui do outro lado, englobando o menu.

Então presta atenção aí: é uma div, dentro dessa div, dentro dessas duas aqui, essa aqui vai ser a estrutura HTML que a gente vai estar adotando. E aí, dentro dessa lista aqui, eu posso colocar mais três, literalmente são os itens das listas, que são os links, então mais um, mais esse e mais esse. A partir daí a gente vai construir o nosso layout.

## Desenhando a estrutura de divs: o conteúdo

Segunda parte é mais voltada para o conteúdo. A gente vai aplicar mais ou menos a mesma regrinha: a gente vai ter aqui uma div container, deixa eu copiar e colar aqui que fica mais fácil, a gente vai ter uma div container compreendendo 1440p de largura, centralizado, onde vai englobar todos os itens.

Como em flexbox a gente sempre pensa em linhas, a gente vai dividir primeiro aqui em duas colunas: a gente tem a coluna do conteúdo principal do vídeo e aqui dos vídeos sugeridos. Mais uma vez, a gente vai colocar uma outra div aqui no meio, onde vai estar englobando esse conteúdo aqui. Dentro desse aqui a gente vai ter mais duas divs: literalmente vai ser a div para englobar a parte da imagem e outra div para poder englobar essa partezinha do texto. E eu vou até mudar de cor, vou colocar uma azul para a gente enxergar essa parte da melhor forma possível.

Então basicamente essa é a estrutura, espero que vocês estejam entendendo como eu estou desenhando. Uma outra div maior vai englobar todos os itens dos vídeos sugeridos, ou seja, daqui até aqui, vou mudar a cor mais uma vez também para a gente visualizar, e mais uma div para cada elemento em específico. Deixa eu diminuir aqui, e vai ter mais uma div para cada elemento em específico, deixa eu colocar em rosa, não, em verde, para cada elemento em específico. E aí dentro eu tenho mais duas divs, que vai ser uma div para a imagem, para o vídeo em si, onde tem essa thumbnail do vídeo, e para a descrição do vídeo. Então essa é a estrutura HTML de divs que a gente vai estar aplicando para poder o Flexbox sair bem fácil.

## Preparando o projeto

Sem mais delongas, eu abri o meu VS Code, criei uma pastinha chamada Flexbox aula, onde a gente vai criar tudo do zero: index.html, para poder estar codando, e uma pastinha CSS com um arquivo style.css lá dentro também. Vamos colocar a estrutura HTML5, vou dar um zoom aqui para poder melhorar a visualização, e também vou linkar o meu arquivo CSS, link css, css barra style.css, para poder encontrar o nosso arquivo, e vou abrir isso com o Live Server, para vocês estarem acompanhando junto comigo.

Então vamos começar a codar. O fundo está preto por causa do tema do Google Chrome. Não é porque eu já apliquei e não dá para entender, é porque o próprio Google Chrome força o tema escuro, então aqui, como era branco, ele ficou preto, mas eu vou estar forçando, só para poder modificar.

Padding, margin: a gente zera os primeiros itens, para poder facilitar quando estivermos aplicando, e coloca sempre o border-size em border-box. Juntamente vou colocar o body, vou deixar ele sempre tela inteira, então vamos colocar o width 100% e um height de 100vh, para poder forçar e ficar em também da tela. Vou colocar uma borda 5px solid green, só para vocês visualizarem se está funcionando perfeitamente.

Vou colocar um background-color claro, só para vocês verem, white. Quando coloca o white, o sistema dark do Google Chrome força, mas está funcionando perfeitamente, só para poder mostrar para vocês. Se eu colocasse, por exemplo, black, acredito que ele vai mudar: ele força apenas os temas claros a converterem para o escuro. Então vamos colocar aqui um a1a, que é o pretinho básico que a gente sempre está utilizando nos nossos projetos, mas eu estou tendendo a escurecer um pouco mais, eu sempre estou colocando agora 0c, 0c, 0c. Enfim, o nosso CSS já está funcionando.

## A estrutura HTML do menu

Sem mais delongas, vamos construir a estrutura HTML para poder fazer o nosso projetinho. Então vamos lá, primeira parte é construir essa estrutura do menu, então sempre utilizando HTML semântico. Então vou colocar aqui um header, onde esse header vai ser a div pegando de ponta a ponta. Aqui dentro eu vou construir uma div de navegação, onde eu vou chamar ela simplesmente de nav, e vou construir uma outra div aqui, onde eu vou dar o nome dela de nav-logo, portanto chamada de nav-menu, bem intuitivo.

Dentro da parte de nav-menu eu vou desmembrar e vou colocar uma lista aqui dentro. Aliás, vou fazer dessa aqui uma própria lista, e aí dentro de uma lista eu vou colocar os li, que são os itens, onde eu posso estar colocando aqui li.nav-item, para poder sempre ficar intuitivo. E você constrói uma árvore, essa aqui é uma boa prática, onde você constrói uma árvore de classes: se a pai é nav, a filho faço nav, traço, o nome dela, bem específico e intuitivo, que indique qual é o item que eu estou de fato codando.

Então vamos lá, nav-item, e aí eu posso colocar também um link aqui dentro, onde eu faço nav-link, e a gente está codando. E aí simplesmente eu vou colocar aqui produtos, o nome do link, produtos. Vou dar um enter aqui para poder a gente visualizar da melhor forma possível: produtos, sobre e contato, sobre e contato. Então já está aparecendo os nossos itens. A outra parte a gente vai estar codando, a gente vai estar estilizando, mas os itens já apareceram.

## A estrutura HTML do conteúdo

E agora a gente precisa de fato colocar a estrutura HTML do menu. Então vamos lá, eu vou colocar aqui o section.container. A gente vai definir essa classe container, onde, lembrando, nós temos duas estruturas maiores, essa aqui e essa aqui. Então vamos colocar aqui, div, eu posso colocar item1, item1, que é o item do container, ou simplesmente container-item1 e container-item2, onde o container-item1 vai compor na parte do vídeo principal aqui, item2, os vídeos sugeridos.

E dentro dele eu tenho qual estrutura? Do item1, eu tenho duas divs, concordam comigo? A div para texto, as divs aqui para texto e descrição, e também a div do vídeo em si. Então eu posso colocar div video-main, e posso colocar simplesmente a descrição direto. Posso colocar aqui uma h3, título do vídeo, do vídeo, quase que não sai, e aqui uma breve descrição do vídeo escrito 5000 visualizações há um mês.

E a parte dos outros vídeos são a parte dos vídeos sugeridos em si, o container-item2 aqui, onde eu posso colocar o vídeo. Container-item2, eu posso colocar uma div com o nome de vídeo sugerido, e eu vou colocando todas essas divs aqui, onde aqui eu vou colocar o primeiro elemento, onde vai ser div vídeo. Aliás, eu vou fazer melhor: eu estou colocando aqui português junto com o inglês, isso aqui não é legal. Eu vou colocar video-side, que é a parte aqui do lado, então o video-side, onde isso aqui é cada item. E aqui eu vou colocar como div thumb, que é a thumb do vídeo, e por final a descrição, onde eu posso colocar título do vídeo, só que aqui com um tamanho menor, vou colocar com h4, e aqui um parágrafo.

Então basicamente essa aqui é a estrutura HTML que a gente vai estar codando, e vou colocar aqui vários itens para poder a gente estar visualizando. Então, na próxima aula, pessoal, a gente vai estar agora codando, estilizando toda essa parte aqui. Até a próxima.
