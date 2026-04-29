---
date: 2026-03-29
tags: [tech-mentor, system-design, arquitetura, microsserviços, monolito]
skill: tech-mentor-system-design/references/architecture-foundations
level: arquiteto
---

# Microsserviços vs Monolito Modular

## Contexto

A escolha entre monolito e microsserviços é talvez a decisão arquitetural mais debatida — e mais mal aplicada — da engenharia moderna. Times adotam microsserviços por hype, sem necessidade real, e colhem complexidade operacional sem os benefícios prometidos.

A pergunta certa não é *"monolito ou microsserviços?"*, mas *"qual é o custo de cada opção dado o meu contexto atual?"*

---

## Como Funciona

### Monolito Modular

Um único processo deployável, com código dividido em módulos com fronteiras bem definidas. Módulos se comunicam via chamadas in-process, não via rede.

```
┌─────────────────────────────────────────┐
│            Monolito Modular             │
│                                         │
│  ┌──────────┐  ┌──────────┐  ┌───────┐ │
│  │ Pedidos  │  │Pagamentos│  │Usuário│ │
│  │          │  │          │  │       │ │
│  │ (módulo) │  │ (módulo) │  │(módulo│ │
│  └────┬─────┘  └────┬─────┘  └───┬───┘ │
│       └─────────────┴────────────┘     │
│                     │                  │
│              Banco de Dados            │
└─────────────────────────────────────────┘
```

**Fronteira de módulo** significa: interface pública explícita (sem acesso direto a internals de outro módulo), dependências declaradas, e idealmente schema de banco separado por módulo — mesmo que no mesmo banco.

### Microsserviços

Cada serviço é um processo independente, com deploy, banco e ciclo de vida separados. A comunicação acontece via rede (HTTP/gRPC/mensageria).

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│  Pedidos │────▶│Pagamentos│     │ Usuário  │
│ service  │     │ service  │     │ service  │
│          │     │          │     │          │
│  DB:     │     │  DB:     │     │  DB:     │
│ Postgres │     │ Postgres │     │ Postgres │
└──────────┘     └──────────┘     └──────────┘
```

---

## Trade-offs

| Critério | Monolito Modular | Microsserviços |
|---|---|---|
| **Time** | 1–5 pessoas | 5+ times independentes |
| **Deploy** | 1 artefato, simples | Pipeline por serviço, infra complexa |
| **Escala** | Vertical + read replicas | Escala granular por serviço |
| **Latência** | Chamadas in-process (µs) | Chamadas de rede (ms) |
| **Consistência** | Transações ACID nativas | Eventual consistency, saga necessário |
| **Observabilidade** | Simples (1 app, 1 log) | Distributed tracing obrigatório |
| **Desenvolvimento** | Rápido, sem overhead de infra | Overhead alto: Docker, K8s, service discovery |
| **Debugging** | Stack trace local | Rastreamento cross-service |
| **Falha** | Processo inteiro falha | Falha isolada por serviço |
| **Organização** | 1 time cuida de tudo | Cada time tem ownership claro |

---

## Quando Usar / Quando Evitar

### Comece com Monolito Modular quando:
- Time pequeno (< 10 engenheiros)
- Produto ainda em validação (pivots são baratos)
- Domínio ainda não completamente mapeado
- Não há necessidade de escala por componente diferente
- Velocity importa mais que isolamento

### Extraia para Microsserviços quando houver necessidade real:
- **Times independentes**: dois times não conseguem trabalhar no mesmo repo sem conflito constante
- **Escala diferente**: o serviço de busca precisa de 20× mais recursos que o resto
- **Deploy independente**: um componente tem ciclo de release diferente dos demais
- **Isolamento de falha crítico**: uma parte do sistema não pode afetar outra (pagamento vs catálogo)
- **Tech stack diferente**: um serviço precisa de Python/ML enquanto o resto é Node.js

### Nunca extraia por:
- Hype ou "porque é moderno"
- Cada CRUD virar um serviço
- Sem times com ownership claro de cada serviço

---

## O Distributed Monolith — O Pior dos Mundos

O erro mais comum: pegar um monolito mal estruturado e dividi-lo em serviços sem cuidar das fronteiras. O resultado é um *distributed monolith*: você tem toda a complexidade de microsserviços sem nenhum dos benefícios.

**Sintomas**:
- Deploy de serviço A sempre exige deploy de serviço B
- Mudança de schema do serviço A quebra o serviço B
- Não existe time com ownership claro de nada
- Chamadas síncronas em cadeia: A → B → C → D (latência acumulada, falha em cascata)

**Diagnóstico rápido**: se você não consegue fazer deploy de um serviço sem coordenar com outros times, você tem um distributed monolith.

---

## Caminho Arquitetural Saudável

```
1. Monolito bem modularizado
        ↓
2. Identificar módulo com necessidade real de extração
   (escala diferente / time separado / deploy independente)
        ↓
3. Extrair módulo com banco próprio (Strangler Fig Pattern)
        ↓
4. Microsserviço com ownership claro
```

**Strangler Fig Pattern**: em vez de reescrever tudo de uma vez, você coloca o novo serviço na frente do monolito via API Gateway. Gradualmente, o novo serviço "estrangula" o monolito ao assumir funcionalidades — sem big bang rewrite.

```
                ┌───────────────┐
Clientes ──────▶│  API Gateway  │
                └───────┬───────┘
                        │
          ┌─────────────┴──────────────┐
          │                            │
          ▼                            ▼
  ┌───────────────┐           ┌────────────────┐
  │  Novo Serviço │           │    Monolito    │
  │  (Pagamentos) │           │  (restante)    │
  └───────────────┘           └────────────────┘
```

---

## Conway's Law na Prática

*"Organizations which design systems are constrained to produce designs which are copies of the communication structures of those organizations."* — Melvin Conway, 1967

Antes de propor microsserviços, verifique a estrutura de times. Se dois serviços são mantidos pelo mesmo time, eles vão convergir para um monolito de fato — mesmo que sejam processos separados.

**Inverse Conway Maneuver**: design a organização que você quer ver refletida na arquitetura. Quer microsserviço independente? Garanta time independente com ownership completo: código, banco, deploy, on-call.

---

## Código de Referência

### Monolito Modular — fronteira explícita entre módulos

```typescript
// ✅ módulo Pedidos expõe apenas a interface pública
// src/modules/pedidos/index.ts
export { criarPedido } from "./usecases/criar-pedido.usecase";
export { buscarPedidoPorId } from "./usecases/buscar-pedido.usecase";
export type { Pedido, CriarPedidoDTO } from "./types/pedido.types";

// ❌ nunca importar internals de outro módulo diretamente
import { PedidoRepository } from "../pedidos/repositories/pedido.repository"; // proibido
```

```typescript
// ✅ módulo Pagamentos usa a interface pública de Pedidos
import { buscarPedidoPorId } from "../pedidos";

export async function processarPagamento(pedidoId: string, valor: number) {
  const pedido = await buscarPedidoPorId(pedidoId);
  if (!pedido) throw new PedidoNaoEncontradoError(pedidoId);
  // ...
}
```

### Microsserviços — comunicação via HTTP com contrato explícito

```typescript
// Serviço de Pagamentos chama Serviço de Pedidos via HTTP
type PedidoResponse = {
  id: string;
  valor: number;
  status: "pendente" | "confirmado" | "cancelado";
};

async function buscarPedido(pedidoId: string): Promise<PedidoResponse> {
  const response = await fetch(`${PEDIDOS_SERVICE_URL}/pedidos/${pedidoId}`, {
    headers: { Authorization: `Bearer ${getServiceToken()}` }
  });

  if (!response.ok) throw new PedidoServiceError(response.status);
  return response.json() as Promise<PedidoResponse>;
}
```

---

## Conceitos Relacionados

[[api-gateway-bff]] · [[service-mesh]] · [[cqrs]] · [[event-sourcing]] · [[distributed-tracing]] · [[circuit-breaker]] · [[zero-downtime-deploy]]

---

*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-29*
