---
type: concept
title: "Criar e inserir elementos no DOM (createElement, appendChild, append)"
aliases: ["createElement", "createTextNode", "appendChild", "append", "setAttribute", "textContent", "DocumentFragment", "remove", "criar elementos com JavaScript"]
date_created: 2026-11-16
date_updated: 2026-11-17
source_count: 3
tags: [javascript, dom, createelement, appendchild, setattribute, textcontent, xss]
skill: lang-dynamic
status: stub
---

# Criar e inserir elementos no DOM

APIs do [[wiki/concepts/dom]] para montar HTML pelo JavaScript. `[external]` https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement

```js
const link = document.createElement('a')       // nasce sem atributos
link.href = 'https://frontpush.com.br'         // ou link.setAttribute('href', ...)
link.textContent = 'acessar o FrontPUSH'        // ou link.appendChild(document.createTextNode(...))
document.querySelector('#app').append(link)     // ou appendChild(link)
```

## Peças

- `document.createElement(tag)`: cria o elemento, ainda fora da página.
- `setAttribute(nome, valor)` / propriedades (`el.href`, `el.id`, `el.className`); `classList` para classes ([[wiki/concepts/classlist-javascript]]).
- `textContent` para texto (seguro); `createTextNode` é a forma longa.
- `pai.appendChild(filho)` (um nó, devolve o filho); `pai.append(...nós ou strings)`; `prepend`, `before`, `after`, `insertAdjacentElement`.
- `el.remove()` e `pai.replaceChildren(...)` para tirar ou trocar.
- `DocumentFragment` (ou montar tudo antes de anexar) para inserir muitos nós com um só recálculo de layout ([[wiki/concepts/reflow-layout]]).

## innerHTML

`el.innerHTML = '<a href="...">x</a>'` é mais curto, mas interpreta o texto como HTML: com dados do usuário, abre [[wiki/concepts/xss]]. Use `createElement` + `textContent` para conteúdo de fora; se precisar de HTML, sanitize antes.

## Relação com frameworks

React, Vue e afins usam essas mesmas APIs por baixo, mas decidem o que mudar comparando árvores ([[wiki/concepts/virtual-dom]]) e montam tudo dentro de um nó raiz (`#root` no create-react-app, `#app` no Vue) ([[wiki/concepts/single-page-application]]).

## No FrontPUSH

Em [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]], [[wiki/entities/nasser|Násser]] cria um `<a>` com `createElement`, põe o `href` com `setAttribute`, o texto com `createTextNode` + `appendChild` e anexa o link pronto a `div#app`, "assim como é feito na framework".

## Key sources

- [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]]: FrontPUSH, JavaScript aula 09: createElement, setAttribute, createTextNode, appendChild
- [[wiki/sources/frontpush-conceitos-gerais-react-interface-dinamica-spa-virtual-dom-jsx]]: FrontPUSH, React aula 03: "Tudo é o JS que faz", com createElement e .style como ponte para o React
- [[wiki/sources/frontpush-jsx-webpack-babel-react-createelement-create-react-app]]: FrontPUSH, React aula 06: React.createElement × document.createElement
