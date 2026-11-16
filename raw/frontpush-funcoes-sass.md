# Funções no Sass: @function e @return

Então, pessoal, vamos dar continuidade às nossas aulas de Sass, falando sobre os principais fundamentos e funcionalidades, onde, na aula de hoje, a gente vai falar sobre funções, um tópico recorrentíssimo, importantíssimo, que, quando a gente fala de linguagem de programação, não tem como a gente não falar sobre funções.

Então, se eu fosse definir para vocês o que seria: a criação de estruturas para reaproveitar códigos. Quando a gente percebe que algum tipo de funcionalidade, ou execução, ou cálculo, que você percebe que ele sempre está sendo feito de maneira recorrente durante o nosso código, e a gente pode fazer uma função para sempre fornecer parâmetros ou não, para que ele retorne o valor e a gente não precise ficar reescrevendo o mesmo código sempre ao longo da nossa estrutura. Então, torna versátil toda essa parte e traz otimização e produtividade para o nosso trabalho.

## Função × mixin

Então, o que eu queria dizer, pessoal, primeiramente, é que existe uma diferença de como a gente trata, por exemplo, função de mixin aqui no Sass. A função, como eu disse para vocês, é um bloco de estrutura, é uma criação de estrutura para poder reaproveitar código. É um bloco que retorna sempre um valor. Então isso aqui é importante: você vai ver que em toda função, pelo menos na grande maioria, não vou generalizar aqui, mas pelo menos na grande maioria das linguagens de programação, ele sempre vai retornar alguma coisa, vai fazer algo.

Já o mixin é literalmente um bloco de código que a gente escreve, e essas funções já são pré-definidas, onde você consegue, sim, fornecer argumentos para essa função, mas o que você faz no mixin é basicamente um Ctrl+C, Ctrl+V. Você estabelece aqui o nome do mixin, é um conjunto de pré-propriedades que você sempre vai estar aplicando, e aí você dá o include, onde dá um Ctrl+C, Ctrl+V.

Diferente da função: você percebe que ela vai fazer algum tipo de conta, algum tipo de cálculo, alguma verificação, alguma tomada de decisão que vai te retornar algo, seja um array, seja um valor, ele tem por essa característica. Já queria deixar claro a diferença de função para mixin.

## A sintaxe e a função grid

Se eu fosse falar para vocês a estrutura, a sintaxe seria essa aqui: arroba function, e aqui você vai colocar o nome da função. Eu coloquei grid para poder já ambientalizar vocês do que eu vou fazer e como eu vou utilizar esses recursos para construir uma estrutura de grids, que eu já falei na aula passada do que se trata. Então, se você não assistiu, corre e assiste lá.

Onde é que você fornece a coluna que você quer, o tamanho de grid da sua div, o total de colunas que você está utilizando, que na grande maioria é 12, porque é o padrão que eu utilizo, mas existem outros padrões, e aí ele retorna o valor da div considerando que eu queira, por exemplo, três grids. Se eu chamar essa função e dizer que eu quero três grids, ele vai me dar um width de 25%.

"Assim, eu não estou entendendo, como assim 25% corresponde ao tamanho de grid três?" Então eu vou vir aqui no meu Figma mais uma vez, vamos aqui no trecho do Nubank. Então vamos supor que eu queira traçar uma div com esse tamanho aqui. Então eu coloco vermelhinho, 30% de opacidade, e eu quero uma div desse tamanho aqui, de 576 pixels, mas que seja fluida.

O que é fluido? Você tem que entender que, quando a gente está trabalhando com responsividade, o caráter ser responsivo precisa ser adaptável e ele precisa ser fluido. Então o meu website foi desenhado, por exemplo, para resoluções de 1920 por 1080, são telas Full HD, mas tem, por exemplo, pessoas que utilizam o notebook com resoluções menores, por exemplo, de 1366. E aí o tamanho do meu grid de 12 colunas que eu estabeleci, você pode ver que ele tem 1416, e até para telas menores. Então o ideal é que ele aperte um pouquinho. Então pensa o seu grid como se fosse uma sanfona, em que ele vai lá e dá uma apertadinha para poder ir cabendo antes de quebrar para a versão mobile. Então ele precisa ser fluido.

Para poder ser fluido, ele precisa utilizar porcentagem, onde o tamanho do meu grid total é esse de 1416, e ele, por estar dentro do meu grid maior, ele ocupa um determinado tamanho, uma determinada porcentagem do container maior. E você pode ver que ele utiliza o quê? Um, dois, três, quatro, cinco grids. Cinco grids correspondem a quanto de 12? Então basta eu fazer aqui uma conta simples: eu pego cinco dividido por 12 e eu vou pegar a parte do que representa cinco grids em cima dos 12, 41, porque eu multipliquei com esse aqui por 100. Então é como se 41,6% é o tamanho dessa div com relação ao grid maior.

Então você percebe que eu tenho uma conta para ser feita, e ele faz essa continha para mim. E, quando eu faço o grid três, ele já me devolve o width já certinho com relação ao tamanho do grid três, quatro ou cinco. Então é uma exemplificação de como a gente pode utilizar funções, e também vou dar outros exemplos com base na própria documentação do Sass.

## Funções de cor prontas

Uma outra coisa muito interessante são as funções predefinidas que existem no próprio Sass, que adicionam funcionalidades muito legais. Esses aqui são funções de cores que o próprio Sass traz.

Quando eu tenho um hexadecimal e eu quero uma versão dele mais escura... Eu não preciso muito disso, porque, quando eu faço a variação de cores aqui no Figma, a gente já faz a versão mais escura, a versão mais clara, então eu passo como variável no próprio Sass. Mas existe a possibilidade de você, por exemplo, conseguir: ele vai te retornar um hexadecimal com base nesse que você colocou aqui, 50% mais escuro, utilizando essa função darken. Da mesma forma o lighten: eu coloquei a mesma cor, um verdinho, 20% mais claro, e ele vai me devolver um hexadecimal dessa mesma cor aqui, só que em um tom mais claro.

Mas o que eu mais utilizo, de fato, é o transparentize, porque ele converte o hexadecimal, 5FE36A, que não possui transparência, o hexadecimal puro. Mas, quando a gente utiliza o RGBA, ele já consegue. Então, quando eu pego qualquer cor, por exemplo, esse quadradinho aqui, você percebe que ele é transparente, ele tem opacidade. Então você vem aqui no Inspect, ele está como RGBA, 23600 .3. E aí, essa função aqui, transparentize, ela já faz essa conversão do hexadecimal para o RGB com esse caráter de opacidade 0.7 já de forma automática, está bom?

Então, para poder a gente entender um pouco mais de como se dá essa estrutura, pessoal, eu abri aqui o sass:color em Built-In Modules. Você pode procurar aqui mais opções de funções pré-definidas, que, por exemplo, tem adjust-hue, onde você pode colocar uma cor aqui e coloca o valor em graus, que ele vai modificar a sua cor, por exemplo, modificando no círculo cromático 60 deg com relação a essa referência aqui, está bom?

Você pode colocar o caráter de alfa, opacidade. O que mais? Blackness, quando você deixa a cor mais escura, por exemplo. Deixa eu ver aqui outras opções: cor complementar, está vendo? O darken, que eu acabei de falar para você, ele te dá uma versão mais escura de acordo com o valor que você coloca aqui. O desaturate, para poder tirar a saturação: então, da mesma forma, eu quero pegar essa cor aqui, só que 20% com menos saturação, você coloca a cor em hexadecimal aqui, 20%, já te devolve esse valor. Grayscale; green é quando você, por exemplo, quer preservar só o R do RGB; tem hue.

Então tem várias funções já pré-definidas de cores, entre outras que você pode utilizar do próprio Sass. Tem um item dos quais eu não utilizo muito, pessoal, mas estou falando aqui para vocês conhecerem. Por exemplo, tem um mix, que mistura as cores e tudo mais, tem fade-in, opacify, e você pode ir controlando e modificando com essas funções pré-definidas do próprio Sass.

## Funções com o que já vimos

Mas vamos falar aqui de funções, de fato, as funções que a gente pode construir a partir disso, onde eu dei o exemplo para vocês do grid. Então vamos construir essa função aqui e ver como ela funciona na prática.

Mas, além disso, eu queria mostrar para vocês alguns exemplos que as funções, você pode muito bem estar vinculando as funções com todas as funcionalidades que a gente viu até agora, ou seja, estruturas if-else encadeadas, o próprio mixin, estrutura de repetição e tudo mais.

Então, se eu for fazer, por exemplo, uma função que vai ter como parâmetro calcular potenciação de números, então eu vou falar a base e o expoente. Então ele deu um exemplo aqui para a gente de como se dá. Você vai ver, ele tem um estrutura de repetição para ele ficar repetindo quantas vezes o expoente repete. Então, se eu for falar, sei lá, 2 elevado a 3, que é 8, 2 vezes 2 vezes 2, aí ele vai pegar aqui a base, multiplicar pelo resultado inicial, que é 1, e preservar. E aí, quando ele faz a próxima estrutura, ele repete quantas vezes tem um expoente. Então, como o expoente é 3, ele vai ficar 2 vezes 1 na primeira, depois 2 vezes 2 na segunda, depois 2, que é o 4, que já tinha feito aqui, vezes 2 de novo, que é o 8. Ele vai te retornar 8, e você consegue construir uma função no Sass utilizando isso aqui.

Você consegue ver algumas funções de argumentos e tudo mais, utilizando as próprias funções pré-definidas que existem no Sass. Eu construí aqui invert, aí você coloca a cor primária, 80%, onde ele vai retornar um mix da cor inversa, enfim, da função que ele acabou de criar aqui com as funções pré-definidas de cores. Por isso que eu decidi explicar para vocês, que é mais keywords, são palavras-chaves, basicamente isso, pessoal.

## Operadores

E lembre-se sempre que uma coisa muitíssimo importante é que existem os operadores para poder a gente fazer essas operações. Você sempre vai precisar multiplicar, somar, dividir. Então, tenho aqui para poder a gente comparar dois elementos, diferenciar dois elementos, tem o símbolo de maior, menor, maior ou igual. Você pode também fazer numéricos, ou seja, somar, subtrair, dividir, resto ou divisão. Como operar strings: olha só como é que você concatena as strings, muito parecido com o JavaScript, que é o símbolo de mais para poder você concatenar. Como ele faz a soma de números, ele coloca aqui com hashtag também entre chaves para poder fazer isso. Então é sempre bom a gente lembrar disso quando estiver falando de funções.

## Construindo a função grid

Mas, sem mais delongas, vamos construir essa função bem aqui. Então vamos lá, pessoal, como é que se dá essa construção de grids, que aí eu estou meio que explicando o passo a passo para podermos chegar na parte prática, onde eu demonstro tudo, vocês já estão entendendo.

Mas eu declaro aqui arroba function, vou definir o nome da função como grid, e ela vai ter como parâmetro duas coisas. Que primeiro eu tenho que dizer qual é o tamanho que eu quero de grid, então eu posso colocar aqui arroba col, uma variável, e aqui o total de colunas do seu grid, onde na maioria das vezes eu utilizo 12, senão todas as vezes, porque é o padrão que eu utilizo.

E aí o que acontece? Basicamente aqui é uma continha matemática, que eu tenho que pegar aquilo que eu quero do total para poder extrair uma porcentagem. Se o total é esse aqui, se eu quero a parte, eu tenho que dividir a coluna, que é o que eu escolhi, o tamanho que eu quero, a partir do total. Então eu já vou declarar aqui o return, onde eu vou primeiro fazer qual conta? Eu preciso da parte de coluna, ou seja, de coluna, dividido pelo total, e ele vai me dar o valor certinho, só que em parte, não em porcentagem.

E vamos supor que eu quero o valor de uma coluna: 1 dividido por 12, uma coluna representa o quê? Isso aqui vezes 100, 8,33% do tamanho total. Eu quero construir um grid de 7, tamanho 7 com relação ao 12, então eu pego 7 dividido por 12 e multiplico por 100. Então, quando eu quiser construir um grid de tamanho 7, ele corresponde a 58,33% do grid total de 12 colunas. Então esse aqui é o tamanho que ele tem com relação ao pai, é simples e relativo.

Isso aqui, mais uma vez, pessoal, eu não estou levando em consideração o gutter, então a conta vai ficar um pouquinho mais complexa, porque eu tenho que levar em consideração o gutter, que é a distância entre um e outro, para poder termos mais exatidão. Estou fazendo só com colunas para vocês entenderem o princípio.

Então eu faço isso aqui vezes 100%. Se eu colocasse só 100, ele iria me devolver o valor, mas, como eu coloquei uma unidade, 100%, ele também vai me devolver 100%. E aí eu posso simplesmente abrir uma div normal e eu coloco width, width, que é o tamanho da minha div, que ela já vai ser colocada com relação a porcentagem. Então eu posso colocar aqui grid, onde eu estabeleço o tamanho da coluna que eu quero, então eu posso colocar 3.

Quando eu salvo isso aqui, ele criou uma div com width de 25%, porque 3 é divisível por 12 de forma exata, por isso que deu 25%. Mas, se eu fosse colocar, por exemplo, um grid de 5, vai ver que ele deu 41.66667%. Então ele já faz o cálculo de maneira automática utilizando funções.

Isso aqui é generalista, para você literalmente fazer a conta que você bem entender, mas ela se aplica muito bem quando a gente está construindo essa estrutura de grids, e vocês vão entender bem mais quando eu estiver falando sobre a prática geral, de como eu utilizo todas essas funcionalidades do Sass no meu dia a dia para poder ter mais produtividade na minha programação do CSS.
