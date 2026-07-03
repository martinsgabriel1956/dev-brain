---
type: concept
title: "Server-Sent Events (SSE)"
aliases: ["sse", "event stream", "text/event-stream"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 2
tags: [sse, realtime, http, redis, backend, tempo-real]
skill: tech-mentor-backend
status: stable
---

# Server-Sent Events (SSE)

Comunicação **unidirecional servidor→cliente** sobre uma única conexão HTTP mantida aberta indefinidamente. O servidor nunca finaliza a resposta — escreve novos eventos dentro dela conforme acontecem. Ver comparação com [[wiki/concepts/websocket-vs-polling]] para quando escolher SSE em vez de WebSocket.

## Como funciona por baixo dos panos

```
1. Cliente abre new EventSource('/stream')
   → header Accept: text/event-stream
2. Servidor abre conexão TCP, responde com:
   Content-Type: text/event-stream
   Connection: keep-alive        (só relevante em HTTP/1 legado)
3. Servidor NUNCA fecha a resposta — escreve dentro dela continuamente
4. Cliente recebe cada `write()` como um novo evento
```

O protocolo roda inteiramente sobre [[wiki/concepts/protocolo-de-rede|TCP/HTTP]] — não há upgrade de protocolo como no WebSocket.

## Formato obrigatório da mensagem

```
data: <payload>\n\n
```

- `data:` é obrigatório em toda mensagem.
- Uma quebra de linha (`\n`) separa campos dentro da mesma mensagem.
- Duas quebras de linha (`\n\n`) terminam a mensagem — sem isso o protocolo não sabe onde uma mensagem acaba e outra começa.

### Eventos nomeados

```
event: deposito\n
data: {"valor": 100}\n\n
```

Cliente:
```javascript
const es = new EventSource('/stream')
es.addEventListener('deposito', (e) => handle(JSON.parse(e.data)))
```

Sem `event:`, usa-se `onmessage` genérico — funciona, mas não escala para sistemas com múltiplos tipos de evento (log, transação, notificação).

## O erro mais comum: polling disfarçado de SSE

Se o servidor escreve uma vez e **finaliza a resposta**, o `EventSource` do browser reconecta automaticamente (comportamento nativo do protocolo) — criando a ilusão de tempo real quando na verdade é uma sequência de requisições HTTP completas, visível no painel de rede do browser como requisições repetidas com status 200. A correção: nunca finalizar a resposta; usar `setInterval`/callback de evento para escrever dentro da mesma resposta continuamente.

## Gerenciamento de conexão obrigatório

```javascript
req.on('close', () => {
  // cliente fechou aba/navegador — parar de escrever, liberar recursos
})
```

Sem isso, o servidor tenta escrever em conexões mortas indefinidamente — problema de escala com milhares de usuários abrindo/fechando abas. Ver [[wiki/concepts/graceful-shutdown]] para o princípio geral de liberar recursos externos ao encerrar um fluxo.

## Escalando com Redis Pub/Sub

Para propagar eventos de múltiplos microsserviços para clientes SSE conectados a instâncias diferentes:

```
Serviço A → Redis PUBLISH notifications "evento X"
Back end (endpoint SSE) → Redis SUBSCRIBE notifications
  → a cada mensagem recebida do Redis, escreve no response HTTP do cliente
```

**Armadilha**: abrir uma conexão Redis nova a cada requisição SSE que chega derruba o Redis em escala (100 usuários = 100 conexões). Solução: [[wiki/concepts/singleton-pattern]] — uma única conexão Redis reutilizada para todos os assinantes, aproveitando a multiplexação nativa do [[wiki/concepts/redis]]. Ver também [[wiki/concepts/pub-sub]] para o padrão geral e [[wiki/concepts/mensageria]] para onde o Redis Pub/Sub se encaixa frente a Kafka/SQS/RabbitMQ (sem persistência, sem replay — só broadcast efêmero).

## Autenticação

`EventSource` não permite enviar headers customizados (sem `Authorization: Bearer <jwt>`). Solução prática: passar o JWT via query string (`/stream?jwt=...`). Aceitável porque JWT não foi desenhado para ser secreto — só não deve carregar dados sensíveis no payload. Atenção (não coberto pela fonte original): query strings completas tendem a aparecer em logs de acesso, proxies e histórico do browser — um ponto de risco adicional a considerar em produção.

## Vantagens e desvantagens

| ✅ | ❌ |
|---|---|
| Simples de implementar e escalar | Unidirecional — só servidor→cliente |
| Baixo overhead (uma única conexão) | Só texto — sem binário (vídeo, foto, PDF) |
| Reconexão automática nativa do browser | — |
| Baixa latência (sem round-trip por mensagem) | — |

## Quando usar SSE vs WebSocket

- **SSE**: notificações, feeds, dashboards, LLM streaming — cliente só recebe.
- **WebSocket**: chat, jogos, colaboração — cliente também precisa enviar dados com baixa latência.

## Key Sources

- [[wiki/sources/server-sent-events-sse-tempo-real]]
- [[wiki/sources/updates-tempo-real-polling-sse-websocket]] — mesmo mecanismo de Redis Pub/Sub usado para WebSocket também propaga eventos SSE entre instâncias diferentes
