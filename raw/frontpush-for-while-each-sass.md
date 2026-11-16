# Estruturas de repetição no Sass: @for, @while e @each

Opa, então, pessoal, sejam bem-vindos a mais uma aulinha de Sass, onde a gente está percorrendo os principais fundamentos e principais funcionalidades desse pré-processador, onde, na aula de hoje, nós vamos conhecer um pouco sobre estruturas de repetição.

Eu acredito que, se você já estudou alguma linguagem de programação, seja ela C, seja ela JavaScript, seja ela PHP, você já se deparou com essas estruturas aqui, que é o for, o while, o próprio do while e o each, ou forEach, para poder percorrer o mesmo loop, só que em arrays, em estruturas de vetores e tudo mais, tá bom?

Então, nós vamos conhecer um pouco mais de como a gente estabelece, qual é a sintaxe que a gente escreve no Sass para poder a gente obter esse recurso, para poder dar mais possibilidades, e de forma mais organizada, concisa e compacta, aos nossos mixins e funções aqui no Sass.

Lembrando que uma estrutura de repetição nada mais é do que são sequências de códigos que estabelecem como se deve repetir a cada loop, como se deve ser a estrutura para poder, em um pequeno bloco de código, fazer a configuração de várias extensões, por exemplo, quando a gente for construir grids. Não se preocupe, que eu vou explicar nessa aula.

## A sintaxe do @for

Enfim, essa aqui é a estrutura, a sintaxe do for, e eu vou estar apresentando vocês a do while e do each, não se preocupem, para poder a gente conhecer um pouco mais de como funcionam essas estruturas, onde basicamente tem a variável que a gente estabelece, como ela começa, como ela modifica e como ela termina.

No caso aqui do for, não tem um caráter muito, muito rebuscado, por exemplo, de controle, que a gente vê em linguagem de programação. Aqui, literalmente, a gente vai ver que ele modifica de 1 em 1, sempre de mais 1 em mais 1, e agora a gente estabelece de onde ele começa, from 1.

Então, a variável i que eu estabeleci aqui, que pode ser qualquer variável, é utilizada o i, o j e o k, simplesmente puxando um pouquinho da matemática, que são índices de matrizes, e é muito utilizada essa sintaxe, mas poderia ser qualquer variável, onde a gente estabelece o começo dela, from 1, ou seja, ela vai começar do 1, through, é meio que do inglês, vem "através de", ou então "de um lado até o outro", pode significar isso, até o 12.

E aqui dentro eu coloco a estrutura que será repetida. No caso, eu estou colocando aqui grid- e estou colocando o i dentro de uma hashtag, porque o Sass não entende que eu quero que aqui seja reproduzida a variável, e não o $i. Se eu simplesmente colocar $i, como ele não está estabelecido dentro de uma propriedade, ele vai meio que reproduzir grid-$i na repetição, e não é isso que eu quero.

Então, para forçar que o Sass entenda que eu quero que ele me mostre o valor da variável i naquele momento do loop, para poder gerar grid-1, grid-2, eu coloco ele entre chaves e uma hashtag aqui, simplesmente isso, a gente vai ver isso aí. E aí ele faz uma determinada conta: quando é o grid-1, qual é o tamanho do grid? Aí eu coloco 72 pixels, que é o tamanho de uma coluninha de grid, por exemplo. Vou explicar para vocês como é que se dá a estrutura de grid também, não se preocupe. E ele vai multiplicar por 1, aí no próximo loop vai multiplicar por 2, por 3, e vai criar uma estrutura de grids para mim no CSS.

## A documentação

Então, sem mais delongas, vamos para o código, onde eu vou demonstrar para vocês. E já abri, já deixei aberto, indico vocês demais a sempre estarem verificando a documentação do próprio Sass, onde você vem em At-Rules e em Flow Control, onde tem a estrutura de if e else, aí tem as estruturas de repetição, que é o each, o for e o while.

Então, olha só um outro exemplo do for no próprio Sass, onde ele estabeleceu a variável i, está vendo? Até o 3, deixa eu dar um zoom aqui, e colocou a propriedade de 3n mais a variável aqui. E aí, se você quiser ver a tradução de como fica isso aqui no Sass, ele traduz assim: 1, 2 e 3, ou seja, a variável i está só aqui, vai 1, 2 e 3.

Mas, olha só, ele aplica uma outra função básica do próprio Sass. Isso aqui é uma função do próprio Sass, onde você coloca uma cor e modifica a porcentagem dela, de quanto você quer deixar em um tom mais claro ou um tom mais escuro, e aí ele gera os hexadecimais para você, de acordo com a posição do elemento na lista. Então, basicamente, ele está falando que, a partir do terceiro elemento da lista, mais 1, você coloca essa cor; mais 2, essa cor; mais 3, essa cor, está bom?

Então, essa aqui é a sintaxe. Esse aqui é um exemplo da aula passada, salvo de engano, onde a gente modificava o valor aqui para light, e aí ele modificava aqui, por meio de estruturas encadeadas, ou você mudaria para dark e ele modificaria o texto e o background-color, está bom?

## Por que um sistema de grids

Então, um pequeno exemplo, pessoal, para a gente começar aqui, é eu criar uma estrutura de grid, está bom? "Ah, Násser, o que significa essa estrutura de grid? Tenta explicar para mim em primeiro", está bom?

Então vamos lá, eu vou vir, por exemplo, aqui no próprio set da Nubank, onde, lembra, que os grids são de suma importância para poder a gente alinhar os nossos elementos e distribuir o conteúdo, e até facilitar na responsividade, de forma que, quando a gente aplique, por exemplo, os grids aqui, eu consiga estabelecer qual é a ocupação de conteúdo.

Então eu posso, por exemplo, criar um div, um bloco aqui, onde eu vou colocar ele vermelhinho com 30% de opacidade. E aí eu coloco esse bloco aqui, e ele está ocupando um, dois, três, quatro, cinco grids. E aí, quando a gente vai traduzir isso para o código, talvez fique um pouco complicado, porque, por exemplo, utilizando flexbox, a gente precisa estar utilizando o flex grow, e aí a gente vai verificando no olho de como tem a divisão. Então não é uma divisão muito exata, mas a gente, com o olho, consegue ter uma boa aproximação.

Já se a gente criar um sistema de grids, a gente pode literalmente ser bem mais fiel ao layout projetado, que eu vou mostrar para vocês como é que eu faço esse sistema de grids nas próximas aulas, meio que isso aqui explicando a estrutura de repetição que eu faço para poder utilizar.

Mas olha só: eu utilizo um, dois, três, quatro, cinco grids, e a gente tem um tamanho de div de 576 pixels, enquanto aqui eu estou utilizando um, dois, três, quatro, cinco, seis, sete grids, dando um total de tamanho de 816 pixels. E, quando a gente vai traduzir o layout para o código, como eu disse, fica um pouquinho complicado. Mas, quando a gente sabe implementar o sistema de grids, pegando agora pela distância e ele construindo com base no tamanho da sua tela, fica mais fácil e fluido a responsividade seguindo esse método.

E aí, literalmente, eu preciso criar várias classes de grids estabelecendo os tamanhos específicos. Então eu posso muito bem fazer .grid1, e o meu conteúdo de classe tenha o tamanho de um grid. Qual o tamanho de um grid? Um grid tem o tamanho de 96 pixels. Então eu venho aqui e coloco o width 96 pixels.

Eu quero que o meu conteúdo estabeleça um tamanho de dois grids, então eu faço o quê? 96 mais 96, porém tem o gutter. Então eu preciso também de uma continha para poder colocar o gutter aqui entre eles. Então, no caso, ficaria o quê? 216 pixels. Então eu viria aqui e aplicaria 216 pixels, e, quando eu quisesse utilizar esse tamanho de grid 2, eu aplicaria a classe grid 2.

Mas você percebe que eu preciso fazer isso de 1 até 12, porque é o padrão que eu utilizo, são 12 colunas. E, se eu precisar modificar alguma coisa, eu tenho que sempre vir aqui e modificar na mão. E aí a gente pode utilizar a estrutura de repetição para poder facilitar isso. Mas meio que estou dando spoiler aqui das próximas aulas de prática, mas é para vocês entenderem o contexto de por que e como eu utilizo essa estrutura de grids aqui, utilizando estrutura de repetição for, while ou each no próprio Sass.

## O @for na prática

Então vamos lá. Se eu fosse criar, deixa eu dar um zoom aqui, eu criaria for e a variável i, que vai rodar from 1, estou falando para ele que comece do 1, e coloque through 12. Então ele vai executar o loop começando do 1 e indo até o 12, então 1, depois 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. E aí, o que eu posso fazer?

Eu posso colocar, por exemplo, de maneira bem simples, sem considerar o gutter, só para vocês entenderem, eu posso colocar aqui o width, coloco o tamanho de uma coluna de um grid, 96 pixels, e multiplico ele pelo índice, que ele vai estar modificando de 1 a 12. E, dentro dele, eu faço um grid, uma classe chamada grid, onde eu tenho que colocar o valor da variável e colocar esse width aqui dentro. Então, Ctrl X, Ctrl V.

Ele vai dar erro, porque ele não identifica isso aqui como uma variável, então ele está considerando como se fosse uma label. Então, se eu vir aqui em salvar, olha só o problema que ele vai me dar, olha como ele vai gerar o grid, está vendo? Com $i.

E aí, para eu forçar que ele me mostre não o $i, mas o valor da variável $i, eu abro uma hashtag, abro chaves e fecho chaves. Isso aqui é o mesmo artifício que a gente, por exemplo, utiliza no JavaScript, quando a gente quer concatenar e forçar que o valor da variável seja mostrado, e não a variável em si. E aí, quando eu salvo, ele já está gerando agora grid 1, 2 e 3, e olha só, ele já está fazendo a multiplicação, está vendo?

Então ele está gerando do 1 ao 12, vocês podem ver aqui. Não estou levando em consideração o gutter, porque eu precisei de uma continha um pouquinho, levando em consideração a margem e tudo mais, que a gente vai fazer na aula prática, mas eu queria demonstrar para vocês como é que se dá, como é que funciona essa estrutura de repetição.

## O @while

Agora, falando um pouquinho sobre o while, pessoal, não muda a ideia, ela é bem próxima. E nós temos aqui, por exemplo, um exemplo de utilização do próprio while dentro de uma função, que é o próximo tópico que a gente vai estar utilizando, que também tem como construir.

Mixins é uma coisa e funções é outra. A função tem por característica trazer algum tipo de retorno, já o mixin eu posso simplesmente dar um include e ele vai puxar todo o código do que eu escrevi para outro lugar. Já a função precisa retornar um valor, basicamente é essa a diferença.

Então eles colocaram aqui uma função chamada scale-below, onde ela tem como parâmetros 3, value, base e ratio, onde o ratio tem como valor base 1.618. Então já estou relembrando com vocês algumas propriedades: enquanto o valor que você está me passando nesse parâmetro for maior que a base, faça isso com a variável value, então divida a value pelo ratio e retorne value.

Então, enquanto o valor que ele está passando nessa variável aqui for menor ou igual que essa variável aqui, ele simplesmente vai retornar o mesmo valor que você passou, não vai modificar absolutamente nada. Agora, quando você passar o valor que seja maior que o de base, ele vai modificar esse valor pelo ratio, dividindo o valor pelo ratio.

Então vou abrir aqui a calculadora, só para poder ficar mais claro de o que retornaria dessa função aqui utilizando o while. Lembrando que você também pode estar utilizando operadores. Você percebe que o for sempre está falando de um lugar até outro, e aí você sempre está somando, e aí vai 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. Então ele é mais sequencial. E aqui, que a estrutura do for é mais sequencial, já do while ele te traz mais algumas possibilidades, porque tem como você comparar enquanto um é igual ao outro, então é meio que um if encadeado aí dentro.

Sendo que você também pode colocar um if aqui dentro, se eu quero continuar utilizando for: aí você coloca um if aqui dentro, faz alguma comparação, abre e fecha chaves, e aí vai funcionar como um while. São estruturas diferentes, mas cada uma tem mais ou menos a sua finalidade.

Então, abrindo aqui essa calculadora, vamos supor que eu colocasse como valor 10 e como base 8, aliás, como base 12. Então vamos primeiro ao primeiro exemplo, nesse quesito aqui, e vai simplesmente retornar 10, concorda comigo? Agora, se eu vir aqui no valor e colocar 16: 16 é maior que 12 da base? Sim. Aí o que ele vai fazer? 16 dividido por 1.618. Então você vai fazer 16 dividido por 1.618, e aí ele vai me retornar esse valor aqui como valor da função.

E olha só a tradução para o CSS: ele está me voltando esse valor de font-size, aplicando essa função scale-below, onde ele passou 20 e 16. Por que foi 20 e 16? Ele vai perguntar: 20 é maior que 16? Sim. Então ele vai pegar 20 e dividir por 1.618. Então vamos lá, 20 dividido por 1.618, 12.36, que é justamente o valor que está aparecendo aqui.

## O @each

A estrutura de repetição é o each, que, como eu disse nas primeiras aulas, ele é mais utilizado para quando você está extraindo ou querendo percorrer dentro de um array. O que é um array? Literalmente é um vetor com vários valores dentro.

Então, olha só, ele criou uma variável com o valor 40, com o valor 50 e com o valor 80, e aí ele utilizou each size in sizes, e ele criou essa variável size para ela rodar nos sizes. Lembrando que sizes é o vetor grande, que contém todos os tamanhos; size ele colocou no singular, está vendo?

Então ele vai pegar e vai rodar com 40, na segunda vez ele vai rodar com 50 e na terceira vez ele vai rodar com 80. Ele vai simplesmente rodar nos valores que já existem da estrutura de repetição. Então ele vai criar um ícone do tamanho 40, com font-size 40, com height 40 e com width 40. Depois ele vai rodar no segundo valor do array, aliás, quase que não me vem a palavra, e aí ele vai rodar ícone-50, está vendo? Com font-size 50, com height 50 e com width 50. Na mesma forma, 80. Então, olha só como ele plotou o CSS, está vendo? Icon 40px, 40px, 40px, 40px, icon 50px, 50px, 50px, icon 80px, 80px, 80px.

Da mesma forma ele faz com ícones. Lembrando que esses ícones, você pode colocar um dentro do outro. Por exemplo, o barra F112 representa um ícone em uma tabela pré-estabelecida, então não fique pensando que isso aqui é coisa de outro mundo. O barra F112 é um ícone de olho, o start, o F112e é um ícone de start, como se fosse um ícone de start, ou de play, e o F112f é um ícone de stop. E ele organizou isso aqui na variável de ícones, mais um aspecto das variáveis, que é sempre bom a gente estar utilizando e vendo a documentação para poder a gente descobrir mais funcionalidades de como declarar variáveis.

E simplesmente ele faz o quê? Name e glyph, ou seja, name é o nome do ícone, glyph é o código do ícone. E ele está abrindo e lendo todos esses valores no vetor icons, que é o que contém o array, esse aqui é o array que contém todos os valores. E ele está colocando o quê? icon-name, before, para quando você aplicar essa classe name, o font-family vem com o content do código do ícone.

Então, olha só como acontece no CSS: icon-eye, está vendo? Before, ou seja, eu vou aplicar o ícone eye quando eu quiser aplicar o ícone. E olha só, o content vai aplicar barra F112 quando for o olho; quando for o start, ele vai aplicar o barra F12e; e, quando for o ícone de stop, F12f, ele vai aplicar isso aqui.

Então, bons exemplos para podermos descobrir como funciona essa estrutura de repetição. E eu deixo essa aqui para vocês também descobrirem, mas ela segue exatamente a mesma coisa, só que escrita o vetor de maneira diferente, mas segue o mesmo raciocínio.

## Resumo

Então, só para podermos relembrar, são três estruturas de repetição utilizadas aqui no Sass. O for e o each são mais sequenciais, sendo que o each roda em um vetor sem precisar você estabelecer nada: você colocou o vetor, ele já vai rodar naquele vetor automaticamente, dentro de um array de valores, que é um vetor. O for é um pouquinho mais sequencial, onde você tem que estabelecer como ele começa e como ele termina. Nada impede de você, por exemplo, começar do 5, aí ele vai plotar só do grid 5 até o grid 12, e ele é mais sequencial. Enquanto o while, você consegue colocar algumas comparações para poder ele fazer essa estrutura de repetição: enquanto algo estiver diferente de outro, você consegue funcionalidades a partir disso.

Beleza, pessoal? Então, essa aqui é a aulinha de estrutura de repetição, onde a gente vai utilizar esses conceitos para poder construir a nossa estrutura de grids um pouco mais para frente, beleza? Falou, pessoal, até a próxima!
