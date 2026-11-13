---
type: concept
title: "Centralização óptica"
aliases: ["centro óptico", "alinhamento óptico", "optical alignment", "optical centering", "ajuste óptico", "balanceio de formas"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 3
tags: [ui, ui-design, icones, simetria, percepcao, equilibrio]
skill: ux-ui-mentor
status: stub
---

# Centralização óptica

Centralizar pelo que o olho percebe, não pelas coordenadas. Uma forma de peso desigual, como o triângulo, fica "torta" quando centralizada pelo bounding box, porque a massa visual se concentra no lado maior.

## Na aula

[[wiki/entities/nasser|Násser]] centraliza um triângulo de play pelas guias do [[wiki/entities/figma]] e pergunta: "para o olho humano ele está centralizado? Logicamente que não". Motivo: "a base do triângulo [ocupa] mais espaço do que a ponta", então "visualmente ele fica desequilibrado". Ele chama isso de "balanceio de algumas formas geométricas" ([[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]]).

Na mesma aula: um círculo de 7×7 (ímpar) num frame par "fica torto" por um pixel, e "o seu olho percebe isso". Daí a regra de tamanhos pares e [[wiki/concepts/grid-de-icones|grid]].

## Por que acontece

`[external]` O centro do bounding box de um triângulo não coincide com o seu centroide, que fica a 1/3 da altura a partir da base. No play (ponta para a direita), o centro de massa fica à esquerda do centro da caixa; por isso o ícone costuma ser deslocado para o lado da ponta. A aula afirma que o Figma já deixa "dois pixels vazios" no shape de triângulo para compensar; não verificado.

## Relação

- [[wiki/concepts/simetria-visual]]: a simetria que importa é a percebida.
- [[wiki/concepts/icones-em-interfaces]]: em ícones pequenos, um pixel de erro aparece.

## O card não resolve sozinho

Na edição "W7" ([[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]]), colocar ícones de proporções diferentes dentro de cards "dá uma equilibrada", mas "nada adianta" se o play "não está exatamente no centro": "sempre se preocupe em ele estar alinhado, centralizado e equilibrado uns com relação aos outros".

## Estruturas regulares

Em [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]]: círculo, card ou quadrado em volta do ícone "para poder causar um equilíbrio maior" entre ícones retangulares, deitados ou em pé. A estrutura padroniza a área; o centro óptico do desenho ainda precisa de ajuste.

## Key Sources

- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — triângulo do play e círculo ímpar "tortos"
- [[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]] — cards homogeneízam ícones, mas o play fora do centro continua errado
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — ícone dentro de círculo ou card para equilibrar proporções
