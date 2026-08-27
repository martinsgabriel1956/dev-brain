---
type: source
title: "CQRS — Volume, Modelo e as Formas de Manter Consistência"
aliases: ["cqrs volume e modelo", "cqrs consistencia forte vs eventual"]
date_created: 2026-08-27
date_updated: 2026-08-27
source_count: 0
tags: [tech-mentor-backend, cqrs, arquitetura, system-design, api-gateway, api-composition, read-replicas, event-driven-architecture, dual-write-problem, materialized-view]
skill: tech-mentor-backend
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/cqrs-volume-modelo-consistencia-forte-eventual.md
source_url:
author: desconhecido (canal de vídeo, série de System Design)
date_published:
date_ingested: 2026-08-27
---

# CQRS — Volume, Modelo e as Formas de Manter Consistência

## TL;DR

Transcrição de vídeo de uma série de System Design sobre CQRS. Difere das fontes já ingeridas por enquadrar a decisão de adotar CQRS em **dois motivadores explícitos e independentes** — divergência de **volume** (proporção leitura/escrita) e divergência de **modelo/assinatura** (formato de payload) — e por catalogar, de forma organizada, **seis técnicas concretas de sincronização** entre write e read model, divididas em duas categorias: consistência forte (mesma base com views/materialized views, transação cruzando os dois serviços, API Composition) e consistência eventual (read replicas, eventos com o "bug da escrita dupla", polling). Argumento central: nenhuma técnica de consistência forte resolve os dois problemas (volume e modelo) ao mesmo tempo — só a consistência eventual entrega o "trunfo" completo do CQRS.

## Key Claims

1. **Dois motivadores independentes para CQRS**: volume (proporção leitura/escrita muito diferente — ex.: logs e IoT são write-heavy, e-commerce é read-heavy) e modelo/assinatura (payloads muito diferentes entre escrita e leitura, ex. escrita via evento + leitura via HTTP, ou escrita via HTTP + leitura via GraphQL). Se só o modelo diverge e o volume é parecido, o autor considera CQRS "demais" para o problema.
2. **CQRS não exige código-fonte diferente** — a forma mais simples é o **mesmo código-fonte** deployado em dois conjuntos de réplicas com escalabilidade independente (ex.: 30 réplicas de escrita vs. 3 de leitura), com o [[wiki/concepts/api-gateway]] roteando por método HTTP. Só na prática, quando o serviço "ganha corpo", é que costuma virar código-fonte de fato separado.
3. **Fonte da verdade é sempre onde se escreve** — o serviço de escrita é responsável por validação e garantir que o estado persistido é verdadeiro; a leitura nunca é fonte da verdade.
4. **Três formas de consistência forte, cada uma resolvendo só um dos dois problemas**: (a) mesma base de dados com [[wiki/concepts/materialized-view|views/materialized views]] — resolve modelo, não volume, porque o gargalo de banco compartilhado permanece; (b) escrita em transação cruzando write e query service — quebra a separação de responsabilidade (o query service vira também um serviço de escrita) e não resolve volume, mas mantém um modelo de leitura dedicado; (c) [[wiki/concepts/api-composition|API Composition]] — o query service perde base própria e passa a ter só cache, compondo a resposta via fan-out para os serviços downstream que têm a informação.
5. **Três formas de consistência eventual**, onde o autor situa a maioria das implementações reais de CQRS: (a) [[wiki/concepts/read-replicas|read replicas]] de banco (cluster com main node de escrita + réplicas de leitura, ex. Aurora ou cluster Postgres manual); (b) eventos via broker ([[wiki/concepts/event-driven-architecture|EDA]] — Kafka, RabbitMQ, SNS/SQS), com o **bug da escrita dupla** (dual write problem) como risco explícito quando escrita na base e publicação do evento não são atômicas; (c) **polling/job periódico**, em que o query service busca mudanças acumuladas (ex. logs em S3, tabela temporária exposta via API) em vez de reagir em tempo real.
6. **Réplicas de banco preservam o schema; eventos permitem transformação livre** — a diferença central entre a opção (a) e (b) de consistência eventual: com réplicas, o read model tem exatamente a mesma estrutura da base de escrita; com eventos, o query service pode salvar no formato final que quiser (ex.: escrita relacional → leitura em Elasticsearch/Solr, otimizada para busca textual/facetada que o Postgres não faz bem).
7. **Dois contras centrais do CQRS**: duplicação de código e infraestrutura, e o desafio permanente de manter consistência entre os dois lados — se não for bem gerenciado, a leitura fica "stale" (desatualizada) em relação à escrita.
8. **Responsabilidade de roteamento deve ficar no API Gateway, não no frontend** — o autor recomenda explicitamente não empurrar para o cliente a decisão de qual host/serviço chamar; isso é responsabilidade de borda.
9. **Pergunta de fechamento**: "vale a pena?" — o autor reforça que CQRS é trade-off, não default, e que a decisão deve ser proporcional ao tamanho real da divergência de volume/modelo, não adotada por padrão em qualquer sistema com leitura e escrita.

## Entidades Mencionadas

Nenhuma entidade nomeada (empresa, produto, framework específico) além de tecnologias genéricas citadas como exemplo (Aurora, Postgres, Kafka, RabbitMQ, SNS/SQS, Elasticsearch/Lucene/Solr, GraphQL).

## Conceitos Tocados

- [[wiki/concepts/cqrs]]
- [[wiki/concepts/api-gateway]]
- [[wiki/concepts/api-composition]]
- [[wiki/concepts/read-replicas]]
- [[wiki/concepts/event-driven-architecture]]
- [[wiki/concepts/materialized-view]]
- [[wiki/concepts/outbox-pattern]]
- [[wiki/concepts/dual-write-problem]]

## Open Questions

- Fonte não cita autor nem canal — mesmo padrão de anonimato já observado em outras fontes da série de System Design já ingeridas (ex. [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]]). Sem como verificar se é o mesmo autor/canal de outras transcrições de System Design já na wiki.
- O "bug da escrita dupla" é citado apenas nominalmente, remetendo a "um vídeo no canal" — a fonte não detalha a solução (transactional outbox), que já está registrada com profundidade em [[wiki/concepts/outbox-pattern]] e na skill `tech-mentor-backend` (`references/architecture-eda-patterns.md`). Tratado aqui como ponte, não como fonte primária do tema.
- Nenhuma contradição encontrada com [[wiki/concepts/cqrs]] — a fonte principalmente organiza e nomeia de forma mais sistemática (dois motivadores, seis técnicas em duas categorias) trade-offs que já apareciam espalhados nas fontes anteriores (Fowler, Código Fonte TV, Full Cycle, cache-e-redis).

## Raw Quotes

> "Se eu tenho leituras e escritas em volumes muito diferentes, eu posso querer escalar de forma independente — então faz sentido eu separar o meu software em dois blocos."

> "O CQRS não força você a ter código-fonte diferente — você pode, no mesmo código-fonte, ter deployments com réplicas ou gatilhos de escalabilidade diferentes."

> "Se eu tô escrevendo dentro de uma transação nessa base e depois faço uma escrita no serviço de query, o serviço de query acabou sendo também um serviço de escrita — então eu quebrei essa separação entre um só escreve e o outro só consome."

> "Eu preciso garantir consistência na minha base e no meu evento — se eu tenho uma inconsistência entre o que eu salvei e o que eu postei, eu vou gerar uma inconsistência entre o que eu salvei e o que eu li."

> "O CQRS adiciona muita complexidade no sistema... mas sempre faça a pergunta: vale a pena? Como toda pergunta boa de system design."
