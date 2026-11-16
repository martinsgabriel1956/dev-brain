---
type: concept
title: "Cascata do CSS (prioridade entre estilos)"
aliases: ["cascade", "cascata CSS", "prioridade do CSS", "estilo inline", "estilo incorporado", "CSS externo", "formas de aplicar CSS"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [css, cascata, especificidade, frontend]
skill: tech-mentor-frontend
status: stub
---

# Cascata do CSS (prioridade entre estilos)

O "C" de [[wiki/concepts/css]]: quando várias declarações miram a mesma propriedade do mesmo elemento, a cascata decide qual vale.

## As três formas de aplicar

Em [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]], três formas, em prioridade crescente segundo o slide:

| Forma | Onde | Alcance | Uso |
|---|---|---|---|
| Externo | arquivo `.css` ligado por `<link>` | todas as páginas que o ligam | "a forma mais utilizada" |
| Incorporado | `<style>` no `<head>` | só a página | exceção por página |
| Inline | atributo `style` na tag | só a tag | exceção por tag |

O argumento é de manutenção: com um arquivo externo, trocar uma cor é editar um lugar, não 40 páginas.

## O que de fato decide

`[external]` A ordem é: origem e importância (`!important` vence o normal), depois especificidade do seletor (inline > id > classe > tag), depois ordem no código (o último vence). Externo e incorporado empatam em origem e especificidade, então vence o que aparece depois no documento; a própria aula mostra o `style.css` sobrescrevendo o `<style>`. Fontes: https://developer.mozilla.org/en-US/docs/Web/CSS/Cascade e https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity.

`[skill: tech-mentor-frontend]` Em escala, a ordem é controlada por arquitetura: ITCSS (camadas por especificidade crescente) ou `@layer`, em que a ordem das camadas vence a especificidade e o código fora de camada vence tudo em camada.

## Key sources

- [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]] — externo, incorporado e inline; "quanto mais para baixo, maior a prioridade"; demo em que o externo vence o incorporado
- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: estilos padrão do navegador sobrescritos pelo autor; ver [[wiki/concepts/estilos-padrao-do-navegador-e-reset]]
