---
título: "Codificação de Caracteres: ASCII, ISO-8859-1 e Unicode"
autor: "Professor Olibário"
tipo: transcrição de vídeo (aula)
idioma_original: português
data_ingestão: 2026-07-31
---

Oi, oi, pessoal, professor Olibário aqui. Hoje a gente vai falar sobre codificação de caracteres.

A codificação é o mapeamento dos símbolos que a gente está acostumado a ver no nosso dia a dia — e alguns outros símbolos também — em códigos que podem ser entendidos pelo computador. Por exemplo, existe uma classificação e a gente já vai ver, lá daqui a pouco, que informa que o caractere A maiúsculo é dado por esse código binário aqui: `01000001`, ou seja, o número 65. Isso significa que toda vez que o computador estiver trabalhando com essa codificação aqui e ele se deparar com este valor na memória, ele vai saber que isso daqui é a letra A maiúscula.

## ASCII

A codificação mais antiga e mais simples que a gente tem é a ASCII. Essa codificação utiliza a tabela ASCII, que é uma tabela que representa os símbolos em 8 bits, mas só 7 bits são de fato dados — o primeiro bit da série é utilizado como bit de verificação.

Por utilizar 7 bits de dados, ela consegue representar valores de 0 a 127, porque 127 é `1111111`, ou seja, 7 bits em 1. Vocês já devem imaginar que, com 127 valores, a gente não consegue codificar todos os símbolos que existem no mundo. Pensa, por exemplo, no árabe, no chinês, no japonês — são vários símbolos completamente diferentes dos que nós utilizamos.

Então essa tabela aqui não é utilizada em qualquer contexto — inclusive ela não é utilizada no Brasil com frequência, porque ela não contempla os caracteres acentuados.

Os primeiros símbolos da tabela ASCII não são imprimíveis. Então aqui a gente tem, por exemplo, de 0 a 12, nenhum desses pode ser visto a olho nu. O primeiro, por exemplo, é o caractere nulo — nas strings em C, ele termina uma cadeia de caracteres. A gente tem outros símbolos aqui para representar, por exemplo, o botão Esc do teclado, o botão Delete, o botão Backspace, e assim por diante.

Na tabela ASCII, as letras do alfabeto começam no número 65. Então 65, que em binário é aquele valor ali, é o A maiúsculo; 66 é o B maiúsculo; 67 é o C maiúsculo; e assim por diante. Após as letras maiúsculas, a gente tem alguns caracteres especiais, e depois começam as letras minúsculas.

Percebam que a gente não tem, então, à, ã — a gente não tem acento agudo, a gente não tem circunflexo, til. É uma tabela com as suas limitações.

## ISO-8859-1 (Latin-1)

Por conta disso, a gente tem outras codificações que são mais abrangentes. Por exemplo, a ISO-8859-1, também conhecida como Latin-1. Ao contrário da ASCII, que tem 7 bits de dados, a ISO-8859-1 utiliza 8 bits — utilizando um bit a mais, ela consegue representar o dobro de símbolos da tabela ASCII. Então, ao invés de termos símbolos de 0 a 127, temos símbolos de 0 a 255.

Observando a tabela dessa codificação, a gente percebe que até o 127 ela é idêntica à tabela ASCII, e depois ela tem novos símbolos — notem que ela já tem os caracteres acentuados. Por isso ela é bastante utilizada no Brasil e em vários outros países; ela abrange a maioria dos países do mundo.

## Unicode

Existe ainda uma outra codificação, que é a Unicode, que utiliza de 8 bits até 32 bits — então pode usar aí 4 bytes de informação. Com essa quantidade de bits, ela consegue representar símbolos de todos os idiomas do mundo. A mais comum, utilizada na web, é a Unicode UTF-8.

## Exercício

Vamos ver um exercício para ver se ficou claro. Sabendo que a letra A maiúscula é representada pelo código 65 na tabela ASCII, que os valores dessa tabela são representados em 8 bits, sendo o primeiro sempre zero, e que os caracteres do alfabeto são contíguos (ou seja, a gente tem o A, depois o B, o C, o D, e assim por diante), decodifique a mensagem a seguir.

Nós já sabemos que a codificação é ASCII e que a gente precisa separar isso aqui de 8 em 8 bits. Então os primeiros 8 bits serão um caractere, depois temos mais 8 bits compondo o segundo caractere, mais 8 bits compondo o terceiro caractere, e por fim os últimos 8 bits compondo o quarto caractere. Temos uma mensagem de 4 caracteres aqui.

O exercício nos informa que 65 é a letra A. 65 em binário é `01000001`. A gente vai ver o que são esses números aqui — então, para cada grupo de 8, a gente vai ver qual é o número em decimal.

- O primeiro grupo é 66.
- O segundo número é 69.
- O terceiro é 67.
- O quarto é 65.

65 é a letra A. Então 66 vai ser B, 67 vai ser C, 68 vai ser D, 69 vai ser E. Então aqui eu tenho a letra B seguida da letra E; na sequência, temos a letra C; e, por fim, a letra A. Portanto, a mensagem escrita aqui na codificação ASCII é: BECA.

Espero que vocês tenham gostado do vídeo. Se gostaram, deem um joinha aqui embaixo, se inscrevam para novos vídeos no canal. Um abraço, e até a próxima!
