---
type: concept
title: "Command Bus"
aliases: ["barramento de comando"]
date_created: 2026-08-17
date_updated: 2026-08-17
source_count: 3
tags: [cqrs, arquitetura, ddd]
skill: tech-mentor-system-design
status: stub
---

# Command Bus

## TL;DR

Mecanismo que roteia um Command até o handler responsável por processá-lo, num sistema orientado a [[wiki/concepts/cqrs]]. Desacopla quem dispara a intenção (ex.: a camada de aplicação/HTTP) de quem sabe executá-la (o handler de domínio).

## Regra Central: Command Não Retorna Dados

Um Command processado pelo command bus deveria retornar **void** — no máximo um ID de referência, nunca os dados completos da entidade alterada. Retornar dados de um Command quebra a separação entre o modelo de escrita e o modelo de leitura, que é a razão de existir do CQRS. Se uma parte do sistema depende de receber dados de volta ao executar uma escrita, esse é um sinal de que essa parte não deveria estar usando CQRS.

## Key Sources

- [[wiki/sources/cqrs-dicionario-programador-codigo-fonte-tv]] — command bus como um dos quatro aspectos de implementação de CQRS, com a regra "Command nunca deve retornar dados"
- [[wiki/sources/cqrs-e-event-sourcing-explicado-na-pratica]] — descreve o mecanismo (ex.: Kafka) que consome eventos do write model e os transforma em projeções de leitura, equivalente ao papel do command bus no lado de escrita
- [[wiki/sources/cqrs-event-sourcing-full-cycle-wesley-williams]] — reforça a regra "Commands retornam void" como sinal de maturidade no design de sistemas orientados a comando
