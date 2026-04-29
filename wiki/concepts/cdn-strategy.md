---
type: concept
title: "CDN Strategy"
aliases: ["cdn", "content delivery network", "edge cache", "cloudfront"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, cdn, cache, infra, performance, video]
skill: tech-mentor-system-design
status: stable
---

# CDN Strategy

Rede de servidores de borda (PoPs) que serve conteúdo do nó mais próximo do usuário — elimina latência intercontinental.

## Fluxo

```
Request → CDN edge node mais próximo
  hit  → serve direto (sub-10ms)
  miss → busca na origem (S3) → cacheia no edge → serve
```

## TTL por Tipo de Conteúdo

| Conteúdo | TTL | Motivo |
|---|---|---|
| Segmentos de vídeo | 365 dias | Imutáveis após geração |
| Manifesto HLS/DASH | 60s | Pode mudar (novos segmentos) |
| Thumbnails | 30 dias | Raramente mudam |
| Assets estáticos (JS/CSS) | Hash no nome → 1 ano | Imutáveis por versão |

## Imutabilidade = Cache Agressivo

Segmentos de vídeo **nunca mudam** após geração. TTL máximo, sem invalidação. Manifesto tem TTL curto porque pode receber novos segmentos (live stream, capítulos adicionados).

## Pré-aquecimento

Ao detectar crescimento anômalo de views → push proativo do vídeo para edges estratégicos. Evita cache miss em cascata quando conteúdo viraliza e milhões de usuários pedem o mesmo segmento simultaneamente.

## Scale

28 Tbps de saída distribuído entre centenas de PoPs globais — nenhum edge sozinho processa isso.

## Relacionado

[[concepts/cache-hot-path]] — mesmo princípio de servir do mais próximo/rápido. CDN é a camada de cache mais extrema.

## Key Sources

- [[sources/case-youtube-streaming]]
