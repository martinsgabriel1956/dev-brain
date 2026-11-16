---
type: concept
title: "Desestruturação (JavaScript)"
aliases: ["desestruturação", "destructuring", "destructuring assignment", "desestruturar objeto", "desestruturar array"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [javascript, sintaxe, objeto, array, lang-dynamic]
skill: tech-mentor-data
status: stub
---

# Desestruturação (JavaScript)

Sintaxe que tira valores de um objeto ou array direto para variáveis:

- **Objeto:** `const { a, b } = obj` pega as propriedades pelo nome, em qualquer ordem. `{ a: x }` renomeia, e `{ a = 1 }` dá um valor padrão.
- **Array:** `const [x, y] = lista` pega pela posição.
- **Parâmetros:** `function f(db, { a, b })` desestrutura o objeto recebido, o que funciona como argumentos nomeados.

Propriedade que não existe vira `undefined`, sem erro. Desestruturar `undefined` ou `null` lança `TypeError`. Ver [[wiki/concepts/null-e-undefined]] `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], [[wiki/entities/mayk-brito|Mayk]] usa as três formas:

- `const { subjects, weekdays, getSubject } = require("./utils/format")`, em que os nomes "tem que ser exato os mesmos";
- `const [hour, minutes] = time.split(":")`, "mais moderna" que `split(":")[0]`;
- `async function (db, { proffyValue, classValue, classScheduleValues })` no `createProffy`, em que a ordem "não importa, porque se for o mesmo nome, ele sabe identificar".

Ele também usa a forma curta de propriedade, `{ weekday }` no lugar de `{ weekday: weekday }`: "se eu repito os nomes eu não preciso ficar repetindo".

## Key sources

- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: desestruturação no require, no split e nos parâmetros do createProffy
