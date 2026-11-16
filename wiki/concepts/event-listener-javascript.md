---
type: concept
title: "Event listener (addEventListener)"
aliases: ["addEventListener", "ouvidor de eventos", "event listener", "event.target", "evento change"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 7
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

Em [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]], `addEventListener` é descrito como "uma função dentro de outra função". É um método de `EventTarget` que recebe uma função (callback) como argumento.

Em [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]], o `addEventListener('click', fn)` é o exemplo de callback que prepara o `forEach`. A aula sugere `e` ("de evento") também como nome do item do array, onde `marca` seria mais claro.

Em [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]], eventos são clique, scroll, arrastar e tecla, e "cada evento desse pode ser adicionado a uma função" que modifica a árvore. A direção é a inversa: a função é registrada como listener do evento de um elemento. Todo elemento tem `addEventListener` porque herda de `EventTarget`.

## No FrontPUSH, módulo de JavaScript, aula 10 (Násser)

Em [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]], "tudo que você faz no seu browser é um evento". `addEventListener('click', callback)` com a função nomeada passada por referência ("se eu colocar assim [com parênteses] ela já vai executar"), o objeto `event` (`currentTarget`, `target`, `type`, o extinto `path`), a lista de eventos de mouse e teclado, `classList.toggle` no clique e `event.key` no `keydown`. `keydown` e `resize` não disparam na `div`: o primeiro pede foco, o segundo só existe no `window`. `keypress` está obsoleto; `mousemove` e `scroll` pedem throttle ([[wiki/concepts/propagacao-de-eventos-dom]]).

## Key sources

- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: change no select de UF, event.target, selectedIndex
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: click em lista; target x currentTarget; pointer-events
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: botão Novo horário
- [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]: FrontPUSH, JavaScript aula 05: addEventListener como "função dentro de função"
- [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]]: FrontPUSH, JavaScript aula 07: addEventListener como modelo de callback
- [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]]: FrontPUSH, JavaScript aula 08: eventos que modificam a árvore
- [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]]: FrontPUSH, JavaScript aula 10: click, event, target, keydown, resize no window
