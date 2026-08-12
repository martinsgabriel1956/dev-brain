---
type: concept
title: "Teste de Integração: Estreito vs. Amplo"
aliases: ["narrow integration test", "broad integration test", "teste de integração narrow", "teste de integração broad", "system test", "end-to-end test (Fowler)"]
date_created: 2026-07-07
date_updated: 2026-08-12
source_count: 4
tags: [testes, integracao, martin-fowler, contract-testing, microservices, terminologia]
skill: tech-mentor-testing
status: stable
---

# Teste de Integração: Estreito vs. Amplo

"Teste de integração" é um termo sobrecarregado — Martin Fowler identifica que a comunidade usa a expressão para duas práticas bem diferentes, o que gera confusão sempre que dois times comparam suas suítes de teste.

## As duas definições

| | Estreito (narrow) | Amplo (broad) |
|---|---|---|
| Escopo | só a fatia de código que fala com um serviço externo | todos os serviços reais, ativados juntos |
| Dependência | [[test-doubles]] do serviço externo (in-process ou over-the-wire, ex. mountebank) | instâncias reais de cada serviço |
| Velocidade | próxima de um teste unitário — roda no mesmo framework | lenta — precisa de ambiente e rede |
| Onde roda no pipeline | estágio inicial do [[ci-cd]] | staging, geralmente como gate de deploy, não de PR |
| Risco não coberto | double não fiel ao serviço real | — |
| Mitigação do risco | [[contract-testing]] valida que o double é fiel | n/a — testa o real |

## Origem histórica

A definição "ampla" vem do waterfall dos anos 80: módulos eram construídos isoladamente por meses e só se juntavam numa fase de QA que ativava tudo junto para validar a composição. Não havia alternativa prática — testar carrinho + catálogo exigia rodar os dois.

A definição "estreita" só se tornou viável quando a prática de dublês de teste fiéis amadureceu: hoje dá para testar a integração do carrinho com o catálogo exercitando apenas o código do carrinho que fala com o catálogo, contra um double do catálogo. A fonte primária de [[test-doubles]] ([[wiki/sources/test-double-xunitpatterns-meszaros]]) formaliza por que isso funciona: substitui-se o **DOC** (o catálogo) por um double que só precisa expor a **mesma API** que o SUT (o carrinho) exercita — "fiel o suficiente", não idêntico.

## O combo que substitui o teste amplo

Narrow integration test + [[contract-testing]] cobrem, juntos, o que o teste amplo cobria:
- o narrow test garante que o *seu* código chama a dependência corretamente;
- o contract test garante que o double usado é fiel ao comportamento real do provider.

Com essa combinação, é possível confiar numa integração externa sem nunca rodar contra uma instância real do serviço — o que acelera o build. Ainda pode fazer sentido manter um teste amplo residual como *smoke test* final, especialmente sem uma cultura madura de observabilidade em produção.

## Terminologia recomendada por Fowler

Para evitar a ambiguidade, Fowler prefere renomear em vez de qualificar todo mundo:
- teste de integração **amplo** → chamar de **"system test"** ou **"end-to-end test"**;
- teste de integração **estreito** → manter "integration test", mas sempre com o qualificador **"narrow"**.

## Ver também

- [[test-doubles]] — a ferramenta que viabiliza o teste estreito
- [[contract-testing]] — mitiga o risco de um double não fiel
- [[piramide-de-testes]] — onde estreito e amplo se encaixam nas camadas
- [[testes-integracao-banco-real]] — caso particular: banco de dados costuma ser tratado como infraestrutura própria, não como "serviço externo" no sentido de Fowler
- [[unit-test-solitario-vs-sociavel]] — confusão irmã: parte da comunidade chama de "integration test" o que é um unit test sociável
- [[wiki/entities/martin-fowler]]

## Key Sources

- [[wiki/sources/integration-test-martin-fowler]]
- [[wiki/sources/test-double-xunitpatterns-meszaros]] — fonte primária do double (DOC / "mesma API, fiel o suficiente") que viabiliza o teste estreito
- [[wiki/sources/contract-test-martin-fowler]] — mecânica do contract test que mitiga o double não-fiel
- [[wiki/sources/teste-unitario-integracao-e2e-opiniao]] — caso prático de "amplo" ambíguo em sistema com PSP e fornecedor externos
- [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] — testes de integração como o tipo de melhor custo-benefício segundo o consenso de CTOs relatado, usável como critério de aceitação por task para conter code rot
