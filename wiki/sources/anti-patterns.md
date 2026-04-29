---
type: source
title: "Anti-patterns Arquiteturais"
aliases: ["anti-patterns", "big ball of mud", "distributed monolith", "god class", "anemic domain model"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/anti-patterns.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [anti-patterns, big-ball-of-mud, distributed-monolith, god-class, anemic-domain-model, accidental-complexity, resume-driven-development]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Os 5 anti-patterns arquiteturais mais destrutivos: Big Ball of Mud (sem estrutura, impossível evoluir), Distributed Monolith (microsserviços que se comportam como monolito acoplado), God Class (uma classe que faz tudo), Anemic Domain Model (entidades sem comportamento), Resume-Driven Development (tecnologia por prestígio, não por problema).

## Key Claims

**Claim:** Distributed Monolith é pior que um monolito — tem a complexidade de ambos.
**Evidence:** Microsserviços com banco compartilhado ou chamadas síncronas em cadeia. Deploy de um serviço exige deploy de outros. Falha em cascata. Sem a agilidade de microsserviços independentes nem a simplicidade transacional do monolito.
**Confidence:** alta

**Claim:** God Class é o code smell #1 — classe importada em 80% do código.
**Evidence:** O `UserService` com métodos de auth, billing, notificação e relatório. Impossível testar em isolamento. Qualquer mudança tem efeito colateral. Solução: dividir por responsabilidade com UseCases dedicados.
**Confidence:** alta

**Claim:** Anemic Domain Model viola o princípio OO fundamental — comportamento junto ao dado.
**Evidence:** Entidade com apenas getters/setters + services com lógica de negócio espalhada. Resultado: regras de negócio duplicadas, sem invariantes do domínio garantidas, fácil de colocar objeto em estado inválido.
**Confidence:** alta

**Claim:** Resume-Driven Development é o anti-pattern organizacional mais caro.
**Evidence:** Adotar Kubernetes para monolito de 5k usuários. Event Sourcing para CRUD simples. Microsserviços para time de 2 devs. A tecnologia deveria resolver o problema atual, não o problema hipotético futuro ou o currículo do arquiteto.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/big-ball-of-mud]]
- [[concepts/distributed-monolith]]
- [[concepts/god-class]]
- [[concepts/anemic-domain-model]]
- [[concepts/accidental-complexity]]
- [[concepts/clean-architecture]]

## Open Questions

- Como identificar que um monolito modular está virando Big Ball of Mud antes que seja tarde demais?
- Existe um critério objetivo para distinguir "complexidade essencial" de "acidental"?
