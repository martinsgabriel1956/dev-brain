---
type: concept
title: "Adaptive Bitrate Streaming (ABR)"
aliases: ["abr", "hls", "dash", "adaptive streaming", "http live streaming"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, video, streaming, hls, dash, abr, cdn]
skill: tech-mentor-system-design
status: stable
---

# Adaptive Bitrate Streaming (ABR)

Player consome segmentos de 2-10s, cada um disponível em múltiplas qualidades. Muda qualidade a cada segmento conforme bandwidth — sem rebuffering.

## HLS (HTTP Live Streaming)

Padrão Apple, amplamente adotado.

```m3u8
# Manifesto master (.m3u8)
#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=800000,RESOLUTION=640x360
360p/index.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=2800000,RESOLUTION=1280x720
720p/index.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=5000000,RESOLUTION=1920x1080
1080p/index.m3u8

# Manifesto de qualidade (720p/index.m3u8)
#EXT-X-TARGETDURATION:6
#EXTINF:6.0,
segment_001.ts
#EXTINF:6.0,
segment_002.ts
```

## DASH (Dynamic Adaptive Streaming over HTTP)

Padrão aberto usado no YouTube. Manifesto em XML (MPD). Mais flexível, suporte nativo a DRM (Widevine, PlayReady).

## Fluxo do Player

```
1. Download manifesto master
2. Escolhe qualidade inicial com base em bandwidth estimado
3. A cada segmento: bandwidth atual > threshold? sobe. < threshold? desce.
4. Buffer 30s de antecipação → troca de qualidade sem rebuffering
```

## Por que Segmentos e Não o Arquivo Inteiro

- Seek é O(1) — vai direto ao segmento do timestamp
- Troca de qualidade sem interrupção — segmentos futuros em qualidade diferente
- Cache eficiente — segmentos são imutáveis, CDN TTL 365 dias → [[concepts/cdn-strategy]]

## Key Sources

- [[sources/case-youtube-streaming]]
