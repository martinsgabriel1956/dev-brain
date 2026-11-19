---
type: concept
title: "WebP"
aliases: ["webp", "web picture format"]
date_created: 2026-07-29
date_updated: 2026-11-19
source_count: 5
tags: [formatos-de-imagem, compressao, webp, google]
skill: cs-fundamentals
status: stub
---

# WebP

Formato apresentado pelo Google em 2010 para unificar num único contêiner o que antes exigia três formatos separados: JPEG (fotografia), PNG (transparência) e GIF (animação). Suporta [[wiki/concepts/compressao-com-perdas-vs-sem-perdas|compressão com e sem perdas]], transparência e animação, gerando tipicamente arquivos 20-30% menores que JPEG/PNG equivalentes com qualidade comparável.

## Adoção

Levou anos para ganhar suporte amplo em navegadores — inicialmente visto como "mais um padrão imposto pelo Google". Hoje tem suporte nativo praticamente universal, e muitos sites convertem imagens para WebP automaticamente quando o navegador do visitante é compatível, de forma transparente ao usuário.

## Ver também

- [[wiki/concepts/formato-heic-avif]] — geração seguinte, com compressão ainda melhor mas adoção mais lenta

## Na prática de UI

Na aula de imagens de [[wiki/entities/nasser|Násser]], WebP é o quarto formato para web: mesma qualidade de JPG e PNG, "bem mais otimizado" em tamanho. O autor diz que ele "não é muito conhecido hoje em dia", o que está datado diante do suporte universal descrito acima ([[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]). `[skill: ux-ui-mentor]` O checklist de performance da skill pede hero image em WebP.

## No módulo de otimização do FrontPUSH

Em [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo]], "sempre otimize os PNGs e JPGs. Mas, além disso, eu vou falar sobre o WebP": tema adiado para a aula 03.

## "O melhor hoje em dia" (FrontPUSH, otimização aula 03)

Em [[wiki/sources/frontpush-otimizacao-de-imagens-svg-webp-lazy-loading]], WebP é "o melhor hoje em dia", recomendado pelo PageSpeed em "formatos de última geração"; converte JPG e PNG num site online. AVIF já comprime mais ([[wiki/concepts/formato-heic-avif]]); o padrão robusto é `<picture>` com AVIF, WebP e JPEG de reserva.

## "Ele quer em WebP" (FrontPUSH, otimização aula 06)

Em [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]], o aviso "formatos de última geração" é traduzido como "ele quer em WebP, ele não quer em PNG e JPEG", embora a ferramenta cite "WebP ou AVIF".

## Key Sources

- [[wiki/sources/historia-dos-formatos-de-imagem]]
- [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]] — WebP como quarto formato para web; afirmação de pouca adoção, datada
- [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo]]: FrontPUSH, otimização aula 02: WebP anunciado
- [[wiki/sources/frontpush-otimizacao-de-imagens-svg-webp-lazy-loading]]: FrontPUSH, otimização aula 03: WebP como formato recomendado
- [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]]: FrontPUSH, otimização aula 06: WebP como tradução do aviso de formato
