---
type: concept
title: "Large Scale Architecture"
aliases: ["arquitetura de larga escala", "large scale", "alta escala"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [system-design, arquitetura, escalabilidade, sharding, alta-disponibilidade, control-plane]
skill: tech-mentor-system-design
status: stub
---

# Large Scale Architecture

Arquitetura projetada para suportar sistemas que operam com volume extenso de dados/tráfego — não é necessariamente uma [[wiki/concepts/arquitetura-complexa|arquitetura complexa]]; large scale e complexidade são eixos independentes. Uma arquitetura large scale pode ser conceitualmente simples em alto nível (poucas camadas, tecnologia homogênea) mesmo usando técnicas sofisticadas a nível de código, como [[wiki/concepts/sharding]].

## Características

- Necessidade de **alta disponibilidade** ([[wiki/concepts/alta-disponibilidade]]) — picos de tráfego, sistemas bancários, lojas virtuais.
- Princípio central: **dividir para conquistar** — dividir dados/carga em pedaços (shards, partições) para atender volume que uma única unidade não suportaria.
- Uso de diferentes storage engines por finalidade (ex: banco relacional + [[wiki/concepts/s3|S3]] para objetos + [[wiki/concepts/cdn|CDN]] + Redis/Memcached para chave-valor) — uma forma de complexidade tecnológica, mas não poliglota/interdependente como na arquitetura complexa.
- Exige um **[[wiki/concepts/control-plane]]** — camada de controladores separada do software que atende o negócio, responsável por operações como mover um usuário de um shard para outro.
- Risco característico: **[[wiki/concepts/over-engineering]]** — acumular ferramental/tecnologia além do necessário por antecipação de escala que ainda não existe.

## Distinção de Arquitetura Complexa

| | Large Scale | [[wiki/concepts/arquitetura-complexa|Complexa]] |
|---|---|---|
| Foco | Capacidade/engenharia para volume | Interdependência e heterogeneidade |
| Causa típica | Crescimento de tráfego/dados | Legado convivendo com o novo |
| Anti-pattern associado | Over-engineering | Over-thinking |
| Exemplo | Sharding, CDN, cache distribuído | Mainframe + AS/400 + Linux + Windows coexistindo |

## Key Sources

- [[wiki/sources/large-scale-vs-complex-architecture]]
