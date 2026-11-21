---
type: concept
title: "WCAG (Web Content Accessibility Guidelines)"
aliases: ["Web Content Accessibility Guidelines", "diretrizes de acessibilidade ao conteúdo da web", "WCAG 2.1", "WCAG 2.2", "A AA AAA"]
date_created: 2026-11-15
date_updated: 2026-11-20
source_count: 3
tags: [acessibilidade, a11y, wcag, w3c, contraste, padronizacao, web]
skill: ux-ui-mentor
status: stub
---

# WCAG

"Diretrizes de acessibilidade ao conteúdo da web", no slide de [[wiki/sources/acessibilidade-wcag-contraste-textos-invisiveis-kiss-patterns]]. É a referência de [[wiki/concepts/acessibilidade]] citada na wiki: "inúmeras guidelines", tantas que "é difícil um website compreender a totalidade de regras". Por isso a aula escolhe as principais.

## Níveis A, AA e AAA

Na aula: "uma letra A, acessibilidade mínima; duas letras A, acessibilidade média; três letras A, acessibilidade alta". Násser mira "no mínimo" em AA e diz que AAA cabe a interfaces de governo de alcance massivo, como o auxílio emergencial. `[skill: ux-ui-mentor]` AA é o "padrão de mercado".

`[external]` Os níveis valem para cada critério de sucesso e para a conformidade da página. Em contraste, só há critérios AA (1.4.3) e AAA (1.4.6). Não há contraste de nível A, embora a aula fale em três notas "quando a gente fala de contraste de cor" (https://www.w3.org/TR/WCAG22/#contrast-minimum).

| Critério | Nível | Exigência |
|---|---|---|
| 1.4.1 Uso de cor | A | Não passar informação só pela cor (ver [[wiki/concepts/cor-semantica]]) |
| 1.4.3 Contraste mínimo | AA | 4.5:1 em texto normal; 3:1 em texto grande (≥ 18pt, ou 14pt em negrito) |
| 1.4.6 Contraste aprimorado | AAA | 7:1 e 4.5:1 |
| 1.4.11 Contraste não textual | AA | 3:1 em bordas de input e ícones informativos |
| 1.1.1 Conteúdo não textual | A | Alternativa em texto para imagens ([[wiki/concepts/texto-alternativo]]) |
| 2.5.8 Tamanho do alvo (mínimo) | AA (2.2) | 24×24 CSS px ([[wiki/concepts/area-clicavel]]) |

Fonte da tabela: `[skill: ux-ui-mentor]` (`references/usabilidade.md`, `references/design-acessibilidade.md`) e `[external]` WCAG 2.2 (https://www.w3.org/TR/WCAG22/).

## Princípios POUR

`[skill: ux-ui-mentor]` Perceptível, operável, compreensível e robusto. Ver [[wiki/concepts/acessibilidade]] para o que a aula cobre de cada um.

## Quem publica e quem obriga

`[external]` O WCAG é publicado pela WAI do [[wiki/entities/w3c]] e é uma recomendação, não uma lei. A aula fala em "muitas leis". Vira obrigação quando a legislação o adota: a LBI brasileira (Lei 13.146/2015, art. 63) exige acessibilidade em sites, e o eMAG do governo federal segue o WCAG.

## Ferramentas citadas

- [[wiki/entities/who-can-use]]: nota por tipo de visão simulada.
- Contrast Ratio: citado na aula, sem página própria. `[external]` Provavelmente o contrast-ratio.com de Lea Verou.

## AA é a meta (FrontPUSH, otimização aula 05)

Em [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]], o corpo de texto deve passar "no teste do AAA". O Lighthouse e a maioria das leis cobram AA (4,5:1 texto normal, 3:1 grande); AAA (7:1) é o extra.

## 2.2.2 e animações em loop (FrontPUSH, básico CSS aula 03)

Em [[wiki/sources/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode]], loops `infinite alternate` são o padrão do instrutor; o critério 2.2.2 (Pausar, parar, ocultar) pede mecanismo de pausa para movimento automático acima de 5 s.

## Key Sources

- [[wiki/sources/acessibilidade-wcag-contraste-textos-invisiveis-kiss-patterns]] — WCAG como fonte das recomendações; A/AA/AAA; AA como mínimo, AAA para governo
- [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]]: FrontPUSH, otimização aula 05: AA × AAA
- [[wiki/sources/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 03: loops infinitos e o critério 2.2.2
