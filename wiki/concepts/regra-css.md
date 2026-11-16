---
type: concept
title: "Regra CSS (seletor, propriedade e valor)"
aliases: ["sintaxe CSS", "seletor CSS", "declaração CSS", "propriedade e valor"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [css, sintaxe, seletor, frontend]
skill: tech-mentor-frontend
status: stub
---

# Regra CSS (seletor, propriedade e valor)

Unidade básica do [[wiki/concepts/css]]: `seletor { propriedade: valor; }`. O seletor escolhe os elementos; cada declaração `propriedade: valor` define um aspecto deles.

Em [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]], o slide escreve `elemento{ propriedade: valor; }` → `h1{ color: green; }`, e o autor define seletores como "literalmente as tags". "A grande questão está em conhecer essas propriedades, saber como aplica os valores." Valores de cor podem ser nome (`red`), [[wiki/concepts/sistema-hexadecimal|hexadecimal]] ou RGBA ([[wiki/concepts/modelos-de-cor]]).

No atributo `style` (inline) não há seletor: só as declarações, que valem para a própria tag. Ver [[wiki/concepts/cascata-css]].

`[external]` Seletor de tag é só o tipo mais simples; há classe, id, atributo, pseudo-classe e combinadores, cada um com sua especificidade: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors.

## Key sources

- [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]] — elemento, propriedade, valor; seletor = tag
