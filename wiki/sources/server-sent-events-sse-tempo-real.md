---
type: source
title: "Server-Sent Events (SSE): Comunicação em Tempo Real na Prática"
aliases: ["SSE tempo real", "server-sent events tutorial", "SSE vs WebSocket na prática"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 0
tags: [sse, server-sent-events, websocket, realtime, redis, pub-sub, microsservicos, backend, tempo-real]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/server-sent-events-sse-tempo-real.md
source_url:
author: desconhecido (canal de vídeo, criador se autodenomina "Renato" no texto)
date_published:
date_ingested: 2026-07-03
---

# Server-Sent Events (SSE): Comunicação em Tempo Real na Prática

## TL;DR

Transcrição de vídeo tutorial que ensina SSE (Server-Sent Events) do zero: por que polling e long polling não escalam, como o SSE mantém uma resposta HTTP aberta via `text/event-stream`, como implementar em Node.js/Express, como propagar eventos entre múltiplas instâncias com Redis Pub/Sub, e os erros de produção mais comuns (SSE que na verdade é polling disfarçado, conexão Redis sem Singleton, falta de cleanup ao desconectar, autenticação via query string).

## Key Claims

1. **Polling é HTTP request-response em loop, motivado só pela simplicidade** — `setInterval` + fetch a cada N segundos; funciona para dashboards internos de baixo tráfego mas não escala para muitos usuários (overhead de headers repetidos a cada request).
2. **Long polling seguraw a requisição no servidor até ter dado ou timeout, depois fecha e o cliente reabre** — mais eficiente que polling puro, mas ainda reabre conexão a cada mensagem; considerado obsoleto frente ao SSE para quem não tem restrição de proxy legado.
3. **SSE mantém uma única conexão TCP aberta e nunca finaliza a resposta HTTP** — o servidor escreve continuamente dentro da mesma resposta (`Content-Type: text/event-stream`), criando um "tunelamento" unidirecional servidor→cliente.
4. **O formato SSE exige campos `data:` (obrigatório) e duas quebras de linha para terminar uma mensagem** — uma quebra de linha separa campos dentro da mesma mensagem (ex: `event:` e `data:`); duas quebras de linha sinalizam fim da mensagem para o protocolo.
5. **`EventSource` do browser reconecta automaticamente quando a conexão cai** — é isso que faz um bug comum (fechar a resposta no servidor após escrever) parecer estar funcionando: na verdade gera polling disfarçado, visível como uma sequência de requisições no painel de rede do browser em vez de uma única conexão persistente.
6. **Nomear eventos com o campo `event:` permite múltiplos canais de dados na mesma conexão** — o cliente usa `addEventListener(nomeDoEvento, handler)` em vez de `onmessage` genérico, permitindo rotear diferentes tipos de evento (depósito, saque, log) separadamente.
7. **Redis Pub/Sub funciona como notificador entre microsserviços** — um serviço publica em um canal (`PUBLISH notifications "msg"`) sem precisar criar o canal antecipadamente; qualquer serviço inscrito (`SUBSCRIBE`) recebe a mensagem e a repassa para os clientes SSE conectados.
8. **Sem padrão Singleton na conexão Redis, cada requisição SSE abre uma nova conexão com o Redis** — com 100 usuários simultâneos, seriam 100 conexões Redis abertas, o que pode derrubar o Redis; o Redis usa multiplexação por baixo dos panos e é projetado para reaproveitar uma única conexão entre muitos assinantes.
9. **É obrigatório detectar o fechamento da conexão pelo cliente (`req.on('close')`) e liberar recursos** — sem isso, o servidor continua tentando escrever em conexões mortas (aba fechada, navegador fechado), o que em escala de milhares de usuários gera vazamento de recursos.
10. **SSE não permite enviar headers customizados** — como `EventSource` não aceita headers arbitrários (ex: `Authorization: Bearer <jwt>`), a prática comum é passar o JWT como parâmetro de query string; isso é aceitável porque JWT não foi desenhado para ser secreto, só não deve carregar dados sensíveis.
11. **SSE é unidirecional e só transporta texto** — não aceita binário (vídeo, foto, PDF); para comunicação bidirecional (chat, jogos, colaboração), o WebSocket é a escolha correta apesar de maior complexidade de implementação, gerenciamento de conexões e necessidade de load balancer de camada 4.

## Entidades Mencionadas

- Redis (Pub/Sub, canivete suíço de estruturas de dados)
- Node.js / Express (implementação do back end)
- `EventSource` (API nativa do browser)

## Conceitos Tocados

- [[wiki/concepts/server-sent-events]]
- [[wiki/concepts/websocket-vs-polling]]
- [[wiki/concepts/redis]]
- [[wiki/concepts/pub-sub]]
- [[wiki/concepts/singleton-pattern]]
- [[wiki/concepts/protocolo-de-rede]]
- [[wiki/concepts/mensageria]]
- [[wiki/concepts/graceful-shutdown]]
- [[wiki/concepts/load-balancer]]
- [[wiki/concepts/connection-pooling]]
- [[wiki/concepts/realtime-tracking]]

## Open Questions

- A fonte trata `keep-alive` no header `Connection` como opcional, restrito a arquiteturas legadas em HTTP/1 — não aprofunda a interação com HTTP/2/3, onde multiplexação de streams muda esse comportamento. Ver `references/realtime.md` da skill (`X-Accel-Buffering: no` para desabilitar buffer de proxy, `Last-Event-ID` para replay) para o que a fonte não cobriu.
- A fonte propõe JWT via query string como solução definitiva para auth em SSE, sem mencionar riscos de exposição em logs de acesso/proxy (URLs completas frequentemente vão parar em logs de servidor, APM, browser history) — vale registrar como ponto de atenção adicional, não presente na transcrição original.
- Nenhuma contradição direta com [[wiki/concepts/websocket-vs-polling]], que já cobria a comparação em nível mais superficial — esta fonte aprofunda a implementação prática e os erros de produção que a página anterior não detalhava.

## Raw Quotes

> "Isso aqui é polling, ou seja... ele tá fazendo uma requisição atrás da outra... Isso não é SSE, e eu já vi gente implementar isso aqui, então toma cuidado com isso aqui."

> "O Redis é diferente, você não faz igual o banco de dados que você tem que criar uma tabela para depois enviar dado pra tabela. Só o fato de você publicar uma mensagem em um canal chamado notifications, o próprio Redis já verifica: existe esse canal aqui? Não existe? Então já cria."

> "Se a gente tem 100 usuários ativos agora, significa que a gente tá pendurado no Redis 100 vezes... isso aqui derrubaria o Redis, dependendo do número de usuários."

> "O JWT não foi feito para ser secreto, ele foi feito justamente para trafegar os dados, desde que você não trafegue dados sensíveis."
