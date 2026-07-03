---
type: source
title: "Updates em Tempo Real: Polling, SSE e WebSocket na Entrevista"
aliases: ["real-time updates system design", "polling vs sse vs websocket entrevista", "load balancer L4 websocket"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 0
tags: [realtime, polling, long-polling, sse, websocket, load-balancer, redis, pub-sub, system-design, entrevista, backend]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/updates-tempo-real-polling-sse-websocket.md
source_url:
author: Pedro Camaforte
date_published:
date_ingested: 2026-07-03
---

# Updates em Tempo Real: Polling, SSE e WebSocket na Entrevista

## TL;DR

Quarto vídeo de uma série de system design para entrevistas: percorre as três estratégias de real-time (polling, SSE, WebSocket) do ângulo "o que o entrevistador quer ouvir além do óbvio" — quando polling simples é a resposta certa, por que WebSocket exige load balancer de camada 4 (não camada 7), como servidores WebSocket se comunicam entre si via Redis Pub/Sub por tópico de usuário/grupo, e como tratar usuários offline com uma tabela de mensagens pendentes.

## Key Claims

1. **Polling é a resposta certa quando a demanda é baixa e a tolerância a delay é alta** — sistemas de notificação/relatório com poucos usuários simultâneos não justificam infraestrutura de WebSocket; citar isso na entrevista (em vez de saltar direto para soluções complexas) demonstra senioridade, não falta de conhecimento.
2. **Long polling é uma ponte entre polling e SSE, mas não escala para o caso geral** — o servidor segura a conexão até ter dado ou até um timeout (20-30s) em vez de responder instantaneamente; mais preciso que polling puro, mas ainda reabre conexão a cada ciclo, motivo pelo qual a maioria das empresas migra para SSE quando precisa de precisão real.
3. **WebSocket exige load balancer de camada 4 (L4/TCP), nunca de camada 7 (L7/HTTP)** — um LB L7 abre a requisição, lê os cabeçalhos, empacota de novo e refaz a chamada ao servidor, o que quebra o fluxo contínuo que o WebSocket precisa manter; o LB L4 apenas redireciona bytes para o servidor com menos conexões abertas, sem inspecionar o conteúdo.
4. **Um único servidor de 16 cores / 32GB RAM comporta ~300-500 mil conexões WebSocket simultâneas** (estimativa com mensagens de ~1KB e ~100 mil mensagens/segundo agregadas) — a escala real (ex: WhatsApp) exige replicação horizontal de servidores atrás do LB L4.
5. **Servidores WebSocket replicados não se enxergam entre si — a comunicação exige um broker externo** — se o usuário A cai no servidor 1 e o usuário B no servidor 4, nenhum dos dois sabe do outro sem um mecanismo central; a fonte cita Redis Pub/Sub como a estratégia mais comum por simplicidade (alternativas: Raft, Kafka).
6. **Redis Pub/Sub para chat usa um tópico por usuário (`user:<id>`), não um tópico global** — cada usuário se inscreve no tópico com seu próprio ID ao conectar; para mandar uma mensagem, o remetente publica no tópico do destinatário (não no próprio); o mesmo padrão funciona para grupos (`group:<id>`) com N inscritos recebendo o mesmo evento.
7. **SSE usa exatamente o mesmo mecanismo de Redis Pub/Sub para propagar eventos entre instâncias** — quando o servidor que gera o evento não é o mesmo em que o cliente está conectado via SSE, o Pub/Sub faz a ponte da mesma forma que faz para WebSocket.
8. **Mensagens publicadas no Redis Pub/Sub para um usuário offline se perdem — não há buffer implícito** — a mitigação é manter uma tabela de "mensagens pendentes" no banco, escrita em paralelo a cada publicação; ao reconectar, o cliente busca essa tabela e recebe tudo de uma vez.
9. **Existem dois vieses para a tabela de mensagens pendentes: histórico permanente vs. limpeza após entrega** — a fonte cita o WhatsApp como exemplo do segundo viés: mensagens pendentes são deletadas do servidor assim que entregues, por motivos de compliance/dados sensíveis (o dispositivo do usuário guarda o histórico, com backup próprio).
10. **Alternativa ao "vieses de mensagens pendentes": timestamp do último evento recebido** — o cliente informa a última mensagem que recebeu, e o servidor calcula e devolve tudo que veio depois disso, sem precisar de uma tabela dedicada de pendências.
11. **Os erros mais comuns em entrevista sobre real-time**: não saber lidar com escala horizontal de servidores, não citar como servidores se comunicam entre si (a "segunda etapa" que a maioria ignora), não saber tratar usuário offline, e travar diante da pergunta — e, inversamente, usar WebSocket/infra pesada para um sistema de baixíssima escala é tão erro quanto os anteriores.

## Entidades Mencionadas

- Redis (Pub/Sub)
- Google Docs, Figma (colaboração em tempo real via WebSocket)
- Uber, iFood (tracking em tempo real)
- WhatsApp (exemplo de retenção temporária de mensagens pendentes por compliance)

## Conceitos Tocados

- [[wiki/concepts/websocket-vs-polling]]
- [[wiki/concepts/server-sent-events]]
- [[wiki/concepts/load-balancer]]
- [[wiki/concepts/pub-sub]]
- [[wiki/concepts/redis]]
- [[wiki/concepts/mensageria]]
- [[wiki/concepts/chat-distribuido]]
- [[wiki/concepts/protocolo-de-rede]]
- [[wiki/concepts/escalabilidade-horizontal]]

## Open Questions

- A fonte não detalha o que acontece se o próprio Redis (o broker Pub/Sub) cair — sem persistência nem réplica, esse é um ponto único de falha para toda a comunicação entre servidores, algo que [[wiki/concepts/chat-distribuido]] já cobre parcialmente ao comparar Redis Pub/Sub (fire-and-forget) com Kafka (log persistente, replay via offset).
- Nenhuma contradição com [[wiki/sources/server-sent-events-sse-tempo-real]] ou [[wiki/sources/websocket-sse-realtime]] — esta fonte aprofunda especificamente a camada de infraestrutura (LB L4 vs L7, matemática de conexões por servidor) e o padrão de tópico-por-usuário no Redis, que as fontes anteriores não detalhavam com esse nível de "resposta de entrevista".
- A estimativa de "300-500 mil conexões por servidor" não vem com metodologia de cálculo explícita na fonte — tratar como ordem de grandeza ilustrativa, não como número de capacity planning real.

## Raw Quotes

> "Problemas simples requerem soluções simples. Se a gente precisar de algo mais avançado, existe uma solução mais apropriada, mas para sistemas desse nível, o polling é totalmente razoável."

> "O layer 4 permite que o load balancer não abra nem faça nada com o conteúdo — ele só redireciona pro servidor que tiver com menos conexões abertas."

> "Quando o usuário 1 se conecta no servidor, ele se inscreve em um tópico do Redis chamado, por exemplo, user:1 [...] Quando aperta enter e manda a mensagem, o servidor publica essa mensagem no tópico user:2."

> "Não caia nessa cilada de usar uma arquitetura super forte para um sistema que é super simples."
