---
type: concept
title: "Amazon DynamoDB"
aliases: ["DynamoDB", "Dynamo"]
date_created: 2026-08-04
date_updated: 2026-08-18
source_count: 3
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

## Modos de Capacidade e Casos Ideais

Exemplo canônico de partition key + sort key: partition key = customer ID, sort key = order date → busca todos os pedidos de um cliente ordenados por data. Dois modos de capacidade: **Provisioned** (quando o padrão de tráfego é conhecido, mais barato) e **On-Demand** (quando não é, mais caro por request mas sem necessidade de planejamento). Casos ideais: sessões, leaderboards, IoT, carrinhos de compra, metadata — **não** ideal para analytics complexos ou dados fortemente relacionais, reforçando o contraste já registrado com [[wiki/concepts/rds]]. Ver [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]].

## Desenvolvimento Local com LocalStack

Antes de ir para produção, é possível desenvolver contra uma emulação local do DynamoDB via [[wiki/concepts/localstack]] — evita custo de nuvem e dependência de rede durante o desenvolvimento. [[wiki/entities/lucas-badico]] usa esse caminho no core do seu sistema de mentoria em Go, reservando DynamoDB para casos de uso já pensados nativamente para AWS (ex.: agendar notificação uma hora antes de uma mentoria), enquanto o banco relacional principal é PostgreSQL/PostGIS. Ver [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]].

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — exemplo de partition/sort key, modos Provisioned vs. On-Demand, e casos ideais vs. não ideais
- [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]] — uso via LocalStack para desenvolvimento local, em conjunto com PostgreSQL como banco principal
