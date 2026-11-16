---
type: concept
title: "Legibilidade e leiturabilidade"
aliases: ["legibilidade tipográfica", "legibility", "readability", "legibilidade", "leiturabilidade", "leitorabilidade", "fonte de corpo", "fonte de título"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 2
tags: [ui, ux, ui-design, tipografia, acessibilidade, legibilidade, hierarquia-visual]
skill: ux-ui-mentor
status: stub
---

# Legibilidade e leiturabilidade

Dois critérios de [[wiki/concepts/tipografia]] que costumam andar juntos e são diferentes: quão fácil é reconhecer as letras de uma fonte e quão fácil é ler um bloco de texto.

## Definições

`[skill: ux-ui-mentor]`
- **Legibilidade** (legibility): reconhecer cada caractere. Depende sobretudo da fonte.
- **Leiturabilidade** (readability): ler blocos de texto com facilidade. Depende de tamanho, entrelinha (1.5–1.6 no corpo), [[wiki/concepts/contraste]] e medida de linha (45–75 caracteres, `max-width: 65ch`).

Uma fonte pode ser legível e ter leiturabilidade ruim, como uma fonte display usada no corpo: legível num título, ruim como corpo.

A aula de classificações usa "legibilidade" para os dois sentidos ([[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]]).

## Na aula de classificações: a regra título x corpo

Em [[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]], a legibilidade decide onde cada [[wiki/concepts/classificacao-tipografica|classificação]] pode entrar:

- **Corpo em sem serifa:** "mais leves, mais neutras e modernas e terem boa legibilidade"; serve "tanto para títulos, como para textos".
- **Expressivas só em texto curto:** serifadas grossas, script, blackletter e display têm legibilidade "não tão boa assim"; vão para títulos, anúncios e [[wiki/concepts/botoes-em-interfaces|botões]], "para poder passar a ideia, passar o sentimento". "Não as coloque em corpo de texto."
- **Caso do convite:** nome dos noivos em script, corpo e endereço em sem serifa, "para o pessoal não se confunde". Uma letra lida como outra muda um endereço.

É uma divisão de papéis que reforça a [[wiki/concepts/hierarquia-visual]]: a fonte expressiva marca o título, a neutra carrega a leitura.

## Na aula de escala

É "a primeira coisa" ao definir uma [[wiki/concepts/escala-tipografica]], sobretudo nos corpos de texto, onde as fontes são menores. A regra geral é corpo de 14 a 21 px; o tamanho "também mexe na acessibilidade" ([[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]). A legenda de 10 px do NYT, citada na mesma aula, fica abaixo dos 12 px que a skill aceita para captions.

## Valores de corpo: aula x skill

`[skill: ux-ui-mentor]` Para corpo: 16 px no mínimo, line-height 1.5–1.6, 45–75 caracteres por linha (`max-width: 65ch`).

O piso diverge: a aula de escala aceita corpo a partir de 14 px ([[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]); a skill pede 16 px. Ver também [[wiki/concepts/altura-de-linha]] e [[wiki/concepts/largura-do-texto]] para as faixas de entrelinha e medida das aulas.

`[external]` A WCAG não define tamanho mínimo; exige ampliar o texto a 200% sem perda (1.4.4): https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html.

## Key Sources

- [[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]]: sem serifa no corpo, classificações expressivas só em texto curto
- [[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]: primeira preocupação da escala; corpo de 14 a 21 px
