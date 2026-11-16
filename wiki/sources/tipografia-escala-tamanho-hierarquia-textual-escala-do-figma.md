---
type: source
title: "Tipografia (edição \"W7\"): escala e tamanho, hierarquia textual e a escala do Figma"
aliases: ["aula de escala e tamanho", "escala e tamanho W7", "tipografia escala W7", "escala tipográfica do Násser"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, tipografia, escala-tipografica, hierarquia-visual, consistencia, legibilidade, design-responsivo, style-guide, html, figma]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-15
---

# Tipografia (edição "W7"): escala e tamanho, hierarquia textual e a escala do Figma

## TL;DR

Aula (cerca de 18 min) do módulo de [[wiki/concepts/tipografia]] da edição "W7". Abre com um slide esquecido na aula anterior (placa "PARE" com e sem serifa; maiúsculas imponentes, minúsculas amigáveis; etimologia de tipografia) e entra no tema: **seguir uma [[wiki/concepts/escala-tipografica|escala]]**, comum em style guides, para ter [[wiki/concepts/consistencia-visual|consistência]]. A primeira preocupação é [[wiki/concepts/legibilidade-e-leiturabilidade|legibilidade e leiturabilidade]]; regra geral, **corpo de texto de 14 a 21 px**, mas o tamanho depende do **espaço versus a quantidade de conteúdo**: o [[wiki/entities/new-york-times]] usa 14 px no corpo e 10 px na legenda; o Framer, 106 px no título e 32 no corpo (45 e 23 no mobile); a [[wiki/entities/apple]], SF Pro Display com peso 600, 80 px no título e 28 no corpo. **[[wiki/concepts/hierarquia-visual|Hierarquia textual]]: o que é maior se enxerga primeiro** (manchete da Globo sobre a morte de Maradona). O style guide do [[wiki/entities/nubank]] em produção define h1–h3 em versões desktop e mobile ([[wiki/concepts/design-responsivo]]). **Até 6 variações** (as tags h1–h6 do HTML), mas ele usa **4**. Por [[wiki/concepts/contraste]] visual, tamanhos devem ter **diferenças significativas**: a escala do [[wiki/entities/figma]] cresce em passos maiores no topo (96 → 144 → 288). Ele combina essa escala com a [[wiki/concepts/grid-de-8-pontos|regra dos 8pt]]: **14, 16, 18, 24, 36, 48, 52, 64, 72, 84, 96**.

## Key Claims

### O slide que faltou

- **Fonte errada se estranha "de cara"**: a mesma placa "PARE" com e sem serifa; a serifada "não combina".
- **Maiúsculas** passam imponência, grandiosidade, elegância (predominam em logos de marcas); **minúsculas** são "mais amigável, mais próximo, mais simpático". Ele trabalha "só com letras maiúsculas" nas logos dele. Em um par de fontes, a de maiúsculas "por si só" tem hierarquia maior. Ver [[wiki/concepts/tipografia]].
- **Etimologia:** do grego *týpos* (forma) e *graphein* (escrita): "a arte e o processo de criação na composição de um texto de forma física ou digital".

### Por que uma escala

- É a dúvida mais comum de quem começa: "quais são os tamanhos dos títulos, dos subtítulos". A escala, "muito comum [...] em style guides", serve "para poder a gente conseguir consistência", princípio que "sempre" volta. Ver [[wiki/concepts/escala-tipografica]] e [[wiki/concepts/consistencia-visual]].
- **Primeira preocupação: legibilidade e leiturabilidade**, sobretudo nos corpos de texto. Ver [[wiki/concepts/legibilidade-e-leiturabilidade]].

### Tamanho versus espaço

- **"Sites que têm muito conteúdo geralmente vão utilizar de tamanhos menores"**; com pouco conteúdo textual, "vão abusar desse tamanho". O tamanho também "mexe na acessibilidade".
- **Regra geral: "você não vai errar corpo de texto de 14 pixels a 21 pixels."**
- **New York Times** (medido com o plugin WhatFont): corpo de 14 px, título também de 16 px mas mais escuro e com peso 700 contra 400; legenda de imagem com 10 px. Muito conteúdo obriga a diminuir espaçamentos e fonte "para poder caber a maior quantidade de conteúdo no mesmo espaço". Ver [[wiki/entities/new-york-times]].
- **Framer:** mais visual que descrição; título de 106 px e corpo de 32. No inspecionar, em tela menor, cai para 45 e 23 px: o "balanceio" do mobile. "Existem exceções à regra."
- **Apple** (página do iPhone): SF Pro Display, peso 600, título de 80 px, corpo de 28. "Foge a regra" porque a página tem pouca informação e "é bem seccionado". Ver [[wiki/entities/apple]].
- **Sketch:** "a mesmíssima coisa"; ver na versão mobile como diminuem. Ver [[wiki/entities/sketch]].

### Hierarquia textual

- **"Aquilo que é maior você enxerga primeiro."** No site da Globo, a manchete "Maradona morre aos 60 anos na Argentina" é maior que as outras e alinhada à esquerda; "o povo ocidental [...] lê da esquerda para a direita", e a regra pode mudar em línguas da direita para a esquerda. Ver [[wiki/concepts/hierarquia-visual]].
- No site dele, o texto do hero ("primeira dobra") é maior "de propósito", porque é onde quer chamar atenção para "do que se trata o meu site".

### Style guide: desktop e mobile

- Ele está fazendo o **Style Guide do Nubank** (a ser disponibilizado). A seção de tipografia define as famílias (não serão Ubuntu nem Mukta, que aparecem no rascunho) e o tamanho de heading 1, 2 e 3 numa **versão desktop e numa versão mobile**, seguindo "tamanho versus espaço". Ver [[wiki/entities/nubank]] e [[wiki/concepts/design-responsivo]].

### Até 6 variações, na prática 4

- **"O legal é até 6 variações"**; 6 só para sites complexos, "com muito, muito conteúdo". Ele usa **4 no máximo**: "h1 para títulos maiores e aí conforme vai aumentando o número vai diminuindo o tamanho. É assim que é o padrão em HTML". As tags h1–h6 servem "para apontar para consistência".
- **O site dele:** h1 "bem grande mesmo" no hero; h2 com 48 px, o título que mais se repete e abre cada bloco de conteúdo; h3 com 18 e h4 com 36 ("ou é ao contrário"); corpo de 16 px.

### Contraste visual e a escala do Figma

- **"Definir tamanhos que têm diferenças significativas."** Ver [[wiki/concepts/contraste]].
- **Use a escala do próprio Figma**, que começa em 9. A diferença entre os tamanhos menores é menor, e entre os maiores, maior: "ele é proporcional". De 96 vai para 144 porque 144 e 160 lado a lado mal se distinguem; por isso "coloca 288". Ver [[wiki/entities/figma]].
- **Escala do Figma + regra dos 8pt:** acrescenta valores que o Figma não tem, como 16 ("entre o 14 e o 18"). Os que mais usa: **14, 16, 18, 24, 36, 48, 52, 64, 72, 84, 96** (lista confirmada pela imagem anexada pelo usuário; na fala aparecem ainda 23 e a ordem "64, 52"). Ver [[wiki/concepts/grid-de-8-pontos]].

## Entities

- [[wiki/entities/nasser]]: autor inferido (continuidade "W7", "mas Násser, qual escala que eu uso?", logo W7 no slide); o nome é dito pelo próprio professor ao imitar a pergunta do aluno.
- [[wiki/entities/new-york-times]]: exemplo de muito conteúdo, letras pequenas.
- [[wiki/entities/apple]]: SF Pro Display, peso 600, 80/28 px.
- [[wiki/entities/sketch]]: diminuição no mobile.
- [[wiki/entities/nubank]]: style guide em produção com escalas desktop e mobile.
- [[wiki/entities/figma]]: escala de tamanhos de fonte da ferramenta.
- Sem página própria: Framer, Globo (G1), WhatFont, SF Pro Display, Ubuntu, Mukta.

## Concepts

- [[wiki/concepts/escala-tipografica]] (novo)
- [[wiki/concepts/legibilidade-e-leiturabilidade]] (novo)
- [[wiki/concepts/tipografia]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/contraste]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/grid-de-8-pontos]]
- [[wiki/concepts/escala-de-espacamento]]
- [[wiki/concepts/elementos-da-interface]]

## Tensões com a wiki

- **"14 a 21 px" e a legenda de 10 px.** `[skill: ux-ui-mentor]` A skill põe o corpo base em 16 px ("nunca abaixo disso") e 12 px para captions; no mobile, input abaixo de 16 px faz o iOS dar zoom. O 14 px vale para texto secundário e interfaces densas, como o próprio exemplo do NYT. A WCAG não fixa tamanho mínimo; exige que o texto possa ser ampliado a 200% (1.4.4) `[external]` https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html.
- **h1–h6 "para apontar para consistência".** `[external]` No HTML, o nível do heading é estrutura do documento, não tamanho: o MDN pede para não usar headings para redimensionar texto nem pular níveis (https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements). O tamanho vem do CSS. O próprio site dele mostra isso: se h3 = 18 e h4 = 36, a regra "número maior, tamanho menor" já não vale. A leitura útil: a escala visual tem 4 degraus; o nível semântico segue a estrutura.
- **"Proporcional".** `[skill: ux-ui-mentor]` É a ideia de escala modular: uma razão fixa (1.25 Major Third é a mais comum em UI) gera passos que crescem com o tamanho. A lista dele não tem razão fixa (52 → 64 → 72 → 84 → 96 é quase linear), é uma escala de valores escolhidos à mão, como a [[wiki/concepts/escala-de-espacamento|escala híbrida de espaçamento]].
- **Regra dos 8pt na fonte.** Dos valores dele, 14, 18, 36 e 52 não são múltiplos de 8 (36 e 52 são de 4). "Regra dos 8pt" aqui é inspiração, não restrição. `[skill]` O que costuma seguir a grade de 4/8 é o line-height, não o tamanho da fonte.
- **"Escala do Figma" começando em 9 com 96, 144 e 288.** Não verificado: a busca não confirmou a lista de presets do dropdown de tamanho do Figma. Inferência: é a lista clássica de editores (9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64, 72, 96, 144, 288), o que explica "16 não existe, está entre o 14 e o 18".
- **Hierarquia só por tamanho.** No NYT ele mesmo mostra título e corpo quase do mesmo tamanho, diferenciados por cor e peso. `[skill]` Tamanho, peso, cor, casing, itálico e família são ferramentas de contraste; escolher 2–3 por contexto.

## Open Questions

- **Data de gravação.** "Maradona morre aos 60 anos [...] é meio que a notícia de hoje" sugere 25/11/2020 `[external]` (https://en.wikipedia.org/wiki/Diego_Maradona). Inferência; `date_published` vazio.
- **"wide frame hero" e "iframe hero"**: provável seção hero (primeira dobra); mantidos literais no raw.
- **h3 = 18 e h4 = 36** ou o contrário: ele mesmo não tem certeza.
- **"Na última aula"**: a aula anterior de tipografia (o slide esquecido) não está na wiki.
- **Style guide do Nubank** e a aplicação da escala "quando a gente chegar em Style Guide": prometidos, ainda não ingeridos.
- **Autoria inferida** (Násser).

## Raw Quotes

> "Como uma regrinha geral que a gente vai encontrar na maioria deles, você não vai errar corpo de texto de 14 pixels a 21 pixels."

> "Uma outra coisa que eu queria destacar é hierarquia textual: aquilo que é maior você enxerga primeiro, lógico."

> "Então por isso que a escala é maior espaçada em fontes maiores e menor espaçada em fontes menores."

## Ver também

- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — "tipografia compõe 90% da web"; hierarquia textual no G1
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — a regra dos 8pt aplicada ao espaço; line-height engana a medição
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — font-size 16 px nos botões, "fica para a seção de tipografia"
