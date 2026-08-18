---
type: concept
title: "API Gateway"
aliases: ["api gateway", "gateway de api", "ponto único de entrada de api"]
date_created: 2026-07-23
date_updated: 2026-08-18
source_count: 7
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
| AWS API Gateway | Managed | Stack AWS — roteia por rota até [[wiki/concepts/aws-lambda|Lambdas]] específicos (ex.: `/user` → Lambda de usuário), timeout e custo por request próprios, além da latência adicional inerente a passar por mais uma camada |
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

## AWS API Gateway — REST vs. HTTP API

Duas opções na AWS: **REST API** (mais features) e **HTTP API** (mais simples, mais barato). Recomendação prática: comece com HTTP API, migre pra REST só se precisar de uma feature específica que falte. Integração mais comum é com [[wiki/concepts/aws-lambda|Lambda]], mas o gateway também pode fazer proxy direto para EC2, ECS, ou escrever direto no [[wiki/concepts/dynamodb|DynamoDB]] sem Lambda no meio. Autorização: IAM (chamada service-to-service), Cognito (validação de JWT), Lambda Authorizer (lógica customizada). Throttling protege o backend de sobrecarga; domínios customizados usam certificado via [[wiki/concepts/certificado-ssl-acm|ACM]]. Ver [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]].

## Onde entra na linha do tempo histórica das APIs

Segundo [[wiki/sources/historia-e-evolucao-das-apis-bernardo-lobato]], o API Gateway (junto de OAuth e OpenID Connect) é apontado como um dos padrões que consolidam nos anos 2020 justamente porque o consumo massivo de APIs — resultado das duas ondas de [[wiki/concepts/api-economy]] nas décadas anteriores — passou a exigir segurança e governança centralizadas, não só roteamento.

## Padrões Relacionados

- **API Composition** — orquestração e agregação de múltiplos endpoints em um único resultado. Ver [[wiki/concepts/api-composition]].
- **BFF (Backend for Frontend)** — tipo específico de Gateway, um backend por tipo de cliente. Ver [[wiki/concepts/bff-pattern]].
- **Gatekeeper Pattern** — a formalização de segurança do mesmo princípio de ponto único de entrada obrigatório. Ver [[wiki/concepts/gatekeeper-pattern]].

## Key Sources

- [[wiki/sources/api-gateway-bff]]
- [[wiki/sources/api-gateway-padrao-essencial-arquiteturas-distribuidas]]
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]] — API Gateway aparece como conhecimento esperado a partir do nível pleno, junto de workers e load balancer
- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]] — no ecossistema AWS, é a forma mais comum de encaminhar requests até [[wiki/concepts/aws-lambda]]; comparado explicitamente ao [[wiki/concepts/load-balancer]] (mecanismo parecido, intuito diferente — não é balancear carga, é rotear por endpoint)
- [[wiki/sources/infraestrutura-como-codigo-cdk-aws]] — usado como componente central de uma stack de exemplo descrita em [[wiki/concepts/infraestrutura-como-codigo|IaC]] (`/user`, `/products` roteando para Lambdas distintos, sem que o backend tenha acesso direto à internet)
- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — REST API vs. HTTP API, integração com Lambda/EC2/ECS/DynamoDB, e as três formas de autorização (IAM, Cognito, Lambda Authorizer)
- [[wiki/sources/historia-e-evolucao-das-apis-bernardo-lobato]] — API Gateway como resposta de governança/segurança ao consumo massivo de API nos anos 2020, junto de OAuth e OpenID Connect
