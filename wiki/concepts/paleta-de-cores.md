---
type: concept
title: "Paleta de cores"
aliases: ["paleta", "color palette", "paleta de cor", "base e enfoque", "cor de base", "cor de destaque", "escala de cinza"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, cor, paleta-de-cores, contraste, hierarquia-visual, design-tokens]
skill: ux-ui-mentor
status: stub
---

# Paleta de cores

Conjunto fechado de cores de uma interface, cada uma com um papel. No modelo **"base e enfoque"** da aula de [[wiki/entities/nasser|Násser]], há três papéis: uma **cor de base** (com tons mais escuros e mais claros), uma **cor de destaque** "para poder compor" e **cores neutras** para texto e composição ([[wiki/sources/aplicando-paleta-de-cores-base-destaque-hierarquia-gradiente-icones]]).

## Para que serve

- **Contraste**: "um dos objetivos da paleta de cores é ter um bom contraste". As cores de destaque e de texto precisam contrastar com a base. Ver [[wiki/concepts/contraste]].
- **Hierarquia**: a cor de destaque marca o que importa; o neutro fica com o resto. Ver [[wiki/concepts/hierarquia-visual]].
- **Consistência**: uma paleta escolhida e mantida em toda a interface. Ver [[wiki/concepts/consistencia-visual]].

## Escala de cinza

Sem cor de destaque, a hierarquia sai de variações de neutro (um branco mais forte, um cinza mais claro). As variações precisam ser grandes o bastante para se ver a diferença, "por isso que é importante a gente também ter a escala de cinza". Um tom pastel da base pode fazer o mesmo papel, como na paleta do [[wiki/entities/quarto-criativo]].

## A cor principal não é tudo

A cor de base não precisa cobrir a interface. O site pode ser branco (60% da interface), com blocos em cinza para separar seções e a cor de base só no hero; roxo em tudo "fique enjoativo" ([[wiki/sources/aplicando-paleta-de-cores-base-destaque-hierarquia-gradiente-icones]]). `[external]` A proporção lembra a regra 60-30-10 (dominante, secundária, destaque), que a aula não cita.

## Olhar de dev

`[skill: ux-ui-mentor]` Na implementação, a paleta vira tokens em três camadas: **primitivos** (`purple-100`…`purple-900`, `neutral-*`), **semânticos** (`color-background`, `color-text-primary`, `color-brand`, `color-accent`) e, se necessário, tokens de componente. Componentes usam só os semânticos. A cor de destaque da marca e o amarelo de warning ([[wiki/concepts/cor-semantica]]) devem ser tokens diferentes. HSL ou OKLCH facilitam gerar a escala de tons variando só a luminosidade.

## Armadilha comum

Pôr a cor de destaque atrás de texto claro: branco sobre amarelo não passa de 4.5:1. Na aula, um gradiente linear ameniza o problema ([[wiki/concepts/elementos-de-composicao]]).

## Key Sources

- [[wiki/sources/aplicando-paleta-de-cores-base-destaque-hierarquia-gradiente-icones]] — modelo base e enfoque (roxo + amarelo + neutros), hierarquia por cor, escala de cinza, 60% branco, ícones em tons pastéis
