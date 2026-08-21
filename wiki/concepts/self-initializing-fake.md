---
type: concept
title: "SelfInitializingFake"
aliases: ["self-initializing fake", "fake auto-inicializável", "fake autoinicializável"]
date_created: 2026-07-27
date_updated: 2026-08-21
source_count: 3
tags: [testes, test-doubles, contract-testing, martin-fowler]
skill: tech-mentor-testing
status: stable
---

# SelfInitializingFake

Padrão de [[wiki/concepts/test-doubles|Test Double]] descrito em detalhe por [[wiki/entities/martin-fowler]] em [[wiki/sources/self-initializing-fake-martin-fowler]] (bliki de 2009) e recomendado por ele em [[wiki/sources/contract-test-martin-fowler]] como forma de construir o double usado num [[wiki/concepts/contract-testing|contract test]]: um Fake que, na primeira invocação, encaminha a chamada ao serviço remoto real e grava a resposta em cache; chamadas seguintes leem do cache em vez de bater no serviço de novo.

Isso combina os dois lados do problema num só objeto: o mesmo double usado nos testes normais (rápidos, offline) é também o mecanismo que periodicamente confirma sua própria fidelidade ao serviço real — reduzindo o risco central que motiva o [[wiki/concepts/contract-testing|contract test]], que é o double "mentir" sobre o comportamento do serviço externo.

## Por que "Fake" e não "Stub" ou "cache comum"

Fowler faz duas distinções de vocabulário que valem reter:

- **Fake, não Stub**: um Stub exigiria popular a fixture manualmente com os dados esperados antes do teste rodar; o self-initializing fake opera de forma autônoma — ele mesmo busca e grava seus dados na primeira execução, sem setup externo. Isso o mantém dentro da definição primária de Fake em [[wiki/sources/test-double-xunitpatterns-meszaros]] (implementação funcional simplificada do DOC).
- **Parecido com caching, mas sem invalidação**: o mecanismo lembra caching comum, mas evita deliberadamente o problema de invalidação de cache — o snapshot só é regravado quando o teste decide invalidá-lo (ex.: rodar de novo contra o serviço real), não por TTL ou heurística automática.

## Dados que mudam: quando o snapshot antigo ainda serve

Testes automatizados normalmente não precisam de dados *atuais* do serviço externo, só de dados *válidos no formato*. Um snapshot antigo continua útil enquanto o formato da resposta não mudar — o que é exatamente o que o [[wiki/concepts/contract-testing|contract test]] verifica separadamente. No relato de Josh Price citado no artigo, dados remotos supostamente estáticos ocasionalmente mudavam, e essa mudança em si sinalizava que o sistema consumidor precisava de atualização; o time dele manteve uma suíte que verificava periodicamente se o snapshot do fake ainda correspondia ao serviço real — na prática, o contract test que valida o fake.

## Pipeline em dois estágios

O mesmo relato descreve um build com estágios iniciais rodando contra os fakes (rápido, todo commit) e estágios posteriores rodando contra o serviço real (lento, cadência menor) — o mesmo desenho de cadência descrito em [[wiki/sources/contract-test-martin-fowler]] para contract tests em geral.

## Detalhe prático: parâmetros irrelevantes na chave de cache

Um desafio citado é lidar com parâmetros que variam entre chamadas sem afetar o resultado (ex.: um timestamp ou id de sessão na URL) — a solução foi removê-los da chave de lookup usada para achar a entrada em cache, evitando que o fake trate chamadas equivalentes como diferentes e perca o cache sem necessidade.

## Ver também

- [[wiki/concepts/test-doubles]] — categoria geral (Fake é um dos cinco tipos de Meszaros); na definição primária ([[wiki/sources/test-double-xunitpatterns-meszaros]]), um **Fake** é uma implementação funcional simplificada do DOC, usada por razões que **não** são controle nem observação — exatamente o caso deste padrão, cuja autoinicialização é uma camada extra sobre esse Fake
- [[wiki/concepts/contract-testing]] — o problema que o SelfInitializingFake ajuda a resolver
- [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]] — onde esse double é usado (narrow integration test)

## Key Sources

- [[wiki/sources/self-initializing-fake-martin-fowler]] — fonte primária do padrão: mecanismo de cache na primeira chamada, distinção Fake vs. Stub, caso de dados que mudam, pipeline em dois estágios, chave de cache sem parâmetros irrelevantes
- [[wiki/sources/contract-test-martin-fowler]] — recomendação do padrão como técnica para construir doubles usados em contract tests
- [[wiki/sources/test-double-xunitpatterns-meszaros]] — definição primária de Fake (implementação simplificada do DOC, nem controle nem observação)
