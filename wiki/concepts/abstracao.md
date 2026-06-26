---
type: concept
title: "Abstração"
aliases: ["abstraction", "esconder detalhes", "contrato genérico"]
date_created: 2026-04-25
date_updated: 2026-06-26
source_count: 2
tags: [abstracao, software-design, clean-code, arquitetura, interfaces]
skill: tech-mentor-backend
status: stable
---

# Abstração

Abstração é **esconder o que não precisa ser visto**. O consumidor de uma abstração sabe *o que* ela faz, não *como*.

Analogia: você disca um número e aperta ligar. A complexidade de antena, rede e codificação fica oculta. Você só precisa do contrato (número → ligação).

## No código

Abstração é implementada via contratos (tipos, interfaces) que desacoplam o consumidor da implementação concreta.

```typescript
// contrato genérico — consumidor só precisa saber disso
type PedidoRepository = {
  buscarPorId: (id: string) => Promise<Pedido | null>;
};

// implementações concretas — detalhes ocultos
class PedidoRepositoryDB implements PedidoRepository {
  async buscarPorId(id: string) {
    return db.query(`SELECT * FROM pedidos WHERE id = '${id}'`);
  }
}

class PedidoRepositoryAPI implements PedidoRepository {
  async buscarPorId(id: string) {
    return api.get(`/pedidos/${id}`);
  }
}

// consumidor: não sabe se é banco ou API
async function processarPedido(repo: PedidoRepository, pedidoId: string) {
  const pedido = await repo.buscarPorId(pedidoId);
  // ...
}
```

Você pode trocar `PedidoRepositoryDB` por `PedidoRepositoryAPI` **sem tocar em `processarPedido`**.

## Níveis de abstração

- **Baixo nível:** lidar diretamente com banco, HTTP, filesystem
- **Alto nível:** consumir contratos sem saber a implementação

Misturar níveis na mesma função é um code smell — viola [[single-responsibility]] e aumenta [[acoplamento]].

## Relações

- [[acoplamento]] — boa abstração é o que permite baixo acoplamento entre camadas
- [[single-responsibility]] — cada abstração deve representar uma única responsabilidade
- [[hexagonal-architecture]] — Ports & Adapters é a formalização arquitetural de abstração: Port = contrato, Adapter = implementação concreta
- [[dependency-injection]] — DI é o mecanismo que injeta a implementação concreta numa abstração

## Key sources

- [[wiki/sources/acoplamento-abstracao-estado]]
- [[sources/roadmap-dev-senior-2026]] — abstração como pilar 2: camadas que escondem complexidade sem esconder clareza
- [[wiki/sources/10-conceitos-fundamentais-computacao]] — abstração como o #1 conceito fundamental; cada um dos 9 outros conceitos é uma camada de abstração
