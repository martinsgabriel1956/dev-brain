---
type: source
title: "Position no CSS: static, relative, absolute, fixed e sticky"
aliases: ["aula de position CSS", "position CSS FrontPUSH", "Básico CSS: position", "FrontPUSH CSS aula 6"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, frontend, position, layout, viewport, vh, flexbox, menu-fixo, sticky, html-semantico, transition, frontpush]
skill: tech-mentor-frontend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/position-css-static-relative-absolute-fixed-sticky.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-16
---

# Position no CSS: static, relative, absolute, fixed e sticky

## TL;DR

Aula 06 do módulo "Básico CSS" do [[wiki/entities/frontpush|FrontPUSH]] (autoria de [[wiki/entities/nasser|Násser]] inferida). Com uma `section.box` de 500 × 500 px, centralizada no `body` por flexbox, e dois quadrados de 100 px (vermelho e azul), o autor passa pelos cinco valores de [[wiki/concepts/css-position|`position`]]. **static** é o padrão: o elemento fica onde o documento o coloca. **relative** desloca o elemento a partir da posição original dele (`top`, `left`, `bottom`, `right`). Com um valor negativo grande mais `transition`, isso vira o truque de esconder e mostrar um menu mobile. **absolute** mede as distâncias a partir do pai "que tem position relative" (sem ele, o `body`). **fixed** só olha para a tela e não sai do lugar no scroll, por isso serve a menus. **sticky** fica no fluxo até o scroll chegar ao `top` dado e então "transita para o modo fixed". De passagem: [[wiki/concepts/unidades-de-viewport|viewport units]] (`100vh`) para o `body` ocupar a tela inteira. O slide da aula define `absolute` com mais precisão que a fala: "primeiro elemento pai com posição diferente de static".

## Key Claims

### Preparação

- **Position é ferramenta de layout ao lado do flexbox e do grid**: serve a "seções com funcionalidades legais" que flexbox ou grid sozinhos não resolvem.
- **`section` em vez de `div`** "para poder ficar um pouco mais interessante na questão da semântica" ([[wiki/concepts/html-hipertexto]]).
- **`body` com `width: 100%` e `height: 100vh`.** Viewport units são "unidades com relação ao tamanho da tela", criadas porque "hoje em dia nós temos vários dispositivos e a gente quer construir interfaces responsivas" ([[wiki/concepts/unidades-de-viewport]], [[wiki/concepts/design-responsivo]]). Também existe `vw` para a largura.
- **Centralizar com flexbox no pai**: `display: flex`, `justify-content: center` (horizontal) e `align-items: center` (vertical); "a minha seção [...] já se tornou um flex item". O flexbox fica para uma seção própria do curso.

### static

- **É o padrão de "todo e qualquer elemento"**: o elemento "é apresentado na hierarquia que ele é apresentado no documento". Por isso declarar `position: static` não muda nada.
- O slide acrescenta que em `static` "não é possível usar o top e left, pois eles não fazem efeito". `[external]` Correto; `z-index` também não tem efeito: https://developer.mozilla.org/en-US/docs/Web/CSS/position.

### relative

- **"Uma posição relativa em relação a ele mesmo"**: `relative` sem deslocamento não muda nada. Com `top: 100px` o vermelho desce e fica "atrás do azul"; com 200px fica logo abaixo do azul (100 + 100 px).
- **Imagine o contorno tracejado**: a posição original continua ali e "só a parte vermelha vai sair". `[external]` É isso mesmo: o espaço original continua reservado no fluxo e os vizinhos não se mexem (MDN, link acima).
- **Porcentagem também funciona** e é "meio que responsivo", mas dentro de uma caixa de tamanho fixo o resultado fica fixo.
- **Truque de transição**: um valor negativo grande (−1000 px) tira o elemento da tela; num hover ou clique o valor volta a zero e, com `transition`, "dá um efeito legal". É o efeito do menu mobile responsivo que ele mostrou no canal do YouTube. Ver [[wiki/concepts/menu-fixo]].

### absolute

- **Mede as distâncias "com relação ao elemento pai"** que é relative; sem nenhum, "o pai dele é o body". Com `bottom: 0` o quadrado aparece fora da caixa, na base da página.
- **Dar `position: relative` à `.box`** a torna a referência: `bottom: 0; right: 0` cola o item no canto inferior direito da caixa; `top: 0; left: 100%` o cola do lado de fora, à direita.
- **O azul "subiu do nada"** quando o vermelho virou absolute. A aula faz a pergunta e não responde. `[external]` `absolute` tira o elemento do fluxo normal, e o irmão ocupa o espaço que ficou livre: https://developer.mozilla.org/en-US/docs/Web/CSS/position#absolute_positioning.

### fixed

- **"Ele só olha para a sua tela"**: mesmo com o pai `relative`, o `fixed` ignora a caixa. Com `top: 0` fica no lugar enquanto a página (uma `.box` de 2000 px de altura) rola.
- **"Muito utilizado para menus"**: fica fixo "em alguma parte que você queira" ([[wiki/concepts/menu-fixo]]).

### sticky

- **Antes só se fazia "com o JavaScript"**; agora só com CSS.
- **Exemplo**: `nav` com `ul` (produtos, sobre, contato) sobre fundo `#CCC`, um `span` de texto acima e um parágrafo de 2000 px abaixo para criar scroll. Com `position: sticky; top: 0` nada muda no início; ao rolar, o menu para no topo: "ele faz a transição do position sticky para o position fixed".
- Fecha com "não deixem de ler e procurar mais referências"; os links prometidos não estão na transcrição.

## Entities

- [[wiki/entities/nasser]]: autor inferido. A legenda está na pasta "FrontPush", junto com as aulas de interfaces web; o slide traz o logo do curso e o do autor. Ele cita "meu canal do YouTube" e um menu mobile responsivo que fez lá. O nome não é dito.
- [[wiki/entities/frontpush]]: curso de origem; slide "Básico CSS".

## Concepts

- [[wiki/concepts/css-position]] (novo)
- [[wiki/concepts/unidades-de-viewport]] (novo)
- [[wiki/concepts/menu-fixo]] (novo)
- [[wiki/concepts/css]]
- [[wiki/concepts/box-model]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/reflow-layout]]
- [[wiki/concepts/paint-composite]]
- [[wiki/concepts/html-hipertexto]]
- [[wiki/concepts/handoff-design-dev]]
- [[wiki/concepts/style-guide]]

## Tensões com a wiki

- **"O pai que tem position relative" x "diferente de static".** A fala reduz a regra a `relative`; o slide está certo. `[external]` A referência do `absolute` é o ancestral posicionado mais próximo (`relative`, `absolute`, `fixed` ou `sticky`); `transform`, `filter` ou `contain` também criam o bloco de contenção. Sem nenhum, a referência é o *initial containing block* (o tamanho da viewport), não o `body`: https://developer.mozilla.org/en-US/docs/Web/CSS/Containing_block. Na demonstração não faz diferença, porque o `body` ocupa a tela.
- **"fixed só olha para a tela" tem exceção.** `[external]` Um ancestral com `transform`, `perspective` ou `filter` vira a referência do `fixed`, e o "menu fixo" passa a rolar junto com esse ancestral (MDN, link de `position`).
- **Sticky não vira fixed para sempre.** `[external]` Pela MDN, o elemento é tratado como relative até cruzar o limite e como fixed "até encontrar a borda oposta do seu bloco de contenção". O menu só acompanha o scroll enquanto o pai estiver na tela. `overflow: hidden` ou `auto` num ancestral faz o sticky se prender a esse ancestral. Na aula a `nav` é filha do `body`, então funciona.
- **Animar `top` x `transform`.** O truque do −1000 px com `transition` anima uma propriedade de layout. `[skill: tech-mentor-frontend]` `references/frontend-performance-deep.md` marca `left`/`top` como "provoca reflow" e recomenda `transform: translateX()` + `opacity`, que só passam pelo composite ([[wiki/concepts/reflow-layout]], [[wiki/concepts/paint-composite]]). Mesmo efeito, mais barato.
- **"Camadas" ficaram no slide.** O slide fala em posicionamento em três dimensões ("horizontal, vertical e em camadas"), mas a aula não fala de `z-index`. O vermelho fica "atrás do azul" porque os dois são posicionados e o azul vem depois no DOM `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Stacking_context). Inferência do agente.
- **`100vh` no celular.** `[external]` Em navegadores móveis `100vh` usa a altura com a barra de endereço recolhida e pode cortar conteúdo; `100dvh` (dinâmica) e `100svh` (menor) resolvem: https://developer.mozilla.org/en-US/docs/Web/CSS/length#relative_length_units_based_on_viewport. E `width: 100%` no `body`, com a margem padrão de 8 px, cria scroll horizontal.
- **Figma descarta position, a aula de CSS ensina.** Nas aulas de [[wiki/concepts/style-guide]] o `position` gerado pelo Figma vai fora "tendo o flexbox e o grid" ([[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]]). Aqui position é para o que flexbox e grid não fazem (sobrepor, fixar, grudar). Não há contradição: o layout é do flexbox e do grid, e o position fica para casos pontuais.

## Open Questions

- Os "links que eu também vou deixar" não estão na transcrição; provavelmente no Notion do curso.
- A legenda pula de 00:10:20 para 00:10:38 (cerca de 18 s sem fala) bem quando ele dá `position: relative` à `.box`; "o próprio azul já desapareceu" deve se referir ao `display: none` do item 2.
- "Olha, não tem a minha tag body" (provavelmente "eu tenho") e "o outro quadradinho que está em média de 100px" (provavelmente "de medida") ficaram literais no raw.
- `date_published` vazio.

## Raw Quotes

> "É uma posição relativa, mas é uma posição relativa em relação a ele mesmo."

> "Ele só olha para a sua tela, essa é a única referência do position fixed."

> "Ele faz a transição do position sticky para o position fixed."

## Ver também

- [[wiki/sources/usabilidade-facilmente-tres-esferas-boas-praticas-auxilio-emergencial]]: menu fixo no topo como padrão de usabilidade (site da Apple)
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]: por que animar `top` custa mais que animar `transform`
