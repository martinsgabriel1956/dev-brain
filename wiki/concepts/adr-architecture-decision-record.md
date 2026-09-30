---
type: concept
title: "ADR — Architecture Decision Record"
aliases: ["ADR", "Architecture Decision Record"]
date_created: 2026-05-17
date_updated: 2026-09-30
source_count: 4
tags: [adr, documentação, arquitetura, decisão]
skill: tech-mentor-system-design
status: stub
---

# ADR — Architecture Decision Record

Registro histórico de uma decisão arquitetural já tomada, com contexto, alternativas consideradas e motivo da escolha. Serve para rastreabilidade — futuros membros do time entendem *por que* o sistema é como é.

Diferente do [[rfc-request-for-comments]] (decisão em aberto) e do [[wiki/concepts/trd-technical-requirements-document]] (especificação para implementar).

Formato clássico: título · status · contexto · decisão · consequências.

## Key Sources

- [[wiki/sources/trd-technical-requirements-document]]
- [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] — ADRs (e comentários explicando decisões não usuais) como forma de externalizar o *porquê* das decisões e reduzir a dependência do [[wiki/concepts/bus-factor|Dev Gandalf]]
- [[wiki/sources/tres-mentiras-que-te-reprovam-em-entrevistas-de-arquitetura-de-sistemas]] — "justificar cada escolha" como o que a entrevista de arquitetura de fato avalia; mesma lógica do ADR aplicada ao vivo
- [[wiki/sources/openrouter-como-profissional-provedores-quantizacao-retencao-fallback-ronald-hulk]] — escolha de modelo+provedor documentada em ADR/PR com tabela antes de implementar
