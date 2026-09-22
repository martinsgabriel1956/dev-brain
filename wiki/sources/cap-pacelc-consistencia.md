---
type: source
title: "CAP Theorem, PACELC e Modelos de Consistência (v2)"
aliases: ["cap-pacelc-consistencia"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/cap-pacelc-consistencia.md
source_url: ""
author: ""
date_published: "2026-03-29"
date_ingested: 2026-04-22
source_count: 0
tags: [system-design, cap, pacelc, consistencia, distribuido]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Aprofundamento em CAP e PACELC com foco no comportamento prático durante partições. Detalha os 5 modelos de consistência do mais forte (Linearizability) ao mais fraco (Eventual Consistency) e os mecanismos de convergência em sistemas AP: Read Repair, Anti-Entropy com Merkle Trees e Hinted Handoff.

## Claims Principais

| Claim | Confiança |
|---|---|
| CP durante partição pode recusar escritas mas continua servindo leituras | Alta |
| AP durante partição aceita escritas divergentes e reconcilia ao curar a partição | Alta |
| Sistemas PA/EL são mais rápidos em condições normais por não necessitarem coordenação | Alta |
| Sistemas PC/EC sempre coordenam via quorum mesmo sem partição | Alta |
| Read Repair corrige réplicas desatualizadas durante leitura com quorum | Alta |
| Anti-Entropy com Merkle Trees requer apenas O(log N) comparações para N registros | Alta |
| Hinted Handoff reduz janela de divergência quando réplica está offline | Alta |
| Vector Clocks detectam escritas concorrentes vs causalmente relacionadas | Alta |

## Conceitos Abordados

- [[concepts/cap-theorem-concept]]
- [[concepts/pacelc]]
- [[concepts/linearizability]]
- [[sequential-consistency]]
- [[concepts/causal-consistency]]
- [[concepts/eventual-consistency]]
- [[read-repair]]
- [[concepts/anti-entropy]]
- [[concepts/hinted-handoff]]
- [[concepts/vector-clock]]
- [[concepts/merkle-tree]]
