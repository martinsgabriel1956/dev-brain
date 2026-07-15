---
type: concept
title: "Acoplamento"
aliases: ["coupling", "baixo acoplamento", "alto acoplamento"]
date_created: 2026-04-25
date_updated: 2026-07-15
source_count: 2
tags: [acoplamento, software-design, clean-code, arquitetura]
skill: tech-mentor-backend
status: stable
---

# Acoplamento

Acoplamento mede o **grau de dependência entre partes de um sistema**. Não é sobre estar fisicamente junto — é sobre quanto uma mudança em A força uma mudança em B.

## Alto acoplamento (problema)

Uma função que busca dados, valida, transforma, envia e loga tem todas as etapas interdependentes. Mudar o schema do banco obriga a alterar a validação. Mudar o formato da API obriga a alterar a transformação.

```typescript
// alto acoplamento — tudo numa função
function processarPedido(pedidoId: string) {
  const pedido = db.query(`SELECT * FROM pedidos WHERE id = '${pedidoId}'`);
  if (!pedido || pedido.status !== "pendente") throw new Error("Inválido");
  const payload = { id: pedido.id, total: pedido.valor * 1.1 };
  await api.post("/pedidos", payload);
  console.log({ message: "Pedido processado", pedidoId });
}
```

Analogia: quebra-cabeça com peças coladas. Não dá para tirar uma sem destruir as vizinhas.

## Baixo acoplamento (solução)

Cada função tem uma responsabilidade. Mudanças ficam locais.

```typescript
async function buscarPedido(pedidoId: string) { ... }
function validarPedido(pedido: Pedido) { ... }
function transformarPedido(pedido: Pedido) { ... }
async function enviarPedido(payload: PedidoPayload) { ... }
```

Mudança no banco → só `buscarPedido`. Mudança na API → só `enviarPedido`.

## Por que importa

Sistemas altamente acoplados congelam: uma mudança pequena quebra coisas inesperadas, o time tem medo de mexer, o código para de evoluir. O próximo passo é sempre "precisamos refatorar tudo".

## Relações

- [[abstracao]] — abstração é o mecanismo que permite baixo acoplamento entre módulos
- [[single-responsibility]] — SRP é a diretriz que orienta como separar responsabilidades
- [[coesao]] — conceito complementar: coesão alta dentro de um módulo + acoplamento baixo entre módulos é o alvo
- [[efeito-colateral]] — funções com efeitos colaterais ocultos aumentam o acoplamento implícito

## Key sources

- [[wiki/sources/acoplamento-abstracao-estado]]
- [[sources/ports-and-adapters-codebase-para-ia]] — forte acoplamento em god class quebra três módulos por uma mudança
- [[wiki/sources/design-pattern-adapter]] — `new` de uma classe concreta de baixo nível (lib externa) dentro de uma classe de alto nível é a manifestação de acoplamento que o [[wiki/concepts/adapter-pattern]] resolve
