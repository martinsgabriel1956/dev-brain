---
type: concept
title: "Igualdade em JavaScript (== x ===)"
aliases: ["==", "===", "igualdade estrita", "igualdade abstrata", "comparação em JavaScript"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [javascript, tipos, coercao, lang-dynamic]
skill: tech-mentor-frontend
status: stub
---

# Igualdade em JavaScript (== x ===)

`=` atribui; `==` e `===` comparam. A diferença:
- **`===` (estrita)** só dá `true` com o mesmo tipo e o mesmo valor.
- **`==` (abstrata)** converte os tipos antes de comparar: `"1" == 1`, `0 == ""` e `null == undefined` dão `true`.

`!=` e `!==` seguem a mesma regra. Prática comum: `===` sempre, `==` só quando a conversão é intencional (o caso clássico é `x == null`). `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness)

Ver [[wiki/concepts/tipos-primitivos-javascript]], onde está a coerção de `"1" + 12` do dia 2.

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] explica que "o igual assim ele é para atribuir valor. Dois iguais é para comparar valor". Sobre o terceiro igual: "há uma diferença entre dois iguais para três iguais que não nos cabe entender agora [...] Posso colocar só dois ou três tanto faz". Ele usa `==` e `!=` no `findIndex` e no `filter`. O código funciona porque os dois lados são strings vindas de `dataset.id`. Mas não é "tanto faz", pelo mesmo motivo do "tanto faz" de [[wiki/concepts/var-let-const]] no dia 2.

## Key sources

- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: `==` e `!=` em findIndex/filter; "tanto faz" (impreciso)
