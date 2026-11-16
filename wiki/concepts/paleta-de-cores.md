---
type: concept
title: "Paleta de cores"
aliases: ["paleta", "color palette", "paleta de cor", "esquema de cores", "base + enfoque", "cor de base", "cor de enfoque"]
date_created: 2026-11-14
date_updated: 2026-11-14
source_count: 1
tags: [ui, ui-design, cor, paleta-de-cores, harmonia-de-cores, identidade-visual, design-tokens]
skill: ux-ui-mentor
status: stub
---

# Paleta de cores

"Conjunto de cores pré-selecionadas que são utilizadas em harmonia" ([[wiki/sources/paleta-de-cores-base-enfoque-monocromatica-analoga-triadica]]). Serve para três coisas: garantir [[wiki/concepts/contraste]] e uma boa experiência, passar um sentimento e sustentar a [[wiki/concepts/identidade-visual]].

## Receita mínima

Cores de contraste, "uma cor característica que leve algum tipo de sentimento", e branco e preto para compor o resto (corpo de texto, outros elementos). Mais cores que isso confundem: "utilizar várias cores em um projeto faz ficar confuso". Ver [[wiki/concepts/simplicidade-visual]].

## Quatro tipos da aula

| Tipo | Como se monta | Exemplo da aula |
|---|---|---|
| Base + enfoque | cor primária de marca + cor de destaque complementar ou "dividir complementar" | roxo dark + verde da [[wiki/entities/rocketseat]]; laranja + azul |
| Monocromática | uma cor em tons claros e escuros + neutros | identidade do autor: laranja, preto, branco, cinzas |
| Análoga | duas vizinhas no círculo, uma escura e uma clara | roxo escuro + rosa; azul + turquesa |
| Triádica | uma predominante + duas de destaque | turquesa, vermelho, amarelo |

As relações entre cores vêm do círculo cromático: ver [[wiki/concepts/harmonia-de-cores]]. A proporção entre base e enfoque vem da [[wiki/concepts/regra-60-30-10]].

## Princípio, não regra

"Tudo que eu dizer aqui são princípios, não são regras." Há paletas que não cabem em nenhum tipo ("muito eclético"). Paletas não são patenteadas: o [[wiki/entities/color-hunt]] dá os hexadecimais para copiar.

## Olhar de dev

`[skill: ux-ui-mentor]` Uma paleta de UI vira três camadas de tokens: primitivos (escala `50` a `950` de cada matiz, que é a "variação de tons claros e escuros" da monocromática), semânticos (`--color-brand` para a base, `--color-accent`/`--color-interactive` para o enfoque, `--color-text-primary` para o preto) e de componente quando necessário. Componentes usam só os semânticos; dark mode muda o valor dos semânticos, não o nome. Em OKLCH, o mesmo L dá o mesmo brilho percebido entre matizes, o que facilita a "luminosidade do espectro" que o slide da análoga pede. Cor de marca e [[wiki/concepts/cor-semantica]] (sucesso, erro) ficam em tokens separados.

## Key Sources

- [[wiki/sources/paleta-de-cores-base-enfoque-monocromatica-analoga-triadica]] — definição, receita mínima, quatro tipos, Rocketseat, Color Hunt
