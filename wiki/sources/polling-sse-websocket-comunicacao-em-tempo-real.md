---
type: source
title: "Comunicação em tempo real: Polling, SSE e WebSocket"
aliases: ["polling sse websocket rafael", "três formas de comunicação em tempo real", "só vá pro websocket se os outros dois não funcionarem"]
date_created: 2026-11-10
date_updated: 2026-11-10
source_count: 0
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/polling-sse-websocket-comunicacao-em-tempo-real.md"
source_url: ""
author: "Rafael (sobrenome e canal não identificados; nome inferido do próprio vídeo)"
date_published:
date_ingested: 2026-11-10
tags: [realtime, polling, sse, websocket, http, chat, llm-streaming, serverless, trade-off, backend, networking]
skill: tech-mentor-backend
status: draft
---

# Comunicação em tempo real: Polling, SSE e WebSocket

**Formato:** transcrição de vídeo do YouTube (legenda automática, PT-BR), limpa sem alteração de conteúdo. Vídeo introdutório, sem código, apoiado em diagramas que a transcrição não mostra.

## TL;DR

O [[wiki/concepts/requisicao-http|HTTP]] só responde quando o cliente pergunta, então o servidor não tem como avisar o cliente por conta própria. O autor apresenta três saídas, da mais simples à mais poderosa: **polling** (o cliente pergunta de tempos em tempos, com um token de "última alteração"), **[[wiki/concepts/server-sent-events|SSE]]** (uma resposta HTTP que fica aberta e na qual só o servidor escreve) e **WebSocket** (handshake HTTP e depois uma conexão full-duplex). A conclusão é uma regra de escalada: só vá para o WebSocket se polling e SSE não resolverem, porque não existe resposta certa fora do [[wiki/concepts/tradeoff-arquitetural|trade-off]] do seu problema. Ver o hub [[wiki/concepts/websocket-vs-polling]].

## Key Claims

1. **HTTP é request/response: sem gatilho do cliente, não há comunicação.** O servidor não tem mecanismo para iniciar a conversa, e por isso surgiram as "gambiarras" e soluções mais robustas. Evidência: descrição do protocolo (método, caminho, versão, cabeçalho, corpo; resposta `200`). Confiança: alta. Ver [[wiki/concepts/requisicao-http]] e [[wiki/concepts/arquitetura-cliente-servidor]].
2. **Polling usa um token de cursor.** O servidor devolve um valor (por exemplo, o timestamp da última alteração), e o cliente o reenvia a cada pergunta para receber só o que veio depois. Na prática é um `setInterval`. Evidência: explicação do autor. Confiança: alta; é o mesmo cursor que [[wiki/concepts/chat-distribuido]] descreve como alternativa à tabela de pendentes. A fonte não fala de long polling.
3. **O custo do polling é desperdício: 1000 clientes a cada 2 s dão cerca de 500 req/s, quase todas "não mudou nada".** Para dados que mudam pouco, como status de atividade, um intervalo de 30 s a 1 min basta. O polling é fácil de implementar e de depurar e não tem dependências. Evidência: aritmética correta (1000 ÷ 2). Confiança: alta. Ver [[wiki/concepts/presenca-online]].
4. **SSE mantém aberta a conexão do primeiro GET, e daí em diante só o servidor escreve.** A resposta tem tipo `text/event-stream` e é mão única. Evidência: MDN, "This is a one-way connection" ([external](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)). Confiança: alta. O autor diz que SSE "não é nativo do HTTP" e nasceu do event stream do JavaScript. É impreciso: a API `EventSource` é do padrão HTML, mas o transporte é HTTP comum.
5. **SSE não precisa de handshake nem de protocolo novo, reconecta sozinho e funciona atrás de CDN, load balancer e proxy reverso.** Evidência: a reconexão automática confere com a MDN ("the connection is restarted", com campo `retry:` e `id:`). Confiança: alta para a reconexão. Para a infraestrutura a confiança é média: a skill alerta que proxies que fazem buffer (nginx) exigem `X-Accel-Buffering: no` `[skill: tech-mentor-backend]`, e sem HTTP/2 há o limite de 6 conexões por navegador e domínio ([external](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)). "Sem handshake" quer dizer sem *upgrade*: o handshake TCP/TLS continua. Ver [[wiki/concepts/reverse-proxy]], [[wiki/concepts/cdn]] e [[wiki/concepts/load-balancer]].
6. **O streaming do ChatGPT, palavra por palavra, "é SSE puro".** Evidência: a OpenAI documenta o streaming da API como "HTTP streaming (`stream=true`) over server-sent events (SSE)" e também oferece um modo WebSocket ([external](https://developers.openai.com/api/docs/guides/streaming-responses)). Confiança: alta para a API. A interface web do ChatGPT não foi conferida. Ver [[wiki/entities/openai]].
7. **SSE serve para dashboards e mapas ao vivo, como o rastreamento de um caminhão por GPS.** Evidência: exemplo do autor. Confiança: alta para o lado de quem só assiste. O lado de quem envia a posição (o motorista) ainda precisa de outro canal; ver [[wiki/concepts/realtime-tracking]], em que o case Uber usa WebSocket.
8. **WebSocket usa o HTTP só como handshake e depois abre uma conexão duplex.** Evidência: RFC 6455, "an HTTP Upgrade request" com resposta `101 Switching Protocols`, e "each side can, independently from the other, send data at will" ([external](https://datatracker.ietf.org/doc/html/rfc6455)). Confiança: alta.
9. **O caso típico é o chat com indicador de "digitando", em que os dois lados enviam ao mesmo tempo.** O modelo é de eventos: o cliente reage a mensagem, notificação e reação recebidas, e o servidor a mensagem, notificação e reação enviadas. Evidência: exemplo do autor. Confiança: alta. Ver [[wiki/concepts/chat-distribuido]].
10. **WebSocket não é [[wiki/concepts/sem-balas-de-prata|bala de prata]]: é preciso gerenciar desconexão e perda de mensagem, e nem toda aplicação comporta, como as serverless.** Evidência: a dificuldade de gerenciar conexões confere com a skill (heartbeat, backoff, close codes) `[skill: tech-mentor-backend]`. Confiança: média para a parte de serverless. Uma função como [[wiki/concepts/aws-lambda]] não segura conexão, mas o API Gateway oferece WebSocket APIs "bidirectional" integradas a Lambda ([external](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html)). É possível com uma camada gerenciada, não "impossível".
11. **Comparativo do autor:** polling é simples, mas desperdiça; SSE só se comunica quando há mudança, é HTTP puro, leve e reconecta sozinho, mas é unidirecional; WebSocket é full-duplex, tem protocolo dedicado e baixa latência, mas é mais complexo e pede infra mais resiliente. Confiança: alta; bate com a tabela da skill `[skill: tech-mentor-backend]`.
12. **Combinar SSE com outro canal para ter ida e volta "não tem muito porquê".** Evidência: opinião. Confiança: baixa. O próprio exemplo do ChatGPT (claim 6) é a combinação de uma requisição comum de ida com uma resposta SSE de volta, padrão comum em chats com LLM. Ver Open Questions.
13. **Regra final: só vá para o WebSocket se os outros dois não funcionarem; a resposta certa depende de quais problemas você aceita.** Evidência: argumento. Confiança: alta como heurística e coerente com [[wiki/sources/updates-tempo-real-polling-sse-websocket]] ("polling não é escolha inferior"). Ver [[wiki/concepts/tradeoff-arquitetural]].

> "Só vai pro WebSocket se os outros dois não funcionarem." (Rafael)

## Entidades

- Autor: Rafael, nome inferido de duas falas em que ele se dirige a si mesmo ("Ué, Rafael"). Sobrenome, canal e blog não identificados; sem página própria.
- [[wiki/entities/openai]]: ChatGPT como exemplo de SSE.
- Sem página própria: YouTube, usado numa analogia de "conexão" com o inscrito.

## Conceitos

- [[wiki/concepts/websocket-vs-polling]]: hub das três técnicas.
- [[wiki/concepts/server-sent-events]]
- [[wiki/concepts/requisicao-http]]
- [[wiki/concepts/chat-distribuido]]
- [[wiki/concepts/realtime-tracking]]
- [[wiki/concepts/presenca-online]]
- [[wiki/concepts/notification-system]]: notificação e feed como casos de SSE.
- [[wiki/concepts/sem-balas-de-prata]]
- [[wiki/concepts/tradeoff-arquitetural]]
- [[wiki/concepts/reverse-proxy]], [[wiki/concepts/cdn]], [[wiki/concepts/load-balancer]]: infraestrutura em que o SSE "só funciona".
- [[wiki/concepts/aws-lambda]]: o limite do serverless.

## Relação com fontes anteriores

- [[wiki/sources/updates-tempo-real-polling-sse-websocket]] cobre o mesmo trio com profundidade de entrevista (LB L4, Redis Pub/Sub, usuário offline). Esta fonte é mais introdutória e não trata de escala horizontal.
- [[wiki/sources/server-sent-events-sse-tempo-real]] e [[wiki/sources/websocket-sse-realtime]] detalham a implementação do SSE (formato `data:`, `Last-Event-ID`), que aqui não aparece.
- **Tensão:** o claim 5 (SSE "funciona atrás de load balancer") e a afirmação da fonte de entrevista de que WebSocket exige LB de camada 4 se referem a protocolos diferentes, então não se contradizem diretamente. A skill, porém, faz proxy de WebSocket no nginx (camada 7) com `Upgrade` `[skill: tech-mentor-backend]`, o que já relativiza a regra "nunca camada 7" registrada em [[wiki/concepts/websocket-vs-polling]].

## Open Questions

- A fonte não fala de long polling nem do limite de 6 conexões do SSE em HTTP/1.1, dois pontos que pesam na escolha entre polling e SSE.
- Qual é a arquitetura preferível para chat com LLM: requisição comum de ida com SSE de volta (o padrão da OpenAI) ou WebSocket? O autor descarta a primeira sem argumento.
- Trechos ambíguos da transcrição (ver log) não mudam os claims técnicos.
