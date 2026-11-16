# Variáveis, tipos de dados e operadores em JavaScript

Opa, olá pessoal, então vamos dar continuidade às nossas aulas de JavaScript, nas próximas aulas agora eu vou meio que desaparecer da sua tela, para você ficar totalmente focado no conteúdo, escutando apenas a minha voz. Então vamos lá, na aula de hoje, nós vamos verificar os principais conceitos de variáveis, tipo de dados e operadores de uma forma sucinta para poder começarmos.

## O que é uma variável

Primeira coisa, o que é uma variável? Variável é basicamente um nome que a gente define, então eu posso muito bem definir let nome igual a, sei lá, Násser, o meu nome. O que está acontecendo de fato? Eu fui lá na memória, aloquei um espacinho lá, defini uma label para esse espacinho chamado nome e coloquei o conteúdo Násser lá dentro, então literalmente é um espacinho na memória que eu aloquei definindo uma variável, porque quando eu defino variáveis facilita a minha vida no código para eu não ficar redefinindo muitas coisas, simplesmente colocar um conteúdo em uma variável e depois simplesmente chamar ela, ou então manipular, ou qualquer coisa do tipo. Enfim, então variável é isso.

## var, let e const

Agora existem basicamente três tipos que a gente utiliza, que é o var, o let e o const. "Ah, Násser, quais as diferenças entre elas?" Basicamente antes do ES6 só existia o var, então quando você tinha que definir algum tipo de variável, então o var nome é igual o que, Násser, então você definia assim, agora com o ES6 teve o let, que é muito parecido com o var, tem uma pequena diferença que eu vou explicar para vocês e o const.

Primeira coisa, o const, como o próprio nome já diz, é uma constante, ou seja, é uma variável que não é para alterar o conteúdo dela ao longo do código, então você pode ver que se eu vir aqui e colocar nome é igual, por exemplo, a Yousef, que é o meu sobrenome, e salvar, olha só o que vai aparecer, vai dar erro. O que ele está dizendo aqui para vocês? Você está tentando atribuir um valor diferente a uma variável constante, então a gente já sabe que variável constante você tem que definir um valor para ela e não pode mais alterar, esse é o escopo.

Já a diferença do var e do let, basicamente é entender o que é uma variável de bloco ou não, uma variável que tem um caráter mais global e uma variável que tem um caráter de bloco, é interessante a gente entender esse conceito porque quando estiver construindo funções, essa funcionalidade vai ficar mais evidente, então basicamente eu vou fazer o seguinte, eu vou definir um nome e vou colocar para ela o valor Násser, que é o meu primeiro nome. Vou abrir um pequeno bloco, como se fosse uma função, entenda que é um bloco diferente do código principal, onde eu vou definir o nome da mesma variável chamada nome, só que agora com o meu sobrenome Yousef, vou dar um console.log para poder verificar o que vai acontecer, onde eu vou plotar nome e quando acabar o de ler o código, eu quero que ele plote mais uma vez console.nome.

Então vamos lá ver o que vai acontecer, quando eu salvar, olha só o que apareceu no console, apareceu Yousef, ou seja, eu defini o nome Násser na variável nome, ele veio aqui no bloco var nome Yousef, atribuiu o Yousef para o nome, printou Yousef, mesmo sendo de blocos diferentes, esse aqui está no bloco de fora e esse aqui está no bloco de dentro.

Agora vamos aplicar a mesma coisa com let, então olha aí, agora plotou Yousef Násser, ou seja, ele respeitou o bloco em que a variável está inserida, como eu defini let nome dentro desse bloco, ele vai respeitar a variável nome dentro desse bloco, enquanto eu defini a mesma variável let nome fora do bloco e ele plotou Násser fora do bloco e Yousef dentro do bloco, basicamente essa é a diferença de escopo entre as variáveis.

Então, outra coisa que é importante é que o JavaScript é case sensitive, ou seja, se você declarar uma variável chamada nome com o n minúsculo e uma outra variável aqui embaixo com o N maiúsculo, isso aqui é considerado como variáveis diferentes.

## Tipos de dados

Agora vamos conhecer um pouco sobre os sete tipos de dados, eu posso definir aqui let nome, onde eu atribuo uma string com aspas, então coloco Násser, então isso aqui é uma string, é um conjunto de caracteres, eu posso colocar let idade, onde eu coloco um valor numérico, no caso 25, é a minha idade, então é um valor numérico.

O outro tipo de dado é um dado booleano, ou seja, aquele verdadeiro ou falso, eu posso colocar aqui feliz é igual a true, então esse aqui é um valor booleano, você escreve assim, booleano, é muito interessante para poder a gente saber trabalhar com estruturas condicionais que a gente vai ver logo, eu posso definir aqui uma variável chamada, por exemplo, nada, quando eu não faço nada na variável, não atribuo, ela é indefinida, ou seja, undefined.

Uma outra variável, o tipo de dado, eu posso colocar um símbolo, onde você atribui o symbol e por último um objeto, então eu posso definir assim o object, e quando eu vou definir um objeto, eu abro e fecho chaves, então isso aqui se tornou um objeto, o que é objeto, vocês vão perceber que entender o que é objeto, vai facilitar demais vocês compreenderem muita coisa do JavaScript, porque justamente tudo em JavaScript é objeto.

Lembra que eu dizia que lá em CSS tudo é div, tudo é caixa, aqui praticamente tudo é objeto e vocês vão perceber, por exemplo, o próprio console.log é um objeto, o que é um objeto, é basicamente uma classe gigante, uma caixa muito grande onde lá dentro tem variáveis e funções e quando você abre a caixa, você tem que dizer qual é a variável e qual é a função, quando você está abrindo várias coisas, console é o nome da caixa, .log é o nome da função que tem dentro de console, que quando eu coloco, por exemplo, nome, ele vai plotar para mim lá no console, e se você quiser descobrir o tipo de dado, você pode colocar aqui typeof, ele vai plotar aqui, string, eu posso colocar idade, number, eu posso colocar aqui feliz, boolean, posso colocar aqui object, quase que não sai, e aqui vai plotar um objeto.

Então, esse entendimento é super importante da gente entender e vai ser retomado nas próximas aulas, podem ficar tranquilos com relação a isso.

## Concatenação e template string

Uma coisa que também é interessante eu dizer é, por exemplo, concatenar strings, onde eu posso criar uma variável chamada sobrenome, onde eu vou colocar aqui o meu sobrenome, Yousef, e se eu quiser juntar essas duas variáveis aqui, eu posso fazer o seguinte, colocar nome mais sobrenome, ele juntou, só que ele não colocou o espaço, está vendo, ele literalmente juntou uma na outra, quando eu quiser colocar um string, eu posso fazer assim, colocar um espacinho aqui, aí ele vai plotar dessa forma, então você concatena com mais em JavaScript.

Tem uma outra forma que eu posso colocar aqui, let string, onde é uma tipologia, é uma sintaxe do próprio ES6 para frente, onde você coloca acento, isso aqui é o acento em crase, para você não ficar emendando dessa forma aqui, e quando você coloca isso, você pode colocar o, aí eu coloco aqui a variável, seguida de dólar entre chaves, e aí eu posso colocar o que eu quiser de JavaScript aqui dentro, que ele vai entender, então eu posso colocar aqui nome, o Násser tem o sobrenome, aí eu coloco o dólar mais uma vez aqui dentro, sobrenome, e aí eu declarei ele dessa forma, e ao invés de colocar mais, ou mais e ficar concatenando dessa forma, eu também posso escrever desse jeito aqui e colocar, por exemplo, string aqui, vamos ver como é que ele executa, executou certinho, beleza?

## Operadores

No mais é isso, pessoal, agora vamos falar um pouquinho sobre números e operadores, bem simples isso aqui, vamos com a soma, no sentido que a gente pode definir assim, var soma é igual o quê? 200 mais 200, operação de mais, operação de menos, operação de multiplicação, operação de divisão, operação de resto ou o resto da divisão aqui, então esses aí são os operadores aritméticos que a gente vai trabalhar, por exemplo, em estruturas condicionais, quando a gente está falando if e else, então no mais é isso, até a próxima.
