# Functions e arrow functions em JavaScript

Opa, fala pessoal, tudo certo com vocês? Vamos lá para mais uma aula de JavaScript, onde na aula de hoje nós vamos falar sobre funções e funções de seta, se eu for traduzir literalmente. Functions e Arrow functions, conceitos importantíssimos para poder a gente progredir na linguagem e além disso, da gente compreender como é que se dá as principais funcionalidades em questão de frameworks, como React ou Vue, que é muito comum a gente sempre estar batendo na tecla em Arrow functions, e a gente vai perceber quais são as diferenças de funções para funções de seta, se é que eu posso dizer assim, e ver os principais conceitos que norteiam essa categoria aqui. Então vamos lá, sem mais delongas, vamos entender primeiro.

## O que é uma função

Funções, quando eu falo o que é função, o que é? São blocos de códigos que são reaproveitados. "Ah, Násser, como assim?" Então vamos primeiro entender essa primeira seção aqui, são blocos de códigos que são reaproveitados. Vamos supor que você tem um programinha onde ele faz diversas contas de polígonos, e aí você sempre vai precisar calcular a área, por exemplo, de um quadrado, de um retângulo, ou então calcular a sucessiva área de outros polígonos que você pode dividir em quadrados menores, mas sempre a unidade fundamental é um quadrado ou um retângulo.

Então é interessante que você tenha aqui o function, por exemplo, uma área retângulo com uma função para você sempre chamar ela a fim de o código que está aqui dentro, eu sempre vou estar repetindo ao longo do meu código, então eu criei uma função para eu sempre chamar essa função para executar determinada coisa, para ele me devolver um determinado valor, para que eu não precise ficar escrevendo esse mesmo trecho de código toda vez.

## Parâmetros e argumentos

Então basicamente é isso, que pode deter ou não de parâmetros, ou seja, a gente percebe que na área do retângulo a gente precisa de duas coisas, um lado do retângulo e o outro lado do retângulo, ou seja, o lado A e o lado B, ou o lado 1 e o lado 2, a gente detém nesse caso aqui de dois parâmetros na nossa função, mas eu posso muito bem ter uma função que se chama function HelloWorld, onde eu quero que ela simplesmente printe no console.log a questão do HelloWorld no console, eu quero que ele digita isso aqui para mim, em que se eu vir aqui e executar essa função, olha só, ela printou bem aqui HelloWorld no console, vocês estão vendo aqui.

Então pessoal, essa aqui é uma função que não tem parâmetros, mas essa aqui é uma função que tem parâmetros, ou seja, ela pode ou não ter. Por exemplo, no próprio console.log, com o conceito de a gente ter visto de objeto, a gente vê que console é um objeto em que quando eu aperto o ponto, eu tenho como acessar tanto os métodos, que são as funções, tanto as propriedades, como por exemplo, memory é uma propriedade, log é um método em que esse log vai plotar uma string, que é a string que eu colocar aqui dentro, ele vai plotar bem aqui.

Então uma outra função, que tem como argumento, lembrando que quando eu escrevo aqui é parâmetro, quando eu passo diretamente é argumento, e que executam determinadas funcionalidades, podendo ou não retornar algo.

## Retorno

Por exemplo, essa própria função do helloWorld, ela não me retorna nada, ela simplesmente executa alguma coisa, e esse executar alguma coisa é plotar helloWorld no console, mas eu posso muito bem escrever a área retângulo, onde eu vou retornar, por exemplo, a vezes b. E aí tem uma regrinha também, que é sempre bom, aquilo que você insere, o tipo de dado que você insere na função, é o mesmo tipo de dado que retorna na função. Então se eu estou colocando aqui um número inteiro, um número de fato, o ideal é que retorne também um número, são boas práticas.

Enfim, pessoal, basicamente eu tenho aqui a área do retângulo, onde se eu colocar 4 e 2, ele vai me voltar 8, porém ele não está retornando no console, ele só vai retornar o número, então eu vou dar um console.log e executar essa função área retângulo aqui dentro, 4, 2, e aí sim ele me retornou 8.

## Arrow function

Então, pessoal, essa é a forma, porém, quando eu falo de arrow function, ela tem uma diferença para funções, onde essa aqui é a sintaxe padrão de funções, só que tem como eu escrever a mesma coisa, só que de maneira diferente. Por exemplo, vamos escrever essa função aqui declarando uma variável.

Então eu vou vir aqui, definir uma constante chamada área retângulo e eu vou atribuir essa constante uma função, uma function, e aí eu vou passar os mesmos dois parâmetros, a, b, e aí eu vou abrir as chaves, ou seja, eu declarar a função área retângulo dessa forma aqui é exatamente igual a eu declarar dessa forma aqui. Se eu vir aqui e dar um Ctrl C, Ctrl V e vir aqui comentar, você vai ver que vai funcionar do mesmo jeito, posso colocar aqui 6 e 2, vai dar 12, está vendo? Eu simplesmente mudei a forma de como eu inseri, de como eu declarei a minha função, essa aqui é uma forma.

Uma outra forma é, por exemplo, eu apagar esse function e colocar uma setinha, por isso que se chama arrow function, arrow vem de seta, está bom? Em que é exatamente a mesma coisa, então se eu vir aqui e salvar, continua dando 12, eu posso vir aqui e colocar, por exemplo, 8, vai dar 16, está vendo?

E uma outra, e tem como, por exemplo, encurtar mais ainda esse quesito aqui. Você está vendo que o meu retorno da função está em somente uma linha, então quando está em somente uma linha, eu posso apagar o return, fazer isso aqui e simplesmente apagar as chaves, ou seja, olha eu declarando a mesma função com bem menos verbosidade em uma única linha, você vai ver que vai continuar funcionando. Se eu colocar aqui 10, 2, vai dar 20, ou seja, são formas diferentes de eu declarar a mesma função, só que com menos verbosidade, com menos trecho de código para você especificar as coisas. Talvez não seja muito intuitivo eu encurtar muito, mas é importante que a gente entenda essas sintaxes que são muito comuns quando a gente partir para algum tipo de framework e coisa e tal.

## Um parâmetro só

Uma outra coisa muito importante, pessoal, que eu me lembrei aqui, é que vocês podem ver que eu tenho dois parâmetros, eu tenho o lado A e o lado B, mas vamos supor que eu queira declarar uma outra função, onde eu só vou precisar de somente um argumento. Eu posso declarar, então, constante e o nome da função vai se chamar upperName, onde essa função vai receber como parâmetro uma string e essa string eu simplesmente vou devolver ela só que em caixa alta, todas as letras maiúsculas.

Então, eu posso fazer assim, function, declarar aqui dentro, por exemplo, o name e o que eu vou retornar? Eu vou dar um return name.toUpperCase, que é uma função própria de string e como isso aqui é um string, ele já se torna um objeto, só de ser um objeto, o string já herda várias propriedades e vários métodos que são inerentes a ele, que são próprios do JavaScript e um deles é o toUpperCase.

Então, se eu vir aqui no console e agora executar o upperName e passar, por exemplo, o meu nome, Násser, a gente vai ver que ele vai retornar para nós Násser em caixa alta, está vendo aqui, onde, mais uma vez, aplicando o arrow function, eu posso apagar essa function e colocar uma setinha. Ele vai executar da mesma forma, porém, o meu retorno detém de somente uma linha, então eu posso apagar o return, deixar aqui somente uma linha e tirar as chaves, ele vai funcionar da mesma forma, mas ele só detém de um argumento, então eu posso vir aqui e tirar os parênteses, quando eu tenho mais de um argumento eu preciso, quando eu tenho somente um, não é necessário. E olha só, ele vai funcionar da mesmíssima forma, então é importante a gente conhecer a sintaxe do arrow function para que, quando a gente for lá em frameworks, não te soe estranho esse tipo de sintaxe para funções.
