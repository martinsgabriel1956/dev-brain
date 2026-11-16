---
type: concept
title: "Padrão de luminosidade"
aliases: ["luminosidade das cores", "luminosidade por matiz", "brilho percebido", "perceived lightness", "luma", "luminância relativa"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, cor, luminosidade, matiz, contraste, acessibilidade, oklch]
skill: ux-ui-mentor
status: stub
---

# Padrão de luminosidade

Cada matiz carrega um brilho próprio, mesmo com saturação e brilho no máximo. Amarelo puro parece quase branco; azul puro parece quase preto.

## Os valores da aula

Em [[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]], Násser pinta o ciclo cromático numa barra e muda o tipo de layer para luminosity ([[wiki/concepts/blend-modes]]) no [[wiki/entities/figma]]. Valores aproximados do slide:

| Matiz | Luminosidade |
|---|---|
| Amarelo | 89% |
| Ciano | 70% |
| Verde | 60% |
| Rosa (magenta) | 41% |
| Vermelho | 31% |
| Azul | 11% |

Consequências tiradas na aula:

- **Branco sobre amarelo** (ou ciano) quase não se lê: os dois já são claros. Ele deixa o texto ao lado do logo amarelo em preto.
- **Azul** é "um dos mais queridos" para fundo: já é escuro e dá o maior [[wiki/concepts/contraste]] com texto claro.
- **Girar a matiz** dá um tom mais claro quando o brilho já está em 100 (ou mais escuro, no amarelo). O autor mostra, mas não recomenda ([[wiki/concepts/variacao-de-cores]]).

## De onde vêm os números

`[external]` São os pesos da luma Rec. 601: Y' = 0,299 R + 0,587 G + 0,114 B (vermelho 30%, verde 59%, azul 11%; amarelo = R + G = 89%; ciano = G + B = 70%; magenta = R + B = 41%). É a fórmula de "color brightness" do W3C AERT (https://www.w3.org/TR/AERT/#color-contrast) e reflete a sensibilidade do olho, maior no verde.

Para contraste, a WCAG usa a luminância relativa, com canais linearizados e pesos Rec. 709 (0,2126 / 0,7152 / 0,0722): amarelo puro dá cerca de 93%, azul 7% (https://www.w3.org/TR/WCAG22/#dfn-relative-luminance). A ordem dos matizes não muda.

`[skill: ux-ui-mentor]` HSL e HSB ignoram esse padrão: "azul e amarelo com o mesmo L parecem ter brilhos diferentes". OKLCH é perceptualmente uniforme, então o mesmo L dá o mesmo brilho percebido em qualquer matiz.

## Key Sources

- [[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]] — barra do espectro em modo luminosity; amarelo 89%, azul 11%
