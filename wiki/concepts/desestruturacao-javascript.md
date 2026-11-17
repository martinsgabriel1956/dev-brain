---
type: concept
title: "Desestruturação (JavaScript)"
aliases: ["desestruturação", "destructuring", "destructuring assignment", "desestruturar objeto", "desestruturar array"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 5
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

## Na NLW #2, dia 2 (Diego Fernandes)

`const { name, avatar, whatsapp, bio, subject, cost, schedule } = request.body`, `const [hour, minutes] = time.split(':').map(Number)` e `const { total } = totalConnections[0]`. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

## Na NLW #2, dia 3 (Diego Fernandes)

`({ label, name, ...rest })` (rest) e `{...rest}` no JSX (spread); `const { total } = response.data`; `[...scheduleItems, novo]` e `{ ...scheduleItem, [field]: value }` com chave computada. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## No JStack, aula 03

Em [[wiki/sources/jstack-o-que-sao-modulos]], `const { printName, lastName } = require('./printName')` desestrutura o objeto exportado, e o acesso deixa de precisar de `modulo.algumaCoisa`. A mesma aula usa o *shorthand* inverso na exportação: `module.exports = { printName, lastName }`.

## No FrontPUSH, JavaScript aula 18

Em [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]], [[wiki/entities/nasser|Násser]] parte do `mousemove`: uma `const` por propriedade (`event.clientX`, `event.clientY`) vira `const { clientX, clientY } = event` e depois `function mouseMove({ clientX, clientY })`, desestruturando "diretamente no argumento". Para arrays, `const [marca1, marca2, marca3, marca4] = carros`: "objeto chaves, array, colchetes". Diz que dá para usar outro nome ("eixoX"), mas não mostra a sintaxe `{ clientX: eixoX }`, sem a qual o valor sai `undefined`. O caso de "desestruturação com funções" que o React usa é `const [count, setCount] = useState(0)`.

## Key sources

- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: desestruturação no require, no split e nos parâmetros do createProffy
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: body, split e count
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: rest, spread e chave computada
- [[wiki/sources/jstack-o-que-sao-modulos]]: desestruturação no require; shorthand no module.exports
- [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]]: FrontPUSH, JavaScript aula 18: objeto, parâmetro e array com mousemove
