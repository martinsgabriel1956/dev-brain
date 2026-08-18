---
type: concept
title: "CORBA e RMI"
aliases: ["CORBA", "RMI", "Common Object Request Broker Architecture", "Remote Method Invocation"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [corba, rmi, rpc, apis-remotas, historia-da-computacao, anos-90]
skill: tech-mentor-backend
status: stub
---

# CORBA e RMI

Padrões dos anos 90 que representam a primeira geração de **APIs remotas** — a primeira vez que "API" passa a significar comunicação entre processos separados por rede, e não só uma biblioteca local do sistema operacional. Surgiram no mesmo período em que a web nascia.

- **CORBA** (Common Object Request Broker Architecture) — padrão multi-linguagem/multi-plataforma para invocar objetos remotos.
- **RMI** (Remote Method Invocation) — equivalente do ecossistema Java, para invocar métodos de objetos remotos entre JVMs.

Ambos descritos na fonte como "complexos", mas foram o que abriu caminho para a integração em rede que veio depois — [[wiki/concepts/soap]] nos anos 2000 é citado, em [[wiki/sources/tecnologias-hype-passado-soap-xml-esb-jquery-cobol]], como resposta justamente à limitação de soluções "same-platform" como CORBA e RMI, que não resolviam bem interoperabilidade entre Java, C++ e .NET.

## Key Sources

- [[wiki/sources/historia-e-evolucao-das-apis-bernardo-lobato]] — CORBA e RMI como primeira geração de APIs remotas, anos 90
