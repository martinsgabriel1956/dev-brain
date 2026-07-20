---
type: concept
title: "Acoplamento"
aliases: ["coupling", "baixo acoplamento", "alto acoplamento"]
date_created: 2026-04-25
date_updated: 2026-07-19
source_count: 3
tags: [acoplamento, software-design, clean-code, arquitetura, under-engineering]
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

## Acoplamento como sinal de under-engineering, não só de over-engineering

[[wiki/sources/underengineering-overengineering-mario-souto]] traz acoplamento (tight coupling) como um dos sintomas do lado oposto do espectro descrito em [[wiki/concepts/under-engineering]] — não é uma abstração excessiva, é a ausência de qualquer separação. O exemplo dado é concreto e reconhecidamente parcial: lógica de login e de criação de conta no mesmo arquivo de autenticação, porque o autor "colocou todos os tipos de autenticação num arquivo só" e reconhece que "poderia quebrar isso um pouco mais". O critério prático que ele usa para decidir onde cortar é funcional, não teórico: "se esse arquivo é o arquivo de login, eu evito colocar coisas de criar conta junto" — a separação de responsabilidades sendo descoberta durante o trabalho ("é um pouco filosófico... conforme você vai trabalhando nos projetos, você vai vendo que existe uma separação natural"), não definida a priori.

## Relações

- [[abstracao]] — abstração é o mecanismo que permite baixo acoplamento entre módulos
- [[single-responsibility]] — SRP é a diretriz que orienta como separar responsabilidades
- [[coesao]] — conceito complementar: coesão alta dentro de um módulo + acoplamento baixo entre módulos é o alvo
- [[efeito-colateral]] — funções com efeitos colaterais ocultos aumentam o acoplamento implícito

## Key sources

- [[wiki/sources/acoplamento-abstracao-estado]]
- [[sources/ports-and-adapters-codebase-para-ia]] — forte acoplamento em god class quebra três módulos por uma mudança
- [[wiki/sources/design-pattern-adapter]] — `new` de uma classe concreta de baixo nível (lib externa) dentro de uma classe de alto nível é a manifestação de acoplamento que o [[wiki/concepts/adapter-pattern]] resolve
- [[wiki/sources/underengineering-overengineering-mario-souto]] — exemplo real de login e criação de conta acoplados no mesmo arquivo; separação tratada como algo que se aprende na prática, não como regra fixa
