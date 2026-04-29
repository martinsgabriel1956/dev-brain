---
type: concept
title: "Logs em Produção"
aliases: ["logging estruturado", "logs com contexto", "logs > código"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
tags: [logging, observabilidade, producao, debugging, craftsmanship]
skill: tech-mentor-leadership
status: stub
---

## TL;DR

Logs são mais importantes que o código. Quando algo quebra em produção às 3h, logs determinam se você resolve em minutos ou passa horas debugando às cegas.

## A Regra

Logue tudo que importa — inputs, outputs, erros — sempre com contexto suficiente para reconstruir o que aconteceu sem precisar do stack trace completo.

```python
# RUIM
print("erro")

# BOM
logger.error("Falha ao processar pagamento", extra={
    "user_id": user.id,
    "amount": amount,
    "error": str(e)
})
```

## Relacionado

- [[observabilidade]] — logs como um dos três pilares de observabilidade
- [[strings-de-log-integras]] — nunca quebrar mensagens de log (impossibilita grep)

## Key Sources

- [[sources/5-principios-programador]]
