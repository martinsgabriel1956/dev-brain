---
type: concept
title: "Igualdade em JavaScript (== x ===)"
aliases: ["==", "===", "igualdade estrita", "igualdade abstrata", "comparação em JavaScript"]
date_created: 2026-11-16
date_updated: 2026-11-25
source_count: 14
tags: [javascript, tipos, coercao, lang-dynamic]
skill: tech-mentor-frontend
status: stub
---

# Igualdade em JavaScript (== x ===)

`=` atribui; `==` e `===` comparam. A diferença:
- **`===` (estrita)** só dá `true` com o mesmo tipo e o mesmo valor.
- **`==` (abstrata)** converte os tipos antes de comparar: `"1" == 1`, `0 == ""` e `null == undefined` dão `true`.

`!=` e `!==` seguem a mesma regra. Prática comum: `===` sempre, `==` só quando a conversão é intencional (o caso clássico é `x == null`). `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness)

Ver [[wiki/concepts/tipos-primitivos-javascript]], onde está a coerção de `"1" + 12` do dia 2.

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] explica que "o igual assim ele é para atribuir valor. Dois iguais é para comparar valor". Sobre o terceiro igual: "há uma diferença entre dois iguais para três iguais que não nos cabe entender agora [...] Posso colocar só dois ou três tanto faz". Ele usa `==` e `!=` no `findIndex` e no `filter`. O código funciona porque os dois lados são strings vindas de `dataset.id`. Mas não é "tanto faz", pelo mesmo motivo do "tanto faz" de [[wiki/concepts/var-let-const]] no dia 2.

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], o `{% if filters.subject == loop.index %}` do Nunjucks só funciona porque o `==` é frouxo: a query traz a string "2" e o loop dá o número 2. Com `===` nenhuma opção seria selecionada.

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], `{% if proffys == "" %}` reconhece a lista vazia porque `[] == ""` é verdadeiro: o array vira string vazia. É a segunda vez na NLW #2 que o `==` frouxo faz o template funcionar.

Em [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]], o `+` aparece como soma e como concatenação, sem a coerção que os une: `'200' + 200` dá `'200200'`. É a mesma conversão implícita por trás de `==`. Ver [[wiki/concepts/operadores-aritmeticos-javascript]].

## No FrontPUSH, módulo de JavaScript, aula 03 (Násser)

Em [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]], `==` "está comparando o conteúdo" (`10 == '10'` é `true`, "porque ele vai tentar converter o valor") e `===` compara "o conteúdo e o tipo de dado"; `!=` e `!==` são as negações. Certo no resultado, mas o `==` não compara "conteúdo": converte por regras próprias (`0 == ''` e `null == undefined` também dão `true`).

## No JStack, aula 05

Em [[wiki/sources/jstack-criando-a-primeira-rota-da-api]], a rota usa `===` ("igual igual igual") para `request.url` e `request.method`, ambos strings: comparação estrita, sem conversão de tipo.

## No JavaScript Ninja, aula 02 (Fernando Daciuk)

[[wiki/sources/javascript-ninja-operadores-aritmeticos]] termina anunciando "operadores de igualdade e operadores relacionais" para o vídeo seguinte do [[wiki/entities/javascript-ninja|JavaScript Ninja]].

## No JavaScript Ninja, aula 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]], `==` e `!=` comparam e `=` atribui; `'1' == 1` dá true "porque JavaScript, ele faz conversão de tipos", e `===`/`!==` "testam também o tipo". A recomendação é a desta página: "a gente vai usar sempre a notação com três igual [...] porque isso é mais seguro". Imprecisão: `!==` não é "diferente, mas o mesmo tipo"; dá true se o tipo **ou** o valor diferem.

## No JavaScript Ninja, semana 2, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-logicos]], `x === 3 && y === 7` e `y === '7'` falso "porque eu testei pelo tipo". A segunda metade volta ao `!=` × `!==` com `x = 3` e `'3'`: sem testar o tipo, "isso é bastante problemático"; fique com o estrito. Mesma recomendação desta página. Negar a comparação com `!` "não é utilizado": `x !== 3`, não `!(x === 3)` (e `!x === 3` é outra coisa, por precedência).

## No JavaScript Ninja, semana 2, vídeo 04 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-instrucoes-condicionais-if]], todas as condições do `if` usam `===`, como a aula de igualdade recomendou. Também evita o erro de `if (x = 2)`, que atribui e sempre entra.

## No JavaScript Ninja, semana 4, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-truthy-e-falsy]], `'0'` é truthy no `if` e no `!!`. `[external]` Mas `'0' == false` e `[] == false` são `true`, porque o `==` converte para número e não usa *ToBoolean*. Truthy não é o mesmo que `== true`.

## No JavaScript Ninja, semana 4, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-condicional-ternario]], as condições do ternário usam `===` (`1 === 2`, `pessoa.sexo === 'feminino'`). `1 === 2 ? true : false` é redundante: a comparação já devolve booleano ([[wiki/concepts/operador-ternario-javascript]]).

## No JavaScript Ninja, semana 6, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operador-virgula-e-switch]], o `switch` compara com o "igual, igual, igual": "testa o valor e o tipo". Por isso `switch (x)` com `x = '1'` não entra no `case 1` ([[wiki/concepts/estruturas-condicionais-javascript]]).

## No JavaScript Ninja, semana 6, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-estrutura-de-repeticao-while]], o 0 "não é igual a false" com `===`, "mas se eu não testar o tipo, ele é igual a falso" (`0 == false`), para justificar que o `while (0)` não entra ([[wiki/concepts/truthy-e-falsy]]).

## Key sources

- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: `==` e `!=` em findIndex/filter; "tanto faz" (impreciso)
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: == frouxo salva a comparação string x número
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: [] == "" no estado vazio
- [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]]: FrontPUSH, JavaScript aula 02: + como soma e concatenação
- [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]]: FrontPUSH, JavaScript aula 03: == "conteúdo", === conteúdo e tipo
- [[wiki/sources/jstack-criando-a-primeira-rota-da-api]]: === na condição da rota
- [[wiki/sources/javascript-ninja-operadores-aritmeticos]]: JavaScript Ninja, aula 02: igualdade anunciada para o próximo vídeo
- [[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]]: JavaScript Ninja, aula 03: ==, !=, ===, !==; "três igual" por segurança
- [[wiki/sources/javascript-ninja-operadores-logicos]]: JavaScript Ninja, semana 2, vídeo 01: != × !== de novo; === dentro de &&
- [[wiki/sources/javascript-ninja-instrucoes-condicionais-if]]: JavaScript Ninja, semana 2, vídeo 04: === em todas as condições do if
- [[wiki/sources/javascript-ninja-truthy-e-falsy]]: JavaScript Ninja, semana 4, vídeo 01: truthy × `== true`
- [[wiki/sources/javascript-ninja-condicional-ternario]]: JavaScript Ninja, semana 4, vídeo 02: `===` como condição do ternário
- [[wiki/sources/javascript-ninja-operador-virgula-e-switch]]: JavaScript Ninja, semana 6, vídeo 01: switch compara com ===
- [[wiki/sources/javascript-ninja-estrutura-de-repeticao-while]]: JavaScript Ninja, semana 6, vídeo 02: 0 == false, 0 !== false
