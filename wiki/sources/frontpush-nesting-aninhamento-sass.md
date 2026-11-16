---
type: source
title: "Nesting (aninhamento) no Sass: tags, & e propriedades (FrontPUSH)"
aliases: ["Propriedade Nesting", "aninhamento Sass FrontPUSH", "módulo de CSS Sass, aula 05", "e comercial Sass"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, sass, scss, nesting, aninhamento, parent-selector, seletores, pseudo-classe, pseudo-elemento, shorthand, menu, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-nesting-aninhamento-sass.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-16
---

# Nesting (aninhamento) no Sass (FrontPUSH)

## TL;DR

Aula 05 do módulo de CSS Sass do [[wiki/entities/frontpush|FrontPUSH]] (instrutor inferido: [[wiki/entities/nasser|Násser]]). Assunto: [[wiki/concepts/aninhamento-css]].

- **O que é:** pôr "uma tag dentro da outra" no SCSS, "a criação do efeito cascata do CSS com mais facilidade"; "pode emendar n cascatas" (slide). Facilita saber qual elemento está sendo estilizado. Uso típico: menu → itens → links.
- **Demo de tags:** `ul.list` > `li` > `a`. Em CSS puro, `.list li`; no SCSS, o `li` vai para dentro do bloco do `.list`, e o CSS gerado é o mesmo ("nada se modificou").
- **`&` (e comercial):** o aninhamento põe espaço entre os seletores; para "colar", usa-se `&`: `&:hover` vira `a:hover`. Mesma lógica para `.active` no link da página atual (`a.active` × `a .active`: "a questão ou não de ter o espaço é importantíssimo") e para `&::before`/`&::after`, que ele usa "demais" nos links do projeto Nubank.
- **Nesting de propriedades:** `border: { style: solid; color: purple; }` gera `border-style` e `border-color`. "Não utilizo muito esse daqui." Ver [[wiki/concepts/shorthand-css]].

## Key Claims

### Aninhamento de tags

- "Você pode estar emendando N cascatas, e a forma de como você coloca no Sass, que pode ser uma tag dentro da outra, facilita na identificação de qual elemento você está estilizando."
- "Essa estrutura aqui é muito utilizada [...] nos meus projetos, quando você vai criar algum menu, onde você cria aqui o menu, aqui os itens do menu e aqui os links do menu" ([[wiki/concepts/listas-html]], [[wiki/concepts/menu-fixo]]).
- HTML: `ul` com classe `list`, `li`s e um link em cada, três vezes. `.list` com borda vermelha de 1 px, `padding: 16px`, `margin-top: 16px`.
- CSS puro: `.list li` = "estilize apenas as tags li que estão dentro da classe list", com `list-style: none` e borda azul ([[wiki/concepts/seletores-css]]).
- SCSS: "simplesmente abrir um li e jogar todo o conteúdo aqui para dentro [...] ele já vem tabulado, então facilita também a organização, a hierarquia visualmente". Ao salvar, "nada se modificou"; o `style.css` gerado é o mesmo.

### & para colar

- Links: `text-decoration: none`, cor branca, e `:hover` "para [...] dar essa resposta para o usuário que isso aqui é um item clicável" ([[wiki/concepts/pseudo-classe-css]], [[wiki/concepts/affordance]]).
- "Quando você faz essa estrutura de nesting, um dentro do outro, ele automaticamente dá um espaço, só que, no caso do hover, você percebe que ele é colado [...] eu preciso simplesmente dar um e comercial."
- "O e comercial está avisando [...]: 'o que eu escrevi aqui, coloque colado dessa tag'." Hover em `pink`.
- Classe `active`: o link da página atual fica rosa ("quando eu estiver na página de produtos, fica só o produto em rosa"), inclusive no menu responsivo. Com espaço: "aplique na classe active que esteja dentro do elemento a"; colado: "as tags [...] a com a classe active".
- `&::before` com `content` vazio "só para poder gerar o CSS" ([[wiki/concepts/pseudo-elemento-css]]). O CSS gerado tem `.list`, `.list li`, `.list a`, `.list a:hover`, `.list a::after`; o SCSS fica "bem encadeado, bonitinho".

### Aninhamento de propriedades

- `border-width: 2px` e `border-color: red` resumíveis em `border: 1px solid red`; "várias propriedades do CSS [...] seguem esse mesmo padrão" (`font` também).
- No Sass: "abrir o border [...] abrir e fechar chaves [...] e dentro desse border eu vou colocar style [...] solid, [...] color [...] purple".
- "Não utilizo muito esse daqui, eu faço mesmo o de tags."

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/frontpush]]: curso; aula 05 do módulo de CSS Sass.
- [[wiki/entities/nubank]]: projeto em que ele usa `&` com `::before`/`::after` nos links.

## Concepts

- [[wiki/concepts/aninhamento-css]]
- [[wiki/concepts/seletores-css]]
- [[wiki/concepts/pseudo-classe-css]]
- [[wiki/concepts/pseudo-elemento-css]]
- [[wiki/concepts/especificidade-css]]
- [[wiki/concepts/cascata-css]]
- [[wiki/concepts/shorthand-css]]
- [[wiki/concepts/listas-html]]
- [[wiki/concepts/menu-fixo]]
- [[wiki/concepts/affordance]]
- [[wiki/concepts/acessibilidade]]
- [[wiki/concepts/pre-processador-css]]

## Precisões e tensões com a wiki

- **Aninhar não é cascata.** "Efeito cascata" aqui quer dizer seletor descendente (`.list li a`). A [[wiki/concepts/cascata-css|cascata]] é o algoritmo que decide qual declaração vence. É a mesma troca de termos das aulas anteriores ("profundidade de cascata" na NLW, "o CSS lê linha a linha" na aula 03).
- **O `&` é o seletor pai.** `[external]` `&` é trocado pelo seletor de fora: `&:hover` → `a:hover`, `&.active` → `a.active`, `& .active` → `a .active`, `&::before` → `a::before`; também serve para sufixos (`&__item` → `.list__item`, o truque do BEM) e para contexto (`.dark &`) (https://sass-lang.com/documentation/style-rules/parent-selector/). O CSS nativo aceita `&` no aninhamento, menos a concatenação de sufixo ([[wiki/concepts/aninhamento-css]]).
- **"N cascatas" tem custo.** `[skill: tech-mentor-frontend]` Cada nível soma especificidade e amarra o CSS ao HTML: `.list li a:hover` vale (0,2,2); um `.list__link:hover` vale (0,2,0) e não quebra se o `li` mudar. Regra usual: no máximo três níveis ([[wiki/concepts/especificidade-css]]).
- **Link ativo e acessibilidade.** `[external]` Além da classe `.active`, o link da página atual deve ter `aria-current="page"`, que o leitor de tela anuncia; dá para estilizar direto por ele: `&[aria-current="page"]` (https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-current). Ver [[wiki/concepts/acessibilidade]].
- **Sintaxe do nesting de propriedades.** `[external]` Precisa de dois-pontos depois do nome: `border: { style: solid; color: purple; }`; dá até para pôr um valor antes da chave (`font: 16px/1.4 { weight: bold; }`) (https://sass-lang.com/documentation/style-rules/declarations/#nesting). Não existe no CSS nativo. Na prática, o shorthand (`border: 1px solid purple`) resolve, e quase ninguém usa o recurso, como ele diz.
- **Shorthand zera o que falta.** `border: 1px solid red` redefine largura, estilo e cor; o que não for escrito volta ao padrão. As longhands mudam só uma parte ([[wiki/concepts/shorthand-css]]).
- **`.list .li`** na fala: com ponto, `li` seria uma classe; o seletor é `.list li a:hover`.
- **`::before` precisa de `content`.** Sem `content`, o pseudo-elemento não é gerado. Por isso o `content: ""` "só para poder gerar o CSS". O padrão atual é `::` (dois-pontos duplos) para pseudo-elementos.

## Open Questions

- "Dentro do parágrafo eu vou escrever o login.y": provavelmente um texto de preenchimento (Emmet `lorem`?); mantido como na legenda.
- O CSS gerado lido em voz alta ("list after") mostra `::after`, mas o código escrito usou `::before`: houve as duas regras, ou é lapso?

## Raw quotes

- "a questão ou não de ter o espaço é importantíssimo no CSS"
- "o que eu escrevi aqui, coloque colado dessa tag"
- "não utilizo muito esse daqui, eu faço mesmo o de tags"
