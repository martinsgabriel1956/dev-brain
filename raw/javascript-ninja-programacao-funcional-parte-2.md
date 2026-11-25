# JavaScript Ninja: programação funcional, parte 2 (funções que retornam funções)

Olá. Voltamos com o curso JavaScript Ninja, e eu sou Fernando Daciuk. E nós estamos falando sobre o retorno de objetos. [A] gente acabou de ver que a gente consegue retornar objetos a partir de uma função, e a gente também consegue, agora vai ver que a gente também consegue retornar funções diretamente [de] outras funções. Como assim? Isso a gente não viu ainda. Não vi, isso é algo novo.

Quem te viu mais, é uma das coisas que o poder de uma linguagem funcional nos permite fazer, como funções, como eu já falei, que funções são objetos de primeira classe em JavaScript. Eles fazem exatamente as mesmas coisas. Eles podem fazer, ou ser submetidos, às mesmas coisas que os objetos também estão submetidos. Então, da mesma forma, se eu consigo retornar um objeto, uma força, eu consigo fazer uma função retornar ao objeto, eu consigo fazer também uma função retornar uma, ou outra função. E qual a vantagem disso?

## Uma função dentro da outra

Ela só cria uma função e deu certo, e essa função vai receber um parâmetro. O retorno dessa função vai ser uma segunda função, que também vai receber um parâmetro, isso, e o retorno dessa segunda função vai ser o X mas o tipo B. Olha que loucura. Ficou difícil de entender?

Então vou mudar um pouquinho a abordagem aqui. Olha só: agora estou criando uma função dentro da outra função. E existe isso? Funciona? E eu consigo fazer em JavaScript? Sim, você consegue criar uma função dentro de outra função no JavaScript. Você não consegue torná-la, retornar uma função, porque você não conseguiria também criar uma função.

Então, por exemplo, eu tenho uma função, certo? Aí eu passo um parâmetro para essa função, que é o X, e dentro dela eu crio uma outra função, chamada de poder, onde ele vai retornar o Y. Essa idiota vai ser um retorno da EDP. É basicamente exatamente o mesmo exemplo que [a] gente fez aqui, só que aqui tinha uma função direta. Quem está criando uma função que vai retornar aos parâmetros, que vai retornar a ela sem executar, sem executar, porque a gente vai chamar ela na hora da criação dessa função, a gente vai, vai invocar ela.

## Para que serve: o add2

Beleza. Então vamos ver como é que isso funciona e para quê que isso aqui serve. Olha só exemplo. Então eu crio uma variável chamada add2, ou seja, em que ele vai adicionar dois, e eu passei a minha função e passei dois parâmetros. Ou seja, minha função agora é add2. Ela passou dois parâmetros. Voltando aqui no exemplo que eu fiz: e voltei essa função e passei o 2 aqui, preparando o retorno dela. Nada mais é do que uma função, certo?

Então, por exemplo, passei dois parâmetros, logo aquele meu add2, ele vai, ele vai ser uma função. Entendeu? Ele vai receber por parâmetro uma função executiva aqui. Passei um parâmetro, mas ela tem outro para mim, que ela recebe aqui, ali, uma segunda função. Está. Feito isso, aqui que eu faço: eu executa novamente o add2 e passa por parâmetro que o outro número tem como fazer. Eu vou somar 3 com o 2 que eu já tinha passado na primeira vez. Ou seja, eu passei o primeiro parâmetro e retornei uma função. No segundo parâmetro que eu for passar, eu vou, eu vou, então, na soma dos dois parâmetros que eu passei. Isso vai retornar para 25.

A dúvida? Eu sei que funciona. Vamos testar, então, como verificar se aquilo funciona mesmo.

## Testando

Então eu vou me executar aqui. Vamos limpar a nossa equipa. Vamos executar de novo. Como criar uma função chamada... que vai receber um parâmetro e vai retornar uma outra função, está? E olha só como eu estou fazendo um retorno de uma função: eu não estou criando uma função literal aqui. Eu estou fazendo a minha função, ela ser uma, uma instrução JavaScript, porque eu estou usando o return para retornar a ela. Eu preciso sempre colocar o ponto e vírgula no final. Ponto e vírgula é necessária, que é necessário que no final do ano.

Beleza. Então eu vou retornar essa outra função, vai receber um segundo parâmetro, y, e eu vou retornar o X mais Y. Essa segunda função vai retornar [x] mais y. Então o adder vai retornar uma função, e essa segunda função vai retornar a soma dos dois parâmetros passados. Isso aqui funciona.

Então eu vou dar um console.log, vou chamar que eu... vou criar uma variável, o primeiro, vai tu chamar o adder, eu vou passar dois pra ela. E agora eu vou dar um console.log, ele tirou três.

Eu vou mostrar a função aqui que eu criei. Então eu crio a função que retorna uma outra função, e essa segunda função retorna a soma dos dois parâmetros passados para as duas funções. Então aqui eu crio uma variável e passei o valor de dois como parâmetro. Logo, o retorno dessa função era uma segunda função, então o [add2] vai ser uma função. Eu posso passar mais um parâmetro aqui, que é, que vai ser esse parâmetro aqui. Passei três. Vou ver qual vai ser o retorno disso. Olha só: ele me retorna cinco.

## Só com funções de primeira classe

Ou seja, isso é algo que só linguagens que te dão o poder de utilizar funções de primeira classe você consegue fazer. Então tem algumas linguagens que você consegue fazer isso, e algumas linguagens de onde você só consegue escrever programação imperativa, você não consegue fazer algo assim. Você precisa passar os dois parâmetros aqui direto com ele. Por exemplo, eu uso algumas outras abordagens um pouco mais verbal. Então isso era uma coisa que eu queria mostrar para vocês. É algo bastante interessante da linguagem JavaScript.

## Duas invocações seguidas

E uma outra coisa, até para você entender melhor. Olha só o segundo exemplo que eu chamei web aqui, e ali ele não precisa necessariamente atribuir uma variável. Posso fazer duas invocações seguidas com JavaScript. Por que é que eu posso fazer isso? Porque quando eu chamo a função, é, certo, quando eu chamo a minha função e invoco ela, passo o primeiro parâmetro, a partir do momento que eu invoco ela, ela me retorna uma outra função. Então, se essa expressão aqui, o passo por parâmetro 2, retorna uma, ou outra função, essa expressão aqui vai me retornar uma outra função. Eu já posso invocar a segunda função aqui direto. Então, se eu fizer isso aqui, ele vai trazer para mim o mesmo resultado.

Vamos ver se aqui funciona. Como testar? Então ele tem que retornar pra gente outro. Sim, claro. Eu vou até usar outros números aqui pra você [não] dizer que estou roubando. Então vamos lá: cinco, vocábulo oito, por exemplo. Portanto, aqui você tem que retornar pra gente quanto? Cinco mais 8, 13, certo?

Então, que eu tô fazendo aqui? Eu estou fazendo aqui: eu estou invocando a função, estou passando o primeiro parâmetro, invocando ela. Ok. Passei o primeiro parâmetro. Esse cara que vai retornar uma função, logo eu posso invocar essa segunda função passando outro parâmetro, que vai, quando ele invocar, vai retornar para a soma dos dois números. Isso aqui tem que retornar treze. Vamos ver se isso aqui funciona de mídia. Olha só: ele retorna o 13 é pra gente. Que bacana.

Então essa é uma outra coisa legal que é, a programação funcional nos permite fazer, o JavaScript, como uma linguagem em que ele te permite trabalhar com programação funcional, exatamente por ter funções como objetos de primeira classe. Você consegue fazer esse tipo de coisa, em que tem muito mais coisas que ele consegue ver, muito mais coisa a gente consegue fazer. E no próximo vídeo vai ver mais uma coisa nova.

Então, nessa altura, você está vendo bastante coisas novas sobre funções, e na próxima, da próxima, no próximo vídeo, eles vão estar vendo como a gente consegue passar objetos por parâmetros, [a] gente também consegue fazer com funções. Beleza? Então eu vou te mostrar isso, mas no próximo vídeo. Beleza? Até lá.
