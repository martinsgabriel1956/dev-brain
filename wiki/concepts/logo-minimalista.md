---
type: concept
title: "Logo minimalista"
aliases: ["marca minimalista", "logo versátil", "logotipo minimalista", "menos é mais no logo", "flat logo", "logo plano"]
date_created: 2026-11-22
date_updated: 2026-11-22
source_count: 1
tags: [ui-design, design, branding, identidade-visual, logo, minimalismo, simplicidade]
skill: ux-ui-mentor
status: stub
---

# Logo minimalista

Logo simples o bastante para ser reproduzido em qualquer meio sem perder a identidade: bordado, marca d'água, uma cor só, fundo claro ou escuro, tamanho pequeno. Na mentoria de identidade visual do FrontPUSH ([[wiki/sources/frontpush-mentoria-identidade-visual-marca-minimalista-gradiente-paleta-tipografia]]), [[wiki/entities/nasser|Násser]] define o teste: "você se perguntar se a sua marca, do jeito que ela é, pode ser replicada e aplicada de várias maneiras diferentes, tanto no modo dark como no modo light". É a [[wiki/concepts/simplicidade-visual]] aplicada à marca.

## Os exemplos da aula

- **Nike:** "a forma é tão simples que ela consegue costurar"; vira marca d'água e sai em qualquer cor.
- **BMW:** trocou o logo com relevo por um plano, "mais fácil de imprimir e de replicar em qualquer lugar". `[external]` O redesenho é de 2020 (alta).
- **[[wiki/entities/apple|Apple]]:** a mesma maçã em várias cores e no papel de parede.
- **Burger King × McDonald's:** o hambúrguer no logo "amarra muito no nicho"; o "M" do McDonald's "não diz nada sobre o nicho", e a associação vem da repetição.

## Formato: perto do quadrado ou do círculo

"Não fuja muito do quadrado": desenhar sobre um quadrado, aceitar um pouco de retângulo, nunca "retangular demais". `[skill: ux-ui-mentor]` A razão prática é o encaixe: favicon, avatar de rede social e ícone de app são quadrados ou circulares, e um logo largo fica minúsculo neles (alta).

## Forma e sentido

O logo minimalista ainda comunica pela forma: traço reto passa precisão, redondo passa proximidade ([[wiki/concepts/formas-geometricas-e-organicas]]). No caso Black Dev da aula, o K (preto em CMYK) e o `->` do PHP viraram símbolo, com bordas levemente arredondadas.

## Olhar de dev

`[skill: ux-ui-mentor]` Um logo que passa nesse teste costuma ser um SVG de poucos paths, com uma cor que pode virar `currentColor`. Aí a versão dark e light sai de uma variável CSS, sem um arquivo por tema ([[wiki/concepts/formato-svg]]).

## Ver também

[[wiki/concepts/identidade-visual]], [[wiki/concepts/branding]], [[wiki/concepts/mascote-de-marca]]

## Key Sources

- [[wiki/sources/frontpush-mentoria-identidade-visual-marca-minimalista-gradiente-paleta-tipografia]]: teste do dark/light, Nike, BMW, Burger King, McDonald's, Apple; desenhar sobre um quadrado
