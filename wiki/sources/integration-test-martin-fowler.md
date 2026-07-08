---
type: source
title: "Integration Test"
aliases: ["integration test fowler", "narrow vs broad integration test", "teste de integração fowler"]
date_created: 2026-07-07
date_updated: 2026-07-07
source_count: 0
tags: [testes, integracao, terminologia, contract-testing, test-doubles, martin-fowler]
skill: tech-mentor-testing
source_file: /home/nemomartins/Documentos/new/dev-study/raw/integration-test-martin-fowler.md
source_url: "https://martinfowler.com/bliki/IntegrationTest.html"
author: "Martin Fowler"
date_published: 2018-01-16
date_ingested: 2026-07-07
status: stable
---

# Integration Test (Martin Fowler)

## TL;DR

"Teste de integração" carrega dois significados incompatíveis. O sentido **amplo**, herdado do waterfall dos anos 80, exige ativar todos os serviços reais juntos. O sentido **estreito**, viável hoje graças a dublês de teste fiéis, testa só a fatia de código que fala com um serviço externo, contra um double — e roda quase tão rápido quanto um unitário. Combinando teste estreito com [[wiki/concepts/contract-testing]], dá para confiar numa integração sem nunca rodar contra o serviço real, o que acelera o pipeline. Uma terceira confusão se soma: parte da comunidade reserva "unit test" só para o unit test [[wiki/concepts/unit-test-solitario-vs-sociavel|solitário]] e chama de "integration test" o que é, na verdade, um unit test sociável. Fowler resolve isso na própria escrita: teste amplo vira "system test"/"end-to-end test"; teste estreito continua "integration test" mas sempre qualificado como "narrow"; "unit test" segue servindo para os dois, distinguido por "solitary"/"sociable" quando necessário.

## Key Claims

- **Origem histórica da ambiguidade**: no waterfall dos anos 80, "teste de integração" nasceu como a fase de QA que ativava vários módulos construídos isoladamente, o que misturava sem perceber duas preocupações — "os módulos conversam certo?" e "o sistema composto se comporta certo?". → [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]]
- **Teste de integração estreito**: exercita só o código que fala com um serviço externo, contra um double local ou over-the-wire (ex. mountebank); escopo e velocidade próximos de um unitário. → [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]]
- **Teste de integração amplo**: exige instâncias reais de todos os serviços, ambiente e rede substanciais; exercita caminhos de código de todos os serviços, não só a integração em si. → [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]]
- **O ponto fraco do teste estreito é resolvido por contract testing**: a fidelidade do double não é garantida pelo próprio narrow test — precisa de um contract test separado validando que o double reflete o provider real. → [[wiki/concepts/contract-testing]]
- **Combo narrow + contract testing substitui o teste amplo**: permite confiar numa integração externa sem nunca rodar contra o serviço real, acelerando o pipeline; um smoke test E2E residual ainda pode fazer sentido sem QA in Production madura. → [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]], [[wiki/concepts/ci-cd]]
- **Terceira camada de confusão — unit test sociável rotulado de integration test**: quem define unit test como só o solitário (tudo mockado) às vezes chama de "integration test" o que é um unit test sociável (colaboração real entre objetos internos). → [[wiki/concepts/unit-test-solitario-vs-sociavel]]
- **Solução terminológica pessoal de Fowler**: teste amplo → "system test"/"end-to-end test"; teste estreito → "narrow integration test"; unit test → mantido, qualificado com "solitary"/"sociable" quando necessário. → [[wiki/entities/martin-fowler]]

## Entities

[[wiki/entities/martin-fowler]]

## Concepts

[[wiki/concepts/teste-de-integracao-estreito-vs-amplo]] · [[wiki/concepts/unit-test-solitario-vs-sociavel]] · [[wiki/concepts/contract-testing]] · [[wiki/concepts/test-doubles]] · [[wiki/concepts/piramide-de-testes]] · [[wiki/concepts/testes-integracao-banco-real]] · [[wiki/concepts/tdd]] · [[wiki/concepts/ci-cd]]

## Open Questions

- [[wiki/concepts/testes-integracao-banco-real]] defende nunca mockar o banco de dados em testes de integração — isso não contradiz Fowler porque banco próprio não é o tipo de "serviço externo" que ele tem em mente, mas a wiki não tinha essa distinção explícita antes desta fonte; vale revisitar se surgir um caso de banco *compartilhado entre times/serviços*, que se aproximaria mais do cenário que Fowler descreve.
- O `references/` da skill `tech-mentor-testing` (test-patterns.md, test-strategy.md) não continha a distinção narrow/broad nem solitary/sociable antes desta ingestão — pode valer avisar o mantenedor da skill para incorporar esses termos, já que são vocabulário padrão da indústria.

## Raw Quotes

*(Fonte tratada como paráfrase/resumo em `raw/`, não tradução literal — ver `raw/integration-test-martin-fowler.md` para a versão comentada. Para o texto exato, ver `source_url`.)*
