---
type: concept
title: "Paleta de cores"
aliases: ["paleta de cor", "color palette", "esquema de cores", "cores complementares", "paleta monocromática", "paleta análoga", "cor de base", "cor de destaque"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, cor, paleta-de-cores, style-guide, design-tokens]
skill: ux-ui-mentor
status: stub
---

# Paleta de cores

Conjunto de cores de uma interface, cada uma com um papel, mais as variações de cada uma. Na aula prática de [[wiki/entities/nasser|Násser]], a paleta nasce de um esquema e de papéis ([[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]]).

## Esquemas da aula

| Esquema | Como é | Exemplo da aula |
|---|---|---|
| Complementar | duas matizes opostas | roxo e amarelo, azul e laranja, salmão e verde |
| Neutra + uma cor | uma cor sobre base neutra | [[wiki/entities/nubank]] (roxo e branco); os cursos do autor (preto + uma cor + gradiente) |
| Monocromática | uma matiz, vários tons | azul do [[wiki/entities/frontpush]] nos [[wiki/concepts/elementos-de-composicao]] |
| Análoga | matizes vizinhas | só citada |

## Papéis

- **Cor de base:** a identidade (o roxo).
- **Cor de destaque:** a que chama atenção; na complementar, "o amarelo se destaca muito bem no roxo". Ver [[wiki/concepts/contraste]] e [[wiki/concepts/hierarquia-visual]].
- **Neutro claro:** F1/F2, "que ela não seja o branco chapado".
- **Neutro escuro:** 30 30 30 ou 20 20 20.

Cada papel ganha uma escala ([[wiki/concepts/variacao-tonal-de-cor]]), e os neutros levam um pouco da matiz da base ([[wiki/concepts/neutros-tingidos]]). As cores saem de referências ([[wiki/concepts/repertorio]]) e se ajustam no [[wiki/concepts/modelo-de-cor-hsb]].

## Da paleta ao sistema

A paleta é o primeiro passo do style guide, para "aplicar estilos de maneira ordenada e organizada" e manter a [[wiki/concepts/consistencia-visual]].

`[skill: ux-ui-mentor]` Em código, três camadas: primitivos (`purple-50…950`), semânticos (`color-brand`, `color-background`, `color-text-primary`) e, se preciso, de componente. Componente nunca usa primitivo direto. Cores de estado ficam em [[wiki/concepts/cor-semantica]].

## Key Sources

- [[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]] — esquemas, base e destaque, neutros F1/F2 e 20–30
