---
type: concept
title: "Event listener (addEventListener)"
aliases: ["addEventListener", "ouvidor de eventos", "event listener", "event.target", "evento change"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [javascript, dom, eventos, frontend]
skill: tech-mentor-frontend
status: stub
---

# Event listener (addEventListener)

`elemento.addEventListener(tipo, função)` registra uma função que o navegador chama quando o evento acontece no elemento (ou num filho, por *bubbling*). A função recebe um objeto `Event`; `event.target` é o elemento que disparou. Ver [[wiki/concepts/dom]].

## Na NLW #1

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] chama de "ouvidor de eventos", que fica "com o ouvidão ligado". No select de UF ouve `change`; para testar, precisa de uma segunda `option`, porque sem opções não há mudança. A função `getCities` é passada por referência e recebe o evento: `event.target` é o select e `event.target.value` é o id do estado, que entra na URL de municípios do [[wiki/entities/ibge]]. `event.target.options[event.target.selectedIndex].text` dá o nome do estado selecionado.

## Precisões

- Num `select`, `change` dispara quando a seleção muda; `input` dispara a cada alteração em campos de texto `[external]` (https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event).

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa `querySelectorAll` + `for...of` para registrar `click` nos seis itens de coleta. Mostra que `event.target` pode ser a `img` ou o `span` filho. A correção é no CSS, com `pointer-events: none` nos filhos. `[external]` `event.currentTarget` (ou `closest('li')`) resolveria no próprio JavaScript (https://developer.mozilla.org/en-US/docs/Web/API/Event/currentTarget). No modal, usa funções anônimas no `click` do botão e do "Fechar".

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], `document.querySelector('#addTime').addEventListener('click', cloneField)`: o JavaScript na página "é muito voltado à ideia de eventos", e o listener é "um ouvidor de eventos". O botão precisou de `type="button"` para o clique não enviar o formulário.

## Key sources

- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: change no select de UF, event.target, selectedIndex
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: click em lista; target x currentTarget; pointer-events
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: botão Novo horário
