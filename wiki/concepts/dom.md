---
type: concept
title: "DOM — Document Object Model"
aliases: ["Document Object Model"]
date_created: 2026-07-28
date_updated: 2026-11-17
source_count: 18
tags: [browser, dom, html-parsing, rendering-pipeline, frontend-frameworks]
skill: tech-mentor-frontend
status: draft
---
# DOM — Document Object Model

Árvore de nós que representa a estrutura do HTML: cada tag vira um nó, cada texto vira um nó, cada atributo fica acessível. É construída pelo parser de HTML em etapas: bytes → caracteres (decodificados via a codificação declarada, geralmente UTF-8) → tokens (tags de abertura/fechamento, atributos, texto) → nós → árvore, organizada pela hierarquia de abertura/fechamento das tags.

**Parsing incremental**: o parser não espera o documento inteiro chegar — constrói o DOM conforme os bytes chegam pela rede. É por isso que páginas grandes renderizam de cima para baixo.

**Tolerância a erros**: o parser de HTML nunca falha. Tags não fechadas são fechadas automaticamente; elementos mal aninhados (ex. `<div>` dentro de `<p>`) são reorganizados segundo o algoritmo de parsing do HTML5.

**Limitação**: o DOM sozinho não sabe aparência — cor, tamanho, posição. Isso vem do [[wiki/concepts/cssom]], que é combinado com o DOM para formar a [[wiki/concepts/render-tree]]. Ver o pipeline completo em [[wiki/concepts/critical-rendering-path]].

## Por que os frameworks de UI existem: o custo de tocar o DOM

Cada mutação de DOM tem custo real — o navegador pode precisar recalcular estilos, recalcular layout ([[wiki/concepts/reflow-layout]]) e repintar pixels. Uma mudança isolada é barata; várias em sequência descontrolada deixam o navegador lento. Essa é a motivação declarada por trás de praticamente todo mecanismo interno de React/Vue/Angular: [[wiki/concepts/virtual-dom]] e [[wiki/concepts/signals]] existem para decidir *o que* mudou sem recalcular tudo, [[wiki/concepts/reconciliacao]] decide *como* aplicar a mudança mínima necessária, e [[wiki/concepts/batching]] agrupa várias mudanças de estado numa única passada de DOM em vez de uma por mudança.

## Ver também

- [[wiki/concepts/virtual-dom]]
- [[wiki/concepts/reconciliacao]]
- [[wiki/concepts/hydration]] — como o DOM gerado no servidor é conectado a comportamento no cliente

## ID e classe como ganchos

Em [[wiki/sources/classes-e-ids-no-css]], classe e ID são "um gancho" para aplicar estilo e função, usados no CSS e no JavaScript. `[external]` `getElementById` devolve só o primeiro elemento com aquele ID; com IDs duplicados o script age no elemento errado sem erro, que é o "conflito" silencioso da aula: https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById.
## Seletores andam pela árvore

Os [[wiki/concepts/seletores-css|seletores CSS]] descendente (`div p`), filho (`div > p`) e adjacente (`ul + p`) são relações da árvore do DOM: ancestral, pai e irmão anterior ([[wiki/sources/seletores-e-pseudo-elements-css]]). `[external]` A aula ilustra o filho direto com um `<p>` dentro de outro `<p>`, mas o parser fecha o primeiro ao abrir o segundo e os dois viram irmãos: o DOM não é o HTML escrito.

## Na NLW #1, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] apresenta `document` como "um formato que a gente chama de objeto", com propriedades e funcionalidades (`write`). Usa `document.querySelector("select[name=uf]")` e `querySelectorAll("input")` (uma NodeList) com a sintaxe de seletor do CSS, e `innerHTML +=` para inserir options. `document.write` no console apaga a página inteira.

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] esbarra em um bug clássico: `querySelectorAll` devolve uma NodeList, e "não consigo colocar numa lista o add event listener [...] ele funciona num elemento". Também tira o `querySelector` de dentro da função, para não buscar o elemento "toda hora". Ver [[wiki/concepts/classlist-javascript]] e [[wiki/concepts/atributos-data-html]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]], o "View Page Source" mostra só a `div#root`, enquanto o inspetor mostra o `h1`: a DOM é "uma árvore de elementos em tempo real", montada pelo `react-dom`.

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], o primeiro contato com o DOM na NLW #2: `document` é "o objeto que eu tenho disponível para acessar a página"; `querySelector` devolve um elemento com `.style`; o DOM é uma árvore de nós ("Document Object Model"), por isso `cloneNode` e `appendChild`. Mayk separa a linguagem das APIs do navegador: essas funcionalidades não são "do JavaScript, é do JavaScript no browser".

## Na NLW #2, dia 1 (Diego Fernandes)

O `react-dom` é o renderizador que diz ao React que a interface "é com a DOM", "a árvore de elementos do HTML"; no React Native o alvo é a interface nativa. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

Em [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]], "DOM e os seus principais eventos" é um dos blocos do módulo de JavaScript do FrontPUSH: o JS "vai justamente manipular" HTML e CSS. O DOM é API da plataforma web, não parte do [[wiki/concepts/ecmascript]].

Em [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]], métodos de string e número são chamados de "API, porque é uma conversa entre o JavaScript e o browser". Esses vêm da linguagem; a API do navegador é o DOM (e `fetch`, `localStorage`). O `lastChild` que aparece na lista é propriedade de nó do DOM, não de string.

## No FrontPUSH, módulo de JavaScript, aula 08 (Násser)

Em [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]], o DOM é "uma interface que representa o HTML [...] por meio de objetos", a definição certa. Pelo painel Elements, a aula conclui que ele é "a árvore de conteúdo de tag de HTML e as propriedades CSS"; os estilos são do [[wiki/concepts/cssom]]. Também chama de "árvore" a cadeia `window.location...`, que é o BOM ([[wiki/concepts/window-e-bom]]). Na prática: `document.querySelector('h1')` com seletor de CSS, `innerText`, `classList` (um `DOMTokenList`) e `id`.

Em [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]], a parte 2 cria nós: `createElement('a')`, `setAttribute('href', ...)`, `createTextNode` + `appendChild` e o link anexado a `div#app` ([[wiki/concepts/criacao-de-elementos-dom]]).

Em [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]], a parte 3 liga eventos a mudanças no DOM: clique e tecla trocando classes da `.box` ([[wiki/concepts/propagacao-de-eventos-dom]]).

Em [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]], `document.documentElement` (o elemento `<html>`) recebe o listener de `mousemove` "para poder ele executar sem ser em cima de algum outro elemento, a própria página".

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
- [[wiki/sources/classes-e-ids-no-css]] — ID único como gancho do JavaScript; duplicado não dá erro
- [[wiki/sources/seletores-e-pseudo-elements-css]] — combinadores CSS como relações da árvore; `<p>` dentro de `<p>` vira irmão
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: document como objeto; querySelector; innerHTML
- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: classe e ID como etiquetas para o JavaScript "puxar e manipular esses elementos"
- [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]]: selecionar no CSS "é muito similar ou deveras igual" ao JavaScript (`querySelector`); pseudo-elements não estão no DOM
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: querySelectorAll x querySelector; cache do elemento
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: DOM em tempo real x HTML de origem
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: document, querySelector, cloneNode, appendChild
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: react-dom como renderizador
- [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]]: FrontPUSH, JavaScript aula 01: manipular HTML e CSS pelo DOM
- [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]: FrontPUSH, JavaScript aula 05: built-ins da linguagem × APIs do navegador
- [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]]: FrontPUSH, JavaScript aula 08: interface que representa o HTML por objetos; DOM × CSSOM × BOM
- [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]]: FrontPUSH, JavaScript aula 09: criar e anexar elementos
- [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]]: FrontPUSH, JavaScript aula 10: eventos que mudam o DOM
- [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]]: FrontPUSH, JavaScript aula 18: documentElement como alvo
- [[wiki/sources/frontpush-o-que-preciso-saber-de-javascript-antes-do-react]]: FrontPUSH, React aula 02: manipulação do DOM no checklist; o React substitui esse hábito imperativo
