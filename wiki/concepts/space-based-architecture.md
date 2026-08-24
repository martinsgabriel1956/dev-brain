---
type: concept
title: "Space-Based Architecture"
aliases: ["SBA", "arquitetura baseada em espaço"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_count: 1
tags: [arquitetura, sistemas-distribuidos, escalabilidade, tuple-space]
skill: tech-mentor-backend
status: stub
---

# Space-Based Architecture

Estilo arquitetural que resolve gargalo de escalabilidade removendo o banco de dados central do caminho crítico: unidades de processamento mantêm dados **in-memory**, replicados/particionados, e se coordenam através de um **espaço de tuplas** compartilhado ([[wiki/concepts/tuple-space|tuple space]]) em vez de consultas diretas a um banco compartilhado. Descendente direto do modelo [[wiki/concepts/linda-coordination-language|Linda]]/tuple space dos anos 1980.

Citado apenas na seção "Ver também" do verbete de origem — ainda não aprofundado na wiki; candidato a ingest futuro dedicado (ex.: GigaSpaces, Hazelcast como implementações modernas).

## Key sources

- [[wiki/sources/tuple-space-wikipedia]] — citado como conceito relacionado ("See Also"), sem aprofundamento no verbete
