---
type: concept
title: "Estruturas condicionais em JavaScript (if/else, switch)"
aliases: ["if else", "else if", "switch case", "estrutura encadeada", "operadores lógicos", "&&", "||", "early return"]
date_created: 2026-11-16
date_updated: 2026-11-25
source_count: 10
tags: [javascript, condicionais, if-else, switch, operadores-logicos, controle-de-fluxo]
skill: lang-dynamic
status: stub
---

# Estruturas condicionais em JavaScript

Desviam o fluxo conforme uma condição convertida para booleano ([[wiki/concepts/truthy-e-falsy]]). `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else

## if / else if / else

```js
if (nota >= 9) console.log('A')
else if (nota >= 7) console.log('B')
else console.log('C')
```

A cadeia para na primeira condição verdadeira; o `else` pega o resto. **`if` separados** avaliam todas as condições: é o certo quando mais de uma pode valer ao mesmo tempo, e o errado quando elas se excluem (gasta verificações e pode executar dois blocos). Em funções, o **early return** (`if (!usuario) return`) evita cadeias e aninhamentos fundos.

## Operadores de comparação e lógicos

- Comparação: `>`, `>=`, `<`, `<=`, `===`, `!==` (e os frouxos `==`, `!=`; [[wiki/concepts/igualdade-javascript]]).
- Lógicos: `&&` (e), `||` (ou), `!` (não). `&&` e `||` param no primeiro operando que decide (curto-circuito) e devolvem esse operando, não um booleano. `&&` tem precedência maior que `||`.
- `??` (ES2020) escolhe o padrão só para `null`/`undefined` ([[wiki/concepts/null-e-undefined]]).

## Ternário

`cond ? a : b` é uma expressão: cabe numa atribuição, num template literal ou no JSX ([[wiki/concepts/renderizacao-condicional]]). Página própria: [[wiki/concepts/operador-ternario-javascript]].

## switch

```js
switch (nome) {
  case 'Násser': console.log('nome'); break
  case 'Yousef': console.log('sobrenome'); break
  default: console.log('exceção')
}
```

- Compara com `===`.
- Sem `break`, cai no `case` seguinte (*fall-through*); útil para agrupar (`case 'a': case 'b':`), bug quando esquecido.
- Alternativa comum: um objeto como tabela (`const rotulos = { Násser: 'nome', Yousef: 'sobrenome' }`), com `rotulos[nome] ?? 'exceção'`.

Relacionado: [[wiki/concepts/logica-booleana]], [[wiki/concepts/logica-de-programacao]], e o equivalente na compilação do Sass, [[wiki/concepts/if-else-sass]].

## No FrontPUSH

Em [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]], [[wiki/entities/nasser|Násser]] chama a cadeia `if / else if / else` de "estrutura encadeada" ("uma nova estrutura sempre se inicia com if"), diz que vários `if` seguidos são "teoricamente errado[s]" (são outra lógica, não um erro), agrupa `&&` e `||` com parênteses e mostra o `switch` com `case`, `break` e `default`. Prefere `if/else`, "bem mais aberto".

Em [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]], um `if` dentro do `while` decide quando o contador sobe, "misturar as estruturas condicionais [...] dentro do while". A aula também chama `for` e `while` de "estruturas condicionais"; são de repetição ([[wiki/concepts/estruturas-de-repeticao-javascript]]).

Em [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]], `if (event.key === 'r') ... else if ('b') ... else` troca a cor pela tecla; a aula chama a cadeia de "lista encadeada" (é a "estrutura encadeada" da aula 03).

## No JavaScript Ninja, aula 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]], `==`, `===`, `!=`, `!==`, `>`, `<`, `>=` e `<=` aparecem antes do `if`, testados soltos no REPL ([[wiki/concepts/operadores-relacionais-javascript]]).

## No JavaScript Ninja, semana 2, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-logicos]], `&&`, `||` e `!` combinam as comparações antes de qualquer `if` (que vem em vídeo posterior). Precedência e curto-circuito em [[wiki/concepts/operadores-logicos-javascript]].

## No JavaScript Ninja, semana 2, vídeo 04 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-instrucoes-condicionais-if]], o `if` dá "um controle pra gente [...] tomar algumas decisões", e a condição "vai se tornar um valor booleano". Demonstra `if` sozinho, com `&&` e `||`, com condição falsa (o bloco "simplesmente" é ignorado), `else` ("vai servir como senão") e a cadeia `else if` / `else`, que "é como se fosse mais um if": é isso mesmo, `else if` é um `else` com outro `if` dentro. Sempre com `===` e chaves. Ficam de fora ternário, `switch` e early return.

## No JavaScript Ninja, semana 4, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-truthy-e-falsy]], o `if` vira ferramenta de teste: `if (valor) { teste = true } else { teste = false }` mostra se o valor é truthy. Completa o vídeo 04 da semana 2, que só usou comparações ([[wiki/concepts/truthy-e-falsy]]).

## No JavaScript Ninja, semana 4, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-condicional-ternario]], o ternário "substitui o if" quando o `if`/`else` só escolhe um valor: uma linha no lugar de cinco, "para verificações pequenas" ([[wiki/concepts/operador-ternario-javascript]]).

## No JavaScript Ninja, semana 6, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operador-virgula-e-switch]], o `switch` é "uma outra forma da gente fazer uma estrutura condicional": `case` por valor, comparado com `===` ("testa o valor e o tipo"), `break` para sair e `default` quando nada casa. A demo do `break` esquecido mostra o fall-through: com 2, imprime o `case 2` e também o `default`, "olha só que perigo". Para o instrutor, é a cadeia `if` / `else if` / `else` com `===` escrita "de uma forma um pouco mais legível". A aula diz que, sem `break`, ele "continua avaliando" os outros valores; na verdade executa os corpos seguintes sem testar os `case` ([[wiki/concepts/igualdade-javascript]]).

## No JavaScript Ninja, semana 6, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-estrutura-de-repeticao-while]], o `while` é apresentado pela diferença com o `if`: a mesma condição convertida em booleano, mas "enquanto esse valor for verdadeiro" ele repete ([[wiki/concepts/estruturas-de-repeticao-javascript]]).

## Key sources

- [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]]: FrontPUSH, JavaScript aula 03: if/else if/else, && e ||, switch case
- [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]]: FrontPUSH, JavaScript aula 06: if dentro do while
- [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]]: FrontPUSH, JavaScript aula 10: if/else if por tecla
- [[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]]: JavaScript Ninja, aula 03: comparadores antes do if
- [[wiki/sources/javascript-ninja-operadores-logicos]]: JavaScript Ninja, semana 2, vídeo 01: &&, || e ! para combinar condições
- [[wiki/sources/javascript-ninja-instrucoes-condicionais-if]]: JavaScript Ninja, semana 2, vídeo 04: if, else e else if com && e ||
- [[wiki/sources/javascript-ninja-truthy-e-falsy]]: JavaScript Ninja, semana 4, vídeo 01: if/else para descobrir truthy e falsy
- [[wiki/sources/javascript-ninja-condicional-ternario]]: JavaScript Ninja, semana 4, vídeo 02: ternário como if/else de uma linha
- [[wiki/sources/javascript-ninja-operador-virgula-e-switch]]: JavaScript Ninja, semana 6, vídeo 01: switch, case, break, default e o fall-through do break esquecido
- [[wiki/sources/javascript-ninja-estrutura-de-repeticao-while]]: JavaScript Ninja, semana 6, vídeo 02: while como if que repete
