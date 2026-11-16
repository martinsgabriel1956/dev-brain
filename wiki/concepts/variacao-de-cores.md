---
type: concept
title: "Variação de cores"
aliases: ["tints and shades", "tons mais claros e mais escuros", "escala de cor", "color scale", "variação no HSB", "tint", "shade"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, cor, paleta, hsb, saturacao, brilho, matiz, design-tokens]
skill: ux-ui-mentor
status: stub
---

# Variação de cores

Gerar tons mais claros e mais escuros de uma cor da paleta sem quebrar a [[wiki/concepts/harmonia-visual|harmonia]]. É o que alimenta estados (hover, ativo), hierarquia, paletas monocromáticas, fundos e neutros tingidos.

## Para que serve

Em [[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]], Násser lista os usos:

- **Mudança de estado:** o botão no hover "vai ficar ou mais escuro ou mais claro" sem sair da paleta ([[wiki/concepts/feedback-do-sistema]]).
- **Hierarquia** e **paleta monocromática**, que depende de contraste entre claro e escuro do mesmo matiz.
- **Fundos e ilustrações** no mesmo matiz deixam o ambiente "mais harmonizado".
- **Neutros tingidos:** um pouco da cor de base no preto e no branco. O preto do Facebook "tem um pingo de azul" ([[wiki/entities/meta]]).

## A regra no HSB

| Direção | Brilho (B) | Saturação (S) | Matiz (H) |
|---|---|---|---|
| Mais claro | aumenta | diminui | opcional: girar para um matiz mais luminoso |
| Mais escuro | diminui | aumenta | opcional: girar para um matiz menos luminoso |

O slide chama isso de "variação diagonal": S e B andam em sentidos opostos. Mexer só no brilho "acontece", mas o resultado fica pior. Girar a matiz depende do [[wiki/concepts/padrao-de-luminosidade]], e o autor não recomenda: "sem mudar a matiz, já é sucesso".

`[external]` No HSB, misturar com branco já baixa S e sobe B; misturar com preto baixa só B. Subir a saturação no escuro é escolha para evitar tons "sujos", a mesma receita de guias como Refactoring UI e o "Color in UI Design" de Erik Kennedy.

## Na prática

- Ferramentas geram a escala a partir de uma cor. Násser usa poucos passos ("4 e 4", ou "3, 2"), com rotação de matiz perto de 0.
- `[skill: ux-ui-mentor]` Escala de primitivos (50–950) separada de tokens semânticos (`color-brand-hover`, `color-surface`). Em **OKLCH**, mudar só o L dá passos de brilho perceptualmente iguais entre matizes, o que resolve no espaço de cor o que a aula faz girando matiz.
- Sombras não devem ser pretas: sobre fundo colorido, a sombra é a mesma cor mais escura (artigo citado na aula). Ver também a sombra de hover na cor do botão em [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]].

## Key Sources

- [[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]] — usos, regra brilho x saturação, girar o Hue, ferramenta geradora
