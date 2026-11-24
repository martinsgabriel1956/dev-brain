# JavaScript Ninja: variáveis e tipos de dados

## Variáveis

Olá pessoal, tudo bem? Voltamos aqui então com a nossa segunda parte, a segunda parte da primeira aula do curso JavaScript. Eu sou o Fernando Daciuk, que agora vai dar um giro pela linguagem JavaScript.

A primeira coisa que nós vamos falar agora são sobre variáveis, que são variáveis variadas. Na verdade, ele é um nome simbólico que você vai dar para um tipo de valor.

Então, as variáveis, elas têm um nome simbólico que você vai dar para tipo de valor, como havia falado. E para você declarar uma variável, você precisa usar a palavra-chave var, certo?

Então, como você vai... Como é que você vai fazer isso? Como exemplificar aqui: então, estou aqui no meu terminal, certo? É que no meu terminal vou acessar a interface do Node para poder digitar os comandos, para poder mostrar para você como funciona a declaração de uma variável. Então, sempre que você for declarar uma variável em JavaScript, você precisa utilizar a palavra-chave. Então você vai usar palavra-chave var, dar um nome para uma variável, pressionando, pressionando Enter aqui, eu dei...

Eu queria uma variável chamada X e ela não tem nenhum valor, nenhum valor definido para ela, então por isso apareceu aqui ou ali. Se eu... Se eu tentar avaliar essa variável, ou seja, passar esse valor aqui pelo interpretador do Node, então ele vai avaliar essa variável e vai me mostrar o valor que ela recebeu. Como eu não atribuí valor nenhum ela, então o valor dela é undefined, ou é um valor indefinido, ok?

Mas se ela é um nome simbólico para um valor, como eu faço para atribuir um valor então uma variável? Eu vou usar o sinal de igual. Então, se eu fizer x é igual a zero, automaticamente o valor zero foi atribuído à variável x. Então agora, se eu pressionar o X aqui e dê um valor, X já não é mais avaliado como undefined como antes. Agora ele é avaliado como valor zero. Por quê? Porque eu disse que o X agora ele vale zero, e com ensino de matemática que você aprende na 5ª série. OK? Então você, que você atribui um valor a uma variável com o sinal de igual, certo?

Você, com o JavaScript, ele aceita vários tipos de valores. Então, por exemplo, a gente atribuiu um número 0, é um tipo de valor número, que eu posso atribuir outros tipos de valores uma variável. Por exemplo, se eu quiser mudar o valor dessa variável X, que era 0, para 1, eu posso mudar o valor dela para 1. Então variável, ela tem esse nome exatamente por esse motivo, por ele, se ele é avaliado, porque ela tem um valor que pode variar, que pode mudar. Então hoje ela tem um valor. Ela começou com um valor não definido, atribuí o valor zero e agora ela atribui o valor. Eu mudei o valor dessa variável pra 1, ok?

JavaScript também tem alguns outros tipos de valores que eu posso atribuir para uma variável. Então, por exemplo, o meu número x, atribuí 1.2. 1.2 também é um tipo de número, mas é um tipo de número conhecido como float, ou como números reais, que é o número, número que nós conhecemos na matemática como um número decimal. Então, números decimais também são válidos em JavaScript. Basicamente, o padrão é o número de jovens, que são números decimais, mas a gente vai ver mais para frente, quando falar da estrutura lexical, digamos, que está. Então, só para você saber que é avaliado basicamente.

Então você vai, você declara ela com a palavra-chave var, você dá um nome qualquer e você pode atribuir um valor a ela. OK. Quando eu tento, quando eu chamo essa variável, ele me retorna o valor que eu foi atribuído para ela. Ok.

## Tipos de dados: number, string, boolean, null e undefined

Então, tipo de dado. JavaScript, ele tem... Ele aceita vários tipos de dados. Alguns deles são os mais conhecidos, pelo menos sob o nome de boolean, null, undefined. Então a gente vai ver todos esses tipos de valores começar que...

Então a gente já viu o valor number aqui, como é que funciona, certo? Control L para limpar meu terminal, que normalmente funciona no shell também, se você usa Linux, se você usa o Windows. Não sei, se você usa Mac, provavelmente deve ser Command L, onde ele está. Você pode ir em seu terminal.

Eu já disse que ele tem vários tipos de valores. Eu tenho a variável x definida aqui como 1.2. Só que eu posso adicionar essa variável e outros tipos de valores também, certo? Então eu vou colocar aqui a variável x, uma frase, chamada uma frase, Hello World, que acontece. Hello World não é um número, mais ou menos, mas sim uma sequência de caracteres. Strings em JavaScript, elas são representadas por qualquer caractere dentro de aspas duplas, se eu fizer "Hello World", ou dentro de apóstrofo, como eu fiz aqui no primeiro exemplo.

Então, em JavaScript, isso não tem diferença alguma. Em algumas linguagens, algumas linguagens de programação, é diferente, e elas precisam que você coloque dentro aspas duplas, mas o JavaScript não gera esse tempo, que você pode usar tanto com aspas duplas como apóstrofo. Ele vai entender exatamente como ao mesmo tempo. Ok, então posso, posso, posso chamar tanto com aspas simples como com uma seta.

Outro tipo de valor, isso é boolean. Boolean é representado basicamente true ou false. Então é falso. Algo que é verdadeiro ou algo que é falso, certo? São esses dois valores booleanos que nós, que nós temos aqui, ok?

Outro valor também que pode ser, que pode ser passado: o valor null. Valor null. Valor... Na verdade significa nenhum valor, significa que o X não tem valor nenhum definido para ele. Ou ainda eu posso passar o valor chamado undefined. Falei, ele é parecido com null, não é a mesma coisa, mas ele, digamos assim, a ausência de valor. Tá, null é nenhum valor. Eu andei falando quando eu tenho a ausência de valor. A gente vai ver mais para frente também algumas outras definições de null e undefined para deixar um pouco mais claro, mas basicamente os dois têm uma função bastante parecida de deixar uma variável sem valor.

Novamente: o null, ele representa o valor de uma variável quando ela não tem nenhum valor, ela pode ser null; e undefined representa quando a variável não existe, mas no JavaScript a variável pode existir e pode continuar tendo valor undefined. Então, nem se fala, isso são basicamente a mesma coisa. Na maior parte das vezes a gente vai tratar eles como sendo a mesma coisa, e mais para frente, alguns casos específicos, nós vamos ver aqui quais são as pequenas diferenças que têm entre o null e o undefined. Beleza.

## Objetos

Então, existem mais dois tipos de dados ali que são, são bastante importantes para JavaScript, principalmente o tipo de dado objeto, object, e o array. Então são dois, são outros dois tipos de dados diferentes também para JavaScript.

O objeto, na verdade, ele é um, ele é um dos temas mais importantes em JavaScript, mas a maior parte das coisas que nós vamos fazer com JavaScript, a gente vai estar tratando diretamente com esse tipo de dado objeto. A representação literal do objeto vai ser esse finalzinho de bichado e se fecha chaves. Então, se eu quiser que o X, que o variável X agora ela seja um objeto, simplesmente eu faço uma representação com o chaves e eu fecho chaves.

O que é um objeto uma linguagem orientada a objeto? Se você já trabalhou com uma linguagem orientada a objetos, você sabe que um objeto, ele tem propriedades e métodos. Série que são as propriedades, os métodos. As propriedades são basicamente coisas que têm um objeto. Então imagine uma janela, um objeto, ou pessoa, certa? Pessoa, e a pessoa, um objeto, certo, em que suas propriedades são coisas referentes àquela pessoa. Então, por exemplo, uma pessoa, digamos que eu vou definir a altura, altura da pessoa.

Então, em JavaScript, a notação para definir o objeto: eu posso definir tudo de um objeto só, está, iniciando aqui com pessoa igual chaves, eu vou colocar a altura, dois pontos, e a altura da pessoa vai ser 1.87, por exemplo, certo? O peso da pessoa: digamos que ela vai ter 90 quilos. Ok, eu vou fechar aqui então meu objeto.

Então eu tenho um objeto pessoa, certa? Ele tem uma altura de 1 metro e 87, ele tem um peso de 90 quilos. Aqui é mostrado meu objeto completo. Se eu chamar o meu objeto pessoa, ele vai mostrar altura e peso, certo? Como eu faço para acessar cada valor aqui separadamente? A notação de objeto no JavaScript, pra você, pra você pegar a altura ou o peso da pessoa, é usar o ponto. Então eu posso usar a pessoa à altura, eu vou obter o valor da altura da pessoa, que é o metro e 87. Se eu quiser pegar o peso, mas uma coisa pessoal de peso, eu vou receber o valor 90 que eu tinha cadastrado antes, certo?

Essa primeira forma quente que a gente criou o nosso objeto, está. Existem duas formas de inserir objetos: pode criar todo ele de uma vez só, assim, onde todos os valores vão ser atribuídos de uma única vez essa variável pessoa. Então esse objeto, desde do início das chaves até o fim, deixámos esse objeto, e está sendo atribuído a uma variável chamada pessoa. Ok.

A outra forma de você atribuir valores é você usar a própria notação de objeto. Então, por exemplo, se eu colocar a pessoa à altura, eu posso descrever a altura da pessoa. Eu vou dizer que agora essa pessoa não tem mais um metro e 87. Agora essa pessoa tem um metro e noventa. A pessoa tem um metro e noventa. Então, se você sabe agora pessoa, uma pessoa, eu vou ver que a altura mudou. O peso continua o mesmo, porque eu só mudei a propriedade a altura da pessoa, certa? E se eu colocar a pessoa no peso, vamos dizer que essa pessoa emagreceu. Agora ela tem 80 quilos. Antes ela tinha 90. Se você sabia a pessoa até ter altura um metro e noventa e peso 80 quilos. Então essa é a notação de objeto que a gente vai trabalhar.

## Arrays

Em JavaScript, como funciona a notação de array, que sou o primeiro que não arrisca? Na verdade, ele é uma lista, uma lista de valores. Então, por exemplo, eu vou querer um array aqui chamado números, na notação de arrays. Eu criei um array vazio, que não tem valor nenhum, se chama números. Aqui eu vou chamar simplesmente abre e fecha colchetes, daqui que é o nosso, que é o meu array vazio. Como eu vou definir valores? Array, eu posso definir dessa forma, certo? É passar aqui separado dos valores por vírgula: 1, 2, 3, 4, 5, 6. Se eu chamar números, eu vou ter o meu array 1, 2, 3, 4, 5, 6.

E como que eu faço para acessar esses valores aqui de números? Array, ele é acessado por índices. Então, os índices do array, eles são números iniciados a partir do zero. Então, por exemplo, se eu quiser acessar a primeira posição aqui, que é o número 1, a posição 1, a primeira posição do array, na verdade a posição 0, no que você chama de números, números, e passar posição 0. Com essa notação aqui de colchetes e array, ele vai me devolver o primeiro valor, certo? Então o primeiro valor, zero do array, o 24 do array, o valor 4 do array, que é 1, 2, 3, 4. O índice dele é 0, 1, 2, 3. Então, acessar o número 4, eu preciso passar o número e dizendo que eu quero acessar o índice 3. Números, eu coloquei número aqui e ele disse que o número não está definido, certo? Porque eu não tenho essa variável, um número, variável de números. O meu array é números. Ok, então números 3. Ele vai me devolver o valor 4. Ok, então bastante simples aqui.

## Arrays são objetos

Na verdade, no JavaScript não existem arrays, está? Usar isso: eles, eles nada mais são do que objetos. Tanto que, se eu pegar o meu, meu objeto a pessoa, que eu tenho o meu índice altura e o meu índice peso, está, se eu tentar acessar dessa forma, a pessoa, e passar uma string com o valor do índice, eu consigo também acessar a altura da pessoa. Então posso usar tanto a notação de objeto, que a pessoa aponta à altura, como eu posso acessar também com a notação de array, que a pessoa está, tanto com aspas simples como as duplas. Tanto faz, a pessoa altura, a minha escolha, é o mesmo resultado. A notação de objeto é mais rápida, então procuro usar sempre que possível. A gente vai usar essa notação aquele objeto está mais à frente, gente vai ver, gente vai ver mais explicitamente sobre isso, sobre esses tipos de valores, mas agora, agora é isso que eu queria, que eu queria mostrar para vocês, certo?

Então aqui a gente viu quais são os tipos de dados em JavaScript. Vamos falar aqui sobre variáveis, como criar variáveis, e os tipos de dados do JavaScript. Agora já falou um pouco sobre operadores, mas já deu dez minutos desse vídeo. Vamos parar de falar então sobre os operadores. Até a próxima.
