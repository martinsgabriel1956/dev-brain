---
type: concept
title: "var, let e const (JavaScript)"
aliases: ["var", "let", "const", "declaração de variável", "variáveis em JavaScript"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [javascript, variaveis, escopo, lang-dynamic]
skill: tech-mentor-frontend
status: stub
---

# var, let e const (JavaScript)

Três formas de declarar variável. `var` tem escopo de função e é içada (*hoisting*) com valor `undefined`. `let` tem escopo de bloco e não pode ser lida antes da declaração. `const` também tem escopo de bloco e impede reatribuição, mas não torna o valor imutável: um objeto em `const` aceita novas propriedades. Prática comum: `const` por padrão, `let` quando o valor precisa mudar, `var` nunca em código novo.

## Na NLW #1

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] define variável como "guardar em memória alguma coisa para usar mais tarde"; declarada sem valor, é `undefined`. Sobre as três: "com o JavaScript mais moderno, ao invés de a gente ficar usando var, a gente acaba usando aqui a palavra-chave let", "mas também poderia ser var, tanto faz"; ele usa muito `const` "porque eu quero fazer algumas coisas que não mudam o seu valor".

## Precisões

- Não é "tanto faz": a diferença de escopo muda o comportamento de laços e closures (o clássico `for (var i...)` com callbacks) `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let).
- `const` impede reatribuição, não mutação `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const).

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] explica por que `selectedItems` é `let`: "se eu deixasse ele como const, eu não ia conseguir sobrescrever esses valores. Porque const é uma constante. Let é uma variável." O dia 2 dizia "tanto faz". No dia 3 o `push` muda o array e o `filter` reatribui, e só a reatribuição exige `let`.

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], `const newFieldContainer` e `const fields`: "eu não gostaria que [...] fosse trocado"; "como uma variável pode ser constante?". `const` impede reatribuir o nome, não alterar o objeto, e é recriado a cada chamada da função.

## Key sources

- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: variável como memória; var, let e const "tanto faz" (impreciso)
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: let porque reatribui; const não impede push
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: const no cloneField
