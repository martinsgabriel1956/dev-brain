---
type: concept
title: "CAP: classificação por comportamento, não por tecnologia"
aliases: ["CP e AP são comportamento", "banco gerenciado não elimina o CAP"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_count: 1
tags: [system-design, cap-theorem, bancos-de-dados, cloud]
skill: tech-mentor-system-design
status: draft
---

# CAP: classificação por comportamento, não por tecnologia

CP e AP descrevem **o que uma operação faz durante uma partição**, não um rótulo fixo para um produto inteiro.

- Muitos bancos permitem ajustar o comportamento por operação: [[wiki/concepts/mongodb]] (níveis de read/write concern), Cassandra (consistência configurável, foco em disponibilidade e escala) e [[wiki/concepts/dynamodb]] (leitura eventual vs. forte). Exemplos citados pelo autor do vídeo, sem detalhamento.
- **Serviços gerenciados de nuvem** ([[wiki/entities/amazon-web-services]], Azure, GCP) escondem replicação e backups, mas **não eliminam o CAP**: escolher entre configuração orientada a consistência ou a disponibilidade numa falha entre regiões é uma escolha CAP.
- Contraste: a tabela fixa CA/CP/AP por produto cobrada em concurso ([[wiki/sources/sgbd-conceitos-fundamentais-questoes-concurso]]) é simplificação didática; ver [[wiki/concepts/cap-theorem]].

Relação: [[wiki/concepts/cap-por-servico]] (granularidade), [[wiki/concepts/pacelc]] (ajuste de latência vs. consistência por operação).

## Key sources

- [[wiki/sources/teorema-cap-decisao-de-arquitetura-quando-a-comunicacao-falha-bernardo-lobato]]
