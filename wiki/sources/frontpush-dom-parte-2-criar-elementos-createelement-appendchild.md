---
type: source
title: "Árvore DOM de elementos, parte 2: criando elementos com JavaScript (FrontPUSH)"
aliases: ["FrontPUSH DOM parte 2", "módulo de JavaScript ES6, aula 09", "DOM pt.2", "createElement e appendChild"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, dom, createelement, createtextnode, appendchild, setattribute, spa, react, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-dom-parte-2-criar-elementos-createelement-appendchild.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Árvore DOM de elementos, parte 2: criando elementos (FrontPUSH)

## TL;DR

Aula 09 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] (autoria pela sequência do módulo). Aula curta (6 min): criar HTML só com JavaScript, "um dos princípios" dos frameworks, que montam a página em [[wiki/concepts/single-page-application|SPA]].

- **Motivação:** "quando a gente abre o React, você vai ver que é tudo JavaScript, é o próprio JavaScript que renderiza o HTML, é o próprio JavaScript que renderiza o CSS". Ver [[wiki/entities/react]].
- **Passo a passo** ([[wiki/concepts/criacao-de-elementos-dom]]):
  1. `const link = document.createElement('a')`.
  2. `link.setAttribute('href', 'https://frontpush.com.br')`.
  3. `const conteudo = document.createTextNode('acessar o FrontPUSH')` e `link.appendChild(conteudo)`. "Child vem de filho."
  4. `<div id="app">` no HTML, "assim como é feito na framework"; `const container = document.querySelector('#app')` e `container.appendChild(link)`.
- **Resultado:** o link aparece dentro de `div#app` no inspetor, e o clique abre o site do curso.
- **Próximas aulas:** modificar o CSS pelo JavaScript.

## Key Claims

- "Essa aula é muito importante para poder a gente entender um dos princípios do que acontece, por exemplo, em frameworks [...] o JavaScript sozinho constrói a página web em modos SPA, que é Single Page Application."
- "Eu vou criar uma variável chamada link, onde eu vou acessar o método chamado createElement [...] e vou colocar o nome da tag que eu quero criar."
- "Pode ver que quando a gente cria um link, ele já vem com o atributo href, onde literalmente você pode colocar um endereço para um link interno [...] um endereço de página, então https."
- "Existe a propriedade atributo, então a gente vai acessar ele, link.setAttribute, onde eu vou colocar aqui o atributo href e aqui eu coloco o conteúdo."
- O texto: "criar uma outra variável que se chama conteúdo, onde eu vou criar um outro elemento e jogar um dentro do outro" (um `createTextNode`, digitado num trecho sem legenda).
- "Vou utilizar a propriedade appendChild, traduzindo do inglês, child vem de filho, de criança, então é adicionar informações ao filho [...] através do appendChild eu estou colocando esse conteúdo dentro do link."
- "Assim como é feito na framework, eu vou criar uma div chamada app, por isso que tem o create-react-app, ele renderiza dentro dessa div chamada app."
- `container` é "a div do aplicativo", selecionada com `querySelector`. Como link e texto já estão juntos, "simplesmente eu vou colocar aqui dentro o link".
- "Quando a gente quer criar elementos, a gente pode colocar um dentro do outro por meio da função appendChild e a gente cria de fato as tags, por meio do método createElement."

## Entities

- [[wiki/entities/nasser]]: instrutor (autoria inferida pela sequência do módulo; o nome não é dito).
- [[wiki/entities/frontpush]]: curso; o link da demo aponta para frontpush.com.br.
- [[wiki/entities/react]] e [[wiki/entities/create-react-app]]: o "framework" que a aula usa de motivação.
- [[wiki/entities/javascript]]: assunto da aula.

## Concepts

- [[wiki/concepts/criacao-de-elementos-dom]] (criado neste ingest)
- [[wiki/concepts/dom]]
- [[wiki/concepts/single-page-application]]
- [[wiki/concepts/renderizacao-ssr-vs-csr]]
- [[wiki/concepts/virtual-dom]]
- [[wiki/concepts/reflow-layout]]
- [[wiki/concepts/xss]]
- [[wiki/concepts/carregamento-de-scripts]]

## Precisões e tensões com a wiki

`⚠️` Sem arquivo de referência na skill lang-dynamic para APIs do DOM; as precisões vêm do MDN (`[external]`) e das páginas de React e renderização da wiki.

- **O create-react-app não tem esse nome por causa de uma `div#app`.** O CRA cria `<div id="root">` e o monta com `ReactDOM.createRoot(document.getElementById('root'))`; o nome descreve a ferramenta (criar um app React). A wiki já registra o CRA como descontinuado ([[wiki/entities/create-react-app]]). O Vue CLI, esse sim, usa `#app`.
- **O React não "renderiza o CSS".** Ele cria e atualiza nós do DOM. O CSS chega por arquivos importados que o bundler injeta, ou por CSS-in-JS. E o React não chama `appendChild` a cada mudança: compara árvores ([[wiki/concepts/virtual-dom]]) e aplica só a diferença. O princípio da aula vale; o mecanismo é outro.
- **SPA não é a única forma.** Com renderização no servidor (Next.js, por exemplo), o HTML já chega pronto e o JavaScript só "hidrata" ([[wiki/concepts/renderizacao-ssr-vs-csr]]). "O JavaScript sozinho constrói a página" descreve o CSR.
- **`createElement('a')` não "já vem com o atributo href".** `[external]` O elemento nasce sem atributos; um `<a>` sem `href` não é link (não recebe foco pelo Tab nem aparece como link para leitores de tela). Por isso o `setAttribute` é necessário.
- **`setAttribute` × propriedade.** `link.href = '...'` faz o mesmo e é mais comum; a propriedade devolve a URL absoluta, o atributo devolve o texto escrito.
- **Um nó de texto não é "outro elemento".** `createTextNode` cria um `Text`, que é `Node` mas não `Element`. Para só pôr texto, `link.textContent = 'acessar o FrontPUSH'` faz isso numa linha. `append()` aceita strings e vários nós de uma vez.
- **`appendChild` acrescenta um filho ao pai**, não "informações ao filho": `pai.appendChild(filho)` põe `filho` como último filho de `pai`. É método, não propriedade.
- **Montar fora da página e anexar uma vez** (como a aula faz: link e texto prontos, depois `container.appendChild(link)`) evita recálculos de layout repetidos ([[wiki/concepts/reflow-layout]]). Para muitos itens, `DocumentFragment`.
- **`createElement` + `textContent` é seguro com dados de fora; `innerHTML` não.** Texto do usuário via `innerHTML` executa HTML e scripts ([[wiki/concepts/xss]]).
- **O script precisa rodar depois de `#app` existir**, senão `querySelector` devolve `null` e o `appendChild` quebra; `defer` ou o `<script>` no fim do `body` resolvem ([[wiki/concepts/carregamento-de-scripts]]).
- **"Como a gente viu na última aula, existe a propriedade atributo":** a aula 08 mostrou `innerText`, `classList` e `id`; `setAttribute` aparece aqui pela primeira vez.

## Open Questions

- Há 15 s sem legenda (00:02:56–00:03:11), onde ele digita `document.createTextNode`.
- O nome não é dito nesta aula; a autoria segue a sequência do módulo.

## Raw quotes

- "o JavaScript sozinho constrói a página web em modos SPA"
- "child vem de filho, de criança"
