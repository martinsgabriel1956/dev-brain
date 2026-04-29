---
date: 2026-04-17
tags: [tech-mentor, system-design, realtime, presenca, websocket, redis]
skill: tech-mentor-system-design/references/design-cases
level: avançado
---

# Presence System — Online/Offline em Tempo Real

## Contexto
Sistemas de presença indicam se um usuário está online/offline (e às vezes "digitando", "em call", "ausente"). Aparecem em: Slack, WhatsApp, Discord, colaboração em tempo real. O desafio é escalar para milhões de usuários mantendo latência baixa e não sobrecarregar o banco.

## Arquitetura

```
Client ──WebSocket──► Node A ──PUBLISH──► Redis Pub/Sub
                                                │
                                    ─────────────────────
                                    │           │        │
                              Node B        Node C    Node D
                                │
                           Client B (vê Alice online)
```

A presença é **efêmera** — não precisa de persistência durável. Redis é ideal: TTL nativo, pub/sub para broadcast, baixíssima latência.

## Heartbeat com TTL

```typescript
const PRESENCE_TTL = 30; // segundos
const HEARTBEAT_INTERVAL = 15_000; // 15s

// No WebSocket server
class PresenceService {
  async userConnected(userId: string, connectionId: string) {
    // Marcar online com TTL
    await redis.setEx(`presence:${userId}`, PRESENCE_TTL, JSON.stringify({
      status: "online",
      connectionId,
      lastSeen: new Date().toISOString()
    }));

    // Notificar contatos via Pub/Sub
    await redis.publish("presence:updates", JSON.stringify({
      userId, status: "online"
    }));
  }

  async userDisconnected(userId: string) {
    await redis.del(`presence:${userId}`);
    await redis.publish("presence:updates", JSON.stringify({
      userId, status: "offline"
    }));
  }

  // Heartbeat — cliente envia a cada 15s, servidor renova TTL
  async heartbeat(userId: string) {
    const exists = await redis.expire(`presence:${userId}`, PRESENCE_TTL);
    if (!exists) {
      // TTL expirou antes do heartbeat — usuário reconectou sem desconectar
      await this.userConnected(userId, `conn-${Date.now()}`);
    }
  }

  async isOnline(userId: string): Promise<boolean> {
    return (await redis.exists(`presence:${userId}`)) === 1;
  }

  async getBulkPresence(userIds: string[]): Promise<Map<string, boolean>> {
    // Pipeline para evitar N round-trips
    const pipeline = redis.pipeline();
    userIds.forEach(id => pipeline.exists(`presence:${id}`));
    const results = await pipeline.exec();

    return new Map(
      userIds.map((id, i) => [id, results[i] === 1])
    );
  }
}
```

## Client — Heartbeat e Reconexão

```typescript
class PresenceClient {
  private ws: WebSocket;
  private heartbeatTimer: ReturnType<typeof setInterval> | null = null;

  connect(url: string, token: string) {
    this.ws = new WebSocket(`${url}?token=${token}`);

    this.ws.onopen = () => {
      this.startHeartbeat();
    };

    this.ws.onclose = () => {
      this.stopHeartbeat();
      setTimeout(() => this.connect(url, token), 3000); // reconexão automática
    };
  }

  private startHeartbeat() {
    this.heartbeatTimer = setInterval(() => {
      if (this.ws.readyState === WebSocket.OPEN) {
        this.ws.send(JSON.stringify({ type: "heartbeat" }));
      }
    }, 15_000);
  }

  private stopHeartbeat() {
    if (this.heartbeatTimer) clearInterval(this.heartbeatTimer);
  }
}
```

## Escalando para Múltiplos Nodes

```typescript
// Cada node subscreve ao canal de atualizações de presença
const subscriber = redis.duplicate();
await subscriber.subscribe("presence:updates");

subscriber.on("message", (_, message) => {
  const update = JSON.parse(message);
  // Notificar todos os clients conectados NESTE node que acompanham userId
  const watchers = presenceWatchers.get(update.userId) ?? [];
  for (const ws of watchers) {
    ws.send(JSON.stringify(update));
  }
});
```

## Presence em Escala — Desafios

| Desafio | Solução |
|---|---|
| Desconexão sem evento (rede caiu) | TTL no Redis — expira automaticamente após 30s sem heartbeat |
| Múltiplas abas abertas | Contagem de conexões — só offline quando count = 0 |
| Escala de leitura | Cache local por N segundos — não consultar Redis por request |
| "Typing" indicator | Evento separado com TTL de 3s — não persistido |
| Privacidade | Filtro por amizade/sala antes de expor presença |

## Typing Indicator

```typescript
// "Fulano está digitando..." — evento efêmero, sem persistência
async function startTyping(userId: string, roomId: string) {
  const key = `typing:${roomId}:${userId}`;
  await redis.setEx(key, 3, "1"); // expira em 3s automaticamente

  await redis.publish(`room:${roomId}:events`, JSON.stringify({
    type: "typing.start", userId
  }));
}

// Client para de digitar → ação explícita OU TTL expira → parou de digitar
async function stopTyping(userId: string, roomId: string) {
  await redis.del(`typing:${roomId}:${userId}`);
  await redis.publish(`room:${roomId}:events`, JSON.stringify({
    type: "typing.stop", userId
  }));
}
```

## Conceitos Relacionados
[[websocket-sse-realtime]] · [[redis-avancado]] · [[notification-system]] · [[crdt-colaboracao-tempo-real]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
