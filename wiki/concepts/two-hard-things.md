---
type: concept
title: "Two Hard Things"
aliases: ["only two hard things in computer science", "phil karlton quote", "cache invalidation and naming things"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_count: 1
tags: [naming, cache, folclore-de-programacao, martin-fowler]
skill: tech-mentor-leadership
status: draft
---

# Two Hard Things

Aforismo de folclore de engenharia, atribuído a **Phil Karlton**: "só existem dois problemas difíceis em Ciência da Computação: [[wiki/concepts/tradeoff-de-cache|invalidação de cache]] e [[wiki/concepts/naming|nomear coisas]]". Curado e mantido como página viva por [[wiki/entities/martin-fowler]] desde 2009, que documenta tanto a origem incerta da frase quanto uma coleção de variações (*riffs*) que a comunidade produziu sobre ela ao longo de mais de uma década. Fonte primária: [[wiki/sources/two-hard-things-martin-fowler]].

Esta página é o lugar dedicado ao **aforismo em si** — sua origem, atribuição e as variações que geram — separado das páginas que tratam de cada problema técnico individualmente ([[wiki/concepts/naming]] e [[wiki/concepts/tradeoff-de-cache]]).

## Atribuição incerta

Mesmo Fowler, que curou a página, nunca encontrou "uma URL satisfatória" confirmando que Karlton disse a frase — é uma atribuição de boa-fé, não uma citação verificada com fonte primária. [[wiki/entities/phil-karlton]] é conhecido quase exclusivamente por essa atribuição. A pista histórica mais concreta vem de Tim Bray, que registrou a frase em seu blog e disse tê-la ouvido pela primeira vez por volta de 1996-97 — sugerindo origem oral na cultura de engenharia, sem registro escrito localizável até então.

## Riffs documentados

| Autor | Riff | O que faz |
|---|---|---|
| Leon Bambrick | adiciona "off-by-1 errors" como terceiro item, mas continua chamando de "2 problemas" | a piada é a própria contagem errada |
| Mathias Verraes | substitui os dois problemas por "guaranteed order of messages" e "exactly-once delivery" (sistemas distribuídos) | aplica a piada da numeração trocada/duplicada ao domínio onde ordem e duplicação são problemas reais — ver [[wiki/concepts/idempotencia]] |
| Phillip Scott Bowden | diz que programadores só têm uma piada e ela não é engraçada | meta-piada sobre o próprio gênero de riff |
| Nat Pryce | vê na quantidade de variações uma evidência de que programar não é fácil | inverte o registro humorístico em observação séria |

## Por que isso importa além da piada

Cada riff aponta para um problema real da área que ele imita:

- **Naming** ([[wiki/concepts/naming]]) — nomear bem exige entender completamente o que o código faz; nome ruim é dívida cognitiva permanente.
- **Cache invalidation** ([[wiki/concepts/tradeoff-de-cache]]) — saber quando invalidar é mais difícil que implementar o cache.
- **Ordem garantida e entrega exactly-once** ([[wiki/concepts/idempotencia]], via riff de Verraes) — os dois problemas centrais que tornam sistemas distribuídos difíceis de raciocinar, e que motivam idempotência como pré-requisito de retry seguro.

## Ver também

- [[wiki/concepts/naming]] — um dos dois problemas originais
- [[wiki/concepts/tradeoff-de-cache]] — o outro problema original
- [[wiki/concepts/idempotencia]] — os dois problemas do riff de sistemas distribuídos
- [[wiki/entities/martin-fowler]] — curador da página desde 2009
- [[wiki/entities/phil-karlton]] — atribuição original, não verificada

## Key Sources

- [[wiki/sources/two-hard-things-martin-fowler]] — fonte primária: citação original, atribuição incerta, nota histórica de Tim Bray, quatro riffs
