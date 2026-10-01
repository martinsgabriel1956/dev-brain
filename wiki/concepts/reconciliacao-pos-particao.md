---
type: concept
title: "Reconciliação pós-partição"
aliases: ["recuperação após partição", "o que o CAP não resolve"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_count: 1
tags: [system-design, cap-theorem, transacoes-distribuidas, saga]
skill: tech-mentor-system-design
status: stub
---

# Reconciliação pós-partição

O [[wiki/concepts/cap-theorem]] orienta **o que fazer durante a falha** (responder com dado possivelmente velho ou recusar), mas **não diz como arrumar a divergência depois** que a comunicação volta e, por exemplo, Pedido e Estoque precisam voltar a bater.

Esse é o território de [[wiki/concepts/distributed-transactions]]: [[wiki/concepts/saga-pattern]] (compensações) e [[wiki/concepts/two-phase-commit]]. O vídeo deixa o tema para outro episódio.

[external] Brewer (2012) trata a recuperação como etapa explícita: ao fim da partição o sistema, que registrou log durante o modo de partição, restaura a consistência e compensa erros cometidos no período ([[wiki/entities/eric-brewer]]). Caso real: [[wiki/concepts/github-incidente-2018-particao-de-rede]] (rede voltou em 43 s, reconciliação levou 24 h+).

Não confundir com [[wiki/concepts/reconciliacao]] (diffing do React).

## Key sources

- [[wiki/sources/teorema-cap-decisao-de-arquitetura-quando-a-comunicacao-falha-bernardo-lobato]]
