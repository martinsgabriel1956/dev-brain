---
type: concept
title: "Tolerância à Desatualização de Cache"
aliases: ["quanta desatualização aceitar", "staleness tolerance"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [cache, consistencia, decisao-arquitetural, ttl]
skill: tech-mentor-system-design
status: stub
---

# Tolerância à Desatualização de Cache

A pergunta de arquitetura do [[wiki/concepts/cache]]: **por quanto tempo a informação servida pode divergir da fonte de verdade?** O cache reduz tempo de acesso (ex.: 1 s → 10 ms) e custo, mas atualiza a cada intervalo (1 min, 5 min, 1 h), então pode servir dado velho.

- **Intolerante:** saldo bancário. Quem acabou de receber um Pix de R$ 10 mil e vê R$ 0 pode achar que sofreu golpe.
- **Tolerante:** post de blog. Edição de texto ou foto nova tem efeito final pouco problemático.

Define o [[wiki/concepts/ttl]] e a estratégia de invalidação. Ver [[wiki/concepts/tradeoff-de-cache]], [[wiki/concepts/cache-invalidation]] e [[wiki/concepts/stale-while-revalidate]].

## Key sources

- [[wiki/sources/introducao-arquitetura-de-software-conceitos-decisoes-kiper-academy]]
