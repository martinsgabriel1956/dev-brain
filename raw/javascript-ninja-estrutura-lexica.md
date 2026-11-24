# JavaScript Ninja: estrutura léxica

Olá, voltamos com a nossa segunda aula do curso JavaScript Ninja. Meu nome é Fernando Daciuk.

E agora nós vamos começar um pouquinho sobre estrutura léxica [do] JavaScript. O que é estrutura léxica? E estrutura léxica de uma linguagem qualquer de programação é um conjunto de regras que vai definir quais são o modo que a gente vai usar para se escrever nessa linguagem.

Então, basicamente, ela diz qual é o nível mais baixo da linguagem, que ela vai especificar detalhes de como são e como ele pode nomear variáveis, de como pode nomear funções, e tipo de caracteres que a gente pode utilizar. A forma como a gente cria comentários, como [a] gente pode gerar comentários. Como separar uma instrução de outra.

Então é isso, quem é esse, que é o que é a estrutura léxica, uma vez que vamos mostrar aos anos. Ela vai nos dar toda a base e toda estrutura pra gente saber o que pode e o que a gente não pode utilizar dentro, dentro do JavaScript.

## Case sensitive

A gente vai começar a falar um pouquinho sobre case sensitive. Que é case sensitive? Que esse case sensitive significa que há o JavaScript... Ele, na verdade, ele diferencia letras maiúsculas de letras minúsculas.

Então, basicamente, falando sobre o case sensitive: quando você vai nomear uma variável, por exemplo, seu nome é uma variável chamada var animal, estar, eu vou dizer que o valor dela [é uma] string chamada cachorro. Se eu criar uma outra variável e dizer que o nome dele é Animal, e o nome dela e o valor dele é um macaco, as duas variáveis são diferentes.

Se eu chamar um animal com a minúscula, ele vai chamar o cachorro. Se eu chamar o Animal com A maiúsculo, Animal com A maiúsculo vai chamar macaco. Ou seja, Animal é diferente de animal, sim. Ou seja, ele [é] case sensitive.

Então, qualquer coisa que você escrever, que você fizer dentro do JavaScript, cuide muito com a forma como você vai escrever. Porque se você chamar ela de um jeito, se você se declarar uma variável de um jeito, por exemplo, [e] chamar de outro, isso no seu nome, digamos. Por exemplo, você declarou o animal em cima de você chamado de mau uso do ANIMAL. Ele vai dizer que o ANIMAL, todo em maiúsculo, não está definido, porque ele é todo em maiúsculo, não existe.

Então o JavaScript é case sensitive. Ele lê, ele diferencia letras maiúsculas de letras minúsculas. Ok.

## Comentários

Comentários. Como aqui, que são comentários e como funcionam os comentários no JavaScript? Então existem ali basicamente dois formatos de comentários no JavaScript, que tem um comentário de linha, que usa duas barras, está, como eu mostrei lá no último, no nosso último exercício, nosso último desafio, um desafio da semana passada.

A gente viu que quando você colocar duas barras de uma linha, o JavaScript simplesmente ignora que aquele comando, porque aquilo significa um comentário, e um comentário que você vai colocar no código. E qualquer coisa que você quiser colocar, você vai escrever um comentário normalmente. O comentário vai ser usado para dizer o que está sendo, o que está sendo feito naquele momento, ou para você marcar alguns trechos de código. É basicamente isso que você vai usar, para isso que você vai usar os comentários.

Então, por exemplo, se eu utilizar um comentário que [é] um barra barra, e dizer que a variável animal é igual cachorro... define uma chamada animal, e qual o valor dela de cachorro, certo? Que eu já vi esse tipo de efeito, que aquilo simplesmente ignorou. Sei que não há nada que aqui. Ele simplesmente ignora e não interpreta.

O que são, e o que é esse segundo? Esse segundo tipo, que é o comentário de bloco, que na verdade você pode escrever mais de uma linha. Então, cada vez que você quiser um comentário de uma linha, você vai escrever, que você vai usar o barra barra, uma linha, duas linhas. E quando você vai escrever o comentário de bloco, você usa o basta. Isso dá uma linha, outra linha e outra linha, e fecha, e ele termina instrução, ok?

Então aqui eu criei um comentário de bloco, que eu posso também utilizar em uma única linha, que funciona do mesmo jeito, como você acessa, tem um comentário parecido, mas eu já vi escrito que você pode utilizar uma linha para quando você vai usar esse comentário, ok? Então são esses dois formatos de comentários que nós temos no JavaScript.

## Literais

Literais. Uma vez que ele tem alguns, alguns literais, que na verdade, ou porque são literais? Literais são valores que aparecem diretamente no programa. Digamos que são valores que não mudam. São valores que fazem parte do código JavaScript, digamos assim.

Então, por exemplo, vamos dar alguns, alguns exemplos aqui de literais. Então, por exemplo, eu tenho ali o número 12, é literal, porque sei que se eu colocar aqui no meu terminal o número, por exemplo, número 12, ele vai me retornar 12 meses, certo? Fui chamado Marduk detonador de medo, então mais string é literal. Eu chamar um cachorro aqui, ele vai dizer que é um cachorro, mas string é literal. O valor booleano, literal, porque ele vai ter o mesmo falso, que também é literal.

Então aqui, por exemplo, eu tenho aqui um ponto 2, que é um número decimal, também literal, mas tem de tudo com aspas simples como com aspas duplas, ou um literal, um valor booleano. O valor no objeto literal, que é formado pela chave. Aí você vai colocar os valores do objeto ali com a chave e o valor: da chave, 2 pontos, de valor. Um array literal, se que o objeto, objeto literalmente, tem um array literal, portanto, no JavaScript.

Se eu fizer isso aqui na minha escolha, esse valor, então, é o literal da linguagem. Então não existe nada que crie ele. Ele já existe dentro da linguagem JavaScript. Por isso ele é um literal, que o array também é literal.

Então, basicamente, literais são isto. Literais é quando você vê esses valores que aparecem diretamente em uma linguagem, e ele, ele não muda, o valor dele não muda. Tu entrou mesmo no menu 12 e nem sempre 12, a variável nem sempre isso, é, ele não vai ser um número, não vai mudar para o numeral, não vai mudar para o Estado. Então esses são valores literais dentro do JavaScript.

## Identificadores

Como falar pouco agora sobre identificadores? Que são os identificadores? Identificadores nada mais são do que nomes. A gente vai nomear, novamente, [a] gente vai usar identificadores pra quê? Para nomear uma variável, para nome[ar] uma função, que o cliente pode usar em JavaScript pra nomear as variáveis, nome e as funções, para usar como identificador.

Então tive aqui que os identificadores, eles podem iniciar com underscore ou $. Eles podem começar com qualquer letra minúscula ou qualquer letra maiúscula. Como a gente viu no episódio anterior, ou nos slides anteriores, que o JavaScript é case sensitive, então eu posso com a maiúscula diferente do minúsculo.

Então o identificador, ou o nome de uma variável, no nome de uma função, por exemplo, ele pode iniciar com um underscore, ele pode iniciar com $. São os únicos caracteres diferentes que ele pode iniciar, ou com qualquer letra [de A a] Z. E eles podem conter, além de todos os caracteres que eu já falei, dígitos de 0 a 9. Então, além de você poder usar tanto um underscore, cifrão, letras, jazem no meio do, da tua palavra, ou da tua variável, da função, você pode usar também dígitos de 0 a 9.

E eles podem conter também qualquer caractere Unicode, que os caracteres Unicode... o JavaScript, na verdade, ele têm, eles são escritos com um conjunto de caracteres Unicode. Então esse conjunto de caracteres, e eles são permitidos dentro do script. Então os caracteres Unicode, normalmente, eles englobam a maioria dos tipos de caracteres para maio... para a maioria das línguas existentes no mundo hoje, está?

Então você pode usar qualquer tipo de caracteres. Se você me pergunta: então posso fazer isso, por exemplo, var por variável pi igual a 3,14? Posso fazer isso, por exemplo, que é uma variável aqui, vou colocar um fim 3 ponto 14. Isso aqui vale, isso aqui funciona. Vamos ver: se eu chamar o pi, que acontece? Olha só, ele me retorna o valor 3,14. Assim, dizer que o pi seja igual a você, por exemplo: posso fazer isso? Pode fazer isso. Então, ele viu, o JavaScript funciona com os caracteres Unicode também.

Mas ele funcionou, sim, mas você não deve utilizar. Você não deve utilizar eles, pelo seu bem e pelo bem dos, dos programadores, ou dos próximos desenvolvedores que forem pegando no teu código. Beleza? Porque é bastante... se você não utilizar caracteres comuns, ou caracteres ocidentais, isso que costumam usar, são dígitos, letras de A a Z, underscore, cifrão. O curioso é somente esses caracteres, que são caracteres válidos para nomear suas funções e suas variáveis.

Porque isso aqui vai facilitar bastante para os próximos passos [de] um programador que foi usar o teu código. Já pensou em um cara ao lado da Arábia Saudita, por exemplo, começar a nomear variáveis, ele, com aqueles caracteres arábicos? Entendeu? Ele, ele pode usar aquilo, mas já pensou se ele começa [a] usar aquilo dentro dos nomes de variáveis dele, ou dentro dos nomes de função? Como que a gente aqui no Brasil vai ditar um código dele?

Então, se você deixar algo, se você usar letras maiúsculas e minúsculas, dígitos 0 [a] 9, underscore ou cifrão, você [vai] ter o código mundialmente fácil [de] digitar. Então facilita pra você e facilita para os outros produtos, programadores também. Beleza?

## Palavras reservadas

E o JavaScript também, ele tem algumas, algumas palavras reservadas. Com essas palavras reservadas, eu não coloquei no slide porque ia ocupar muito espaço, então deixei aberta que o link, que eu vou colocar esse link também para você na descrição desse vídeo. Eu vou colar esse link pra você, que é o link que mostra lá no site da MDN, que é o developer Mozilla org. Ele mostra quais são as palavras reservadas em JavaScript.

Que são, o que são essas palavras reservadas? Palavras reservadas, basicamente, são palavras que o JavaScript separa para eles, são identificadores de palavras-chave da própria linguagem. Então são coisas que são usados dentro do JavaScript que você não pode usar para nomear variáveis e nem para nomear funções, ok?

Então essas palavras aqui você não pode usar de jeito nenhum, que são só as palavras: gay, 15, LS, 7, const, continue, debugger, default, delete, do, que se tem falha, ele fora, function, isso, import. Estão todas essas palavras aqui. E aqui tem mais algumas palavras reservadas, que ainda não existem, milhares escritos, estão reservadas pro futuro, para versões futuras, que são: enum, await, implements, protected.

São palavras reservadas do JavaScript que você não pode utilizar, e já foram reservadas futuramente também, para você não utilizar, futuramente o programa, provavelmente o JavaScript vai utilizar essas palavras. Essas, essas palavras no qual ele tá. Então essas palavras indexadas também você não pode usar.

## Encerramento

Então, basicamente, a gente deu um giro pela estrutura léxica do JavaScript. Basicamente são essas regras que você precisa saber. Como, com o andar do curso, a gente vai ver algumas outras regras [que] a gente pode utilizar também, mas basicamente são essas que você precisa ter. Beleza? E agora a gente vai ver qual é o desafio dessa próxima semana, tá, visto no próximo vídeo. Valeu.
