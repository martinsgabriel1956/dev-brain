---
type: concept
title: "DB Sharding"
aliases: ["sharding", "database sharding", "horizontal partitioning"]
date_created: 2026-04-23
date_updated: 2026-08-06
source_count: 7
tags: [sharding, escalabilidade, banco-de-dados, consistent-hashing, shard-key]
skill: tech-mentor-system-design
status: stub
---

# DB Sharding

Particionamento horizontal de um banco de dados em múltiplos nós independentes (shards) para ultrapassar os limites de uma única máquina.

**Três algoritmos:**
- **Range-based**: intervalo de valores por shard — range queries eficientes, mas hot spots em dados recentes.
- **Hash-based**: hash da shard key % N — distribuição uniforme, sem range queries, resharding move quase todos os dados.
- **Consistent hashing**: ring circular — resharding move apenas ~1/N dos dados. Usado por Redis Cluster (16.384 slots), Cassandra, DynamoDB.

**A decisão mais importante:** escolha da shard key — errar gera cross-shard queries (caras) ou hot spots.

**Considerar quando:** > ~10TB ou > ~100k QPS. Antes disso, read replicas + connection pooling resolvem.

## Roteamento por Módulo — Exemplo Passo a Passo

O roteador de hash-based sharding calcula `chave % N` (N = número de shards) para decidir onde inserir ou buscar um dado. Exemplo com N=3: `user_id=10` → `10 % 3 = 1` (resto 1) → shard 1; `user_id=30` → `30 % 3 = 0` → shard 0. Convenção: os índices de shard começam em **zero**, não em um — com N shards, o resto de uma divisão por N nunca pode ser N, então os índices válidos vão de 0 a N-1. Quando a shard key não é um inteiro (ex.: UUID), gera-se um **hash numérico não criptográfico** determinístico do valor antes de aplicar o módulo — a mesma entrada precisa sempre produzir o mesmo hash, senão o roteador erra o shard tanto na inserção quanto na busca. Ver [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]].

## Geração de ID em Sistema Shardeado

Auto-incremento nativo do banco não funciona em sistema distribuído (race condition entre shards). O fluxo correto: um **gerador de ID exclusivo/distribuído** (ex.: Snowflake do Twitter, ou implementação própria via Redis) gera o ID antes da inserção; esse ID passa pelo cálculo de hash/módulo para decidir o shard de destino, e só então o registro é inserido nesse shard. Ver [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]].

## Merge de Bases Shardeadas e Colisão de Chave

Um risco prático de usar chaves sequenciais (auto-incremento) em bases separadas por shard, cliente ou região: ao consolidar essas bases em um único banco (merge), IDs sequenciais colidem — o registro `1` do banco A e o registro `1` do banco B não podem coexistir sob a mesma chave. [[wiki/sources/uuid-quando-usar-pergunta-diogo]] descreve um caso real onde essa colisão exigiu semanas de reescrita manual de chaves. [[wiki/concepts/uuid]] é apontado como mitigação: por ter risco de colisão desprezível (128 bits, randômico), evita esse problema de raiz — o merge deixa de precisar de reescrita de chave.

## Key Sources

- [[sources/db-sharding]]
- [[sources/clusters]]
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]] — sharding (horizontal/vertical, partições, escolha de shard key) é citado como tópico de aprofundamento típico de entrevista sênior, junto de reader replicas e Federation
- [[wiki/sources/anatomia-entrevista-system-design-bigtech]] — tradeoff de escrita do SQL como motivador de sharding/NoSQL em sistemas de throughput alto
- [[wiki/sources/large-scale-vs-complex-architecture]] — sharding apresentado como resposta ao limite finito de TPS de qualquer banco de dados, dentro do princípio geral de "dividir para conquistar" em [[wiki/concepts/large-scale-architecture]]
- [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] — exemplo passo a passo do cálculo de módulo (por que a numeração de shard começa em zero) e do fluxo de geração de ID distribuído antes do roteamento
- [[wiki/sources/uuid-quando-usar-pergunta-diogo]] — merge de bases shardeadas com chave sequencial gera colisão; UUID evita o problema
