---
type: concept
title: "Detector de N+1"
aliases: ["n+1 detector", "query counter middleware", "n plus 1"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
tags: [n-plus-um, performance, orm, middleware, banco-de-dados, ia]
skill: tech-mentor-ai
status: stub
---

## TL;DR

Um middleware que conta queries por request e loga um alerta quando o número ultrapassa um threshold. Detecta N+1 antes de ir para produção — o bug mais comum no código gerado por LLMs.

## Por que LLMs Geram N+1

LLMs constroem loops com queries individuais em vez de batch/JOIN. Em dev com 100 requests: invisível. Em prod com 10.000 requests × 20 queries = 200.000 queries no banco.

## Implementação

```python
# Qualquer stack com ORM — Django, Prisma, ActiveRecord
def query_counter_middleware(request, next):
    with count_queries() as counter:
        response = next(request)

    if counter.total > THRESHOLD:  # ex: 15
        log.warning(f"N+1: {counter.total} queries em {request.path}")

    return response
```

## Relacionado

- [[banco-de-dados]] — N+1, índices, connection pooling
- [[vibe-coding]] — contexto: bug mais frequente em código gerado por IA

## Key Sources

- [[sources/apagao-de-seniors-vibe-coding]]
