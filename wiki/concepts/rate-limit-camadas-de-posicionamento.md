---
type: concept
title: "Rate Limit: Onde Posicionar na Arquitetura"
aliases: ["camadas de rate limit", "rate limit na borda, gateway e aplicação"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 2
tags: [rate-limiting, arquitetura, borda, api-gateway, defesa-em-profundidade]
skill: tech-mentor-backend
status: draft
---

# Rate Limit: Onde Posicionar na Arquitetura

Segundo [[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]], três lugares, cada um trocando **contexto de negócio** por **proximidade da borda**:

| Camada | Vantagem | Limite |
|---|---|---|
| **Aplicação** | máximo contexto (usuário, plano, tenant, endpoint, permissões); controle total | cada instância precisa do mesmo estado ([[wiki/concepts/rate-limit-estado-compartilhado]]); mais complexidade |
| **API Gateway / LB / proxy reverso** | política central; poupa os serviços; gateway tem auth, identificação de cliente, roteamento | menos contexto de domínio; LB é mais genérico que gateway |
| **Borda (CDN/WAF/nuvem)** | bloqueia cedo, barato; parte da defesa contra DDoS | quase sem lógica de negócio |

As camadas **combinam**: não é preciso escolher uma. Ferramentas citadas: borda em [[wiki/entities/cloudflare]] (regras por URL, país etc.); gateway em [[wiki/entities/spring-cloud-gateway]] e [[wiki/entities/kong]]; aplicação em [[wiki/entities/bucket4j]] (Java) e [[wiki/entities/nestjs-throttler]] (NestJS).

Relacionados: [[wiki/concepts/api-gateway]], [[wiki/concepts/waf]], [[wiki/concepts/cdn]], [[wiki/concepts/load-balancer]], [[wiki/concepts/ddos-syn-flood]], [[wiki/concepts/rate-limiting]]. Exemplo prático de duas camadas em outra fonte: proxy + app em [[wiki/concepts/rate-limiting]] (OMXTerm).

Parte 2 resume: decisão 1 = onde ([[wiki/concepts/rate-limit-camadas-de-posicionamento]]), decisão 2 = como ([[wiki/concepts/rate-limit-escolha-de-algoritmo]]).

## Key Sources

- [[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]
- [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]] — decisão 'onde' vs. decisão 'como'
