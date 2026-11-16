---
type: concept
title: "Design tokens"
aliases: ["token de design", "tokens de design", "variáveis de design", "labels de design", "nomenclatura de estilos"]
date_created: 2026-11-15
date_updated: 2026-11-16
source_count: 2
tags: [ui, design-system, design-tokens, css, sass, nomenclatura, dark-mode, handoff]
skill: ux-ui-mentor
status: stub
---

# Design tokens

Valores de design com nome (cor, tamanho de fonte, sombra, raio, espaçamento) usados do mesmo jeito no arquivo de design e no código. O nome é o contrato entre os dois times.

## Na aula de style guide

[[wiki/entities/nasser|Násser]] não usa o termo, mas descreve a prática ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]):

- **Labels que design e dev entendem:** `card-dark`, `card-hover`. Hover porque é o nome do estado no CSS.
- **Cifrão para variável:** `$orange`, orange dark e orange light, "para quando eu estiver até no código utilizar essa mesma label". O cifrão é a sintaxe de variável do Sass.
- **Hexadecimais no Sass ou em variáveis CSS**, para dar consistência ao código ([[wiki/concepts/consistencia-visual]]).
- **Grupos de estilo no [[wiki/entities/figma]]** (texto, cor, sombra), o lado do design dos mesmos valores.

## Primitivo x semântico

`[skill: ux-ui-mentor]` A skill separa duas camadas. Primitivos dão nome ao valor (`color-blue-500: #3B82F6`) e não vão direto no componente. Semânticos dão nome ao papel (`color-brand-primary`, `color-feedback-error`) e apontam para um primitivo. Os componentes só usam semânticos. Com isso, trocar de tema ou de marca é trocar o valor do semântico, não o componente.

`orange`, `orange dark` e `orange light` da aula são primitivos. `card-dark` mistura componente e tema no nome. No dark mode da skill, o nome continua `--color-surface` e só o valor muda por modo (`[data-theme="dark"]`).

```scss
// como a aula descreve (Sass)
$orange: #fcbd38;      // valor ilustrativo, não mostrado na aula
$orange-dark: #e0a020;
$orange-light: #ffd77a;

// camada semântica sugerida pela skill (CSS custom properties)
:root              { --color-brand: #{$orange}; --card-bg: #fff; }
[data-theme="dark"] { --card-bg: #1e293b; }
.card:hover        { box-shadow: var(--shadow-hover); }
```

## Ferramentas

`[skill: ux-ui-mentor]` Figma Variables (com modos light e dark) define os tokens no próprio Figma. Tokens Studio exporta um `tokens.json` e o Style Dictionary gera CSS, SCSS, JS e plataformas nativas a partir dele. `[external]` O formato está em padronização pelo W3C Design Tokens Community Group (https://www.designtokens.org/).

## `:root` na aula de seletores

Em [[wiki/sources/seletores-e-pseudo-elements-css]], "o root é quando a gente está definindo variáveis". `[external]` `:root` é a pseudo-classe que casa com `<html>`; as custom properties declaradas ali valem na página toda, por isso é o lugar costumeiro dos tokens. Ver [[wiki/concepts/pseudo-classe-css]].

## Key Sources

- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]: labels `card-hover`, `$orange`, orange dark/light; hexadecimais no Sass; grupos de estilo no Figma
- [[wiki/sources/seletores-e-pseudo-elements-css]] — `:root` como lugar das variáveis CSS
