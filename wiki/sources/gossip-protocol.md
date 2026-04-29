---
type: source
title: "Gossip Protocol"
aliases: ["gossip-protocol", "epidemic-protocol"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/gossip-protocol.md
source_url: ""
author: ""
date_published: "2026-04-14"
date_ingested: 2026-04-22
source_count: 0
tags: [distributed-systems, protocolos, coordenacao, escalabilidade, gossip]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Gossip Protocol propaga informação em clusters distribuídos de forma epidêmica: cada nó fala periodicamente com K vizinhos aleatórios. A convergência é logarítmica — O(log N / log K) ciclos para todos os nós saberem de uma mudança. Cassandra usa gossip para membership, detecção de falhas (via SWIM) e anti-entropy com Merkle Trees.

## Claims Principais

| Claim | Confiança |
|---|---|
| Convergência ocorre em log(N)/log(K) ciclos com N nós e fanout K | Alta |
| Gossip não requer coordenador central — sem SPOF | Alta |
| SWIM combina gossip com indirect probing para detectar falhas com menos falsos positivos | Alta |
| Anti-entropy com Merkle Trees permite detectar divergências com O(log N) comparações | Alta |
| Cassandra usa gossip a cada segundo com fanout 3 para membership e estado do cluster | Alta |
| Para operações de consistência forte (locks, transações) gossip não é adequado | Alta |
| Gossip tem latência de propagação em segundos vs milissegundos de Raft/etcd | Alta |

## Conceitos Abordados

- [[gossip-protocol]]
- [[swim-protocol]]
- [[anti-entropy]]
- [[merkle-tree]]
- [[membership-protocol]]
- [[eventual-consistency]]
- [[cluster-membership]]
