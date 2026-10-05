---
type: concept
title: "Monolito Distribuído"
aliases: ["monolito distribuido", "distributed monolith"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [arquitetura, microsservicos, acoplamento, anti-pattern]
skill: tech-mentor-backend
status: draft
---

# Monolito Distribuído

Serviços separados em deploy, mas acoplados por chamadas síncronas encadeadas: se um dependente (ou externo) cai ou demora, o fluxo inteiro cai. Frase da fonte: "microsserviços que têm dependências fora do microsserviço deles não são microsserviços de verdade; são monolitos distribuídos".

Exemplo: Pedidos chamando por HTTP Pagamentos → Nota Fiscal → Estoque → E-mail, e respondendo ao usuário só no fim; se o gateway de pagamento cair, o pedido falha. Saída: publicar evento e reagir de forma assíncrona ([[wiki/concepts/mensageria]], [[wiki/concepts/comunicacao-assincrona]]), com compensação via [[wiki/concepts/saga-pattern]] quando algo falha.

Relaciona-se a [[wiki/concepts/acoplamento]], [[wiki/concepts/comunicacao-sincrona]], [[wiki/concepts/microsservicos]], [[wiki/concepts/monolito]]. Nota: "monolito distribuído" é termo de uso geral; a definição aqui é a da fonte, não de autoridade externa.

## Key sources

- [[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]]
