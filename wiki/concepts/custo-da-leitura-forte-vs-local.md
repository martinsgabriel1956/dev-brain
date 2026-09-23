---
type: concept
title: "Custo da leitura forte vs. leitura local"
aliases: ["leitura forte vs local", "strong read vs local read", "round trip ao quórum"]
date_created: 2026-09-23
date_updated: 2026-09-23
source_count: 1
tags: [system-design, consistencia, latencia, pacelc, quorum]
skill: tech-mentor-system-design
status: draft
---

# Custo da leitura forte vs. leitura local

Uma leitura **local** responde no primeiro nó; uma leitura **forte** exige que o nó consulte o quórum, somando um round trip. É a face cotidiana do [[wiki/concepts/pacelc]] (trecho "Else": latência vs. consistência).

Medição do autor (teste local, 3 nós, sem rede real entre zonas):

| Situação | Leitura local | Leitura forte | Escrita |
|---|---|---|---|
| Rede saudável | ≈ 0,05 ms | ≈ +0,19 ms (round trip ao quórum) | n/d |
| Nó isolado | responde na hora, dado pré-partição | falha | 5 s de timeout, falha |

Leitura: o custo da consistência é pago **em toda leitura forte, todo dia**, não só em partições. Números não generalizam para produção multi-zona/região (ressalva do autor). Relacionado: [[wiki/concepts/consistency-models]], [[wiki/concepts/raft-paxos]], [[wiki/concepts/eventual-consistency]].

## Key sources

- [[wiki/sources/github-2018-cap-pacelc-particao-video]]
