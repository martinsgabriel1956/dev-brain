# A propriedade nesting (aninhamento) no Sass

Então, pessoal, vamos dar continuidade às nossas aulas sobre os fundamentos e principais recursos do Sass, onde, na aula de hoje, nós vamos ver um pouco sobre aninhamento, do termo aninhar do português, ou também nesting, mais um termo voltado ao inglês.

Basicamente, pessoal, isso aqui é um recurso que também eu havia demonstrado de maneira indireta nas aulas passadas, e vamos dar um enfoque maior aqui, onde nós temos a criação do efeito cascata do CSS com mais facilidade. Vou demonstrar para vocês, mas é basicamente isso aqui. Você pode estar emendando N cascatas, e a forma de como você coloca no Sass, que pode ser uma tag dentro da outra, facilita na identificação de qual elemento você está estilizando.

Então, basicamente, tem um nesting tanto de tags, que essa aqui, uma dentro da outra, essa estrutura aqui é muito utilizada, por exemplo, nos meus projetos, quando você vai criar algum menu, onde você cria aqui o menu, aqui os itens do menu e aqui os links do menu, sempre um debaixo do outro, um dentro do outro. E aí você pode fazer esse nesting tanto de tags, que é esse aqui, como de propriedades, que eu também vou demonstrar para vocês. Então, é um recurso simples, mas também que ajuda demais na identificação e organização do nosso código.

## Nesting de tags

Então, sem mais delongas, deixa eu demonstrar aqui para vocês esse processo. Vou construir uma estrutura, onde nesse ul eu vou, por exemplo, colocar uma lista; dentro dele tem os lis, que são o list items. List items, e aí, dentro de cada um deles, eu tenho o list link, se é que eu posso colocar assim. E aí eu vou colocar aqui link1, e aí nós vamos copiar essa estrutura aqui, vamos colocar aqui três links para poder a gente ver como estiliza esses caras utilizando esse recurso. Então, nós temos aqui os links já todos certinhos, e aí a gente vai começar a estilizar.

Primeira coisa, o list é como se eu estivesse utilizando o ul normalmente. Posso colocar aqui um border, um px solid red, somente para eu enxergar onde ele está, vou dar um padding de 16 pixels para poder melhor visualizar aqui, e vou dar um margin-top também de 16 pixels para poder ter espaço na nossa demonstração. Beleza.

Como é que eu faria, pessoal, se fosse, por exemplo, o CSS puro, CSS padrão, e eu quisesse estilizar apenas os lis que estão dentro dessa class list? Como é que eu faria? Eu declararia novamente o list e aqui colocava o li. Então, o que esse comando aqui do CSS está dizendo para mim? Ele está falando: estilize apenas as tags li que estão dentro da classe list. E aí sim, eu poderia colocar, por exemplo, um padding um pouquinho maior entre os elementos, apagaria as bolinhas do list-style none, e, por exemplo, colocaria uma borda, um px solid blue, só para poder a gente visualizar as modificações. Então, está aí.

E olhe só, usando o nesting: você percebe que esses dois elementos aqui, se tiver muitos elementos na sua tela, pode acabar confundindo se esse aqui é o mesmo desse. E, com esse recurso do Sass, você pode simplesmente abrir um li e jogar todo o conteúdo aqui para dentro. E aí eu venho aqui e apago, ele já vem tabulado, então facilita também a organização, a hierarquia visualmente, faz com que eu identifique isso aqui de maneira mais fácil.

E quando eu dou um Ctrl+S para salvar, nada se modificou, e você pode ver que no style.css ele cuspiu bonitinho essa estrutura. E isso, quando a gente tem vários arquivos, uma árvore de tags uma dentro da outra, facilita demais eu identificar, do que ficar copiando e colando um list e constrói aqui embaixo.

## O e comercial

Ou quando eu preciso, por exemplo, estabelecer um link, por exemplo, eu tirar aqui o text-decoration none. Você vai perceber que em links é muito comum eu não só mudar a cor dos links, então eu posso colocar aqui, por exemplo, branco nesses links aqui, mas também é muito comum eu estar utilizando os termos como hover.

Então, como é que eu faria se fosse no CSS eu fazer isso aqui? Eu teria que fazer o .list .li, a, hover, para poder escrever um elemento hover, para poder colocar aqui e dar essa resposta para o usuário que isso aqui é um item clicável.

E você percebe que, quando você faz essa estrutura de nesting, um dentro do outro, ele automaticamente dá um espaço, só que, no caso do hover, você percebe que ele é colado. A propriedade hover é colada no a. E quando eu preciso aplicar essa propriedade que é colada, que é grudada, eu preciso simplesmente dar um e comercial.

O e comercial está avisando para o CSS: "o que eu escrevi aqui, coloque colado dessa tag". Então eu posso simplesmente escrever o elemento hover dessa forma aqui, para, por exemplo, mudar a cor para pink. E quando eu passar o mouse aqui, você vai ver que ele já está mudando para rosa, porque eu coloquei o e comercial aqui, ele entendeu, e ele colou o elemento hover no a.

Da mesma forma se dá quando, por exemplo, eu tenho que aplicar alguma classe active em um determinado link. Por exemplo, quando eu estiver na página home, fica o home em rosa. Quando eu estiver na página de produtos, fica só o produto em rosa, para indicar para o usuário que ele está naquela página, e eu aplico uma classe active, ou até mesmo em um próprio menu responsivo.

Como é que eu faria? Vamos supor que eu tenho um link que é chamado a. É diferente eu fazer active, é diferente eu aplicar o CSS dessa forma do que o CSS dessa forma. O CSS dessa forma, o que ele está dizendo para mim? "Olha, aplique na classe active que esteja dentro do elemento a." Então ele vai todas nas tags de link a e vai procurar se tem alguma classe active dentro dessa tag e vai aplicar essas estilizações aqui.

É diferente de eu aplicar dele colado. Quando eu falo colado, ele vai procurar as tags de link, com a tag a, com a classe active, para poder aplicar essas estilizações. Então, a questão ou não de ter o espaço é importantíssimo no CSS.

E aí eu faço o nesting junto com o e comercial, que eu posso também facilitar demais, por exemplo, quando eu estou criando os elementos after ou elementos before em links, que eu utilizo demais para poder criar os efeitos. No próprio site da Nubank, eu utilizo o Sass dessa forma, e facilita demais a categorização.

Então eu posso, por exemplo, aplicar um content vazio aqui no before, só para poder gerar o CSS. E olha só o tanto de coisa que o meu CSS cuspiu, está vendo? Aqui é o list, list li, list a, list hover, list after. E olha só como ficou no Sass, bem encadeado, bonitinho, onde eu consigo entender mais assim, quando eu tenho muitas linhas em um arquivo muito grande. Então esse recurso facilita demais a vida.

## Nesting de propriedades

Então, isso aqui é o nesting de tags, só que eu falei que também existe o nesting de propriedades. Do que se trata isso?

Vamos supor que eu vou fazer um parágrafo, vou criar um parágrafo, e dentro do parágrafo eu vou escrever o login.y. Então nós temos aqui, e aí eu vou estilizar esse parágrafo aqui embaixo, vou colocar um color gray, aliás, cinza, para poder enxergar. Então está aí o meu parágrafo, onde tem como eu fazer o nesting de propriedades. Como assim?

Lembre-se que eu tenho a propriedade font, onde eu consigo meio que resumir todas as propriedades aqui dentro. Da mesma forma a border. Eu posso colocar o quê? border-width e colocar dois pixels, colocar border-color e colocar o red. Aplicou essa bordinha, mas eu posso resumir isso aqui tudo em um único comando, que é o comando de border.

Mas você percebe que todos esses comandos começam com border-, e tem várias propriedades do CSS que seguem esse mesmo padrão. Então, se eu quisesse, em uma linha só, resumir todos esses, eu simplesmente faria border 1px solid red, e aí ele aplicaria da mesmíssima forma.

Então, o nesting de propriedades é mais ou menos isso: se eu quiser aplicar esse border, eu vou abrir o border dessa forma aqui, vou abrir e fechar chaves, dentro aqui do Sass, e dentro desse border eu vou colocar style e vou colocar solid, e aí, por exemplo, color, eu vou colocar purple, e aí ele vai aplicar o nesting de propriedades para mim.

Não utilizo muito esse daqui, eu faço mesmo o de tags. Esse aqui eu não costumo utilizar muito, mas é um recurso que está aí, estou passando para vocês também.

Então essa foi a aulinha sobre nesting, recurso importantíssimo, que sempre está sendo utilizado na nossa programação do dia a dia, que facilita, é simples e tem tanto de tags como de propriedades. Então, falou, até a próxima.
