---
type: source
title: "Árvore DOM de elementos, parte 3: eventos com addEventListener (FrontPUSH)"
aliases: ["FrontPUSH DOM parte 3", "módulo de JavaScript ES6, aula 10", "DOM pt.3", "eventos no DOM"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, dom, eventos, addeventlistener, callback, target, currenttarget, bubbling, classlist, toggle, keydown, resize, window, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Árvore DOM de elementos, parte 3: eventos (FrontPUSH)

## TL;DR

Aula 10 do módulo de JavaScript ES6+ do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] ("Anás" na legenda). Fecha a parte de elementos com eventos, "talvez [...] a parte mais legal" e "a aula mais importante" do DOM. Ver [[wiki/concepts/event-listener-javascript]].

- **Tudo é evento:** a página é "como se fosse um plano cartesiano"; o navegador detecta posição do mouse, entrar e sair de elementos, botão esquerdo ou direito, tecla, scroll e velocidade, e "tudo simplesmente dá para taguear".
- **Clique:** `h1.addEventListener('click', function () { console.log('o usuário clicou no título') })`, depois em arrow de uma linha ([[wiki/concepts/arrow-functions]]).
- **Boa prática:** função separada passada por referência (`addEventListener('click', callback)`, sem parênteses), "mais organizado e mais fácil de debugar" ([[wiki/concepts/callback-javascript]]).
- **Objeto `event`:** `currentTarget` é sempre o elemento que escuta (a `.box`); `target` é onde o clique aconteceu (o `h1` ou o `h3` dentro dela). Também `type` e `path`. Ver [[wiki/concepts/propagacao-de-eventos-dom]].
- **Lista de eventos:** mouse (`click`, `dblclick`, `mousedown`, `mouseenter`, `mouseleave`, `mousemove`, `mouseover`, `mouseout`, `mouseup`), teclado (`keydown`, `keypress`), `scroll` e `resize`. O `mousemove` dispara "1 milhão de eventos".
- **Interatividade:** `box.classList.toggle('red')` (ou `this.classList`) com `transition: 1s ease`, o mesmo truque dos menus hambúrguer ([[wiki/concepts/classlist-javascript]]).
- **Teclado:** `keydown` e `resize` não disparam na `.box`; no `window` sim. `event.key === 'r'` → red, `'b'` → blue, outra tecla → green, num `if / else if / else`.
- **Método:** "sempre coloca no console" o `event` para ver as propriedades daquele tipo de evento, e pesquise.

## Key Claims

### Eventos

- "Tudo que você faz no seu browser é um evento, o simplesmente arrastar do mouse é um evento, pensa que essa página web é como se fosse um plano cartesiano, onde tem a variação em X e a variação em Y."
- O navegador sabe "qual é o elemento que eu estou passando o mouse, se eu entrei dentro do elemento, se eu saí [...] se eu cliquei com o botão esquerdo ou se foi com o direito, se eu pressionei alguma tecla [...] se eu fiz scroll para cima, para baixo, em qual velocidade".
- "A gente pode vincular todo e qualquer tipo de evento desse [...] a algum tipo de função para poder fazer alguma coisa."

### Clique, arrow e callback por referência

- "No primeiro argumento você vai colocar o evento que no caso é o evento de clique [...] e aqui a gente pode colocar uma função." Clicar fora do `h1` não dispara nada.
- Arrow: "eu apago isso aqui e coloco um sinal de igual setinha e de maior"; com uma linha, sem chaves.
- "É interessante a gente adicionar as funções separadas, ou seja, não no corpo do argumento, mas sim literalmente construindo uma função de callback."
- "Nesse caso eu não quero que ela execute, porque se eu colocar assim [com parênteses] ela já vai executar [...] eu quero simplesmente deixar o nome da função como referência e aí quando clica, ele busca o nome da função [...] e executa." "Mais fácil de debugar."

### O objeto event

- "Dentro dessa função, ela tem o event, que é literalmente as informações do evento [...] você vai ver em muitos exemplos [...] só a letrinha e, mas eu gosto de deixar event para poder deixar claro que é um evento."
- `currentTarget`: "o target vem de alvo, o alvo atual". Com o listener na `.box` (padding 36 px, fundo `#101010`), "ele está sempre retornando a caixa [...] o próprio que eu estou utilizando para poder escutar o evento".
- `target`: "ele vai nos filhos [...] clicar no h1, ele me voltou o h1, posso clicar no h3, ele me voltou o h3".
- `type` é "de clique"; `path` devolve "meio que o array de informações, todo o caminho [...] no body, no div box".

### Tipos de evento

- Pesquisando "events javascript" no Google, num site que ele "sempre" visita: "os mais típicos são os eventos de tela, os eventos de teclado e os eventos do próprio mouse".
- "O mouse move [...] vai literalmente disparar 1 milhão de eventos [...] para cada micro levadinha que eu passo."
- Teclado: "key down, key press, quando alguma tecla for pressionada"; e `scroll`.

### classList.toggle e this

- "Na maioria grandiosa das vezes, quando a gente faz algum evento de callback, a gente quer adicionar alguma classe."
- "Fazer o toggle, que é o que eu faço demais quando eu desenho, por exemplo, os hambúrgueres, os menus hambúrgueres." `.red { background-color: red; transition: 1s ease }`: "quando eu clico, ele troca, quando eu clico, ele destroca".
- "Eu vou colocar, por exemplo, this, que eu estou referenciando o próprio evento"; depois: "o this referencia o próprio elemento [...] o próprio box".

### keydown, resize e window

- "Sempre quando você tiver dúvidas do que é o evento, você dá um console.log do evento [...] dependendo do evento que você selecionar, ele apresenta propriedades diferentes."
- `keydown` e `resize` na `.box` não respondem: "ele estava disparando somente quando tinha o resize do elemento box, por isso que o keydown e o resize não estavam funcionando". No "window, lembrando que aqui, quando não tem nada, ele está referenciando o objeto principal e maior de todos" ([[wiki/concepts/window-e-bom]]).
- `event.key` mostra a tecla ("do tipo A"). `if (event.key === 'r')` → `toggle('red')`; `else if` `'b'` → `blue`; senão `green`.
- "Peguem a ideia do objeto, sempre coloca no console para você ver quais são as propriedades do evento [...] fazer a verificação, colocar a lista encadeada, e aí, só a sua criatividade que vai te limitar."

## Entities

- [[wiki/entities/nasser]]: instrutor ("Anás" na legenda).
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6+.
- [[wiki/entities/javascript]]: assunto da aula.
- [[wiki/entities/google]]: onde ele pesquisa a lista de eventos.

## Concepts

- [[wiki/concepts/event-listener-javascript]]
- [[wiki/concepts/propagacao-de-eventos-dom]] (criado neste ingest)
- [[wiki/concepts/callback-javascript]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/arrow-functions]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/classlist-javascript]]
- [[wiki/concepts/window-e-bom]]
- [[wiki/concepts/estruturas-condicionais-javascript]]
- [[wiki/concepts/transition-e-transform-css]]
- [[wiki/concepts/acessibilidade]]
- [[wiki/concepts/dom]]

## Precisões e tensões com a wiki

`⚠️` Sem arquivo de referência na skill lang-dynamic para eventos do DOM; as precisões vêm do MDN (`[external]`).

- **O que liga `target` e `currentTarget` é o *bubbling*, que a aula não nomeia.** `[external]` O clique nasce no `h1` (o `target`) e sobe pelos ancestrais; o listener da `.box` roda quando o evento passa por ela, e nesse momento `currentTarget` é a `.box` (https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Event_bubbling). É a base da **delegação de eventos**: um listener no pai atende todos os filhos, inclusive os criados depois ([[wiki/concepts/propagacao-de-eventos-dom]]).
- **`event.path` não existe mais.** `[external]` Era propriedade não padronizada do Chrome, removida no Chrome 109 (2023). O padrão é `event.composedPath()`.
- **`this` no listener é o elemento, não "o próprio evento".** Numa `function`, `this` é o `currentTarget` (a aula se corrige depois). Numa arrow, `this` é o de fora, e `this.classList` quebraria; a diferença que a [[wiki/concepts/arrow-functions|aula 04]] não mostrou aparece aqui. Mais claro: `event.currentTarget.classList`.
- **Por que `keydown` e `resize` não disparam na `.box`.** `[external]` `keydown` vai para o elemento com foco, e uma `div` não recebe foco sem `tabindex`. `resize` só dispara no `window`; para medir um elemento, `ResizeObserver`. "Ele só ativa com o resize do elemento" não é o motivo.
- **`keypress` está obsoleto.** Use `keydown` (ou `keyup`). `event.key` é o caractere (`'a'`, `'A'` com Shift); `event.code` é a tecla física (`'KeyA'`). Comparar com `'R'` maiúsculo falha sem Shift.
- **`toggle` de várias classes acumula.** Apertar R e depois B deixa `red` e `blue` juntas, e vence a que vem depois no CSS. Para trocar de cor, remover as outras ou usar `classList.replace`.
- **"1 milhão de eventos" é força de expressão**, mas o problema é real: `mousemove` e `scroll` disparam dezenas de vezes por segundo. Trabalho pesado no handler pede *throttle*, `requestAnimationFrame` ou listener `{ passive: true }` ([[wiki/concepts/event-loop-performance-js]]).
- **Clique em `div` não é acessível pelo teclado.** O exemplo vale para mostrar eventos; numa interface real, a ação vai num `<button>`, que recebe foco e responde a Enter e Espaço ([[wiki/concepts/acessibilidade]]).
- **Função nomeada também permite remover o listener:** `removeEventListener('click', callback)` só funciona com a mesma referência. Um nome descritivo (`alternarCor`) ajuda mais que `callback`.
- **"Colocar a lista encadeada"** é a "estrutura encadeada" (`if / else if / else`) da [[wiki/concepts/estruturas-condicionais-javascript|aula 03]]; lista encadeada é outra estrutura de dados.
- **Positivos:** referência × execução no `addEventListener`, `event` com nome claro, `console.log(event)` como método de descoberta, `toggle` + `transition` como padrão de interface.

## Open Questions

- Qual é o site de eventos que ele "sempre" visita (link roxo)? W3Schools ou MDN; a legenda não diz.
- A comparação foi com `'r'` ou `'R'`? A legenda só diz "digitar R".
- Há 3 s sem legenda (00:13:35–00:13:38) depois do "ele destroca".

## Raw quotes

- "tudo que você faz no seu browser é um evento"
- "eu quero simplesmente deixar o nome da função como referência"
- "só a sua criatividade que vai te limitar"
