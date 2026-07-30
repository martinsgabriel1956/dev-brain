---
type: concept
title: "Adaptive Bitrate Streaming (ABR)"
aliases: ["abr", "hls", "dash", "adaptive streaming", "http live streaming"]
date_created: 2026-04-22
date_updated: 2026-07-30
source_count: 2
tags: [system-design, video, streaming, hls, dash, abr, cdn, live-streaming, buffer]
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

## Buffer de Leitura Antecipada como Custo de Latência

O buffer de 30s citado acima existe para absorver oscilação de rede sem rebuffering — mas em **live streaming**, esse mesmo buffer é, segundo a documentação do YouTube (citada em [[wiki/sources/delay-tv-aberta-vs-youtube-live-latencia-streaming]]), o principal causador de latência em relação ao instante real do evento. É o mesmo mecanismo, dois efeitos: em VOD, buffer maior só significa mais resiliência sem custo perceptível (o conteúdo já existe todo); em live, todo segundo de buffer é um segundo de atraso em relação ao "ao vivo" real. O YouTube expõe esse trade-off diretamente ao produtor via modos de latência (normal, baixa, ultra baixa) — ver [[wiki/concepts/latencia-streaming-ao-vivo]] para os números e o comportamento sob rede instável.

## Key Sources

- [[sources/case-youtube-streaming]]
- [[wiki/sources/delay-tv-aberta-vs-youtube-live-latencia-streaming]] — buffer de leitura antecipada em live streaming e modos de latência do YouTube
