---
type: concept
title: "HTML semântico (tags semânticas do HTML5)"
aliases: ["tags semânticas", "semantic HTML", "HTML5 semântico", "elementos semânticos"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
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

## "Tudo no final são caixinhas" (aula 02 do FrontPUSH)

Em [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]], [[wiki/entities/nasser|Násser]] volta ao tema: dá para montar o site todo com `div` dentro de `div`, "porque tudo no final são caixinhas", mas fica difícil "compreender de como é a estrutura, porque está tudo genérico", difícil refatorar e difícil "a vida do Google de indexar o seu site". Regra: "Qual é a tag semântica para poder representar isso? É essa, vai lá e utiliza". Tags citadas: `section`, `header`, `footer`, `nav`, `div`, `h1`–`h6`, `p`, `span`, `strong`, `img`, `form`, `input`. A aula também não menciona acessibilidade.

## Key Sources

- [[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]] — header, nav, section, article, figure, footer; visual igual à div; motivo dado: Google
- [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]]: div dentro de div x tags semânticas; Google e refatoração
- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: menu `header` > `nav` > `ul` > `li`; trocar por `div` "vai contra o HTML semântico"
