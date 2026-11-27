# JavaScript Ninja: hoisting

Olá. Voltamos com um curso JavaScript Ninja. Eu sou o Fernando Daciuk aqui, e no último vídeo nós falamos sobre hoisting, e você ficou curioso para saber o que acontece. Ficou curioso para saber como é que funciona. Quem se é. Digo isso porque uma função era só a exemplo de quem estava vendo, né?

A gente tem uma, duas variáveis sendo declaradas, e fazemos o retorno de uma função que nem sequer existe ainda. E logo depois do retorno a gente cria uma função, e ela funciona quando a gente executa, quando a gente invoca ela. Por que isso aqui funciona?

## O que é hoisting

Então, eu estava explicando no vídeo anterior que isso, na verdade, esse efeito, essa funcionalidade do JavaScript, significa... que significa royalty na tradução literal. Augusto citou alguns tradutores de livros, de alguns, de alguns artigos sobre novos escritos, que traduzem isso como içamento ou elevação: algo que você está movendo para cima. Então, basicamente, é isso que faz, o que acontece num código JavaScript.

Quando você tem uma variável declarada... a gente viu algumas aulas atrás que, quando você declara uma variável... quando você declara uma variável depois, o que acontece: em JavaScript, pega essa variável, move para cima como um undefined, e depois, naquele ponto da variável, que ele atribui valor. A gente vai ver mais um exemplo disso aqui.

## Função literal × função atribuída a variável

Mas o que acontece, o que acabou acontecendo com funções? O que eu faço: ele simplesmente, se ele tiver uma função literal dessa forma, não é uma função atribuída [a] uma variável. Que você atribui [a] uma variável, não vai funcionar. Eu já vou mostrar isso. Isso acontecendo.

Mas assim: quando eu tenho uma função literal em JavaScript, ainda que eu retorne, ainda aquele que chame, ela cria ela depois de uma instrução britânico, uma vez que depois ele pega essa função e moda aqui pra cima. Então, basicamente, uma que eu faço aqui, você criou assim, mais que JavaScript. Isso aqui, aqui, na verdade, é isso, é isso que, que acontece com o JavaScript. É exatamente aquilo, exemplo que a gente tinha anteriormente.

Ou seja, se eu criar ela depois, ou se eu criar as minhas variáveis aqui antes, por exemplo, o JavaScript sempre vai fazer isso com a gente, pois sempre que tiver uma função literal, ela vai valer para todo o escopo da função.

E olha o que acontece. Vamo, vamo fazer algum sucesso daqui. Por exemplo, aqui a gente cria uma função dessa forma, e dessa forma perceber o que funciona. Então vou, uma técnica, eu vou mostrar pra você aqui que a criação da função sum depois do ano, certo, será executado único, e ele vai funcionar.

Agora, se eu criar uma variável aqui, por exemplo, e atribuir a função sum a essa variável sum, teoricamente para funcionar, já que ele faz o que ele faria, ele perderia essa função de, iria pra cima, certo? Mas olha só o que acontece nesse caso. Ele disse que anda falando "is not a function". Ou seja, agora ele disse que a função sum não existe. Porque, quando eu tinha uma literal e uma função, o JavaScript conseguiu fazer o gol e jogar para cima. Mas a partir do momento que eu atribuo isso a uma variável, que você não consegue entender... Mas o que acontece, na verdade, qualquer funcionalidade, uma vez que ele interpreta, ou como aquele que ele faz essa função funcionar.

Na verdade, isso aqui, coloca um comentário, que só para você poder visualizar. Vou criar aqui a função mais de juntar... myFunction. Ora, se alguém com JavaScript te faz, basicamente: se eu tenho exatamente essa linha aqui, o que você vai fazer? Ele tem uma variável. Ele vai atribuir... o que ele faz: ele pega todas as funções, funções literais, e joga pra cima, tapa a primeira linha da função, ou o início da função. Então, qualquer função literal, ela está disponível dentro do escopo de, ela estar disponível dentro de todo o escopo.

Então, basicamente, que acontece: eu chamei o var aqui, e ali ele... Ele conseguiu chamar, ele criou o número um e atribuiu ao number1, porque essa minha atribuição, a declaração da minha variável, é atribuição de um só variável, quando está sendo feito no início da função. Número 2000 uma coisa. Então eu já disse que ele vai ler o número dois e já vai atribuindo isso também. E daí ele vai fazer o 8 ano de... 8, e como ele tem o gene aqui, ele simplesmente vai ignorar o que tem para baixo, se não for uma função literal.

Como eu tenho uma variável aqui, teoricamente, o que faz quando eu tenho variáveis? Quando eu tenho uma função declarada aqui para uma variável, ele pega essa variável, ele coloca aqui como um undefined, e depois, aí, ele cria a variável e atribui a função que a gente tem que cortar.

Então, basicamente, esse é um hoisting que acontece com variáveis em JavaScript. A função literal, JavaScript pega o jogador para cima, mas quando tem uma atribuição, ele pega as variáveis e joga pra cima também da função, pelo início da função, e só faz a atribuição no momento exato onde está sendo feita atribuição da equipe consegue entender com isso: que funções literais em JavaScript, funções literais, elas estão disponíveis dentro de todo o escopo onde elas foram criadas. Você tem uma função literal que vai ficar disponível dentro de toda essa função, mas variáveis, elas só estão disponíveis a partir do ponto onde eles são, onde é feita a atribuição para elas.

Então essa variável só vai ter o valor, você vai receber a função aqui, aqui embaixo, logo depois do retorno. Então, quando o JavaScript chegando, então ele vai retornar, ele vai ver que não tem nada, porque isso aqui é uma função literal. Ficou claro essa parte, que é difícil de entender?

## Hoisting de variáveis

Vou tentar criar outro exemplo aqui pra gente ver quem tiver mais ou menos isso funcionando. Então vamos lá: vai pagar aqui minha função, mas eu vou fazer o seguinte: vou criar uma variável chamada de novo. Eu vou passar dez aqui pra ela, e vamos ver como funciona esse esquema do escopo de variáveis agora.

Então, por exemplo, console.log. Não estamos chamando o ano antes de criar ela. Eu vou chamar aqui um ano depois de criado. Vou colocar um comentário aqui, "antes de criar". E você pode passar parâmetros para o console. Então você pode separar por vírgula aqui os, os parâmetros que você passar, que ele vai mostrar todos pra você. Beleza. Algo ele funciona.

E depois... "Depois de declarar". O colocar "declarar" em vez de "criar": estou declarando uma variável. Beleza. Então aqui vou fazer um console.log antes de declarar. Vamos ver qual vai ser o valor de antes e depois de declarar, qual vai ser o valor de no mesmo ano. Vamos executar aqui onde DJs.

Então olha só: "depois de declarar", no meu olho, onde é que ele deu, o que ele deu... Eu, foi que eu esqueci de colocar vírgula para separar. Que a função, desculpe, foi besteira minha, que eu vou me salvei aqui. Vamos encontrar de novo. Dar o que tinha para você ver o conteúdo dela.

Eu tenho a minha função falando. Estou dando um console.log nela para executar e para ver o resultado que ela retorna. Aí estou com o console.log aqui, uma frase, a gente se declarar pra gente viu o valor dela. Aí a declaração da variável é depois de declarar, é pra gente o valor que ela vai ter depois de declarar. Estado, se vai executar ela, o que acontece: antes de declarar a função, o valor de Allende. Depois de declarar a função, o valor dela deve estar aí. Como eu não tenho, como a função não retorna nada, então ela vai, a função, com a função retornando, porque eu não tenho muito aqui. Então a função vai, então editar, então esse tem sido em por causa disso, porque eu não tenho um item dentro de uma função.

Mas se eu consigo entender essa parte do que eu já vi, do que eles fazem, então, na verdade, olha só o valor dela: ele não disse que a variável não existia. Se eu criar, por exemplo, aqui, digamos, console.log, colocar aqui dois. Vou chamar variavam a variável, pois lá não existe mesmo. Ela existe, mas ela... E eu estou passando, eu falei para ela que ela ainda não foi passada nenhum valor, e aqui já foi passado. Mas ela realmente não existe. Olha o que acontece. Olha só, tenho aqui dois. Agora vamos executar esse cara aqui pra gente ver o que acontece.

Então ele é só a gente declarar. Então não tem valor, não definitivo, mas eu não B2C, ele disse que 2 não foi definida. Ou seja, não foi nem criada.

O que a gente consegue entender com isso? Que, na verdade, a variável ano, ela foi criada. Ele conseguiu verificar que ela foi criada, porque o JavaScript, que ele faz: ele simplesmente pega, vai e faz isso aqui, declara ela, não coloca atribuição nenhuma, e aqui, onde ela está sendo atribuída, que ele faz a atribuição da esculhambação que faz. Por isso que aqui na frente seria basicamente exatamente a mesma coisa fazer isso aqui. Ele criou também aqui com uma falha que não passa nenhum valor... ela sabe que eu fiz aqui também... então ela só a gente declarando ele faria, e depois declarava ele deve estar, porque ele declara. Ele simplesmente declarou como diferente, e basicamente isso queríamos que ele te faz.

Então, assim: variáveis, elas existem dentro do escopo onde elas estão, mas elas só estão disponíveis a partir do momento onde elas foram declaradas. Então, o que é feito com variáveis, é assim que funciona em JavaScript.

## Recapitulando

Então, só para recapitular: função literal. Falando de solução, eu tenho mais dois chamado aqui console.log. Vamos ver que ela retorna aqui console.log. São gente vai, então o antes e depois: olha só, eles são amantes e eles só depois, estão todos como depois. Ele retorna resultado, porque ele faz isso aqui: ele joga a função pra cima e simplesmente executa.

Ou seja, funções que estão disponíveis dentro do escopo, o escopo dela vai ser sempre a função onde ela está dentro. E essa função, myFunction, essa função myFunction, ela está disponível no escopo global. Eu consigo acessar de qualquer lugar do meu código, então, assim como ela foi criada aqui fora, ou fora de qualquer função. Então eu tenho myFunction no escopo global, e eu tenho a função sum no escopo local.

E com variáveis, como funciona com variáveis? Que, então, com funções, a gente viu que ela só funciona... com funções, ela está disponível dentro de todo escopo que ela está. Com variáveis: uma variável aí, vai 50 quilos no valor de um ano. Está invocar aqui, no primeiro vai entender, e depois vai ser 50 o valor dela. Esse terceiro valor, o esquema do retorno: porque eu não tenho retorno, em branco, simplesmente inventou um valor em branco pra mim.

## A dica

Então, você entendeu que o que acontece é bem simples e bem fácil de entender, mas é importante você entender esse tipo de coisa, porque isso pode causar efeitos colaterais na hora de você desenvolver um programa. Que eu disse que iria vetar qualquer ideia, qualquer melhor forma de eu criar funções ou criar variáveis em JavaScript, que eu vou criar uma função depois? Então, obviamente, não. Obviamente você não vai fazer isso aqui, que é uma função depois do return. Não faz sentido nenhum você fazer isso. Mais interessante você saber que o JavaScript funciona dessa forma, que ele trabalha dessa forma, e se você vê um código dessa forma, você sabe que assim ele vai funcionar.

Então, qualquer dica que eu dou para você: sempre que você for declarar uma variável, declarei no início da função. Você vai usar o número 2 aqui, declará-la sempre no início da função, porque é basicamente isso que o JavaScript vai fazer se você não fizer. Só que a diferença é que ele não vai atribuir o valor, ele vai deixar como undefined.

Você também pode fazer isso, não tem problema nenhum: 2, e depois você fazer as atribuições. Mas se você fizer isso, você vai acabar tendo mais linhas de código. Só que você vai ter quatro linhas; você poderia economizar isso com duas linhas. Não sei que seja realmente necessário. Você só cria as variáveis como definidas no início da função e depois você faz a atribuição. Mas variável deve sempre ser criado no início da função, ok?

Logo depois, você pode criar suas funções literais, cria estas funções que fazem o que você quiser. No caso, eu crio a função sum aqui. E, no final, você vai fazer um retorno, deixando retorne sempre na última linha da função, a não ser que você faça isso. Aí sim, sei lá, qualquer coisa. Aí você vai fazer uso de alguma coisa. Porque você vai ter dois anos, você vai ter um return dentro do if, então ele fora do estado.

Mas a dica que eu dei pra você, pra evitar problemas com hoisting no JavaScript, é declarar sempre funções, variáveis no início da função, para que você tenha elas disponíveis dentro de todo o escopo da função que você tiver trabalhando.

Beleza, interesse eu queria mostrar por enquanto sobre Tim, e até aproximá-la, ou até o próximo vídeo. Valeu, até lá.
