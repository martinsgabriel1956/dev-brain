---
type: source
title: "Strangler Fig Pattern"
aliases: ["Strangler Pattern", "Figueira Mata-Pau"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/strangler-fig.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-22
source_count: 0
tags: [strangler-fig, migração, legado, proxy, cdc, feature-flags]
skill: tech-mentor-backend
status: stable
---

# Strangler Fig Pattern

## TL;DR
O Strangler Fig substitui sistemas legados de forma incremental em três estágios: Transform (novo sistema em paralelo), Coexist (proxy roteia tráfego gradualmente com feature flags) e Eliminate (desligar o legado). A migração de banco é feita com CDC para sincronização bidirecional durante a transição.

## Claims Principais
| Claim | Confiança |
|---|---|
| Big-bang rewrites falham em ~80% dos casos — migração incremental é sempre preferível | Alta |
| Shadow mode permite validar comportamento do novo sistema sem impacto ao usuário | Alta |
| Expand-Contract é o padrão correto para mudança de contrato de API durante migração | Alta |
| CDC (Debezium) é a estratégia para sincronização bidirecional de banco durante transição | Alta |
| Roteamento consistente por user ID evita que o mesmo usuário experimente comportamentos diferentes | Alta |

## Conceitos Abordados
- [[strangler-fig]]
- [[cdc]]
- [[feature-flags]]
- [[expand-contract]]
- [[shadow-mode]]
- [[proxy-facade]]
- [[migração-incremental]]
