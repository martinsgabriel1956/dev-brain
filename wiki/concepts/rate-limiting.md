---
type: concept
title: "Rate Limiting"
aliases: ["throttling", "rate limit", "token bucket", "sliding window"]
date_created: 2026-04-23
date_updated: 2026-08-14
source_count: 8
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

## Teste de Rate Limiting em Autopentest: "Resposta Sempre Tem Que Ser Sim"

[[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] trata rate limiting como um teste de checklist com resultado binário obrigatório: para toda rota mapeada, a pergunta "um usuário tem limite quantitativo de acesso?" precisa responder sim, sem exceção — moldura simples para verificar, rota por rota, que a defesa contra brute force existe antes de publicar o sistema.

## Contornando Rate Limit por Conta: Rotação de Free Tier

[[wiki/concepts/rotacao-de-contas-free-tier]] descreve o lado inverso desta página, visto do ponto de vista de quem sofre o rate limit em vez de quem o implementa: em vez de escalar uma única conta contra o limite do provider, cadastra-se múltiplas contas free tier e um [[wiki/concepts/ai-gateway-llm-router|gateway]] rotaciona entre elas quando a corrente esgota — efetivamente multiplicando a cota disponível ao custo de risco de detecção/banimento pelo provider.

## Key Sources

- [[sources/rate-limiting]]
- [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]] — rotação de contas free tier como forma de contornar rate limit por conta individual
- [[sources/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay]]
- [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]]
- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]]
- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]] — brute force e credential stuffing no login sem rate limiting
- [[wiki/sources/reacao-artigo-visual-algoritmos-load-balancing]] — o mesmo dilema estrutural (dropar a requisição vs. enfileirar e aceitar latência maior) aparece em load balancing sob carga, espelhando a escolha entre rejeitar (429) e enfileirar em rate limiting
- [[wiki/sources/back-pressure-producer-consumer-filas-bounded-admission-control]] — rate limit aplicado no **produtor** (não na borda de uma API pública): trava a taxa de produção na mesma capacidade que o consumidor consegue processar, como controle de [[wiki/concepts/back-pressure]]
