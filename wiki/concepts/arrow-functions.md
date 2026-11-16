---
type: concept
title: "Arrow functions em JavaScript"
aliases: ["arrow function", "função de seta", "=>", "fat arrow", "retorno implícito", "this léxico"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 4
tags: [javascript, funcoes, arrow-function, es6, this, react, vue]
skill: lang-dynamic
status: stub
---

# Arrow functions em JavaScript

Sintaxe curta de função, do ES2015 ([[wiki/concepts/ecmascript]]): `(a, b) => a * b`. Sempre é uma expressão, então vive numa variável (`const f = ...`), num argumento (callback) ou numa propriedade. `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions

## Formas

```js
const area = function (a, b) { return a * b }   // expressão comum
const area = (a, b) => { return a * b }          // arrow com corpo de bloco
const area = (a, b) => a * b                     // retorno implícito
const upper = name => name.toUpperCase()         // um parâmetro, sem parênteses
const nova = () => ({ id: 1 })                   // objeto precisa de parênteses
```

- **Retorno implícito:** só quando o corpo é uma expressão. Com chaves, é bloco, e sem `return` devolve `undefined`.
- **Parênteses:** opcionais só com um parâmetro simples; obrigatórios com zero, padrão, desestruturação ou rest.

## O que muda além da sintaxe

| | `function` | arrow |
|---|---|---|
| `this` | definido por quem chama | o do escopo de fora (léxico) |
| `arguments` | tem | não tem (usar `...args`) |
| `new` / `prototype` | pode ser construtor | não pode |
| Hoisting | a declaração é içada | segue a variável (`const` só depois da linha) |

**Consequências nos frameworks:** no [[wiki/entities/react]], arrow como handler (`onClick={() => setOpen(true)}`) e callback de `map` evitam o `.bind(this)` dos antigos componentes de classe. No [[wiki/entities/vue]] (Options API), `methods`, `computed` e `watch` escritos como arrow perdem o `this` do componente; ali se usa a forma `nome() {}`. Como método de objeto que depende de `this`, a arrow também não serve.

Relacionado: [[wiki/concepts/funcoes-javascript]], [[wiki/concepts/callback-javascript]].

## No FrontPUSH

Em [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]], [[wiki/entities/nasser|Násser]] transforma `function areaRetangulo(a, b)` em expressão, depois em arrow e por fim em `(a, b) => a * b`, e `upperName` em `name => name.toUpperCase()`. Chama cada passo de "exatamente a mesma coisa". A aula anuncia "as diferenças de funções para funções de seta", mas mostra só a sintaxe: a tabela acima é o que faltou.

Em [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]], os métodos usam `this.lado` e `this.a` com `function` e com o shorthand `area() {}`. Escritos como arrow, perderiam esse `this`: é a diferença que a aula 04 não mostrou.

Em [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]], `marcas.forEach(item => console.log(item))`: a aula diz que a seta entra "ao invés de abrir e fechar chaves"; ela entra no lugar do `function`, e as chaves saem só com corpo de expressão. No `map` com chaves, o `return` é obrigatório, e a aula o usa.

Em [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]], o listener vira arrow de uma linha, e depois a aula usa `this.classList` dentro de uma `function`. Em arrow, esse `this` não seria a `.box`; com `function`, `this` é o `currentTarget`.

## Key sources

- [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]]: FrontPUSH, JavaScript aula 04: de function a arrow com retorno implícito
- [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]: FrontPUSH, JavaScript aula 05: this em métodos (arrow não serviria)
- [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]]: FrontPUSH, JavaScript aula 07: arrow em forEach e map
- [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]]: FrontPUSH, JavaScript aula 10: this no listener (function × arrow)
