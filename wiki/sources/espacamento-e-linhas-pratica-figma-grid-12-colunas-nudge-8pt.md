---
type: source
title: "Espaçamento e linhas na prática no Figma: grid de 12 colunas, nudge de 8pt e medição com Alt"
aliases: ["aula prática de espaçamento no Figma", "nudge de 8pt", "big nudge 8", "grid de 12 colunas aula", "medir distância com Alt no Figma"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, elementos-da-interface, espacamento, figma, grid, grid-de-colunas, escala-de-espacamento, grid-de-8-pontos, consistencia, hierarquia-visual, wireframe, line-height]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Espaçamento e linhas na prática no Figma: grid de 12 colunas, nudge de 8pt e medição com Alt

## TL;DR

A prática prometida em [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]]. O autor bagunça de propósito um [[wiki/concepts/wireframe]] da futura seção de interface web e o realinha no [[wiki/entities/figma]] em quatro passos: (1) **[[wiki/concepts/grid-de-colunas|grid de 12 colunas]]** no desktop, porque 12 divide por 2, 3, 4 e 6 (72 de largura por coluna, gutter de 32, centralizado); (2) **big nudge de 8pt** em Preferences → Nudge amount, para que Shift + seta mova de 8 em 8; (3) **Alt** com o mouse sobre outro elemento para medir a distância; (4) a [[wiki/concepts/escala-de-espacamento|escala geométrica]] 2, 4, 8, 16, 32, 64 aplicada como [[wiki/concepts/hierarquia-visual|hierarquia]]: 16 dentro do grupo, 32 entre grupos, 128 entre blocos. Ressalva: a medição em texto inclui o line-height, assunto da aula de [[wiki/concepts/tipografia]].

## Key Claims

### Antes de começar

- **Quem não sabe nada de Figma deve ver antes um vídeo do autor no YouTube** com "o basicão do basicão do basicão"; o curso também vai passo a passo.
- **O exemplo vem da seção de wireframes**, que fica na parte de interface web do curso, onde o tema será tratado "com mais veemência".

### Grid de 12 colunas

- **A primeira coisa a alinhar é o grid**: "colunas, réguas para poder a gente ajustar o conteúdo dentro da nossa página". Ver [[wiki/concepts/grid-de-colunas]].
- **Desktop usa "por padrão sempre 12 colunas"**, porque 12 "é um número com bons múltiplos": divide por 2, 3, 4 e 6.
- **Configuração da aula:** 12 colunas, 72 de largura cada, gutter de 32 ("o espaço entre cada coluna"), centralizado. Conta do agente: 12 × 72 + 11 × 32 = 1216 de largura de conteúdo.
- **O headline fica "coladinho" com a primeira coluna.**

### Nudge de 8pt e medição com Alt

- **Configure o sistema no Figma**: menu → Preferences → Nudge amount, big nudge = 8pt. Com isso, Shift + seta move o elemento de 8 em 8. `[external]` A ajuda do Figma confirma o diálogo com Small nudge e Big nudge (padrões 1 e 10, em pontos independentes de resolução) e que Shift troca o small pelo big nudge: https://help.figma.com/hc/en-us/articles/4404575206295-Set-small-and-big-nudge-values.
- **Alt mede distâncias**: com um elemento selecionado, segurar Alt e passar o mouse sobre outro mostra a distância entre eles. Clique em apenas um elemento; com os dois selecionados não funciona (o autor erra e corrige ao vivo).
- **Escala da aula: geométrica 2, 4, 8, 16, 32, 64, com passo 8 no teclado**, "porque o 8 é múltiplo de todos esses números". Ver a ressalva em Tensões.

### Aplicando a hierarquia

- **Agrupe antes de medir** (Ctrl + G): título e texto viram um grupo; o item e o texto ao lado, outro.
- **Texto engana na medição:** entre título e descrição o Alt mostrou 17, porque a caixa de texto "também leva em consideração o tamanho do line-height". O autor ajusta para 16 mesmo assim, já que a aula é "a parte mais operacional".
- **Mesma relação, mesma distância:** 16 entre título e descrição e 16 entre os itens da lista, "para poder manter a consistência". Ver [[wiki/concepts/consistencia-visual]].
- **Mais distância para o que está mais alto na hierarquia:** 32 entre o bloco de texto e a lista; 32 também entre os dois grupos maiores; 128 (64 + 64) entre a seção e o bloco seguinte, ajustado a partir de 160 com Shift + seta.
- **Distribuição horizontal:** com os elementos alinhados na horizontal e selecionados, o autor digita 128 de distância e eles ficam "igualmente separados" e alinhados ao grid.
- **"Melhora bastante"**: o antes e depois serve de prova; não há outra métrica.

## Entities

- [[wiki/entities/nasser]]: autor, confirmado pelo usuário em 2026-11-13 (o nome não é dito na aula). Fala do "meu" vídeo no YouTube e do material do curso.
- [[wiki/entities/figma]]: ferramenta da aula (grid, Nudge amount, Alt, Ctrl + G, distribuição).
- Sem página própria: YouTube (vídeo de Figma básico do autor).

## Concepts

- [[wiki/concepts/grid-de-colunas]] (novo)
- [[wiki/concepts/escala-de-espacamento]]
- [[wiki/concepts/grid-de-8-pontos]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/lei-da-proximidade-gestalt]]
- [[wiki/concepts/espaco-em-branco]]
- [[wiki/concepts/wireframe]]
- [[wiki/concepts/tipografia]]
- [[wiki/concepts/densidade-de-informacao]]

## Tensões com a wiki

- **"8 é múltiplo de todos esses números".** Não é: 8 é múltiplo de 2 e 4; 16, 32 e 64 é que são múltiplos de 8. O que a aula quer dizer funciona assim mesmo: com passo 8, todos os valores a partir de 8 (16, 32, 64, 128) se alcançam com Shift + seta; 2 e 4 ficam para a seta sem Shift, se o small nudge for 1 ou 2. Ressalva do agente.
- **Geométrica na teoria, 128 na prática.** A escala falada vai até 64; o vão entre blocos é 128 (64 + 64), que segue dobrando. Coerente com a preferência da aula anterior. `[skill: ux-ui-mentor]` A escala de referência da skill para quando a geométrica fica esparsa: 4, 8, 16, 24, 32, 48, 64. Ver [[wiki/concepts/escala-de-espacamento]].
- **Gutter de 32 x skill.** `[skill: ux-ui-mentor]` A tabela de grids da skill dá, para desktop (1024–1440 px), 12 colunas com gutter de 24 e margem de 32; gutter de 32 aparece só em telas largas (> 1440 px), com max-width centralizado. A aula não fala de breakpoint nem de margem. Ver [[wiki/concepts/grid-de-colunas]].
- **Medir texto.** O 17 em vez de 16 vem da caixa de texto, que inclui o espaço do line-height acima e abaixo das letras. `[skill: ux-ui-mentor]` A skill usa o sub-grid de 4 para line-height e ajustes finos. Ajustar o vão da caixa para 16, como na aula, deixa o vão visual entre as letras um pouco maior que 16. Inferência do agente; o autor adia o tema para tipografia.
- **Grid prometido.** Em [[wiki/sources/elementos-da-interface-introducao-ui-design]] o grid ficou para outra aula; aqui ele aparece só de forma operacional e o tratamento completo volta a ser adiado para a parte de interface web.

## Open Questions

- Qual é o vídeo de Figma básico no YouTube?
- Os 72 de coluna e 32 de gutter valem para qual largura de frame? 1216 de conteúdo cabe num frame de 1440 com margens de 112, mas a aula não diz.
- "43, 35 e aí eu só subo 3": o 43 provavelmente é 40 (32 + 8) mal transcrito; mantido literal no raw.
- `date_published` vazio.

## Raw Quotes

> "Na interface desktop a gente usa por padrão sempre 12 colunas."

> "Sempre que você apertar shift para cima ou para baixo, ele vai se mover de 8pt em 8pt."

> "Muito cuidado ao aplicar essa distância em textos."
