---
type: source
title: "Case: Twitter/X Feed"
aliases: ["twitter feed", "x feed", "timeline feed"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/case-twitter-feed.md
source_url: ""
author: ""
date_published: "2026-03-29"
date_ingested: 2026-04-22
source_count: 0
tags: [system-design, twitter, fan-out, timeline, cache, kafka, redis]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

O feed do Twitter é o caso clássico de **fan-out de escrita em escala extrema**. A solução é híbrida: fan-out on write para usuários normais (pré-computa timelines no Redis) e fan-out on read para celebridades (>10k followers), porque propagar 1 tweet de 150M seguidores on-write é inviável. O Timeline Service mescla as duas fontes na leitura.

## Claims Principais

| Claim | Confiança |
|---|---|
| Fan-out on write para usuários normais (<10k followers), on read para celebridades | Alta |
| Redis Sorted Set como cache de timeline com TTL de 7 dias e máximo de 800 tweet_ids | Alta |
| Kafka desacopla o post do fan-out e permite replay em falha | Alta |
| Tweets DB em Cassandra/MySQL sharded por user_id com clustering key por tweet_id DESC | Alta |
| Upload de mídia direto ao S3 via presigned URL (não passa pelo backend) | Alta |
| Ratio leitura:escrita de ~100:1 nos tweets | Alta |
| 500M tweets/dia = ~5.800 writes/s; fan-out gera ~1.15M writes Redis/s (pico) | Média |

## Conceitos Abordados

- [[fan-out-on-write]]
- [[fan-out-on-read]]
- [[cache]]
- [[consistent-hashing]]
- [[mensageria]]
- [[db-sharding]]
- [[cdn]]
- [[snowflake-id]]
