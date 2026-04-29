---
type: concept
title: "Video Transcoding"
aliases: ["transcodificação", "transcoding pipeline", "ffmpeg", "encoding paralelo"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, video, encoding, s3, sqs, workers, youtube]
skill: tech-mentor-system-design
status: stable
---

# Video Transcoding

Conversão do vídeo original para múltiplas qualidades e formatos, de forma assíncrona e paralela.

## Pipeline

```
S3 event (ObjectCreated) → SQS → Transcoding Workers (EC2/ECS)

Por vídeo, workers paralelos:
  - Transcodifica para cada qualidade (FFmpeg): 360p, 720p, 1080p, 4K
  - Gera thumbnails (frames em 5s, 10s, 30s)
  - Extrai metadados (duração, resolução, codec, bitrate)
  - Divide em segmentos HLS/DASH (2-10s cada)

Outputs → S3 (segmentos + thumbnails)
       → CDN (CloudFront) distribui globalmente
       → PostgreSQL: status PROCESSING → READY
```

## Paralelismo por Segmento

```
Vídeo 2h sequencial = horas de CPU
Vídeo 2h paralelo:
  → 720 segmentos de 10s
  → 720 workers em paralelo
  → ~10min de wall-clock time

SQS: 1 mensagem por segmento por qualidade
DLQ: segmentos que falharam → retry automático
Auto-scaling: workers escalam com base no tamanho da fila
```

## Codecs

| Codec | Compressão | Compatibilidade | Licença |
|---|---|---|---|
| H.264 | Moderada | Máxima | Patenteado |
| H.265 (HEVC) | 2× melhor | Menor | Cara |
| VP9 | Melhor que H.264 | Boa | Open-source |
| AV1 | Melhor que HEVC | Crescente | Open-source |

YouTube usa AV1 para conteúdo popular (economia de CDN/storage), H.264 como baseline de compatibilidade.

## Relacionado

[[concepts/media-upload-pattern]] — upload direto para S3 sem passar pelo backend.

## Key Sources

- [[sources/case-youtube-streaming]]
