---
type: concept
title: "Storage Tiering"
aliases: ["storage hierárquico", "hot warm cold", "s3 glacier", "tiered storage"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, storage, s3, glacier, custo, infra]
skill: tech-mentor-system-design
status: stable
---

# Storage Tiering

Armazenamento em camadas de custo/acesso conforme a temperatura dos dados — quanto mais antigo e menos acessado, mais barato e mais lento.

## Camadas (AWS S3)

```
Hot — últimos 30 dias (~5% volume, ~80% tráfego)
  S3 Standard
  CDN TTL 365 dias
  Custo: referência

Warm — 30 dias a 1 ano
  S3 Standard-IA (Infrequent Access)
  ~40% mais barato que Standard
  TTL moderado no CDN

Cold — > 1 ano (~90% volume, <5% tráfego)
  S3 Glacier (~80% mais barato que Standard)
  CDN sem cache
  Restauração: 3-5h (Glacier) ou minutos (Glacier Instant Retrieval)
```

## Por que Funciona

Distribuição de acesso segue power law — cauda longa de conteúdo antigo tem volume enorme mas tráfego mínimo. Mover 90% do volume para Glacier com 80% de desconto → economia massiva sem impacto em UX para conteúdo popular.

## Automação

S3 Lifecycle Policy move objetos automaticamente entre tiers com base em idade:

```json
{
  "Rules": [{
    "Transitions": [
      { "Days": 30,  "StorageClass": "STANDARD_IA" },
      { "Days": 365, "StorageClass": "GLACIER" }
    ]
  }]
}
```

## Relacionado

[[concepts/cache-hot-path]] — mesmo princípio de concentrar recursos onde está o tráfego real.

## Key Sources

- [[sources/case-youtube-streaming]]
