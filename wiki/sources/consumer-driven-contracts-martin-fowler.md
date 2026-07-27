---
type: source
title: "Consumer-Driven Contracts: A Service Evolution Pattern"
aliases: ["consumer-driven contracts article", "cdc pattern origin", "ian robinson contracts"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_file: /home/nemomartins/Documentos/new/dev-study/raw/consumer-driven-contracts-martin-fowler.md
source_url: "https://martinfowler.com/articles/consumerDrivenContracts.html"
author: "Ian Robinson"
date_published: 2006-06-12
date_ingested: 2026-07-27
source_count: 0
tags: [testes, contract-testing, consumer-driven-contracts, api-versioning, schema-evolution, martin-fowler, thoughtworks]
skill: tech-mentor-testing
status: stable
---

# Consumer-Driven Contracts: A Service Evolution Pattern (Ian Robinson)

## TL;DR

Artigo de Ian Robinson (Thoughtworks), publicado no site de [[wiki/entities/martin-fowler]] em 2006 — **não escrito por Fowler**, apenas hospedado no seu domínio. É a fonte primária que cunha o padrão **Consumer-Driven Contracts**: em vez do provedor de um serviço definir um contrato "completo" isoladamente, o contrato é derivado da união do que cada consumidor realmente usa. Usa um serviço fictício `ProductSearch` como exemplo recorrente. Introduz também o padrão [[wiki/concepts/must-ignore-pattern|Must Ignore]] para extensibilidade de schema e aplica o Robustness Principle (Postel's Law) à validação de payloads — "liberal no que recebe, conservador no que envia".

## Key Claims

- **O problema**: um serviço com múltiplos consumidores (ex.: `ProductSearch`, usado por marketing interno e por revendedores externos) trava a própria evolução quando validação rígida (XSD tudo-ou-nada) faz qualquer mudança de schema — mesmo em uma parte que um consumidor específico nunca usou — quebrar esse consumidor. → [[wiki/concepts/contrato-de-api]]
- **Must Ignore pattern**: schemas devem ter pontos de extensão explícitos que um consumidor pode ignorar com segurança se não reconhecer — permite compatibilidade retroativa (backward) e "para frente" (forward) sem exigir que todo consumidor seja atualizado em lockstep com o provedor. → [[wiki/concepts/must-ignore-pattern]]
- **Robustness Principle aplicado a validação**: para remover um campo não utilizado sem quebrar consumidores, Robinson recomenda validar "na medida certa" — cada consumidor valida apenas os campos que efetivamente usa, não o payload inteiro. Cita o Schematron como alternativa ao XSD, permitindo asserções pontuais em vez de validação tudo-ou-nada.
- **O padrão Consumer-Driven Contracts propriamente dito** — modelo de três camadas:
  - **Provider Contract**: tudo que o serviço expõe (schemas, interfaces, conversas/protocolos, políticas, QoS).
  - **Consumer Contract**: o subconjunto do provider contract que um consumidor específico usa e espera.
  - **Consumer-Driven Contract**: o contrato do provedor *derivado* da união de todos os consumer contracts conhecidos — construído de baixo para cima, em vez de definido unilateralmente. → [[wiki/concepts/contract-testing]]
- **Inversão de quem define o contrato**: em vez do provedor desenhar um contrato "completo" e esperar adaptação dos consumidores, ele enxerga explicitamente quais elementos do contrato sustentam valor de negócio real (porque algum consumidor os usa) e quais são seguros para remover.
- **Implementação é agnóstica**: consumer contracts podem existir como planilhas, testes automatizados, ou asserções em runtime (Schematron, WS-Policy). A comunicação entre provedor e consumidores acontece fora de banda — conversa direta ou infraestrutura de coordenação, não é automática pelo protocolo.
- **Benefício central**: dá ao provedor feedback granular — antes de uma mudança, dá para saber exatamente qual consumidor será afetado e decidir deliberadamente sobre compatibilidade retroativa.
- **Limitação de escopo**: o padrão funciona melhor dentro de uma única empresa ou comunidade fechada de serviços, onde o provedor tem influência real sobre os consumidores. Não elimina o acoplamento entre provedor e consumidor — só torna esse acoplamento "escondido" visível e negociável. Há risco de comprometer a integridade do serviço se consumidores exigirem algo fora do escopo de negócio do provedor.
- **Distinção explícita de WS-Agreement/WSLA**: esses são acordos de nível de serviço (SLA), não expressões de expectativas funcionais de um consumidor específico — não devem ser confundidos com consumer contracts.

## Entities

[[wiki/entities/martin-fowler]] (site host, não autor) · [[wiki/entities/ian-robinson]] (autor) · [[wiki/entities/thoughtworks]]

## Concepts

[[wiki/concepts/contract-testing]] · [[wiki/concepts/must-ignore-pattern]] · [[wiki/concepts/contrato-de-api]]

## Open Questions

- O artigo cita o **Schematron** como mecanismo de validação pontual, mas esta wiki não tem uma fonte primária sobre a ferramenta — se aparecer de novo em outra fonte, vale considerar um stub próprio.
- Existe uma inconsistência estrutural pré-existente na wiki: `wiki/sources/tolerant-reader.md` é o único lugar que cobre o Robustness Principle/Postel's Law (via [[wiki/entities/martin-fowler|Tolerant Reader]] de Fowler), mas está tipado como `source`, não tem uma página de `concept` correspondente, e vários dos links que ele usa (`[[concepts/robustness-principle]]`, `[[concepts/expand-contract]]`, `[[concepts/backward-compatibility]]`, `[[concepts/event-versioning]]`) apontam para páginas que não existem. Este artigo de Robinson reforça o mesmo princípio de outro ângulo (validação "na medida certa" em vez de leitura tolerante genérica) — candidato a sinalizar no próximo `lint the wiki`.
- O artigo distingue Consumer-Driven Contracts (Robinson, 2006) do uso mais recente e ferramentizado do termo em torno do Pact/`can-i-deploy`, já coberto em [[wiki/concepts/contract-testing]] — vale confirmar se alguma fonte futura documenta explicitamente essa linha do tempo (2006 → Pact).

## Raw Quotes

*(Fonte tratada como paráfrase/resumo em `raw/consumer-driven-contracts-martin-fowler.md`, não tradução literal — para o texto exato em inglês, ver `source_url`.)*
