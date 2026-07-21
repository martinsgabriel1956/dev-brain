---
type: source
title: "Application Boundary (Martin Fowler)"
aliases: ["application boundary bliki", "fronteira de aplicação", "aplicações como construções sociais"]
date_created: 2026-07-20
date_updated: 2026-07-20
source_file: /home/nemomartins/Documentos/new/dev-study/raw/application-boundary-martin-fowler.md
source_url: "https://martinfowler.com/bliki/ApplicationBoundary.html"
author: "Martin Fowler"
date_published: 2003-09-11
date_ingested: 2026-07-20
source_count: 0
tags: [arquitetura, ddd, bounded-context, soa, contexto-organizacional, martin-fowler, strategic-design]
skill: tech-mentor-backend
status: stable
---

# Application Boundary (Martin Fowler)

## TL;DR

Bliki entry curto de 2003 em que Fowler argumenta contra a previsão (comum na época, no auge do discurso de SOA) de que "aplicações" desapareceriam em favor de composição pura de serviços. Sua tese: aplicações não vão desaparecer pela mesma razão que suas fronteiras são difíceis de traçar — **aplicações são construções sociais**, não unidades tecnicamente objetivas. Um bliki entry curto, mas que antecipa em anos o argumento organizacional que hoje sustenta [[wiki/concepts/ddd|DDD estratégico]] e a lei de Conway.

## Key Claims

- **Aplicações são construções sociais, definidas por três lentes diferentes e nem sempre alinhadas**: (1) um corpo de código que devs veem como unidade única, (2) um conjunto de funcionalidade que o negócio vê como unidade única, (3) uma iniciativa que quem controla o orçamento vê como um orçamento único. → [[wiki/concepts/application-boundary]]
- **Fronteiras de aplicação podem ser traçadas de "centenas de maneiras arbitrariamente diferentes"** — não existe um critério técnico objetivo que resolva sozinho onde uma aplicação termina e outra começa.
- **A causa raiz das fronteiras não é técnica, é humana**: "essas fronteiras são traçadas primariamente por relações humanas e política, mais do que por considerações técnicas e funcionais."
- **Contra-argumento à previsão de que SOA extinguiria as aplicações**: Fowler discorda explicitamente da tese (comum entre proponentes de SOA em 2003) de que o desenvolvimento corporativo futuro seria só "montar serviços" — porque o problema que gera aplicações (agrupamento social) não desaparece ao trocar a unidade técnica de "aplicação" por "serviço".
- **Aponta para o strategic design de Domain-Driven Design** como leitura complementar para quem quer aprofundar como aplicações se inter-relacionam — conexão explícita com [[wiki/concepts/ddd]] (Bounded Context, Context Map), feita pelo próprio Fowler.

## Entities

[[wiki/entities/martin-fowler]]

## Concepts

[[wiki/concepts/application-boundary]] · [[wiki/concepts/ddd]] · [[wiki/concepts/contexto-organizacional-para-arquitetura]] · [[wiki/concepts/arquitetura-de-software]]

## Conexão com Conway's Law e Monolito Modular

Embora o texto não cite [[wiki/sources/conways-law|a lei de Conway]] diretamente (o artigo é de 2003; a formulação popular "Conway's Law" e o Inverse Conway Maneuver como a wiki os documenta vêm de fontes posteriores), a tese central — "sistemas espelham as estruturas de comunicação/política que os produzem" — é o mesmo argumento em outra formulação: aqui aplicado a por que a fronteira de uma *aplicação* é social, lá aplicado a por que a fronteira de um *serviço/módulo* é social. O debate SOA-vs-aplicações de 2003 também prefigura, em espírito, a discussão mais recente entre [[wiki/sources/microservicos-vs-monolito-modular|microsserviços e monolito modular]]: em ambos os casos, a pergunta "qual é a unidade certa?" não tem resposta puramente técnica.

## Open Questions

- O artigo não define um método prático para decidir onde traçar uma fronteira de aplicação — apenas nomeia o problema como social. A literatura de DDD estratégico (Bounded Context, Context Map) que o próprio Fowler recomenda como leitura complementar preenche essa lacuna com mais rigor; vale ingestão futura de uma fonte primária de DDD estratégico (Eric Evans ou Vaughn Vernon) para essa ponte.
- Não há, nesta wiki, uma fonte primária ingerida sobre a onda de discurso "SOA vai substituir aplicações" de 2003 contra a qual Fowler está argumentando — o contexto histórico foi inferido apenas do próprio texto.

## Raw Quotes

> "Applications are social constructions."

> "There's little science in how this works, and in many ways these boundaries are drawn primarily by human inter-relationships and politics rather than technical and functional considerations."

*(Tradução completa em `raw/application-boundary-martin-fowler.md`; para o texto exato em inglês, ver `source_url`.)*
