---
type: source
title: "Imagens e ilustrações (edição \"W7\"): como funciona o SVG no Figma (unDraw, mockup de iPhone e o código do SVG)"
aliases: ["SVG no Figma", "mockup de iPhone no Figma", "estrutura do SVG", "aula de SVG W7"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, figma, svg, ilustracoes, undraw, mockup, operacoes-booleanas, export, css, motion, isometria, wireframe]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Imagens e ilustrações (edição "W7"): como funciona o SVG no Figma

## TL;DR

Aula curta (cerca de 10 min) que fecha a sequência de ilustrações da edição "W7" mostrando o que um [[wiki/concepts/formato-svg|SVG]] é por dentro: (1) os [[wiki/concepts/wireframe|wireframes]] do autor usam o mesmo princípio da [[wiki/concepts/ilustracao-isometrica|isometria]] da aula anterior, mais gradiente linear e sombra (feitos com o "skill-that"); (2) uma ilustração do [[wiki/entities/undraw]] baixada em SVG pesa 9KB, entra no [[wiki/entities/figma]] como frame e é **toda editável** (trocar cor, copiar trechos para montar a sua); (3) "o grande pulo do gato": a ilustração é só um conjunto de formas, então dá para construir a sua. Exemplo: um **mockup de iPhone** desenhado por cima de uma foto, com retângulos a 20% de opacidade, guias da régua, border-radius e a **subtração** do modo de combinar ([[wiki/concepts/operacoes-booleanas-em-formas]]); (4) **export do frame em SVG**: 2KB (4KB em disco), "resolução infinita"; (5) aberto no VS Code, o SVG é **código**: `defs` com o gradiente linear e filtros (inclusive de sombra), um ID ("paint-linear") aplicado aos caminhos, preenchimentos em hexadecimal. Por ser código com tags, o [[wiki/concepts/css]] manipula: "a magia do Motion surgiu daqui", tema do curso seguinte.

## Key Claims

### Isometria nos wireframes

- **Mesmo princípio da isometria**, com os elementos posicionados sobre "algum gradiente linear embaixo", efeitos de sombra "com contraste legal" e boa seleção de cores. Um deles ele acredita ter feito com o "skill-that" (o plugin "skill-depth" da aula anterior; ver Open Questions). Ver [[wiki/concepts/ilustracao-isometrica]] e [[wiki/concepts/wireframe]].

### SVG do unDraw no Figma

- **Baixar em SVG** ("download SVG", "mostrar na pasta") e arrastar para o Figma.
- **Leve:** a ilustração pesa 9KB, "já vem embutido no modo frame". Ver [[wiki/concepts/otimizacao-de-imagens]].
- **Tudo editável:** mudar totalmente a cor (exemplo: roxo), copiar e colar elementos, ou "pegar apenas trechos para poder você formar as suas próprias ilustrações". É por isso que ele gosta do [[wiki/entities/undraw]]: "download vasto de ilustrações, onde você pode mudar a cor". Ver [[wiki/concepts/ilustracoes-em-interfaces]].

### Ilustração é um conjunto de formas: o mockup de iPhone

- **"O grande pulo do gato":** "isso aqui são todas formas"; se o unDraw construiu a ilustração com formas, "a gente pode muito bem construir a nossa". Prova: o iPhone de mockup do style guide dele, colado e preenchido com 1A, é "um conjunto de formas que eu consigo fazer no Figma".
- **Construído no Figma, exporta em SVG "exatamente"** como está.
- **Como fez o iPhone:** pegou "algum mockup de alguém, ou então uma foto do próprio iPhone"; arrastou guias da régua; desenhou um retângulo a **20% de opacidade** para enxergar a foto embaixo e arrastou até a borda bater; repetiu para a parte de dentro; um terceiro retângulo para o recorte (notch), ajustado com as setas e com border-radius.
- **Recorte por subtração:** voltar a opacidade a 100%, selecionar os dois com Shift e, no modo de combinar, escolher subtrair (há também interseção). Ver [[wiki/concepts/operacoes-booleanas-em-formas]].
- **Atalhos lembrados:** espaço para navegar, Ctrl-Mais e Ctrl-Menos para zoom.
- **Régua:** ele não lembra onde ativa ("window, preference, enfim") e promete dizer depois. `[external]` No Figma é Main menu → View → Rulers, ou "Show or hide rulers" no menu de ações (Ctrl K) (https://help.figma.com/hc/en-us/articles/360040449713-Add-guides-to-the-canvas-or-frames).
- **"Dá um trabalhinho"**: fica de exercício.

### Export em SVG

- **Clicar no frame → export → SVG**, nome "mockup-iphone", salvo na área de trabalho.
- **Abre no navegador** com duplo clique; nas propriedades, "pesa apenas 2KB, e o tamanho diz 4KB": "muito, muito leve", "muito fiel" e com "resolução infinita". `[external]` A diferença 2KB vs. 4KB é tamanho real vs. tamanho em disco (o sistema de arquivos aloca em blocos de 4KB).

### A estrutura do SVG em código

- **Aberto no VS Code, "é só código".**
- **Definições (`defs`)** estabelecem o gradiente linear; **filtros em SVG**, "inclusive filtros de sombra", tudo "configurado via código".
- **O gradiente laranja** tem duas cores laranja e recebe um ID ("paint-linear"), aplicado aos caminhos: "os círculos, os retângulos e os outros caminhos que a gente definiu lá com o Figma". O preenchimento também vem em hexadecimal.
- **Por ser código, é leve**; e por ter tags, "eu posso muito bem manipular eles via CSS": "meio que a magia do Motion surgiu daqui". Os detalhes ficam para o curso de Motion. Ver [[wiki/concepts/formato-svg]] e [[wiki/concepts/css]].

## Entities

- [[wiki/entities/nasser]]: autor (confirmado pelo usuário).
- [[wiki/entities/figma]]: ferramenta da aula toda (régua, guias, modo de combinar, export).
- [[wiki/entities/undraw]]: biblioteca da ilustração baixada em SVG.
- Sem página própria: VS Code, o plugin "skill-that"/"skill-depth", o curso de Motion.

## Concepts

- [[wiki/concepts/formato-svg]]
- [[wiki/concepts/operacoes-booleanas-em-formas]] (novo)
- [[wiki/concepts/ilustracoes-em-interfaces]]
- [[wiki/concepts/ilustracao-isometrica]]
- [[wiki/concepts/wireframe]]
- [[wiki/concepts/otimizacao-de-imagens]]
- [[wiki/concepts/css]]

## Tensões com a wiki

- **CSS só alcança o SVG inline.** A fala diz que, por ter tags, o SVG é manipulável via CSS. `[external]` Vale para SVG inline no HTML; via `<img>` ou `background-image` os caminhos ficam opacos ao CSS da página (mesma ressalva da abertura "W7", ver [[wiki/concepts/formato-svg]]). `[skill: ux-ui-mentor]` O trade-off é renderizar junto do HTML (inline) vs. ganhar cache (`<img>`).
- **"Resolução infinita" com filtros.** Os vetores escalam sem perda, mas `[external]` filtros SVG (sombra com `feGaussianBlur`, por exemplo) são rasterizados pelo navegador na hora e custam processamento; o Figma exporta sombras e alguns gradientes como filtros, o que pesa mais que caminhos simples. Para animar, o custo importa ([[wiki/concepts/mobile-animacoes-performaticas]]).
- **Mesmo número de opacidade, outro uso.** Os 20% de opacidade da [[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao|aula prática]] eram a capa preta atrás do texto; aqui são só para enxergar a foto de referência enquanto desenha, voltando a 100% no fim.
- **Ilustração pronta vs. própria.** A [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg|parte 4]] diz que designer não é ilustrador; aqui ele incentiva montar a sua com formas ou trechos do unDraw. Não é contradição: o mockup é geométrico e copiado de uma foto, não desenho livre. Mas misturar trechos de outra biblioteca quebraria a regra de uma biblioteca só ([[wiki/concepts/consistencia-visual]]).

## Open Questions

- ~~**Autoria inferida.**~~ **Resolvido (2026-11-13):** o usuário confirmou que a aula é de [[wiki/entities/nasser|Násser]].
- **"skill-that" = "skill-depth" = SkewDat?** Aqui a legenda escreve "skill -that"; na aula anterior, "skill -depth". A pronúncia "skill-that" reforça o candidato `[external]` SkewDat (https://alternativeto.net/software/skewdat/about). Mantido literal no raw.
- **"paint-linear"**: a legenda diz "pent -linear". `[external]` O Figma exporta IDs como `paint0_linear_<id>`; a correção para "paint" tem confiança média.
- **"body-radius"** corrigido para border-radius (confiança média; no Figma o campo é "corner radius").
- **Onde ativa a régua** prometido e não dito na fala.
- `date_published` vazio.

## Raw Quotes

> "E o grande pulo do gato, galera, é porque você percebe que isso aqui são todas formas."

> "Ele pesa apenas 2KB [...] e você tem uma ilustração de qualidade, e que é muito, muito fiel, além de você ter resolução infinita."

> "Por ser estabelecido por código e ter tags HTML, que é um SVG, eu posso muito bem manipular eles via CSS, então meio que a magia do Motion surgiu daqui."

## Ver também

- [[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]] — aula anterior: isometria, "skill-depth" e export pelo frame
- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — abertura "W7": SVG com caminhos manipuláveis por CSS como base do motion
- [[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]] — aula seguinte: o que não sai de formas se traça com a Pen Tool e a Bend Tool
