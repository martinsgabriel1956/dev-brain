---
date: 2026-03-29
tags: [tech-mentor, system-design, avançado, crdt, colaboração, tempo-real, ot]
skill: tech-mentor-system-design/references/collaborative-systems-design
level: arquiteto
---

# CRDT e Colaboração em Tempo Real

## Contexto

Sistemas colaborativos — Google Docs, Figma, Notion, Linear — resolvem o problema de múltiplos usuários editando o mesmo estado simultaneamente, de dispositivos diferentes, potencialmente offline. O desafio central é **resolver conflitos de forma determinística sem coordenação centralizada bloqueante**.

Duas abordagens dominam: OT (Operational Transformation) e CRDT (Conflict-free Replicated Data Type). A escolha define a arquitetura inteira.

---

## O Problema Fundamental

```
Estado inicial: "Hello"

Usuário A (online, SP):  deleta "H" → "ello"
Usuário B (offline, NY): insere "!" no final → "Hello!"

Ambos sincronizam. Qual é o estado final correto?

Sem algoritmo de merge: resultado depende da ordem de chegada
  → "ello!" ou "!ello" → ambos errados

Com OT ou CRDT: resultado determinístico → "ello!"
```

---

## OT vs CRDT

| Aspecto | Operational Transformation (OT) | CRDT |
|---|---|---|
| **Mecanismo** | Transforma operações em relação ao estado atual | Estrutura de dados que sempre converge |
| **Servidor central** | Necessário (sequencia todas as operações) | Não necessário (P2P possível) |
| **Complexidade** | Alta — algoritmo de transformação sutil, fácil de introduzir bugs | Moderada — design da estrutura de dados |
| **Latência** | Depende do servidor central (round-trip obrigatório) | Pode ser local-first (aplica localmente, sincroniza depois) |
| **Histórico** | Preservado como sequência de operações | Não preservado nativamente |
| **Offline** | Limitado | Nativo |
| **Exemplos** | Google Docs, Etherpad | Figma, Linear, Y.js, Liveblocks |

**Quando usar OT**: histórico de operações ordenado é requisito ("João deletou o parágrafo 3 às 14:32"), undo/redo colaborativo preciso.

**Quando usar CRDT**: offline-first, P2P, simplicidade de implementação, escala sem servidor de sequenciamento.

---

## CRDT — Como Funciona

CRDT (Conflict-free Replicated Data Type) é uma estrutura de dados com a propriedade matemática de que merges são sempre comutativas, associativas e idempotentes. Em outras palavras: não importa a ordem em que os updates chegam, o resultado final é sempre o mesmo.

### Propriedades formais

```
Comutatividade: merge(A, B) = merge(B, A)
               ordem não importa

Associatividade: merge(merge(A, B), C) = merge(A, merge(B, C))
                agrupamento não importa

Idempotência:   merge(A, A) = A
               receber o mesmo update duas vezes não causa problemas
```

### Tipos básicos de CRDT

**G-Counter (Grow-only Counter)**:
```
Cada nó mantém seu próprio contador
Merge: pega o máximo de cada nó
Value: soma de todos os contadores

Node A: [3, 0, 0] → incrementou 3 vezes
Node B: [3, 2, 0] → Node A incrementou 3, Node B 2
Merge:  [3, 2, 0] → valor = 5
```

**LWW-Register (Last-Write-Wins)**:
```
Cada write tem timestamp
Merge: sempre vence o write com maior timestamp
Risco: clock skew → usar Hybrid Logical Clock (HLC) em vez de wallclock
```

**OR-Set (Observed-Remove Set)**:
```
Problema do Set sem tag: add("item") em A e remove("item") em B concorrente
  → Qual vence? Add ou Remove?

OR-Set: cada add gera um tag único (UUID)
Remove remove apenas tags específicos, não o elemento
Se A adiciona com tag-1 e B remove todos os tags antes de ver tag-1
→ elemento ainda existe (tag-1 sobreviveu)
```

---

## CRDT de Sequência — Para Texto Colaborativo

Texto é uma sequência de caracteres. O problema: inserção por índice conflita — se A insere na posição 3 e B deleta a posição 2, o índice de A ficou inválido.

**Solução**: cada caractere tem um **identificador único globalmente ordenável** — não usa índice.

### Logoot / LSEQ

```
Posição  Char   ID (gerado pelo cliente)
─────────────────────────────────────────
         H      [clientA, t=1, seq=1]
         e      [clientA, t=1, seq=2]
         l      [clientA, t=1, seq=3]
         l      [clientA, t=1, seq=4]
         o      [clientA, t=1, seq=5]

ClientB insere "!" após "o" (sem ver o estado de A):
         !      [clientB, t=2, seq=1]  ← ID entre "o" e fim

Ordenação por ID: "Hello!" — determinístico, independente da ordem de sync
```

### Y.js — o padrão da indústria

Y.js usa YATA (Yet Another Transformation Approach) — estrutura de CRDT otimizada para texto, com compressão eficiente de estado.

```typescript
import * as Y from "yjs";
import { WebsocketProvider } from "y-websocket";

const ydoc = new Y.Doc();
const ytext = ydoc.getText("document");

// Conexão ao servidor de relay
const provider = new WebsocketProvider("wss://relay.example.com", "doc-id-123", ydoc);

// Inserção local — aplicada IMEDIATAMENTE, sem round-trip
ytext.insert(0, "Hello");

// Y.js sincroniza automaticamente com outros clientes
// Convergência garantida independente da ordem de chegada

// Observer para atualizar a UI quando outros clientes editam
ytext.observe(event => {
  console.log("Documento atualizado:", ytext.toString());
});
```

**State vector** — sincronização eficiente:
```typescript
// Ao conectar, clientes trocam apenas o delta — não o documento inteiro
const stateVector = Y.encodeStateVector(ydoc);        // o que eu já sei
const delta = Y.encodeStateAsUpdate(ydoc, remoteStateVector); // o que você não sabe
Y.applyUpdate(ydoc, remoteDelta);                      // aplicar o que recebi
```

---

## Arquitetura — Figma-like (CRDT + Relay Server)

Mesmo usando CRDTs, sistemas de produção usam um servidor central — não para sequenciar, mas para **relay e persistência**:

```
Cliente A ──WebSocket──▶ Relay Server ──WebSocket──▶ Cliente B
    │                         │                           │
    │ aplica localmente        │ só retransmite            │ aplica localmente
    │ (sem esperar ACK)        │ (sem sequenciar)          │ (sem esperar ACK)
    │                         │                           │
    └──────────── CRDT garante convergência ──────────────┘
```

**O Relay Server faz**:
- Retransmitir deltas para todos os clientes na mesma "room"
- Persistir o estado para clientes que entram depois
- Autenticação e autorização

**O Relay Server NÃO faz**:
- Ordenar operações (CRDT não precisa)
- Resolver conflitos (CRDT resolve localmente)
- Ser ponto de verdade do estado (cada cliente tem o estado completo)

---

## Presença e Cursores

Cursores e presença são efêmeros — não precisam de CRDT. Broadcast simples via WebSocket:

```typescript
type PresenceUpdate = {
  userId: string;
  cursor: { x: number; y: number } | null;
  selection: { start: number; end: number } | null;
  color: string;   // determinístico por userId — sem conflito de cor
  name: string;
};

// Throttle: máximo 20 updates/segundo por usuário
const throttledSendCursor = throttle((cursor: Point) => {
  ws.send(JSON.stringify({ type: "cursor", cursor }));
}, 50);
```

Presença expira quando a conexão WebSocket cai — sem necessidade de cleanup explícito.

---

## Persistência

```
Edição ativa   → Redis (in-memory, TTL 24h após última edição)
                    ↓ job de persistência a cada 5s ou em idle
Documento frio → PostgreSQL / S3 (estado serializado do Y.Doc)

Novo cliente entra na sessão ativa:
  1. Fetch do estado atual do Redis
  2. Recebe deltas em tempo real via WebSocket

Novo cliente entra em sessão fria:
  1. Fetch do estado base do PostgreSQL
  2. Fetch de updates recentes do Redis (desde o último persist)
  3. Aplica tudo → estado atualizado
```

```typescript
// Persistência periódica
const persistInterval = setInterval(async () => {
  const state = Y.encodeStateAsUpdate(ydoc);
  await db.document.upsert({
    where: { id: documentId },
    update: { state: Buffer.from(state), updatedAt: new Date() },
    create: { id: documentId, state: Buffer.from(state) }
  });
}, 5000);
```

---

## Escala

### Sharding por documento (room)

Cada documento é uma "room" — todos os clientes do mesmo documento precisam estar no mesmo servidor para receber broadcasts eficientemente.

```
documentId → hash(documentId) % N_SERVERS → servidor responsável

Se servidor cai → redireciona para outro
Estado recuperado do Redis/DB
```

### Fanout para muitos viewers

Documento com 1000 viewers simultâneos: não conectar todos ao mesmo servidor de edição.

```
Servidor A (editores) → Redis Pub/Sub → Servidores B, C, D (viewers)
```

### Batching de updates no cliente

Digitação rápida gera 10+ updates/segundo. Enviar cada keystroke individualmente satura a rede.

```typescript
const pendingUpdates: Uint8Array[] = [];
ydoc.on("update", update => pendingUpdates.push(update));

setInterval(() => {
  if (pendingUpdates.length > 0) {
    const merged = Y.mergeUpdates(pendingUpdates);
    ws.send(merged);
    pendingUpdates.length = 0;
  }
}, 100); // batch a cada 100ms — máximo 10 envios/segundo
```

---

## Trade-offs

| Aspecto | CRDT | OT |
|---|---|---|
| **Offline** | Nativo — edita sem conexão, sincroniza depois | Limitado — precisa do servidor |
| **Servidor** | Relay simples (não sequencia) | Servidor de sequenciamento obrigatório |
| **Undo/redo colaborativo** | Complexo de implementar | Natural (sequência de operações) |
| **Histórico** | Não preservado nativamente | Preservado como log de operações |
| **Adoção** | Y.js, Automerge, Liveblocks | Google Docs, Etherpad |
| **Memory overhead** | Tombstones de caracteres deletados acumulam | Menor |

**Tombstone problem**: em CRDTs de sequência, caracteres deletados precisam ser mantidos como "tombstones" para garantir convergência. Documentos com muitas edições acumulam tombstones — necessário garbage collection periódico.

---

## Quando Usar / Quando Evitar

**Use CRDT quando:**
- Offline-first é requisito (mobile, PWA)
- Colaboração P2P sem servidor central
- Simplicidade de implementação com Y.js
- Escala sem gargalo de sequenciamento

**Use OT quando:**
- Histórico de operações nomeadas é requisito de produto
- Undo/redo colaborativo preciso (quem desfez o quê)
- Legado baseado em Google Docs API

**Evite colaboração em tempo real quando:**
- Conflitos são raros → optimistic locking é suficiente
- Usuários editam seções distintas → partition por seção resolve sem CRDT

---

## Conceitos Relacionados

[[cap-pacelc-consistencia]] · [[distributed-locks-raft]] · [[mensageria]] · [[cache]] · [[observabilidade]]

---

*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-29*
