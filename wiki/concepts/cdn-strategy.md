---
type: concept
title: "CDN Strategy"
aliases: ["cdn", "content delivery network", "edge cache", "cloudfront"]
date_created: 2026-04-22
date_updated: 2026-07-30
source_count: 2
tags: [system-design, cdn, cache, infra, performance, video, live-streaming]
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

## CDN em Live Streaming — TTL de Manifesto Muito Mais Curto

Em VOD, o manifesto tem TTL de ~60s porque só muda quando o vídeo recebe capítulos. Em **live streaming**, o manifesto muda constantemente — novos segmentos são publicados a cada poucos segundos enquanto a transmissão está no ar — então o TTL do manifesto precisa ser da ordem de segundos, não de dezenas de segundos. [[wiki/sources/delay-tv-aberta-vs-youtube-live-latencia-streaming]] mostra o outro lado dessa moeda: a CDN reduz a distância física até o espectador, mas não elimina a necessidade de cada player consultar o manifesto e pedir seu próprio próximo segmento — essa consulta repetida, somada ao buffer de leitura antecipada, é o que compõe a maior parte da [[wiki/concepts/latencia-streaming-ao-vivo]] em relação a uma transmissão por radiodifusão (TV aberta), que não depende de CDN nem de sessão individual por espectador.

## Relacionado

[[concepts/cache-hot-path]] — mesmo princípio de servir do mais próximo/rápido. CDN é a camada de cache mais extrema.

## Key Sources

- [[sources/case-youtube-streaming]]
- [[wiki/sources/delay-tv-aberta-vs-youtube-live-latencia-streaming]] — CDN em live streaming e o contraste com radiodifusão (TV aberta)
