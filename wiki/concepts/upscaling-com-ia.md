---
type: concept
title: "Upscaling com IA (super-resolução)"
aliases: ["upscale", "super resolução", "AI upscaling", "aprimoramento de vídeo", "video enhancement"]
date_created: 2026-11-23
date_updated: 2026-11-23
source_count: 1
tags: [ia-generativa, video, imagem, upscaling, super-resolucao, interpolacao-de-frames]
skill: tech-mentor-ai
status: stub
---

# Upscaling com IA

Aumentar a resolução de imagem ou vídeo com um modelo que **reconstrói** detalhe plausível, em vez de só esticar pixels como a interpolação bicúbica. Em vídeo, costuma vir junto com *denoise*, nitidez e interpolação de frames (30 → 60 fps).

## Na prática da fonte

[[wiki/entities/nasser|Násser]] usa o [[wiki/entities/topaz-video]] como última etapa do [[wiki/concepts/pipeline-de-midia-com-ia]] ([[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]]):

- **2x, não 4x:** de 1080p, 2x "fica próximo do 4K". O 4x "na maioria das vezes não reconstrói muito bem, porque ele precisa inventar muita coisa".
- **Ajuste por conteúdo:** carro, renderização e vídeo comum pedem configurações diferentes. Muita nitidez "denuncia" texto, e muito *denoise* fica "artificial demais" e apaga textura que se queria manter.
- **Produzir acima e reduzir:** nivela tudo em 4K60 para entregar 1080p30 ou 1080p60 no site.

## Precisões `[external]`

- O upscale não recupera informação, ele inventa detalhe estatisticamente provável. Por isso o fator alto falha, e texto e logos saem errados primeiro (alta).
- Subir para 4K e voltar a 1080p ajuda pelo *denoise* e pela limpeza de artefatos, não pela resolução. Reduzir resolução (*supersampling*) só suaviza (média).
- A interpolação de frames é outro modelo e outro risco: cria quadros intermediários e pode gerar artefatos em movimento rápido (alta).

## Key Sources

- [[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]]
