---
type: concept
title: "Logging Estruturado"
aliases: ["structured logging", "logs estruturados", "logging com contexto"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 1
tags: [logging, observabilidade, producao, debugging, boas-praticas]
skill: tech-mentor-leadership
status: stable
---

# Logging Estruturado

## TL;DR

Prática de registrar eventos de sistema com metadados estruturados (campos chave-valor) em vez de strings livres. Logs sem contexto são inúteis às 3h da manhã quando algo quebra em produção.

## Por que Importa

Todo código quebra em produção. Sem logs estruturados:
- Você sabe que algo falhou, mas não **o quê** de fato aconteceu
- Debugging se torna busca cega em logs de texto livre
- Correlação entre eventos (mesma requisição, mesmo usuário) é impossível

Com logs estruturados, cada evento carrega o contexto necessário para entender, reproduzir e corrigir o problema.

## Anatomia de um Log Estruturado

```python
# RUIM: log sem contexto
print("erro")

# BOM: log com contexto estruturado
logger.error("Falha ao processar pagamento", extra={
    "user_id": user.id,
    "amount": amount,
    "payment_method": method,
    "error": str(e),
    "trace_id": request.trace_id
})
```

## Campos Essenciais

| Campo | Por que incluir |
|-------|-----------------|
| `user_id` / `tenant_id` | Correlação a um ator |
| `trace_id` / `request_id` | Correlação entre serviços |
| `error` / `exception` | Causa raiz |
| `input` relevante | O que acionou o evento |
| `timestamp` | Sequência temporal |

## Integração com Observabilidade

Logging estruturado é um dos três pilares da [[wiki/concepts/observabilidade|observabilidade]] junto com métricas e traces. Logs sem estrutura não integram bem com ferramentas de agregação como Datadog, Grafana Loki ou ELK Stack.

## Key Sources

- [[wiki/sources/5-principles-that-changed-me-as-a-programmer]]
