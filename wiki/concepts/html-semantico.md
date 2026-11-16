---
type: concept
title: "HTML semântico (tags semânticas do HTML5)"
aliases: ["tags semânticas", "semantic HTML", "HTML5 semântico", "elementos semânticos"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 8
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

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] troca a `div` sem significado por `header` e `main` ("essa parte talvez principal"), para dar sentido "tanto para quem for da manutenção do meu código, quanto para robozinhos do Google". Também pede nomes de classe semânticos.

## Na NLW #1, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa `fieldset` + `legend` no formulário em vez de `div`, "uma caixa que não tem muito significado": "isso daqui é para uma ideia mais semântica do HTML". Ver [[wiki/concepts/formulario-html]].

## "Tudo no final são caixinhas" (aula 02 do FrontPUSH)

Em [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]], [[wiki/entities/nasser|Násser]] volta ao tema: dá para montar o site todo com `div` dentro de `div`, "porque tudo no final são caixinhas", mas fica difícil "compreender de como é a estrutura, porque está tudo genérico", difícil refatorar e difícil "a vida do Google de indexar o seu site". Regra: "Qual é a tag semântica para poder representar isso? É essa, vai lá e utiliza". Tags citadas: `section`, `header`, `footer`, `nav`, `div`, `h1`–`h6`, `p`, `span`, `strong`, `img`, `form`, `input`. A aula também não menciona acessibilidade.

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] diz que "geralmente a gente usa tags li para semântica de lista", mas põe os `li` direto numa `div`, sem `ul` (inválido). Nos cards, um `h1` por card e um `h4` antes deles quebram a hierarquia de títulos.

## HTML da prática do YouTube (FrontPUSH, módulo de Flexbox)

Em [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]], [[wiki/entities/nasser|Násser]] diz "sempre utilizando HTML semântico" e usa `header`, `ul`/`li`/`a` e `section`, mas o resto é `div` (`div.nav`, `div.video-side`) e não há `h1`. `[external]` `<nav>`, `<main>`, `<aside>`/`<article>` e um `h1` no título do vídeo fecham a semântica.

## Key Sources

- [[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]] — header, nav, section, article, figure, footer; visual igual à div; motivo dado: Google
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: header e main; SEO
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: fieldset e legend no formulário
- [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]]: div dentro de div x tags semânticas; Google e refatoração
- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: menu `header` > `nav` > `ul` > `li`; trocar por `div` "vai contra o HTML semântico"
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: li sem ul; h1 por card
- [[wiki/sources/frontpush-order-e-align-self]]: ordem do HTML como ordem de leitura; `order` do flexbox só muda o visual `[external]`
- [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]]: header/ul/section, mas nav em div e sem h1 `[external]`
