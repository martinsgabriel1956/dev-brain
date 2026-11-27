# JavaScript Ninja: Wrapper Objects

Olá. Voltamos com um curso [de] JavaScript Ninja. Eu sou Fernando Daciuk, que posso fazer a revisão do desafio novo agora, do Desafio da Semana 9. Agora ele vai entrar no assunto novo, que ainda não conversou, mas fala um pouquinho sobre [wrapper] objects, que são o objeto.

## Valores primitivos e objetos

Bom, a gente sabe que valores primitivos, eles não são objetos. Então, quais são os valores primitivos que a gente tem? Por exemplo, [a] gente tem o número, x isto, a gente tem um valor booleano, os valores booleanos é falso. Esses são valores, valores primitivos, de valor indefinido também são valores primitivos. Os outros, todos os outros tipos de valores em JavaScript são objetos: arrays, objetos, funções.

Então, a gente sabe que esses valores primitivos, eles não são objetos. E o que, o que diz se um valor é um objeto ou não, se algo dentro do JavaScript [é] um objeto ou não? Se esse cara, ele tem propriedades e métodos, então ele é um objeto, certo? Se ele não tem propriedades e métodos, então ele não é um objeto. Basicamente, essa diferença está: um objeto dentro do JavaScript, que ele vai ter sempre propriedades, ou ele pode ter propriedades e métodos, e o valor primitivo, ele não tem propriedades e métodos, ele é um valor exatamente da forma como ele, como ele é apresentado, por exemplo, sim.

Então, por exemplo, vendo um exemplo aqui, a gente cria uma variável chamada name, eu atribui o valor Daciuk. Eu peguei uma propriedade chamada length, da propriedade do variável name, e se esse length, ele me retorna seis, que é o valor da quantidade de caracteres que tem na string.

Só que eu acabei de falar que valores primitivos não são objetos. Então, o porquê que eles têm propriedades? Porque, assim, essa variável, essa variável nem me atrai em si mas sim, mas tinha um valor primitivo, e eu estou conseguindo usar uma propriedade length. Nela, está uma propriedade que gera o JavaScript, aquele que ele serve para contar a quantidade de caracteres de uma, de uma string, da mesma forma que tenho F para o array, que ele conta a quantidade de itens do array, mas temos também o Luis Peru pra isso.

## Construtores e o new

Então, porquê que ele se tem propriedades? Aí que entram os objetos, os preços dos objetos construtores. Então, eu vou mostrar pra você aqui na prática, mais ou menos, como que isso acontece. Então, eu tenho uma oportunidade name, vou atribuir, vou chamar name.length. Olha só o que acontece. Ele me retorna 6, ele me retorna 6. Se nem me seu tamanho mínimo aqui sentado.

Então, o que são esses objetos? Esses construtores, os jovens. Construtores em JavaScript. São objetos, ou funções, no caso, que criam novos objetos. Então, basicamente, quando você utiliza os construtores JavaScript, JavaScript que tem alguns construtores próprios, a gente vai falar mais para frente sobre construtores. Mas agora o comando precisa ver esse esquema de conversão de tipos, então eu preciso mostrar para vocês sobre os construtores agora. Vou mostrar para a base que agora, só que mais para frente isso vai voltar a falar sobre construtores.

Então, como você usa o construtor hoje em JavaScript? Você utiliza a palavra-chave, palavra-chave new, que vai criar algo novo, que você usa o construtor. Então, uma vez que ele tem basicamente três construtores ali para esses valores primitivos, que é o String. Então, por exemplo, estou atribuindo ali a minha variável nem Manuel da Silva, que para uma variável chamada Meu nome está passando 30, para variável mídia estão atribuindo lhe o Boolean com um valor falso.

Então, o que acontece em JavaScript? Quando você cria um desses construtores, esse construtor, na verdade, é o objeto da construtor, ele é um objeto, e como objeto ele tem propriedades e métodos. Então, o que é, na verdade, JavaScript faz se por debaixo dos panos? Ele faz isso aqui: vai nem me viu isso. É como se eu passasse aqui. Se eu for chamar agora meio ano, que acontece? Ele é um objeto do tipo String. Agora se o combinado do tipo que tem um valor nasceu, logo, se eu chamar name.length, então ele vai mostrar esse valor pra mim.

Só que a diferença é: quando eu crio com o meu filho isso, ele vai ser simples, sei que ele vai ser um objeto que nunca venceu uma. Ele nunca venceu ser mais time, ele terá alta. Ele vai impor seu objeto, e esse objeto, ele tem um valor baixo. E ele tem algumas, algumas propriedades que tem todo o valor real desse, desse objeto. É o valueOf, name ponto valueOf. Essa função, aí sim, vai me retornar esse time dócil, que é o valor exato, ou o valor literal que eu tenho nessa idade.

## O wrapper object

Então, o que acontece quando você cria um inimigo e volta assim, por exemplo? Você consegue chamar o name.length. Na verdade, não é esse cara aqui, ou essa, essa, essa stringzinha literal que ela tem a propriedade length. O vez que ele faz é o seguinte: ele pega, quando você tenta buscar um método e um objeto, digamos que entende o tipo do objeto. Então, por exemplo, ele entende que eu tenho uma string, porque do jeito que faz, ele pega, cria um novo objeto pra mim, que é o objeto wrapper. Por isso, por esse nome, para o objeto que ele vai criar, um envoltório, está ok? A tradução de wrapper significa um envoltório.

Então, digamos que você vai fazer isso: não vai pegar ele, vai envolver a minha string literal, se o que é o objeto, um objeto do tipo String, para que eu possa utilizar a propriedade. Logo depois que eu utilizo a propriedade de length, e eu verifico o valor da propriedade length, gera esse tipo de descarte. Se o objeto da memória, é o name, ele continua sendo essa minha propriedade. Então aqui, basicamente, digamos que faz a curva T o valor de name para um objeto, para que eu possa utilizar a propriedade length, está?

Basicamente, é essa a diferença de você utilizar um objeto do tipo construtor e um objeto, um objeto literal. E da mesma forma que eles têm os construtores, agora que eu apresentei os construtores para você, não, não é o que você vai utilizar muito no dia a dia. É interessante você saber, você entender como o JavaScript faz essa conversão de valores. Mas, assim, não é algo que você vai utilizar realmente no seu dia a dia. Você não vai criar mas sim usando nisto. Você vai utilizar o valor literal desse.

Você não vai querer um número também passando lá: var igual a Nildo 30, por exemplo. Aí você vai chamar. Olhe aqui, você vê que ele é um objeto. Do ponto valueOf, ele traz o valor literal do que é o número 30. Então, assim, você não vai utilizar o objeto no teu dia a dia para você, para você querer string, para você criar valores, para você criar um número, que está, você não utilizar o objeto, literal.

## Construtores sem new: conversores

É interessante você saber que esses construtores existem, e eles servem também, essas funções, elas podem servir também para outro, para outros casos. Quando a gente usa sem new, esses caras, eles servem mais como conversores do que construtores. Então, basicamente, quando você usa o new, ele cria um novo objeto; quando você não utiliza new, se com essas funções, essas funções globais, porque elas estão disponíveis em qualquer lugar do teu código, a função String, a função também, a função Boolean, você acaba convertendo esse valor.

Então ela só, eu posso pegar um valor aqui, por exemplo, vai ser lá vai, eu vou colocar aqui um String, eu passo que o valor dez, por exemplo, o valor dez, como o número que você chama aqui, vai. Ele vai passar o décimo também como esse tipo, que ele passou por aqui, porque eu usei o, a função String aqui do JavaScript, que ele converteu o meu número. Para isso fiz uma coisa: para se eu pegar uma var que fizer o número, eu tiver entre String, e que o número 52, por exemplo, ele vai, quando eu chamar aqui vai, ele vai chamar %52 como o número. Pode ver que se eu somar mais vai mais 2, ele fala sobre somando, faz a concatenação.

Você lembra que o operador de mais, ele tem, se você tenta somar no caso das strings, ou uma string com qualquer coisa, ele converte os dois valores para esse fim. É concatenar. É exatamente isso que o que achamos que ele faz: ele pega o objeto, ele cria, ele, ele converte aquele valor, mas tem ele concatenado. Nesse caso aqui, eu usei o Number, ele vai ter esse valor aqui pra matar.

Exatamente acontece a mesma coisa quando eu tenho o Boolean. Então, por exemplo, lembro que a gente tem o zero, zero. Ele é um valor falso, ele representa o valor falso. Se você chamar uma var aqui com zero, ele só, ele vai dizer que o meu valor é falso. Agora, se eu criar mais, vai chamar o Boolean, por exemplo, [com] um objeto vazio, ele vai dizer que o vai tu, porque o objeto vazio representa true. Então isso aqui é o mesmo que a gente usar aquele esquema do, dos dois sinais de exclamação lá, que ele vai mostrar o equivalente booleano daquele valor. É basicamente isso que a gente faz por baixo dos panos. Então ele converte esse valor naquele tipo específico.

## Tipagem dinâmica

Então, o JavaScript é uma linguagem de tipagem dinâmica, ou seja, você não precisa dizer a esse objeto: o número é esse cara, que é uma string, ou esse cara, que é tal coisa. Você não precisa dizer por JavaScript que tipo é aquele valor que você está tentando usar, algo que você está tentando converter, o que você está tentando somar, o que você está tentando concatenar. Lembre-se que o, ele tem tipagem dinâmica, ou seja, ele automaticamente vai mudar o tipo, se for necessário. Ele automaticamente um esse tipo, se ele achar que é necessário. E por isso é bastante importante você entender como ele faz essa, essa conversão de valores, para que você não se perca, e para que você entenda realmente o que o JavaScript está fazendo nesses casos.

Então, era isso que eu queria mostrar para vocês sobre a conversão de tipo. Se ficou alguma dúvida, já sabe: mandou e-mail pra mim, abre uma issue, ou qualquer duvidava você, por enquanto, quando você estiver resolvendo o desafio, que vai cair isso aqui no seu desafio. Beleza? Valeu, um abraço e até o próximo vídeo.
