---
type: concept
title: "AWS ElastiCache"
aliases: ["ElastiCache", "Redis gerenciado AWS", "Memcached gerenciado AWS"]
date_created: 2026-08-17
date_updated: 2026-08-17
source_count: 1
tags: ["aws", "elasticache", "redis", "cache", "infra", "cloud"]
skill: tech-mentor-infra
status: stub
---

# AWS ElastiCache

Redis ou Memcached gerenciado pela AWS. Cache em memória com latência de sub-milissegundo, usado para sessões, cache de resultados de query, e leaderboards. Papel típico numa arquitetura de referência AWS: entre a camada de computação ([[wiki/concepts/aws-lambda|Lambda]] ou [[wiki/concepts/ec2|EC2]]) e o banco de dados relacional ([[wiki/concepts/rds|RDS]]) — a aplicação consulta o cache antes de bater no banco.

## Relação com outros conceitos

- [[wiki/concepts/cache]] — instância gerenciada do padrão geral de cache
- [[wiki/concepts/redis]] — ElastiCache é a versão gerenciada do Redis (ou Memcached) na AWS
- [[wiki/concepts/rds]] — tipicamente posicionado entre a aplicação e o RDS, absorvendo leituras repetidas

## Key Sources

- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — mencionado na "visão rápida" de serviços adicionais e usado na arquitetura de referência final (Lambda → ElastiCache → RDS)
