---
type: concept
title: "Closure (JavaScript)"
aliases: ["closure", "closures", "clausura", "fechamento", "função que lembra o escopo"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 1
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

## Key sources

- [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]]: JavaScript Ninja, semana 8, vídeo 03: adder/add2, o 2 lembrado pela função interna
