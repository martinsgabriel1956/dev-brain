---
type: concept
title: "Eventual Consistency"
aliases: []
date_created: 2026-09-22
date_updated: 2026-09-30
source_count: 9
tags: [eventual-consistency]
skill: tech-mentor-system-design
status: stub
---

# Eventual Consistency

Stub criado durante sweep de lint (links quebrados) a partir de referências em 6 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/sources/cap-pacelc-consistencia]]: [[eventual-consistency]]
- Em [[wiki/sources/cap-theorem]]: [[eventual-consistency]]
- Em [[wiki/sources/cqrs]]: [[eventual-consistency]]
- Em [[wiki/sources/gossip-protocol]]: [[eventual-consistency]]
- Em [[wiki/sources/quorum]]: [[eventual-consistency]]

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

## Consistência Eventual como Custo da Comunicação Assíncrona

Terceiro desafio da [[wiki/concepts/comunicacao-assincrona]] segundo [[wiki/entities/bernardo-lobato]]: um pedido e um pagamento em serviços distintos podem divergir enquanto a mudança de status se propaga, e uma consulta pode devolver dado desatualizado. Ponto prático: é preciso alinhar com liderança/cliente que o sistema não será consistente o tempo inteiro.

## Key sources

- [[wiki/sources/cap-pacelc-consistencia]]
- [[wiki/sources/cap-theorem]]
- [[wiki/sources/cqrs]]
- [[wiki/sources/gossip-protocol]]
- [[wiki/sources/quorum]]
- [[wiki/sources/vector-clocks]]
- [[wiki/sources/github-2018-cap-pacelc-particao-video]] — leitura local no nó isolado devolve dado pré-partição; divergência de escritas no GitHub 2018
- [[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]] — exemplo pedido/pagamento: dado desatualizado entre serviços; "vender" o modelo à liderança
- [[wiki/sources/cqrs-desbalanco-leitura-escrita-banco-de-leitura-eventos]] — delay entre banco de escrita e banco de leitura como custo da atualização assíncrona do read model via eventos
