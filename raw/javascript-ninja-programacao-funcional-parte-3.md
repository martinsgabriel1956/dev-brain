# JavaScript Ninja: programação funcional, parte 3 (funções como parâmetro)

Olá novamente. Voltamos com um curso JavaScript Ninja. Eu sou o [Fernando] Daciuk, que nós estamos fazendo as loucuras de ver programação funcional em JavaScript. Olha que doideira.

Então, a gente já viu que a gente, com funções, elas são objetos de primeira classe de JavaScript: que você consegue criar funções literais [em] JavaScript, que você consegue passar funções por parâmetros, que você consegue passar, atribuir funções a variáveis, que você consegue retornar funções de outras funções, da mesma forma que você faz essas três coisas com objetos.

## Objeto como parâmetro

Agora [a] gente vai ver que você também consegue passar, da mesma forma que você consegue passar objetos por parâmetros para funções. Então, por exemplo, cria uma variável, que cria ali uma propriedade, qual é ela, está? Aí eu criei uma função de caracol, que vai receber uma variável ali, que é um objeto, mágico. Ela vai retornar ao marcar ponto, ou seja, vai retornar para pegar a color do objeto. Bem simples, coisa que a gente já fez [em] alguns exercícios anteriores. Então, basicamente, a partir do momento em que eu invocar o de caracol, ele vai retornar yellow pra mim. Estava a meu ver na prática como é que funciona isso.

Então, como estou testar aqui, vou criar aqui um objeto, que esse objeto vai ter uma propriedade color, se eu yellow. Beleza. Eu vou criar uma função também, chamada função de Caracol, Caracol, que vai receber um parâmetro, que vai ser o objeto, que o retorno vai ser esse objeto marcar ponto. Play. Beleza. Então criamos o nosso objeto, criamos a nossa função, e agora vai invocar a nossa função, mostrando no console, Guedes cola, passando o cara como parâmetro aqui pra ele. Vamos ver porque ele retorna.

Então ele só queria que a minha variável, o meu objeto com a propriedade color. Criei minha função de caracol e chamei a de caracol aqui, passando meu carro como parâmetro. Ele deve retornar a cor do meu carro. Vamos ver se aqui funciona à noite.

Olha só que a besteira que eu fiz: coloquei um ponto e vírgula dentro do objeto. Então ele disse que ele não esperava isso. Então vamos resolver esse problema. Vamos mover o ponto e vírgulas ali. Dentro do objeto não pode ter, não pode ter um ponto e vírgula. Eu fiz besteira, colocar o ponto e vírgula. Errei. E com agora. Agora, quando eu chamam de mídia, ele vai executar e eu vou mostrar para a gente o yellow, que é o gato de Cartola.

## Função como parâmetro

Então, da mesma forma que você consegue passar um objeto por parâmetro para uma função e manipulá-lo dentro da função, da mesma forma você também consegue fazer com funções. Você pode passar funções no parâmetro. Olha que doideira que você pode fazer aqui. Que só esse exemplo. Então vamos lá.

Tem aqui uma função chamada showFunction, que ela vai receber uma outra função por parâmetro, está? O retorno dessa choldra, eu falo que só vai ser a execução nessa função. Olha só que legal: eu recebo ela aqui como um parâmetro normal. Poderia ser qualquer tipo de valor. Poderia ser um array, poderia ser uma variável, poderia ser um objeto, poderia ser qualquer coisa. Mas eu posso passar uma função, e como é uma função, eu posso invocar. Como uma função, eu tenho o poder [de] invocar ela, para que ela retorne o que é, o que a função tiver jantar. Então o retorno dessa função aqui vai ser a invocação da função passando por parâmetro, que nós vamos passar aqui direto para a função.

Então eu tenho duas formas de passar. A gente pode, pode criar a função, [a] gente poderia criar uma segunda função aqui, passar. Ou isso pode passar como estou fazendo aqui: pode passar diretamente ela. Não preciso passar um parâmetro, colocar uma variável, ou passar o nome da função, não. Eu posso chamar direto showFunction, passar uma função como parâmetro, que monitora a função já está definido. E quando a invocar ela, ele vai então olhar pra gente. Vamos ver na prática como é que funciona.

## Primeiro formato: uma segunda função

Então eu vou lá. Vou criar aqui o meu aqui Bonilha de novo. Vou criar aqui uma função, uma função que vai chamar... Xô xô xô. Ou seja, a ideia dela é mostrar uma outra função, que ela vai receber por parâmetro uma função. Olha só que loucura é o retorno: o retorno dela vai ser a função executada. Simplesmente executar a função, que funciona essa eu não sei. Não tem essa função ainda.

Quais são as coisas, quais são os formatos que eu posso fazer para retornar isso? O que eu posso fazer para retornar? Primeiro de tudo, eu posso criar uma segunda função, que eu vou usar para retornar. Vou chamar de elefante, e vou retornar aqui fantochada. E quando eu chamá-la, o console.log, é invocar o showFunction passando por parâmetros rede internet. Sem invocar, e vou um infantil com os parênteses aqui. Passei por parâmetro de um restaurante infantil. Quando eu passei o showFunction, ele vai pegar alguém torno de um show. Aqui vai invocar ela. Quando ele voltar, ele vai retornar para minha área infantil. É isso que a gente precisa tê-la no nosso tempo. Isso aqui funciona.

Então aqui o conteúdo do nosso arquivo, que tem a função, e agora a gente vai executar esse cara, o arquivo, pra ver se ele vai retornar para a gente. Então a gente foi lá para internet: fantoche controlado com sucesso. Então isso que acontece. Então esse é o primeiro formato.

## Segundo formato: função anônima direto no parâmetro

Eu poderia também fazer isso aqui ao invés de criar uma nova função. Eu fui chamado direto aqui, por exemplo, console.log. Eu vou chamar essa função inteira. Olha só: o console é, e já recebe. Eu posso passar um parâmetro. Estou passando uma função preparando. Vou passar outra equipe show chão, e vou passar a função na internet direto aqui no parâmetro. Eu posso nomear ela, como não, tanto faz. Vou usar a função anônima aqui, só para ficar menos, menos coisa escrita para você, para facilitar a visualização.

Então, basicamente, eu estou fazendo um console.log na showFunction e passando, passando aqui a fantoche, uma, uma função anônima, sem nome, que ela vai escolher ficar aqui. Então, a partir do momento que ela for executada, ela deve retornar, ou até mudar, retorna aqui pra gente visualizar. Quero deixar igual, por exemplo, quando você não está. Então, quando eu executar o showFunction aqui, passando uma função por parâmetro, ele simplesmente vai retornar e ficar aqui. Vamos ver se funciona. Ponto js. Ele retorna ao fórum profissional assim. Olha só que legal.

## Fecho

Isso é pra você ver o poder que a gente tem utilizando o formato de programação funcional. A gente usa esse formato, a gente vai ver, a gente vai falar muito sobre isso no curso. Vou conversar muito sobre isso. Em seu oitavo aula, e ele vai ter mais ou menos umas 30 aulas, um total do curso. Então a gente vai ver muito ainda. Tem muita coisa ainda sobre objeto, muita coisa pra gente vendo uma programação funcional. Tem bastante coisa pra gente ver. Então isso [a] gente vai conversar bastante sobre isso aí, a gente vai passar bastante por isso.

Se você ficou com alguma dúvida disso aqui, você me avisa, pra gente poder resolver tudo. Então era isso que eu queria mostrar pra vocês nesse vídeo. Então, até o próximo vídeo, onde nós vamos mostrar o desafio da semana, ok? Valeu. Até lá.
