---
type: concept
title: "Escalabilidade Horizontal"
aliases: ["horizontal scaling", "scale out", "escalar horizontalmente"]
date_created: 2026-06-26
date_updated: 2026-08-24
source_count: 20
tags: [escalabilidade, arquitetura, sistemas-distribuidos, nosql, redis, backend]
skill: tech-mentor-backend
status: stable
---

# Escalabilidade Horizontal

## TL;DR

Aumentar capacidade adicionando mais máquinas ao sistema (scale out), ao invés de aumentar recursos na mesma máquina (scale up / escalabilidade vertical).

## Horizontal vs Vertical

| | Vertical (Scale Up) | Horizontal (Scale Out) |
|---|---|---|
| Estratégia | Mais CPU/RAM/banda na mesma máquina | Mais máquinas no cluster |
| Custo | Caro; hardware tem teto físico | Linear com o número de nós |
| Disponibilidade | Ponto único de falha | Redundância por design |
| Complexidade | Simples | Requer coordenação distribuída |
| Melhor para | Bancos relacionais, sessão com estado | [[nosql]], stateless services |

## NoSQL e Escalabilidade Horizontal

Bancos [[nosql]] foram projetados para escalar horizontalmente. Exemplos:

- **[[redis]] Cluster** — 16.384 hash slots distribuídos entre N masters; adicionar nós redistribui slots
- **Cassandra** — partição por consistent hashing; adicionar nó redistribui automaticamente
- **MongoDB** — sharding nativo por shard key

## Por Que Bancos Relacionais Escalam Menos Horizontalmente

Normalização e transações ACID entre tabelas exigem coordenação entre nós (2PC, distributed locks) — o que é caro e complexo. Por isso PostgreSQL e Oracle escalam melhor verticalmente.

## Redis e Single CPU

[[redis]] roda em **um único CPU por instância**. Escalar verticalmente (mais núcleos) não ajuda. A solução correta é clusterizar: múltiplas instâncias redis em diferentes nós, cada uma usando 1 CPU.

## Pré-requisitos para funcionar

1. **Servidores [[stateless]]** — sessão em Redis, arquivos em S3, dados no banco; nada em memória local
2. **[[load-balancer]]** — distribui requisições entre as instâncias
3. **[[auto-scaling]]** — sobe e derruba instâncias automaticamente por regras (CPU, fila, memória)

Quando distribuir dados entre máquinas, entra o [[cap-theorem]] — consistência vs disponibilidade vs tolerância a partições.

## Granularidade Fina de Capacidade

Uma vantagem de custo pouco discutida: horizontal permite adicionar exatamente a capacidade necessária para absorver um pico (ex.: um servidor a mais), enquanto vertical em cloud providers costuma forçar dobrar o tier da instância inteira (ver [[wiki/concepts/escalabilidade-vertical]]). Menos servidores maiores também concentram mais risco — mais réplicas menores reduzem o impacto de qualquer ponto único de falha, já que as demais continuam operando se uma cair.

## Escalar por Redundância, Não Só por Volumetria

Nem toda escalabilidade horizontal existe para absorver alta volumetria. [[wiki/sources/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto]] traz um caso explícito: os data providers de um sistema de placares ao vivo produzem "centenas ou milhares" de eventos por segundo — não milhões — e um único servidor bastaria para esse volume. Ainda assim, a arquitetura escala horizontalmente a API de ingestão e os consumers, porque o requisito não-funcional de **alta disponibilidade 24x7** exige redundância: sem réplicas, a queda de qualquer componente único (API de ingestão, consumer) para toda a cadeia de atualização. Escalar aqui compra tolerância a falha, não capacidade adicional.

## Gatilho de Escala Além da Volumetria: Decisão de Negócio de Cobertura Global

[[wiki/sources/world-cup-system-design]] (slide deck da mesma aula que [[wiki/sources/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto]]) nomeia um quinto gatilho de escala, além dos quatro problemas técnicos já documentados (recalcular timeline, refresh manual do cliente, sem HA, volume de usuários): a decisão de produto de atender **todos os campeonatos do mundo simultaneamente** — não só a Copa — evidenciada por um mosaico de 14 competições reais (Champions League, Brasileirão, Libertadores, La Liga, Premier League etc.). Diferente dos gatilhos anteriores (todos técnicos, sobre uma única competição), este é um gatilho de **escopo de produto**: mais partidas simultâneas ao redor do mundo implica mais partições Kafka, mais linhas em `matches`, e potencialmente milhares de streams SSE concorrentes em fusos horários diferentes — sem que o board detalhe explicitamente a resposta arquitetural a esse requisito específico (ver open question na fonte).

## Caso especial: serviços de conexão persistente (WebSocket)

Escalar horizontalmente um serviço de conexões longas (WebSocket) tem uma restrição que serviços HTTP request-response não têm: exige [[wiki/concepts/load-balancer|load balancer de camada 4]] em vez de camada 7, porque o LB não pode reabrir a conexão para rotear (quebraria o tunelamento TCP). Além disso, servidores replicados não se comunicam entre si automaticamente — precisam de um broker externo (ex: [[wiki/concepts/redis]] Pub/Sub) para que uma mensagem publicada num servidor alcance um usuário conectado em outro. Ver [[wiki/concepts/chat-distribuido]].

## Key Sources

- [[wiki/sources/arquitetura-de-sacrificio]] — crescimento exponencial (ordens de grandeza) é o que invalida a arquitetura inicial e dispara o sacrifício; regra do "10×" do Google
- [[wiki/sources/como-arquitetar-com-cache-e-redis]]
- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
- [[wiki/sources/updates-tempo-real-polling-sse-websocket]] — escalabilidade horizontal de servidores WebSocket, LB L4 obrigatório, comunicação entre servidores via Redis Pub/Sub
- [[wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos]] — tipos de load balancer e algoritmos de balanceamento (Weighted RR, Least Connections, Least Time, Sticky RR) usados para distribuir carga entre as réplicas
- [[wiki/sources/10-conceitos-fundamentais-backend]] — framing de entrada nível-10-conceitos: começar com um servidor só, crescer para "mais usuários, mais chamadas de API, mais consultas ao banco, mais jobs assíncronos, mais picos inesperados"
- [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]] — read replicas como escalonamento horizontal da camada de leitura do banco ("adicionar réplicas quase infinitamente"), distinto do scale-out de servidores de aplicação
- [[wiki/sources/system-design-simulador-hotel-booking-replit]] — réplicas de SQL database removem o alerta de bottleneck do banco num exercício simulado, mas deslocam o gargalo para o app server — demonstração direta de que escalar horizontalmente uma camada sem tratar a seguinte só move o problema
- [[wiki/sources/escalabilidade-horizontal-vertical-custo-grafico]] — exemplo gráfico de granularidade fina de capacidade (um servidor a mais vs. dobrar instância) e resiliência via mais réplicas menores
- [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] — recapitula escalar horizontalmente a aplicação (réplicas + load balancer) como resposta ao gargalo de volumetria, antes de mostrar que isso apenas desloca o gargalo para o banco de dados, motivando [[wiki/concepts/sharding]]
- [[wiki/sources/escalar-para-um-milhao-de-usuarios]] — como os dados vivem no banco (não no servidor), a aplicação vira um cluster de servidores atrás de um load balancer; também a etapa final de replicar o cluster inteiro por data center (multi-região) com roteamento por geolocalização
- [[wiki/sources/reacao-artigo-visual-algoritmos-load-balancing]] — visualização passo a passo de por que um servidor único satura sob carga e como adicionar réplicas atrás de um load balancer elimina drops, antes de detalhar os algoritmos de distribuição
- [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]] — argumento "monolito basta": rodar o monolito em 3-4 máquinas com load balancer e réplica de banco atende ~1M de usuários (exemplo Pieter Levels), sem precisar de microsserviços
- [[wiki/sources/back-pressure-producer-consumer-filas-bounded-admission-control]] — paralelizar consumidores (cluster) e a própria fila como resposta a um produtor mais rápido que o consumidor, no contexto de [[wiki/concepts/back-pressure]]
- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — implementação concreta na AWS: [[wiki/concepts/auto-scaling|Auto Scaling Group]] (min/desejado/máximo) atrás de um [[wiki/concepts/load-balancer|Application Load Balancer]], escalando por métrica de CPU
- [[wiki/sources/system-design-load-balancer-nivel-macaco]] — demonstração passo a passo em simulador (1 → 4 servidores atrás de um load balancer com round robin eliminando falhas em cascata) e a heurística de quando NÃO escalar horizontalmente ainda (baixa complexidade/poucos usuários = over-engineering)
- [[wiki/sources/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto]] — caso explícito de escalar horizontalmente por redundância/alta disponibilidade, não por volumetria (data providers produzem centenas/milhares de eventos por segundo, não milhões); paralelismo real do Kafka amarrado ao número de partições, não ao número de consumers
- [[wiki/sources/world-cup-system-design]] — quinto gatilho de escala, de escopo de produto (atender todos os campeonatos do mundo), distinto dos quatro gatilhos técnicos já documentados na fonte-irmã
- [[wiki/sources/como-projetar-sistemas-encurtador-de-urls-passo-a-passo]] — redundância de servidores (mínimo dois por microsserviço via EC2 + Elastic Load Balancer) como tática concreta para atender ao requisito não-funcional de resiliência a falhas, não só de volumetria
- [[wiki/sources/escalando-aplicacao-zero-a-um-milhao-usuarios-renato-augusto]] — versão de autoria explícita (Renato Augusto) do mesmo desenho SPOF-a-SPOF de [[wiki/sources/escalar-para-um-milhao-de-usuarios]]; reforça que servidores atrás do LB passam a usar IPs privados, inacessíveis diretamente da internet, como prática de segurança adicional à escala
