---
type: source
title: "Mentoria: prática com CSS Grid, grid-template-areas como mesclar células no Excel (FrontPUSH)"
aliases: ["Mentoria Prática com CSS Grid", "FrontPUSH mentoria CSS Grid", "grid-template-areas FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, css-grid, grid-template-areas, grid-area, gap, flexbox, media-query, design-responsivo, frontend, curso, mentoria]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-mentoria-pratica-com-css-grid.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-16
---

# Mentoria: prática com CSS Grid (FrontPUSH)

## TL;DR

Sessão de mentoria do [[wiki/entities/frontpush|FrontPUSH]] (instrutor inferido: [[wiki/entities/nasser|Násser]]; um aluno responde "Sim, tranquilo"). Ele monta um layout de cards ("cores", "interface", "tipografia", "Figma", "elementos") com [[wiki/concepts/css-grid]]:

- **Por que grid e não flex:** o [[wiki/concepts/flexbox]] é "unidimensional"; quando linhas e colunas se mesclam, dá para fazer com flex, mas vira "flexbox dentro do flexbox, que fica dentro do flexbox [...] uma salada". Duas dimensões, grid; uma, flex.
- **Analogia do Excel:** o layout é "uma tabela cheia de células pequenas"; cada card é um "mesclar e centralizar". O tamanho da linha sai do **menor elemento** (o card "Figma", uma célula). Resultado: matriz 5 × 5, 25 células.
- **Código:** `display: grid` no container (o pai; os filhos diretos viram grid itens, como em [[wiki/concepts/flex-container-e-flex-item]]), `grid-template-areas` escrito "em forma de matriz", `grid-area: A` etc. em cada item, `grid-gap`.
- **Responsivo:** uma media query `max-width: 960px` redefine só o `grid-template-areas` (por exemplo, para 4 × 4). Ver [[wiki/concepts/breakpoint]] e [[wiki/concepts/design-responsivo]].

## Key Claims

### Grid × flexbox

- "Da mesma forma que a gente faz com o flexbox, a gente precisa de um container pai [...] o grid container, e todos os filhos diretos viram grid itens."
- "O CSS Flexbox é unidimensional, então sempre quando a gente está fazendo um layout em que ele é composto por linhas, onde não tem [...] linhas e colunas sendo mescladas, a gente faz com o flexbox."
- "Quando a gente mexe com duas dimensões, mesclando linhas e colunas, é melhor o CSS Grid, quando é só uma dimensão, a gente faz com o flexbox, que é mais fácil."

### Desenhar a matriz antes do código

- No Excel, A1, A2, B1 e B2 "viram uma área só": "a gente mescla linha e coluna, então o CSS Grid é exatamente a mesma coisa".
- "Você vai pegar sempre o menor elemento, o menor elemento é esse Figma aqui, então toma ele com o tamanho de uma linha." Daí saem cinco linhas e cinco colunas.
- Seis colunas também serviriam, mas "como elas são vizinhas, quando você mandar mesclar e centralizar é a mesma coisa".
- Áreas nomeadas por letra: A (cores, 6 células), B, C, D (o "Figma pequeno", "só ocupa uma célula") e E. "Você pode chamar da área que você quiser."
- "A primeira coisa é você dividir o seu layout dessa forma aqui para poder a gente conseguir desenhar isso." O mesmo passo de desenhar caixas sobre o design aparece em [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]].

### Base do projeto

- Reset com margin e padding zerados e `box-sizing: border-box` ([[wiki/concepts/estilos-padrao-do-navegador-e-reset]], [[wiki/concepts/box-model]]); fundo `#070707`.
- `.container` com `max-width: 1440px`, `margin: 0 auto`, fundo `#090909`, borda de 1 px e altura de 700 px "só para poder a gente visualizar"; `padding` de 24/16 px no body.
- Roboto pelo [[wiki/entities/google-fonts]] ([[wiki/concepts/webfonts]]); h1 branco, parágrafo `#555`; classe comum `.item` com fundo `#0B0B0B` e `padding: 16px` "para deixar a interface respirando".

### display grid, template areas e gap

- Sem mais nada, `display: grid` "parece que está no display block, porque continua um elemento embaixo do outro [...] não é que nem o display flex". Os itens preenchem a largura do container ([[wiki/concepts/display-css]]).
- `grid-template-areas`: "nós vamos literalmente escrever isso aqui, as células": duas linhas `AAABB` e três `CCEEE`. Dá para escrever tudo em sequência, "mas é bom a gente se colocar sempre em forma de matriz para a gente visualizar".
- "Eu defino que o item A tem o grid-area [...] É o A, enquanto o B é o B [...] quando você salva, automaticamente ele já desenhou para você."
- Margin fica de fora: o espaço vem do `grid-gap` ("eu quero uma distância entre os elementos, aí você coloca o grid-gap").

### Mudar o layout por media query

- "Você faz aqui um media screen e max-width, dá 960 pixels, e aí você vai definir um container aqui dentro, onde você vai mudar o grid-template-areas [...] ele vai ler o novo grid-template-areas e vai aplicar."
- Uso citado: "construir esses layouts de grids para galerias de forma bem mais fácil".

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/frontpush]]: curso; sessão de mentoria.
- [[wiki/entities/google-fonts]]: Roboto.

## Concepts

- [[wiki/concepts/css-grid]]
- [[wiki/concepts/flexbox]]
- [[wiki/concepts/flex-container-e-flex-item]]
- [[wiki/concepts/display-css]]
- [[wiki/concepts/box-model]]
- [[wiki/concepts/estilos-padrao-do-navegador-e-reset]]
- [[wiki/concepts/webfonts]]
- [[wiki/concepts/breakpoint]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/mobile-first]]
- [[wiki/concepts/acessibilidade]]
- [[wiki/concepts/grid-de-colunas]]

## Precisões e tensões com a wiki

- **Os nomes da matriz precisam de espaço.** `[external]` Em `grid-template-areas`, cada célula é um token separado por espaço: `"A A A B B"`. Escrito colado, `"AAABB"` é **uma** célula chamada `AAABB`, e o grid fica com uma coluna só; `grid-area: A` então não acha área nenhuma e o item vai para linhas implícitas. A fala ("faço AAA [...] AAABB") deve ser só a leitura em voz alta, mas o código precisa dos espaços: https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-areas.
- **Cadê o D?** A matriz falada (`AAABB` ×2, `CCEEE` ×3) não tem a área D, o card "Figma" que serviu de medida da linha. Um item com `grid-area: D` sem área correspondente cai fora do desenho. Pela planilha, D ocuparia uma célula própria; a transcrição não mostra a linha certa. Ver Open Questions.
- **Áreas só retangulares.** `[external]` Cada nome tem de formar um retângulo; um L é inválido e a declaração inteira é descartada. O "mesclar e centralizar" do Excel tem a mesma regra. Células vazias usam `.`.
- **`grid-gap` é o nome antigo.** `[external]` Hoje é `gap` (o antigo continua como alias). O valor é a distância inteira entre trilhas, sem metade de cada lado: o trecho "16 pixels, então 8 pixels, vai ter uma distância de 8 pixels" mistura as duas coisas. A wiki já usa `gap` em [[wiki/concepts/css-grid]].
- **Desktop-first.** A media query é `max-width: 960px`, o mesmo número da aula de `flex-direction` do curso ([[wiki/sources/frontpush-flex-direction-flex-wrap-flex-flow]]). A NLW #2 faz o contrário com `min-width` ([[wiki/concepts/mobile-first]]). As duas funcionam; mudar só o `grid-template-areas` dentro dela é o ponto forte da técnica.
- **Reordenar por área é como `order`.** `[external]` Trocar a posição das áreas muda só o que se vê; leitor de tela e Tab seguem o HTML, como já anotado em [[wiki/sources/frontpush-order-e-align-self]] e [[wiki/concepts/acessibilidade]].
- **`height 100` sem unidade.** Como foi dito, é inválido (só `0` dispensa unidade); deve ser `100%` ou `100vh`.
- **"Por que seria tão difícil [...] utilizando o CSS Grid? O CSS Flexbox".** Ele se corrige na hora: o difícil seria com flexbox.

## Open Questions

- Onde entra a área D no `grid-template-areas`? Faltou uma linha, ou B era menor (por exemplo, `"A A A B D"`)?
- "A gente starta o SAS": Live Sass Compiler ou outro servidor? O arquivo criado é `style.css`.
- Autoria: inferida como Násser pelo curso, pelos fundos quase pretos (`#070707`/`#090909`/`#0B0B0B`, como o `#0c0c0c` da prática 1) e pelo breakpoint de 960 px. A gravação não diz o nome. `date_published` vazio.

## Raw quotes

- "vai virando uma salada"
- "o CSS Grid é exatamente a mesma coisa"
- "você vai pegar sempre o menor elemento"
