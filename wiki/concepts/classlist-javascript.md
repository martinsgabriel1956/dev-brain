---
type: concept
title: "classList (JavaScript)"
aliases: ["classList", "classList.toggle", "classList.add", "classList.remove"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [javascript, dom, css, frontend]
skill: tech-mentor-frontend
status: stub
---

# classList (JavaScript)

`elemento.classList` é a lista de classes do elemento, com `add`, `remove`, `toggle` (tira a classe se tiver, põe se não tiver; devolve `true` ou `false`), `contains` e `replace`. É o jeito comum de o JavaScript mudar o visual: a regra fica no CSS, e o script só troca a classe. Ver [[wiki/concepts/dom]].

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa o `classList` duas vezes:
- **Itens de coleta:** `itemLi.classList.toggle("selected")`. "Ele olha lá o elemento [...] Existe a selected? [...] Então eu vou remover."
- **Modal:** `classList.remove("hide")` para abrir e `add("hide")` para fechar, "diferente só pra gente poder trabalhar com essas ideias".

Mayk pronuncia "togo" e soletra "t-o-g-g-l-e". Ver [[wiki/concepts/modal]].

## Key sources

- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: `toggle("selected")` nos itens; `add`/`remove("hide")` no modal
