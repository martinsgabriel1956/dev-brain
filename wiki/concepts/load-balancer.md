---
type: concept
title: "Load Balancer"
aliases: ["lb", "load balancing", "l4", "l7", "round robin"]
date_created: 2026-04-23
date_updated: 2026-08-17
source_count: 16
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
- **Dynamic Weighted Round Robin** — resolve a limitação prática do Weighted Round Robin estático (peso calibrado manualmente, o que exigiria benchmark de carga real por servidor e raramente é feito): calcula o peso de cada servidor dinamicamente, usando a latência média das últimas N requisições servidas como métrica proxy — um servidor 3x mais rápido recebe, na sequência, cerca de 3x mais requisições, sem que ninguém precise declarar um `weight` fixo. Ainda assim, em cenários de alta variância de potência/custo, ocasionalmente dropa requisição, embora se adapte bem ao longo do tempo.
- **PEWMA (Pick Exponentially Weighted Moving Average)** — combina a adaptação por latência do Dynamic Weighted Round Robin com o monitoramento de carga em tempo real do Least Connections, buscando simultaneamente baixa latência e alta resiliência a drops. `[skill: tech-mentor-infra]` Família próxima da técnica **Power of Two Choices (P2C)**, usada internamente por Envoy/Nginx: em vez de rastrear o estado exato de todos os servidores (custoso em LBs distribuídos), escolhe 2 servidores aleatoriamente e envia para o menos carregado dos dois — atinge resultado quase tão bom quanto Least Connections global sem exigir estado compartilhado entre múltiplos load balancers. A skill também registra essa exigência de estado compartilhado como uma limitação explícita do Least Connections "puro" em topologias com múltiplos LBs, ponto não coberto pela fonte que descreve o algoritmo com um único load balancer.

### Fila de requisições como mitigação (não solução) de drops

Uma alternativa simples a mudar de algoritmo é colocar uma **fila de requisições** na frente de cada servidor (na prática, um broker como Redis ou RabbitMQ). A requisição só é dropada quando a própria fila enche. É um trade-off, não um ganho gratuito: reduz drops, mas aumenta a latência de algumas requisições que esperam na fila — e com custo de requisição variado, as filas tendem a se acumular de forma desigual entre servidores, mesmo com Round Robin distribuindo "igualmente" por fora.

### Por que Least Connections é mais resiliente que qualquer Round Robin

Least Connections elimina a incerteza que os algoritmos baseados em Round Robin (mesmo ponderados dinamicamente) ainda carregam: em vez de estimar a partir de peso ou latência passada, o load balancer mantém contagem exata de conexões em aberto por servidor — porque está posicionado entre cliente e servidor, vendo cada requisição abrir e fechar. Isso faz com que Least Connections só drope uma requisição quando **todas** as filas de **todos** os servidores já estiverem cheias, ou seja, quando não há mais capacidade em lugar nenhum do sistema — diferente do Round Robin (ponderado ou não), que pode dropar num servidor individual mesmo havendo capacidade ociosa em outro.

**Health check ativo:** coração do LB — remove instâncias não-saudáveis. Sem health check, o LB distribui para instâncias caídas.

**Alta disponibilidade:** LB não pode ser SPOF — active-passive com VIP (Virtual IP).

**Em microsserviços:** dois níveis — externo (L7 + SSL) + interno (service mesh/Envoy).

**L4 e o par `IP:porta`:** o roteamento "cego" do L4 nada mais é do que ler [[wiki/concepts/porta-de-rede|IP e porta]] do pacote — sem abrir o payload da aplicação. É por isso que L4 serve qualquer protocolo (TCP genérico, UDP) enquanto L7 exige entender o protocolo de aplicação específico (HTTP).

## Pré-requisito

Para distribuir livremente, os servidores precisam ser [[stateless]]. Com estado em memória, é necessário usar [[sticky-session]] — o que limita os benefícios de distribuição.

## WebSocket exige L4 dedicado

Conexões WebSocket são de longa duração e stateful — um L7 comum pode ter timeouts de idle incompatíveis com conexões que ficam abertas por horas. Por isso WebSocket geralmente exige um load balancer de camada 4, enquanto [[wiki/concepts/server-sent-events|SSE]], por rodar sobre HTTP convencional (uma única resposta mantida aberta, sem upgrade de protocolo), funciona sem infraestrutura especial de LB — uma das vantagens operacionais do SSE frente ao WebSocket.

**Por que L7 quebra o fluxo:** um LB de camada 7 não é um simples repassador — ele termina a conexão HTTP recebida, lê os cabeçalhos, empacota uma nova requisição e a reenvia ao servidor escolhido. Para request-response isso é transparente, mas para WebSocket quebra o tunelamento TCP contínuo que a conexão precisa manter. O LB L4 evita isso porque nunca abre o conteúdo — apenas encaminha bytes ao servidor com menos conexões abertas no momento (uma forma de balanceamento por carga de conexão, não por round-robin cego).

## Load Balancer vs. Reverse Proxy

Nem todo [[wiki/concepts/reverse-proxy]] é um load balancer: um LB decide **entre múltiplas instâncias equivalentes** usando algum algoritmo (Round Robin, Least Connections...); um reverse proxy pode apontar para **um único destino fixo** e ainda assim já cumprir seu papel — só interceptar, inspecionar e repassar. Num deploy [[wiki/concepts/blue-green-deploy|blue/green]] de host único, o Nginx atua como reverse proxy nesse segundo sentido: nunca distribui tráfego entre blue e green ao mesmo tempo, só redireciona 100% para um dos dois por vez.

## Key Sources

- [[sources/load-balancer]]
- [[sources/clusters]]
- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
- [[wiki/sources/server-sent-events-sse-tempo-real]] — WebSocket exige LB L4 e infra especializada; SSE não
- [[wiki/sources/updates-tempo-real-polling-sse-websocket]] — por que L7 quebra o fluxo do WebSocket; LB L4 roteia por menor número de conexões
- [[wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos]] — tipos de LB (hardware/software/cloud), algoritmos de balanceamento (Weighted RR, Least Connections, Least Time, Sticky RR), demonstração prática com Nginx
- [[wiki/sources/portas-de-rede-como-funcionam]] — L4 roteia por `IP:porta`, sem inspecionar conteúdo
- [[wiki/sources/10-conceitos-fundamentais-backend]] — regra didática mínima: "o load balancer não deveria mandar tráfego para uma instância que travou"
- [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]] — Nginx como reverse proxy (não LB) num deploy blue/green de host único, redirecionando 100% do tráfego para uma porta por vez
- [[wiki/sources/system-design-simulador-hotel-booking-replit]] — inserido entre client e app server num exercício de hotel booking; o material reforça que a escolha do algoritmo (round robin, least connections etc.) deve ser justificada numa entrevista, mesmo quando o foco do exercício está em outra camada
- [[wiki/sources/escalar-para-um-milhao-de-usuarios]] — o LB entra exatamente quando surge o segundo servidor (o usuário precisa saber para qual instância mandar o request); é o que remove o SPOF de servidor e, na multi-região, também roteia por geolocalização entre data centers
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]] — saber que um load balancer existe é tratado como conhecimento "dado" a partir do nível pleno/sênior; o que se avalia em sênior é usar essa peça para escalar a milhões de usuários, não a definição básica
- [[wiki/sources/system-design-entrevista-cinema-draw-io]] — usado como peça "de praxe" mesmo num desenho simples de entrevista (3 web servers atrás de 1 load balancer), com justificativa didática de não sobrecarregar uma instância já saturada
- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]] — ALB (AWS Load Balancer) como L7 explícito: só por operar na camada de aplicação é que o roteamento por rota HTTP (`/produtos` vs. `/admin` para destinos diferentes) é possível; distribuição pode alcançar destinos heterogêneos (EC2, Lambda) na mesma regra
- [[wiki/sources/reacao-artigo-visual-algoritmos-load-balancing]] — simulação visual do porquê Round Robin dropa requisição sob variância de custo/potência, fila de requisições como trade-off latência-vs-drop, Dynamic Weighted Round Robin (peso por latência observada) e PEWMA (combina latência + carga em tempo real)
- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — ALB acoplado ao [[wiki/concepts/auto-scaling|Auto Scaling Group]] como arquitetura clássica AWS: health checks constantes removem instâncias falhas do pool automaticamente
