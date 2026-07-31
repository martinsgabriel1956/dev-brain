---
type: concept
title: "Reverse Proxy"
aliases: ["proxy reverso", "reverse proxy", "web server como proxy"]
date_created: 2026-07-20
date_updated: 2026-07-31
source_count: 2
tags: [nginx, reverse-proxy, infra, deploy, web-server, traefik, coolify, auto-update, disponibilidade]
skill: tech-mentor-infra
status: stub
---

# Reverse Proxy

Servidor que fica na frente de um ou mais servidores de aplicação, recebendo as requisições do usuário e repassando internamente para o processo real — o cliente nunca fala diretamente com a aplicação. Nginx e HAProxy são as implementações de software mais comuns; em setups gerenciados por PaaS self-hosted como [[wiki/concepts/coolify]], o Traefik cumpre esse papel.

## Risco: auto-update de proxy em produção

O reverse proxy é um ponto único por onde passa todo o tráfego — uma regressão nele derruba a aplicação inteira mesmo que o código da aplicação em si esteja saudável. Em [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]], o Coolify atualizou o Traefik automaticamente para uma versão (3.6.16) com bug de CPU constante (35% mesmo sem tráfego) e memory leak (4,7 GB em 40 minutos), consumindo capacidade que deveria estar disponível pra aplicação — e agravando um ataque de [[wiki/concepts/ddos-syn-flood|SYN flood]] simultâneo. Aprendizado registrado: travar a versão do proxy reverso em produção, tratando atualização como mudança deliberada, não automática.

## Reverse Proxy vs. Load Balancer

Não são a mesma coisa, mas a mesma peça de software costuma fazer os dois: um [[wiki/concepts/load-balancer]] distribui tráfego entre **múltiplas instâncias equivalentes**; um reverse proxy só precisa apontar para **uma porta/processo**, sem decidir entre opções. Um deploy [[wiki/concepts/blue-green-deploy|blue/green]] de host único usa o reverse proxy nesse segundo modo: nunca balanceia entre blue e green ao mesmo tempo, só troca qual dos dois é o alvo — a decisão é binária e manual (ou via script), não um algoritmo de balanceamento como Round Robin.

## Deploy blue/green num host único

Padrão mínimo, sem Kubernetes nem múltiplas máquinas:

```
Usuário → Nginx (porta 80) → app na porta 3001 (blue) ou 3002 (green)
```

1. As duas versões da aplicação já rodam em paralelo, em portas diferentes, na mesma VPS.
2. A versão nova é testada acessando sua porta diretamente, sem passar pelo proxy.
3. A troca de tráfego é só uma edição da configuração do proxy (`proxy_pass` apontando para a outra porta) seguida de reload — nenhum processo é criado ou destruído nesse passo.
4. A versão antiga fica de pé por um tempo depois da troca, permitindo rollback instantâneo (reverter a config do proxy de volta).

## Key Sources

- [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]] — demo prática de reverse proxy com swap manual entre duas portas via script, sem load balancing real entre elas
- [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]] — auto-update de proxy (Traefik via Coolify) como causa raiz de um bug de CPU/memory leak que agravou um SYN flood
