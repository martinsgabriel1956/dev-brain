---
type: concept
title: "Propagação de eventos no DOM (bubbling, target × currentTarget, delegação)"
aliases: ["event bubbling", "bubbling", "capturing", "captura", "target", "currentTarget", "delegação de eventos", "event delegation", "stopPropagation", "preventDefault", "composedPath"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [javascript, dom, eventos, bubbling, delegacao, target, currenttarget]
skill: lang-dynamic
status: stub
---

# Propagação de eventos no DOM

Um evento atravessa a árvore em três fases: **captura** (do `window` até o alvo), **alvo** e **bubbling** (do alvo de volta até o `window`). Por padrão, os listeners rodam no bubbling. `[external]` https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Event_bubbling

## target × currentTarget

```html
<div class="box"><h1>Título</h1></div>
```

```js
box.addEventListener('click', (event) => {
  event.target        // onde o clique aconteceu: o <h1>
  event.currentTarget // quem está escutando: a .box
})
```

Clicando no `h1`, o evento sobe até a `.box` e dispara o listener dela. Numa `function`, `this` é o `currentTarget`; numa arrow, não ([[wiki/concepts/arrow-functions]]).

## Delegação

Um listener no pai atende todos os filhos, inclusive os que entram depois:

```js
lista.addEventListener('click', (e) => {
  const item = e.target.closest('li')
  if (item) item.classList.toggle('feito')
})
```

Menos listeners e nada a religar quando a lista muda ([[wiki/concepts/criacao-de-elementos-dom]]).

## Controle

- `event.stopPropagation()`: para de subir.
- `event.preventDefault()`: cancela a ação padrão (seguir o link, enviar o formulário), não a propagação.
- `addEventListener(tipo, fn, { capture: true })` escuta na captura; `{ once: true }` roda uma vez; `{ passive: true }` promete não chamar `preventDefault` (rolagem mais fluida).
- `event.composedPath()` devolve o caminho; `event.path` era só do Chrome e foi removido.
- Nem todo evento sobe: `focus`, `blur`, `mouseenter` e `mouseleave` não fazem bubbling (`focusin`, `focusout`, `mouseover` e `mouseout` fazem).

Relacionado: [[wiki/concepts/event-listener-javascript]], [[wiki/concepts/dom]].

## No FrontPUSH

Em [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]], [[wiki/entities/nasser|Násser]] põe o listener numa `.box` com `h1` e `h3` dentro: `currentTarget` "está sempre retornando a caixa", e `target` "vai nos filhos". Ele não dá nome ao mecanismo; é o bubbling. Também mostra o `event.path`, hoje removido.

Em [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]], o `mousemove` é escutado no `document.documentElement`; como o evento sobe por bubbling, `document` ou `window` também receberiam o movimento em qualquer ponto da página.

## Key sources

- [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]]: FrontPUSH, JavaScript aula 10: target × currentTarget numa .box com filhos
- [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]]: FrontPUSH, JavaScript aula 18: mousemove no documentElement
