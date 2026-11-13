---
type: concept
title: "Border Radius"
aliases: ["radius", "raio de borda", "cantos arredondados", "arredondamento", "8-radius"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 5
tags: [ui, ui-design, formas, border-radius, consistencia, design-tokens, botao]
skill: ux-ui-mentor
status: stub
---

# Border Radius

O raio dos cantos de botões, cards, inputs e ícones. É a alavanca mais direta das [[wiki/concepts/formas-geometricas-e-organicas|formas]]: a mesma caixa, reta ou arredondada, comunica coisas diferentes ([[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]]).

## Uma escala de proximidade

[[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]] dá valores concretos:

| Radius | Leitura | Exemplo |
|---|---|---|
| 0 (reto) | Exato, distante; confiança racional | Sites de arquitetura |
| 3–4 px | Racional, levemente suavizado | [[wiki/entities/spider-man-projeto-nasser]] (com elementos inclinados); FrontPUSH antigo |
| 8 px | Meio-termo: racional e amigável, sem perder seriedade | [[wiki/entities/frontpush]] |
| Mais que 8 / pill | Amigável, próximo | [[wiki/entities/creatorpush]]; botão da página do [[wiki/entities/nubank]] (inferido) |

Para Násser, arredondar aproxima o usuário, mas proximidade demais "não transmite seriedade". O valor foi achado testando (4, depois 8) e olhando "de longe" com a cor da marca aplicada.

## Um valor para tudo

Escolhido o radius do botão, ele vale para cards, ícones e demais elementos. Botão arredondado com ícones retos é "uma quebra" de [[wiki/concepts/consistencia-visual]] ([[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]]).

## Olhar de dev

`[skill: ux-ui-mentor]` O radius vira token semântico (`--radius-button`, `--radius-card`) que os componentes consomem, nunca um `border-radius: 6px` solto. Em multi-brand theming, é um dos tokens sobrescritos por marca (`--radius-card: 8px` numa, `0px` noutra), junto com cor e família tipográfica. É o caso FrontPUSH × Creator Push: mesma fonte, radius diferente.

## Arredondar para aproximar

O [[wiki/entities/nubank]] "deu uma amenizada arredondando as bordas" de uma seção muito geométrica; bordas mais arredondadas trazem "um pouco mais perto da pessoa" ([[wiki/sources/formas-geometricas-organicas-exemplos-dropbox-madero-coco-bambu-nubank]]).

## Radius de botões

Em [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]: primário e secundário com "exatamente a mesma" bordinha arredondada; no slide, 16 px nos três tokens de botão. Ver [[wiki/concepts/botoes-em-interfaces]].

## Do reto ao pill nos botões

Em [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]]: reto (0) passa seriedade e serve de contraste em sites orgânicos (Madero); arredondado é o "ótimo coringa"; circular (pill) "traz mais para perto". O [[wiki/entities/nubank]] usa botões e links "totalmente circulares", o que confirma a linha "pill (inferido)" da tabela acima. Chanfrado, diagonal e hexagonal saem da escala de raio ([[wiki/concepts/formas-de-botoes]]).

## Key Sources

- [[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]] — arredondado vs. reto muda a mensagem
- [[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]] — 8 px no FrontPUSH, 3–4 px no Spider-Man, mais redondo no Creator Push
- [[wiki/sources/formas-geometricas-organicas-exemplos-dropbox-madero-coco-bambu-nubank]] — Nubank arredonda bordas para aproximar
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — mesmo radius em primário e secundário (16 px no slide)
- [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]] — reto, arredondado e circular nos botões; Nubank totalmente circular
