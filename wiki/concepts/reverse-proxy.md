---
type: concept
title: "Reverse Proxy"
aliases: ["proxy reverso", "reverse proxy", "web server como proxy"]
date_created: 2026-07-20
date_updated: 2026-07-20
source_count: 1
tags: [nginx, reverse-proxy, infra, deploy, web-server]
skill: tech-mentor-infra
status: stub
---

# Reverse Proxy

Servidor que fica na frente de um ou mais servidores de aplicação, recebendo as requisições do usuário e repassando internamente para o processo real — o cliente nunca fala diretamente com a aplicação. Nginx e HAProxy são as implementações de software mais comuns.

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
