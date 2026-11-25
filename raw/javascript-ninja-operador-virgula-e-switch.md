# JavaScript Ninja: operador vírgula e estrutura condicional switch

Olá, voltamos com o nosso curso JavaScript Ninja, eu sou o Fernando Daciuk, que após a revisão do nosso desafio cinquentinha vai falar um pouco sobre o assunto quem ainda não começou aqui: é o operador vírgula. Operador vírgula. Como assim?

## O operador vírgula na declaração de variáveis

Vou mostrar pra vocês aqui que o esquema do operador vírgula, como ele funciona basicamente. Pra que serve o operador vírgula? Vírgula no JavaScript, um operador, como aquele, estou dizendo aqui. Mas como que ele funciona? Basicamente é o seguinte: a vírgula, ele vai separar, ele vai ser para algumas distorções e vai juntar numa única e uma única expressão.

Então basicamente o que acontece no exemplo que eu estou declarando algumas variáveis. Estado declara uma variável a, você para regular uma variável B e digo que o valor dela vai ser igual a dois, ele é claro uma variável C. O que eu tinha visto que você interpreta com isso aqui: ele entende que estou declarando uma variável a como se fosse normal, ou default. Só que como, quando eu usei a vírgula, ele entende que eu preciso utilizar o var também para declarar o B.

Então basicamente o que estou fazendo: estou declarando três variáveis utilizando uma vez só a palavra-chave. Como eu sei como você declarar se ela três vezes: var B igual a dois e var C.

Então basicamente isso, com o operador vírgula, faz: ele junta várias expressões em uma única expressão, que Betina avalia. Da esquerda para direita. Então ele vai dizer que vai declarar primeiro como default, vai declarar depois o B com o valor 2 e depois vai declarar o como falei isso também.

Então esse vai ser um exemplo onde você vai, onde você vai ver mais frequentemente em alguns códigos. Porém eu não gosto muito desse formato aqui. Eu prefiro o formato declarando a variável como a gente tem feito até agora, e eu vou explicar porque daqui a pouco.

## O operador vírgula no retorno de uma função

Está uma outra forma de você também utilizar o operador vírgula: quando você tem um retorno de uma função. Então, por exemplo, eu tenho uma função myFunc, isto é, quando uma variável x, estou passando valores zero para ela, e o retorno dela eu estou dizendo, eu estou retornando aqui o X mais igual, vírgula, X. Uma vez que eu entendi com isso que eu preciso retornar o valor, eu vou retornar o valor de x. Ele vai avaliar da esquerda para a direita e vai retornar o último valor, que é o valor de x. Mas antes de retornar ainda vai fazer essa avaliação aqui, uma vez que eles só conseguem ganhar um valor com os outros que você não consegue retornar.

Então nesse caso o que que ele vai fazer? Ele vai simplesmente avaliar isso aqui, ele vai fazer o X receber tudo o que ele tem mais o que no caso vai valer, e vai retornar o valor de x. É a mesma coisa que usar o operador de pré-incremento, quem te viu algumas aulas atrás. Da mesma coisa que você usar o retorno mais isso.

Então basicamente é assim que funciona. Eu vou me dar um exemplo na prática aqui, como funciona esse negócio.

## Na prática: vírgula, escopo local e escopo global

Então basicamente, como eu sei, digamos, como eu sei que ele está realmente utilizando a palavra-chave aqui? Vamos dar um exemplo. Meu cliente conversou lá atrás sobre o escopo global e escopo local, que é uma função daquilo: o escopo local, e as variáveis criadas no escopo local você não consegue sair fora. Só que se você criar uma variável sem a palavra-chave var dentro de uma função, ela é acessível fora da função, porque ela cria um escopo global, quando você não utiliza o banco como vem.

Então, se ele funciona desse jeito, crie uma função aqui chamada... Eu vou declarar as variáveis que igual, a variável B igual a 2 e a variável C igual a 3, porque eu vou retornar [um] array com as três variáveis aqui: a, b e c. Invocar a função: ele vai retornar o array com os valores de A, B e C.

E aqui, se eu colocar seu ponto e vírgula que no lugar da vírgula, ele cria a, b, c como variáveis globais, porque eu não estou utilizando a palavra-chave pra eles. Mas como eu estou usando o operador vírgula aqui, B e C são locais, se elas não são globais. Ou seja, eu não consigo acessar aqui fora. Se eu tentar acessar aqui agora só, ele vai dizer que o ato não foi definido. Se tentasse saber, a mesma coisa. E o C, exatamente a mesma coisa. Ou seja, a, B e C só foram definidos aqui dentro da minha função.

Olha só que legal. Então você pode também utilizar esse formato aqui. Nas nossas aulas, os nossos testes aqui, quem vai fazer, a gente vai utilizar sempre o formato uma palavra-chave var para cada variável declarada, porque fica mais no código e tal. Beleza? Fica maior aqui. Se você, se você verificar, olha só, fica muito mais espaço. Se você pode ter isso aqui, por exemplo, agora 3 vai ver vai ser igual a bonito, por exemplo. Aí, por exemplo, se eu quiser mover essa variável daqui, eu simplesmente tiro essa expressão inteira daqui e joga pra outro lugar. Entendeu? Se eu quiser remover, ou simplesmente removê. Agora, se eu tiver uma expressão assim, eu vou precisar dar uma olhada melhorada, que eu acho que tem que cuidar de remover. Entendeu? Então fica, digamos, uma expressão um pouco mais complicada de você olhar. Visualmente falando, você avaliar uma empresa, principalmente por essa avaliação visual.

Então o operador vírgula, como funciona dessa forma, funciona também com o retorno de uma função. Então para qualquer expressão que você quiser, o que você quiser juntar, ela vai, ela vai funcionar.

Então foi um show, mas foi aí: eu vou fazer um raio X igual a zero, vou conseguir na mão dele. Vou terminar aqui falando should x 0, x mais igual e X. Então você chamar Marfan, ele deve retornar pra mim isso que aconteceu. É a mesma coisa aqui, mas falando baixinho igual a zero. Caetano x, eu vou ficar muito feliz aqui que ele vai retornar também, tá?

Então bem simples de entender como é que funciona o operador, o operador. Se você tiver alguma dúvida depois, você pode perguntar, mas essa prática é bastante simples e é basicamente isso que você vai, que você vai ver por aí. Dificilmente você vai ver um retorno e assim está com ele tentou não valer uma expressão. Novamente, você vai valer essa expressão antes de fazer o retorno. E isso aqui pode ser que você veja em vários códigos pela internet, tá, em vários códigos e vários códigos, eu penso. Eu acho que se eu for mexer você vai, provavelmente você vai ver isso daqui, está mais em TI. Vai utilizar nos nossos códigos um para cada variável declara. Beleza?

## Estruturas condicionais: if, else if e ternário

Sobre variáveis era isso que eu queria dizer. Vamos baixar agora para [o] assunto que são estruturas condicionais. A gente já viu algumas estruturas condicionais: if. A gente já viu que o if consegue usar com o else if pra testar outros tipos de valores, e quando a gente não sabe o valor eu quer testar um última coisa pode dizer Tamiel. [A] gente viu também que a gente consegue utilizar o operador ternário, que é o Lau, que quando você faz isso aqui. Quando você utiliza, por exemplo, vai receber: se for igual igual, sim, ele vai receber um, não, receber 2. x, vai B2, que não é igual a falso e nem o tipo dele é igual falso. Ele vai ser 2.

## O switch

Então basicamente isso tem o formato ternário, do formato que a gente tenha o switch. O switch é uma outra forma da gente fazer uma estrutura condicional.

Então, por exemplo, como dar um exemplo bem prático aqui: vou criar uma função de novo aqui, mas falei para passar um valor x para ela, e vou avaliar esse valor de x: switch X. Eu vou utilizar o case para verificar se o X é igual ao valor que eu passar aqui. Então verificar o x é igual a 1. Aí eu vou fazer o console ponto log, vou colocar aqui só para você verificar que isso é um. Beleza? Que você vai utilizar a chave break, que ela vai parar essa instrução se X for igual a 1. Por exemplo, 2: ele vai testar se o x é igual a 2. E lembrando que ele utilizou o operador igual, o Citi, que é igual aos 30, ou seja, ele testa o valor e o tipo. Então, se ele for igual a dois, console ponto log x 2. Eu posso usar também um default, ou default, que ele vai dizer: se o X não for igual [a 1] n[em] foi igual a 2. Então um console ponto log: x não é nem um nem dois. Beleza?

Aqui no ano 2, eu acabei de colocar o que eu esqueci de colocar o aqui. Isso aqui é um problema, eu vou mostrar pra você porque é um problema você não usar o break.

Então basicamente qualquer estrutura do switch, ele vai verificar pelo valor, ou ele vai verificar uma expressão. Expressão aqui no Brasil X, que eu vou passar como parâmetro pra mim. Ele vai verificar o x é igual a um; caso X for igual, ele vai dar um console ponto log: x é igual a x e 1, e vai parar. Ou seja, não vai, vai ignorar qualquer outro comando que tiver aqui dentro. Além de verificar não é igual, então ele passa o próximo: X é 15 2, ou seja, se o X for igual a 2, ele vai mostrar console ponto log x 2. E aqui eu não coloquei o break, ou seja, quando eu não coloco break ele não para, ele continua avaliando as outras instruções. Ainda que essa aqui seja verdadeira, ele continua falhando e continua passando por todos os valores. Então isso é um grande problema, eu vou mostrar para você agora na prática como. Mas se x não for o inimigo 2, ele vai cair no default. No default, por padrão.

## O switch na prática e o problema do break esquecido

Então invocar aqui mais fundo que, sem passar valor nenhum, tem um valor de x aqui muitíssimo diferente. Ele já retornou aqui que x não é um nem dois. Começou ele logo no início em 2 x 0. O retorno da função ainda fica no território. Então ele diz que ele entrou no valor default do switch. Beleza?

Agora, por exemplo, se eu colocar aqui x é igual a 1, mas passar o valor. Ele vai dizer que x é igual, porque o que ele vai verificar aqui: vai dar um console ponto log x e 1 e vai dar um break pra parar, vai sair daqui. Certo?

Agora olhe o que acontece. Olha o problema que acontece quando passo 2 aqui. Se eu tivesse colocado um boi que entornar o X2 ia parar. Mas como eu não coloquei, do que acontece? Ele disse que x é igual a 2, ele continua no default, dizendo que x não é nem um nem dois. Então olha só que perigo. O problema é que isso pode não ter o código. Então presta bastante atenção quando você usar o switch.

## Switch comparado ao if

Eu sei que ele vai pressionar mais ou menos como o if, mas ele vai validar somente usando o operador turístico. Era a mesma coisa que você tinha que fazer. Falei isso aqui: if x igual a... Coloquei 3 pontinhos, vendeu quem vai ter. Basicamente eu sei dizer: x é igual a, ele faz alguma coisa, se... else if X 2, faz outra coisa. Sci fi ou é o seu caso, aí retorna aquela última coisa. Então basicamente isso aqui que ele faz. Ele vai verificar sempre esse o X, é basicamente isso que ele faz.

Que você pode ver que ele faz de uma forma um pouco mais legível quando você utiliza, quando você utiliza o switch. É basicamente um switch X. Aí ele vai fazer alguma coisa, lembrando sempre que colocar alguém que no final, certo? De dois ou qualquer outra expressão que você quiser verificar alguma coisa, break, que você pode fazer quantos cases você precisar, estar de fora de qualquer outra coisa, e fecha, e fecha o switch com uma interrogação que eu fiz aqui. Mas com esse cara que, beleza?

Então é basicamente assim que funciona o switch. É bem simples também, é uma estrutura, uma estrutura condicional também, parecido com o if, e a gente vai usar ele algumas vezes. A gente vai experimentar algumas coisas, como verificar, como utilizar, está em jogo quando utilizar, em que momento utilizar. Em breve vou conversar um pouco mais sobre a estrutura de quando saltava, e tenho alguns exemplos no teste de hoje e também para você usar o switch, para poder treinar e usar. É basicamente sobre isso.

Agora na próxima a gente vai falar sobre como, começar a conversar um pouco sobre estruturas de repetição. Beleza? Só que isso na próxima época, nosso tempo já acabou. Valeu. Até a próxima.
