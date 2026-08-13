---
type: entity
title: "Principles of Product Development Flow"
aliases: ["Principles of Product Development Flow", "Reinertsen", "Donald Reinertsen"]
date_created: 2026-08-10
date_updated: 2026-08-13
source_count: 2
tags: [livro, lean, fluxo, engineering-management, teoria-de-filas, referencia]
skill: tech-mentor-leadership
status: stub
---

# Principles of Product Development Flow

Livro de gestão de desenvolvimento de produto atribuído a **Donald G. Reinertsen** `[external]` (2009), citado em [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] como fonte da regra de **nunca alocar 100% da capacidade** de um time. A obra aplica teoria de filas e princípios lean ao fluxo de desenvolvimento, argumentando que alta utilização de recursos aumenta o tempo de ciclo de forma não-linear — daí a defesa de manter [[wiki/concepts/folga-de-capacidade-slack|folga (slack)]] no sistema.

> **Nota de verificação:** a transcrição da fonte menciona apenas o título do livro (sem tradução em português), não o autor. A atribuição a Donald Reinertsen e o ano vêm de conhecimento externo `[external]`, não confirmados contra a fonte primária nesta ingestão.

## Segunda Fonte: "Inventário É Custo" Aplicado a Pull Requests

[[wiki/sources/pull-requests-por-que-falham-alternativas-sem-pr]] cita o mesmo livro (na transcrição, com o título provavelmente garbled "Principles of *Software* Development Flow" — tratado aqui como a mesma obra, sem confirmação literal) como origem da tese de que **inventário é custo**, de raiz toyotista, aplicada dessa vez a pull requests abertos: código não mergeado é código que não gera valor, com exemplo numérico de custo salarial por semana de PR parado. Ver [[wiki/concepts/inventario-e-custo]] para o desenvolvimento completo do argumento. Essa é uma aplicação diferente da já registrada abaixo (folga de capacidade de time) — mesmo princípio de fluxo, unidade de análise diferente (PR individual vs. capacidade agregada do time).

## Key Sources

- [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] — cita o livro como base da "regra dos ~20%" de folga de capacidade
- [[wiki/sources/pull-requests-por-que-falham-alternativas-sem-pr]] — "inventário é custo" aplicado a PR aberto (custo de código parado, cadência de revisão diária/2x-dia)
