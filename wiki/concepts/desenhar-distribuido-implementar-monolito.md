---
type: concept
title: "Desenhar Distribuído, Implementar Monolito"
aliases: ["monolito preparado para distribuir", "design distribuído com implementação monolítica"]
date_created: 2026-10-02
date_updated: 2026-10-02
source_count: 1
tags: [arquitetura, monolito, monolito-modular, evolucao-arquitetural, tomada-de-decisao]
skill: tech-mentor-system-design
status: stub
---

# Desenhar Distribuído, Implementar Monolito

Duas posturas sobre quando pensar em distribuição, segundo [[wiki/sources/arquitetura-distribuida-introducao-historico-desafios-bernardo-lobato]]: (a) **desenhar** já como componentes independentes, mesmo implementando como monolito, para definir escopo e comportamento de cada módulo; (b) pensar monolito, atento aos seus problemas, mantendo a arquitetura **preparada** para ser distribuída depois com o menor impacto. Críticos da (a) chamam de [[wiki/concepts/over-engineering]]. O autor não escolhe: o importante é permitir a mudança com mínimo efeito colateral, sem anos de migração e retrabalho. Na prática converge com [[wiki/concepts/monolito-modular]] e [[wiki/concepts/monolith-first]]. Lacuna: o vídeo não define 'preparada' (fronteiras de módulo, dados por módulo, contratos explícitos — inferência).

## Key sources

- [[wiki/sources/arquitetura-distribuida-introducao-historico-desafios-bernardo-lobato]] — introdução da série de arquiteturas distribuídas de [[wiki/entities/bernardo-lobato]]
