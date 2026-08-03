---
type: concept
title: "Sharding"
aliases: ["database sharding", "particionamento horizontal", "shard", "shard key"]
date_created: 2026-06-26
date_updated: 2026-08-03
source_count: 2
tags: [system-design, banco-de-dados, sharding, escalabilidade, distribuido]
skill: tech-mentor-system-design
status: stub
---

# Sharding

Estratégia de escalar banco de dados horizontalmente **dividindo os dados em múltiplos bancos** (shards). Cada shard contém um subconjunto dos dados — nenhum shard tem tudo.

```
Shard 1: usuários 1–1.000.000
Shard 2: usuários 1.000.001–2.000.000
Shard 3: usuários 2.000.001–3.000.000
```

A chave que determina qual shard recebe qual dado é chamada de **shard key**.

## Por que sharding existe

Bancos de dados são [[stateless-nao]] por natureza — eles *são* o estado. [[escalabilidade-vertical]] tem teto físico. [[replicacao-de-banco]] ajuda com leitura, mas escrita ainda vai para um único primário. Sharding divide tanto leitura quanto escrita.

## Trade-offs

| Vantagem | Desvantagem |
|---|---|
| Escala leitura e escrita | Queries cross-shard são complexas e lentas |
| Sem teto teórico de dados | Joins entre shards são proibidos ou caros |
| Cada shard é menor e mais rápido | Re-sharding (redistribuir dados) é doloroso |
| Falha de um shard não derruba todo o sistema | Shard key mal escolhida cria hot spots |

## Escolha da shard key

A escolha da shard key é crítica:

- **Distribuição uniforme** — evita hot spots onde um shard recebe 80% do tráfego
- **Colocalização de dados relacionados** — queries que acessam dados do mesmo usuário devem ir para o mesmo shard
- **Imutabilidade** — a shard key não deve mudar após a inserção

## Quando usar

- Volume de dados supera a capacidade de um único servidor
- Writes por segundo ultrapassam o limite do banco primário
- [[replicacao-de-banco]] não é suficiente (só escala reads)

## Alternativas antes do sharding

1. [[escalabilidade-vertical]] — mais RAM/CPU no banco (mais simples)
2. [[replicacao-de-banco]] — read replicas para aliviar leitura
3. [[cache]] — reduzir hits ao banco antes de distribuí-lo

> **Regra:** sharding é complexo. Esgote as alternativas primeiro.

## Relação com outros conceitos

- [[replicacao-de-banco]] — a outra estratégia de escalar banco; complementar ao sharding
- [[cap-theorem]] — sharding força decisões sobre consistência vs disponibilidade
- [[escalabilidade-horizontal]] — sharding é a escalabilidade horizontal aplicada ao banco de dados
- [[gargalo]] — banco é o gargalo mais comum; sharding é o último recurso para ele

- [[wiki/concepts/control-plane]] — camada de coordenação necessária para mover dados/usuários entre shards
- [[wiki/concepts/large-scale-architecture]] — sharding como técnica central do princípio "dividir para conquistar"

## Key sources

- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
- [[wiki/sources/large-scale-vs-complex-architecture]] — sharding citado como exemplo de técnica que escala TPS/resiliência sem necessariamente tornar a arquitetura "complexa" em alto nível; movimentação de usuário entre shards como caso concreto que exige control plane
