---
type: source
title: "Quorum — Leitura, Escrita e o Modelo Dynamo"
aliases: ["quorum", "dynamo-quorum"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/quorum.md
source_url: ""
author: ""
date_published: "2026-04-16"
date_ingested: 2026-04-22
source_count: 0
tags: [distributed-systems, quorum, dynamo, replicacao]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Quorum permite sistemas distribuídos balancear consistência e disponibilidade na replicação via parâmetros N (réplicas), W (write quorum) e R (read quorum). A regra R + W > N garante strong consistency. Sloppy Quorum com Hinted Handoff mantém alta disponibilidade mesmo com nós indisponíveis.

## Claims Principais

| Claim | Confiança |
|---|---|
| R + W > N garante que toda leitura vê o write mais recente | Alta |
| W > N/2 garante durabilidade da escrita | Alta |
| Com N=3, W=2, R=2 é o balanço padrão do Cassandra (LOCAL_QUORUM) | Alta |
| W=1, R=1 com N=3 tem 2/3 de chance de ler dado stale | Alta |
| Sloppy Quorum aceita confirmações de nós substitutos quando alvo está down | Alta |
| Hinted Handoff entrega writes pendentes quando réplica volta | Alta |
| Cassandra expõe model de quorum diretamente na API com consistency levels | Alta |

## Conceitos Abordados

- [[quorum]]
- [[replicacao]]
- [[sloppy-quorum]]
- [[hinted-handoff]]
- [[consistent-hashing]]
- [[vector-clock]]
- [[eventual-consistency]]
- [[dynamo-paper]]
