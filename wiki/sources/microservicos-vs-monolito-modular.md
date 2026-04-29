---
type: source
title: "Microsserviços vs Monolito Modular"
aliases: []
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/microservicos-vs-monolito-modular.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-22
source_count: 0
tags: [microsserviços, monolito, arquitetura, conways-law, distributed-monolith]
skill: tech-mentor-backend
status: stable
---

# Microsserviços vs Monolito Modular

## TL;DR
A escolha entre monolito modular e microsserviços deve ser guiada por necessidade real — times independentes, escala diferencial, deploy independente — e não por hype. Começar com monolito modular e extrair serviços via Strangler Fig quando há razão concreta é o caminho saudável.

## Claims Principais
| Claim | Confiança |
|---|---|
| Um monolito modular bem estruturado tem fronteiras tão claras quanto microsserviços, sem o overhead operacional | Alta |
| Distributed monolith é o pior resultado: complexidade de microsserviços sem os benefícios | Alta |
| Conway's Law: a arquitetura do sistema reflete a estrutura de comunicação da organização | Alta |
| Big-bang rewrites falham em ~80% dos casos (Standish Group) | Média |
| Extrair serviço só faz sentido quando há time com ownership completo (código, banco, deploy, on-call) | Alta |

## Conceitos Abordados
- [[microsserviço]]
- [[monolito-modular]]
- [[distributed-monolith]]
- [[conways-law]]
- [[strangler-fig]]
- [[ownership]]
- [[bounded-context]]
