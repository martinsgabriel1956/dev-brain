---
date: 2026-04-17
tags: [tech-mentor, arquitetura, estilos-arquiteturais, escalabilidade]
skill: tech-mentor-system-design/references/architecture-styles
level: avançado
---

# Space-Based Architecture

## Contexto
Projetada para **eliminar o banco de dados como gargalo central** em cenários de altíssima carga. O nome vem de "tuple space" — uma memória compartilhada distribuída originada no Linda (1986). É usada em sistemas de trading de alta frequência, plataformas de gaming em tempo real e leilões online.

O problema que resolve: quando o banco relacional centralizado não aguenta o throughput peak mesmo com sharding, caching e read replicas.

## Como Funciona

```
        Requests
            │
    ┌───────▼────────┐
    │  Virtual Middleware│  ← roteamento, sessão
    └───────┬────────┘
            │ distribui
    ┌───────▼──────────────────────────┐
    │         Processing Units (PUs)   │
    │  PU-1        PU-2        PU-3    │
    │  [In-Memory] [In-Memory] [In-Memory]│
    │  [Business]  [Business]  [Business]│
    └────────────┬─────────────────────┘
                 │ async replication
    ┌────────────▼─────────────────────┐
    │         Data Grid                │
    │  Hazelcast / Apache Ignite       │
    │  Replicação entre PUs            │
    └────────────┬─────────────────────┘
                 │ eventual write
    ┌────────────▼─────────────────────┐
    │         Data Pumps (async)       │
    │  Escrita no DB relacional        │
    └──────────────────────────────────┘
```

**Processing Unit (PU):** contém lógica de negócio + cópia do dado em memória. É stateful — cada PU carrega o subconjunto de dados que precisa para operar.

**Data Grid:** sincroniza o estado entre PUs usando replicação (Hazelcast, Apache Ignite, Redis Cluster).

**Data Pumps:** escrevem de forma assíncrona no banco persistente. O banco sai do caminho crítico das requisições.

**Virtual Middleware:** balanceia requisições considerando qual PU tem os dados relevantes (locality-aware routing).

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Throughput | Escala linearmente adicionando PUs | Complexidade operacional muito alta |
| Latência | Sem I/O de banco no caminho crítico | Inconsistência eventual entre PUs |
| Custo | Menos infraestrutura em pico com auto-scale | Custo base alto (memória é cara) |
| Confiabilidade | Sem single point of failure no DB | Perda de dados se o data pump falhar antes de persistir |
| Consistência | Eventual — aceitável para muitos casos | Não adequado onde ACID é mandatório |

## Quando Usar / Quando Evitar

**Usar quando:**
- Picos de carga são extremos e imprevisíveis (Black Friday, lançamentos simultâneos)
- Latência sub-milissegundo é requisito real, não aspiracional
- O domínio tolera consistência eventual (ex: reservas, scores, leilões)

**Evitar quando:**
- O sistema exige ACID forte (financeiro, saúde, jurídico)
- O time não tem maturidade com sistemas distribuídos stateful
- O budget para memória RAM distribuída é limitado
- O volume não justifica: um PostgreSQL bem tunado aguenta ~50k TPS

## Conceitos Relacionados
[[cap-theorem]] · [[modelos-de-consistencia]] · [[db-sharding]] · [[consistent-hashing]] · [[cqrs]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
