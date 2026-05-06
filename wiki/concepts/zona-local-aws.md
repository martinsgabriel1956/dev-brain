---
type: concept
title: "Zona Local AWS"
aliases: ["Local Zone", "AWS Local Zone"]
date_created: 2026-05-06
date_updated: 2026-05-06
source_count: 1
tags: ["aws", "edge", "baixa-latência", "infraestrutura"]
skill: tech-mentor-infra
status: stable
---

# Zona Local AWS (Local Zone)

Extensão de uma [[regiao-aws|Região AWS]] posicionada em grandes centros metropolitanos, fora da localização física da região principal. Permite executar workloads com latência de um dígito (single-digit ms) para usuários finais em cidades específicas.

## Quando Usar

- Jogos online que precisam de < 5ms
- Streaming de vídeo ao vivo com baixa latência
- Renderização em tempo real (VDI, simulações)
- Aplicações financeiras com requisito de latência rigoroso
- Machine learning de inferência próximo ao usuário

## Como Funciona

```
Região principal (ex: us-east-1, Virgínia)
└── Zona Local (ex: Los Angeles, CA)
    ├── Subconjunto de serviços AWS disponíveis
    ├── Conectada à região via backbone AWS
    └── Usuários LA → < 5ms latência
```

Os serviços disponíveis em Local Zones são um subconjunto dos serviços da região pai — nem tudo está disponível.

## Diferença: Local Zone vs. AZ

| | Local Zone | AZ |
|---|---|---|
| Localização | Centro metropolitano distante | Próxima às outras AZs da região |
| Propósito | Latência ultra-baixa para usuários | Resiliência e alta disponibilidade |
| Serviços | Subconjunto da região | Todos os serviços da região |

## Números Atuais (2025)

- **33 Zonas Locais** globalmente (combinado com Wavelength = 43 zonas de borda)

## Key Sources

- [[wiki/sources/aws-infraestrutura-global]]
