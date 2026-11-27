---
type: concept
title: "Tipos Primitivos em JavaScript"
aliases: ["8 tipos de javascript", "typeof javascript", "primitive types javascript", "Object.prototype.toString"]
date_created: 2026-07-10
date_updated: 2026-11-27
source_count: 20
tags: [javascript, tipagem, type-checking, fundamentos]
skill: lang-dynamic
status: draft
---

# Tipos Primitivos em JavaScript

Apesar de JavaScript ser uma linguagem de **tipagem fraca** (fraca no sentido de conversão implícita de tipo entre operações — ver [[wiki/concepts/sistema-de-tipos]]), ela define **oito tipos** de valor: `null`, `undefined`, `boolean`, `number`, `bigint`, `string`, `symbol` e `object`.

## Duas formas de checar tipo

| | `typeof valor` | `Object.prototype.toString.call(valor)` |
|---|---|---|
| **Precisão** | Menos precisa — `typeof null` retorna `"object"` | Mais precisa — retorna `"[object Null]"`, `"[object Array]"` etc. |
| **Motivo** | Internamente, tudo em JS deriva de `Object` | Lê a assinatura interna `[[Class]]` do valor |
| **Uso histórico** | Checagem rápida do dia a dia | Usado por bibliotecas como Underscore para type-checking mais confiável |

`typeof` erra de forma notória em dois casos: `typeof null === "object"` (bug histórico da linguagem, mantido por compatibilidade) e `typeof NaN === "number"` (`NaN` significa "Not a Number", mas seu tipo *é* `number`).

## Os 8 tipos

| # | Tipo | `typeof` |
|---|---|---|
| 1 | `null` | `"object"` |
| 2 | `undefined` | `"undefined"` |
| 3 | `boolean` | `"boolean"` |
| 4 | `number` | `"number"` |
| 5 | `bigint` | `"bigint"` |
| 6 | `string` | `"string"` |
| 7 | `symbol` | `"symbol"` |
| 8 | `object` | `"object"` |

`Array`, `Date`, funções etc. não são tipos primitivos separados — são todos estruturas construídas sobre `object` (funções são exceção parcial: `typeof` de uma função retorna `"function"`).

## `undefined` vs. `null` em valores default

Uma distinção sutil e fonte comum de bugs: **parâmetros default de função só reagem a `undefined`**, não a `null` — porque `null` é considerado um valor "de verdade", enquanto `undefined` é a ausência de valor.

```js
function bar(a = [1, 2, 3]) { return a; }
bar();       // [1, 2, 3] — sem argumento, undefined aciona o default
bar(null);   // null — null É um valor, default não é acionado
```

Já expressões booleanas com `||` (`a = a || [1, 2, 3]`) reagem a **qualquer** valor falsy (`0`, `""`, `null`, `undefined`, `false`, `NaN`) — não só `undefined`. Confundir os dois mecanismos é uma armadilha comum: `bar(0)` com default de parâmetro preserva `0`, mas `a = a || fallback` substitui `0` pelo fallback.

## Conversão de tipo em concatenação e comparação

- `string + number` sempre vira concatenação de string, em qualquer ordem: `"1" + 2` e `1 + "2"` ambos retornam `"12"`.
- `==` faz conversão de tipo antes de comparar (`null == undefined` → `true`); `===` não converte nada. Ver detalhamento em [[wiki/concepts/pitfalls-de-linguagem]].

## Relação com outros conceitos

- [[wiki/concepts/sistema-de-tipos]] — tipagem fraca é sobre *conversão implícita entre tipos*, um eixo distinto (mas relacionado) de tipagem estática vs. dinâmica
- [[wiki/concepts/pitfalls-de-linguagem]] — `typeof null`, `==` vs `===` e coerção implícita já documentados ali como armadilhas gerais; esta página aprofunda o mecanismo tipo a tipo

## Na NLW #1, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] percorre string, number, boolean e undefined (variável sem valor, propriedade inexistente, função sem `return`). Mostra a coerção do `+`: `1 + 12` dá 13, `"1" + 12` dá `"112"`, porque "já que eu não consigo fazer soma de string com número [...] eu vou concatenar".

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], aparecem string (aspas simples ou duplas), boolean (`true` no `cloneNode`, "o famoso 8 ou 80"), null (o retorno de `querySelector` sem resultado) e objetos tipados como NodeList.

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], `Number((hour * 60) + minutes)` concatena: `"09" * 60` vira 540, mas `540 + "00"` vira `"54000"`. O filtro funciona por acaso, porque cadastro e busca usam a mesma função. O certo é `Number(hour) * 60 + Number(minutes)`.

Em [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]], [[wiki/entities/nasser|Násser]] anuncia "os sete tipos de dados" e mostra seis: string, number, boolean, undefined, symbol e object, com `typeof`. Faltam `null` e `bigint`, e a frase "tudo em JavaScript é objeto" ignora que primitivos não são objetos (`'x'.length` funciona por *autoboxing*). `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures

Em [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]], os tipos da aula 02 viram condição: string não vazia e número diferente de 0 são verdadeiros; `''`, `0`, `undefined` e `NaN` são falsos ([[wiki/concepts/truthy-e-falsy]]).

Em [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]], o *autoboxing* aparece de novo como "o string já se torna um objeto": o primitivo ganha um embrulho `String` temporário só para a chamada do método.

Em [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]], pela terceira aula seguida, a string "já é um objeto": `nome.length` e o autocomplete com `indexOf` e `matchAll` são apresentados como prova. É *autoboxing*: o primitivo é embrulhado em `String` só durante o acesso ([[wiki/concepts/objetos-javascript]]).

Em [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]], `typeof frutas` dá `object`, "mas é um objeto do tipo array". Para testar array, `Array.isArray`.

Em [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]], o JSON aceita número, string, booleano, objeto e array; a aula esquece o `null`. `[external]` `undefined`, `Symbol` e funções somem no `JSON.stringify`, `NaN`/`Infinity` viram `null`, e `BigInt` lança `TypeError` (`[skill: lang-dynamic]`, `nodejs-patterns-runtime.md`).

## No JavaScript Ninja, aula 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]], a lista é number, string, boolean, null, undefined, object e array. Inteiro e decimal são o mesmo number ("float, ou como números reais"); `[external]` todo number é double IEEE 754, por isso `0.1 + 0.2 !== 0.3`. Array não é tipo próprio (`typeof []` dá `"object"`), e faltam `symbol` e `bigint`, posteriores à aula. A mesma `x` recebe valores de vários tipos: o tipo está no valor ([[wiki/concepts/sistema-de-tipos]]).

## No JavaScript Ninja, aula 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]], `'1'` e `1` são de tipos diferentes ("eu sei que não é um número, porque ele está entre [...] aspas simples"): `==` os iguala, `===` não. `[external]` `NaN` é o único valor diferente de si mesmo (`NaN !== NaN`); para testar, `Number.isNaN`.

## No JavaScript Ninja, aula 04 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-funcoes]], `soma()` sem argumentos dá `NaN`, "not a number": `undefined + undefined` não é número. `[external]` `typeof NaN` é `"number"`; testa-se com `Number.isNaN`.

## No JavaScript Ninja, semana 2, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-logicos]], `y === '7'` é falso e `y === 7` é true com `y = 7`: "o tipo dele é o número". Mesmo par number × string das aulas de igualdade, agora dentro de `&&` e `||`.

## No JavaScript Ninja, semana 2, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-unarios]], `+'3'` vira o número 3 e `+` sobre "uma frase" dá `NaN`, que "é avaliado como o tipo número [...] mas ele significa que esse valor não é um número". `+x` é `Number(x)`: `+''` é `0`, `+null` é `0`, `+undefined` é `NaN` ([[wiki/concepts/operadores-unarios-javascript]]).

## No JavaScript Ninja, semana 2, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-estrutura-lexica]], `12`, `1.2`, strings e booleanos como literais, "valores que aparecem diretamente no programa". `null` é literal; `undefined` não, é propriedade global ([[wiki/concepts/estrutura-lexica-javascript]]).

## No JavaScript Ninja, semana 3, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]], os tipos se dividem em "duas categorias principais": primitivos (number, inteiro ou "float"; string; boolean; e os "valores especiais" `null` e `undefined`) e objetos, que são "todos os outros". A divisão está certa; a lista é de novo a do ES5, sem `symbol` e `bigint`.

## No JavaScript Ninja, semana 4, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-truthy-e-falsy]], cada primitivo é classificado como truthy ou falsy: `NaN` ("um tipo de número"), `0`, `-0`, `''`, `null` e `false` são falsy; strings preenchidas, inclusive `'0'`, e números diferentes de zero são truthy ([[wiki/concepts/truthy-e-falsy]]).

## No JavaScript Ninja, semana 10, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-wrapper-objects]], primitivos "não são objetos" porque não têm propriedades nem métodos; o `length` de uma string vem de um [[wiki/concepts/wrapper-objects-javascript|wrapper]] temporário. A lista da aula (número, string, booleano, "valor indefinido") omite `null`, `symbol` e `bigint`.

## Key sources

- [[wiki/sources/8-tipos-de-javascript]]
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: coerção string + number; undefined
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: string, boolean, null, NodeList
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: + concatena string em convertHoursToMinutes
- [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]]: FrontPUSH, JavaScript aula 02: "sete tipos", seis mostrados, sem null e bigint
- [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]]: FrontPUSH, JavaScript aula 03: tipos como verdadeiro ou falso
- [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]]: FrontPUSH, JavaScript aula 04: string "vira objeto" no método
- [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]: FrontPUSH, JavaScript aula 05: "toda variável já é um objeto"
- [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]]: FrontPUSH, JavaScript aula 06: typeof de array
- [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]]: FrontPUSH, JavaScript aula 11: tipos aceitos pelo JSON
- [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]]: JavaScript Ninja, aula 01: sete tipos com array no lugar de symbol e bigint; inteiro e decimal no mesmo number
- [[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]]: JavaScript Ninja, aula 03: '1' × 1 com == e ===
- [[wiki/sources/javascript-ninja-funcoes]]: JavaScript Ninja, aula 04: NaN em soma() sem argumentos
- [[wiki/sources/javascript-ninja-operadores-logicos]]: JavaScript Ninja, semana 2, vídeo 01: 7 × '7' com ===
- [[wiki/sources/javascript-ninja-operadores-unarios]]: JavaScript Ninja, semana 2, vídeo 02: +'3' e NaN do tipo number
- [[wiki/sources/javascript-ninja-estrutura-lexica]]: JavaScript Ninja, semana 2, vídeo 03: primitivos como literais
- [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]]: JavaScript Ninja, semana 3, vídeo 01: primitivos × objetos; cinco primitivos da era ES5
- [[wiki/sources/javascript-ninja-truthy-e-falsy]]: JavaScript Ninja, semana 4, vídeo 01: primitivos por truthy/falsy
- [[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos]]: JavaScript Ninja, semana 5, vídeo 01: primitivos como os retornos usados até ali; faltam symbol e bigint
- [[wiki/sources/javascript-ninja-wrapper-objects]]: JavaScript Ninja, semana 10, vídeo 01: primitivo sem propriedades; wrapper explica o length
