---
type: source
title: "Elementos da interface: espaçamento e linhas (organização, espaço vs. meio, sistema de espaçamento, padding)"
aliases: ["aula espaçamento e linhas", "espaço vs. meio", "escala linear vs. geométrica", "sistema de espaçamento aula"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, elementos-da-interface, espacamento, linhas, espaco-em-branco, densidade-de-informacao, escala-de-espacamento, padding, consistencia, hierarquia-visual, lei-da-proximidade, figma]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Elementos da interface: espaçamento e linhas (organização, espaço vs. meio, sistema de espaçamento, padding)

## TL;DR

Primeira aula de aprofundamento depois de [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] (mesmo logo "W7" no slide e a mesma promessa de "pegar cada um dos tópicos" da introdução). Teórica; a prática no [[wiki/entities/figma]] fica para a aula seguinte. Sete pontos do slide "Espaçamento & Linhas": **organização** (espaço curto agrupa, longo separa, como nos resultados do [[wiki/entities/google]]); **ênfase e hierarquia** (espaço, recuo e cor); **consistência**; **melhor visualização** em telas densas; **espaço vs. meio**, a ideia nova da aula: quanto mais denso o conteúdo, mais o espaço encolhe e mais linhas e cards entram ([[wiki/entities/meta|Facebook]], G1), enquanto um site simples pode ter espaços grandes ([[wiki/concepts/densidade-de-informacao]]); **sistema** de espaçamento, fixo ou por porcentagem, com escala **linear** (soma constante) ou **geométrica** (dobra), e o autor prefere a geométrica ([[wiki/concepts/escala-de-espacamento]]); **espaçamento interno** (padding), que deixa o card "mais clean".

## Key Claims

### Organização

- **Espaço curto entre elementos agrupa; espaço longo separa.** Slide: "Agrupa elementos: espaço curto / Separa os elementos: espaço longo". Ver [[wiki/concepts/lei-da-proximidade-gestalt]] e [[wiki/concepts/espaco-em-branco]].
- **Google de novo:** um resultado se diferencia do outro "justamente pelo espaço maior que tem entre eles". Mesmo exemplo das aulas anteriores.

### Ênfase e hierarquia

- **Agrupamento, espaço maior até o próximo elemento e recuo lateral criam hierarquia**, somados à diferença de cor. Ver [[wiki/concepts/hierarquia-visual]].

### Consistência

- **Espaçamento precisa de consistência**, explicada pelo "sistema" mais adiante. Ver [[wiki/concepts/consistencia-visual]].

### Melhor visualização e espaço vs. meio

- **Espaçamento e linhas importam mais em interfaces com muita informação**: Google, Facebook, portais de notícia.
- **O espaço depende do meio.** Com o espaçamento largo do site do autor, um portal de notícia "talvez não seria tão confortável" de ler. O site dele se lê "uma vez só"; o portal e o Facebook se abrem quase todo dia para consumir conteúdo. Ver [[wiki/concepts/densidade-de-informacao]].
- **Em conteúdo denso, organize com mais hierarquia de espaço e linha.** O Facebook divide o feed em cards; dentro do card, as informações ficam "mais juntinhas" e linhas enfatizam a divisão; uma linha "de ponta a ponta" separa a seção de conteúdo da seção de interação. O G1 faz o mesmo com linhas e espaçamento.
- **Conteúdo simples permite espaçamentos maiores**, como no site do autor ("é engraçado a gente perceber essa particularidade").

### Sistema de espaçamento

- **O sistema precisa de consistência em todo ele, "um dos princípios do design".**
- **O sistema pode ser fixo ou por porcentagem** (relativo ao elemento pai). A aula fica no fixo.
- **Linear: soma sempre o mesmo valor.** Slide: 2, 4, 6, 8, 10, 12, 14... Com passo de 8 ("8pt, que também é muito comum"): 10, 18, 26...
- **Geométrica: soma com o anterior**, ou seja, dobra. Slide: 2, 4, 8, 16, 32, 64...
- **"Eu aconselho fortemente você trabalhar com a geométrica"**: de 16 para 32 e de 32 para 64 "muda uma quantidade legal", é "mais progressivo e você nota mais a diferença"; de 10 para 12, no linear, quase não. Ver [[wiki/concepts/escala-de-espacamento]].

### Espaçamento interno (padding)

- **Espaçamento interno é o padding do CSS.** Ajuda a manter os elementos "mais focalizáveis" e o design "mais limpo". O autor tem um post no Instagram sobre isso.
- **No card, o padding afasta o conteúdo da borda** e dá "essa sensação de limpeza"; o autor diz que faz isso em todos os cards do site dele. Ver [[wiki/concepts/espaco-em-branco]].

## Entities

- [[wiki/entities/nasser]]: autor, confirmado pelo usuário em 2026-11-13 (o nome não é dito na aula). Fala de "meu site" com espaçamento largo e cards e de um post no Instagram sobre padding.
- [[wiki/entities/google]]: resultados de busca agrupados e separados pelo espaço.
- [[wiki/entities/meta]]: Facebook como interface densa organizada com cards e linhas.
- [[wiki/entities/figma]]: ferramenta da próxima aula, a parte prática.
- Sem página própria: G1 (Globo), portal denso com linhas e espaçamento; Instagram (post do autor sobre padding).

## Concepts

- [[wiki/concepts/densidade-de-informacao]] (novo)
- [[wiki/concepts/escala-de-espacamento]] (novo)
- [[wiki/concepts/espaco-em-branco]]
- [[wiki/concepts/grid-de-8-pontos]]
- [[wiki/concepts/lei-da-proximidade-gestalt]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/elementos-da-interface]]
- [[wiki/concepts/sobrecarga-de-informacao]]

## Tensões com a wiki

- **Geométrica x grid de 8.** Em [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]], a escala é de múltiplos de 8 (16, 24, 32, 40, 48, 56...), que é praticamente **linear** com passo 8, mais 18, 28 e 36 por bom senso. Aqui o autor diz preferir a geométrica (2, 4, 8, 16, 32, 64). As duas aulas parecem ser de edições diferentes do curso (FrontPUSH x "W7"). Não é contradição de fundo: o passo constante só pesa nos valores altos. `[skill: ux-ui-mentor]` A escala de referência da skill é híbrida: 4, 8, 16, 24, 32, 48, 64. Dobra nos valores baixos e inclui 24 e 48 entre as potências de 2. Uma escala puramente geométrica salta de 32 para 64, um vão grande demais para muitos casos (gap entre cards, padding de seção). Ver [[wiki/concepts/escala-de-espacamento]].
- **Linear de 8 com 10, 18, 26.** O exemplo começa em 10, então os valores não são múltiplos de 8; o "8pt" aqui é o passo, não a base. Não é o mesmo que o [[wiki/concepts/grid-de-8-pontos]], cujos valores são múltiplos de 8.
- **"Mais focalizáveis".** O sentido não fica claro: foco visual (o conteúdo se destaca da borda) ou foco de teclado. `[skill: ux-ui-mentor]` Na implementação, o padding de um elemento clicável amplia a área de clique e de toque, que é onde ele ajuda a acessibilidade. `[external]` A WCAG 2.2, critério 2.5.8 (Target Size, Minimum, nível AA), pede alvos de pelo menos 24 × 24 px CSS: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (não relido nesta sessão). Inferência sobre a intenção do autor.
- **Espaço vs. meio x "na dúvida, mais espaço".** `[skill: ux-ui-mentor]` A skill diz que design de iniciante costuma ser denso demais e, na dúvida, pede mais espaço; e trata densidade como modo do sistema (compacto/confortável) em produtos B2B. A aula vai pelo outro lado: conteúdo de consumo diário pede menos espaço. As duas coisas cabem juntas: a densidade certa depende do conteúdo e da frequência de uso, não do gosto. Ver [[wiki/concepts/densidade-de-informacao]].

## Open Questions

- Prática prometida para a aula seguinte: feita em [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] (grid de 12 colunas, nudge de 8pt, escala 16/32/128 no Figma).
- Qual é o post do Instagram sobre espaçamento interno?
- "Meu site": é o [[wiki/entities/frontpush]] ou outro? As aulas "W7" não o nomeiam.
- O que significa "W7"? Edição, turma ou outra marca do curso?
- `date_published` vazio.

## Raw Quotes

> "Quando eu tenho, por exemplo, espaço curto entre elementos, geralmente há o agrupamento e quando eu tenho espaço longo, eu separo os elementos."

> "Uma vez que você lê o meu site, você lê ele uma vez só e você entende, diferente do site de notícia."

> "Eu aconselho fortemente você trabalhar com a geométrica."

## Ver também

- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — seção seguinte da mesma edição "W7" (imagens e ilustrações)
