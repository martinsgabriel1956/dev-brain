---
type: concept
title: "Variação tonal de cor"
aliases: ["variação de cores", "tons mais claros e mais escuros", "tints and shades", "escala de cor", "color scale", "rampa de cor"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, cor, paleta-de-cores, hsb, design-tokens]
skill: ux-ui-mentor
status: stub
---

# Variação tonal de cor

Gerar tons mais claros e mais escuros de uma mesma cor para compor a [[wiki/concepts/paleta-de-cores]]. A receita de [[wiki/entities/nasser|Násser]], no [[wiki/concepts/modelo-de-cor-hsb]] ([[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]]):

| Direção | Brilho | Saturação | Exemplo da aula (base B78) |
|---|---|---|---|
| Mais escuro | −10 a 15 pontos | sobe, "não necessariamente na mesma proporção" | B62; depois B50 com S67–68 |
| Mais claro | sobe | cerca de −10 pontos | B90; depois B96–97 com S30 |
| Neutros | passos de ~3 | ±1 por passo | branco 98 → 95 → 92; 99/S3, 100/S2 |

## Por que mexer nos dois

Só baixar o brilho dá um tom "próximo" demais, quase imperceptível; baixar o brilho e subir a saturação "fica mais natural" e mais distinto. No branco, os passos são menores porque "qualquer mudança no branco, a diferença é bem mais acentuada" ([[wiki/concepts/neutros-tingidos]]).

## Conferir com ferramenta

A escala manual foi posta ao lado da gerada por uma ferramenta (não nomeada, de uma aula anterior) e ficou "muito próxima". O processo manual ensina o conceito; a ferramenta acelera. "Isso tudo galera é muito, muito, muito de um teste."

`[skill: ux-ui-mentor]` A escala vira primitivos (`purple-100…900`). Em OKLCH, variar só L dá passos de brilho percebido iguais entre matizes, o que a receita em HSB não garante.

## Key Sources

- [[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]] — brilho para baixo e saturação para cima; conferência com ferramenta
