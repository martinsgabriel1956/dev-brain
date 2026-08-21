---
type: source
title: "Two Hard Things (Martin Fowler)"
aliases: ["two hard things bliki", "phil karlton quote", "cache invalidation and naming things"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_file: /home/nemomartins/Documentos/new/dev-study/raw/two-hard-things-martin-fowler.md
source_url: "https://martinfowler.com/bliki/TwoHardThings.html"
author: "Martin Fowler"
date_published: 2009-07-14
date_ingested: 2026-08-21
source_count: 0
tags: [naming, cache, folclore-de-programacao, martin-fowler, api-design]
skill: tech-mentor-leadership
status: stable
---

# Two Hard Things (Martin Fowler)

## TL;DR

Bliki entry curtíssimo, mantido por Fowler como uma página viva de curadoria: registra a citação clássica atribuída a Phil Karlton — "só existem dois problemas difíceis em Ciência da Computação: invalidação de cache e nomear coisas" — junto com quatro variações (*riffs*) que foram adicionadas ao longo de mais de uma década, e uma nota histórica de que a frase circulava já em 1996-97. É a fonte mais próxima de "primária" que existe na internet para uma citação citada nesta wiki em pelo menos quatro outras páginas ([[wiki/concepts/naming]], [[wiki/concepts/tradeoff-de-cache]], [[wiki/sources/cache-stampede-invalidation]], [[wiki/sources/5-principios-programador]]) sem nenhuma delas linkar a uma origem.

## Key Claims

- **A citação original, com atribuição incerta**: Fowler mesmo admite nunca ter encontrado "uma URL satisfatória" para confirmar que Phil Karlton disse a frase — ele registra a atribuição de boa-fé, não como fato verificado. → [[wiki/entities/phil-karlton]]
- **Nota histórica de Tim Bray**: o primeiro registro da frase encontrado na internet foi no blog de Tim Bray; Bray afirmou ter ouvido a frase por volta de 1996-97, o que sugere uma origem oral na cultura de engenharia bem anterior a qualquer registro escrito localizável.
- **A página é viva, não um post fechado**: Fowler documenta as revisões (2009, 2010, 2015, 2017×2, 2021) — cada uma adicionando uma variação nova conforme apareciam, um padrão de manutenção de bliki (acréscimo incremental) diferente de um artigo datado e imutável.
- **Riff de Leon Bambrick (off-by-one)**: brinca que existem "2 problemas difíceis: cache invalidation, naming things, and off-by-1 errors" — o próprio ato de listar 3 itens como "2" é a piada.
- **Riff de Mathias Verraes (sistemas distribuídos)**: substitui os dois problemas originais por dois problemas de sistemas distribuídos (ordem garantida de mensagens, entrega exactly-once) — e o riff repete a piada da numeração trocada/duplicada do original, aplicando-a ironicamente ao próprio domínio de sistemas distribuídos onde ordem e duplicação são exatamente os problemas reais. → [[wiki/concepts/idempotencia]]
- **Riff de Phillip Scott Bowden (meta-piada)**: acha que os programadores só têm uma piada, e ela não é nem engraçada — comentário sobre o próprio gênero de riffs que a página coleciona.
- **Riff de Nat Pryce**: a quantidade de variações da piada é evidência, para ele, de que programar não é realmente fácil — inverte o registro humorístico para uma observação séria sobre a profissão.

## Entities

[[wiki/entities/martin-fowler]] · [[wiki/entities/phil-karlton]]

## Concepts

[[wiki/concepts/two-hard-things]] · [[wiki/concepts/naming]] · [[wiki/concepts/tradeoff-de-cache]] · [[wiki/concepts/idempotencia]]

## Open Questions

- **Autores dos riffs não ganharam entity page**: Leon Bambrick, Mathias Verraes, Phillip Scott Bowden e Nat Pryce são citados só pelo tweet reproduzido, sem outro conteúdo na wiki que os caracterize — tratados como citação, não como entidade. Diferente de Phil Karlton, que é o sujeito central do próprio artigo e por isso ganhou stub.
- **Fonte primária do próprio Karlton nunca localizada** — nem por Fowler, nem por Tim Bray. Se uma fonte escrita anterior a 1996-97 aparecer, é candidata a atualizar tanto esta página quanto [[wiki/entities/phil-karlton]].

## Raw Quotes

*(Fonte buscada via `curl` direto no HTML — não resumo de WebFetch — para preservar o texto exato das citações/piadas em inglês; narração de Fowler em torno delas traduzida em `raw/two-hard-things-martin-fowler.md`.)*

> "There are only two hard things in Computer Science: cache invalidation and naming things." — Phil Karlton
