---
type: concept
title: "Rate Limiting"
aliases: ["throttling", "rate limit", "token bucket", "sliding window"]
date_created: 2026-04-23
date_updated: 2026-07-04
source_count: 3
tags: [rate-limiting, token-bucket, sliding-window, redis, throttling, protecao-api, gatekeeper, attack-surface]
skill: tech-mentor-backend
status: stub
---

# Rate Limiting

Mecanismo de controle que limita a frequência de requests para proteger APIs de abuso e sobrecarga.

**Quatro algoritmos:**
| Algoritmo | Precisão | Memória | Bursts |
|---|---|---|---|
| Fixed Window | Média — boundary burst | O(1) | Sim |
| Token Bucket | Alta | O(1) | Controlado |
| Sliding Window Log | Exata | O(N) | Não |
| Sliding Window Counter | ~90% | O(1) | Não |

**Escolha padrão:** Sliding Window Counter para APIs gerais. Token Bucket quando bursts controlados são desejados (upload em lote).

**Implementação:** Redis + Lua script (atomicidade). Hierarquia: global → por IP → por usuário → por endpoint.

## Dimensão de Segurança

Rate limiting é também responsabilidade do [[concepts/gatekeeper-pattern]] — aplicado na borda antes de chegar nos serviços internos. Reduz [[concepts/attack-surface]] contra brute force, credential stuffing e DDoS na camada de aplicação.

## Custo Financeiro Direto da Ausência de Rate Limit

Além do risco de segurança, não limitar rotas públicas gera custo direto: um `POST` público sem limite permite criação em massa de registros falsos (custo de armazenamento em banco), e uma API de envio de e-mail sem limite permite que um atacante esgote a cota paga do provedor. Login sem proteção habilita brute force de senha. Rate limiting em rotas sensíveis/caras é tão financeiro quanto defensivo.

## Key Sources

- [[sources/rate-limiting]]
- [[sources/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay]]
- [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]]
