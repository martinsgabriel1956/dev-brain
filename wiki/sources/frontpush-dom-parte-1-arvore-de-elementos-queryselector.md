---
type: source
title: "Árvore DOM de elementos, parte 1: o que é o DOM e o que dá para fazer com ele (FrontPUSH)"
aliases: ["FrontPUSH DOM parte 1", "módulo de JavaScript ES6, aula 08", "DOM pt.1", "árvore DOM de elementos"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, dom, bom, window, document, eventos, queryselector, innertext, classlist, devtools, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-dom-parte-1-arvore-de-elementos-queryselector.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Árvore DOM de elementos, parte 1 (FrontPUSH)

## TL;DR

Aula 08 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] ("Nácio" na legenda). Introdução ao [[wiki/concepts/dom|DOM]]: o que é, o que dá para fazer e como pesquisar; o detalhe fica para as próximas aulas. A "manipulação DOM de elementos" é a que ele já usou no projeto do [[wiki/entities/nubank]].

- **Sigla:** Document Object Model, "modelo de objeto de documento".
- **Painel Elements:** mostra a árvore HTML, os estilos e o layout; daí ele conclui que o DOM "nada mais é do que a árvore de conteúdo de tag de HTML e as propriedades CSS".
- **Definição escrita:** "uma interface que representa o HTML [...] por meio de objetos", e esses objetos herdam propriedades e métodos ([[wiki/concepts/objetos-javascript]]).
- **Manipular:** criar e retirar tags, atributos e classes, mudar conteúdo e estilo, "vincular esse gerenciamento por meio de eventos" (clique, scroll, arrastar, tecla). Ver [[wiki/concepts/event-listener-javascript]].
- **Por que "árvore":** "objetos dentro de objetos": `window` engloba tudo, com `location` (URL) e `document`; dentro deste, `html`, `head` (`meta`, `title`) e `body`. Ver [[wiki/concepts/window-e-bom]].
- **Como estudar:** pesquisar "de forma leiga" no Google e no Stack Overflow ("como fazer para clicar em um título e mudar a cor JavaScript"); `document.` no console lista "uma infinidade de coisas".
- **Na prática:** `document.querySelector('h1')` usa o seletor do CSS ([[wiki/concepts/seletores-css]]); `.innerText` dá o texto, `.classList` devolve um `DOMTokenList` "like array" ([[wiki/concepts/classlist-javascript]]), e `.id` sem id dá string vazia.

## Key Claims

### O que é

- "O D vem de document, o O de object e o M de model, ou seja, se fosse traduzir modelo de objeto de documento."
- No painel Elements, "apareceu a árvore HTML, o conteúdo em HTML, apareceu os estilos dos elementos, apareceu os layouts, ou seja, a gente consegue deduzir disso aqui que a árvore DOM de elementos nada mais é do que a árvore de conteúdo de tag de HTML e as propriedades CSS."
- "É uma interface que representa o HTML, mas por meio de objetos [...] por isso que é documento object model." "Quando a gente instancia um objeto, automaticamente ele é filho de algum outro objeto que ele herda propriedades e métodos."

### O que dá para fazer

- "Criar uma nova tag, eu retirar uma tag, eu adicionar uma nova propriedade, um novo atributo, adicionar uma nova classe, retirar uma nova classe, vincular esse gerenciamento por meio de eventos."
- "Um clique é um evento, um scroll na página é um evento, um clicar e arrastar é um evento, pressionar uma tecla do nosso teclado é um evento e cada evento desse pode ser adicionado a uma função que [...] faz algum tipo de modificação nessa árvore."
- Exemplo: clicar no `h1` "JS ES6+" e adicionar uma classe que muda a cor ou põe borda. "Eu consigo manipular o HTML e o CSS, da minha árvore inteira por meio do JavaScript."
- Manipular a estrutura (onde e com quais atributos uma tag é criada), o conteúdo (um link novo com texto) e o estilo (um botão que muda cor, layout ou borda).

### Como estudar

- "Literalmente pesquisando, mesmo que de forma leiga no Google [...] 'como fazer para clicar em um título e mudar a cor, JavaScript' [...] você já vai estar pesquisando sobre a árvore DOM de elementos." Também o Stack Overflow, "porque são muitos".
- `document.` no console: "olha só o tanto de propriedades e métodos que existem nele, e eu nem sei se está listando todos."

### Por que árvore

- "É porque literalmente eu tenho objetos dentro de objetos [...] window, ponto alguma coisa, ponto alguma coisa [...] esse aqui é um atributo, dentro desse atributo [...] pode ter outra propriedade que tem outra propriedade que é o método que eu quero."
- "A árvore maior, que engloba tudo, que é a window, dentro da window eu tenho um outro objeto maior chamado location, onde ele traz informações de URL, que é mais se diz respeito aos metadados [...] temos também a document, que é a que a gente mais vai estar verificando."
- `document` → `html` → `head` (meta, title, "os metadados da minha página") e `body` ("engloba todas as tags que a gente conhece": h1, p, span, listas, button, formulário).

### querySelector e propriedades

- "Selector vem de seletor, que é o seletor do CSS, então como eu disse que para você estudar JavaScript é melhor [...] estudar CSS primeiro." `h1`, `.classe`, `#id`, atributo como `alt`: "é a mesma seleção que a gente faz no CSS".
- "Como isso aqui virou um objeto, ele tem propriedades e métodos atreladas a ele." `innerText` "revela qual é o conteúdo que está dentro dessa tag".
- `classList` "vai listar em formato de likeArray, porque não é exatamente um array [...] ele vai devolver um DOMTokenList". Com `class="titulo titulo-maior"`, `classList[0]` é `titulo` e `[1]` é `titulo-maior`.
- `id`: "como não tem nenhum ID, ele está voltando vazio".

## Entities

- [[wiki/entities/nasser]]: instrutor ("Nácio" na legenda).
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6.
- [[wiki/entities/javascript]]: assunto da aula.
- [[wiki/entities/nubank]]: projeto do curso onde a manipulação do DOM já apareceu.
- [[wiki/entities/google]]: onde pesquisar "de forma leiga".

## Concepts

- [[wiki/concepts/dom]]
- [[wiki/concepts/window-e-bom]] (criado neste ingest)
- [[wiki/concepts/cssom]]
- [[wiki/concepts/event-listener-javascript]]
- [[wiki/concepts/seletores-css]]
- [[wiki/concepts/classlist-javascript]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/head-html-metadados]]
- [[wiki/concepts/html-hipertexto]]

## Precisões e tensões com a wiki

`⚠️` Sem arquivo de referência na skill lang-dynamic para DOM e BOM; as precisões vêm do MDN (`[external]`) e das páginas de renderização da wiki.

- **O DOM não inclui "as propriedades CSS".** `[external]` O DOM é a árvore de nós do documento; os estilos vivem no [[wiki/concepts/cssom]], e o navegador combina os dois na render tree ([[wiki/concepts/critical-rendering-path]]). O painel Elements mostra os dois lado a lado (a árvore e o painel Styles/Computed), o que explica a conclusão da aula. O JavaScript mexe no estilo por `element.style` e `classList`, que estão no DOM, mas o modelo dos estilos é o CSSOM.
- **A "árvore" é a do documento, não `window.x.y.z`.** `[external]` O DOM é árvore porque cada nó tem pai e filhos (`html` → `body` → `h1` → texto). `window.location.href` é acesso encadeado a propriedades de objetos do navegador, o BOM; `window` não é nó do DOM, e `document` é uma propriedade dele ([[wiki/concepts/window-e-bom]]). A aula junta as duas ideias.
- **`location` não é "metadados".** É a URL da página atual (`href`, `pathname`, `search`) e permite navegar (`location.assign`). Os metadados ficam nas `meta` do `head` ([[wiki/concepts/head-html-metadados]]).
- **"Filho de outro objeto" é literal aqui.** `[external]` Um `h1` é `HTMLHeadingElement`, que herda de `HTMLElement` → `Element` → `Node` → `EventTarget`; é por isso que todo elemento tem `addEventListener`.
- **`querySelector` devolve o primeiro e só o primeiro.** `[external]` Sem resultado, devolve `null` ([[wiki/concepts/null-e-undefined]]); para todos, `querySelectorAll` (um `NodeList`).
- **`innerText` × `textContent`.** `innerText` devolve o texto como renderizado (respeita `display: none`, provoca cálculo de layout); `textContent` devolve o texto cru, mais barato. Para escrever texto, os dois evitam o risco de `innerHTML` com dados de fora.
- **`DOMTokenList` não tem `map`.** Tem `length`, índice, `forEach`, `add`, `remove`, `toggle` e `contains`; para os outros métodos de array, `Array.from(el.classList)` ([[wiki/concepts/metodos-de-array-javascript]]).
- **"Cada evento [...] pode ser adicionado a uma função"** está invertido: a função (listener) é registrada no evento de um elemento ([[wiki/concepts/event-listener-javascript]]).
- **Pesquisa:** além do Google e do Stack Overflow, a [[wiki/entities/mdn-web-docs|MDN]] é a referência das APIs do DOM, e a conclusão do módulo de CSS do curso já a recomendava.

## Open Questions

- "Documento object model": ele disse "documento" ou a legenda trocou "document"? Ficou literal.
- Há 3 s sem legenda (00:06:32–00:06:35) antes de repetir a definição.

## Raw quotes

- "é uma interface que representa o HTML por meio de objetos"
- "literalmente é um mundo de coisas que dá para fazer"
- "selector vem de seletor, que é o seletor do CSS"
