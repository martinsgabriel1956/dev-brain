---
type: source
title: "CAP Theorem, PACELC e Modelos de Consistência"
aliases: ["cap-theorem", "cap-pacelc"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/cap-theorem.md
source_url: ""
author: ""
date_published: "2026-04-17"
date_ingested: 2026-04-22
source_count: 0
tags: [system-design, distribuidos, cap, pacelc, consistencia, disponibilidade]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

CAP Theorem afirma que sistemas distribuídos só podem garantir 2 de 3 propriedades: Consistency, Availability e Partition Tolerance. Como P é obrigatório em redes reais, a escolha real é entre CP e AP. PACELC complementa o CAP adicionando a dimensão de latência para o caso sem partição (Else: Latency vs Consistency).

## Claims Principais

| Claim | Confiança |
|---|---|
| P (Partition Tolerance) não é opcional em sistemas distribuídos reais | Alta |
| A escolha real em CAP é CP vs AP — CA só existe em single-node | Alta |
| PACELC classifica sistemas como PA/EL ou PC/EC | Alta |
| Cassandra e DynamoDB são PA/EL; PostgreSQL, HBase e etcd são PC/EC | Alta |
| Linearizability garante que toda leitura retorna o write mais recente com custo de latência | Alta |
| Eventual consistency não garante quando os nós convergem, apenas que convergem | Alta |
| Vector Clocks implementam causal consistency sem relógio global | Alta |
| W + R > N garante strong consistency em sistemas quorum | Alta |

## Conceitos Abordados

- [[cap-theorem-concept]]
- [[pacelc]]
- [[linearizability]]
- [[eventual-consistency]]
- [[causal-consistency]]
- [[vector-clock]]
- [[quorum]]
- [[partition-tolerance]]
