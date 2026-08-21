---
type: source
title: "Self Initializing Fake (Martin Fowler)"
aliases: ["self-initializing fake bliki", "fake autoinicializável fowler"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_file: /home/nemomartins/Documentos/new/dev-study/raw/self-initializing-fake-martin-fowler.md
source_url: "https://martinfowler.com/bliki/SelfInitializingFake.html"
author: "Martin Fowler"
date_published: 2009-08-04
date_ingested: 2026-08-21
source_count: 0
tags: [testes, test-doubles, contract-testing, martin-fowler]
skill: tech-mentor-testing
status: stable
---

# Self Initializing Fake (Martin Fowler)

## TL;DR

Bliki entry curto que introduz o padrão em detalhe: um Fake que, na primeira chamada, encaminha a requisição ao serviço remoto real e grava a resposta em cache; chamadas seguintes leem do cache em vez de bater no serviço de novo. Fowler distingue isso de caching comum por evitar o problema de invalidação, e esclarece que é um **Fake** (implementação autônoma) e não um **Stub** (que exigiria fixture manual). O artigo fecha a lacuna deixada aberta em [[wiki/sources/contract-test-martin-fowler]], que recomendava o padrão sem detalhar seu mecanismo.

## Key Claims

- **Mecanismo central**: na primeira invocação o fake repassa a chamada ao serviço remoto real e armazena em cache a resposta; chamadas subsequentes leem do cache, não do serviço. → [[wiki/concepts/self-initializing-fake]]
- **Diferença de caching comum**: parece caching, mas evita a complexidade de invalidação de cache — vantagem central apontada por Fowler.
- **Por que é "Fake" e não "Stub"**: um Fake opera de forma autônoma (se autoinicializa contra o serviço real); um Stub exigiria popular a fixture manualmente com os dados esperados. → [[wiki/concepts/test-doubles]]
- **Dados remotos que mudam**: em um caso relatado, o double falava com um banco controlado por outro sistema, cujos dados mudavam com frequência; como testes automatizados normalmente não dependem de dados atuais, guardar valores antigos em cache funcionou bem.
- **Caso de Josh Price — dados "estáticos" que às vezes mudavam**: dados remotos supostamente estáticos ocasionalmente mudavam, e essa mudança sinalizava que o sistema precisava de atualização. O time dele manteve uma suíte separada que verificava periodicamente se os valores em cache do self-initializing fake ainda correspondiam ao serviço real — essa suíte é, na prática, o [[wiki/concepts/contract-testing|contract test]] que valida o fake.
- **Pipeline em dois estágios**: estágios iniciais do build rodavam contra os fakes (rápido); estágios posteriores rodavam contra o serviço real (lento) — o mesmo desenho de cadência descrito em [[wiki/sources/contract-test-martin-fowler]].
- **Parâmetros irrelevantes na chave de cache**: um desafio prático foi lidar com parâmetros que mudavam entre chamadas sem afetar o resultado — a solução foi removê-los da URL usada como chave de lookup do cache, para não invalidar o fake por uma diferença que não importa.
- **Créditos**: Josh Price, Darren Cotterill e Gerard Meszaros contribuíram com ideias para o artigo — reforça, junto com [[wiki/sources/test-double-xunitpatterns-meszaros]], o papel recorrente de Meszaros como referência de Fowler em vocabulário de test doubles. → [[wiki/entities/gerard-meszaros]]

## Entities

[[wiki/entities/martin-fowler]] · [[wiki/entities/gerard-meszaros]]

## Concepts

[[wiki/concepts/self-initializing-fake]] · [[wiki/concepts/test-doubles]] · [[wiki/concepts/contract-testing]]

## Open Questions

- Josh Price e Darren Cotterill são citados apenas como contribuidores pontuais (créditos), sem outras fontes na wiki que os caracterizem — não foram criadas entity pages para eles por não haver conteúdo além do nome; candidatos a entity stub se aparecerem em outra fonte.
- O artigo não detalha uma estrutura de dados ou implementação concreta do cache (ex.: em memória, arquivo, banco) — trata o mecanismo em nível conceitual. Fonte complementar sobre implementação real, se existir, é candidata a ingestão futura.

## Raw Quotes

*(Fonte tratada como tradução/paráfrase em `raw/self-initializing-fake-martin-fowler.md`, a partir de extração de conteúdo via ferramenta de fetch — não HTML bruto. Para o texto exato em inglês, ver `source_url`.)*
