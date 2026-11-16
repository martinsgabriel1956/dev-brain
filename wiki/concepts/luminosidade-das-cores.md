---
type: concept
title: "Luminosidade das cores"
aliases: ["luminosidade da paleta de cores", "luminância relativa", "relative luminance", "brilho percebido das cores"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, cor, contraste, acessibilidade, wcag, paleta]
skill: ux-ui-mentor
status: stub
---

# Luminosidade das cores

Cores de mesma saturação não parecem igualmente claras: o olho é mais sensível ao verde e ao amarelo do que ao azul. Isso decide com que cor de texto cada cor da paleta combina.

## Na aula

Retomando o módulo de cores, [[wiki/entities/nasser|Násser]] lembra que o amarelo é "a mais clara do espectro visível" e o azul "o mais escuro"; ciano é muito claro e "em terceiro vem o verde". Por isso amarelo, ciano e verde têm dificuldade de dar [[wiki/concepts/contraste]] com branco, e "muito dessa característica se dá por ter muitas interfaces puxadas para o azul" ([[wiki/sources/tipografia-e-cores-contraste-hierarquia-textual-cor-como-informacao]]).

Primeiro passo antes de qualquer correção: "observe a luminosidade da paleta de cores". Depois vêm peso, escala, inversão e, por último, mexer na saturação ou no brilho da cor.

## A conta

`[external]` Luminância relativa WCAG: L = 0,2126 R + 0,7152 G + 0,0722 B, com R, G e B linearizados do sRGB (https://www.w3.org/TR/WCAG22/#dfn-relative-luminance). Para as cores puras: amarelo 0,93, ciano 0,79, verde 0,72, magenta 0,28, vermelho 0,21, azul 0,07 (cálculo do agente). A ordem da aula se confirma. É a base da [[wiki/concepts/razao-de-contraste]].

`[skill: ux-ui-mentor]` A skill monta paletas em OKLCH, em que o L é a luminosidade percebida: com L fixo, trocar o matiz não muda o contraste, coisa que HSL não garante.

## Key Sources

- [[wiki/sources/tipografia-e-cores-contraste-hierarquia-textual-cor-como-informacao]] — amarelo, ciano e verde claros; azul escuro; observar a luminosidade antes de escolher a cor do texto
