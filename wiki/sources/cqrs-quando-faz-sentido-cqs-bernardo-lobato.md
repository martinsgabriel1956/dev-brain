---
type: source
title: "CQRS: o que é, de onde veio (CQS) e quando faz sentido"
aliases: ["cqrs bernardo lobato", "cqs ao cqrs"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/cqrs-quando-faz-sentido-cqs-bernardo-lobato.md
source_url: ""
author: "Bernardo Lobato"
date_published: ""
date_ingested: 2026-10-09
source_count: 1
tags: [cqrs, cqs, arquitetura, read-model, write-model, trade-off, consistencia-eventual]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

[[wiki/entities/bernardo-lobato|Bernardo Lobato]] apresenta o [[wiki/concepts/cqrs]] como **decisão arquitetural condicional**: nasce do [[wiki/concepts/cqs|CQS]] de [[wiki/entities/bertrand-meyer|Bertrand Meyer]] (1988, nível de operação em objetos) e sobe de nível ao separar **modelos** de escrita e leitura. Só se justifica quando há [[wiki/concepts/assimetria-leitura-escrita|assimetria real]] entre os dois lados e a complexidade extra é compensada; **não exige** microsserviços, event sourcing, mensageria, Kafka nem dois bancos.

## Key Claims

**Claim:** CQRS não exige microsserviços, event sourcing, mensageria ou dois bancos; pode ser aplicado num monólito com o mesmo banco. O conceito está na separação de responsabilidades, não na infraestrutura.
**Evidence:** definição do autor; arquitetura distribuída só aparece se houver motivo para separar física/operacionalmente.
**Confidence:** alta (bate com [[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] e [[wiki/sources/cqrs-martin-fowler]]).

**Claim:** CQS (Meyer, *Object-Oriented Software Construction*, 1988) separa operações de um objeto em commands (mudam estado) e queries (não mudam, sem efeito colateral); é princípio de design interno, não separa banco, serviço ou modelo.
**Evidence:** `changeAddress` vs `getAddress`; exemplo de notificações (`visualizar` que também marca como lida → separar em `obterNaoLidas` e `marcarComoLidas`; UI pode ficar igual).
**Confidence:** alta; ver [[wiki/concepts/efeito-colateral]]. Ressalva [external]: a edição de 1988 é da Prentice Hall; o CQS aparece no cap. de design de classes (a 2ª edição é de 1997).

**Claim:** CQRS = CQS elevado do nível de operação ao nível de **modelo**: write model (regras, invariantes) e read model (formato de consulta, desnormalizado, várias projeções).
**Evidence:** exemplos de pedido (e-commerce) e extrato (financeiro).
**Confidence:** alta.

**Claim:** Critérios para adotar: (1) assimetria entre leitura e escrita — não só proporção de volume, mas natureza do trabalho; (2) problema concreto (contenção, ex.: contador de views com tabela travada); (3) a separação simplifica uma parte importante; (4) a complexidade extra é compensada.
**Evidence:** pedido vs tela consolidada; contador de visualizações; extrato bancário; pedidos simples como contraexemplo.
**Confidence:** alta (opinião fundamentada, sem dados).

**Claim:** Custos: dois módulos, mecanismo de sincronização, possível [[wiki/concepts/eventual-consistency|consistência eventual]], debug mais difícil (gravou? publicou? projetou? atualizou?), mais componentes para a equipe.
**Evidence:** argumento do autor.
**Confidence:** alta.

**Claim:** CRUD simples, necessidades iguais, baixo volume → manter arquitetura simples é decisão válida.
**Evidence:** conclusão do vídeo; "complexidade do sistema por si só não justifica".
**Confidence:** alta.

## Entities

[[wiki/entities/bernardo-lobato]], [[wiki/entities/bertrand-meyer]].

## Concepts

[[wiki/concepts/cqrs]], [[wiki/concepts/cqs]], [[wiki/concepts/assimetria-leitura-escrita]], [[wiki/concepts/read-model]], [[wiki/concepts/projecao]], [[wiki/concepts/efeito-colateral]], [[wiki/concepts/desnormalizacao]], [[wiki/concepts/eventual-consistency]], [[wiki/concepts/over-engineering]], [[wiki/concepts/event-driven-architecture]], [[wiki/concepts/event-sourcing]], [[wiki/concepts/materialized-view]], [[wiki/concepts/ddd]], [[wiki/concepts/precondicao-poscondicao-invariante]], [[wiki/concepts/contencao-de-lock-leitura-escrita]], [[wiki/concepts/tradeoff-arquitetural]].

## Open Questions

- O autor promete vídeo sobre estratégias de implementação (sincronização, falhas); ainda sem cobertura nesta fonte — ver técnicas em [[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]].
- Contador de views usa "YouTube hipotético"; sem dados reais de como o YouTube implementa.
- Nada sobre como tratar leitura logo após escrita ([[wiki/concepts/read-your-writes]]) na consistência eventual.
- Menciona "query" no CQS como sem efeito colateral algum; na prática, logs/caches são tolerados — a fonte não discute.

## Quotes

> "O conceito fundamental tá na separação das responsabilidades e não na infraestrutura."

> "Não basta a solução funcionar: o benefício que ela traz precisa justificar a complexidade que a gente tá introduzindo."

> "Existe uma diferença entre leitura e escrita que justifique a complexidade de manter esses dois lados separados?"
