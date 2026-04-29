---
date: 2026-04-17
tags: [tech-mentor, mensageria, eventos, versionamento, event-sourcing]
skill: tech-mentor-backend/references/messaging
level: avançado
---

# Event Versioning

## Contexto
Eventos são contratos imutáveis — uma vez publicados em um tópico ou armazenados em um Event Store, não podem ser alterados. Mas o domínio evolui: campos mudam de nome, tipos mudam, novos campos são adicionados. **Event Versioning** é o conjunto de estratégias para evoluir eventos sem quebrar consumers ou corromper o histórico.

O problema é especialmente crítico em **Event Sourcing**: o aggregate state é reconstruído replaying todos os eventos. Um evento antigo que não pode mais ser deserializado quebra o replay.

## Estratégias

### 1. Weak Schema (Tolerant Reader)
A mais simples. O consumer ignora campos desconhecidos e usa defaults para campos ausentes. Funciona bem para adição de campos opcionais.

```typescript
// Consumer tolerante — .passthrough() aceita campos extras
const orderCreatedSchema = z.object({
  orderId: z.string(),
  customerId: z.string(),
  totalAmount: z.number(),
  currency: z.string().default("BRL")  // campo novo com default para eventos antigos
}).passthrough();
```

**Limitação:** não resolve mudança de tipo ou remoção de campo obrigatório.

### 2. Versioning Explícito no Schema

Adiciona um campo `version` (ou `schemaVersion`) ao evento. O consumer usa o número de versão para escolher o deserializador correto.

```typescript
type OrderCreatedV1 = {
  version: 1;
  orderId: string;
  customerId: string;
  total: number; // campo foi renomeado para "totalAmount" na V2
};

type OrderCreatedV2 = {
  version: 2;
  orderId: string;
  customerId: string;
  totalAmount: number;
  currency: string;
};

type OrderCreatedEvent = OrderCreatedV1 | OrderCreatedV2;

function deserializeOrderCreated(raw: unknown): OrderCreatedV2 {
  const event = raw as OrderCreatedEvent;
  
  // Upcast: transforma V1 em V2
  if (event.version === 1) {
    return {
      version: 2,
      orderId: event.orderId,
      customerId: event.customerId,
      totalAmount: event.total,   // renomeado
      currency: "BRL"             // default para eventos antigos
    };
  }

  return event;
}
```

### 3. Upcasting (Event Sourcing)

No Event Sourcing, o upcaster intercepta eventos ao serem carregados do Event Store e os transforma para a versão atual antes de serem aplicados ao aggregate.

```typescript
type Upcaster = (event: StoredEvent) => StoredEvent;

const upcasters: Record<string, Upcaster[]> = {
  "OrderCreated": [
    // Upcast de V1 → V2: renomeia "total" para "totalAmount"
    (event) => {
      if (event.schemaVersion === 1) {
        return {
          ...event,
          data: { ...event.data, totalAmount: event.data.total, currency: "BRL" },
          schemaVersion: 2
        };
      }
      return event;
    },
    // Upcast de V2 → V3: adiciona campo "items" (array vazio para eventos antigos)
    (event) => {
      if (event.schemaVersion === 2) {
        return {
          ...event,
          data: { ...event.data, items: [] },
          schemaVersion: 3
        };
      }
      return event;
    }
  ]
};

function applyUpcasters(event: StoredEvent): StoredEvent {
  const casters = upcasters[event.type] ?? [];
  return casters.reduce((e, upcast) => upcast(e), event);
}

// No repositório, ao carregar eventos:
async function loadEvents(aggregateId: string): Promise<DomainEvent[]> {
  const stored = await eventStore.getEvents(aggregateId);
  return stored.map(applyUpcasters).map(deserialize);
}
```

### 4. Copy-Transform (migração em background)

Para mudanças breaking (ex: dividir um aggregate em dois), cria-se um job que lê todos os eventos antigos e os republica transformados em um novo tópico/stream.

```
events-v1 → [Transform Job] → events-v2
                │
                ▼
        Consumers migram para events-v2
        events-v1 fica disponível por período de deprecação
```

## Regras Gerais para Evolução Segura

| Operação | Seguro? | Estratégia |
|---|---|---|
| Adicionar campo opcional | ✅ | Weak schema + default no consumer |
| Renomear campo | ⚠️ | Upcasting — mantém nome antigo por período |
| Remover campo | ⚠️ | Deprecar e remover após todos consumers migrarem |
| Mudar tipo | ❌ | Copy-transform em novo tópico/stream |
| Dividir evento em dois | ❌ | Copy-transform + novo schema |

## Conceitos Relacionados
[[event-sourcing]] · [[schema-registry]] · [[tolerant-reader]] · [[expand-contract]] · [[kafka]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
