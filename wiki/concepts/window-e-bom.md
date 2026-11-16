---
type: concept
title: "window e BOM (Browser Object Model)"
aliases: ["window", "BOM", "Browser Object Model", "objeto global do navegador", "location", "globalThis"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [javascript, navegador, window, bom, location, dom, web-apis]
skill: lang-dynamic
status: stub
---

# window e BOM (Browser Object Model)

No navegador, `window` é o objeto global: as variáveis globais e as APIs do ambiente ficam nele. "BOM" é o nome informal do conjunto de objetos do navegador fora do documento. `[external]` https://developer.mozilla.org/en-US/docs/Web/API/Window

## O que fica em window

- `window.document`: o [[wiki/concepts/dom]], a árvore do documento.
- `window.location`: a URL atual (`href`, `pathname`, `search`, `hash`) e navegação (`assign`, `reload`).
- `window.history`, `window.navigator`, `window.screen`.
- `localStorage`, `sessionStorage`, `fetch`, `setTimeout`, `console`.
- Eventos da janela: `resize`, `scroll`, `load`.

`window.document.querySelector` e `document.querySelector` são a mesma coisa, porque o global dispensa o prefixo.

## DOM × BOM × linguagem

| Camada | Exemplos | Onde existe |
|---|---|---|
| Linguagem ([[wiki/concepts/ecmascript]]) | `Array`, `String`, `Math`, `JSON` | navegador e Node |
| DOM | `document`, `Element`, `querySelector`, `classList` | navegador |
| BOM / Web APIs | `window`, `location`, `history`, `localStorage` | navegador |

No Node não há `window` nem `document`; o objeto global é `global`, e `globalThis` (ES2020) funciona nos dois ([[wiki/entities/nodejs]]).

O DOM é árvore porque seus nós têm pai e filhos. `window.location.href` é só acesso encadeado a propriedades, não um caminho na árvore.

## No FrontPUSH

Em [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]], [[wiki/entities/nasser|Násser]] põe `window` como "a árvore maior, que engloba tudo", com `location` (URL, que ele chama de metadados) e `document` dentro. A hierarquia de objetos está certa; chamar isso de "árvore DOM" mistura o BOM com o documento.

Em [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]], `resize` e `keydown` só funcionam no `window`: "quando não tem nada, ele está referenciando o objeto principal e maior de todos, que é o window" (o `addEventListener` sem prefixo é `window.addEventListener`).

## Key sources

- [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]]: FrontPUSH, JavaScript aula 08: window, location e document
- [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]]: FrontPUSH, JavaScript aula 10: resize e keydown no window
