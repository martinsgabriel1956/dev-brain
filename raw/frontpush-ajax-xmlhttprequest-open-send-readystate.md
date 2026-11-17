# AJAX na prática: XMLHttpRequest, open, send, readyState e JSON.parse

Opa, olá pessoal, sejam muito bem-vindos à nossa aula de AJAX, onde nós vamos verificar, na prática, todas as três aulas teóricas anteriores. Então, onde eu falei de JavaScript assíncrono, falei de JSON, falei de APIs e requisição de protocolo HTTP, a gente vai juntar tudo isso. Nós vamos ver, na prática, como é que se dá uma requisição de maneira bem simples utilizando o AJAX, tá bom? Então, vamos lá.

## O que é AJAX

Se eu for traduzir o que é o AJAX, ele significa Asynchronous JavaScript XML, se eu fosse falar para você, é simplesmente o JavaScript assíncrono. É o uso do objeto XML HTTP request para se comunicar com os scripts do lado do servidor, quando você está requisitando, por meio de uma API, algum tipo de informação.

E a gente vai verificar, na prática, que no JavaScript, ao invés de a gente recarregar a página inteira para poder ter novas informações do servidor, que é o clássico do F5, para poder verificar de novo se tem mais alguma informação e forçar o JavaScript síncrono para poder fazer uma requisição, eu posso requisitar uma nova informação do servidor de maneira assíncrona. Então, nós vamos verificar agora isso na prática, bom?

## Instanciando o XMLHttpRequest

Então, eu vou abrir aqui o meu aplicativo, o nosso app.js, onde nós vamos definir uma constante que vai se chamar XHR. Ah, Násser, por que vai se chamar XHR? Vocês vão entender agora, porque eu vou atribuir para eles uma classe chamada XMLHttpRequest.

Ah, Násser, isso aqui é uma classe, você está instanciando uma classe, o que significa isso? Então, pessoal, sempre quando você estiver definindo uma variável, espaço, new, e atribuindo um método, que você entende que isso aqui é um método, consegue identificar porque ele fica azulzinho, tem o abrir e o fechado parênteses, isso aqui você está instanciando uma classe.

Uma classe, pessoal, literalmente, tem um conceito muito parecido com um objeto. Dentro dele tem métodos e atributos específicos dessa classe, que quando você instancia ela em alguma variável, automaticamente essa variável vira um objeto, um objeto que herda todas essas propriedades, esses métodos, esses atributos.

Então, quando eu vir aqui e, por exemplo, colocar XHR e acessar os métodos e os objetos com um ponto, olha só, tem muita coisa que foi herdada porque eu instanciei a classe nela, então ele virou um objeto de XMLHttpRequest, onde agora eu posso acessar os seus métodos, seus atributos para poder fazer uma requisição HTTP.

Lembra-se disso? A gente vai requisitar uma URL que é a API de um determinado servidor por meio de um protocolo de transferência de arquivos para enviar e receber dados, que é o protocolo HTTP, e ele vai me devolver alguma coisa, e essa alguma coisa é o JSON, então vocês entenderam?

## open, send e a aba Network

Para poder iniciar isso aqui, vamos utilizar um método chamado open. Dentro desse método chamado open, vamos estabelecer dois parâmetros. O primeiro é o método de acesso, no caso, eu estou só pegando uma informação, então é o método get, e aqui eu posso colocar o endereço da URL do API, que eu vou fazer com a própria do GitHub para poder ficar mais fácil.

E eu posso colocar aqui, além disso, eu tenho que definir aqui o send, onde como eu não tenho nenhum parâmetro, eu estou simplesmente querendo pegar essa informação, eu vou passar ele como null.

Vamos salvar, abrir aqui o nosso console, mais especificamente na seção de network, e aí você vai procurar por esse carinha aqui, XHR, que nada mais é do que a sigla de XML HTTP request, e vocês vão perceber que tem aqui uma requisição, se eu vir aqui atualizar a página, você vai ver que ela demora um pouquinho para fazer, não é instantâneo, ela executa a página e em seguida faz a requisição, só que como é muito rápido, parece que é instantâneo, mas ele fez essa requisição de maneira assíncrona, e quando você clica aqui, você consegue ver a resposta dela, qual é a resposta dela?

É justamente um arquivo JSON, está vendo? Olha só o jeitão desse arquivo, é um arquivo JSON, onde ele traz aqui as propriedades, se deu certo, se não deu, se essa requisição foi bem sucedida, ele traz todas essas informações aqui, onde a gente consegue tratar esses dados aqui no JavaScript, está bom?

## onreadystatechange, readyState e JSON.parse

Onde, para poder acessar, se deu certo, se não deu, para verificar isso aí, eu consigo acessar o XHR.onreadystatechange, o que isso aqui vai verificar? Como o próprio nome já diz, verificar quando o estado mudar, e aí eu vou lá e disparo uma função, function, onde eu posso verificar o seguinte, eu quero verificar o estado, o estado que me diz se deu certo ou não, está bom?

Por exemplo aqui, statusCode, está vendo que ele deu 200, requestMethod, get, ok, o requestUrl, então ele traz todas essas informações aqui, e uma informação que me dá se essa requisição deu certo ou não, por exemplo, eu verificar com a cláusula if, então vamos lá, if, e colocar aqui XHR.readyState, e aí ele vai me dar o código 4 quando der certo, e aí o que eu quero que aconteça quando ele der esse código?

Eu vou dar um console.log e vou plotar esse JSON aqui no console, mas lembre-se, ele me volta isso aqui como um texto, está bom pessoal? Isso aqui é um JSON, então é interessante eu transformar ele para objeto, utilizando o objeto JSON, e aí eu faço o parse, como a gente já viu, e aí sim eu consigo colocar aqui XHR.responseText, então ele vai passar o texto do JSON aqui, por meio dessa propriedade, dentro do método parse, que ele é um método utilizado que a gente já viu, dentro do JSON, que é um objeto próprio do JavaScript para poder tratar o JSON, e vai mostrar para mim no console.

Então, se eu vier aqui, ele já me trouxe aqui, justamente esse JSON aqui em forma de objeto, ou seja, eu consigo acessar isso aqui como um objeto, então qual é o meu avatar, minha bio, qual é o meu blog, a minha companhia, as outras APIs e tudo mais, então eu consigo acessar.

Então, basicamente, a gente fez tudo dos conceitos nesse simples exemplo aqui, beleza pessoal? Então falou e até a próxima.
