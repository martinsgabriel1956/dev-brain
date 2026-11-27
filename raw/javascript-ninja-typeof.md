# JavaScript Ninja: o operador typeof

Olá. Voltamos com o curso [de] JavaScript Ninja. Eu sou o Fernando Daciuk, que agora vou conversar um pouco sobre como testar tipos de valores. JavaScript [tem] alguma forma de testar tipos de valores, por exemplo, para saber se o valor é um número, um valor, o mais alto índice, um parâmetro passado na função, quando uma função recebe esse argumento. Ele é uma string, ele é um número, ele é um Boolean? Tem que fazer isso se no JavaScript.

## O operador typeof

Nós temos um operador unário, typeof, seu operador. Basicamente, ele fala: ele é um operador unário, que ele funciona só, ele é um operando, onde você passa o operando para ele. Ele vai te dar o resultado, ou o tipo desse operando.

Então, basicamente, alguns exemplos que a gente tem é que, se você, por exemplo, passar undefined, ele vai retornar para você. Se você passar o tempo todo e passar como operando uma função, ele vai retornar a uma falante. Se você passar um tempo novo com valor true ou false, ele vai retornar que é o Boolean. O typeof ficou um número ou o NaN, ele vai retornar que o number. Está typeof ficou mais literal, ele vai retornar mais tarde. E qualquer outro objeto que não seja uma função, ele vai retornar, tornar objeto.

Então, qualquer tipo de objeto. Por exemplo, se eu tiver um objeto, um objeto mesmo, objeto vazio, objeto preenchido, ele vai retornar como objeto. Se eu tiver um array, ele vai entender como objeto. Se eu tiver null, ele vai retornar como objeto. Eu parei null, null, ele retorna como objeto. Como assim? Por que é que ele retorna o objeto? Na verdade, isso é um erro na implementação do vídeo clipe de JavaScript, que tem um erro na sua implementação. Aqui, quando você usa o typeof null, ele vai retornar para você o objeto, está?

## Na prática

Então, vamos ver os exemplos de forma prática aqui. Então, por exemplo, se usar o operador typeof com um número, ele vai entrar naquele mercado. Da mesma forma, se eu usar o NaN, ele vai entrar na câmera, porque a gente já viu lá atrás, quando a gente estava vendo, falando sobre o tipo de dados, que o NaN é também o número. Pra gente saber se realmente ele é o número, para tirar a prova real, a gente pode utilizar o typeof, que ele vai dizer para gente o que eu que careta.

Então, eu posso usar um typeof 'JS Ninja' aqui, passou, mas ele vai dizer com mais string. Você, eu posso saltar undefined. Ele vai dizer que é do tipo undefined. Você vai passar o tempo de passar a mão no chão aqui, ele vai dizer também que uma fantochada. typeof objeto, ele vai dizer que o objeto está pior. Ele disse que o objeto está aí, então cuidado com isso. Cuidado quando você pode testar objetos, isso é typeof. Ele retorna o objeto.

Isso, na verdade, é um erro da implementação do JavaScript, que já está documentado. Isso está na documentação do JavaScript, que foi feito nas primeiras implementações de JavaScript, que o typeof retornaria como objeto. Na versão 6, eu acredito, ele vai vim já com essa versão já corrigida. Então, até por fim do ano, não vai retornar um objeto. Então, você não procura não testá-lo, e não testar o objeto usando o typeof.

Você me pergunta: mas eu posso confiar no typeof, então, já que a está no objeto, novamente tornar o objeto? Tem como eu confiar no typeof? Você pode confiar no typeof se você for utilizar ele para valores primitivos.

## typeof para validar argumentos

Então, por exemplo, quando você estiver usando ele com o número, por exemplo, você tem uma alma, digamos, você vai querer uma função, criar um arquivo que pode apagar o conteúdo dele, e vou fazer o seguinte. Digamos que você tenha lá, sei lá, uma função chamada sum, porque ela vai receber o número dois, e essa falha você vai retornar somando mais dois. Basicamente isso. Se você der um console.log, chama, invocando essa função, e passar por parâmetro 10, 2, então o que é que vai acontecer? Quando você invoca a função, ela vai retornar a soma desses dois números, certo?

Só que esse, por exemplo, eu fizer isso aqui: console.log, aí eu vou chamar a função e vou passar, por exemplo, 'JS', 2. O que vai acontecer aqui quando eu achar humanoide ninja? Olha só, ele vai concatenar os valores. Porque eu posso ser mais amigo, estou passando um número, certo? Se eu fizer uma implementação mais ou menos assim do seu passado, eu passar aqui um objeto vazio, passam um array, será que vai acontecer se eu pudesse aqui? Olha só, ele vai retornar, na verdade, é um objeto, porque ele está tentando somar dois objetos. Ele retornou o objeto aqui.

O que vai acontecer se eu fizer, por exemplo, isso aqui? Vou mudar a implementação da função. Vou chamar ela de subtract. E aqui eu vou passar o menos em vez do mais. Que vai acontecer quando eu chamar esse cara? Que, olha só, agora me deu erro, porque ele disse que o não faria. Obviamente, falando, agora não é mais. Agora chama subtract, e chamar esse cara aqui. Que vai acontecer? Olha só, ele vai, ele vai me retornar para os dois.

Porque, se lembra, que o operador de mais, ele tem uma sobrecarga. Ele, o operador mais, quando você tá usando com isso, o que você usa com algum outro tipo de objeto, ele tenta fazer um outro tipo de operação. A gente vai ver o que aconteceu lá, que ele converteu. Ele se tornou objeto, que a gente passou um objeto e um array. A gente vai ver depois, nas próximas aulas, como funciona as conversões em JavaScript, este tipo de conversão, como o que ele faz quando eu somar um objeto com array, está mais aqui. Por exemplo, quando você tenta somar strings, ele vai converter string.

Só que quando você usa o operador menos, operador menos, ele não tem essa sobrecarga. Ele vai simplesmente, ele, ele espera que sejam dois números, e que esses dois domínios sejam eles, e eles sejam operadores base de números mesmo, para poder efetuar a operação de subtração. Nesse caso, você deu um kit ninja, que você pode ver que ele está esperando dois números para diminuir o valor, o valor do número menos número 2. Mas eu estou passando aqui mas tinha, que eu estou passando um aí, um bilhetinho rei, e ele retorna NaN, ou seja, um retorno. Na verdade, ele está dizendo que não é um número.

Como o que eu faço para prevenir isso, para não deixar que isso aconteça? Eu posso utilizar o operador typeof. Então, nesse caso, aquilo que eu posso fazer, eu posso fazer isso aqui primeiro, para verificar: não está off é igual a um estado que está typeof num2 e igual número, se eu até ao final muito typeof num2 foi igual. Aí ele vai olhar pra mim. Aí ele vai então olhar pra minha, os dois números, os dois números fazem a operação correto. Então aqui, se eu pior, se o tipo do número um foi, ele também é o tipo do número 2 também Fernando, aí ele vai retornar a diminuição dos dois. Não, vai retornando e falha.

Então, se eu chamar aqui ninja, olha só, eu estou no 8 aqui, era a primeira soma que eu tinha feito, que era o 10 menos 2, eu estou no 8, e aqui estou undefined. Inclusivamente, pode até criar uma mensagem personalizada, se a gente quiser. [A] gente pode personalizar o retorno. Aqui a gente pode dizer que, se ele não, não for, não, ele vai retornar "com dois números". E quando eu achar uma aqui no inimigo, olha só, ele vai passar 8, e se eu não entrar com dois números, ele vai pedir outro, "com dois números", não entrar com dois números. Então ele não vai estourar o valor correto.

Então, basicamente, essa ideia do operador typeof dá pra você testar o tipo de um, de um determinado valor dentro do script. Então você pode, você pode testar a ideia que você usa e ele testar valores primitivos. Testando valores primitivos, você garante que você vai conseguir realmente ter um resultado esperado. Se você foi testar, por exemplo, por um objeto ou por um array, você vai ter o retorno do objeto. Então, se você quiser saber se é realmente um array, você precisa fazer outros tipos de teste. [Se] quiser saber se [é] um objeto mesmo, precisará fazer outro tipo de teste.

## Testando null

Se eu quiser saber, por exemplo, se eu quiser saber se eu nunca vou entrar aqui, por não saber, se o typeof está que ele, então, no objeto. Agora, para saber se ele realmente é nulo, o que eu preciso fazer? Digamos que você tem wi fi lá. Eu faço está typeof, criar uma função, que fica mais fácil de entender.

Agora que criar de novo, eu vou criar aqui uma função para retornar, porque eu vou ter uma função subtract aqui de novo. Ela vai receber dois números, em torno dela vem sendo menos 1/2. Só que se, por acaso, o valor repassado para mim não foi, digamos que o valor passasse, o valor passado for null, eu também quero, quero testar, quero verificar. Aí vou dar uma mensagem retornando, dizendo "não entrei com valores nulos", tal como acontece o seu sou um bailarino.

Então vou testar typeof, por exemplo, igual object, que eu posso testar se ele vai ser igual ao object, que ele vai ensinou, e se o está typeof do que no ano. Então vou saber exatamente o que eu posso testar assim. Posso estar diretamente falando também, não preciso nem notar que, nesse caso, está aqui, eu consigo testar pra saber se o valor realmente ele é nulo, ou ele anda falando que, se eu quiser testar se o valor foi entrado, não foi entrado nesse valor, é falso.

Se você simplesmente, é falso, simplesmente posso colocar um not aqui na frente. Ele vai testar se o valor não é igual a zero, se o valor não é uma string vazia, e o NaN, é o falso, onde fala na ONU. Agora, se eu quiser testar explicitamente pelo valor null, aí eu tenho que utilizar o operador, e o operador de igualdade estrito, o estético, e verificar se o valor realmente está. Se ele for null, ele vai me retornar "não entro com valores nos Estados".

Então aqui eu posso dar um conselho de alguém que, por exemplo, subtract 10, 5; console.log null, 2, por exemplo, aquilo, porque ele está não só pelo valor. Então que gente, que para visualizar o arquivo, certo? Então tem que a função subtract, se o valor num1 for null, ele vai retornar "não entra com valores nulos", senão ele vai retornar a subtração dos dois valores. Que eu estou forçando um valor não sendo pra realmente ele entrar naquele valor. Então não era só ele, mas então eu não, "não entro com valores".

Então, a forma mais correta de você testar, hoje, foi o valor null e você testar se aquele valor é realmente nulo, ou, então, você testar se aquele valor, sem aquele valor, ele, ele não tem, não, não tem nada, ele é um valor falso. Se você testar com a exclamação, aí você consegue testar essa, que aí ele testa todos os tipos de valores falsos.

## A dica

Então, fica a dica para você: sempre que você utilizar o typeof, procure utilizar ele com valores primitivos, de preferência número, string e Boolean. Só esses três tipos de valores, você pode ter garantido que você nunca vai ter problemas com ele. Está construindo e Boolean. Beleza? Para outros tipos de valores, [a gente] vai ver mais pra frente como testar outros tipos. Beleza, então era isso que eu queria mostrar pra você sobre o typeof, e até o próximo vídeo. Olha, eu até lá.
