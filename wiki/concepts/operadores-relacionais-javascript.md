---
type: concept
title: "Operadores relacionais em JavaScript (<, >, <=, >=)"
aliases: ["operadores relacionais", "operadores de comparação", "maior que", "menor que", "maior ou igual", "menor ou igual", "<", ">", "<=", ">=", "comparação de strings"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 1
tags: [javascript, operadores, comparacao, coercao, boolean]
skill: lang-dynamic
status: stub
---

# Operadores relacionais em JavaScript (`<`, `>`, `<=`, `>=`)

Comparam dois valores e devolvem `true` ou `false` ([[wiki/concepts/logica-booleana]]). `>=` e `<=` são "maior ou igual" e "menor ou igual": `1000 >= 1000` é `true`, `1000 > 1000` é `false`. `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#relational_operators

Regras de conversão, diferentes das do `==` ([[wiki/concepts/igualdade-javascript]]):

| Operandos | O que acontece | Exemplo |
|---|---|---|
| dois números | comparação numérica | `10 < 100` → `true` |
| duas strings | caractere a caractere (unidades UTF-16), não numérica | `'10' < '9'` → `true`; `'B' < 'a'` → `true` |
| tipos mistos | convertem para número | `'10' < 9` → `false` |
| `null` | vira 0 aqui, mas não no `==` | `null >= 0` → `true`, `null == 0` → `false` |
| `NaN` ou `undefined` | qualquer comparação dá false | `NaN < 1`, `NaN >= 1` → `false` |

- Não há versão estrita: para evitar conversão, converta antes (`Number(x)`) ou garanta o tipo.
- Para ordenar texto de pessoas, `a.localeCompare(b)` respeita acentos e idioma; `<` só compara códigos ([[wiki/concepts/string]]).
- `array.sort()` sem função compara como string: `[10, 9, 1].sort()` dá `[1, 10, 9]` ([[wiki/concepts/metodos-de-array-javascript]]).
- São a base das condições de [[wiki/concepts/estruturas-condicionais-javascript|if]] e de [[wiki/concepts/estruturas-de-repeticao-javascript|loops]] (`i < arr.length`).

## No JavaScript Ninja (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]], os quatro operadores são "como a matemática", com a dica do jacaré: "a boca do jacaré sempre come o maior". Exemplos só com números: `1 > 2`, `2 < 3`, `1000 >= 1000`, `40 <= 40`. Comparação de strings e tipos mistos não aparece.

## Key sources

- [[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]]: <, >, <=, >= com números; mnemônico do jacaré
