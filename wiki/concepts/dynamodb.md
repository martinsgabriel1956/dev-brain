---
type: concept
title: "Amazon DynamoDB"
aliases: ["DynamoDB", "Dynamo"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
tags: ["aws", "dynamodb", "nosql", "banco-de-dados", "infra", "cloud"]
skill: tech-mentor-infra
status: stub
---

# Amazon DynamoDB

Banco de dados NoSQL gerenciado da AWS, modelo mental de key-value store (como um hash map). Cada item é acessado por duas chaves — **hash key** (partition key) e **sort key** — usadas para ganho de performance na distribuição/indexação dos dados; estruturalmente, apenas a hash key seria necessária. Esquema flexível, com as vantagens e desvantagens usuais de NoSQL.

## Pontos fortes

- **Escala do zero à escala global.** Global Tables permitem replicação e escalabilidade distribuída entre regiões.
- **Latência muito baixa**, especialmente com grandes volumes de dados, em comparação a outros bancos.
- **Bom suporte a eventos**: reage a mudanças de dados (streams) e também pode emitir eventos para outros serviços.

## Contras

- **Custo por request** pode ficar alto em workloads com volume alto de leitura/escrita — o modelo de cobrança é tipicamente pay-per-use por request/capacidade.
- Curva de aprendizado real para modelar dados com eficiência (design de partition/sort key, acesso por padrão de query em vez de normalização relacional).

## Relação com outros conceitos

- [[wiki/concepts/hashmap]] — modelo mental de acesso por chave
- [[wiki/concepts/rds]] — contraparte relacional da AWS
- [[wiki/concepts/consistent-hashing]] — mecanismo relacionado à distribuição de partições em bancos NoSQL de larga escala
- [[wiki/concepts/db-sharding]]

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
