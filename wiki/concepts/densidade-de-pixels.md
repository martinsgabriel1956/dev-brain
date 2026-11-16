---
type: concept
title: "Densidade de pixels"
aliases: ["pixel density", "@2x @3x", "DPR", "device pixel ratio", "dp", "pt"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [mobile, imagens, design, telas]
skill: tech-mentor-mobile
status: stub
---

# Densidade de pixels

Quantos pixels físicos a tela usa para cada unidade lógica (pt no iOS, dp no Android, px de CSS na web). Numa tela @3x, um quadrado de 44×44 pt ocupa 132×132 pixels físicos. É o `PixelRatio.get()` do React Native e o `devicePixelRatio` do navegador.

Na aula de [[wiki/entities/diego-fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]), a regra é exportar cada imagem em três tamanhos (`logo.png`, `logo@2x.png`, `logo@3x.png`). O React Native escolhe sozinho o arquivo certo para o aparelho, e uma imagem de 44 px "vai ficar embaçada" numa tela de densidade 3.

**Correção do exemplo da aula:** Diego compara um Galaxy S2 "1920×1080" a um iPhone 8 @3x de mesma resolução. O Galaxy S2 tinha 800×480, e o iPhone 8 é 1334×750 @2x; o 1920×1080 @3x é o do iPhone 8 Plus `[external]` (https://developer.apple.com/design/human-interface-guidelines/layout). A ideia vale, os números não.

**Alternativas aos três PNGs:** SVG (`react-native-svg`, usado na mesma aula para os ícones dos itens) ou fontes de ícones (`@expo/vector-icons`) escalam sem perder qualidade. Ver [[wiki/concepts/formato-svg]].

Relacionado: [[wiki/concepts/unidades-de-medida-css]], [[wiki/concepts/imagens-em-interfaces]].

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], [[wiki/entities/mayk-brito|Mayk]] diz que "numa tela de 4K, 16 pixels não é nada". O px do CSS é escalado pela densidade, então num 4K com escala do sistema a medida visual se mantém.

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: exportar 1x/2x/3x do Figma
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: "16 pixels num 4K" (imprecisão)
