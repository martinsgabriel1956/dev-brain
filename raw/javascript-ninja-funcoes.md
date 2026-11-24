# JavaScript Ninja: funções

## O que é uma função

Olá, estamos de volta com nosso curso JavaScript Ninja. Meu nome é Fernando Daciuk, que nós estamos dando um giro pela linguagem JavaScript.

Nesse vídeo, nós vamos falar um pouco, então, sobre as funções. Que tinha falado sobre arrays, tinha avisos sobre variáveis, haviam falado sobre objetos, sobre alguns tipos de dados, e agora nós vamos falar sobre funções. Que são, o que são funções? E que é uma função social? Basicamente, um bloco de código JavaScript nomeado e que pode ser invocado usando o operador abre e fecha parênteses, certo? O que significa isso? Como é que funciona isso? Isso na prática.

Então eu tenho aqui o meu, o meu console. Não adianta, eu vou querer uma função aqui. Como é que cria uma função? Eu preciso da palavra-chave function, certo? Vou dar um nome para minha função, vou abrir e fechar parênteses e vou abrir chaves. Ok, dentro das chaves é onde vai todo o conteúdo da minha função. Nessa função não tem conteúdo nenhum. Então eu vou chamar essa função, e não na minha... Estou definindo, ok?

Como faço para invocar essa função? Eu vou usar o nome da função e usar o operador abre e fecha parênteses, que vai me retornar o valor dela. Como eu não tenho nada, o valor é indefinido.

Então o que eu preciso, com o mínimo básico que eu preciso para criar a função: a palavra-chave function, um nome para a função, abrir e fechar parênteses, é o uso blocos, ou as chaves, que é onde dentro deles é onde vai todo o conteúdo da minha função.

Ok, então aqui você viu como é que se invoque uma função: uso o nome dela e uso o operador abre e fecha parênteses. Ele vai retornar o valor da função. Se eu não usar o operador, o que acontece? Ele simplesmente vai me retornar a função. Ele simplesmente não vai executá-lo, o que tenho aqui dentro.

## Instruções e ponto e vírgula

Como vê na prática como é que funciona uma função com conteúdo, um bloco de código dentro de uma função? Então, vamos primeiro criar uma variável x e vamos dar valor para a linguagem.

Olha só, eu fiz uma coisa que eu não tinha mostrado nos outros vídeos ainda: eu coloquei um ponto e vírgula no final, no final da instrução. Aqui, estou aqui, são instruções. Instruções, na verdade, [são] uma sentença de código [que] eu estou fazendo. Então eu estou criando uma variável x, 7, chamando a palavra-chave var, criando a variável x e atribuindo a ela o valor 1, certo? Pelo que eu estou fazendo, trocando uma instrução a cada vez que eu crio uma instrução, a cada instrução. No final de cada instrução, eu devo colocar sempre um ponto e vírgula em JavaScript. O ponto e vírgula, você crente que ali finaliza uma instrução, ok? Em breve vai ver mais, também falar sobre o ponto e vírgula, sobre sob instruções, mas só para você saber.

Então, a gente criou algumas sentenças de código, que são as expressões, né? São as frases que a gente queria, que ela odeie mais dez. O X é igual [a] um, certo? Que são essas expressões, que são as frases em JavaScript, e a sentença é como se fosse... E as instruções são como se fossem sentenças completas de expressões. Então aqui eu estou fazendo, estou tirando uma variável x e atribuindo a ela um maduro.

## Funções reutilizam código

Agora eu vou criar uma função que ela vai somar. Ela vai se somar ao valor e ao valor dessa minha variável x. Então eu vou colocar o nome de soma e vou dizer que o X vai ser igual a x + 1, OK, e vou finalizar, que é minha função.

Se eu chamar o X aqui, eu vou ter o valor 1. Se eu invocar a minha função soma, a minha tornando, eu falei que eu não tem nem retornando nenhum valor dentro dessa função. Só que, se eu chamar o X de novo agora, o que é que vai acontecer? Ele vai ter o valor 2. Porque eu, X tem um valor 2 porque eu vou convoquei a função soma, 7, que faz o que? Faz o X, que está recebendo 1 aqui, receber todo o valor que ele tem mais um, certo?

O que vai acontecer se eu chamar de novo essa função? Qual vai ser o valor de x? Exatamente 3, porque o x se incrementado mais uma vez. Ou seja, funções são blocos de código que eu posso reutilizar. Então imagina a quantidade de código que a gente vai poder ter, em que a gente vai poder ter dentro de uma função, em que vai poder reutilizar isso. Entendeu? Você não vai precisar ficar digitando milhões de códigos aleatórios, você vai poder reutilizar o código que você tem através de uma função.

Se você chamar simplesmente soma, que algo vai acontecer? Ele vai chamar function. Se você chamar um X aqui, ele vai fazer, vai retornar 3. Por quê? Porque você não invocou a função, ele não executou esse código que está aqui dentro. Ele simplesmente retornou a função. Ele vai retornar esse bloco de código todo, mas não o valor que está aqui dentro, ele não vai interpretar isso daqui, porque você não invocou a função. Agora, a partir do momento em que você invoca a função, aí sim o código [é] executado e o valor de x muda agora para 4. Ok.

## Escopo

Então, que acontece? As funções, ou esses blocos de código JavaScript que podem ser nomeados, né, quem te deu o nome ao lado, nossa função soma, e que podem ser invocados usando o operador abre e fecha parênteses. Estão em TI, aprendeu agora mais um operador, que ela abre e fecha parênteses, que ele serve para invocar funções, com funções que tem o escopo.

Como assim, o escopo? Vamos ver na prática, então, é muito mais fácil. Criar uma função aqui. Eu tenho a variável x aqui já, certo, com meu valor 4, quadro que ele tinha chamado àquela hora. Que se ele vier aqui, teria uma função. Vou colocar um nome qualquer para ela, que função qualquer. Eu vou criar aqui dentro uma variável chamada Fernando, o valor dela vai ser string Fernando. Eu vou finalizar minha função, ok?

O que acontece? Eu queria que dentro dessa função uma variável Fernando. O que acontece se eu chamar a variável Fernando aqui? Vai dizer que Fernando não está definido. Por aqui, porque eu defini a variável Fernando dentro da função, mas estou tentando acessar ela de fora da função, eu não consigo. Porque as funções criam um escopo: toda variável declarada dentro da função, ela só existe dentro daquela função. Entendeu? Então o escopo da variável, ela depende da função que ela está inserida.

Se eu sei, se eu criar com uma variável X, que te criou no exemplo anterior, que é uma variável x, certo, que ela foi incrementada dentro da função: eu consigo acessar valores, variáveis, de fora de uma função dentro de uma função de script. Agora, valores que são criados dentro da função, como essa, essa variável Fernando aqui, eu não consigo acessar de fora. Aqui ele vai dizer sempre que eu falei Fernando, eu nem feliz.

Mas, e se eu invocar a função aqui? É a função qualquer: retornou undefined. Ok, então, teoricamente, esse valor que está valendo, certo, né? Não. Porque, ainda que eu tenha invocado a função, esse valor, essa variável Fernando, só vai valer aqui dentro.

## Retorno

Então, o que eu preciso fazer para poder acessar o valor de Fernando? É uma forma que eu consigo fazer para acessar aquele valor Fernando. Como eu criei, então, aqui uma outra função, qualquer dois, só para exemplificar. Vou criar aqui a variável Fernando, portanto igual a Fernando, aqui dentro da função. E eu vou utilizar a expressão return Fernando. Que o que eu estou fazendo? Basicamente, estou retornando um valor aqui.

Opa, mas eu não mostrei que Irina Shayk era o que eu mostrar, já que funções, elas podem me retornar valores. Então, além de se criarem em seu corpo, elas podem também retornar valores. Se você tentar acessar... Eu queria essa função com dois, tem uma variável chamada Fernando, com string Fernando, e estou retornando dentro da função essa variável Fernando.

Você pode ver aqui que a cada instrução... Essa primeira instrução aqui eu terminei com um ponto e vírgula. A segunda instrução também termina com um ponto e vírgula do, e tudo o que acontece no Titanic é o valor que funcionava. Então, se ela tentar chamar Fernando aqui fora da função, ele vai dizer que Fernando ainda não está definido. Mas, se eu invocar a função qualquer dois, ele vai retornar o resultado da variável Fernando, porque é isso que eu estou mandando ele fazer aqui. Usando a palavra-chave return, ele vai retornar o valor dessa variável Fernando. Ok, legal, né?

Isso traz, isso traz para a gente algumas outras possibilidades bacanas. Então, vamo, vamo, vamo, moleque. Mas uma coisa: eu, por exemplo, tinha uma variável Y que tem um valor, eu entrei no intervalo, 4, 7. Eu vou criar uma função com o nome cinco, ok, que ela vai retornar 5, simplesmente vai retornar 5. 7. Vocês chamam aqui, te invocar a função cinco: o resultado vai ser o número 5, ok?

Se eu chamar o y aqui, eu tenho o resultado 4. Se eu fizer y mais cinco, que não vale 4, o resultado vai ser, o resultado vai ser... Porque é, porque y vale 4, a função invocada vale 5, certo? E eu, somando esses dois valores, estou mais 5, eu vou ter o retorno de 9.

Então você entende a vantagem que vai ter funções para a gente: funções retornam valores, e funções que o escopo, e funções são blocos de código onde nós podemos nomeados, onde nós podemos ir buscá-los. Ok.

## Parâmetros

Funções também podem receber argumentos ou parâmetros. Como ver como é que funciona isso? Eu vou criar uma função aqui. Isso já cria soma, sim, tem uma função chamada pessoal. Então eu vou sair daqui e vou entrar de novo. Eu já não tenho mais o aqui.

Então eu vou querer uma função chamada soma, que soma, que ela vai receber dois valores, o X e o Y, que ele vai fazer? Ele vai me retornar o X mais Y. Que o que eu fiz aqui? Basicamente, eu queria uma função do nome pra ela de soma, e passei aqui dentro dos primeiros parênteses dois argumentos, que são... Esses argumentos são valores que eu vou poder passar para essa função quando invocar ela. E o que eu estou aqui, que eu estou dizendo? Estou dizendo que, quando eu retornar, quando eu chamo, quando invocar essa função, eu vou retornar somando esses dois valores que eu passei. Quero ver como é que funciona.

Então, se eu chamar a soma, que vai me retornar? Que não é número, porque eu mandei somar dois valores que eu não passei. Agora, se eu passar somar 1, 2, ele vai me trazer a soma do valor [1] e do valor 2, porque eu passei aqui dois argumentos. Esse NaN aqui significa not a number. Ou seja, não é um número exato. Isso é um valor também para quando eu não tenho, eu não tenho... Quando o valor está sendo feito uma expressão que deveria ser feito com números, que no caso aqui que a soma está, mas ele não retorna um número. Então ele vai retornar para esse valor aqui, ou not a number, ok?

Então aqui nós criamos a função soma, passamos dois parâmetros para ela: o X, que vale o X daquilo que vale [1], e o Y, que vale dois. E dizemos que a função vai retornar o X [mais] Y, então [1] mais dois, ou três, ok?

## Encerramento

Então, quem te viu que funções, eles podem receber também argumentos ou parâmetro, ok? Então, entendeu que funções realmente são coisas bastante poderosas, que a gente pode fazer bastante coisas com funções, que a gente vai de muito bom ouvir falar muito sobre funções durante todo o curso, tirar objetos de funções sobre isso br.

Por enquanto, ele está fazendo um apanhado geral aqui, durante todos, por todos esses anos, essas coisas por valores aqui, para se ter uma ideia, tem uma noção do que se espera pela gente, do que a gente vai trabalhar. Todos esses assuntos que estão sendo falados, sobre variáveis, sobre array, sobre instruções, sobre expressões, sobre funções, isso tudo a gente vai falar muito ainda durante o curso. Não é só isso que você vai ouvir e simplesmente vai ficar nessa. A gente vai ouvir bastante fala ainda sobre funções, como ouvir falar bastante sobre variáveis, e sobre expressões, sobre instruções, sobre objetos, sobre array. Vamos falar detalhadamente sobre eles; aqui foi só um apanhado geral, realmente, para você entender como tudo isso funciona.

Agora a gente vai partir pro desafio dessa semana, certo, que você vai executar. Só que o desafio da semana vai ficar para o próximo vídeo. Até lá.
