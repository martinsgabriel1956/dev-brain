---
type: concept
title: "Razão de contraste"
aliases: ["contrast ratio", "razão de contraste WCAG", "contraste WCAG", "nota de contraste"]
date_created: 2026-11-15
date_updated: 2026-11-23
source_count: 3
tags: [ui, acessibilidade, wcag, contraste, cor, tipografia]
skill: ux-ui-mentor
status: stub
---

# Razão de contraste

Número que mede a diferença de [[wiki/concepts/luminosidade-das-cores|luminância]] entre a cor do texto e a do fundo. É o que checkers como o [[wiki/entities/who-can-use]] calculam. Na aula de [[wiki/entities/nasser|Násser]], é "uma nota de 0 a 21" que a WCAG "elaborou" para trabalhar o contraste de textos "abrangendo as dificuldades visuais" ([[wiki/sources/tipografia-e-cores-contraste-hierarquia-textual-cor-como-informacao]]).

## Como se calcula

`[external]` Razão = (L1 + 0,05) / (L2 + 0,05), com L1 a luminância relativa da cor mais clara. Vai de **1:1** (mesma cor) a **21:1** (preto no branco). Não existe 0 (https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

## Os limites

| Caso | AA | AAA |
|---|---|---|
| Texto normal | 4.5:1 | 7:1 |
| Texto grande | 3:1 | 4.5:1 |
| Componentes e ícones informativos (1.4.11) | 3:1 | — |

`[external]` "Grande" na WCAG é **18 pt (~24 px)** ou **14 pt (~18,7 px) em negrito**. `[skill: ux-ui-mentor]` A skill escreve "18px+ ou 14px bold"; a unidade certa é pt.

## As três notas da aula

O checker mostrado na aula colore o resultado: **vermelho** reprova; **laranja** passa só com peso e tamanho maiores ("em botões você pode utilizar, só que em corpo de texto é um pouco mais complicado"); verde passa. Corresponde a falhar, passar só em texto grande (3:1) e passar em texto normal (4.5:1). Leitura do agente: a faixa laranja não cobre um label comum de botão de 16 px, que não é "texto grande".

## Exemplo: o verde do FrontPUSH

O verde do [[wiki/entities/frontpush]] dá 1.65 contra o branco e reprova. O hex falado ("5F36A") tem cinco dígitos; `#5FE36A` é a única inserção de um dígito que dá ~1,65 (cálculo do agente: 1,66:1 no branco, 12,68:1 no preto). Por isso o botão verde leva texto preto.

## #999, #777 e #666 em branco (FrontPUSH, otimização aula 05)

Em [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]], a demonstração bate com as razões: #999 ≈ 2,8:1 (falha), #777 ≈ 4,5:1 (no limite do AA), #666 ≈ 5,7:1 (passa AA, falha AAA).

## Laranja de marca reprovado (FrontPUSH, mentoria de UI Design)

Na [[wiki/sources/frontpush-mentoria-ui-design-referencias-patterns-leitura-z-f-contraste|mentoria de UI Design]], o laranja com branco "falhou" no [[wiki/entities/who-can-use|Who Can Use]]. Saída sugerida: escurecer no HSB ([[wiki/concepts/modelo-de-cor-hsb]]); o tom mais escuro ainda falhou, porque a ferramenta "considera o pior caso", "uma tipografia pequena em corpo de texto". Negrito e tamanho maior melhoram. `[external]` É a diferença entre os limites de texto normal (4,5:1) e de texto grande (3:1, a partir de 24px, ou 18,66px em negrito) no WCAG 2.x (alta).

## Key Sources

- [[wiki/sources/tipografia-e-cores-contraste-hierarquia-textual-cor-como-informacao]] — nota de 0 a 21 (na verdade 1 a 21); notas vermelha, laranja e verde; verde do FrontPUSH a 1.65
- [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]]: FrontPUSH, otimização aula 05: razões dos cinzas da demonstração
- [[wiki/sources/frontpush-mentoria-ui-design-referencias-patterns-leitura-z-f-contraste]] — laranja + branco reprova; escurecer e engrossar o texto
