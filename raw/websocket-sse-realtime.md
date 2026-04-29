---
date: 2026-04-17
tags: [tech-mentor, apis, websocket, sse, realtime, backend]
skill: tech-mentor-backend/references/apis
level: avançado
---

# WebSocket Avançado e SSE

## WebSocket Avançado

### Arquitetura em Cluster

O problema central: WebSocket é stateful — a conexão persiste em um processo específico. Quando há múltiplos nodes, uma mensagem publicada no Node A precisa chegar aos clients conectados no Node B.

```
Client 1 ──WebSocket──► Node A
Client 2 ──WebSocket──► Node B

Node A publica evento → como Client 2 recebe?

Solução: Redis Pub/Sub como bus entre nodes

Node A ──PUBLISH "channel:user:456"──► Redis
                                           │
                                           └──► Node B (SUBSCRIBE) ──► Client 2
```

```typescript
import { Server } from "socket.io";
import { createAdapter } from "@socket.io/redis-adapter";
import { createClient } from "redis";

const pubClient = createClient({ url: process.env.REDIS_URL });
const subClient = pubClient.duplicate();

await Promise.all([pubClient.connect(), subClient.connect()]);

const io = new Server(httpServer, {
  adapter: createAdapter(pubClient, subClient)
});

// Agora io.to("room:123").emit() funciona mesmo com múltiplos nodes
io.on("connection", socket => {
  socket.on("join-order", (orderId: string) => {
    socket.join(`order:${orderId}`);
  });
});

// Em qualquer node: entrega para todos os clients na sala
io.to(`order:${orderId}`).emit("order-updated", { status: "shipped" });
```

### Backpressure e bufferedAmount

Quando o client não consome mensagens na velocidade de envio, o buffer cresce. Monitorar `bufferedAmount` evita OOM no servidor.

```typescript
function safeSend(ws: WebSocket, data: unknown) {
  const MAX_BUFFER = 1024 * 1024; // 1MB

  if (ws.bufferedAmount > MAX_BUFFER) {
    // Client está lento — aplicar backpressure
    console.log({ message: "WebSocket buffer full, dropping message", buffered: ws.bufferedAmount });
    return;
  }

  ws.send(JSON.stringify(data));
}
```

### Heartbeat e Reconexão

```typescript
// Server: detecta conexões mortas (sem ping/pong = cliente desapareceu sem fechar)
const clients = new Map<WebSocket, { isAlive: boolean }>();

wss.on("connection", ws => {
  clients.set(ws, { isAlive: true });

  ws.on("pong", () => {
    clients.get(ws)!.isAlive = true;
  });
});

// Intervalo de heartbeat
setInterval(() => {
  for (const [ws, state] of clients) {
    if (!state.isAlive) {
      clients.delete(ws);
      ws.terminate(); // conexão zumbi — mata
      return;
    }
    state.isAlive = false;
    ws.ping();
  }
}, 30_000);

// Client: reconexão com backoff exponencial
class ReconnectingWebSocket {
  private ws: WebSocket | null = null;
  private retryDelay = 1000;

  connect(url: string) {
    this.ws = new WebSocket(url);

    this.ws.onopen = () => {
      this.retryDelay = 1000; // reset após sucesso
    };

    this.ws.onclose = () => {
      setTimeout(() => this.connect(url), this.retryDelay);
      this.retryDelay = Math.min(this.retryDelay * 2, 30_000); // max 30s
    };
  }
}
```

---

## SSE — Server-Sent Events

### Quando usar SSE vs. WebSocket

| Critério | SSE | WebSocket |
|---|---|---|
| Direção | Unidirecional (server → client) | Bidirecional |
| Protocolo | HTTP/1.1 ou HTTP/2 | Upgrade para WS |
| Reconexão | Automática pelo browser | Manual |
| Proxy/CDN | Funciona transparentemente | Pode precisar de config |
| Complexidade | Mínima | Maior |
| Uso típico | Live feed, notificações, progress | Chat, jogos, colaboração |

```typescript
// Server — SSE endpoint
app.get("/events/orders/:orderId", (req, res) => {
  const { orderId } = req.params;

  res.setHeader("Content-Type", "text/event-stream");
  res.setHeader("Cache-Control", "no-cache");
  res.setHeader("Connection", "keep-alive");
  res.setHeader("X-Accel-Buffering", "no"); // desabilita buffer do Nginx

  // Envia comentário para manter conexão viva
  const keepAlive = setInterval(() => res.write(": ping\n\n"), 15_000);

  // Last-Event-ID — permite ao cliente retomar de onde parou
  const lastEventId = req.headers["last-event-id"] as string | undefined;
  if (lastEventId) {
    // Recuperar eventos perdidos desde lastEventId
    const missedEvents = getMissedEvents(orderId, lastEventId);
    for (const event of missedEvents) {
      sendEvent(res, event);
    }
  }

  // Subscreve para atualizações do pedido
  const unsubscribe = eventEmitter.on(`order:${orderId}`, event => {
    sendEvent(res, event);
  });

  req.on("close", () => {
    clearInterval(keepAlive);
    unsubscribe();
  });
});

function sendEvent(res: Response, event: { id: string; type: string; data: unknown }) {
  res.write(`id: ${event.id}\n`);
  res.write(`event: ${event.type}\n`);
  res.write(`data: ${JSON.stringify(event.data)}\n\n`);
}
```

```javascript
// Client — EventSource com Last-Event-ID automático
const source = new EventSource(`/events/orders/${orderId}`);

source.addEventListener("order-updated", event => {
  const order = JSON.parse(event.data);
  updateUI(order);
});

// browser envia automaticamente Last-Event-ID no reconnect
source.onerror = () => {
  // EventSource reconecta automaticamente — não precisamos fazer nada
};
```

## Conceitos Relacionados
[[rest-openapi]] · [[api-gateway-bff]] · [[rate-limiting]] · [[redis-avancado]] · [[graceful-degradation]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
