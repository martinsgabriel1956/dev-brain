---
type: concept
title: "Estilos padrão do navegador e reset CSS"
aliases: ["user agent stylesheet", "folha de estilo do navegador", "reset CSS", "CSS reset", "normalize", "estilos padrão"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [css, reset, user-agent, cascata, frontend]
skill: tech-mentor-frontend
status: stub
---

# Estilos padrão do navegador e reset CSS

Antes de qualquer CSS do autor, o navegador aplica a sua própria folha (user agent stylesheet): link azul e sublinhado, roxo quando visitado, marcadores nas listas, margens no `body` e nos títulos, tamanhos de `h1`–`h6`. Um **reset** zera ou padroniza esses valores no início do CSS do projeto.

Na aula 03 do módulo de front-end do [[wiki/entities/frontpush]] ([[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]), [[wiki/entities/nasser|Násser]] tira o sublinhado (`text-decoration: none`), pinta os links de branco e remove os marcadores (`list-style: none`): "isso aqui já participa de uns resets que eu gosto de deixar dentro da página, porque isso aqui é tudo configuração padrão do HTML". Nas aulas do módulo Básico CSS, o reset dele é `* { margin: 0; padding: 0; box-sizing: border-box }` ([[wiki/sources/classes-e-ids-no-css]]; ver [[wiki/concepts/box-model]]).

`[external]` Os padrões vêm do navegador, não do HTML, e mudam um pouco entre navegadores, o que motivou o normalize.css (padronizar em vez de zerar): https://developer.mozilla.org/en-US/docs/Web/CSS/Cascade#user-agent_stylesheets. Por terem a menor prioridade na [[wiki/concepts/cascata-css]], qualquer regra do autor os sobrescreve. `[skill: tech-mentor-frontend]` Na arquitetura ITCSS, o reset fica na camada Generic, antes de elementos e componentes. Ver [[wiki/concepts/compatibilidade-entre-navegadores]].

## Key sources

- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: links e listas "resetados"; "configuração padrão do HTML"
- [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]]: `* { color: white }` como "reset dos seletores" (cor é herdada; basta o `body`)
