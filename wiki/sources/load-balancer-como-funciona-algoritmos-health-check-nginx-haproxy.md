---
type: source
title: "Load Balancer: como funciona, algoritmos, health check, Nginx e HAProxy"
aliases: ["load balancer explicado", "load balancer vídeo curto"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/load-balancer-como-funciona-algoritmos-health-check-nginx-haproxy.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-10-08
source_count: 1
tags: [load-balancer, health-check, nginx, haproxy, escalabilidade, sessao, infra]
skill: tech-mentor-infra
status: stable
---

## TL;DR

Vídeo introdutório (canal não identificado): um servidor único cai sob pico de acesso; a saída é vários servidores idênticos atrás de um [[wiki/concepts/load-balancer]], que escolhe o destino por um algoritmo (Round Robin, Weighted RR, Least Connections, IP Hash) e retira servidores mortos do rodízio via [[wiki/concepts/health-check]]. Na camada 7 também age como [[wiki/concepts/reverse-proxy]]. Ferramentas: [[wiki/entities/nginx]], [[wiki/entities/haproxy]], ALB/NLB da [[wiki/entities/amazon-web-services]] e GCP. Erros comuns: sem health check, ignorar sessão local, esperar que o LB conserte código lento.

## Key Claims

**Claim:** Um servidor único tem CPU/memória/disco/rede finitos e engasga em picos; a solução é replicar e dividir a carga.
**Evidence:** exemplo de 500 req/s divididas em 100 por servidor; [[wiki/concepts/escalabilidade-horizontal]].
**Confidence:** alta

**Claim:** Os algoritmos principais são Round Robin, Weighted Round Robin, Least Connections e IP Hash.
**Evidence:** descrição e analogias (roleta; moto vs carro; menor contagem de conexões; hash do IP). Bate com o catálogo da skill. [skill: tech-mentor-infra] A skill acrescenta que Least Connections exige estado compartilhado entre múltiplos LBs e que IP Hash é uma alternativa sem estado global.
**Confidence:** alta

**Claim:** IP Hashing serve a aplicações com sessão local, mas o ideal é não depender de sessão no servidor.
**Evidence:** carrinho/autenticação em sessão; erro comum nº 2. Ver [[wiki/concepts/sticky-session]], [[wiki/concepts/stateless]].
**Confidence:** alta (ressalva: IP Hash quebra com clientes atrás de NAT/IP mudando — [external], não dito na fonte)

**Claim:** O LB não vira gargalo em aplicações de pequeno/médio porte porque é muito mais leve que a aplicação.
**Evidence:** só afirmação do autor, sem números. Contraponto: LB como SPOF exige redundância (ver [[wiki/concepts/single-point-of-failure]]).
**Confidence:** média

**Claim:** Health check (`/health`, falhas consecutivas para marcar morto, sucessos para reviver) permite falhar sem o usuário perceber.
**Evidence:** [[wiki/concepts/health-check]], [[wiki/concepts/alta-disponibilidade]].
**Confidence:** alta

**Claim:** LB na camada 7 roteia por path para serviços diferentes (`/api`, `/images`), atuando como proxy reverso.
**Evidence:** [[wiki/concepts/reverse-proxy]].
**Confidence:** alta

**Claim:** LB não corrige código ruim, query mal feita ou banco mal otimizado.
**Evidence:** erro comum nº 3.
**Confidence:** alta

## Entidades

[[wiki/entities/nginx]], [[wiki/entities/haproxy]], [[wiki/entities/amazon-web-services]] (ALB/NLB).

## Conceitos

[[wiki/concepts/load-balancer]], [[wiki/concepts/health-check]], [[wiki/concepts/sticky-session]], [[wiki/concepts/reverse-proxy]], [[wiki/concepts/stateless]], [[wiki/concepts/session-management]], [[wiki/concepts/escalabilidade-horizontal]], [[wiki/concepts/alta-disponibilidade]], [[wiki/concepts/single-point-of-failure]], [[wiki/concepts/observabilidade]], [[wiki/concepts/microsservicos]].

## Open questions

- Autor/canal não identificado.
- Fonte afirma "ARB" (ASR) — interpretado como ALB.
- Sem tratar o próprio LB como SPOF (active-passive/VIP), ver [[wiki/concepts/load-balancer]].

## Quotes

> "Load balancer não corrige código ruim."
