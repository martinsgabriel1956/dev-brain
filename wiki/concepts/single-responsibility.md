---
type: concept
title: "Single Responsibility Principle"
aliases: ["SRP", "princípio da responsabilidade única", "single responsibility"]
date_created: 2026-04-25
date_updated: 2026-04-25
source_count: 1
tags: [single-responsibility, solid, software-design, clean-code]
skill: tech-mentor-backend
status: stub
---

# Single Responsibility Principle (SRP)

Uma unidade de código (função, classe, módulo) deve ter **uma única razão para mudar**.

Robert C. Martin: "A class should have only one reason to change." — ou seja, apenas um stakeholder/ator deveria poder exigir mudança naquela unidade.

## Na prática

Uma função que busca, valida, transforma e envia dados tem quatro razões para mudar: mudança no banco, mudança na regra de negócio, mudança no formato de saída, mudança na API destino. Viola SRP.

```typescript
// viola SRP — 4 razões para mudar
function processarPedido(id: string) { /* busca + valida + transforma + envia */ }

// respeita SRP — cada função muda por uma razão
function buscarPedido(id: string) { /* muda quando o banco muda */ }
function validarPedido(pedido: Pedido) { /* muda quando a regra de negócio muda */ }
function transformarPedido(pedido: Pedido) { /* muda quando o formato muda */ }
function enviarPedido(payload: PedidoPayload) { /* muda quando a API muda */ }
```

## SRP não é "fazer apenas uma coisa"

Uma função pode orquestrar múltiplas operações e ainda ter responsabilidade única — se a razão de existir dela for apenas a orquestração. O critério é o ator que causa a mudança, não o número de linhas.

## Relações

- [[acoplamento]] — SRP é a diretriz que leva a baixo acoplamento entre responsabilidades
- [[coesao]] — SRP é a diretriz que leva a alta coesão dentro de uma unidade
- [[abstracao]] — separar responsabilidades cria as fronteiras naturais para abstrações

## Key sources

- [[wiki/sources/acoplamento-abstracao-estado]]
