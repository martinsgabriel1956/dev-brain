# JavaScript Ninja: o método push() e o loop for

Olá, voltamos com um curso de JavaScript Ninja, e eu sou o Fernando Daciuk, que agora vai conversar um pouco sobre o método push, a revista que segue o método do array. Basicamente, ele serve para adicionar um item no final do array. Como é que funciona na prática?

## Revisando o array e o length

Então, basicamente, funciona assim: eu tenho um array com alguns itens. Só vou colocar um, dois, três. Vou colocar um objeto com bola azul, é isso. Então eu tenho o meu array. Array ponto length: quem tiver a propriedade lá no último vídeo, que mostra a quantidade de itens que eu tenho no meu array. Então eu tenho cinco itens, encerrei, encerrei, que eu posso acessar eles com array zero, array 1, 2, 3, 4 e 5, array 4 a 5. E no array 4 eu ainda tenho um objeto, que tenho uma propriedade de bola, então consigo acessar a propriedade bola assim: vai monitorar o valor azul. Então basicamente essa é a propriedade do array.

## Adicionando itens sem o push

Agora vamos ver como é que funciona de verdade push. Eu preciso adicionar mais um item no array. Tenho duas formas de adicionar itens do meu array. Uma delas, a primeira delas, é você escrever todo o seu array. Então você pode escrever todo o seu array e adicionar, por exemplo, uma outra array local, array de 2 a 3. Se eu chamar array ponto length, eu vou ter seis itens. Deixa morrer. Então eu tenho todos os itens, porque eu sou o array.

Só que isso não é inteligente, tão inteligente, que eu soube escrever o meu array toda vez que eu precisar adicionar um item novo. Então ele era escrito como muito conversou com array: ele é um tipo de objeto antigo, viu que ele tinha a propriedade length, e ele também tem um método chamado push.

## O método push

Push, ele serve para que ele serve? Para a tradução: a tradução, push significa empurrar. Então como fazer? Eu vou empurrar um valor para dentro do meu array. Então, por exemplo, tem esse array, que tem seis itens. Agora eu vou empurrar para dentro do meu array mais um item, que vai ser, será mais um objeto, por exemplo, carro, que vai ter o valor BMW.

Olha só, você pode ver que o array ponto push, ele já retorna o length do array. Então eu, por exemplo, tinha seis. Agora o array ponto length, length, que é meu array, ou o tamanho do Boa Esporte: agora eu tenho sete itens do meu array.

Se eu chamar ele aqui, eu posso ver que eu tenho 1, 2, 3, Agostinho da Silva, o objeto bola, um objeto com uma propriedade bola com valor azul, mais uma array, lá, lá, dois laterais, e mais um objeto com a propriedade, o carro tem o valor de me adaptar, porque eu posso processar simplesmente assim. Sei que ele começa em zero. Então você chama array do carro, eu vou ter um valor BMW. Você chamar array cinco, 5, que é mais um array. Array, sim, chamou o valor, bateu lá, 2 x 0. Então isso aqui funciona do mesmo jeito. Eu chamei o array, eu peguei o sexto, entendo, array, tem um outro array, que é um outro array, o quinto, o sexto, no caso, que é a chave 5, né? Meu array é a chave. Deixarei aqui o 0, 1 e o 2, está.

Então, basicamente, é assim que funciona push. Ele serve exatamente pra isso: ele serve para adicionar itens dentro do array. É bem simples o uso dele.

## Função dentro do array

Então, por exemplo, se eu quiser adicionar ao meu array, eu quero adicionar uma foto show no meu array, eu posso falar também. Eu posso fazer uma função. Digamos que eu vou criar uma função formada a soma, que ele vai, ele vai receber um parâmetro x, um parâmetro y, e vai retornar somando x mais y. Eu posso fazer isso também. Agora eu tenho oito itens no meu array. Você chamou array, eu vou ter uma soma. Vocês o array 7, eu vou ter essa fama no chão. Como ele é uma função, eu posso colocar essa função. Ele vai dizer que o retorno menor não nada, porque eu não passei nenhum parâmetro. Mas eu posso invocar essa função e passar um, dois, ele vai retornar três.

Ou seja, olha só que legal o que eu posso fazer com que ele... Olha, olha, que a gente está vendo algumas coisas de programação funcional no JavaScript, que isso aqui vai mais para frente. Como funciona isso, que é eu poder passar uma função com um parâmetro de um outro, de um outro método. Então eu tenho o método push, eu passei uma fase que tinha um pensamento, que depois desse fato legal, e eu consigo acessar ela a partir do meu array.

Mas basicamente a gente vai ver que agora é o método push. Os exercícios vão ser baseados nisso. Falando sobre o método push, a gente não vai falar ainda sobre passar a função por parâmetros, mais para frente, mas é legal você saber que isso é bastante possível. É bem possível.

Se você quiser, por exemplo, passar um outro array para dentro do array, você pode fazer também. Você pode adicionar qualquer tipo de valor: adicionar um menu, você pode adicionar um nulo no final também. Se quiser adicionar, o array ponto push. Se eu quiser adicionar um outro array, eu posso adicionar também. Você adicionar um array que tenha a, b, c. Eu posso adicionar qualquer tipo de valor utilizando o método push. Beleza? Bastante simples e bastante fácil de se trabalhar.

## A estrutura de repetição for

Até agora, vou conversar um pouquinho também sobre uma outra, uma outra estrutura de repetição. Onde conversou sobre a estrutura de repetição, eu agora vou conversar um pouquinho sobre esse futuro tinha pressão for. Eles têm basicamente a mesma ideia, que é gerar uma estrutura de repetição, mas ele tem uma sintaxe um pouco diferente.

Então a sintaxe do for é: você vai passar ali os parâmetros por fora. O primeiro parâmetro é o inicializar. O segundo parâmetro é uma condição. O terceiro parâmetro, a expressão final. Então, basicamente, o é que você vai fazer: o for, ele vai funcionar mais ou menos como funcionou. Só que tudo o que você faria fora do que você vai fazer dentro do for.

Então, por exemplo, quando você vai fazer um, eu ficaria lá em baixo: num igual a zero. Você faz o menor que 20, tem, enquanto ele for menor que 20, console ponto log mais mais, certo? Ele vai imprimir os números de 0 a 20, além de 0 a 19, no caso, porque ele imprimiu somente os números que são menores que 20. Como 20 é igual a 20, não é menor. Então ele imprimiu 20.

Como faço isso utilizando o for? É basicamente a mesma coisa, só que com o for que eu vou fazer: eu vou inicializar aqui. Então var igual a zero, ponto e vírgula, 3 para mim, se você para eu poder perguntar. Então var não é igual a zero. A minha condição é se o número for menor que 20. E o terceiro parâmetro ali, que é a expressão final, que eu vou concatenar, incrementar esse número. Então vou dar um console ponto log. Ele vai fazer para mim exatamente a mesma coisa que a gente tinha lá com o while.

Só que a única diferença é que a gente consegue colocar dentro da própria expressão do for todos os nossos parâmetros. Legal? Lá no ar, eu precisava declarar isso aqui fora do Rio. Isso aqui eu declarava dentro do eu e mais mais, e declarava isso aqui, declarava passando como parâmetro para o while. Isso aqui, aquilo, declarava dentro do while. Então, para você, [no] for, você já declarou as três condições de uma só vez.

## Várias variáveis na inicialização

Você vê que você primeiro faz a inicialização. Aqui você pode inicializar quantas variáveis você precisar. Por exemplo, onde eu posso iniciar duas variáveis, fazendo for, var um igual dois, rounds igual a três. Exemplo: enquanto não for menor que cinco, ou mais mais, enquanto ele for menor que cinco, ele vai adicionar e fazer aquela condição. Então que eu posso ter um console ponto log num, console ponto log no arroz, incrementar o arroz aqui também, se eu quiser. Se eu quisesse incrementar o arroz aqui em cima, eu poderia também incrementar aí. Basicamente isso que ele vai fazer: imprimiu num dois, ou num 3, e o arroz 4, 1, 4, ou 5. Beleza?

Então, basicamente, é isso que o for faz. Bastante sentido, bastante fácil de entender. Acho que ele ficou bastante fácil de compreender. Simplesmente modo estrutura de repetição, modelo estrutura de repetição, o que ele funciona exatamente como eu, só tinha uma pegada um pouco diferente, uma estrutura um pouco diferente do, do pai.

Então era basicamente isso que eu queria mostrar para vocês esse vídeo. Então, até o próximo vídeo, vai continuar com a nossa, com a nossa aula, nosso curso em JavaScript. Valeu, até.
