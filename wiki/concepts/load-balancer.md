---
type: concept
title: "Load Balancer"
aliases: ["lb", "load balancing", "l4", "l7", "round robin"]
date_created: 2026-04-23
date_updated: 2026-07-03
source_count: 5
tags: [load-balancer, l4, l7, round-robin, health-check, alta-disponibilidade, infra]
skill: tech-mentor-infra
status: stub
---

# Load Balancer

Componente que distribui tráfego entre múltiplas instâncias de um serviço para escalar horizontalmente e garantir disponibilidade.

**L4 vs L7:**
- **L4 (TCP/UDP):** mais rápido, sem inspecionar conteúdo. Para TCP genérico (banco, SMTP).
- **L7 (HTTP):** roteamento por path/header/host, SSL termination, cookie stickiness. Essencial para microsserviços e canary.

**Algoritmos:** Round Robin, Least Connections, IP Hash (stickiness), Weighted.

**Health check ativo:** coração do LB — remove instâncias não-saudáveis. Sem health check, o LB distribui para instâncias caídas.

**Alta disponibilidade:** LB não pode ser SPOF — active-passive com VIP (Virtual IP).

**Em microsserviços:** dois níveis — externo (L7 + SSL) + interno (service mesh/Envoy).

## Pré-requisito

Para distribuir livremente, os servidores precisam ser [[stateless]]. Com estado em memória, é necessário usar [[sticky-session]] — o que limita os benefícios de distribuição.

## WebSocket exige L4 dedicado

Conexões WebSocket são de longa duração e stateful — um L7 comum pode ter timeouts de idle incompatíveis com conexões que ficam abertas por horas. Por isso WebSocket geralmente exige um load balancer de camada 4, enquanto [[wiki/concepts/server-sent-events|SSE]], por rodar sobre HTTP convencional (uma única resposta mantida aberta, sem upgrade de protocolo), funciona sem infraestrutura especial de LB — uma das vantagens operacionais do SSE frente ao WebSocket.

**Por que L7 quebra o fluxo:** um LB de camada 7 não é um simples repassador — ele termina a conexão HTTP recebida, lê os cabeçalhos, empacota uma nova requisição e a reenvia ao servidor escolhido. Para request-response isso é transparente, mas para WebSocket quebra o tunelamento TCP contínuo que a conexão precisa manter. O LB L4 evita isso porque nunca abre o conteúdo — apenas encaminha bytes ao servidor com menos conexões abertas no momento (uma forma de balanceamento por carga de conexão, não por round-robin cego).

## Key Sources

- [[sources/load-balancer]]
- [[sources/clusters]]
- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
- [[wiki/sources/server-sent-events-sse-tempo-real]] — WebSocket exige LB L4 e infra especializada; SSE não
- [[wiki/sources/updates-tempo-real-polling-sse-websocket]] — por que L7 quebra o fluxo do WebSocket; LB L4 roteia por menor número de conexões
