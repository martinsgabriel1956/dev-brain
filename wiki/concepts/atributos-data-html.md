---
type: concept
title: "Atributos data-* (HTML) e dataset"
aliases: ["data-*", "data attributes", "dataset", "data-id"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [html, javascript, dom, frontend]
skill: tech-mentor-frontend
status: stub
---

# Atributos data-* (HTML) e dataset

Qualquer atributo `data-<nome>` é válido em qualquer elemento e serve para guardar dados da aplicação no próprio HTML. No JavaScript eles aparecem em `elemento.dataset`: `data-id` vira `dataset.id`, e `data-user-name` vira `dataset.userName` (camelCase). O valor é sempre string. No CSS, dá para selecionar com `[data-id="3"]`. `[external]` (https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes)

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] marca cada item de coleta com `data-id="1"` a `"6"`:
- **Por que não `id`:** "não é muito legal a gente deixar números" num `id`. O HTML5 até aceita `id="1"`, mas o seletor CSS precisaria de escape.
- **Leitura:** o clique lê `event.target.dataset.id` ("o s é menorzinho").
- **Uso:** esse valor alimenta o array `selectedItems`. Ver [[wiki/concepts/classlist-javascript]] e [[wiki/concepts/array]].

## Key sources

- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: `data-id` nos itens de coleta, lido com `dataset.id`
