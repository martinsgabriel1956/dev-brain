---
type: source
title: "Sharding: milhões de escritas por segundo, partition key e consistent hashing (Pedro Camaforte)"
aliases: ["sharding Pedro Camaforte", "como Instagram Discord Notion aguentam milhões de escritas"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/sharding-milhoes-de-escritas-partition-key-consistent-hashing-pedro-camaforte.md
source_url: ""
author: "Pedro Camaforte"
date_published: ""
date_ingested: 2026-10-08
source_count: 1
tags: [system-design, sharding, partition-key, consistent-hashing, hot-shard, saga-pattern, entrevista, escalabilidade, banco-de-dados]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Vídeo de [[wiki/entities/pedro-camaforte]] dedicado a [[wiki/concepts/sharding]], desdobramento do vídeo "como escalar escritas". Caminho: PostgreSQL aguenta ~10k escritas/s; tunado/vertical chega a ~50k; acima disso [[wiki/concepts/escalabilidade-horizontal]] via shards. Receita de entrevista: (1) definir a [[wiki/concepts/partition-key]] (alta cardinalidade, distribuição equilibrada, alinhada às queries); (2) escolher a distribuição — [[wiki/concepts/range-based-sharding]] e [[wiki/concepts/directory-based-sharding]] têm limites, o padrão é [[wiki/concepts/hash-based-sharding]] com [[wiki/concepts/consistent-hashing]] (+ [[wiki/concepts/virtual-node]]); (3) antecipar os três desafios — hot spots (shard dedicado ou chave composta), [[wiki/concepts/cross-shard-query]] (cache com TTL ou [[wiki/concepts/desnormalizacao]]) e consistência entre shards ([[wiki/concepts/two-phase-commit]] vs [[wiki/concepts/saga-pattern]]). Tese final: **faça conta** — sharding nem sempre é necessário e demonstrar isso passa senioridade.

## Key Claims

**Claim:** PostgreSQL bem configurado aguenta ~10k escritas/s; na máquina mais forte da AWS, ~50k; acima disso é preciso sharding.
**Evidence:** números dados pelo autor (remetem ao vídeo anterior), sem benchmark. Complementa o gatilho "> ~100k QPS" de [[wiki/concepts/db-sharding]].
**Confidence:** média (ordem de grandeza plausível; depende de hardware, schema e durabilidade).

**Claim:** Uma boa partition key tem alta cardinalidade, distribuição equilibrada e alinhamento com as queries; contra-exemplos: `is_premium` (2 shards), país (Vaticano vs Brasil), data do evento (shard do ano atual superaquece).
**Evidence:** exemplos Instagram (`user_id`), e-commerce (`order_id`), app financeiro, eventos. Ver [[wiki/concepts/partition-key]].
**Confidence:** alta; bate com [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]].

**Claim:** Range-based sofre de limite (alfabeto), concentração inicial num shard e hot shard nos usuários recentes; directory-based dá flexibilidade mas cria SPOF e dobra as chamadas; hash-based é o padrão por distribuir uniformemente.
**Evidence:** raciocínio passo a passo; ver [[wiki/concepts/range-based-sharding]], [[wiki/concepts/directory-based-sharding]], [[wiki/concepts/hash-based-sharding]].
**Confidence:** alta (ressalva [external]: o diretório pode ser replicado/cacheado, mitigando o SPOF e o overhead — não dito na fonte).

**Claim:** `hash % N` remaneja quase tudo ao mudar N; consistent hashing (anel, sentido horário) limita a migração à faixa do novo nó; virtual nodes evitam desequilíbrio.
**Evidence:** exemplo do anel 0–99 com shard 4 na posição 82. Usado por Cassandra e ScyllaDB.
**Confidence:** alta.

**Claim:** Hot spots (celebridade, post viral) resolvem-se com shard dedicado (diretório) ou partition key composta (`id + N/semana`), ao custo de leituras fan-out → cache.
**Evidence:** exemplo Neymar/CR7/Messi. Ver [[wiki/concepts/hot-shard]].
**Confidence:** alta.

**Claim:** Queries cross-shard devem ser exceção; se frequentes, a partition key está errada. Mitigações: cache com TTL (troca frescor por latência) e desnormalização (escrita dupla, leitura rápida).
**Evidence:** top 10 global; comentários da Joana. Ver [[wiki/concepts/cross-shard-query]], [[wiki/concepts/desnormalizacao]], [[wiki/concepts/cache-layer]].
**Confidence:** alta.

**Claim:** Para consistência entre shards, 2PC existe mas não é recomendado em larga escala; Saga com ações compensatórias é a escolha comum (iFood, Uber citados).
**Evidence:** exemplo Maria→João. Citação de iFood/Uber é só afirmação do autor. Ver [[wiki/concepts/saga-pattern]], [[wiki/concepts/two-phase-commit]].
**Confidence:** média-alta.

**Claim:** Em entrevista, faça contas (usuários, volume, tamanho por usuário, razão leitura/escrita) e conclua se sharding é necessário; 2M de usuários majoritariamente leitores podem gerar só ~500 escritas/s.
**Evidence:** orientação do autor. Ver [[wiki/concepts/entrevista-system-design]], [[wiki/concepts/back-of-envelope]].
**Confidence:** alta.

## Entities

- [[wiki/entities/pedro-camaforte]] — autor
- [[wiki/entities/cassandra]], [[wiki/entities/scylladb]] — bancos com sharding nativo via consistent hashing
- PostgreSQL ([[wiki/concepts/postgresql]]) — sharding não nativo, exige extensões

## Concepts

[[wiki/concepts/sharding]], [[wiki/concepts/db-sharding]], [[wiki/concepts/partition-key]], [[wiki/concepts/range-based-sharding]], [[wiki/concepts/directory-based-sharding]], [[wiki/concepts/hash-based-sharding]], [[wiki/concepts/consistent-hashing]], [[wiki/concepts/virtual-node]], [[wiki/concepts/hot-shard]], [[wiki/concepts/cross-shard-query]], [[wiki/concepts/desnormalizacao]], [[wiki/concepts/saga-pattern]], [[wiki/concepts/two-phase-commit]], [[wiki/concepts/escalabilidade-vertical]], [[wiki/concepts/escalabilidade-horizontal]], [[wiki/concepts/hotspot-analysis]]

## Open Questions / Contradições

- O título cita Instagram, Discord e Notion, mas o vídeo não mostra nenhuma arquitetura real deles — só exemplos hipotéticos. Não tratar como evidência sobre esses sistemas.
- Termos: o autor diz "escala vertical" uma vez onde quis dizer horizontal (transcrição); corrigido no raw.
- Diferença leve com [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]]: lá a chave por faixa de `user_id` é "boa chave, má distribuição"; aqui, o mesmo padrão é rotulado como problema da estratégia range. Mesma conclusão, enquadramento diferente — sem contradição.
- Como migrar dados online ao adicionar shard (dual write, backfill) não é coberto.

## Quotes

> "Engenharia é assim: a gente vai ter que calcular qual é o menor trade-off."
> "O padrão em entrevista é hash-based sharding com consistent hashing."
> "Sempre faça conta."
