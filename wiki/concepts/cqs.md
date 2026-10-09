---
type: concept
title: "CQS — Command Query Separation"
aliases: ["command query separation", "separação comando-consulta"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 1
tags: [cqs, design, oop, cqrs, efeito-colateral]
skill: tech-mentor-system-design
status: draft
---

# CQS

## TL;DR

Princípio de design de [[wiki/entities/bertrand-meyer|Bertrand Meyer]] (*Object-Oriented Software Construction*, 1988): cada operação de um objeto é **command** (muda estado, não devolve informação de negócio) **ou query** (devolve informação, nunca muda estado observável). Nunca as duas coisas.

## Por que importa

- Query sem [[wiki/concepts/efeito-colateral]] → uso previsível e reutilizável em outros módulos.
- Mutação explícita → quem chama sabe que o estado muda.
- Exemplo: `visualizarNotificacoes` que busca *e* marca como lida vira `obterNaoLidas` + `marcarComoLidas`; a UI pode não mudar.

## CQS vs CQRS

| | CQS | [[wiki/concepts/cqrs]] |
|---|---|---|
| Nível | operação/método de um objeto | modelo/componente da aplicação |
| Separa | commands de queries | write model de read model |
| Infra | nenhuma | opcional (mesmo banco serve) |

CQRS é CQS levado a outro nível de abstração (e atribuído a [[wiki/entities/greg-young]]). Ver também [[wiki/concepts/precondicao-poscondicao-invariante]] (Design by Contract, mesmo autor).

## Key sources

- [[wiki/sources/cqrs-quando-faz-sentido-cqs-bernardo-lobato]] — definição, exemplo Customer e notificações
- [[wiki/sources/cqrs-e-event-sourcing-explicado-na-pratica]] — CQS como `get`/`set` em nível de função
