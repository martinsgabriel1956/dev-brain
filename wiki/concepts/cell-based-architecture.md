---
type: concept
title: "Cell-Based Architecture"
aliases: ["arquitetura baseada em células", "scalability units", "cell architecture"]
date_created: 2026-09-15
date_updated: 2026-09-15
source_count: 1
tags: [cell-based-architecture, sharding, blast-radius, escalabilidade, resiliencia, fintech]
skill: tech-mentor-backend
status: stub
---

# Cell-Based Architecture

Particionar a infraestrutura inteira em unidades independentes ("células"), cada uma atendendo um subconjunto de usuários e falhando de forma isolada — diferente de [[wiki/concepts/sharding|sharding]] tradicional, que particiona só o banco de dados, cell-based architecture clona **toda a stack**: serviços, mensageria, cache, banco.

```
[Router Global]
   ├── Célula A (usuários 1-1M)   → DB-A / Cache-A / Workers-A / Kafka-A
   ├── Célula B (usuários 1M-2M)  → DB-B / Cache-B / Workers-B / Kafka-B
   └── Célula C (usuários 2M-3M)  → DB-C / Cache-C / Workers-C / Kafka-C

Falha na Célula B → afeta apenas 1/3 dos usuários
```

## Por que existe

Sharding de banco de dados resolve o gargalo **do banco**. Mas se o gargalo estiver em outro lugar — fila de mensageria, batch job, rede, ou até a disponibilidade de máquinas na cloud — particionar só o banco não ajuda. Cell-based architecture resolve isso clonando a unidade de escala inteira.

## Vantagens

- **Blast radius limitado** — falha ou deploy ruim numa célula afeta só a fração de usuários daquela célula, não a base inteira
- **Previsão de capacidade** — cada célula tem um teto de requisições conhecido e replicável
- **Deploys seguros** — dá para testar uma implantação numa célula antes de propagar para as demais

## Custo

Clonar toda a infraestrutura por célula é caro — cada célula paga o custo fixo de rodar sua própria cópia de cada serviço, mesmo com baixa utilização. O trade-off só compensa quando o gargalo real não é apenas o banco de dados.

## Caso Real: Scalability Units do Nubank

[[wiki/entities/nubank]] adotou esse padrão sob o nome **Scalability Units** depois que o sharding tradicional de banco de dados "bateu em limites físicos, incluindo a AWS ficando sem máquinas" para acompanhar o crescimento (2016). Cada um dos 20 shards brasileiros do Nubank é uma cópia completa da stack: microsserviços, clusters [[wiki/concepts/kafka|Kafka]] dedicados, bancos [[wiki/concepts/datomic|Datomic]] separados, redes isoladas. O roteamento acontece no login — o sistema resolve o shard do usuário uma vez por sessão e direciona todas as requisições subsequentes para lá. Ver [[wiki/sources/nubank-arquitetura-escala-122-milhoes-clientes]].

## Quem mais usa

Segundo `references/architecture-resilience-patterns.md` da skill `tech-mentor-backend`: Slack (cada workspace numa célula), AWS (Availability Zones são células no nível de cloud), Discord.

## Relação com outros conceitos

- [[wiki/concepts/sharding]] — cell-based architecture generaliza sharding: em vez de particionar só o banco, particiona a infraestrutura inteira
- [[wiki/concepts/microsservicos]] — pressupõe decomposição por domínio já feita; célula é uma cópia completa do conjunto de microsserviços
- [[wiki/concepts/circuit-breaker]] — ambos limitam blast radius de falha, em camadas diferentes (célula = infraestrutura; circuit breaker = chamada individual)

## Key Sources

- [[wiki/sources/nubank-arquitetura-escala-122-milhoes-clientes]] — caso real: Scalability Units do Nubank, motivação (AWS sem máquinas em 2016), roteamento por login, 20 shards no Brasil
