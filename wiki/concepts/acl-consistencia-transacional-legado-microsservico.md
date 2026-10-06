---
type: concept
title: "ACL: consistência transacional entre legado e microsserviços"
aliases: ["transação na camada anticorrupção", "propagação de transação acl"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [anti-corruption-layer, transacoes, consistencia, saga, legado, microsservicos]
skill: tech-mentor-backend
status: stub
---

# ACL: consistência transacional entre legado e microsserviços

Quando o legado usa **consistência forte** (várias tabelas, commit único) e parte do dado já vive em microsserviços, a [[wiki/concepts/anti-corruption-layer]] fica no meio de uma transação longa. Segundo [[wiki/sources/anti-corruption-layer-microsservicos-requisitos-arquiteturais]]:

- Transação aberta por mais tempo → risco de **timeout** no banco; é preciso tratar o estouro e **desfazer também nos microsserviços**.
- Ideal: uma transação do lado dos microsserviços e **encadeamento** de transações. Nem toda tecnologia **propaga contexto transacional** entre camadas físicas.
- SOAP + SQL Server permitem propagar a transação (afirmação do áudio, `[external, não verificado]`), mas com **latência**: duas conexões presas à mesma transação; commit no legado primeiro e, após o "commit geral", o outro lado efetiva; falha → rollback de tudo.
- Microsserviço chamando microsserviço dentro do mesmo contexto transacional agrava.
- Alternativa: do lado novo usar consistência mais fraca ([[wiki/concepts/saga-pattern|Saga]]), mas casar transação forte com Saga "dá voltas"; não há resposta fácil.
- Com muita dessa dor, trazer a ACL **para dentro do legado** (onde o objeto de transação propaga), ao custo de alterar o legado a cada evolução.

Conceito geral em [[wiki/concepts/distributed-transactions]]. Ver [[wiki/concepts/two-phase-commit]] para o protocolo clássico (relação inferida; a fonte não o cita).

## Key sources

- [[wiki/sources/anti-corruption-layer-microsservicos-requisitos-arquiteturais]]
