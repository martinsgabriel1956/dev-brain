---
type: concept
title: "Neutros tingidos"
aliases: ["cor de base nas cores neutras", "tinted neutrals", "cinzas com matiz", "branco tingido", "escala de cinza", "escada de cinza"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, cor, cores-neutras, paleta-de-cores, harmonia, blend-modes]
skill: ux-ui-mentor
status: stub
---

# Neutros tingidos

Branco, cinzas e preto que carregam um pouco da matiz da cor de base, em vez de saturação zero. Para [[wiki/entities/nasser|Násser]], "isso faz com que a nossa interface seja mais harmônica" ([[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]]). Ver [[wiki/concepts/harmonia-visual]].

## Dois métodos da aula

1. **Overlay:** copiar a cor de base, pôr em modo overlay sobre o neutro e trazer para a frente ([[wiki/concepts/blend-modes]]). No branco, fica "bem clarinho"; no preto, a saturação sobe demais e ele baixa a opacidade (50% → saturação 22; 10% → saturação 9).
2. **HSB direto:** pôr o neutro na matiz da base (247/245 para o roxo) e dar "um pouquinho de saturação" (cerca de 4). Ver [[wiki/concepts/modelo-de-cor-hsb]].

Depois, a mesma [[wiki/concepts/variacao-de-cores]], com passos menores: brilho de 3 em 3 e saturação de 1 em 1.

## Escada de cinza

No escuro, a cor de composição fica "por volta de um A, um F, ou então dois" (leitura provável: 1A, 1F ou 20 por canal em hex), e as vizinhas sobem e descem em escadinha.

`[external]` Overlay sobre branco puro (FFFFFF) não muda nada: a fórmula usa *screen* quando o fundo é claro e devolve 1,0 (https://www.w3.org/TR/compositing-1/#blendingoverlay). O tingimento da aula aparece porque o branco de partida já é F1/F2.

`[skill: ux-ui-mentor]` A skill usa o mesmo princípio em tokens: fundo `oklch(0.99 0.005 80)`, texto `oklch(0.15 0.01 250)`, croma baixo, não zero. No dark mode, superfícies mais elevadas ganham luminosidade, não sombra.

## Key Sources

- [[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]] — overlay ou HSB com a matiz da base; passos menores; preto em escada
