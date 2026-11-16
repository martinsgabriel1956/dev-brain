---
type: concept
title: "HTML semântico (tags semânticas do HTML5)"
aliases: ["tags semânticas", "semantic HTML", "HTML5 semântico", "elementos semânticos"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [html, html5, semantica, seo, acessibilidade, frontend]
skill: tech-mentor-frontend
status: stub
---

# HTML semântico (tags semânticas do HTML5)

Usar a tag que descreve o **papel** do conteúdo, não só o seu visual: `header` (cabeçalho), `nav` (barra de navegação, conteúdo de links), `section` (trecho de conteúdo), `article` (conteúdo mais textual, autônomo), `figure` (imagem), `footer` (rodapé). Chegaram com o HTML5; antes, a interface era montada quase toda com `div` ([[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]]).

## Visual igual, significado diferente

Para [[wiki/entities/nasser|Násser]], trocar `div` por `section` ou `header` "não faz diferença nenhuma, absolutamente nenhuma visualmente": toda tag é uma caixa do [[wiki/concepts/box-model]]. "A diferença está na semântica", uma boa prática. O motivo que ele dá é a busca: as tags "facilita[m] a vida do Google" e ajudam a hierarquizar o site ([[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]]).

## O ganho mais concreto é acessibilidade

`[external]` Leitores de tela expõem `header`, `nav`, `main`, `aside` e `footer` como landmarks para pular de região em região; `button`, `a` e títulos `h1`–`h6` trazem papel e foco de graça (https://developer.mozilla.org/en-US/docs/Glossary/Semantics). Uma `div` com clique não tem nada disso. Ver [[wiki/concepts/acessibilidade]]. Para SEO, semântica ajuda o buscador a entender a estrutura, mas não é fator forte de ranqueamento (confiança média).

## Key Sources

- [[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]] — header, nav, section, article, figure, footer; visual igual à div; motivo dado: Google
