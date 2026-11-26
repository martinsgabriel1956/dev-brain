---
type: concept
title: "Closure (JavaScript)"
aliases: ["closure", "closures", "clausura", "fechamento", "função que lembra o escopo"]
date_created: 2026-11-25
date_updated: 2026-11-26
source_count: 3
tags: [javascript, funcoes, closure, escopo, programacao-funcional]
skill: lang-dynamic
status: stub
---

# Closure (JavaScript)

Uma closure é uma função junto com as variáveis do escopo onde ela foi criada. A função continua enxergando e usando essas variáveis mesmo depois que a função de fora terminou `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures). Em JavaScript, toda função é uma closure: o escopo é léxico, decidido por onde a função foi escrita ([[wiki/concepts/escopo-javascript]]).

```js
function adder(x) {
  return function (y) { return x + y; };  // captura x
}
var add2 = adder(2);   // adder já terminou, mas x = 2 segue vivo
add2(3);               // 5
var add10 = adder(10); // outro escopo, outro x
add10(1);              // 11; add2(1) continua 3
```

Depende de [[wiki/concepts/funcoes-de-primeira-classe|funções de primeira classe]], já que a função precisa poder ser retornada ou passada adiante. É a base de [[wiki/concepts/currying|currying]] e aplicação parcial, do *module pattern* da era ES5 (estado privado devolvido num objeto) e de muitos callbacks. Função que devolve closure é uma [[wiki/concepts/funcao-de-ordem-superior|função de ordem superior]].

## Armadilhas

- **Captura da variável, não do valor.** Com `var` num `for`, todos os callbacks veem o mesmo `i` final; `let` cria um `i` por volta ([[wiki/concepts/var-let-const]]) `[external]`.
- **Valor antigo preso.** No React, o callback criado numa renderização enxerga o estado daquela renderização ([[wiki/concepts/stale-closure]]).
- **Memória.** Enquanto a closure for alcançável, as variáveis que ela captura não são coletadas ([[wiki/concepts/gerenciamento-de-memoria]]) `[external]`.

## No JavaScript Ninja, semana 8, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]], o `adder` acima aparece como exemplo de função que retorna função: "eu vou somar 3 com o 2 que eu já tinha passado na primeira vez". A aula mostra o efeito sem usar a palavra closure.

## No JavaScript Ninja, semana 9, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-escopo-de-funcoes]], `sum` lê `number1` e `number2` de `myFunction`, e a aula diz que ela "está fazendo o papel de uma coisa [...] que a gente vai ver mais para frente", "uma função que ela consegue acessar parâmetros externos a ela". A legenda engole o nome; provavelmente closure (média). A aula também diz que `sum` "só existe enquanto myFunction existia", o que só vale porque o exemplo devolve `sum()`, não `sum`; o `adder` da semana 8 já mostrava a função interna sobrevivendo à externa.

## No JavaScript Ninja, semana 9, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-iife]], a IIFE isola variáveis num escopo local. `[external]` Quando ela devolve funções que usam essas variáveis, elas são closures: é o *module pattern* da era ES5 citado acima ([[wiki/concepts/iife]]).

## Key sources

- [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]]: JavaScript Ninja, semana 8, vídeo 03: adder/add2, o 2 lembrado pela função interna
- [[wiki/sources/javascript-ninja-escopo-de-funcoes]]: JavaScript Ninja, semana 9, vídeo 01: função interna lê as variáveis da externa; nome adiado
- [[wiki/sources/javascript-ninja-iife]]: JavaScript Ninja, semana 9, vídeo 03: IIFE, a base do module pattern
