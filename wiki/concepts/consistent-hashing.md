---
type: concept
title: "Consistent Hashing"
aliases: ["hash consistente", "anel de hashing", "consistent hash ring"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [consistent-hashing, sharding, sistemas-distribuidos, escalabilidade, banco-de-dados]
skill: tech-mentor-system-design
status: stub
---

# Consistent Hashing

Solução para o custo de resharding do hash-based sharding simples (`chave % N`). Ao invés de calcular o módulo direto pelo número de shards — o que faz **todo** o mapeamento mudar quando N muda —, consistent hashing distribui os shards em um **anel virtual**. Adicionar ou remover um shard só move a fração dos dados que caía naquele trecho específico do anel, não a totalidade dos dados.

## Por Que o Hash Simples Falha ao Reshardar

Com hash-based sharding puro, o roteador calcula `chave % N`. Se N muda (ex.: de 3 para 5 shards), o resultado do módulo muda para praticamente todas as chaves já existentes — o roteador passa a apontar para o shard errado, e a única correção é um **rebalanceamento completo**: mover todos os dados entre os bancos. Ver [[wiki/concepts/db-sharding]].

## Mecanismo do Anel

Shards são posicionados em pontos de um anel (0° a 360°, ou um espaço de hash circular). Cada chave é mapeada para um ponto do anel e roteada para o próximo shard no sentido horário. Adicionar um novo shard entre dois existentes move apenas os dados que caíam naquele intervalo específico para o novo shard — o restante do mapeamento permanece intacto.

## Uso em Bancos Não Relacionais

É o mecanismo por trás de sharding nativo em bancos distribuídos — citado como o funcionamento interno de sistemas como Redis Cluster (16.384 hash slots), Cassandra e DynamoDB. Implementar esse anel manualmente é complexo; em muitos casos compensa mais migrar para um banco com essa capacidade nativa do que reimplementar o mecanismo por conta própria.

## Relação com outros conceitos

- [[wiki/concepts/db-sharding]] — consistent hashing como uma das três estratégias de sharding, ao lado de range-based e hash-based simples
- [[wiki/concepts/sharding]] — resharding é citado como a maior dor operacional do sharding; consistent hashing é a mitigação padrão

## Key Sources

- [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] — anel virtual como solução ao custo de resharding do módulo simples, citado como mecanismo interno de bancos não relacionais com sharding nativo
