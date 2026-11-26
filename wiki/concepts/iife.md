---
type: concept
title: "IIFE (Immediately-Invoked Function Expression)"
aliases: ["IIFE", "IIFEs", "função autoexecutável", "função auto executável", "função autoinvocada", "expressão de função invocada imediatamente", "self-invoking function"]
date_created: 2026-11-26
date_updated: 2026-11-26
source_count: 1
tags: [javascript, funcoes, iife, escopo, function-expression, module-pattern]
skill: lang-dynamic
status: stub
---

# IIFE (Immediately-Invoked Function Expression)

Uma função escrita como **expressão** e chamada no mesmo lugar em que é definida `[external]` (https://developer.mozilla.org/en-US/docs/Glossary/IIFE):

```js
(function () {
  var privado = 1;   // não vaza para fora
})();

(function () { /* ... */ }());  // mesma coisa, chamada dentro dos parênteses
(() => { /* ... */ })();        // com arrow function
;(function () { /* ... */ })(); // ; na frente, para código sem ponto e vírgula
```

- **Por que os parênteses:** em início de instrução, `function` é lido como declaração, e a declaração não aceita `()` depois (`SyntaxError`). Os parênteses, ou `!`, `void` e `+`, forçam contexto de expressão ([[wiki/concepts/expressao-javascript]]).
- **Para que serve:** criar um escopo de função descartável, para que as variáveis não vão para o global ([[wiki/concepts/poluicao-do-escopo-global]], [[wiki/concepts/escopo-javascript]]). Devolvendo um objeto com algumas funções internas, vira o *module pattern*: as funções são [[wiki/concepts/closure-javascript|closures]] sobre o estado privado ([[wiki/concepts/encapsulamento]]).
- **Hoje:** módulos ES têm escopo próprio por arquivo, e `let`/`const` num bloco `{ }` criam escopo sem função. A IIFE sobra para scripts clássicos, para `(async () => { await ... })()` fora de módulo e no código que bundlers geram.
- **Armadilha:** sem `;` na linha anterior, `(function...)()` é lido como chamada do valor da linha de cima (`TypeError: 1 is not a function`, verificado no Node 22).

## No JavaScript Ninja, semana 9, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-iife]], a IIFE é "uma expressão [de] função invocada imediatamente, ou uma função auto executável". O caminho até ela: uma função só se invoca pelo nome, pela variável ou pela propriedade de objeto; a declaração seguida de `()` dá "um erro sintático"; envolvida em parênteses, ela vira "uma expressão de função" e executa "a partir do momento em que ele termina de fazer a leitura". A vantagem é que "você fecha um escopo local". A partir daí, todos os desafios do curso vêm dentro de uma IIFE.

## Key sources

- [[wiki/sources/javascript-ninja-iife]]: JavaScript Ninja, semana 9, vídeo 03: declaração × expressão; parênteses; escopo local; desafios dentro de IIFE
