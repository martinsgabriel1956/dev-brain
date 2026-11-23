---
type: concept
title: "Luminosidade das cores"
aliases: ["padrão de luminosidade", "Padrão de luminosidade", "luminosidade da paleta de cores", "luminosidade por matiz", "brilho percebido", "brilho percebido das cores", "perceived lightness", "luma", "luminância relativa", "relative luminance"]
date_created: 2026-11-15
date_updated: 2026-11-23
source_count: 4
tags: [ui, ui-design, cor, luminosidade, matiz, contraste, acessibilidade, wcag, oklch, paleta]
skill: ux-ui-mentor
status: stub
---

# Luminosidade das cores

Cada matiz carrega um brilho próprio, mesmo com saturação e brilho no máximo: cores de mesma saturação não parecem igualmente claras. Amarelo puro parece quase branco; azul puro parece quase preto. O olho é mais sensível ao verde e ao amarelo do que ao azul. Isso decide com que cor de texto cada cor da paleta combina.

## Os valores da aula de variação

Em [[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]], [[wiki/entities/nasser|Násser]] pinta o ciclo cromático numa barra e muda o tipo de layer para luminosity ([[wiki/concepts/blend-modes]]) no [[wiki/entities/figma]]. Valores aproximados do slide:

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

## Na aula de tipografia e cores

Retomando o módulo de cores, Násser lembra que o amarelo é "a mais clara do espectro visível" e o azul "o mais escuro"; ciano é muito claro e "em terceiro vem o verde". Por isso amarelo, ciano e verde têm dificuldade de dar [[wiki/concepts/contraste]] com branco, e "muito dessa característica se dá por ter muitas interfaces puxadas para o azul" ([[wiki/sources/tipografia-e-cores-contraste-hierarquia-textual-cor-como-informacao]]).

Primeiro passo antes de qualquer correção: "observe a luminosidade da paleta de cores". Depois vêm peso, escala, inversão e, por último, mexer na saturação ou no brilho da cor.

## A conta: duas fórmulas, a mesma ordem

Os números do slide e os da WCAG diferem porque vêm de fórmulas diferentes. A ordem dos matizes é a mesma nas duas, e bate com a da aula de tipografia.

- **Luma (slide).** `[external]` São os pesos da luma Rec. 601: Y' = 0,299 R + 0,587 G + 0,114 B (vermelho 30%, verde 59%, azul 11%; amarelo = R + G = 89%; ciano = G + B = 70%; magenta = R + B = 41%). É a fórmula de "color brightness" do W3C AERT (https://www.w3.org/TR/AERT/#color-contrast) e reflete a sensibilidade do olho, maior no verde.
- **Luminância relativa (WCAG).** `[external]` L = 0,2126 R + 0,7152 G + 0,0722 B, com R, G e B linearizados do sRGB e pesos Rec. 709 (https://www.w3.org/TR/WCAG22/#dfn-relative-luminance). Para as cores puras: amarelo 0,93, ciano 0,79, verde 0,72, magenta 0,28, vermelho 0,21, azul 0,07 (cálculo do agente). É a base da [[wiki/concepts/razao-de-contraste]].

| Matiz | Luma Rec. 601 (slide) | Luminância relativa WCAG |
|---|---|---|
| Amarelo | 89% | 93% |
| Ciano | 70% | 79% |
| Verde | 60% | 72% |
| Magenta | 41% | 28% |
| Vermelho | 31% | 21% |
| Azul | 11% | 7% |

## Olhar de dev

`[skill: ux-ui-mentor]` HSL e HSB ignoram esse padrão: "azul e amarelo com o mesmo L parecem ter brilhos diferentes". A skill monta paletas em OKLCH, em que o L é a luminosidade percebida e o espaço é perceptualmente uniforme: com L fixo, o mesmo L dá o mesmo brilho percebido em qualquer matiz, e trocar o matiz não muda o contraste, coisa que HSL não garante.

## Extremos para contraste (FrontPUSH, mentoria de ID visual)

Na [[wiki/sources/frontpush-mentoria-identidade-visual-marca-minimalista-gradiente-paleta-tipografia|mentoria de identidade visual]]: "para você conseguir contraste, é bom você ir para os extremos". Nina Talks usa azul ("o trecho [...] mais escuro") e branco, e o rosa ("30%, 40%", "no meio") só como destaque, nunca de fundo. Valores ditos: vermelho 30% a 40%, amarelo 80%; diferem dos 89% do amarelo da aula de variação, e o rosa deveria ser mais claro que o vermelho (inferência).

## Na mentoria de UI Design (FrontPUSH)

Na [[wiki/sources/frontpush-mentoria-ui-design-referencias-patterns-leitura-z-f-contraste|mentoria de UI Design]]: "o azul tem de 11% de luminosidade, quando eu vou para o amarelo, ele tem de 80%", e o verde "60%", "na meiuca". Azul e verde batem com a luma Rec. 601 da tabela acima; o amarelo "80%" é lapso (89%), o mesmo da mentoria de identidade visual. Daí as três cores de fundo dominantes (branco, preto, azul-escuro) e o veto a texto branco no amarelo, "o menor contraste possível que existe".

## Key Sources

- [[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]] — barra do espectro em modo luminosity; amarelo 89%, azul 11%
- [[wiki/sources/tipografia-e-cores-contraste-hierarquia-textual-cor-como-informacao]] — amarelo, ciano e verde claros; azul escuro; observar a luminosidade antes de escolher a cor do texto
- [[wiki/sources/frontpush-mentoria-identidade-visual-marca-minimalista-gradiente-paleta-tipografia]]: extremos de luminosidade; rosa no meio; números divergentes
- [[wiki/sources/frontpush-mentoria-ui-design-referencias-patterns-leitura-z-f-contraste]] — azul 11%, amarelo "80%" (lapso), verde 60%; três cores de fundo
