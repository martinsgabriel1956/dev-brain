---
type: concept
title: "Código Espaguete"
aliases: ["code espaguete", "codigo espaguete", "spaghetti code", "codigo sopa"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_count: 1
tags: [code-espaguete, acoplamento, legado, arquitetura, backend]
skill: tech-mentor-backend
status: stub
---

# Código Espaguete

Estado de degradação em que partes do código chamam funções umas das outras em cadeia, sem organização nem fronteiras claras — "uma coisa chama outra, que chama funções de outra". Tipicamente surge quando um [[wiki/concepts/monolito]] cresce de forma desorganizada e vira legado.

## Como cada arquitetura o combate

- **[[wiki/concepts/microsservicos]]** o eliminam por **impossibilidade estrutural**: um serviço não consegue chamar funções de outro; a comunicação passa a ser via rede/API. O acoplamento em cadeia deixa de ser possível — mas ao custo de latência e overhead distribuído (e ainda é possível cair num distributed monolith).
- **[[wiki/concepts/monolito-modular]]** o combate por **contratos/interfaces** entre módulos ([[wiki/concepts/hexagonal-architecture|Ports & Adapters]]), sem pagar o custo da rede.

Ver [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]].

## Key sources

- [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]]
