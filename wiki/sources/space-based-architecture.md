---
type: source
title: "Space-Based Architecture"
aliases: ["space based architecture", "in-memory data grid", "hazelcast", "apache ignite", "processing unit", "data pump"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/space-based-architecture.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [space-based-architecture, in-memory-grid, hazelcast, processing-unit, data-pump, high-throughput, stateful-scaling]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Space-Based Architecture: elimina o banco de dados do caminho crítico das requisições. Processing Units (PUs) contêm lógica + cópia do dado em memória. Data Grid (Hazelcast/Ignite) sincroniza estado entre PUs. Data Pumps escrevem assincronamente no banco persistente. Para: sistemas com picos extremos de throughput (trading, gaming, ticketing). Contra: consistência eventual, complexidade operacional alta.

## Key Claims

**Claim:** Space-Based Architecture elimina o gargalo do banco de dados — todas as operações acontecem em memória.
**Evidence:** Arquiteturas tradicionais: cada request → query banco → resposta. Gargalo: conexões de banco, latência de disco. Space-Based: PU tem cópia do dado relevante em memória. Request processado sem banco. Escrita assíncrona via Data Pump. Throughput limitado por CPU/RAM, não por I/O de banco. Para Ticketmaster (100k req/s no lançamento), banco seria gargalo — memória não.
**Confidence:** alta

**Claim:** Consistência eventual é o trade-off central — replicação entre PUs não é instantânea.
**Evidence:** PU-1 processa pedido, atualiza estado em memória, Data Grid replica para PU-2 em ~5ms. PU-2 pode ver estado ligeiramente desatualizado nesse intervalo. Para casos onde consistência forte é necessária (transações financeiras), Space-Based não é adequado. Para contagem de estoque em flashsale (perder algumas unidades é aceitável), consistência eventual é ok.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/space-based-architecture]]
- [[entities/hazelcast]]
- [[entities/apache-ignite]]
- [[concepts/in-memory-grid]]
- [[concepts/data-pump]]
- [[concepts/eventual-consistency]]

## Open Questions

- Space-Based vs Event Sourcing para sistemas de alta throughput — quando a imutabilidade do log compensa vs estado em memória?
- Data Grid recovery após falha de nó — como garantir que o estado em memória é recuperado sem perda de dados?
