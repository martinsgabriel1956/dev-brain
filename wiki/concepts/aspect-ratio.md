---
type: concept
title: "Aspect ratio (proporção da imagem)"
aliases: ["aspect ratio", "proporção", "proporção de aspecto", "relação de aspecto", "não distorcer imagens"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 4
tags: [ui, ui-design, imagens, aspect-ratio, figma, css, core-web-vitals]
skill: ux-ui-mentor
status: stub
---

# Aspect ratio

Relação entre a dimensão horizontal e a vertical de uma imagem. A regra de UI é preservá-la: "nada de distorção de imagem" ([[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]]).

## No Figma

Ao puxar só um lado de uma imagem, o [[wiki/entities/figma]] "faz meio que um crop automático" em vez de esticar, e mesmo agrupada a imagem não deixa distorcer. Ainda assim dá para forçar: Násser cita um post do Instagram em que distorceu um trecho de imagem sem ficar "tão ruim", e mostra outra foto em que a distorção salta aos olhos.

## No código

`[external]` No navegador não há proteção automática: `<img>` com largura e altura fora da proporção estica. `object-fit: cover` recorta como o Figma, `contain` encaixa sem cortar (https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit).

`[skill: ux-ui-mentor]` A propriedade CSS `aspect-ratio` (ou `width`/`height` no `<img>`) reserva o espaço antes da imagem carregar e evita CLS. Ver [[wiki/concepts/otimizacao-de-imagens]].

## Ver também

- [[wiki/concepts/imagens-em-interfaces]]

## Padronizar o conjunto

A parte 3 acrescenta o outro lado: além de não distorcer cada imagem, entregar **todas no mesmo aspect ratio e resolução**, padronizadas no Figma, para o desenvolvedor "copiar e colar com as outras imagens e vai funcionar". Sem isso, a thumb do post fica "mais para cima" ou "mais para baixo" ([[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]]). `[external]` No código, container com `aspect-ratio` fixo e `object-fit: cover` absorve as diferenças, mas não salva imagem em baixa resolução.

## Proporções do Material Design

Na parte 4, as diretrizes do [[wiki/entities/material-design]] são citadas com 16 por 9, 3 por 4 e 1 por 1 ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]]); lista não conferida no guia.

## Key Sources

- [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]] — "não distorça as imagens"; crop automático do Figma
- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — padronizar a proporção de todas as imagens de uma seção para o handoff
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]] — proporções citadas do Material Design
- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — edição "W7": não esticar uma 1920×1080 para caber num banner; o Figma mantém a proporção e centraliza
