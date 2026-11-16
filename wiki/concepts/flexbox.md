---
type: concept
title: "Flexbox (display: flex)"
aliases: ["flexbox", "display flex", "flex", "flex-direction", "justify-content", "align-items", "flex: 1"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 22
tags: [frontend, css, flexbox, layout, display, alinhamento]
skill: tech-mentor-frontend
status: stub
---

# Flexbox (display: flex)

Modelo de layout em uma dimensão: `display: flex` no pai organiza os filhos ao longo de um eixo principal (linha por padrão, coluna com `flex-direction: column`). `justify-content` distribui no eixo principal, `align-items` alinha no eixo cruzado, e `flex` nos filhos diz quanto cada um cresce ou encolhe. Por fora, o elemento flex continua de bloco. Ver [[wiki/concepts/display-css]] e [[wiki/concepts/box-model]].

## Na NLW #1

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa flexbox em quase toda a página do Ecoleta:

- **Header:** `display: flex` põe logo e link lado a lado, `align-items: center` alinha e `justify-content: space-between` separa. "Você não sabe o tanto que a gente sofreu no passado para fazer esse tipo de alinhamento".
- **Coluna que ocupa a sobra:** `.content` em `flex-direction: column`; `main` com `flex: 1` ("preenche automaticamente todo o espaço") e `justify-content: center`. Ao mudar a direção, o mesmo `justify-content` passa a agir na vertical.
- **Botão:** `a` flex com um `span` fixo de 72 px e um `strong` com `flex: 1` + `text-align: center`.
- **Flex por fora é block:** "Quando eu faço [...] display flex, [...] por fora, ela vai ser a propriedade block".

## Precisões

- `flex: 1` é shorthand de `flex-grow: 1; flex-shrink: 1; flex-basis: 0%`, não só flex-grow `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/flex). Ver [[wiki/concepts/flex-grow-shrink-basis]].
- `gap` no contêiner flex substitui margens entre itens; a aula usa `margin-right` no ícone `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/gap).
- Para duas dimensões (linhas e colunas ao mesmo tempo), `grid` costuma servir melhor `[skill: tech-mentor-frontend]`.

## Na NLW #1, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa `flex-direction: column` em cada `.field` (label sobre input) e `flex: 1` nos campos de um `.field-group` para que "estique automaticamente preenchendo todo o espaço".

## No módulo de front-end do FrontPUSH (aula 06)

Em [[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]], [[wiki/entities/nasser|Násser]] resume: `display: flex` "pega todos os seus filhos diretos, eles vão virar flex-itens e o container é o flex pai", e "automaticamente um vai ficar do lado do outro", porque o `flex-direction` padrão é `row`. Abaixo de 960 px, uma media query troca para `column`. Cita também Grid Layout e "Grid System com Sass, utilizando float" como alternativas, cada uma com módulo próprio. `[external]` Flexbox é unidimensional, Grid bidimensional; float para colunas é legado.

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] contrasta o flex, "unidimensional", com o [[wiki/concepts/css-grid|grid]], "multidimensional". Dentro de cada item de coleta, `flex-direction: column` com `justify-content: space-between` separa imagem e texto na vertical, porque "eu inverti o fluxo". O `span` usa `flex: 1` para ocupar a sobra. No modal, o input com `flex: 1` empurra o botão de 72 px para o canto.

## No módulo de Flexbox do FrontPUSH (aula 01)

Em [[wiki/sources/frontpush-intro-flexbox-flex-container-flex-item]], [[wiki/entities/nasser|Násser]] abre o módulo dizendo que o Flexbox "serve para layout": o CSS básico estiliza, o Flexbox constrói "o esqueleto" responsivo. Divide o estudo em propriedades do contêiner e dos itens; ver [[wiki/concepts/flex-container-e-flex-item]]. Pede repetição e prática sozinho: "já Flexbox você precisa sentar e fazer".

## No módulo de Flexbox do FrontPUSH (aula 02)

Em [[wiki/sources/frontpush-display-flex-flex-container-filhos-diretos]], [[wiki/entities/nasser|Násser]] aplica `display: flex` num `section.container` com quatro `div.item`: em `block`, um embaixo do outro; em flex, "automaticamente, um item ficou um do lado do outro". Com 12 itens, eles transbordam o container. `[external]` Quem quebra a linha é `flex-wrap: wrap` no contêiner, não uma propriedade dos itens.

## No módulo de Flexbox do FrontPUSH (aula 03)

Em [[wiki/sources/frontpush-flex-direction-flex-wrap-flex-flow]], [[wiki/entities/nasser|Násser]] cobre `flex-direction` (`row` padrão, `row-reverse`, `column`, `column-reverse`), `flex-wrap` (`nowrap` padrão, `wrap`, `wrap-reverse`) e `flex-flow`, "simplesmente um atalho" dos dois, que ele evita. Trocar `row` por `column` numa media query é, para ele, "o princípio do sistema responsivo".

## No módulo de Flexbox do FrontPUSH (aula 04)

Em [[wiki/sources/frontpush-justify-content-align-items-box-sizing]], [[wiki/entities/nasser|Násser]] cobre `justify-content` (`flex-start`, `center`, `flex-end`, `space-between`, `space-around`) e `align-items` (`stretch`, `flex-start`, `center`, `flex-end`, `baseline`), e chama `display: flex` + `justify-content: center` + `align-items: center` no `body` de "o combo desses três" para centralizar. Diz que o padrão de `align-items` é `flex-start`; `[external]` é `stretch` (https://developer.mozilla.org/en-US/docs/Web/CSS/align-items).

## No módulo de Flexbox do FrontPUSH (aula 05)

Em [[wiki/sources/frontpush-align-content-linhas-flex-wrap]], [[wiki/entities/nasser|Násser]] mostra `align-content`: só faz diferença com muitos itens e `flex-wrap` ligado, porque distribui as linhas que quebraram. Ele quase não usa ("na maioria das vezes eu coloco três") e prefere `flex-direction`. `[external]` `align-content` move linhas; `align-items` move itens dentro de cada linha.

## No módulo de Flexbox do FrontPUSH (aula 06)

Em [[wiki/sources/frontpush-flex-grow-crescer-espaco-disponivel]], [[wiki/entities/nasser|Násser]] começa as propriedades dos itens com `flex-grow`: padrão 0, só age quando sobra espaço ("aumentar quando está disponível"), e só aparece diferença com fatores diferentes. Ver [[wiki/concepts/flex-grow-shrink-basis]].

## No módulo de Flexbox do FrontPUSH (aula 07)

Em [[wiki/sources/frontpush-flex-basis-tamanho-base-flex-itens]], [[wiki/entities/nasser|Násser]] explica `flex-basis` e o combina com `flex-grow` e `flex-wrap` para cards que "conseguem variar em vários tamanhos de tela". Ver [[wiki/concepts/flex-grow-shrink-basis]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]], o CSS pronto do Ecoleta web usa flexbox em quase tudo: "eu utilizo esse display flex pra tudo na minha vida".

## No módulo de Flexbox do FrontPUSH (aula 08)

Em [[wiki/sources/frontpush-flex-shrink-e-flex-shorthand]], [[wiki/entities/nasser|Násser]] fecha as propriedades de tamanho dos itens com `flex-shrink` e o atalho `flex`, "o que eu mais utilizo"; `flex: 1` = grow 1, shrink 1, basis 0, o mesmo `flex: 1` da NLW #1. Ver [[wiki/concepts/flex-grow-shrink-basis]].

## No módulo de Flexbox do FrontPUSH (aula 09)

Em [[wiki/sources/frontpush-order-e-align-self]], [[wiki/entities/nasser|Násser]] termina a teoria com `order` e `align-self` antes dos projetos práticos. A lista completa está em [[wiki/concepts/flex-container-e-flex-item]].

## No módulo de Flexbox do FrontPUSH (aula 10, prática 1)

Em [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]], [[wiki/entities/nasser|Násser]] planeja uma página de vídeo no estilo do YouTube "utilizando apenas Flexbox": desenha as caixas sobre o design (fundo diferente = div de ponta a ponta; dentro, container centralizado; dentro, linhas e colunas), porque "em flexbox a gente sempre pensa em linhas". Só HTML nesta aula.

## No módulo de Flexbox do FrontPUSH (aula 11, prática 2)

Em [[wiki/sources/frontpush-flexbox-pratica-2-desafio-estrutura-de-divs]], [[wiki/entities/nasser|Násser]] propõe um layout-desafio sem código: container no grid, três flex-itens que quebram de "ABC" para "ABC em coluna" (media query `row` → `column` ou `flex-wrap` + `flex-basis`), e flex dentro de flex, com os itens como "filhos direto" do pai.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], "todos os elementos são display flex por natureza" no React Native, via Yoga. Diferença: o eixo padrão é coluna, não linha.

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], `display: flex` no body muda o "fluxo padrão do HTML" e põe os filhos lado a lado; `align-items: center` e `justify-content: center` "só funcionam quando tem o display flex" (ou grid). Com `height: 100vh` em `html, body`, o `#container` fica no centro da tela.

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: `justify-content: space-between` ("between significa entre"), `space-evenly` ("espaçamentos [...] meio que constantes"), `flex-start` para desfazer o center no desktop, `flex-direction: column` no header e `flex: 1 1` no `.header-content`, que "parece que não fez diferença" até o resto do layout entrar.

Na [[wiki/sources/frontpush-mentoria-pratica-com-css-grid|mentoria de CSS Grid]] do [[wiki/entities/frontpush|FrontPUSH]], o critério fica explícito: layout de linhas sem mescla, flexbox; linhas e colunas mescladas, grid, porque em flex seria "flexbox dentro do flexbox, que fica dentro do flexbox, vai virando uma salada".

## Key sources

- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: header, coluna com `flex: 1`, botão com span + strong
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: campos do formulário em coluna e flex: 1
- [[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]]: filhos diretos viram itens; `row` padrão; `column` na media query
- [[wiki/sources/frontpush-position-css-relative-absolute-coordenadas]]: position "não é feito para fazer layout em si"; no FrontPUSH, "o resto todo, eu utilizo o flexbox"
- [[wiki/sources/frontpush-conclusao-modulo-css-estilo-layout-animacao-documentacao]]: "centralizar uma div" com flexbox ou grid como exemplo de dúvida para o Google
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: flex x grid; space-between em coluna; flex: 1 no input
- [[wiki/sources/frontpush-intro-flexbox-flex-container-flex-item]]: abertura do módulo: "Ele serve para layout"; flex-container x flex-itens
- [[wiki/sources/frontpush-display-flex-flex-container-filhos-diretos]]: aula 02: `display: flex` põe os itens lado a lado; 12 itens transbordam
- [[wiki/sources/frontpush-flex-direction-flex-wrap-flex-flow]]: aula 03: flex-direction, flex-wrap e flex-flow; row → column na media query
- [[wiki/sources/frontpush-justify-content-align-items-box-sizing]]: aula 04: justify-content, align-items e o "combo" de centralizar; align-items padrão é stretch, não flex-start
- [[wiki/sources/frontpush-align-content-linhas-flex-wrap]]: aula 05: align-content só com várias linhas (flex-wrap); pouco usado
- [[wiki/sources/frontpush-flex-grow-crescer-espaco-disponivel]]: aula 06: flex-grow só age com espaço livre; fatores 1, 2, 4
- [[wiki/sources/frontpush-flex-basis-tamanho-base-flex-itens]]: aula 07: flex-basis; cards com base fixa + wrap + grow
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: CSS do Ecoleta web
- [[wiki/sources/frontpush-flex-shrink-e-flex-shorthand]]: aula 08: flex-shrink e o shorthand flex
- [[wiki/sources/frontpush-order-e-align-self]]: aula 09: order e align-self; fim da teoria
- [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]]: prática 1: planejar as caixas sobre o design do YouTube
- [[wiki/sources/frontpush-flexbox-pratica-2-desafio-estrutura-de-divs]]: prática 2: desafio; três colunas que quebram; flex dentro de flex
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: RN: tudo é flex, eixo padrão coluna
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: centralizar o container no body
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: space-between, space-evenly, flex 1 1
- [[wiki/sources/frontpush-mentoria-pratica-com-css-grid]]: mentoria de grid: flex é "unidimensional"; layout com linhas e colunas mescladas em flex vira "flexbox dentro do flexbox [...] uma salada"
