---
type: concept
title: "Routing Key e Binding Key"
aliases: ["routing key", "binding key", "binding"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [rabbitmq, routing-key, binding-key, exchange]
skill: tech-mentor-backend
status: draft
---

# Routing Key e Binding Key

- **Routing key:** rótulo que o producer anexa à mensagem ao publicar (ex.: `order.created`).
- **Binding key:** chave da ligação entre uma [[wiki/concepts/exchange-rabbitmq|exchange]] e uma fila; é o que a exchange compara com a routing key.

Cada tipo de exchange as trata diferente: direct exige igualdade; topic interpreta a binding como padrão (`*` uma palavra, `#` zero ou mais); fanout e headers ignoram a routing key. Convenção de nomes com pontos (`dominio.evento`) é o que torna o topic útil.

## Key sources

- [[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]]
