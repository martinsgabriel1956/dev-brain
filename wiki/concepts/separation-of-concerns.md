---
type: concept
title: "Separation of Concerns"
aliases: ["separation of concerns", "soc", "separacao de responsabilidades"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_count: 1
tags: [separation-of-concerns, encapsulamento, arquitetura, modularidade, backend]
skill: tech-mentor-backend
status: stub
---

# Separation of Concerns

Princípio de dividir um sistema em partes onde cada uma cuida de uma responsabilidade distinta, com interação limitada e explícita. Num [[wiki/concepts/monolito-modular]], é o que os **contratos/interfaces** entre módulos garantem: o módulo `user` define os modos de interagir com ele (input/output), e os demais módulos não alcançam seus internals — junto com [[wiki/concepts/encapsulamento]]. Relacionado a [[wiki/concepts/hexagonal-architecture]] e [[wiki/concepts/contrato-de-api]].

## Key sources

- [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]]
