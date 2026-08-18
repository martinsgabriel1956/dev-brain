---
type: concept
title: "Task-Based UI"
aliases: ["UI baseada em tarefas", "interface orientada a intenção"]
date_created: 2026-08-17
date_updated: 2026-08-17
source_count: 1
tags: [cqrs, ux, ddd, arquitetura]
skill: tech-mentor-system-design
status: stub
---

# Task-Based UI

## TL;DR

Interface desenhada em torno da **intenção do usuário** (uma tarefa concreta que ele quer realizar), em vez de ser uma camada fina de CRUD sobre o banco de dados. É o requisito de UX que dá sentido ao lado de Command em [[wiki/concepts/cqrs]].

## Contexto

Numa UI CRUD tradicional, o usuário edita qualquer campo de um registro genérico — "criar", "ler", "atualizar", "excluir". Isso obedece à estrutura do banco, mas perde a intenção real: por que o usuário está mudando aquele dado? Uma task-based UI expõe ações nomeadas pela intenção (ex.: `CancelarPedido`, `AprovarReembolso`, `MarcarComoEntregue`) em vez de um formulário genérico de edição.

Essa abordagem alinha a interface ao vocabulário do domínio — próximo da Ubiquitous Language de [[wiki/concepts/ddd]] — e faz o Command emitido carregar semântica de negócio, não apenas um diff de campos.

## Key Sources

- [[wiki/sources/cqrs-dicionario-programador-codigo-fonte-tv]] — explica task-based UI como um dos quatro aspectos de implementação de CQRS
