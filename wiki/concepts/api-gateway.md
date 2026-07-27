---
type: concept
title: "API Gateway"
aliases: ["api gateway", "gateway de api", "ponto único de entrada de api"]
date_created: 2026-07-23
date_updated: 2026-07-27
source_count: 3
tags: [api-gateway, arquitetura-distribuida, gatekeeper, roteamento, edge-functions, single-point-of-failure]
skill: tech-mentor-backend
status: stable
---

# API Gateway

Componente centralizado que funciona como único ponto de entrada externo para uma arquitetura distribuída. O client conhece apenas o endereço do Gateway; ele é responsável por rotear cada requisição ao serviço interno correto.

## Problema que Resolve

Sem Gateway, um client (ex.: app mobile) precisa conhecer o endereço de cada serviço individualmente — login, dados pessoais, pedidos, pagamentos — multiplicando chamadas de rede, latência e dados irrelevantes trafegados. Subir uma nova instância de um serviço também não resolve nada sozinho: sem um componente central, o client não tem como descobrir o novo endereço (ver [[wiki/concepts/service-discovery]]) e continua batendo no serviço antigo.

## Responsabilidades

```
Cliente → [TLS Termination]
        → [Autenticação / Autorização]
        → [Rate Limiting]
        → [Roteamento]
        → [Mapeamento de Payload — ex.: REST ↔ gRPC/GraphQL]
        → [Cache / Log / Circuit Breaker]
        → Serviço Backend
```

- **Roteamento** dos endpoints do client para os serviços internos.
- **Autenticação e autorização** de borda.
- **Mapeamento de payload** entre protocolos distintos (JSON REST → gRPC, GraphQL, etc.) quando serviços internos usam tecnologias diferentes.
- **Funções de borda** (edge functions): cache, log, rate limit — ver seção abaixo.

## Ferramentas de Mercado

| Ferramenta | Tipo | Caso de uso ideal |
|---|---|---|
| Kong | Open source, leve, extensível | Microsserviços, multicloud |
| AWS API Gateway | Managed | Stack AWS |
| NGINX | Proxy adaptado a Gateway | Alta performance |
| Traefik | Cloud-native | Kubernetes, Docker |
| Spring Cloud Gateway | Ecossistema Spring | Evolução do Zuul (Netflix) |
| Envoy | Proxy / data plane programável | Service mesh |

Implementação própria também é viável — o Gateway é tecnicamente simples e há frameworks maduros em qualquer linguagem para cobrir suas funções de borda.

## Edge Functions — Cuidado com o Acúmulo

Autenticação, autorização, cache, log e rate limit são comumente atrelados ao Gateway. O risco: acoplar funções demais sem critério transforma o Gateway em **gargalo** — ele deixa de ser rápido e eficiente, que é seu requisito central. Usar edge functions exige avaliar o impacto real de cada uma antes de adicionar, não empilhar por padrão. Ver [[wiki/concepts/over-engineering]].

## Single Point of Failure

O Gateway concentra todo o tráfego externo — se ele cai, a arquitetura inteira fica inacessível. Mitigação:

- Escalabilidade horizontal (múltiplas instâncias)
- Balanceamento de carga entre instâncias
- Observabilidade (métricas de latência p50/p95/p99, taxa de erro por rota, upstream health)

Em ambientes multi-região, mitiga-se com latency-based routing e health checks automáticos (ex.: AWS Route 53 + failover).

## API Gateway vs. Service Mesh

| | API Gateway | Service Mesh |
|---|---|---|
| Onde vive | Borda (entrada externa) | Entre serviços internos |
| Tráfego | Norte-sul (cliente → sistema) | Leste-oeste (serviço → serviço) |
| Foco | Auth, rate limit, routing | mTLS, retries, circuit breaking |

Complementares, não substitutos — ver [[wiki/concepts/service-mesh]].

## Padrões Relacionados

- **API Composition** — orquestração e agregação de múltiplos endpoints em um único resultado. Ver [[wiki/concepts/api-composition]].
- **BFF (Backend for Frontend)** — tipo específico de Gateway, um backend por tipo de cliente. Ver [[wiki/concepts/bff-pattern]].
- **Gatekeeper Pattern** — a formalização de segurança do mesmo princípio de ponto único de entrada obrigatório. Ver [[wiki/concepts/gatekeeper-pattern]].

## Key Sources

- [[wiki/sources/api-gateway-bff]]
- [[wiki/sources/api-gateway-padrao-essencial-arquiteturas-distribuidas]]
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]] — API Gateway aparece como conhecimento esperado a partir do nível pleno, junto de workers e load balancer
