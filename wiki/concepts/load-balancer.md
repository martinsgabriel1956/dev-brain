---
type: concept
title: "Load Balancer"
aliases: ["lb", "load balancing", "l4", "l7", "round robin"]
date_created: 2026-04-23
date_updated: 2026-07-15
source_count: 8
tags: [load-balancer, l4, l7, round-robin, health-check, alta-disponibilidade, infra, nginx]
skill: tech-mentor-infra
status: stub
---

# Load Balancer

Componente que distribui tráfego entre múltiplas instâncias de um serviço para escalar horizontalmente e garantir disponibilidade.

**L4 vs L7:**
- **L4 (TCP/UDP):** mais rápido, sem inspecionar conteúdo — só enxerga IP/porta de origem e destino ("cego"). Para TCP genérico (banco, SMTP), WebSocket, jogos online e videochamada (UDP, tolerante a perda de pacote).
- **L7 (HTTP):** intercepta e desempacota a requisição, roteamento por path/header/host, SSL termination, cookie stickiness, autenticação JWT, rate limiting. Essencial para microsserviços, canary e ~90% das aplicações web tradicionais.

## Tipos de Load Balancer

- **Hardware** — F5 Big-IP, Citrix NetScaler (os mais usados), A10 Networks Thunder (atua como GLB, balanceando entre data centers/regiões inteiras — cenário raro no dia a dia, salvo infraestrutura on-premise ou provedores).
- **Software** — Nginx e HAProxy (concorrentes diretos, os mais usados na prática), Traefik.
- **Cloud** — AWS ALB (L7) e NLB (L4); Google Cloud Load Balancer (L4 e L7); Azure Load Balancer (L4) e Application Gateway (L7). AWS e Azure oferecem dois produtos separados justamente porque cada um opera numa camada OSI diferente — balanceadores de hardware/software tradicionais operam em ambas as camadas dependendo apenas da configuração.

## Algoritmos de Balanceamento

- **Round Robin** — algoritmo padrão de qualquer LB; distribui ciclicamente entre os servidores (1 → 2 → 3 → 1...). Simples, mas não resolve todos os cenários.
- **Weighted Round Robin** — direciona proporcionalmente mais tráfego a um servidor com mais peso/capacidade (ex.: `weight=3` no Nginx). Útil quando o servidor original (já escalado verticalmente) é mantido maior e as réplicas horizontais são mais enxutas.
- **Least Connections** (`least_conn`) — envia a próxima requisição ao servidor com menos conexões ativas no momento. Mais inteligente que Round Robin porque considera que requisições têm tempos de processamento variáveis (uma tarefa simples responde rápido; gerar um relatório demora mais).
- **Least Response Time** (`least_time`) — balanceia pelo tempo de resposta observado de cada servidor, evitando sobrecarregar um servidor já degradado. No Nginx, recurso exclusivo da versão paga (Nginx Plus).
- **IP Hash** — stickiness baseada no hash do IP do cliente.
- **Sticky Round Robin / Sticky Session** — fixa um usuário sempre no mesmo servidor após a primeira requisição. Permite escalar horizontalmente aplicações não-stateless (sessão de login em memória, sem JWT), ao custo de perder parte do benefício de distribuição uniforme.

**Health check ativo:** coração do LB — remove instâncias não-saudáveis. Sem health check, o LB distribui para instâncias caídas.

**Alta disponibilidade:** LB não pode ser SPOF — active-passive com VIP (Virtual IP).

**Em microsserviços:** dois níveis — externo (L7 + SSL) + interno (service mesh/Envoy).

**L4 e o par `IP:porta`:** o roteamento "cego" do L4 nada mais é do que ler [[wiki/concepts/porta-de-rede|IP e porta]] do pacote — sem abrir o payload da aplicação. É por isso que L4 serve qualquer protocolo (TCP genérico, UDP) enquanto L7 exige entender o protocolo de aplicação específico (HTTP).

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
- [[wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos]] — tipos de LB (hardware/software/cloud), algoritmos de balanceamento (Weighted RR, Least Connections, Least Time, Sticky RR), demonstração prática com Nginx
- [[wiki/sources/portas-de-rede-como-funcionam]] — L4 roteia por `IP:porta`, sem inspecionar conteúdo
- [[wiki/sources/10-conceitos-fundamentais-backend]] — regra didática mínima: "o load balancer não deveria mandar tráfego para uma instância que travou"
