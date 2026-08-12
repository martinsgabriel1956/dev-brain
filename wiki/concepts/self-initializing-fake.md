---
type: concept
title: "SelfInitializingFake"
aliases: ["self-initializing fake", "fake auto-inicializável"]
date_created: 2026-07-27
date_updated: 2026-08-12
source_count: 2
tags: [testes, test-doubles, contract-testing, martin-fowler]
skill: tech-mentor-testing
status: stub
---

# SelfInitializingFake

Padrão de [[wiki/concepts/test-doubles|Test Double]] recomendado por [[wiki/entities/martin-fowler]] em [[wiki/sources/contract-test-martin-fowler]] como forma de construir o double usado num [[wiki/concepts/contract-testing|contract test]]: um Fake que sabe se autovalidar — na primeira execução (ou periodicamente) ele chama o serviço real e grava a resposta como snapshot local; nas execuções seguintes, responde a partir desse snapshot, sem precisar do serviço real disponível.

Isso combina os dois lados do problema num só objeto: o mesmo double usado nos testes normais (rápidos, offline) é também o mecanismo que periodicamente confirma sua própria fidelidade ao serviço real — reduzindo o risco central que motiva o [[wiki/concepts/contract-testing|contract test]], que é o double "mentir" sobre o comportamento do serviço externo.

## Ver também

- [[wiki/concepts/test-doubles]] — categoria geral (Fake é um dos cinco tipos de Meszaros); na definição primária ([[wiki/sources/test-double-xunitpatterns-meszaros]]), um **Fake** é uma implementação funcional simplificada do DOC, usada por razões que **não** são controle nem observação — exatamente o caso deste padrão, cuja autovalidação é uma camada extra sobre esse Fake
- [[wiki/concepts/contract-testing]] — o problema que o SelfInitializingFake ajuda a resolver
- [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]] — onde esse double é usado (narrow integration test)

## Open Questions

- O bliki entry que introduz esse padrão em detalhe (implementação, quando regravar o snapshot) ainda não foi ingerido nesta wiki — só é conhecido aqui por menção em [[wiki/sources/contract-test-martin-fowler]]. Candidato a próxima ingestão.

## Key Sources

- [[wiki/sources/contract-test-martin-fowler]]
- [[wiki/sources/test-double-xunitpatterns-meszaros]] — definição primária de Fake (implementação simplificada do DOC, nem controle nem observação)
