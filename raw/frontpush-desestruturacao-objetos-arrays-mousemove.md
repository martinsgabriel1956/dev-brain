# Desestruturação em JavaScript: objetos, parâmetros e arrays com o evento mousemove

Opa, fala pessoal, tudo certo? Vamos lá para mais uma aula de JavaScript, onde nós vamos agora falar sobre desestruturação.

Esse recurso aqui, pessoal, é muito similar a quando a gente, por exemplo, escreve um código de maneira tradicional e quer reescrever ele de maneira mais simples ou mais direta, mais escrevendo e tendo a mesma funcionalidade.

E por que eu bato na tecla da desestruturação? Porque esse recurso aqui é muitíssimo utilizado quando a gente parte para frameworks como React ou Vue, então é importante a gente bater o olho e identificar, poxa, isso aqui é uma desestruturação, eu já sei o que está acontecendo. É um conceito bem simples, mas é importante a gente vir aqui e trabalhar.

## O evento mousemove e as propriedades do evento

Sem mais delongas, vamos escrever aqui mais uma vez no nosso App.js um pequeno exemplo para poder ilustrar isso do que eu estou falando aqui para vocês.

Vamos supor que eu queira criar uma função, pessoal, para poder mostrar aqui no console a posição Y e X do meu mouse, quando eu estou movendo aqui.

A primeira coisa que eu quero criar, por exemplo, é um document e um documentElement, que é para poder ele executar sem ser em cima de algum outro elemento, a própria página, simplesmente isso. E eu vou escrever um documentElement, e aí eu vou colocar um evento para ele escutar um evento utilizando o addEventListener.

Vou colocar o evento de mousemove, e aí ele vai disparar uma função que eu vou chamar essa função de mouseMove, mouseMove, ou seja, quando ele detectar o mover do mouse na tela, ele vai estar escutando esse evento, ele vai vir aqui e vai executar essa função.

E essa função nós vamos escrever aqui, então vamos colocar aqui function mouseMove, já está aqui certinho, onde eu vou ter como parâmetro o evento, o próprio evento para eu obter, por exemplo, as informações do evento.

Se vocês não estão entendendo como se dá essa questão do evento, por favor, dá uma olhadinha nas aulas de manipulação DOM, onde eu tenho aulas específicas para falar disso, onde eu vou querer extrair as informações do evento.

Então, se eu der um console.log do evento, ele vai mostrar para mim todas as características desse evento, então quando eu passo o mouse aqui, você está vendo que ele está disparando um monte de números aqui do lado? Esse aqui foi o mais recente. Olha só todas as informações do evento mouseMove, aqui são todas as propriedades, métodos que estão inerentes a esse evento, só que eu quero dois específicos, que é o clientX e o clientY, vocês estão vendo aqui, eu quero essas duas propriedades apenas, eu não quero que rode todas.

E para poder fazer isso, eu posso criar uma constante chamada clientX, onde eu vou pegar lá no evento e justamente pegar a informação clientX, e aí eu coloquei a constante aqui com uma letra maiúscula, posso colocar minúscula também, não tem problema nenhum. E vou colocar o eixo Y também, e ao invés de plotar o evento, eu vou plotar apenas o x, o y e vou executar a mesma coisa, está vendo?

Agora vocês podem ver que ao invés de plotar todas as informações do evento, eu quero somente as características clientX e clientY, que são os valores do eixo X e Y.

Então, pessoal, vocês percebem que quando eu estava plotando o evento, se eu vir aqui e plotar o event, ele detém de várias características, basta eu abrir aqui, então tenho o clientX, tenho o clientY, tenho o detail, tenho o layerX, o layerY, tenho o offsetX, o offsetY, tenho o pageX, o pageY, então olha só o tanto de características.

E vamos supor que eu quisesse pegar todas essas características, então eu só dei o exemplo aqui do clientX e clientY, mas eu poderia muito bem fazer de todas essas aí que eu te falei, posso fazer do page, então vamos lá, page, aí eu colocaria page, aí eu faria event, page, mais uma vez, então copia, cola, copia, cola.

E aí, se eu extrair muitas características e ficar declarando, o meu código fica muito grande, está vendo? Imagine se eu fosse extrair aqui, sei lá, 15 características, 10 características, então eu teria 10 linhas só para poder extrair essas características, concorda comigo?

## Desestruturação de objeto

E aí tem uma forma de eu fazer isso de forma mais direta, que é a chamada desestruturação, basicamente eu faço const, abro e fecho chaves e aí eu coloco o nome das características aqui direto e é importante, não são constantes, eu poderia muito bem colocar aqui eixoX e eu poderia muito bem aqui colocar eixoY.

Se eu fizesse dessa forma aqui, eu posso muito bem colocar aqui eixoX, que ele vai funcionar, vírgula eixoY, você vai ver que ele está plotando normal e aqui eu coloco o nome que eu quiser, nesse caso aqui, se eu for desestruturar, eu tenho que utilizar a propriedade, então no caso eu tenho que colocar clientX, clientY e aí ele recebe o evento, então ele já está fazendo todo esse processo aqui, já está armazenando uma variável e colocando essas características, então se eu vir aqui e colocar o clientX e o clientY nessa parte aqui, você vai ver que ele vai funcionar igualzinho, isso aqui é a chamada desestruturação, que tira um pouco da verbosidade nessas declarações.

## Desestruturação direto no parâmetro

Uma outra forma de fazer isso aqui, que é importante eu pontuar também, é que eu estou criando uma constante com essas variáveis que estão recebendo exatamente o mesmo nome da propriedade que existe no objeto event, concorda comigo?

Porém, você vê que o event passa aqui automático, porque é uma função de callback, lembre-se disso, é uma função de callback, então o event já está aqui, eu posso muito bem desestruturar isso aqui de maneira direta, ou seja, dar um Ctrl X aqui e colocar aqui e já estou desestruturando ele diretamente no argumento, se eu der um Ctrl X ou um Ctrl S para salvar, vocês vão perceber que ele continua funcionando normal.

## Desestruturação de array

E você pode estender esse conceito da desestruturação, por exemplo, para arrays, vamos supor que eu crie aqui um const carros e eu vou construir com marcas de carros, vamos por Volks e depois eu coloco aqui Fiat, depois eu coloco aqui BMW, depois eu coloco aqui Audi, então eu vou desestruturar, por exemplo, um array de carros.

Lembre-se, eu desestruturei um objeto utilizando chaves, sempre objeto chaves, array, colchetes, concorda comigo?

Então, se eu criar aqui uma const, agora onde eu posso colocar, por exemplo, marca 1, marca 2, marca 3, marca 4, marca, marca, marca. Isso aqui é igual a carros, eu estou justamente desestruturando, eu estou pegando aqui o array carros, passando o primeiro aqui para marca 1, criando uma constante chamada marca 1, pegando esse primeiro valor, marca 2 esse segundo valor, marca 3 esse segundo valor.

Vamos dar um console aqui, console.log, dá, por exemplo, marca 1, só para poder a gente atestar isso aí, marca 1, você viu lá que deu Volks, deixa eu apagar esse console, Volkswagen, se eu colocar marca 3, é para aparecer o que? BMW, está vendo? Vou colocar marca 4, Audi.

## Desestruturação com funções

Então vai ser comum vocês verem essa questão de desestrutura desestruturação, não só para variáveis, mas também para funções, lembre-se que quando a gente declara arrow functions, a gente declara como? A gente pode definir assim uma função que é igual ao que, ao invés de receber um valor, um string, ou então ao invés de receber um número que você está declarando, você pode muito bem declarar uma função, lembre-se disso, que é arrow function, é possível você fazer isso.

Então, eu consigo utilizar a desestruturação não só com variáveis, mas também como funções, então eu posso conseguir aqui, ao invés de colocar marca e só variável, posso colocar aqui funções, então quando a gente estiver trabalhando com algumas frameworks, isso vai ser comum, mas é importante que vocês entendam esse conceito, beleza pessoal? Então é isso, falou e até a próxima.
