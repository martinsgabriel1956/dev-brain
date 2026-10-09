---
type: concept
title: "Speech-to-Speech"
aliases: ["S2S", "voz para voz", "modelo de voz em tempo real"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 1
tags: [ai, multimodal, voz, speech-to-speech, latencia]
skill: tech-mentor-ai
status: stub
---

## Definição

Modelo que recebe **áudio** e responde com **áudio** diretamente, sem pipeline STT → LLM → TTS separado; menor latência e conversa mais fluida (interrupções, tom). Acessível por API (ex.: [[wiki/entities/gemini-live]], GPT Live, Grok Voice). Ver pipeline clássico em [external] skill tech-mentor-ai `multimodal-audio`.

## Pontos da fonte

- Avaliado no *Speech-to-Speech Index*: Gemini 3.8 Live Extended Thinking superou GPT Live 1 e Grok Voice.
- Custo é o gargalo para atendimento telefônico por bot: ~US$ 3/h (GPT Live 1) vs ~US$ 0,84/h (Gemini 3.8 Live).
- Previsão: telemarketing e golpes por IA em escala quando ficar barato.

## Conexões

[[wiki/concepts/time-to-first-token]] (latência percebida), [[wiki/entities/openai]], [[wiki/entities/xai]].

## Key Sources

- [[wiki/sources/google-nao-esta-perdendo-corrida-ia-memory-caching-gemini-live]]
