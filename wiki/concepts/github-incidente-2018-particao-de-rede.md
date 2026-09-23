---
type: concept
title: "Incidente do GitHub de 2018 (partição de rede)"
aliases: ["github outage 2018", "incidente github outubro 2018"]
date_created: 2026-09-23
date_updated: 2026-09-23
source_count: 1
tags: [system-design, sistemas-distribuidos, incidente, split-brain, cap-theorem, replicacao]
skill: tech-mentor-system-design
status: draft
---

# Incidente do GitHub de 2018 (partição de rede)

**TL;DR:** a troca de um equipamento de rede derrubou o link entre dois data centers (leste e oeste) do [[wiki/entities/github]]. A rede voltou em **43 s**, mas o serviço só normalizou após **mais de 24 h**.

## Sequência (segundo a fonte)

1. Dois data centers replicavam um para o outro.
2. O link caiu; a aplicação seguiu gravando no leste.
3. O lado oeste concluiu que o leste tinha caído e passou a aceitar escritas também ([[wiki/concepts/split-brain]]).
4. Com a rede de volta, cada lado tinha dados que o outro não tinha; como nenhum podia ser descartado, a reconciliação levou mais de 24 h.

## Lições

- O tempo de recuperação de uma partição é dominado pela **reconciliação de dados divergentes**, não pela duração da falha de rede.
- Pelo [[wiki/concepts/cap-theorem]] o sistema escolheu **disponibilidade** ([[wiki/concepts/disponibilidade-no-teorema-cap]]) e pagou com consistência.
- Um nó não distingue par caído, lento ou incomunicável ([[wiki/concepts/analogia-agencias-bancarias-cap]]); decidir "o outro morreu" sem [[wiki/concepts/raft-paxos|quórum]] leva a duas escritas concorrentes.

[external] O post-mortem oficial do GitHub tem mais detalhes (failover automático de MySQL); não verificado aqui: https://github.blog/news-insights/company-news/oct21-post-incident-analysis/

## Key sources

- [[wiki/sources/github-2018-cap-pacelc-particao-video]]
