---
type: concept
title: "Arrow functions em JavaScript"
aliases: ["arrow function", "função de seta", "=>", "fat arrow", "retorno implícito", "this léxico"]
date_created: 2026-11-16
date_updated: 2026-11-26
source_count: 11
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

Em [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]], a aula lembra das arrow functions para dizer que a desestruturação vale "não só para variáveis, mas também para funções". O exemplo concreto é tirar funções de objetos ou arrays, como `const [count, setCount] = useState(0)` ([[wiki/concepts/desestruturacao-javascript]]).

## No JavaScript Ninja, semana 8, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]], o curso passa a nomear toda função. `[external]` Arrow function não tem sintaxe para nome: o `name` dela vem só da inferência do ES2015 (`const soma = () => {}` dá `'soma'`), e passada direto como callback fica sem nome no stack trace.

## No JavaScript Ninja, semana 8, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]], o `adder` é escrito com `function` e dois `return`. `[external]` Com arrow, a versão curried cabe numa linha, `const adder = x => y => x + y`, e `adder(5)(8)` dá o mesmo 13 (verificado). É um dos usos em que o retorno implícito mais encurta o código ([[wiki/concepts/currying]]).

## No JavaScript Ninja, semana 9, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-escopo-de-funcoes]], a declaração `function sum() {}` depois do `return` funciona. `[external]` A mesma função como `const sum = () => 3` lança `ReferenceError: Cannot access 'sum' before initialization` (verificado no Node 22), a linha "Hoisting" da tabela acima ([[wiki/concepts/hoisting-javascript]]).

## No JavaScript Ninja, semana 9, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-hoisting]], a função atribuída a `var` depois do `return` dá `TypeError: sum is not a function`. `[external]` Uma arrow em `const` no mesmo lugar dá `ReferenceError` de zona morta temporal: qualquer função guardada em variável segue o hoisting da variável ([[wiki/concepts/hoisting-javascript]]).

## Key sources

- [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]]: FrontPUSH, JavaScript aula 04: de function a arrow com retorno implícito
- [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]: FrontPUSH, JavaScript aula 05: this em métodos (arrow não serviria)
- [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]]: FrontPUSH, JavaScript aula 07: arrow em forEach e map
- [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]]: FrontPUSH, JavaScript aula 10: this no listener (function × arrow)
- [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]]: FrontPUSH, JavaScript aula 18: arrow function citada no fecho
- [[wiki/sources/frontpush-o-que-preciso-saber-de-javascript-antes-do-react]]: FrontPUSH, React aula 02: sintaxe para "bater o olho" no React, "pouquíssima verbosidade"
- [[wiki/sources/frontpush-jsx-webpack-babel-react-createelement-create-react-app]]: FrontPUSH, React aula 06: componente como arrow function; exemplo de sintaxe que os browsers não entendiam
- [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]]: JavaScript Ninja, semana 8, vídeo 01: regra de nomear não se aplica a arrow; nome só por inferência
- [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]]: JavaScript Ninja, semana 8, vídeo 03: adder em uma linha com arrow
- [[wiki/sources/javascript-ninja-escopo-de-funcoes]]: JavaScript Ninja, semana 9, vídeo 01: declaração içada; arrow em const não
- [[wiki/sources/javascript-ninja-hoisting]]: JavaScript Ninja, semana 9, vídeo 02: função em variável não é içada com o corpo
