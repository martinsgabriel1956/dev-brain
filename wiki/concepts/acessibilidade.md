---
type: concept
title: "Acessibilidade (em interfaces)"
aliases: ["a11y", "acessibilidade digital", "acessibilidade web", "design acessível", "design inclusivo", "accessibility"]
date_created: 2026-11-15
date_updated: 2026-11-16
source_count: 4
tags: [acessibilidade, a11y, ux, ui-design, wcag, contraste, alt-text, carga-cognitiva, html-semantico]
skill: ux-ui-mentor
status: stub
---

# Acessibilidade

Projetar para que qualquer pessoa use o produto, incluindo quem tem deficiência ou "imparidade" auditiva, motora ou cognitiva. O ponto de partida em [[wiki/sources/acessibilidade-wcag-contraste-textos-invisiveis-kiss-patterns]] é que "nós não somos quem vai utilizar aquele produto". O conceito "se agrega e muito" à usabilidade, e a referência é o [[wiki/concepts/wcag]].

## As quatro recomendações da aula

[[wiki/entities/nasser|Násser]] não tenta cobrir o WCAG inteiro ("muito texto e muitas leis") e fica com quatro pontos:

1. **[[wiki/concepts/contraste|Contraste de cor]]**: distinguir elementos, garantir legibilidade e guiar a jornada. Mire no mínimo em AA e reserve AAA para serviços de massa, como os de governo. Checkers: Contrast Ratio e [[wiki/entities/who-can-use]].
2. **Textos invisíveis**: descrições em imagens para o text-to-speech ([[wiki/concepts/texto-alternativo]]).
3. **[[wiki/concepts/kiss|KISS]]**: passo a passo, com [[wiki/concepts/feedback-do-sistema|feedback]], confirmação visual, ícones e cor bem usada.
4. **Patterns**: soluções consagradas reduzem a [[wiki/concepts/carga-cognitiva]] ([[wiki/concepts/padroes-de-interface]], [[wiki/concepts/lei-de-jakob]]). Para UI, os UI Kits e as guidelines das big techs.

Aulas anteriores do mesmo curso já tratavam a acessibilidade como contraste para idosos ([[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]]), como "uso de patterns" e feedback ([[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]]), como alt text ([[wiki/concepts/texto-alternativo]]) e como área de toque ([[wiki/concepts/area-clicavel]]).

## O que a aula não cobre

`[skill: ux-ui-mentor]` Os quatro princípios do WCAG são **POUR**: perceptível, operável, compreensível e robusto. A aula fica em perceptível (contraste, alt) e compreensível (KISS, patterns). Faltam três pontos de "operável" e "robusto":

- **Teclado e foco visível**: `outline: none` sem substituto viola o WCAG; o indicador de foco pede 3:1 contra o fundo.
- **Leitor de tela e semântica**: `<label>` em todo input, `aria-describedby` para erros, `aria-label` em ícone funcional.
- **Movimento**: respeitar `prefers-reduced-motion`.

Acessibilidade cognitiva (progressive disclosure, chunking, linguagem simples) "beneficia [...] todos em algum momento", o que dá razão ao argumento de KISS e patterns da aula.

## HTML semântico

`[external]` A aula de box model do [[wiki/entities/frontpush|FrontPUSH]] recomenda [[wiki/concepts/html-semantico|tags semânticas]] só pelo Google; o ganho mais documentado é de acessibilidade: header, nav, main e footer viram landmarks para leitores de tela (https://developer.mozilla.org/en-US/docs/Glossary/Semantics) ([[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]]).

## Key Sources

- [[wiki/sources/acessibilidade-wcag-contraste-textos-invisiveis-kiss-patterns]] — aula dedicada: nós não somos o usuário; contraste A/AA/AAA; textos invisíveis; KISS; patterns e guidelines
- [[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]] — tags semânticas (motivo dado: SEO; ganho documentado: landmarks)
