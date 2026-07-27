---
type: source
title: "Contract Test (Martin Fowler)"
aliases: ["contract test bliki", "integration contract test", "teste de contrato fowler"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_file: /home/nemomartins/Documentos/new/dev-study/raw/contract-test-martin-fowler.md
source_url: "https://martinfowler.com/bliki/ContractTest.html"
author: "Martin Fowler"
date_published: 2011-01-12
date_ingested: 2026-07-27
source_count: 0
tags: [testes, contract-testing, test-doubles, martin-fowler, consumer-driven-contracts]
skill: tech-mentor-testing
status: stable
---

# Contract Test (Martin Fowler)

## TL;DR

Bliki entry curto (originalmente "Integration Contract Test", renomeado depois para "Contract Test") que introduz a técnica: manter os testes normais rodando contra um [[wiki/concepts/test-doubles|Test Double]] de um serviço externo, e separadamente manter um segundo conjunto de testes — os contract tests — que verificam periodicamente se as chamadas contra o double retornam o mesmo que retornariam contra o serviço real. Contract tests não precisam rodar em todo pipeline (o serviço externo muda no próprio ritmo); falha não deve quebrar o build automaticamente, e sim disparar reconciliação — atualizar o double ou conversar com o time fornecedor. Recomenda [[wiki/concepts/self-initializing-fake|SelfInitializingFake]] como técnica para construir esses doubles.

## Key Claims

- **Motivação**: doubles para serviços externos resolvem o problema de redes lentas/não-confiáveis, mas criam a dúvida de se o double reflete fielmente o comportamento real. → [[wiki/concepts/test-doubles]]
- **Dois conjuntos de testes em paralelo**: testes normais (rápidos, todo build) contra o double + contract tests (mais esporádicos) que comparam respostas do double com respostas do serviço real. → [[wiki/concepts/contract-testing]]
- **Cadência de execução**: contract tests não precisam rodar em todo pipeline de deploy — o serviço externo muda no seu próprio ritmo; execução diária costuma bastar.
- **Falha não quebra o build**: uma falha de contract test deve virar uma tarefa de reconciliação (atualizar double/código, ou conversar com o time do serviço), não travar o pipeline automaticamente.
- **Risco maior em serviços críticos de produção**: mudança de contrato não detectada pode quebrar produção e forçar correção de emergência + conversa urgente com o fornecedor.
- **Consumer-Driven Contracts reduz o risco**: compartilhar os contract tests com o time fornecedor, para rodarem no pipeline dele, detecta incompatibilidades antes do deploy. → [[wiki/concepts/contract-testing]]
- **Testa contra instância de teste, não produção**: testar direto contra produção do serviço externo exige coordenação explícita com o fornecedor.
- **O que é validado é o formato, não o dado**: contract test garante que o *formato* da chamada/resposta continua válido; stubs costumam ser snapshots de uma resposta real capturada numa data específica, e isso é aceitável — o que importa é o formato, não a atualidade do dado.
- **Técnica recomendada para construir o double**: [[wiki/concepts/self-initializing-fake|SelfInitializingFake]] — um Fake que sabe se autovalidar/regravar contra o serviço real. → [[wiki/concepts/self-initializing-fake]]

## Entities

[[wiki/entities/martin-fowler]]

## Concepts

[[wiki/concepts/contract-testing]] · [[wiki/concepts/test-doubles]] · [[wiki/concepts/self-initializing-fake]] · [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]] · [[wiki/concepts/piramide-de-testes]]

## Open Questions

- O artigo não detalha a implementação do `SelfInitializingFake` além de recomendá-lo — o padrão completo (como ele decide quando regravar contra o serviço real vs. usar o snapshot local) só está documentado em outro bliki entry de Fowler, ainda não ingerido nesta wiki. Candidato a próxima ingestão.
- "Integration Contract Test" (nome original do artigo) não aparece em nenhuma outra fonte desta wiki — vale ficar atento a fontes antigas que usem esse nome em vez de "Contract Test" para não tratar como conceito diferente.

## Raw Quotes

*(Fonte tratada como paráfrase/resumo em `raw/contract-test-martin-fowler.md`, não tradução literal — para o texto exato em inglês, ver `source_url`.)*
