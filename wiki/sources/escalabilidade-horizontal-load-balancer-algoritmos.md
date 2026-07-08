---
type: source
title: "Escalabilidade Horizontal, Load Balancer e Algoritmos de Balanceamento"
aliases: ["load balancer na prática", "algoritmos de balanceamento de carga", "camada 4 vs camada 7"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 0
tags: [system-design, escalabilidade, load-balancer, osi, tcp, udp, http, nginx, networking]
skill: tech-mentor-system-design
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/escalabilidade-horizontal-load-balancer-algoritmos.md
source_url:
author: Renato Augusto
date_published:
date_ingested: 2026-07-03
---

# Escalabilidade Horizontal, Load Balancer e Algoritmos de Balanceamento

## TL;DR

Vídeo de Renato Augusto aprofundando o tema de [[wiki/sources/escalabilidade-vertical-horizontal-system-design]] com foco específico em Load Balancer: os três tipos de balanceador (hardware, software, cloud), por que provedores cloud oferecem balanceadores separados para camada 4 e camada 7 do modelo OSI, e uma demonstração prática configurando Nginx com diferentes algoritmos de balanceamento (Round Robin, Weighted Round Robin, Least Connections, Least Response Time, Sticky Round Robin).

## Key Claims

1. **Escalar horizontalmente só faz sentido depois de esgotar a escala vertical** — vertical tem teto de custo não-linear e é single point of failure; horizontal resolve isso replicando o servidor atrás de um load balancer.
2. **Load balancers existem em três categorias**: hardware (F5 Big-IP, Citrix NetScaler, A10 Networks Thunder — este último atuando como GLB entre data centers, cenário raro no dia a dia), software (Nginx, HAProxy, Traefik — os mais usados na prática) e cloud (AWS ALB/NLB, Google Cloud Load Balancer, Azure Load Balancer/Application Gateway).
3. **AWS e Azure oferecem dois balanceadores porque operam em camadas OSI diferentes** — ALB (AWS) e Application Gateway (Azure) na camada 7; NLB (AWS) e Load Balancer (Azure) na camada 4. Balanceadores de hardware/software tradicionais operam em ambas as camadas dependendo apenas da configuração.
4. **Camada 4 é "cega"**: só enxerga IP/porta de origem e destino, não interpreta o conteúdo — por isso é mais rápida e é a escolha obrigatória para WebSocket, jogos online em tempo real (UDP) e videochamada (UDP, tolerante a perda de pacote). O vídeo cita o WhatsApp como exemplo de arquitetura que exige LB de camada 4 por usar WebSocket, prometendo um vídeo dedicado à arquitetura completa do WhatsApp.
5. **Camada 7 intercepta e interpreta a requisição HTTP** — permite roteamento por URL/path, leitura de headers/cookies, autenticação JWT, rate limiting. Recomendado para ~90% das aplicações web tradicionais.
6. **Algoritmos de balanceamento cobertos na prática (Nginx)**:
   - **Round Robin** — padrão, distribui ciclicamente entre servidores.
   - **Weighted Round Robin** — direciona proporcionalmente mais tráfego a um servidor com mais capacidade (diretiva `weight`).
   - **Least Connections** (`least_conn`) — envia a nova requisição ao servidor com menos conexões ativas no momento; mais inteligente que Round Robin porque considera tempo de processamento variável por requisição.
   - **Least Response Time** (`least_time`) — balanceia pelo tempo de resposta observado de cada servidor; recurso exclusivo do Nginx Plus (pago).
   - **Sticky Round Robin** — fixa um usuário sempre no mesmo servidor após a primeira requisição, permitindo escalar horizontalmente aplicações com sessão em memória (sem JWT/stateless).
7. **Trocar entre camada 4 e camada 7 no Nginx é uma mudança de poucas linhas** — bloco `http`+`location` para camada 7; bloco `stream` (sem `location`) para camada 4, que apenas fecha a conexão TCP/UDP sem interpretar HTTP.

## Entidades Mencionadas

- Nginx, HAProxy, Traefik (load balancers de software)
- F5 Big-IP, Citrix NetScaler, A10 Networks Thunder (load balancers de hardware)
- AWS (ALB, NLB), Google Cloud Load Balancer, Azure (Load Balancer, Application Gateway)
- WhatsApp (exemplo de arquitetura com LB de camada 4/WebSocket, mencionado como preparação para vídeo futuro)

## Conceitos Tocados

- [[wiki/concepts/escalabilidade-vertical]]
- [[wiki/concepts/escalabilidade-horizontal]]
- [[wiki/concepts/load-balancer]]
- [[wiki/concepts/protocolo-de-rede]]
- [[wiki/concepts/websocket-vs-polling]]
- [[wiki/concepts/cap-theorem]]

## Open Questions

- O vídeo promete um vídeo dedicado (em duas partes) sobre a arquitetura completa do WhatsApp — ainda não ingerido; quando disponível, cruzar com [[wiki/concepts/websocket-vs-polling]] e [[wiki/concepts/load-balancer]].
- `least_time` é citado como exclusivo do Nginx Plus — não verificado com documentação oficial atual do Nginx, marcado como afirmação da fonte, não confirmada por skill.
- O algoritmo IP Hash é mencionado de passagem, sem profundidade — mesma lacuna já registrada em [[wiki/concepts/load-balancer]].

## Raw Quotes

> "Não faz sentido você escalar nada horizontalmente se você ainda não tentou uma escala vertical."

> "Load balancer de camada quatro vai ser muito mais rápido que load balancer de camada sete... ele é cego, ele é burro."

> "O balanceador de camada sete intercepta a requisição, ele pode descompactar esse HTTP, ele vai olhar o que tá dentro... dá para fazer rate limit, dá para fazer muita coisa."

> "Não é simplesmente pegar um load balanceiro aqui e colocar ele aleatório para sair rodando, você precisa configurar qual é o algoritmo baseado no problema que você tá tentando resolver."
