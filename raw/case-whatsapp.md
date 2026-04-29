---
date: 2026-03-29
tags: [tech-mentor, system-design, cases, whatsapp, websocket, mensagens, presença]
skill: tech-mentor-system-design/references/system-design-cases
level: arquiteto
---

# Case: WhatsApp

## Contexto

Chat em tempo real é um dos problemas de system design que expõe mais claramente os limites de arquiteturas stateless. O servidor precisa manter estado de conexão (WebSocket) por usuário, o que torna escala horizontal não trivial. Além disso, garantir entrega de mensagens com semântica de ACK triplo (enviado, entregue, lido) exige protocolo cuidadoso.

---

## Requisitos

**Funcionais:**
- Mensagens 1:1 e grupos (até 256 participantes)
- Status de entrega: enviado ✓, entregue ✓✓, lido ✓✓ (azul)
- Usuário offline recebe mensagens ao voltar online
- Histórico de mensagens
- Indicador de presença (online/offline/último acesso)

**Não-funcionais (escala real):**
```
2B usuários registrados
1B DAU
100B mensagens/dia = ~1.15M mensagens/segundo
48GB/s de mídia uploaded
Latência de entrega: < 100ms p99 (usuários online)
```

---

## Protocolo de Conexão

### WebSocket — Por que não HTTP polling?

```
HTTP Polling (client pergunta a cada Ns):
  Client: "tem mensagem nova?" → Server: "não"
  Client: "tem mensagem nova?" → Server: "não"
  Client: "tem mensagem nova?" → Server: "sim, aqui está"
  Problema: latência = intervalo de polling. 1s de intervalo = 1s de delay.

Long Polling:
  Client abre request → Server segura até ter mensagem ou timeout
  Melhor latência, mas overhead de HTTP por mensagem permanece.

WebSocket:
  Handshake HTTP → upgrade para WS → conexão bidirecional persistente
  Server empurra mensagem ao client em tempo real, sem overhead HTTP
  ✅ Latência mínima (dezenas de ms)
  ✅ Full-duplex: client e server enviam a qualquer momento
  ✅ Um único socket por usuário (vs múltiplas conexões HTTP)
```

---

## O Problema do Chat Distribuído

Usuário A e usuário B podem estar conectados em **chat servers diferentes**. Chat server é stateful — ele conhece quais WebSockets estão abertos. Como A envia mensagem para B se os dois estão em servidores diferentes?

```
Sem broker:
  Chat Server 1 (usuário A)  ←?→  Chat Server 2 (usuário B)
  Não há comunicação direta — cada server só conhece suas conexões

Com Message Broker (Redis Pub-Sub ou Kafka):
  Chat Server 1 (A) → publica no topic user:{B_id}
  Chat Server 2 (B) → subscreveu no topic user:{B_id} → recebe → envia via WS para B
```

Redis Pub-Sub funciona para mensagens diretas. Para grupos com 256 membros: topic por grupo, todos os servers que têm membros do grupo subscrevem.

---

## Garantia de Entrega — ACK Triplo

```
[1] Usuário A envia mensagem
    → Client gera: client_message_id (UUID local, temporário)
    → Envia via WS para Chat Server

[2] Chat Server persiste no DB
    → Gera: server_message_id (Snowflake ID — ordenado)
    → Retorna ACK para A: { client_id, server_id } → ✓ Enviado (tick cinza)

[3] Chat Server entrega para B
    → B online: envia via WS diretamente
    → B offline: mensagem fica no DB (fila de pendentes)
                 Push notification via FCM/APNs para acordar o app

[4] B recebe → envia ACK de entrega → ✓✓ Entregue (dois ticks cinzas)

[5] B abre a conversa → lê → envia ACK de leitura → ✓✓ Lido (dois ticks azuis)
```

**Por que client_message_id?**
Se a conexão WS cair entre o envio e o ACK do server, o client reenvia a mensagem. O server usa `client_message_id` como chave de idempotência — evita duplicatas no DB.

---

## Presença (Online/Offline)

Presença é um dos problemas mais caros de escala em chat: toda mudança de status precisa ser propagada para todos os contatos do usuário.

```
[Detectar online/offline]
  WebSocket conectado → usuário online
  Heartbeat do client a cada 10s → Chat Server atualiza Redis
    key: presence:{user_id}
    value: { status: "online", server_id: "chat-3", last_seen: timestamp }
    TTL: 30s
  Ausência de heartbeat → TTL expira → usuário considerado offline

[Propagar status]
  Ao conectar/desconectar: Chat Server publica evento no Kafka
    topic: presence.updates
    payload: { user_id, status, timestamp }

  Presence Service consume o topic
    → Para cada contato do usuário: notifica via WS se estiver online
    → Atualiza last_seen no DB (PostgreSQL)
```

**O problema de escala de presença:**
Se um usuário tem 500 contatos e todos precisam ser notificados de cada mudança, com 1B DAU conectando/desconectando constantemente, o volume de propagação explode.

**Solução pragmática**: propagar presença apenas para contatos que estão **ativamente na tela de conversa** com o usuário. Demais contatos recebem `last_seen` no próximo acesso — sem propagação em tempo real.

---

## Storage de Mensagens

### Por que Cassandra?

```
Padrão de acesso:
  ✅ Escrita intensa: 1.15M mensagens/segundo — quase sempre INSERT
  ✅ Leitura por conversa: buscar últimas N mensagens entre dois usuários
  ✅ TTL nativo por célula: apagar mensagens após 30 dias (delivery expirada)
  ✅ Horizontal scale linear: adicionar nós aumenta capacidade proporcionalmente
  ✅ Replicação multi-datacenter nativa
  ❌ Não suporta joins — mas chat não precisa de join
  ❌ Eventual consistency — tolerável para chat (ordem por Snowflake ID)
```

```
Schema (simplificado):

Tabela: messages
  partition key: conversation_id       → mensagens da mesma conversa no mesmo nó
  clustering key: message_id DESC      → Snowflake ID ordena cronologicamente
  columns: sender_id, content, type, status, created_at

Tabela: user_conversations
  partition key: user_id
  clustering key: last_message_at DESC → lista de conversas do usuário, mais recentes primeiro
```

### Delivery queue (mensagens offline)

```
Tabela: pending_messages
  partition key: recipient_id
  clustering key: message_id
  TTL: 30 dias (mensagem expira se usuário não voltar)

Ao usuário conectar:
  → Busca todas as mensagens pending para seu user_id
  → Entrega em ordem (clustering key = Snowflake ID = cronológico)
  → Remove da fila após ACK de entrega
```

---

## Mídia

```
Envio de mídia:
  1. Client solicita presigned URL ao backend
  2. Upload direto para S3 (não passa pelo Chat Server)
  3. Backend retorna CDN URL da mídia
  4. Mensagem enviada com { type: "image", media_url: "cdn.whatsapp.com/..." }

Armazenamento:
  S3 para persistência (origin)
  CloudFront para serving (CDN)
  TTL: 1 ano (após expirar, URL quebra — re-upload necessário se compartilhado novamente)

Escala:
  48GB/s de upload = ~4PB/dia
  Compressão no client antes do upload: WhatsApp comprime imagens para max 1600px
```

---

## Arquitetura Completa

```
[Envio de mensagem]
Client A → WebSocket → Chat Server N
  → Persiste em Cassandra (messages)
  → ACK ✓ para A
  → Redis Pub-Sub: publica em channel:{B_id}
        ↓
  Chat Server M (B está conectado) → recebe do Pub-Sub → envia via WS para B
        ↓
  B recebe → ACK ✓✓ entregue → Chat Server M → publica ACK no Kafka
        ↓
  Chat Server N (A está conectado) → recebe ACK → envia WS para A → ✓✓

[Usuário B offline]
  Chat Server → insere em pending_messages (Cassandra, TTL 30 dias)
  → Push notification via FCM/APNs → app acorda
  → App abre WS → flush de pending_messages → ACKs

[Presença]
  Heartbeat → Redis TTL refresh
  Connect/disconnect → Kafka topic presence.updates → Presence Service
  → Notifica contatos ativos na conversa
```

---

## Trade-offs

| Decisão | Escolha | Por quê |
|---|---|---|
| Protocolo | WebSocket | Full-duplex, baixa latência, 1 conexão por usuário |
| Comunicação cross-server | Redis Pub-Sub | Baixa latência para mensagens diretas |
| Storage | Cassandra | Escrita intensa, TTL nativo, scale linear |
| Ordenação | Snowflake ID | Cronológico sem coordenação central |
| Presença real-time | Apenas para contatos ativos na tela | Escala: propagar para todos é inviável |
| Idempotência | client_message_id | Evita duplicata em reconexão |

---

## Problemas a Aprofundar em Entrevista

**"Como funciona criptografia end-to-end?"**
Signal Protocol: cada mensagem criptografada com chave derivada do par de chaves do sender e receiver. O servidor nunca tem a chave privada — não consegue ler o conteúdo. ACKs de entrega e leitura são metadados, não conteúdo.

**"Grupos com 256 membros — fan-out ou fan-in?"**
Fan-out on write: ao receber a mensagem do sender, Chat Server replica para cada membro do grupo (via Pub-Sub para os servers onde cada membro está conectado). Para grupos grandes, Kafka com topic por grupo é mais escalável que Redis Pub-Sub.

**"O que acontece se o Chat Server cai?"**
Conexões WS caem. Clients reconectam em outro Chat Server (load balancer distribui). Mensagens pendentes estão no Cassandra — o novo server entrega na reconexão. Mensagens em trânsito (publicadas no Redis e não consumidas) podem ser perdidas → Kafka com persistent log resolve.

---

## Conceitos Relacionados

[[mensageria]] · [[cache]] · [[banco-de-dados]] · [[distributed-tracing]] · [[circuit-breaker]] · [[horizontal-vs-vertical-scaling]]

---

*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-29*
