# Grid system com Sass (parte 1)

Opa, olá, pessoal, tudo certo com vocês? Sejam muito bem-vindos às aulas práticas de Sass, onde eu vou estar mostrando como eu utilizo o Sass no meu dia a dia, nas minhas aplicações, e literalmente as bibliotecas que eu uso no meu dia a dia na construção dos meus websites.

E, na aula de hoje, pessoal, é uma das aulas mais importantes, porque é uma aula que eu vou falar sobre responsividade, não utilizando o Flexbox ou o Grid Layout, que são dois recursos maravilhosos do próprio CSS, que permitiram e deram infinitas possibilidades para a gente construir diversos layouts diferentes. Mas eu vou falar hoje sobre o sistema de grids que eu utilizo nas minhas aplicações, que é muitíssimo parecida com o Grid System do próprio Bootstrap.

Não sei quem conhece o Bootstrap, é uma das, se não a maior framework CSS, mais difundida e tudo mais, que tem justamente esse sistema de grids, de quebras e tudo mais, linhas e colunas, para a gente estar conhecendo, onde eu construí essa aqui. Então eu vou demonstrar aqui para vocês como se dá.

Ele tem um grid fixo que você estabelece. Esses são os containers, onde você coloca o seu conteúdo e consegue dividir: coloca cinco grids para esse primeiro div, sete para esse, para poder completar o padrão de 12, que a gente sempre estabelece lá nos nossos layouts, e é o que eu costumo mais utilizar. Por exemplo, 3, 3, 3, ou então 4, 4, 4, e literalmente você pode dividir da forma que você quiser.

E, quando você aplica aqui a responsividade, ele se torna fluido em determinada resolução para poder apertar, e você define o breakpoint para poder ele quebrar um embaixo do outro no sistema responsivo, para poder virar em colunas e ter essa versão para celulares, para tablets e tudo mais.

Então nós vamos ver, desde o começo, quais foram os princípios, qual foi a conta que eu utilizei e como eu utilizei os recursos do Sass para poder construir essa biblioteca aqui. Se eu não deixar na descrição, por favor, reclame, me chame a atenção para eu deixar esse arquivo aqui como anexo para vocês utilizarem nos projetos de vocês.

## O layout do Nubank com Flexbox

Mas, antes de eu começar de fato a demonstrar o código, eu queria vir aqui, pessoal, no próprio exemplo da Nubank, que eu vinha dando esse mesmo exemplo para vocês, onde o projeto do Nubank eu desenvolvi com o Flexbox, correto? E, quando a gente precisava layoutar com o Flexbox os trechos do nosso website, o que a gente fazia?

A gente vinha aqui, desenhava uma div. Essa aqui é a div, eu vou colocar até em uma cor diferente aqui, vou colocar em uma cor azul, indicando que isso aqui é uma div de bloco de código. Então você circunda esse conteúdo de título, de texto, de botão aqui dentro dessa div para poder ela quebrar. E aí eu coloco esse outro trecho aqui, onde vai a ilustração.

E no site da Nubank essa estrutura de responsividade se repete, onde literalmente a gente tornava o sistema fluido em determinado tempo, em determinada seção. Então deixa eu até acessar aqui e demonstrar para vocês, só vir aqui, barra Nubank, vocês vão ver como se dá a responsividade do site.

Então nós temos uma pequena div aqui, outra div circundando a ilustração, da mesma forma aqui, e olha só o que acontece: vocês vão perceber que, em determinado momento, ele se torna fluido, ou seja, a div que circunda o conteúdo diminui até chegar no breakpoint específico que foi estabelecido, e ele quebra um em cima do outro.

Isso aqui é um sistema básico de responsividade, só que eu utilizei flexbox, não utilizei grid layout, vocês lembram disso? Se vocês não viram, por favor, vá lá na seção de codificação, nas primeiras aulas, onde eu demonstro como eu construo o layout desse site só utilizando o flexbox.

Você sabe que, quando você está construindo via flexbox, tem a propriedade do flex-grow, que você vai dizer para uma div ou outra o quanto ela cresce com relação a outra. Você sabe que nós temos um determinado container, que eu posso vir aqui e desenhar um container. Container é aquela div que engloba todas as divs filhas, se é que eu posso dizer assim. Eu vou colocar aqui em uma cor verde, também com 30%. Então essa aqui que eu desenhei de verde é a minha div container; dentro dela tem essa div azul, que comporta esse conteúdo, e tem essa outra div azul, que comporta a minha ilustração.

Quando eu aplico as propriedades display flex, automaticamente os filhos direto, que são essas duas aqui, se tornam flex-items, lembra disso? Isso aqui tudo é revisão de flexbox. E aí, quando eu defino um flex-grow, ou seja, um crescimento, grow vem de crescimento do inglês, maior para essa div do que para essa, automaticamente essa aqui vai ficar maior que essa. Mas o quanto maior?

Na maioria das vezes, quando a gente está desenhando um layout, ele se aproxima do layout que foi projetado. Então, sei lá, eu defino um flex-grow 2 para esse e 1 para esse, eu verifico a responsividade e vejo no olho mesmo, comparando se está se aproximando do layout que foi projetado. Então foi feito dessa forma aqui nesse site. Você pode ver que ele se aproxima, ele se aproxima, mas não tem a exatidão e precisão que, por exemplo, o sistema de grids traz para a gente.

## Por que um sistema de grids

Você percebe que, quando a gente está definindo no flexbox, a gente não fala: "eu quero que, no tamanho normal de Full HD, ele tenha 816 pixels de tamanho essa seção, e eu quero que essa tenha 576 pixels de tamanho". Ou então: "eu quero que essa div tenha o tamanho de um, dois, três, quatro, cinco grids, e eu quero que essa div tenha o tamanho de um, dois, três, quatro, cinco, seis, sete grids para poder completar os 12".

Ou, se eu fosse fazer uma estrutura aqui no Nubank, onde eu quero que disponha alguns itens aqui, e eu quero um quadradinho compondo três, outro compondo mais três, outro compondo mais três, outro compondo mais três. Dá para fazer isso aqui com o flexbox? Lógico que dá, absolutamente, porque todos têm o mesmo tamanho: eu coloco ele dentro do grid, e vai ter o mesmo tamanho do container, e eu dou o mesmo flex grow para cada um deles.

Mas só que, com o sistema de grids, a forma de como eu construo o layout com base nesses grids que a gente está fazendo aqui, eu estou fazendo essa alusão para vocês, se torna mais fácil, porque eu posso simplesmente desenhar uma div e falar: "olha, eu quero que essa div tenha o tamanho de X grids", que são essas colunas, o tamanho dessas colunas aqui, levando também em consideração o gutter.

Porque, como eu disse para vocês lá na aula de grids, lá no UI Design, se vocês não viram, dê uma olhada lá, onde eu falo sobre os padrões que a gente utiliza na web, e o padrão que eu mais utilizo é o 1.400, aquele que se aproxima da resolução de 1.400 de container, porque eu consigo abraçar tanto resoluções maiores quanto resoluções menores. Lembrando que tem todos os tamanhos dos dispositivos, que é bom a gente lembrar. Então é essa aulinha que vocês têm que dar uma olhada, a aulinha de grids, onde eu falo aqui os breakpoints dos dispositivos, então PCs, desktops e tudo mais.

## Por que o container tem largura máxima

E muita gente até me perguntou: "Ah, Násser, por que você, por exemplo, não adapta ao tamanho da tela e está tudo bem? Não fica definindo grids ou containers de tamanho fixo, um tamanho máximo fixo, e depois ele fica fluido. Por que você não simplesmente aplica na tela inteira?"

Por um simples motivo, pessoal: se vocês verem aqui no Google e digitarem "monitores 21 por 9", por exemplo, que eles fogem do tamanho widescreen, que é o tamanho padrão, 16 por 9, que a gente mais segue, vocês vão perceber que esses monitores aqui são mais retangulares. Eles estão no padrão 21 por 9, não é o 16 por 9 que comumente a gente utiliza. Então, se eu fosse fazer ele fluido, ele iria esticar em toda a tela.

Então, como o nosso objetivo é sempre abraçar a maior quantidade de dispositivos, esse aqui é um exemplo de por que eu utilizo os containers com tamanho máximo fixo e depois ele se torna fluido: por que abraça a maior quantidade de telas, para poder a gente ter essa compatibilidade.

## O princípio: largura em porcentagem

Então, sem mais delongas, esse é o contexto, e nós vamos construir grids com base em width. Então, qual vai ser o princípio? Eu tenho aqui o container, onde cada coluna tem 96 pixels, cada gutter, que é o espaço entre eles, temos de 24 pixels, e, quando eu faço 12 colunas com esse espaçamento, nós temos um container com o limite máximo de 1416, por volta desse valor. Você pode diminuir depois, não tem nenhum problema, nós vamos fazer no Sass de forma que a gente coloque isso tudo em variáveis e você possa modificar, mas esse é o padrão que eu mais utilizo.

E aí nós vamos construir as divs. Por exemplo, vamos supor que eu estou desenhando essa div aqui: quantos por cento é esse tamanho com relação ao tamanho grandão do nosso container aqui? Então o nosso container é verdinho, e eu me pergunto: quanto por cento desse aqui é desse grandão, para poder definir o tamanho? Então o sistema de grids se baseia com relação ao width em porcentagem, para poder justamente o nosso sistema ficar fluido dessa maneira aqui. Ele aperta em determinada seção, e a gente tem maior controle e maior exatidão em a gente passar. Então é uma das formas da gente construir responsividade com websites.

## O mixin responsive e o container

Então, sem mais delongas, vamos lá. Eu vou apagar essas seções aqui e também vou apagar o style.css, e nós vamos aprender isso aqui do zero.

Então vamos lá. Muito dessas respostas, para vocês entenderem, eu explico com mais detalhes nessa aula aqui. Então é imprescindível você dar uma olhadinha nessa aula, lá na parte de UI design do scriptwd, onde eu falo sobre os breakpoints dos dispositivos, e aí eu defino containers de tamanhos diferentes.

Onde utilizando o mixin de media queries, é um dos recursos que eu mais utilizo. Quem deu uma olhada no projeto do Nubank com certeza viu eu aplicando isso aqui, onde eu defino um mixin com o nome de responsive, e eu passo aqui um device, um tamanho de tela que eu quero aplicar, onde xl eu chamo de extra large, são telas que são acima de 1440 pixels, que eu considero telas extra large. Eu defino com L as telas large, que estão em resoluções entre 1140 pixels e 1440 pixels.

Lembrando que, pessoal, esses números que eu estou te falando, se você pegar números próximos, 1200 ou então 980, não faz diferença, mas são boas divisões com base no próprio sistema de grids do Bootstrap, ele mesmo que estabeleceu esses padrões com base nesses números, e eu adaptei para mim nesses valores. As telas médias estão entre 960 e 1140, enquanto as telas pequenas podem ser consideradas abaixo de 960, e abaixo de 540, que é o extra small.

Então eu dividi por meio de uma estrutura if encadeada, que a gente já viu no Sass, essa estrutura em que, quando eu quero, por exemplo, aplicar um media query específico para resoluções acima de 1440, eu passo o parâmetro xl; quando eu quero estilizar especificamente as telas que estão entre 1140 e 1440, eu passo nesse mixin o device com o nome L, e ele vai aplicar um media query somente aqui dentro, utilizando os limites. Então eu basicamente fiz isso com todos esses intervalos, que facilita demais quando eu estou aplicando a responsividade.

Mas, na maioria dos meus websites, eu não utilizo esses aqui de cima, salvo para poder ter alguma exceção de um elemento ou outro. Na maioria das vezes, eu simplesmente aplico de 960 pixels para baixo, porque eu acho um bom breakpoint, 980 e tudo mais, que é os que eu tenho menos dor de cabeça. Eu simplesmente aplico daqui para baixo e está tudo certo.

Então você pode ver aqui que eu aplico media screen and um max-width. O que eu estou dizendo com esse max-width? Tenha um teto de 960 pixels, ou seja, de 960 pixels para baixo, leia o conteúdo que eu estou passando aqui com o arroba content. Se você não entendeu essa estrutura de mixins atrelada ao content, eu aconselho você a voltar ou nas aulas do Nubank, onde eu faço isso aqui na prática, onde eu já já vou fazer também, ou volte nas aulas teóricas e veja como esses dois aqui combinam muito bem.

Então, só esse código aqui que eu vou deixar pronto, e também vou deixar para download para vocês, não se preocupem. E nós vamos fazer aqui o nosso sistema de grids.

A primeira coisa que eu quero lembrar para vocês é que eu defini aqui uma seção chamada container, onde nós vamos estilizar ela. É sempre aquele container fixo que vai ficar no meio da tela, onde ele vai se tornar fluido, e aí eu posso colocar divs aqui dentro, que são justamente aqueles para poder compor o conteúdo, que são filhas diretas desse container aqui, onde a gente não vai utilizar nem flexbox, nem grid layout para poder construir esse sistema de responsividade.

Então vamos lá, vamos estilizar aqui a class container. A primeira coisa que a gente tem que definir é o max-width. O max-width eu posso definir aqui como container, que é a variável que eu defini aqui pelo próprio size de 1200. Você pode colocar 1400 ou também que você quiser, coloquei em variável justamente para poder ter essa vantagem.

Vou colocar aqui uma margin de 48 pixels em cima e embaixo desse container, e automático de um lado e de outro, para que ela sempre fique centralizada na nossa tela. Também vou dar um padding, um espaçamento interno de 48 pixels, e 16 pixels de um lado e de outro, para que o nosso container não fique colado na nossa janela.

Então vou salvar isso aqui, vou dar um border 1px só de red, só para poder a gente enxergar o nosso container. Então está aqui. Percebeu que ele já está fluido, está vendo? Já está no centro, está vendo? E aí nós vamos começar a construir a nossa estrutura a partir daí.

E aí, só para poder a aula não ficar muito extensa, eu vou deixar essa aula dividida em duas partes, onde a gente vai partir daqui na próxima aula, beleza, galera? Então, falou e até a próxima!
