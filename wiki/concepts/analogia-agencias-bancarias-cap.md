---
type: concept
title: "Analogia das agências bancárias (CAP)"
aliases: ["agências de banco e malote", "recusar ou pagar com caixa local"]
date_created: 2026-09-23
date_updated: 2026-09-23
source_count: 1
tags: [system-design, cap-theorem, analogia, particao-de-rede]
skill: tech-mentor-system-design
status: draft
---

# Analogia das agências bancárias (CAP)

Agências atendem com o dinheiro do caixa local e sincronizam com a matriz por malote. Se a estrada fecha e o malote não chega, há duas opções:

- **Recusar o saque** = consistência (CP).
- **Pagar com o caixa local e acertar depois** = disponibilidade (AP).

Pontos-chave da fonte:
- A decisão só existe **com o canal fechado**; com a rede de pé, não há dilema (mas há custo, ver [[wiki/concepts/pacelc]]).
- Do ponto de vista do nó, o par pode estar **caído, lento ou incomunicável**, e os três chegam como **silêncio**, sem aviso.

Ver [[wiki/concepts/cap-theorem]] e [[wiki/concepts/github-incidente-2018-particao-de-rede]].

## Key sources

- [[wiki/sources/github-2018-cap-pacelc-particao-video]]
