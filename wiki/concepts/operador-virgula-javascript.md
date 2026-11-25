---
type: concept
title: "Operador vírgula em JavaScript"
aliases: ["operador vírgula", "comma operator", "operador de sequência", "sequence expression", "vírgula no JavaScript"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 2
tags: [javascript, operadores, operador-virgula, expressoes]
skill: lang-dynamic
status: stub
---

# Operador vírgula em JavaScript

`expr1, expr2, ..., exprN` avalia cada expressão da esquerda para a direita e produz o valor da **última**. É o operador de menor precedência da linguagem, por isso quase sempre aparece entre parênteses ou num lugar que já delimita a expressão (`return`, terceira parte do `for`). `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator

```js
function f() { var x = 0; return x += 1, x }  // 1, igual a return ++x
for (var i = 0, j = 9; i < j; i++, j--) {}     // o i++, j-- é o operador vírgula
```

## Vírgulas que não são o operador

`[external]` A maioria das vírgulas do JavaScript é só sintaxe de separação e não produz valor:

- na declaração: `var a, b = 2, c` (e `let`/`const`). É uma instrução com uma lista de declarações, não uma expressão ([[wiki/concepts/var-let-const]], [[wiki/concepts/expressao-javascript]]). No `for (var i = 0, j = 9; ...)` acima, a primeira vírgula é desse tipo;
- em argumentos e parâmetros: `f(a, b)`;
- em literais: `[1, 2]`, `{ a: 1, b: 2 }`.

Para ter o operador nesses lugares é preciso parênteses: `f((a, b))` passa um argumento só, `b`.

## Uso e estilo

- Usos legítimos: atualizar dois contadores no `for`, e código minificado (que troca blocos por sequências).
- Fora disso, é lido como truque. O ESLint tem `no-sequences`; o `return x += 1, x` é mais claro como `x += 1; return x` ou `return ++x` ([[wiki/concepts/incremento-e-decremento]]).
- A declaração com várias variáveis num só `var` é outra discussão (regra `one-var`); guias atuais como o da Airbnb pedem uma declaração por variável.

## No JavaScript Ninja, semana 6, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operador-virgula-e-switch]], a vírgula "junta várias expressões em uma única expressão", avaliada "da esquerda para direita". Os exemplos são `var a, b = 2, c` (que é a vírgula da declaração, não o operador), `return x += 1, x` ("a mesma coisa que [...] pré-incremento") e uma função cujas variáveis declaradas na lista ficam locais. O curso adota um `var` por variável, para facilitar mover e remover linhas.

## No JavaScript Ninja, semana 7, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-arrays-metodo-push-e-loop-for]], o cabeçalho do `for` inicializa duas variáveis (`var num = 2, arroz = 3`), vírgula de declaração. Incrementar as duas no cabeçalho (`num++, arroz++`) seria o operador vírgula; a aula sugere incrementar `arroz` no corpo ou "aqui em cima".

## Key sources

- [[wiki/sources/javascript-ninja-operador-virgula-e-switch]]: JavaScript Ninja, semana 6, vídeo 01: vírgula na declaração e no retorno; um var por variável
- [[wiki/sources/javascript-ninja-arrays-metodo-push-e-loop-for]]: JavaScript Ninja, semana 7, vídeo 03: duas variáveis no cabeçalho do for
