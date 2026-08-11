---
type: concept
title: "Encapsulamento"
aliases: ["encapsulamento", "encapsulation", "information hiding"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_count: 1
tags: [encapsulamento, separation-of-concerns, arquitetura, modularidade, backend]
skill: tech-mentor-backend
status: stub
---

# Encapsulamento

Esconder os detalhes internos de uma unidade e expor apenas uma interface controlada de interação. A analogia usada em [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]]: uma classe expõe **getters e setters** definindo como o mundo externo interage com ela; um módulo de [[wiki/concepts/monolito-modular]] faz o mesmo via **contratos** — os outros módulos não chamam seus internals, só o que ele expõe. Anda junto com [[wiki/concepts/separation-of-concerns]] e materializa-se em [[wiki/concepts/hexagonal-architecture]].

## Key sources

- [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]]
