---
type: concept
title: "LPAR (Partição Lógica)"
aliases: ["logical partition", "PR/SM", "partição lógica de mainframe"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [mainframe, virtualizacao, lpar, prsm, isolamento, ibm-z]
skill: tech-mentor-infra
status: stub
---

# LPAR (Partição Lógica)

Partição lógica de um [[wiki/concepts/mainframe]]: o recurso PR/SM (Processor Resource/System Manager) divide um único equipamento físico em várias LPARs, cada uma rodando seu próprio sistema operacional, **isolada e independente** das demais. É a base do compartilhamento de recursos no mainframe, décadas antes da cloud pública — forma de [[wiki/concepts/virtualizacao]].

## Por que importa para MaaS

Se dá para compartilhar uma máquina entre sistemas com isolamento, dá para compartilhar entre **empresas**: o provedor entrega uma ou mais LPARs a cada cliente — a base do [[wiki/concepts/mainframe-as-a-service]] e do [[wiki/concepts/multi-tenancy|multitenant]] em mainframe. A fonte diz que o detalhe de PR/SM/LPAR não é explicado no vídeo (fica para outro conteúdo/livro do autor). [external] https://en.wikipedia.org/wiki/Logical_partition

## Key Sources

- [[wiki/sources/mainframe-as-a-service-casas-bahia-sulamerica-kyndryl]] — PR/SM cria LPARs; base do compartilhamento e do MaaS
