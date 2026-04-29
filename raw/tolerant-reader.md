---
date: 2026-04-17
tags: [tech-mentor, arquitetura, principios, integracao, compatibilidade]
skill: tech-mentor-backend/references/integration-patterns
level: intermediário
---

# Tolerant Reader

## Contexto
Padrão de Martin Fowler: um serviço que consome dados de outro deve ser **tolerante com o formato recebido** — ignorar campos desconhecidos, não quebrar com campos ausentes opcionais, e processar apenas o que precisa.

O objetivo é desacoplar a evolução do produtor da evolução do consumidor. Sem esse princípio, qualquer campo novo ou removido no produtor quebra todos os consumidores.

## O Problema Sem Tolerant Reader

```typescript
// Consumidor frágil — quebra com qualquer mudança no contrato
type UserEvent = {
  id: string;
  name: string;
  email: string;
};

function processUserEvent(event: UserEvent) {
  // Se o produtor adicionar um campo "phone" → TypeScript com strict extras pode rejeitar
  // Se o produtor remover "name" → runtime error
  const greeting = `Hello, ${event.name}`;
  return greeting;
}
```

## Implementação Correta

```typescript
// 1. Tipo permissivo para desserialização
type UserEventRaw = {
  id: string;
  name?: string;       // opcional — pode não existir em versões antigas
  email?: string;
  [key: string]: unknown; // tolera campos extras sem quebrar
};

// 2. Extrai só o que precisa, com defaults
function extractUserData(raw: UserEventRaw) {
  return {
    id: raw.id,
    displayName: raw.name ?? raw.email ?? "Unknown user", // fallback gracioso
    email: raw.email
  };
}

// 3. Valida só o que é necessário, não o contrato completo
import { z } from "zod";

const userEventSchema = z.object({
  id: z.string(),
  name: z.string().optional(),
  email: z.string().email().optional()
}).passthrough(); // .passthrough() = aceita campos extras sem rejeitar

function processUserEvent(raw: unknown) {
  const result = userEventSchema.safeParse(raw);
  if (!result.success) {
    console.log({ message: "Invalid event format", errors: result.error.issues });
    return; // descarta sem quebrar o serviço
  }
  const data = extractUserData(result.data);
  // ...
}
```

## Tolerant Reader em Protobuf/Avro

Em schemas binários, o Tolerant Reader é implementado pelo próprio protocolo:

| Protocolo | Comportamento com campos desconhecidos |
|---|---|
| **Protobuf** | Campos com field numbers desconhecidos são ignorados por default |
| **Avro** | Schema evolution com `default` values — campos novos têm default se ausentes |
| **JSON** | Manual — o consumidor deve ignorar extras explicitamente |

## Expand-Contract como complemento

Tolerant Reader no consumidor + **Expand-Contract** no produtor = evolução de contrato sem breaking changes:

```
Fase 1 — Expand: produtor adiciona novo campo, consumidor ignora (Tolerant Reader)
{ "id": "1", "name": "Alice" }                   → { "id": "1", "name": "Alice", "phone": "..." }

Fase 2 — Consumidores migram para ler o novo campo (quando precisarem)

Fase 3 — Contract: produtor remove campo antigo (todos consumidores já migraram)
{ "id": "1", "phone": "..." }
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Compatibilidade | Produtor evolui sem coordenar com todos os consumidores | Difícil detectar quando um campo foi removido sem perceber |
| Resiliência | Consumidor não cai com mudanças no produtor | Campos silenciosamente ignorados podem causar bugs sutis |
| Deploy | Times evoluem independentemente | Contratos implícitos — difícil saber o que realmente é usado |

## Quando Usar / Quando Evitar

**Usar quando:**
- Consumindo eventos de um produtor que você não controla (API externa, outro time)
- Schema evoluirá ao longo do tempo (sempre — em sistemas vivos)
- Usando CDC ou Event Streaming onde versões antigas de eventos coexistem

**Evitar quando (relativo):**
- O consumidor deve validar estritamente o contrato — use Contract Testing (Pact) em vez disso
- Campos opcionais demais criam ambiguidade semântica real no domínio

## Conceitos Relacionados
[[integration-patterns-eip]] · [[cdc-debezium]] · [[kafka]] · [[contract-testing]] · [[dlq-event-patterns]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
