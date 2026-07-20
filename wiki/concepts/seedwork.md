---
type: concept
title: "Seedwork"
aliases: ["seed work", "framework mínimo reconstruído por time"]
date_created: 2026-07-19
date_updated: 2026-07-19
source_count: 1
tags: [testes, reuso, frameworks, kent-beck, xunit]
skill: tech-mentor-testing
status: stub
---

# Seedwork

Termo cunhado por [[wiki/entities/martin-fowler]] (a partir de uma discussão originada num post de Michael Feathers) para descrever uma alternativa a frameworks reutilizáveis tradicionais: em vez de estender um framework compartilhado de forma controlada, cada time parte de uma funcionalidade mínima ("seed") e a modifica livremente conforme sua necessidade. A consequência é que não há como receber atualizações comuns depois — uma vez que o time "faz crescer" o seedwork, ele é dono daquilo, para o bem e para o mal.

## Por que existe

Reuso de frameworks completos é difícil de acertar — frameworks bem "amadurecidos" funcionam bem, mas chegar lá é raro, e frameworks mal ajustados adicionam complexidade que atrapalha mais do que ajuda. Seedwork não é o ideal (é essencialmente reuso via copiar-e-colar, que Fowler reconhece ser normalmente criticável), mas é mais fácil de criar e usar do que um framework robusto — o critério não é se é elegante, é se é útil.

## Exemplo concreto na wiki: o framework de testes de Kent Beck

[[wiki/entities/kent-beck]] construía frameworks de teste em Smalltalk para si e seus clientes, e preferia que cada time reconstruísse o próprio (levava poucas horas) em vez de compartilhar um único framework — isso é, na prática, um Seedwork, segundo o próprio Fowler. Esse padrão foi o antecessor direto do [[wiki/entities/junit]], que rompeu esse modelo ao se tornar o primeiro framework de testes amplamente compartilhado e reutilizado fora do Smalltalk. Ver [[wiki/sources/xunit-martin-fowler]].

## Nota

Não ingerido como fonte primária própria — página consultada diretamente em [external] `https://martinfowler.com/bliki/Seedwork.html` para calibrar este stub, no contexto da ingestão de [[wiki/sources/xunit-martin-fowler]].

## Ver também

- [[wiki/entities/kent-beck]]
- [[wiki/entities/junit]]
- [[wiki/entities/c3-project]]

## Key Sources

- [[wiki/sources/xunit-martin-fowler]]
