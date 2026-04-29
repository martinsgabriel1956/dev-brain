---
type: source
title: "On-Device AI — Core ML, TFLite, MediaPipe, Gemini Nano"
aliases: ["on device ai mobile", "core ml ios", "tflite android", "mediapipe mobile", "gemini nano"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-on-device-ai.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, on-device-ai, coreml, tflite, mediapipe, gemini-nano, quantization, neural-engine]
skill: tech-mentor-mobile
status: stable
---

# On-Device AI — Mobile

## TL;DR

Inferência local: Core ML (iOS, Neural Engine) e TFLite/LiteRT (Android, NNAPI/GPU). MediaPipe para visão computacional cross-platform. Gemini Nano (Android 14+ Pixel/Samsung) para LLM on-device. Vantagens: privacidade, latência zero, funciona offline. Trade-off: modelos precisam de quantização (INT8/INT4) para caber no dispositivo — precisão menor.

## Claims Principais

| Claim | Confiança |
|---|---|
| Core ML usa Neural Engine em iPhones A12+ — inferência sem consumir CPU/GPU | Alta |
| TFLite quantizado INT8 é 4x menor que float32 — essencial para mobile | Alta |
| MediaPipe Tasks API unifica visão/áudio cross-platform com modelos pré-treinados | Alta |
| Gemini Nano requer AICore (Android 14+, hardware específico) — não disponível para todos | Alta |
| On-device AI: sem latência de rede, sem custo de API, sem PII enviado ao servidor | Alta |

## Conceitos Abordados

- [[mobile-on-device-ai]] · [[mobile-metricas-criticas]] · [[mobile-profiling]] · [[mobile-cross-platform-decision]]
