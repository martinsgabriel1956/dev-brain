---
type: concept
title: "Estilos padrão do navegador e reset CSS"
aliases: ["user agent stylesheet", "folha de estilo do navegador", "reset CSS", "CSS reset", "normalize", "estilos padrão"]
date_created: 2026-11-16
date_updated: 2026-11-20
source_count: 8
tags: [css, reset, user-agent, cascata, frontend]
skill: tech-mentor-frontend
status: stub
---

# Estilos padrão do navegador e reset CSS

Antes de qualquer CSS do autor, o navegador aplica a sua própria folha (user agent stylesheet): link azul e sublinhado, roxo quando visitado, marcadores nas listas, margens no `body` e nos títulos, tamanhos de `h1`–`h6`. Um **reset** zera ou padroniza esses valores no início do CSS do projeto.

Na aula 03 do módulo de front-end do [[wiki/entities/frontpush]] ([[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]), [[wiki/entities/nasser|Násser]] tira o sublinhado (`text-decoration: none`), pinta os links de branco e remove os marcadores (`list-style: none`): "isso aqui já participa de uns resets que eu gosto de deixar dentro da página, porque isso aqui é tudo configuração padrão do HTML". Nas aulas do módulo Básico CSS, o reset dele é `* { margin: 0; padding: 0; box-sizing: border-box }` ([[wiki/sources/classes-e-ids-no-css]]; ver [[wiki/concepts/box-model]]).

`[external]` Os padrões vêm do navegador, não do HTML, e mudam um pouco entre navegadores, o que motivou o normalize.css (padronizar em vez de zerar): https://developer.mozilla.org/en-US/docs/Web/CSS/Cascade#user-agent_stylesheets. Por terem a menor prioridade na [[wiki/concepts/cascata-css]], qualquer regra do autor os sobrescreve. `[skill: tech-mentor-frontend]` Na arquitetura ITCSS, o reset fica na camada Generic, antes de elementos e componentes. Ver [[wiki/concepts/compatibilidade-entre-navegadores]].

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], o reset é `* { margin: 0; padding: 0; box-sizing: border-box }`. No DevTools, o `margin: 8px` do *user agent* no body aparece riscado, e o `h1` mostra o estilo que o navegador já define. O `button` não herda cor nem fonte do body, por isso a Poppins vai em `body, input, button, textarea`.

## No primeiro arquivo Sass (FrontPUSH)

Em [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]], o primeiro `style.scss` começa pelo mesmo reset: `padding: 0`, `margin: 0`, `box-sizing: border-box`.

## "Sempre aplique esse hack" (FrontPUSH, básico CSS aula 01)

Em [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]: `*` zera margin e padding "porque [...] algumas tags do HTML [...] por padrão vem com o margin e com o padding", mais `box-sizing: border-box`. `[external]` O reset moderno inclui `*::before, *::after` ([[wiki/concepts/box-model]]).

## Key sources

- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: links e listas "resetados"; "configuração padrão do HTML"
- [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]]: `* { color: white }` como "reset dos seletores" (cor é herdada; basta o `body`)
- [[wiki/sources/frontpush-justify-content-align-items-box-sizing]]: `box-sizing: border-box` "em todos os projetos"
- [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]]: reset de margin/padding e "border-size" (é `box-sizing`) em border-box no início do projeto
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: reset com box-sizing; margin 8px do body; botão sem herança
- [[wiki/sources/frontpush-mentoria-pratica-com-css-grid]]: mentoria de grid: o "hack" de margin, padding e box-sizing no início do projeto
- [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]]: reset no primeiro `style.scss`
- [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 01: o reset `*` antes das demos de transform
