---
type: source
title: "Estruturas condicionais em JavaScript: booleanos, comparadores, if/else e switch case (FrontPUSH)"
aliases: ["FrontPUSH estruturas condicionais", "módulo de JavaScript ES6, aula 03", "Estruturas Condicionais"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, booleano, truthy-falsy, comparadores, igualdade, if-else, else-if, switch-case, operadores-logicos, console-log, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-estruturas-condicionais-booleanos-comparadores-javascript.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Estruturas condicionais em JavaScript (FrontPUSH)

## TL;DR

Aula 03 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] (usa nome, sobrenome e "terceiro nome" como dados de exemplo). Só voz e tela, como na aula 02.

- **Booleano:** "sempre vai ser ou verdadeiro ou falso", e uma estrutura condicional "só entende isso": converte qualquer valor para `true` ou `false`.
- **Truthy e falsy:** string não vazia e número diferente de 0 entram no `if`; `''`, `0`, `false`, `undefined` e `NaN` caem no `else`. "É mais fácil tratar o falso porque ele é mais específico." `!` nega. Ver [[wiki/concepts/truthy-e-falsy]].
- **Comparadores:** `>`, `>=`; `==` "compara o conteúdo" (`10 == '10'` é `true`), `===` compara "o conteúdo e o tipo de dado"; `!=` e `!==`. Ver [[wiki/concepts/igualdade-javascript]].
- **if / else if / else:** `if` é "sempre a primeira condição", `else` "a exceção", `else if` quantas quiser no meio. Na "estrutura encadeada", a primeira condição verdadeira faz pular o resto. Vários `if` seguidos são "teoricamente errado[s]" porque todos são verificados. Ver [[wiki/concepts/estruturas-condicionais-javascript]].
- **Operadores lógicos:** `&&` (as duas precisam ser verdadeiras) e `||`, com parênteses para agrupar.
- **switch case:** "específico com relação apenas à comparação" de uma variável; `case` + `break` ("vai frear, vai pular") e `default` como exceção. Ele prefere `if/else`, "bem mais aberto".
- **Hábito:** "o programador sempre tem que estar plotando no console" para ver o caminho do código ([[wiki/concepts/debugging]]).

## Key Claims

### Booleano e conversão

- "Se eu vir aqui e criar uma variável let com o nome de boolean, eu posso atribuir para ela um valor true ou um valor falso. Sempre vai ser ou verdadeiro ou falso."
- "Uma estrutura condicional só entende isso, ela sempre vai sintetizar alguma comparação, alguma variável a simplesmente true ou false."
- "Ele identifica sempre, sempre, sempre, um string como verdadeiro [...] uma string que não seja vazia, ela entende como verdadeiro." Vazia cai no falso.
- "O único número que ele entende como falso é o 0 e a única string que ele entende como falso é vazio." 10, 800 e 875 são verdadeiros.
- `!` "sempre vai negar o valor booleano": `!0` entra no verdadeiro, `!1` no falso.
- "É mais fácil tratar o falso porque ele é mais específico, o verdadeiro entende muito mais coisas como verdadeiro do que como falso." Lista: `0`, vazio, `false`, [um item sem legenda], `undefined` e `NaN` ("quando algo não é um número").

### Comparadores e igualdade

- `10 > 5` é `true`, `5 > 10` é `false`, `10 >= 10` é `true`, `10 >= 12` é `false`.
- "Quando eu estou colocando o igual, igual só duas vezes, ele está comparando o conteúdo [...] se eu transformar esse 10 em uma string, ele vai continuar apresentando true, porque ele vai tentar converter o valor."
- "Quando eu quero comparar o conteúdo e o tipo de dado, eu coloco três iguais." Com a exclamação, "significa diferente"; com mais um `=`, compara também o tipo.

### if, else if e else

- `if` "se for traduzido em inglês, ele significa se [...] você vai colocar uma proposição aqui dentro e essa proposição vai ser traduzida em simplesmente um valor booleano".
- `else` "é se não, ou seja, a exceção, se não coube em nenhuma das condições acima, ele cai no else."
- "A estrutura condicional é cada bloquinho desse aqui. Quando eu coloco mais blocos com relação à mesma variável e tudo mais, eu chamo de estrutura encadeada."
- "If é sempre a primeira condição, else é sempre a exceção de todas as condições acima. E o else if é quantas condições eu posso colocar no meio. Posso colocar duas, três, quatro, cinco, 10, 20, 30, 50, mil."
- "Ele lê esse quesito aqui linha a linha [...] A primeira condição é satisfeita? Se sim, ele vai ler isso aqui e ele vai ignorar todos os blocos que estão na estrutura encadeada." "Uma nova estrutura sempre se inicia com if."
- "É teoricamente errado você construir estruturas encadeadas só com if, porque você está fazendo if, if, if, if e ele sempre vai verificar todas."

### Operadores lógicos

- "E comercial e e comercial [...] as duas têm que ser true." "Você consegue [...] colocar várias proposições assim com parênteses": `(c1 && c2) || (c3 && c4)`.
- "Quando eu tenho duas barras retas é ou e quando eu coloco dois e comercial junto são e."

### switch case

- "Eu, particularmente, prefiro bem mais o if else, ele é bem mais aberto [...] no if else você consegue colocar proposições aqui dentro." O switch é "específico com relação apenas à comparação".
- `switch (nome)` com `case 'Yousef'` ("esse é o sobrenome"), `case 'Násser'` ("esse aqui é o nome"), `case 'Ali'` ("esse é o terceiro nome") e `default` ("essa é a exceção").
- `break` "é como se fosse eu estou separando aqui um bloco [...] ele vai entrar nesse bloco e vai brecar, vai frear, vai pular".
- Exercício: repetir a aula e comparar `'Ali'` com `'ali'` no console.

### Console como hábito

- "Eu, justamente, estou sempre plotando no console para vocês criarem esse hábito. O programador sempre tem que estar plotando no console para ver qual é a direção que o código está tomando, já que a gente está criando, agora, bifurcações."

## Entities

- [[wiki/entities/nasser]]: instrutor (nome, sobrenome e terceiro nome nos exemplos).
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6.
- [[wiki/entities/javascript]]: assunto da aula.

## Concepts

- [[wiki/concepts/truthy-e-falsy]] (criado neste ingest)
- [[wiki/concepts/estruturas-condicionais-javascript]] (criado neste ingest)
- [[wiki/concepts/igualdade-javascript]]
- [[wiki/concepts/logica-booleana]]
- [[wiki/concepts/logica-de-programacao]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/null-e-undefined]]
- [[wiki/concepts/operadores-aritmeticos-javascript]]
- [[wiki/concepts/renderizacao-condicional]]
- [[wiki/concepts/if-else-sass]]
- [[wiki/concepts/debugging]]

## Precisões e tensões com a wiki

`⚠️` Sem arquivo de referência na skill lang-dynamic para fundamentos de JavaScript; as precisões vêm do MDN e da especificação (`[external]`).

- **A lista de falsy tem oito itens, e a aula dá cinco (seis com o item sem legenda).** `[external]` `false`, `0`, `-0`, `0n`, `''`, `null`, `undefined` e `NaN` (https://developer.mozilla.org/en-US/docs/Glossary/Falsy). O item sem legenda, entre `false` e `undefined`, é quase certamente `null`. "O único número [falso] é o 0" esquece `-0`, `NaN` (que ele cita depois) e o `0n` do `bigint`. Ver [[wiki/concepts/truthy-e-falsy]].
- **Armadilhas de truthy que a aula não mostra:** `'0'`, `'false'`, `' '` (espaço), `[]` e `{}` são verdadeiros. `if (lista)` não detecta lista vazia; é `lista.length`. Ver [[wiki/concepts/truthy-e-falsy]].
- **`==` não compara "só o conteúdo".** `[external]` Ele converte os tipos por regras próprias (`0 == ''`, `null == undefined`, `[] == ''` dão `true`; `NaN == NaN` dá `false`). A wiki já tem os casos em que o `==` frouxo salvou templates da NLW #2 ([[wiki/concepts/igualdade-javascript]]).
- **Vários `if` seguidos não são "errados".** São outra lógica: condições independentes, todas avaliadas. Use `else if` quando as condições se excluem (uma faixa de nota, um status) e `if` separados quando mais de uma pode valer. Em funções, o *early return* (`if (!x) return`) evita o encadeamento ([[wiki/concepts/estruturas-condicionais-javascript]]).
- **Estrutura "encadeada"** é o nome da aula para a cadeia `if / else if / else`. Não confundir com `if` aninhado (um dentro do outro), que é outra coisa.
- **`&&` e `||` devolvem um dos operandos, não um booleano.** `[external]` `'a' || 'b'` dá `'a'`, `0 && x` dá `0`, e a avaliação para no primeiro valor que decide (curto-circuito). Daí o `cond && <A />` do React ([[wiki/concepts/renderizacao-condicional]]) e o `valor || padrão`, que troca também o `0` e o `''` (o `??` só troca `null`/`undefined`; [[wiki/concepts/null-e-undefined]]). `&&` tem precedência maior que `||`, então os parênteses de `(c1 && c2) || (c3 && c4)` são opcionais, mas deixam claro.
- **`switch` compara com `===`.** `[external]` `case '10'` não casa com `10` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch). Sem `break`, a execução "cai" no próximo `case` (*fall-through*), que é útil para agrupar casos e um bug comum quando esquecido. O `default` não precisa ser o último.
- **`if` "traduz em booleano"** está certo: a especificação aplica `ToBoolean` à condição. O mesmo vale para `while`, ternário e `!` ([[wiki/concepts/logica-booleana]]).
- **Console como hábito:** bom para começar. `[external]` O depurador do navegador (`debugger`, breakpoints no DevTools) mostra o caminho sem editar o código ([[wiki/concepts/debugging]]).
- **Comparação de strings é sensível a maiúsculas.** O exercício `'Ali'` × `'ali'` dá `false`; para ignorar a caixa, `a.toLowerCase() === b.toLowerCase()` ou `localeCompare` com `sensitivity: 'base'`.

## Open Questions

- Trechos sem legenda: 00:05:37–00:05:53 (16 s, depois do `!1`), 00:06:19–00:06:21 (o item falsy entre `false` e `undefined`, provável `null`), 00:06:40–00:06:53, 00:08:07–00:08:15 (provável demo do `===`), 00:08:39–00:08:43 (o `!=`) e 00:09:08–00:09:15 (antes de "Condição um").
- "Ali, que é o meu nome" no fim da aula contra "Ali, que é o meu terceiro nome" no switch: a legenda não mostra se ele se corrigiu.

## Raw quotes

- "uma estrutura condicional só entende isso"
- "é mais fácil tratar o falso porque ele é mais específico"
- "o programador sempre tem que estar plotando no console"
