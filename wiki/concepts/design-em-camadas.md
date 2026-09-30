---
type: concept
title: "Design em Camadas (Simples → Complexo)"
aliases: ["design incremental", "projetar em camadas", "versão simplificada primeiro"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [system-design, metodo, evolucao, gargalo]
skill: tech-mentor-system-design
status: stub
---

# Design em Camadas (Simples → Complexo)

Método: desenhar primeiro a versão mais simples que funciona e evoluí-la, bloco a bloco, conforme cada gargalo aparece — em vez de começar pela arquitetura final. Na fonte, o "Instagram simplificado" parte de um back end único com disco local e PostgreSQL e acrescenta LB, CDN, cache, rate limiter, fila e réplicas/sharding, cada um justificado por um problema ([[wiki/sources/como-estudar-system-design-building-blocks-instagram-simplificado]]).

- Cada camada deve responder: qual gargalo, qual custo, qual alternativa mais barata ([[wiki/concepts/gargalo]]).
- Na wiki, o mesmo método aparece em simuladores ([[wiki/concepts/simulador-de-system-design]]) e na "escada de leitura" cache → réplicas → sharding ([[wiki/concepts/read-replicas]], [[wiki/concepts/sharding]]).
- Complementa [[wiki/concepts/building-blocks-system-design]]; não substitui esclarecer requisitos e estimar escala ([[wiki/concepts/entrevista-system-design]]).

## Key sources

- [[wiki/sources/como-estudar-system-design-building-blocks-instagram-simplificado]] — etapa 3 do roteiro de estudo: versão simples → versão complexa com building blocks
