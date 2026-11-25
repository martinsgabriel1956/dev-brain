# JavaScript Ninja: a importância de nomear funções

Olá. Voltamos com um curso de JavaScript Ninja. Eu sou o Fernando Daciuk, que é, após fazermos a revisão do desafio da semana 7, agora vai começar a falar sobre alguns assuntos novos, algumas coisas bem interessantes agora já JavaScript. E hoje a gente vai falar um pouquinho mais sobre funções. E funções? A gente não conversou sobre funções?

Sim, nós já conversamos sobre funções, mas já aprendemos a criar funções. Já aprendemos também que a gente pode atribuir funções a [variáveis], e as funções em JavaScript, como eu falei alguns, alguns, algumas aulas atrás, funções, na verdade, são uma das partes mais importantes da linguagem: as funções e objetos. [A] gente vai conversar bastante sobre isso. A gente vai usar bastante ainda funções e objetos.

Então hoje eu gostaria de entrar em algumas partes um pouco mais avançadas do uso de funções dentro do JavaScript. Nada que você não consiga fazer. Vai ser tudo baseado em cima do que a gente aprendeu, e já vendo algumas coisas novas e algumas dicas de coisas que a gente vai, que pode fazer, o que a gente deve fazer com as funções.

## Por que nomear funções

Beleza. Então, a primeira coisa que você precisa entender sobre funções: até agora a gente tem colocado, quando a gente atribui uma função a uma variável, no momento em que [a gente] tem criado uma função anônima, certo? Então, por exemplo, a partir de agora a gente vai procurar sempre dar nome às nossas funções. A gente vem sempre procurando nomear as nossas funções, e eu vou mostrar para você agora porque. Então, assim, como dizer que, um exemplo: a gente precisa sempre nomear. Ao invés de eu atribuir a uma variável e atribui uma função sem nome, uma função anônima, pra ela, eu vou fazer isso aqui: eu vou preferir colocar um nome com uma função. Então, vou criar uma variável, vou atribuir uma função chamada de fala, que também pode ser o mesmo nome da variável. De preferência o mesmo nome, para te manter, para ficar mais facilmente encontrada, a gente entendeu o que está acontecendo com uma função.

E por que a gente vai preferir sempre nomear uma função? Porque quando ele nomeia uma função, eu facilita o debug na função. A gente vai facilitar a depuração disso, ou debugar essa função. Quando a gente precisa encontrar erros, ou procurar por erros no nosso código, fica muito mais fácil encontrar um problema se uma função estiver nomeada, porque o debug, normalmente, ou do Node, ou do, do navegador, ele vai utilizar o nome da função pra poder debugar.

Mas se você atribui uma função a uma variável, eu não consigo invocar ela usando o nome da variável? Sim, a gente consegue. Só que [a] gente tem um problema, porque, como a gente conversou alguns dias atrás, a gente sabe que funções, elas, na verdade, são um tipo de objeto. Digamos que ele também é como o tipo de objeto no JavaScript: as funções, elas têm, elas podem ter propriedades e elas podem ter métodos também.

## A propriedade name

Então, ah, o próprio objeto de função, objeto de JavaScript, ele tem algumas propriedades e alguns métodos embutidos. O built-in. Então, é assim: um deles é o método name, que o método name faz e retorna o nome da função.

Então, por exemplo, como exemplo, eu tenho uma variável chamada func, e eu estou atribuindo uma função anônima a ela. Estou retornando Ray. Quando invoca a função, quando eu chamo func e uso os parênteses logo depois do nome da função, eu vou retornar, ou vai ser mostrado, ela vai ser avaliado pelo interpretador de JavaScript, e vai ser mostrado o retorno dessa função para mim. Então, se eu invocar ela, ele vai mostrar para mim o Ray, que é o retorno dessa função. E se eu chamar o nome da função sem invocar... Olha a diferença: ali eu estou invocando a função, ele vai retornar para mim o valor da função. Agora, se eu pegar a função sem colocar, ela é um objeto em que ela tem uma propriedade chamada name. Só que, como não nomeei a função, o name ele vem em branco.

## Testando no console

Vamos ver isso na prática, como é que funciona. Então, assim, eu estou aqui com o meu, com o meu terminal aberto, com, aqui dentro do console, onde a gente vai criar uma função. Aqui está uma função anônima que ela vai retornar exatamente o que, ele, mesmo exemplo. A gente vê lá. O que acontece quando invoco a função, ou seja, quando eu uso o parêntesis para invocar a função? Ele vai retornar para mim o valor da função. Ele retornou aqui o Ray, que é o retorno da função.

Agora, quando eu uso uma função sem executar, ela está sem invocar, invocação: invocação é você utilizar os parênteses logo após a função, é uma das formas de invocar a função. Então, se eu não invocar a função, eu tenho uma propriedade chamada name. Essa função está aí, você pode ver que a propriedade, que ela está aqui, porque eu não nomeei a função, eu passei aqui pra minha variável func uma função anônima, ou seja, ela não tem nome.

Eu não consigo invocar uma função que não tem nome. Eu crio uma função assim, eu não consigo invocar ela, já que ele espera que eu passo, passei um nome para essa função. Então eu preciso criar uma função dessa forma para que o JavaScript consiga criar sem dar nenhum erro, porque se eu não colocar um nome, eu não consigo invocar. Agora, a partir do momento em que eu coloco ela, que eu atribuo a ela para uma variável, então, simplesmente, eu consigo criar a função normalmente. Como ela não tem nenhum retorno, tentar invocar ela aqui, ele vai me dar undefined, porque eu não tenho nenhum retorno para essa expressão aqui.

Beleza. Então, acho que ficou, que ficou claro essa parte de quê. Então, por exemplo, eu chamava de espontânea: olha só, retorna o nome em branco porque eu passei, porque foi uma função anônima.

## Nomeando a função

Agora, voltando aqui, a linguagem: que acontece agora quando você nomeia uma função? Então aqui eu estou dando o nome de frente com uma função. E quando eu chamo de ponto name, ele vai me retornar exatamente o nome dessa função. Vamos testar, ver se isso funciona. Então vamos criar um var funcShow, também com o mesmo nome, vou chamar o name, e olha só: ele vai trazer para mim o nome da função. Ou seja, não é uma variável que ele vai trazer, é o nome da função mesmo. Entendeu?

Então, por exemplo, se eu criar uma fun, uma função chamada funcShow, por exemplo, está falando de... Quando eu invocar essa função, não vai retornar nada, porque ela não tem retorno. Mas se eu chamar o ponto name, ele vai retornar aqui. Só para você ver que, ainda que eu atribuo uma variável àquela função, a variável não quer dizer que o nome da função, uma variável só está recebendo. Mas ela está recebendo uma função anônima.

Então, a partir de hoje, todos os exercícios que a gente fizer, quando estiver criando função e a gente for atribuir uma variável, a gente vai sempre nomear a função. Beleza? Enfim, sempre dá um nome para a nossa função.

## Função literal

Mesmo esquema: se eu criar uma função literal — a gente vai ver depois o que, qualquer diferença de função literal, e por que existe a função literal, e qual outro tipo de função que existe também. Então, por exemplo, onde eu crio uma função literal, mais fundo são dois, só para você ver o detalhe, que são dois, se eu vou cair aqui. Como eu não atribuí a variável, vou invocar ela com o nome da função, estão falando que são dois. Invocar ela, vai retornar o resultado. E se eu chamar ela sem invocar, somente como um objeto, pegar para cuidar de mim, ele vai me retornar o nome dessa função como uma.

Então isso é pra você ver como que, qual a importância de você nomear uma função. Vai ter algum momento, em alguns casos específicos, que a gente vai usar funções anônimas? Sim. Funções anônimas é um recurso bastante interessante do JavaScript. Algumas linguagens têm, o JavaScript que também suporta esse formato de você utilizar funções anônimas atribuindo por uma variável, e a gente vai utilizar bastante esse formato também. Mas, quando você for atribuir uma função para uma variável, ou quando você cria, quando você tem uma função literal, você precisa nomear. Você sempre tem que dar um nome pra ela, mas quando for atribuir uma variável, você sempre também vai nomear essa função. Beleza?

Em alguns casos específicos a gente não vai fazer isso, mas na maioria dos casos agora a gente vai sempre nomear a função, a não ser que isso explicitamente seja dito, que aquela função não precisa de um nome, ela pode ser uma função anônima.

Beleza. Então a gente vai continuar falando um pouco sobre funções no próximo, no próximo vídeo. A gente fala um pouquinho sobre a programação funcional em JavaScript. Mas isso no próximo vídeo. Até lá.
