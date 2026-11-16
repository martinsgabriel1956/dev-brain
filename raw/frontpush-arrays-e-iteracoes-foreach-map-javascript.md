# Arrays e iterações em JavaScript: forEach e map

Opa, então pessoal, sejam bem-vindos a mais uma aulinha do JavaScript ES6+, onde na aula de agora nós vamos falar sobre arrays e interações. Meio que eu vou reiterar o que eu falei na aula passada com relação a isso, mas nós como dev front-end precisamos ter uma atenção especial a isso e conhecer um pouco mais sobre as iterações, sobre os métodos, sobre as propriedades e estudar em si como manipular arrays de objetos, porque de resumo, quando a gente faz uma requisição para o back-end, a gente precisa processar essas informações e elas na maioria das vezes vão voltar em forma de objeto, seja em XML, seja em JSON, então entender todo esse conceito de manipulação de arrays é muitíssimo importante, então nós vamos emergir um pouco mais em funções próprias disso, conhecer as principais que eu sempre estou utilizando, tá bom?

## O array de marcas

Antes de mais nada, vamos, por exemplo, criar um array para poder a gente exemplificar isso aqui. Então, o nome do meu array vai ser carros, não, vou colocar marcas, marcas de carros, então vamos lá, marcas. E aí eu vou colocar Volkswagen, vamos lá, Fiat, vou colocar aqui Renault, vou colocar aqui Ferrari, vou colocar aqui Audi, acredito que já é necessário para a gente começar aqui, tá bom pessoal?

E aí, vocês lembram que para poder mostrar esses itens, eu preciso criar uma estrutura de repetição, definir o índice, ver o tamanho do array e rodar em cada interação o número de arrays. Só que existem funções próprias que já fazem todo esse procedimento, a gente não precisa se estressar e ainda coloca uma função de callback. "Ah, Násser, como assim, me lembra aí?"

## Função de callback

Lembra lá daquelas primeiras aulas onde eu estava falando de funções que existem a propriedade addEventListener, é uma função que você coloca no primeiro argumento, por exemplo, um argumento de clique e aqui você vai colocar no segundo argumento uma função, que é uma função de callback, que é uma função genérica que você simplesmente pode colocar o que você quiser aqui. Então, se eu colocar aqui console.log como está vinculado a um evento de clique, calma que a gente vai dar uma ênfase gigantesca isso aqui quando a gente estiver falando de manipulação DOM de elementos e tudo mais, mas eu posso falar o usuário clicou e aí quando eu executo isso aqui, ele dispara uma função que essa função executa alguma coisa, um console.log.

## forEach

Então, é parecido com isso aqui, só que chama-se forEach, marcas, vou definir aqui marcas e vou acessar o método forEach. Então, for vem da estrutura de repetição e each vem para cada, ou seja, ele já faz a estrutura de repetição já verificando o tamanho do array, ele já percorre todo o array sem você ficar pensando em índice, sem você pegar o tamanho dele e fazer tudo isso na mão, ele já faz isso de forma automática.

Então, você abre o forEach aqui dentro e você vai colocar para ele rodar uma função lá dentro, sendo que essa função já detém de três argumentos. Quais são esses argumentos? Primeiro é o item, qual é o item? É o próprio valor, então o item vai rodar Volkswagen, Fiat, Renault, Ferrari, Audi. O segundo vai rodar o index, que é o índice, ou seja, quando ele rodar, ele vai passar 0, 1, 2, 3, 4 e por último, ele vai devolver o próprio array. Então, esses três argumentos já são pré-definidos dessa função que roda dentro do forEach, mas você não precisa rodar todos, na maioria das vezes você vai querer só o item, ou seja, só o valor, mas estou aqui falando de tudo.

Vamos abrir e, por exemplo, colocar console.log e vamos colocar o que aqui dentro? Item, por exemplo. Então, vamos ver o que isso faz. Ele justamente plotou Volkswagen, Fiat, Renault, Ferrari e Audi. Então, é um método que realiza a mesma coisa que a gente fez lá com for, só que de forma mais direta, está vendo?

Se eu, por exemplo, quiser usar o index, eu faço index mais, coloco aqui um espacinho, coloco mais para poder concatenar. Está aí, 0, Volkswagen, 1, Fiat, Renault e está. Deixa eu colocar agora o array, a gente vai concatenar e colocar agora o array. E deixa eu colocar aqui uma string só para poder separar também. Então, mais array. Então, olha só o que ele retornou para mim, 0, tracinho o item, que é o valor, tracinho o próprio array, ele devolve o array todo.

Mas vocês percebem, pessoal, que eu não estou utilizando, não é interessante às vezes colocar o index, às vezes eu só quero o item. Então, vamos apagar aqui, às vezes eu só quero devolver simplesmente o que tem dentro do array. Então, item.

## O nome não importa, a ordem sim

E se eu não quiser colocar item, pessoal, entenda que isso é uma variável muda. O que importa é a ordem, sempre vai ser item, index e array. Mas eu posso muito bem colocar a, b, c. Ele vai devolver da mesma forma, porque ele já sabe que o primeiro argumento é o item, o segundo argumento é o index e o terceiro argumento é o array. E aqui eu posso colocar a. Está vendo? Ele devolveu da mesma forma. Então, eu posso colocar a, b, c, d. Se eu colocar aqui a, b, c, d, vai rodar. Então, entenda que isso aqui é a posição que influencia e o forEach é amplamente utilizado nesse tipo de coisa.

## forEach com arrow function

Uma outra forma de eu escrever exatamente a mesma coisa utilizando arrow functions, que também vai ter uma aula só para a gente exemplificar, mas por ser importante e eu também estou sempre falando durante as aulas, é porque eu posso suprimir o function aqui dentro e simplesmente colocar item. E aí, ao invés de abrir e fechar chaves assim, eu coloco uma setinha. Ele vai funcionar da mesmíssima forma. Então, olha lá, mesma coisa. É só uma forma diferente de escrever a mesma coisa.

Na maioria das vezes você coloca item ou então só o i, ele vai plotar, ou então só um event do português brasileiro, event aportuguesando, que é de evento. Então, entenda que isso é uma variável muda e agora eu estou utilizando arrow function.

E tem como encurtar mais ainda isso aqui, por exemplo, você percebe que o console.log está ocupando somente uma linha. Quando ocupa somente uma linha, eu posso encurtar isso aqui mais ainda. Então, eu posso fazer assim e tirar as chaves, está vendo? E ele vai executar do mesmo jeito. Então, olha só o tamanho daquele bloco de código, no que eu posso fazer utilizando o forEach com somente uma linha.

Então, é interessante para vocês entenderem e, pessoal, recomendo fortemente para você aprender programação, não tem jeito, é prática. Faça junto comigo todas essas iterações, essas modificações para vocês entenderem as modificações que a gente está fazendo em uma função e estudando as diferentes sintaxes que tem como aplicar.

Então, pessoal, somente resumindo. O forEach é um método que detém três argumentos, item, index e array. E ele devolve uma função de callback, que é essa aqui que está sendo executada, e ela executa essa função para cada item do array. Então, ele roda no array já de forma automática sem precisar se preocupar com, por exemplo, callbacks.

## Modificando cada item

E aí, você pode fazer toda e qualquer modificação, por exemplo, dentro desse mesmo array. Então, eu posso colocar aqui marcas e eu quero colocar, por exemplo, o que eu posso fazer aqui? Eu posso fazer uma pequena modificação. O que eu quero fazer? Por exemplo, adicionar um array fazendo assim, marca e dois pontos o nome da marca. Eu vou fazer mais marca e aqui vem um evento e, que eu defini aqui. E aí, vamos dar um console.log. Como eu quero mais, como se diz, mais de uma linha, deixa eu colocar aqui a chavezinha. Então, vamos lá. Esse aqui é a minha primeira modificação e ele já dá o return aqui dentro. Então, deixa eu dar aqui.

E só que adicionando, por exemplo, marca dois pontos e vamos dar um console.log justamente dessa marca para ver o que está acontecendo. E ele já vai plotar todos os elementos para mim. Então, marca, marca, marca undefined. O que aconteceu?

Então, vamos colocar aqui item, que é mais fácil de entender, que eu entendo melhor assim fazendo item, porque ele já mostra o item direto e ele simplesmente modificou e colocou marca VW, marca Fiat. Eu só concatenei um string a cada item e mostrei ele na tela. Está vendo?

Por exemplo, o que eu posso fazer também é fazer item.toUpperCase. Para que ele é uma string, eu posso colocar aqui, .toUpperCase e executar. E aí, eu mostro. E todas as marcas vão ficar, deixa eu colocar aqui dentro do console.log, todas as marcas vão ficar em caixa alta, ele deixou todas as letras maiúsculas.

## forEach × map

E aí, eu agora vou explicar para vocês qual é a diferença do forEach para o map. O map é muitíssimo parecido com o forEach, porém, o map devolve um array modificado, enquanto o forEach não devolve nada. Ele simplesmente faz as modificações que você quer aqui, mas ele não modifica esse carinha aqui, ele não devolve para você um novo array. Então, vamos supor que você queira fazer um novo array a partir desse, você não consegue com o forEach, a não ser que você faça a modificação de um outro array aqui dentro dele, ele vai executar, mas o map já devolve isso para você de forma direta. A não ser que não entenda o map, faz a mesma coisa do forEach, quer ver? Eu vou demonstrar para vocês.

Eu vou criar aqui um outro array chamado agora carros, onde eles vão receber na mesma ordem dos carros aqui de cima, por exemplo, realmente os carros. Então, vou colocar aqui Polo, que é um carro da Volkswagen, vou colocar Argo, que é um carro da Fiat, vou colocar Kwid, que é um carro da Renault, vou colocar, por exemplo, LaFerrari, que é um carro da Ferrari e vou colocar A3, que é um carro da Audi. Então, eu tenho dois arrays diferentes e agora eu vou utilizar o map.

O que eu vou fazer nesse map, pessoal? Eu vou criar aqui uma nova variável chamada newCarros, ou então Carros e Marcas, melhor, CarrosMarcas, isso. Vamos criar essa constante. O que essa constante vai fazer? Eu quero construir um novo array juntando esses dois aqui, então eu quero que Volkswagen e Polo fiquem juntos, Fiat e Argo fiquem juntos, Renault e assim por diante, entendeu? Então, eu vou construir um novo array, só que agora utilizando o map.

O que eu vou fazer? Eu vou pegar essa variável, ela vai receber, por exemplo, Marcas e eu vou entrar com mapas com o método map. E aí, ele funciona igualzinho ao forEach, só que, como eu disse para vocês, ele retorna um novo array, por isso que eu estou construindo ele sendo atribuído a essa variável aqui, ou seja, o resultado desse método aqui é um novo array que eu vou jogar dentro dessa variável, enquanto se eu fizesse isso aqui com o forEach, ele iria atribuir para essa variável aqui undefined, que ele não retorna nada.

Mas é a mesma ideia, então eu posso colocar item, então ele vai rodar o item desse array, que é Marcas, e aí vamos colocar aqui com arrow function e ele vai rodar isso aqui. O que eu quero que ele retorne para mim? Então, eu posso colocar aqui return, e aí eu quero que ele retorne para mim o index, posso colocar aqui index. Então, o que eu quero? Que ele me retorne o item, ou seja, ele vai me retornar, por exemplo, Volkswagen concatenado com carros no index específico, entendeu?

Então, olha só o que eu estou fazendo, vocês têm que entender esses processos aqui. Estou pegando esse array aqui, Marcas, está vendo? Estou atribuindo o map, que ele faz a mesma coisa do forEach, ou seja, ele vai percorrer o forEach e ele tem três argumentos, o item, o index e o array. No caso, o item vai me voltar o valor, ou seja, se eu estou colocando aqui, ele vai me voltar Volkswagen, Fiat, Renault, Ferrari, Audi. Se eu colocar o index, ele vai me voltar 0, 1, 2, 3, 4, só que, ao invés de pegar o da Marcas, eu vou pegar do carros e vou pegar o index e aí eu vou concatenar com uma estringa de espaço e pontinho, ele vai retornar isso e ele vai jogar isso em uma variável chamada carrosMarcas, porque, como eu disse, o que o map difere do forEach é que ele retorna o array que está sendo construído aqui e aí simplesmente eu vou dar um console.log dessa constante para ver o que tem dentro dela, olha só, ele fez bonitinho para mim, se eu colocar aqui um espaço, ele construiu um array, está vendo? VW, Polo, Fiat, Argo, Renault, Kwid, Ferrari, LaFerrari, Audi a três.

Então eu posso, por exemplo, agora abrir ele com um forEach, posso colocar aqui carrosMarcas.forEach, abro um item, então item, vou abrir aqui uma arrow function e vou fazer console.log, lembre-se que, como é só uma linha, eu não preciso abrir chaves, só quando é mais de uma linha, então console.item, olha só o que ele vai voltar para mim, Volkswagen, Polo, Fiat, Argo, Renault, Kwid, Ferrari, LaFerrari, Audi a três, então olha só, eu construí três arrays aqui, enquanto se eu fosse fazer isso aqui com o forEach, forEach, você vai ver que vai dar errado, está vendo? Não foi possível ler, por quê? Porque ele não volta o array, o forEach, ele volta undefined, enquanto o map já volta um array, beleza pessoal? Então eu recomendo fortemente que vocês façam esses exercícios para vocês entenderem, brinquem assim com os arrays e na próxima aula a gente continua.
