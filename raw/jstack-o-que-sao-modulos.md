# O que são módulos no Node.js

Nessa aula a gente vai entender o que são os módulos dentro do Node, então sem muita enrolação. Vamos lá.

## Preparando o ambiente

Eu criei uma pastinha chamada Modules, que é o tema dessa aula aqui, né? Mas você pode criar essa pasta com o nome que você quiser e onde você quiser, dentro do teu computador também, tá? Que não vai ter diferença nenhuma, tecnicamente falando. Você coloca aí onde você acha que fica mais organizado e mais fácil de você se encontrar.

Então vamos lá. Vou abrir essa pasta no meu VS Code, então comando code e eu passo o ponto aqui pra indicar que eu quero abrir a pasta que eu tô no momento aqui, lá dentro dele.

E aí, se esse comando code aqui não funcionar, aproveitando, o que você pode fazer? Você vai abrir o command palette que a gente já viu como é que faz, command shift P no Mac, control shift P no Windows e no Linux, ou então view E, command palette. E aqui dentro você pesquisa por install code. Aí vai ter essa opção, você seleciona ela, o VS Code já vai fazer as configurações pra você. E aí, se você fizer isso, voltar no terminal, e esse comando ainda não funcionar, o que você faz? Você fecha o terminal, abre de novo, porque daí quando você abrir, ele vai recarregar as configurações e aí provavelmente já vai estar funcionando aí pra você. Beleza?

## Executando um arquivo com o Node

Muito bem, então vou começar criando um arquivinho index.js aqui na raiz. E dentro dele, por enquanto, só vou pôr um console.log hello world. Vou salvar isso aqui, vou abrir o terminal do VS Code aqui, o terminal integrado dele, só pra gente não precisar ficar trocando de janela toda hora. Vamos esperar um pouquinho, show.

E como é que a gente faz pra executar um arquivo JavaScript usando o Node? Super simples, a gente só precisa executar o comando Node e a gente passa pra ele qual é o caminho até o arquivo que a gente quer executar. Então, no caso aqui, eu tô dentro da pasta Modules e o meu arquivo index também tá direto dentro dela, não tá em nenhum subdiretório ou coisa assim. Então, eu só preciso passar o nome dele, index.js, e já tá lá, hello world.

E aí, se a gente quiser, a gente também consegue omitir a extensão, tá? Então, se eu tirar o .js e deixar só o nome do arquivo, o Node também consegue identificar que é um arquivo JavaScript e executa da mesma forma. Mas particularmente, eu prefiro deixar sempre com a extensão, porque fica mais claro o que eu tô tentando fazer.

## O que são módulos

Bom, então vamos entrar no tema da aula agora, que são os módulos. O que são módulos? Módulos são conjuntos de código, ponto. Nem ponto e vírgula, é ponto, tá? Então, os módulos são literalmente conjuntos de código que a gente consegue ou não reutilizar. Eu sei que na teoria aqui pode ser que fique um pouquinho abstrato ainda o que é, mas quando a gente começar a desenvolver, você vai ver que é super tranquilo e bem fácil de entender.

Bom, e aí dentro do Node existem três tipos de módulos. Então, três tipos de módulos. O primeiro deles e o mais comum e o que a gente vai mais usar são os módulos que a gente cria. E dentro do Node, basicamente, eu vou até pôr em Caps Lock aqui ó, liga, liga Caps, aí. Dentro do Node, todos os arquivos JavaScript são módulos. Então, literalmente todo arquivo que a gente criar aqui dentro da nossa aplicação, pro Node, ele enxerga aquele arquivo como sendo um módulo. Então, aqui eu tenho meu index.js, é um módulo, se eu tivesse o abc.js seria outro módulo e assim por diante, beleza? Então, deixa eu apagar isso aqui.

Muito bem, qual que é o segundo tipo de módulo? O segundo tipo de módulo são os módulos nativos, que são módulos que já vêm dentro do próprio Node. A gente não precisa criar nada, a gente só importa eles e usa os métodos que eles já disponibilizam pra gente. Então, exemplo disso é o módulo de HTTP, que é o que a gente vai usar a partir da próxima aula pra criar um servidor HTTP usando o Node e tudo mais pra gente desenvolver a nossa API, beleza? Aí existem vários, tá? Existem um monte aqui dentro, módulo de sistema operacional, de DNS, do V8, enfim, tem muita coisa mesmo.

E o terceiro e último tipo de módulo que a gente tem são os pacotes do NPM, o NPM é o Node Package Manager. Então, eu não vou me aprofundar muito aqui no que ele é, porque nesse capítulo, eu vou tentar não falar módulo do curso pra não te confundir o que é módulo do curso e módulo do Node, mas nesse capítulo aqui do curso, então, a gente não vai estar usando o NPM, a gente só vai começar a usar dependências externas a partir do próximo capítulo do curso. Então, eu não vou me aprofundar nele aqui, eu vou deixar ele em Standby, mas só pra você entender, como eu falei aqui que a gente consegue criar os nossos próprios módulos, então todos os arquivos que a gente cria são módulos, o NPM é basicamente um lugar pra gente conseguir publicar esses módulos que a gente cria, esses arquivos JavaScript que a gente cria com a comunidade, e aí todo mundo consegue fazer a instalação deles, é basicamente isso o NPM, mas de novo, quando a gente for usar ele, eu vou retomar nesse assunto e aí eu me aprofundo um pouco mais.

## require e module.exports

Muito bem, deixa eu apagar esse arquivo aqui na verdade, e vamos começar entendendo então como é que funciona esse sistema de módulos. Eu vou criar um arquivo chamado printName.js, e aqui dentro eu vou declarar uma função chamada printName. Essa função recebe um argumento name e faz um console log nesse argumento que ela recebeu.

Show de bola, como é que eu faria, por exemplo, pra usar essa função printName dentro desse meu arquivo index? Se eu simplesmente chamar ele aqui, Mateus, e tentar executar isso aqui, ele vai dar um erro dizendo que printName is not defined, por quê? Porque a gente não criou, a gente não definiu essa função printName dentro do arquivo index, a gente definiu ele dentro do printName e o index ele não consegue enxergar o que tem dentro do meu printName.

Pra gente fazer isso, o que eu preciso fazer? Aqui dentro do meu index, a gente tem uma função chamada require, e é exatamente essa função que a gente usa pra importar todos os tipos de módulos. Então independente se é um módulo, ou seja, um arquivo que a gente criou, se é um módulo nativo ou do NPM, a gente usa a função require.

Bom, e aí no caso dos módulos que a gente cria, ou seja, dos arquivos da nossa aplicação, pra fazer a importação deles a gente precisa passar o caminho relativo. Então no caso aqui, o meu printName ele tá no mesmo diretório, no mesmo nível que o meu index.js, então eu só preciso passar um ponto barra, o próprio autocomplete aqui do VS Code já identifica que tem o printName aqui dentro e me sugere, então se eu der um enter, ele já seleciona pra mim, e nesse caso aqui a gente não precisa pôr o .js, pra fazer os imports aqui dentro dos nossos módulos, a gente só usa o nome do arquivo, beleza?

E aí a gente precisa salvar esse módulo dentro de uma constante, então vou criar aqui uma const printName igual a require printName. Só que se eu tentar executar isso aqui, olha só, ele ainda não vai funcionar, mudou o erro dizendo que agora printName is not a function, porque agora ela tá definida, então mudou o errinho ali. Porém, o que acontece? Por que ele ainda não tá funcionando?

Basicamente porque dentro dos nossos módulos a gente precisa dizer pro Node quais informações a gente quer que sejam acessíveis de outros módulos, ou seja, de outros arquivos, a partir de outros arquivos. Então como é que a gente faz isso? A gente faz isso dizendo o seguinte, o module.exports, então o que eu quero exportar de dentro desse módulo? No nosso caso aqui é o meu printName, vou salvar isso aqui e agora quando eu executar, tá lá o Mateus, que é a string que eu passei aqui dentro.

## Exportando mais de um dado

Bom, e se a gente quiser, por exemplo, exportar mais coisas aqui dentro? Então sei lá, eu tenho aqui o meu const lastName, vai receber, sei lá, Silva, tá, show. Então como é que eu faria pra exportar isso aqui? Muito simples, ao invés de exportar a função direto eu posso exportar um objeto e aí eu passo lastName, isso aqui é a short syntax do JavaScript, né? Então ao invés de a gente passar lastName, dois pontos lastName, quando o nome da propriedade é o mesmo nome da variável, a gente omite aqui e o JavaScript já faz isso por baixo dos panos pra gente.

Então, basicamente o que eu quero dizer é o seguinte, esse module.exports pode ser qualquer tipo de dado, ele pode ser a função, como a gente já viu, eu poderia passar lastName aqui, uma variável direto, um objeto, como a gente tá fazendo, né? Um array, uma string, número, enfim, literalmente qualquer tipo de informação.

Então no meu caso aqui eu tô passando um objeto contendo printName, lastName, se eu tentar executar agora vai dar um erro, por quê? Porque agora o valor desse meu módulo aqui é esse objeto e não mais só a função. Então pra acessar a função printName, o que eu precisaria fazer? Vou renomear aqui só pra módulo pra não confundir as coisas e aí eu vou ter o meu módulo.printName, vou salvar isso aqui, se eu executar tá ali o Mateus de novo e aí eu poderia usar template string aqui pra fazer interpolação, né? E pôr Mateus e módulo.lastName, você vê que o IntelliSense já identifica que o módulo no caso é um objeto e a gente tem printName, lastName dentro dele, vou salvar isso aqui, executo e tá lá o Mateus Silva.

E aí como isso aqui é um objeto eu posso muito bem chegar aqui dentro do meu import e fazer uma desestruturação em cima dele, né? Então puxar aqui printName e salvar na sua própria constante, e a mesma coisa pro lastName, aí na hora de acessar esses valores eu não preciso passar módulo. alguma coisa. Então vou executar de novo e continua funcionando, beleza? Então essa aqui é a primeira forma da gente exportar mais de um dado, então a gente declara eles aqui em cima, no final a gente exporta um objeto passando quais informações a gente quer externalizar de dentro desse módulo.

Ou então, né, a segunda maneira de fazer isso é a seguinte, ao invés da gente criar, declarar a função, declarar a constante e depois fazer o export, a gente pode simplesmente exportar no momento em que a gente tá criando, então eu dou um exports, ponto, e aí o nome da propriedade e o valor dela, né? E a mesma coisa aqui pra minha function, então exports.printName recebe uma function ou então posso deixar isso aqui um pouco mais enxuto e passar no formato de arrow function, se eu executar aqui tá lá funcionando da mesma forma.

## Módulos nativos

Bom, agora a gente vai falar um pouquinho sobre os módulos nativos, que na verdade não tem muito o que falar, é super simples, vou apagar tudo isso aqui e vou fazer o seguinte, ó, eu vou importar aqui dentro do meu arquivo index um módulo chamado os, que é de operational system, né, sistema operacional, vou dar um require aqui, como a gente já viu ele serve pra importar todos os módulos, e aí no caso dos módulos do node a gente não passa o caminho relativo, né, então ponto, barra e vai entrando nas pastas, até porque a gente nem sabe onde é que estão esses módulos de verdade.

Então pra importar módulos nativos do node, a gente só precisa passar o nome do módulo, então por exemplo os, e aí aqui embaixo se eu digitar os ponto, eu já tenho todos os métodos que eu tenho disponível dentro dele aqui no IntelliSense, né, eu quero pegar por exemplo o type e vou dar um console log os.type, vou salvar isso aqui, node index, e tá lá o darwin, né, que no caso é o do mac os, então essa aula é só isso, esses são os módulos do node, é super simples, eu só queria te introduzir antes neles pra você entender o que que é o tal do require que a gente vai usar bastante, o que que é o module exports, o exports, enfim, todo esse paranauê, e de novo a parte de NPM a gente vai entrar a partir do próximo capítulo do curso, então te vejo na próxima aula.
