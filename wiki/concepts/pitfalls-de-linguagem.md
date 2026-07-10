---
type: concept
title: "Pitfalls de Linguagem"
aliases: ["language pitfalls", "armadilhas de linguagem", "gotchas", "bad parts"]
date_created: 2026-04-22
date_updated: 2026-07-10
source_count: 2
tags: [javascript, typescript, linguagem, qualidade, anti-pattern]
skill: tech-mentor-leadership
status: stable
---

# Pitfalls de Linguagem

Funcionalidades que existem em uma linguagem mas que **não deveriam ser usadas** — seja por comportamento inesperado, risco de bug ou decisões de design que envelheceram mal.

## Por que importam

O argumento de "aprenda 100% de uma linguagem antes de programar" tem um problema: nem tudo que existe numa linguagem é bom. Saber *o que não usar* é parte do aprendizado.

## Exemplos em JavaScript

**`var` — escopo de função, não de bloco**
```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0); // imprime 3, 3, 3 — não 0, 1, 2
}
// Solução: usar let (escopo de bloco)
```

**Coerção implícita**
```javascript
[] + [] // ""
[] + {} // "[object Object]"
{} + [] // 0
"5" - 3 // 2 (coerção numérica)
"5" + 3 // "53" (coerção de string)
```

**`with` statement** — cria escopo dinâmico, impossível de otimizar, proibido em strict mode.

**`==` vs `===`** — coerção de tipo em `==` produz resultados contraintuitivos. Exemplo: `null == undefined` → `true` (coerção), mas `null === undefined` → `false` (comparação estrita, sem conversão).

**`typeof null === "object"`** — bug histórico da linguagem, mantido por compatibilidade retroativa. Internamente tudo em JS deriva de `Object`, então `typeof` erra nesse caso. `Object.prototype.toString.call(null)` (→ `"[object Null]"`) é uma forma mais precisa de checar tipo, historicamente usada em bibliotecas como Underscore. Ver [[wiki/concepts/tipos-primitivos-javascript]] para os 8 tipos primitivos e a comparação completa `typeof` vs. `Object.prototype.toString.call()`.

**Parâmetro default vs. `||` fallback — pitfall sutil.** `function bar(a = [1,2,3])` só usa o default quando `a` é `undefined` — `bar(null)` retorna `null`. Já `a = a || [1,2,3]` substitui *qualquer* valor falsy (incluindo `0` e `null`), não só `undefined`. Confundir os dois mecanismos é fonte comum de bugs silenciosos.

## O padrão geral

Toda linguagem com história longa acumula features que:
- Foram adicionadas antes de boas práticas serem estabelecidas
- Existem por backward compatibility
- Causam bugs difíceis de rastrear em escala

Conhecer os pitfalls permite usar a linguagem com as partes boas e evitar as armadilhas.

## Referência

*JavaScript: The Good Parts* (Douglas Crockford) — livro inteiro dedicado a separar o que usar do que evitar em JS.

## Ver também

- [[concepts/principio-da-inversao]] — hábito ruim nº 4: aprender 100% antes de praticar
- [[concepts/tutorial-hell]] — armadilha de consumir sem construir

## Key Sources

- [[sources/principio-da-inversao-programador]]
- [[wiki/sources/8-tipos-de-javascript]]
