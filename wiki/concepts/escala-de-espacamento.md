---
type: concept
title: "Escala de Espaçamento"
aliases: ["sistema de espaçamento", "spacing system", "escala linear", "escala geométrica", "spacing tokens"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 4
tags: [ui, ui-design, layout, espacamento, escala-de-espacamento, consistencia, design-tokens, grid-de-8-pontos]
skill: ux-ui-mentor
status: stub
---

# Escala de Espaçamento

Conjunto fechado de valores de espaçamento usado em toda a interface, para que nenhum vão seja escolhido no olho. É a [[wiki/concepts/consistencia-visual]] aplicada a medidas: "o nosso sistema precisa ter consistência em todo ele" ([[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]]).

## Fixo ou por porcentagem

O sistema pode ser fixo ou por porcentagem, relativo ao elemento pai. A aula trata só do fixo.

## Linear x geométrica

- **Linear:** soma sempre o mesmo passo. Passo 2: 2, 4, 6, 8, 10, 12, 14... Passo 8: 10, 18, 26...
- **Geométrica:** "soma com o anterior", ou seja, dobra: 2, 4, 8, 16, 32, 64...
- **O autor prefere a geométrica:** de 16 para 32 e de 32 para 64 a diferença se vê; de 10 para 12 quase não. Valores altos de uma escala linear ficam próximos demais para comunicar coisas diferentes.

Inferência (não está na aula): o argumento é perceptual. A diferença que o olho nota é relativa ao tamanho, então passos constantes encolhem em proporção conforme o valor sobe (de 10 para 12 são 20%; de 50 para 52, 4%).

## Na prática: escalas híbridas

O [[wiki/concepts/grid-de-8-pontos]] da aula de whitespace (16, 24, 32, 40, 48, 56...) é linear com passo 8, com 18, 28 e 36 por bom senso ([[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]). As duas aulas parecem ser de edições diferentes do curso.

`[skill: ux-ui-mentor]` A escala de referência da skill fica no meio: 4, 8, 16, 24, 32, 48, 64. Dobra nos valores baixos e põe 24 e 48 entre as potências de 2, porque de 32 a 64 o salto é grande demais para gap entre cards ou padding de seção. Base 8 porque divide por 2 e 4 em inteiros; 4 como sub-grid para ajustes finos.

`[skill: ux-ui-mentor]` Na implementação, a escala vira tokens (`--space-1: 4px`, `--space-2: 8px`...) e os componentes só consomem tokens. Densidade (compacto/confortável) troca os valores resolvidos, não a escala; ver [[wiki/concepts/densidade-de-informacao]].

## Relação com outros conceitos

- [[wiki/concepts/espaco-em-branco]] — a escala diz quanto espaço; o espaço em branco diz para quê.
- [[wiki/concepts/lei-da-proximidade-gestalt]] — os valores menores agrupam, os maiores separam; a escala garante que a diferença se perceba.

## Aplicada como hierarquia

Na prática ([[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]): 16 dentro do grupo (título e descrição; itens da lista), 32 entre grupos, 128 (64 + 64) entre blocos. A escala falada para em 64, mas o vão maior segue dobrando. A aula diz que "o 8 é múltiplo de todos esses números"; na verdade 8 é múltiplo de 2 e 4, e 16, 32, 64 é que são múltiplos de 8 (ressalva do agente).

## Padding de botões

Em [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]: o padding do botão vem "do sistema adotado", "não é qualquer valor aleatório", e é o mesmo em todos os botões. O slide lista 2, 4, 8, 16, 32, 64; a fala diz "2, 4, 6, 8, 32, 64" (provável lapso). Ver [[wiki/concepts/botoes-em-interfaces]].

## Key Sources

- [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]] — sistema fixo ou por porcentagem; linear x geométrica; preferência pela geométrica
- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]] — grid de 8 como escala de "bons números"
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — 16 / 32 / 128 aplicados como hierarquia no Figma
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — padding de botão tirado da escala (2, 4, 8, 16, 32, 64)
