---
type: concept
title: "Seletores CSS (universal, tipo, classe, ID)"
aliases: ["seletor CSS", "seletores", "classe e ID", "class e id", "seletor de classe", "seletor de ID", "seletor universal"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [css, html, seletores, classe, id, frontend]
skill: tech-mentor-frontend
status: stub
---

# Seletores CSS (universal, tipo, classe, ID)

Parte de uma regra [[wiki/concepts/css]] que diz **a quais elementos** as declarações se aplicam. Os quatro básicos:

| Seletor | Sintaxe | Alcança | Exemplo da aula |
|---|---|---|---|
| Universal | `*` | todo elemento | reset de margin, padding e `box-sizing: border-box` |
| Tipo (tag) | `h1`, `a`, `p` | toda tag daquele tipo | h1 branco, parágrafo `#333` |
| Classe | `.btn` | todo elemento com `class="btn"` | botões primário e secundário |
| ID | `#btn-checkout` | o elemento com `id="btn-checkout"` (único) | botão de checkout maior e azul |

## Classe x ID

Em [[wiki/sources/classes-e-ids-no-css]], [[wiki/entities/nasser|Násser]] define os dois como "ganchos" usados no CSS e no JavaScript ([[wiki/concepts/dom]]), que "funcionam de uma mesma forma" e diferem na semântica:

- **ID** identifica um elemento só, "como se fosse o seu CPF". Repetir "vai dar conflito", mas o navegador não avisa.
- **Classe** vale para vários elementos: crie uma quando o estilo se repete. Um elemento pode ter várias, separadas por espaço (`class="btn btn-primary"`).

`[external]` `class` e `id` são atributos globais do HTML (a aula diz "tags"). `class` é uma lista separada por espaços e sensível a maiúsculas; `id` precisa ser único no documento: https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id.

## Por que preferir classe para estilo

O ID tem [[wiki/concepts/especificidade-css|especificidade]] alta: uma regra por ID vence qualquer número de classes. `[skill: tech-mentor-frontend]` Convenções como BEM (`.card__title--truncated`) e ITCSS estilizam só por classe e deixam o ID para âncoras, `label for` e JavaScript. A ordem da aula (reset `*` → tags → classes) é a mesma das camadas Generic → Elements → Components do ITCSS.

## Key Sources

- [[wiki/sources/classes-e-ids-no-css]]: classe x ID (CPF), `#` e `.`, reset universal, estilos por tag, `.btn` com variações, ID de checkout
