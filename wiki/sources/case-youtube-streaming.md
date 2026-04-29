---
type: source
title: "Case: YouTube / Video Streaming"
aliases: ["youtube system design", "video streaming design", "case youtube"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, cases, youtube, streaming, hls, cdn, encoding, s3]
skill: tech-mentor-system-design
source_file: /home/gabriel-martins/Documentos/dev-study/raw/case-youtube-streaming.md
source_url: ""
author: "tech-mentor skill"
date_published: 2026-03-29
date_ingested: 2026-04-22
status: stable
---

# Case: YouTube / Video Streaming

## TL;DR

Três problemas distintos: upload (presigned URL → S3 → SQS → workers paralelos por segmento), entrega (HLS/DASH + ABR + CDN com TTL 365 dias para segmentos imutáveis), e storage (hierárquico Hot/Warm/Cold — 90% do volume em Glacier, 80% de economia). Transcodificação paralela por segmento reduz 4h de CPU para ~10min.

## Key Claims

- **Upload direto para S3 via presigned URL** — backend não vira gargalo de I/O de vídeo. S3 event → SQS → workers. → [[concepts/media-upload-pattern]]
- **Transcodificação paralela por segmento** — vídeo de 2h dividido em 720 segmentos de 10s, cada um transcodificado em paralelo via SQS + workers. → [[concepts/video-transcoding]]
- **HLS/DASH + ABR** — player consume segmentos de 2-10s, muda qualidade a cada segmento conforme bandwidth. Buffer de 30s evita rebuffering. → [[concepts/adaptive-bitrate-streaming]]
- **Segmentos são imutáveis** — CDN TTL de 365 dias. Manifesto TTL curto (60s) porque pode mudar. → [[concepts/cdn-strategy]]
- **Storage hierárquico** — Hot (S3 Standard), Warm (S3-IA), Cold (Glacier). 90% do volume em Cold com <5% do tráfego = 80% de economia. → [[concepts/storage-tiering]]
- **Pré-aquecimento de CDN** — ao detectar crescimento anômalo de views, push proativo para edges evita cache miss em cascata quando vídeo viraliza.
- **AV1 para conteúdo popular** — melhor compressão que H.264/HEVC, open-source. YouTube usa para economizar CDN e storage em vídeos com alto volume de views.

## Scale Numbers

```
Upload:     500h/min → 45TB de vídeo ingerido por hora
Storage:    240TB/hora gerado após transcodificação
Streams:    1B h/dia ÷ 86.400s = 11.5M streams simultâneos
CDN output: 11.5M × 2.5 Mbps (720p) = ~28 Tbps
Total:      ~1 exabyte de storage
```

## Entities

- [[entities/youtube]]
- [[entities/cloudfront]]
- [[entities/s3]]
- [[entities/ffmpeg]]

## Concepts

[[concepts/video-transcoding]] · [[concepts/adaptive-bitrate-streaming]] · [[concepts/cdn-strategy]] · [[concepts/storage-tiering]] · [[concepts/media-upload-pattern]] · [[concepts/estimativas-back-of-envelope]]

## Open Questions

- DRM (Widevine + PlayReady + FairPlay) — como key rotation funciona sem interromper streams ativos?
- Threshold de views para trocar H.264 por AV1 — qual é o break-even de custo de encoding vs economia de CDN?

## Raw Quotes

> "O upload nunca deve passar pelo backend da aplicação — vídeos são grandes demais."

> "Segmentos de vídeo são imutáveis — uma vez gerados, nunca mudam. Isso permite cache agressivo."

> "90% do volume em Cold, <5% do tráfego — storage hierárquico reduz custo drasticamente."
