# JavaScript Ninja: escopo de variáveis e funções

Olá, voltamos aqui com um curso JavaScript Ninja. Meu nome, Fernando Daciuk. Estamos na nossa quarta aula, e agora nós vamos falar um pouco sobre o escopo de variáveis. Na verdade, já falei de escopo de variáveis e funções.

## Escopo global e escopo local

Então, vamos lá: o que acontece no JavaScript, que a gente tem dois tipos de escopo: o escopo global e o escopo local. Qualquer diferença desses dois escopo, escopo, na verdade, é o local onde você declara uma variável.

Então, por exemplo, sempre que eu declaro uma variável na parte mais alto do meu código, ou, digamos assim, que sempre que eu declaro uma variável fora de função, essa variável está sendo declarada no escopo global. Se eu declaro dentro de uma função, eu crio uma variável no escopo local.

Então, o que é interessante saber: a variável, ou o escopo global, no JavaScript, que na verdade é um problema bem grande que a gente pode ter, que eu vou mostrar para vocês agora: o que acontece se você declarar variáveis no escopo global, qual o problema que isso pode acontecer. Isso, basicamente, é um erro de design da linguagem de script. Ele disse não deveria ter, mas como ele foi feito dessa forma, que a gente consegue de algumas formas... Felizmente, a gente consegue, de algumas formas, passar por cima disso e usar somente variáveis como local.

Mas é interessante você saber que o escopo global, ele realmente é algo ruim, e o que ele, ele pode atrapalhar bastante nosso código. Eu vou mostrar para vocês por [quê]. Mas você precisa saber, basicamente, que ela cria o escopo local.

Então, assim como eu falei, que sempre que você cria uma variável dentro de uma função, essa variável está sendo criada dentro do escopo local; você não consegue acessar essa variável de fora da função. Quando você diz o contrário, é verdadeiro: quando você cria uma variável fora de uma função, você está criando e escopo global. Ou seja, em qualquer lugar você consegue acessar aquela variável.

## Exemplo real

Vamos ver um exemplo, um exemplo real disso. Então, por exemplo, eu vou criar aqui uma variável chamada mas vai, passar pelo valor. Se eu chamo a variando no meu bairro, ele vai trazer para mim o valor certo. Então, o que acontece? Eu queria essa variável de escopo global, beleza, eu consigo acessar normalmente.

Eu vou criar agora uma função chamada infantil. Vou me retornar uma mãe vai. Será que eu consigo, de dentro da função, você sabe o valor da variável uma mulher, quando executar uma infantil? Vamos ver o que ela retorna. Olha só: ali, eu não sei porque ele conseguiu encontrar uma imagem que eu criei no escopo global. Ele consegue acessar essa variável que está no escopo global dentro dela, dentro da função.

Então, o que ele consegue entender ou aprender com isso? Que sempre que cria uma variável no escopo global, eu consigo acessar, e acessar ela dentro do escopo dos locais.

Agora vou tentar fazer um outro teste aqui. Como criar uma função em direto. Como criar moda infantil aqui nessa função. A gente vai criar uma variável chamada vai estar, que ela vai receber um valor. Nós vamos retornar o valor nessa etapa.

Então, o que acontece? Essa variável vai... Ela foi criada dentro da função. Ela vai, vai passar a aparecer a partir do momento que vai executar essa função, ou invocar ela, está. Então eu vou executar essa função.

Olha, eu e ele, na minha teoria, o valor é útil, porque ele entrou no truque, porque eu declarei que dentro da função uma variável chamado Honey vai retornar o valor dessa variável. Então, teoricamente, essa variável até vai, ela estar disponível pra mim. Mas ela está disponível somente isso como colocar dentro da função.

Se eu tentar acessar ela aqui fora da função, ele vai dizer que ela vai usar o interpretador onde ele escrito que vai dizer que ele vai estar definido. Ou seja, ele vai, não existe fora da função, porque ele definiu uma variável chamada de fora definido dentro da função, em outro nível.

Então isso que é legal de você, você utilizar sempre no escopo, sempre o escopo local.

## Garbage collection

Uma outra vantagem também de você utilizar escopo local ao invés de utilizar um escopo global: o JavaScript, que tem algo chamado garbage collection, que é coleta de lixo, que ele faz, que funciona mais ou menos assim: quando você cria uma variável dentro de um escopo local, por exemplo, ela só vai ficar disponível dentro daquele escopo. Ou seja, ela só vai aparecer mais só quando ele executa essa função.

Então, o JavaScript vai saber do meu código, que ele vai fazer toda a leitura do meu código e a interpretação dele, ele vai saber que a partir do momento que eu chamar essa função aqui, se eu não for chamar ele mais lugar, em JavaScript, se souber que eu não vou usar mais essa variável em lugar algum, simplesmente elimina da memória o espaço que essa variável está ocupando. Porque essa variável, quando eu crio ela, quando eu defino ela, ela ocupa um espaço na memória para guardar um valor. Esse valor útil é para que eu possa ler depois. O JavaScript guarde memória isso.

Quando eu crio escopo local e eu não preciso mais essa variável, o JavaScript fala automaticamente o garbage collection, e ele remove da memória aquela variável, está. Aí, então, você é bastante legal, porque não fica muita coisa na memória. A gente não guarda lixo da memória, se a gente não vai precisar usar futuramente.

Então isso funciona tanto com funções, funcionam com variáveis, que funcionam como objetos, que funciona como qualquer coisa que eu escrevo saiba que não vai utilizar depois: ele remove da memória. Ok.

Então, basicamente, era isso que você precisava saber sobre a questão de escopo local.

## Variável sem var

Um outro ponto bastante importante é que você sempre precisa utilizar a palavra-chave var para declarar uma variável. Até agora a gente sempre usou a palavra-chave var, mas você precisa saber também, como lixo, você precisa saber e entender que você também consegue criar uma variável sem utilizar a palavra-chave.

Só o problema de você criar uma variável sem utilizar: quando você queria usar o JavaScript, se entende que você está criando aquela variável no escopo global, ao invés de criar um escopo local. Ainda que você cria uma variável dentro de uma função.

Então vamos ver como é que funciona isso. Eu vou criar uma função aqui chamada mil falantes, por exemplo. Eu vou criar uma variável agora, vai, sem utilizar a palavra-chave var, passar uma variável global. Foi, então o valor de mil vai, só para você ver que ela está acessível dentro da função.

E o que acontece? Essa variável aqui, vai, ela ainda não existe aqui no meio de campo global, porque eu ainda não vivo aqui a função. Só que a partir do momento quem invoca a função do Flash, ela me retorna o valor da variável. Ele vai criar essa variável no escopo global, porque eu não usei o var aqui, está, e vai retornar o valor dela.

Então, o que acontece: você viu que lá, quando eu tinha criado um escopo local utilizando a palavra-chave var, eu não conseguia acessar a variável de fora da função. E se eu tentar, queria acessar agora essa variável, vai acontecer exatamente: ele vai avaliar o valor da variável, que ela foi criada sem a palavra-chave.

O, o problema disso: o JavaScript não vai conseguir utilizar alguém para escolher um time dessa variável. Você pode ter conflito de nomes com outras variáveis. Você pode mesmo, tem várias coisas que você pode atrapalhar. Isso, dependendo do tamanho do objeto ou do conteúdo que tem essa variável, você pode fazer com que ela ocupe muito a memória e acabe consumindo muito recurso do seu computador. E o JavaScript não vai poder fazer nada com relação a isso: ele não vai poder limpar aquele espaço de memória que essa variável está ocupando, porque ela está sendo, ela está sendo usada como uma variável global. Então vai ficar bastante difícil, porque você tem que fazer login e coleta, porque você criou uma variável no escopo global.

Então, sempre que você foi criar uma variável, é bastante importante que você sempre utilize a palavra-chave var, está, como sempre, como se está fazendo em todos os vídeos até agora, como eu tenho mostrado em todos os vídeos em que está usando sempre a palavra-chave. Mas é importante frisar que se você esquecer de usar o var e você cria uma variável sem o var, você cria um escopo global, e isso causa um problema bastante grande.

## Argumentos de função

Outra coisa também que você quer interessante saber são sobre os argumentos de função, dos órgãos de função, e também se eles também são locais. Então, por exemplo, quando você cria uma função, que aqui uma função foi chamada outra função, boa para se passar para ela três parâmetros: a, b e c. E eu vou me retornar aqui o parâmetro de ação.

Só para você entender, eu vou executar outra função que vou passar aqui. Ele vai retornar o valor de seu face ao valor e aí B, ele vai retornar o valor, porque eu estou retornando. Mas se eu tentasse saltar fora, olha só o que acontece: não está definido. Porque argumentos em função, tanto B como você também veio, se eles não estão definidos, por argumentos de função.

Sempre que você utiliza essas variáveis de argumento aqui, elas também são locais. Então elas ficam sempre dentro do escopo da função; você não consegue acessar alguém fora da função. Argumentos são sempre locais também.

Beleza, acho que ficou bem fácil de entender, e ficou bem, bem... Se você tiver alguma dúvida com relação ao escopo ainda, gostaria que você perguntasse, que você mandasse e-mail, abrisse isso no GitHub, para que você fique, para que fique claro, bem claro esse assunto. Se ficou alguma coisa difícil de entender, me avisa, quem vai tentar explicar de uma forma melhor. Beleza.

E agora vai fazer o nosso desafio da semana 4, mas no próximo vídeo, que nosso tempo pra acabou. Então.
