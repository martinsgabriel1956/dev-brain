---
type: entity
title: "NVIDIA"
aliases: ["Nvidia"]
date_created: 2026-07-21
date_updated: 2026-11-27
source_count: 6
tags: [nvidia, gpu, hardware, organização, palantir]
skill: tech-mentor-ai
status: stub
---

# NVIDIA

Fabricante de GPUs, hardware dominante para treinamento e inferência de LLMs em escala. Sujeita a [[wiki/concepts/export-controls-chips-ia|sanções de exportação de chips]] para determinados países (notadamente a China) por motivos de política internacional — restrição citada em [[wiki/sources/kimi-k3-china-mercado-ia-open-source]] como pressão de fundo por trás de inovações arquiteturais como o [[wiki/concepts/mixture-of-experts|MoE]] e a otimização agressiva de [[wiki/concepts/kv-cache|KV Cache]] do Kimi K3 ([[wiki/entities/moonshot-ai]]).

## Deal com a Palantir e "a Única que Está Certa"

[[wiki/sources/palantir-ceo-token-tax-nvidia-scam-ia]] descreve um deal entre a Nvidia e a [[wiki/entities/palantir-technologies]] (contexto de uma entrevista do CEO da Palantir à CNBC) e trata a Nvidia como a única parte "correta" na dinâmica de mercado de IA: vende hardware e não fica — não custeia o dado do cliente, não retreina modelos em cima do workflow do cliente, e (segundo o autor, sem confirmação) provavelmente não cobra por resultado — em contraste direto com a crítica feita a [[wiki/entities/openai]] e [[wiki/entities/anthropic]] no mesmo vídeo. A visão da Palantir para o próprio produto combina modelo aberto + camada de aplicação + compute Nvidia.

## TPU do Google como complemento

[[wiki/sources/google-nao-esta-perdendo-corrida-ia-memory-caching-gemini-live]] enquadra os [[wiki/concepts/tensor-processing-unit|TPUs]] do Google como complemento (não substituto direto) à Nvidia na infraestrutura de IA.

## De placa de vídeo a empresa de IA (FrontPUSH, aula 6)

[[wiki/sources/frontpush-ia-o-futuro-da-ia-parte-2]]: a NVIDIA "parou de ser uma empresa de placa de vídeo para quem joga" e virou "empresa de inteligência artificial", com os gamers "em segundo plano". O "corte do chip" na série 5000 é mais agressivo que na 3000: a RTX 5080 tem ~49% dos núcleos CUDA da 5090, contra ~83% da 3080 em relação à 3090. A fala diz "menos de 40%", o que exagera. DLSS e outros recursos de IA embarcados compensam em parte.

## Key Sources

- [[wiki/sources/kimi-k3-china-mercado-ia-open-source]]
- [[wiki/sources/palantir-ceo-token-tax-nvidia-scam-ia]] — deal com a Palantir; Nvidia como a única parte "correta" na economia de IA
- [[wiki/sources/google-nao-esta-perdendo-corrida-ia-memory-caching-gemini-live]] — TPUs do Google como complemento
- [[wiki/sources/big-techs-salarios-vagas-processo-de-aplicacao]] — Big Tech adjacente à FANG
- [[wiki/sources/frontpush-ia-o-futuro-da-ia-parte-1]]: FrontPUSH, módulo de IA, aula 5: GPUs que "nunca mais baixaram de preço"; "a própria Nvidia cortou o chip" (não identificado)
- [[wiki/sources/frontpush-ia-o-futuro-da-ia-parte-2]]: FrontPUSH, módulo de IA, aula 6: virou empresa de IA; corte do chip na série 5000

## NVIDIA como empregadora

Em [[wiki/sources/big-techs-salarios-vagas-processo-de-aplicacao]], listada entre as [[wiki/concepts/big-tech|Big Techs]] fora da FANG, com salários e escritórios globais.
