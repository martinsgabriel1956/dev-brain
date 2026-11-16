---
type: concept
title: "Variáveis CSS (custom properties)"
aliases: ["custom properties", "variáveis no CSS", "var()", ":root", "CSS variables"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [frontend, css, variaveis-css, design-tokens, cores]
skill: tech-mentor-frontend
status: stub
---

# Variáveis CSS (custom properties)

Propriedades com nome começando por `--`, declaradas num seletor (em geral `:root`, a raiz do documento) e lidas com `var(--nome)`. Herdam como qualquer propriedade e podem ser trocadas em tempo de execução, o que as torna o veículo usual de design tokens no CSS. Ver [[wiki/concepts/css]].

## Na NLW #1

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] declara `--title-color: #322153` e `--primary-color: #34CB79` em `:root` para não repetir cores: "se algum dia eu quiser mudar essa cor aqui, eu não preciso ir em todos os lugares que apareça essa cor e vir mudando". Chama de "um atalho" e "em formato de variáveis".

## Precisões

- `var()` aceita um valor reserva: `var(--primary-color, green)` `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/var).
- Diferente das variáveis de Sass, existem no navegador: mudar `--primary-color` num `.dark` troca o tema sem recompilar `[skill: tech-mentor-frontend]`.

## Key sources

- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: `--title-color` e `--primary-color` em `:root`
- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: Sass como pré-processador; ver [[wiki/concepts/pre-processador-css]]
