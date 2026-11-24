# JavaScript Ninja: tipos de dados e objetos

Olá, voltamos com a nossa terceira aula do curso JavaScript Ninja, ou melhor, Fernando Daciuk. E agora nós vamos conversar um pouquinho sobre tipos em JavaScript.

## Tipos primitivos

Em JavaScript, pode ser para eles, ou basicamente [a] gente pode dividi-los em duas categorias principais, que são tipos primitivos, tipos de valores primitivos, e tipos de objeto. Que são esses tipos primitivos e tipo de objeto?

A gente já viu os tipos primitivos [d]o JavaScript, como funciona: que o number, ou seja, um número qualquer, o número decimal, o número inteiro, número decimal, que no caso da chamada é conhecido como float do JavaScript; gerando um número inteiro, mas que na verdade é qualquer coisa escrito envolto por aspas duplas ou simples, ou apóstrofo, no caso aspas simples, um apóstrofo; um valor bool ou booleano, que é true ou falso.

Os valores especiais null e undefined. Especiais, já viu que o Nei define direção, não significa ausência de valor, mas você precisa explicitamente declarar ele, quando o melhor, você explicitamente atribuir ele é uma variável, quando você vai utilizar.

O nu é uma falha de quando uma propriedade, um argumento de função não existe, uma variável não existe. Ele é diferente, ou você pode ainda passar esse valor no referendo, mas o valor não é. Basicamente, ele significa que um valor não foi passado ou não existe para ela, para que ela variável, por aquele argumento. E o null, quando você passa esse valor dizendo a esse cara que não tem, não tem valor, e não tem valor nenhum.

Então esses são basicamente dois tipos de dados primitivos que você consegue utilizar dentro do JavaScript, e todos os outros tipos de dados, eles são objeto. Então tudo o que não for também string, boolean, ou falso, null, undefined, ele vai ser um tipo de objeto.

## Objetos

Ele vai ser o objeto dos objetos, eles são uma das partes mais importantes dentro de JavaScript. Basicamente, tudo o que foi trabalhar juntos tinha uma linguagem orientada a objetos. Basicamente, tudo que faz a gente vai fazer trabalhando em cima, em cima de objetos.

E o que [é], na verdade, o objeto? O objeto, ele é um conjunto de propriedades, e essas propriedades, elas podem receber o nome. Elas podem, não, devem receber o nome e um valor. É esse, esse valor que elas recebem pode ser tanto um valor primitivo, como um número, string, um boolean, falso, ou numa fase de web, ou ele pode ser um outro objeto.

Então vamos ver na prática como funciona um objeto. Então assim, a criação do objeto, serviu como funciona com gente estava dando um giro pela linguagem. A gente viu que a criação do objeto a gente faz utilizando as chaves. Então você utiliza chaves, você cria uma propriedade, dá o nome de uma propriedade, dois pontos, o valor da propriedade. E assim eu criei o meu objeto com uma propriedade chamada propriedade, ok.

Se eu quiser, eu posso atribuir também um objeto ou uma variável. E então eu vou criar uma variável chamado objeto e vou atribuir a ela um objeto com as propriedades, de propriedade que ela vai ter. Mas como o valor foi seu valor é sonho. E vou colocar também uma outra propriedade.

As propriedades no objeto em JavaScript, elas são separadas por vírgula, e o valor, ele é citado, ou ele é atribuído a uma propriedade, com dois pontos, quando você usa dentro dessa notação de objeto. Então eu tenho propriedade de valor, vou criar propriedade 2, que vai ser um número, 10, eu vou criar propriedade 3, que vai ser true, tá.

E agora eu tenho um objeto. Quando acessa esse meu objeto, eu vejo que ele tem três propriedades aqui: a primeira propriedade, chamada valor, mas tem valor; a propriedade 2 é o número, e o número 10; é a propriedade 3, e o valor booleano.

Então isso aqui é onde já tínhamos scripts. Como que eu faço, por exemplo, para aquilo que serve exatamente o objeto? Então, para que eu vou usar o objeto, momento eu vou precisar utilizar o objeto? Basicamente, um objeto, você vai utilizar ele para organizar os seus dados, principalmente nas próximas a ele, para, para ordenar os seus dados, o seu código, e seu objeto. Basicamente, ele se, ele se diferencia objetos da vida real.

Então, por exemplo, eu tenho um objeto aqui e eu tenho essa propriedade. Eu quero acessar o valor de sua propriedade: como faço para acessar esse valor? Eu utilizo essa questão não está aqui: objeto ponto propriedade, está. Ele vai me dar o valor da propriedade.

## Exemplo: pessoa

Dando um exemplo um pouco mais humano da coisa, só para você entender mais ou menos como que funciona, porque não houve um objeto chamado pessoa, e essa pessoa, ela vai ter algumas propriedades. Quais são as propriedades dessa pessoa?

Ela vai ter o nome, certo? E o nome dessa pessoa: Fernando, sou eu. Ela vai ter uma idade, e a idade dessa pessoa é 30. Ela vai ter um peso, e o peso dessa pessoa é 85, 85 quilos, vou passar com o número aqui. E é altura: dessa pessoa vai ter uma altura, e essa altura e um metro. Eu tenho muito tempo.

Então eu criei uma variável chamada pessoa, e essa variável tem um nome, ela tem uma idade, ela tem um peso e ela tem uma altura. Que se chama pessoa, que eu vou ver que tem um objeto, meu bilhete completo.

Então eu tenho um objeto chamado pessoa. Eu quero saber o nome da minha pessoa, como eu faço? Pessoa ponto o nome: Fernando, legal. Eu quero saber qual é a idade dessa pessoa: pessoa ponto idade, 30. Está a altura dessa pessoa: pessoa ponto idade... pessoa ponto a altura, 85.

Então assim, é para isso que serve o objeto, objeto. Você vai colocar a propriedade pra ele, essas propriedades vão fazer referência em seu objeto. Então basicamente, basicamente isso. No caso, no exemplo aqui, eu criei um objeto chamado pessoa, que ele tem alguma, ou algumas propriedades aqui, no caso se referindo a mim.

## Exemplo: carro

Mas eu posso criar também um objeto chamado carro, e ele vai ter também algumas propriedades. Eu posso colocar a cor no carro e dizer que ele vai ser vermelho. Eu posso colocar o motor, que ele vai ser o motor dois pontos zero, por exemplo. Vou passar sim, porque nisso aí, sim, porque ele... Porque se eu colocar dois pontos zero, ele vai colocar como no meu entender. Então eu vou colocar como string, a cor vermelho. Vou colocar aqui quantidade ou... quatro.

Eles, eu tenho um objeto chamado o carro. Ele tem a cor vermelho, ele tem um motor de 11 pontos, ele tem quatro portas. Certo? Um carro cor vermelho, motor dois ponto zero, e tem quatro portas.

Se eu quiser saber quando o carro, me faço carro ponto cor, ele vai me retornar aqui: vermelho. Quer colocar o carro ponto motor, para saber o tipo de motor do carro: tem o motor do carro. Um porta: vou ter quatro portas. Então, basicamente isso.

Basicamente, o objeto vai, ele vai guardar a propriedade para si. Parece bastante simples, mas a gente vai ver que isso vai ter um valor bastante útil para gente, todo, em todo o nosso aprendizado com. Isso aqui parece algo bastante simples, mas, mas algo bastante legal de fazer, tá bom?

## Funções como objeto

Então, por exemplo, eu tenho lá a minha pessoa. Fernando Pessoa. Eu tenho lá o meu objeto pessoa, Fernando, por exemplo. Eu tenho essas, essas propriedades, mas eu falei que o nosso objeto, ele pode receber tanto uma lei permitindo, que estou passando aqui, como string, e estou passando um número aqui, como ele pode também receber, como ele pode também receber um outro objeto. Outro tipo de objeto.

Quais são esses outros tipos de objetos? Um tipo de objeto que já trabalhou, a gente tinha trabalhado, são as funções. Então o function, na verdade, ele é um tipo de objeto. A gente vai ver depois que funções são objetos de primeira classe [em] JavaScript. E por que eles são objetos de primeira classe? Porque eles podem ser atribuídos a variáveis. Você pode atribuir uma função a uma variável, ou ao objeto, no caso.

A gente vai ver aqui, por exemplo: vou criar uma variável aqui chamada me, vai atribuir essa variável uma função sem nome, uma passar no mínimo um pra ela, que eu vou querer uma função anônima. Se a gente não viu ainda, estou voltando agora para você.

Vou criar uma variável chamada Mãe, vai criar uma função que eu vou retornar uma historinha aqui, que vai ser variável, mas vai estar esse fim. Então o que acontece? Chamou mais valia, ele vai retornar que o Mano vai, na verdade, uma função.

Então assim, ele, uma função que ele não tem, ele não tem nome, é uma função anônima. Em JavaScript você pode fazer isso, não é obrigatório o nome. Quando você usa a função, quando você atribui a função a uma variável, não é obrigado, não é obrigatório a função tem um nome, e ela vai ser uma função Malta. Como, como faço para diferenciar essa função? Eu vou utilizar o próprio nome trabalhado para chamar essa função aqui.

Então, por exemplo, eu tenho vocação: se chama essa variável mas, vai invocar ela. Ela é uma função, então pode usar o operador de invocação e função, que algo vai acontecer: que ele vai retornar um valor na função. Olha só que legal.

Então a gente viu mais uma forma de, mais uma forma de gente que há funções. Como falar um pouquinho mais sobre funções, mais, é isso que vai fazer no nosso próximo vídeo. Até mais.
