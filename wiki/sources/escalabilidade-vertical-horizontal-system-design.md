---
type: source
title: "Escalabilidade: Vertical vs Horizontal — System Design"
aliases: ["escalabilidade system design", "vertical vs horizontal scaling"]
date_created: 2026-06-26
date_updated: 2026-06-26
source_count: 0
tags: [system-design, escalabilidade, load-balancer, stateless, cdn, auto-scaling, sharding, replicacao, cap-theorem, cache]
skill: tech-mentor-system-design
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/escalabilidade-vertical-horizontal-system-design.md
source_url:
author: desconhecido (canal de vídeo — série de System Design)
date_published:
date_ingested: 2026-06-26
---

# Escalabilidade: Vertical vs Horizontal — System Design

## TL;DR

Vídeo introdutório de System Design sobre escalabilidade — a capacidade de lidar com mais carga sem degradação perceptível. Apresenta as duas estratégias fundamentais (vertical e horizontal), Load Balancer, stateless servers, as três camadas de um sistema web (web, aplicação, dados) e quando/como escalar cada uma.

## Key Claims

1. **Escalabilidade é a arte de crescer de forma sustentável** — não é só "adicionar servidor", é garantir que cada camada (web, app, dados) escale de forma adequada.
2. **Vertical é simples mas tem teto** — custo não-linear, limite físico e single point of failure impedem crescimento infinito.
3. **Horizontal é praticamente ilimitado, mas requer stateless** — qualquer servidor precisa poder atender qualquer requisição; sessão em memória inviabiliza isso.
4. **Load Balancer é o maestro da horizontal** — Round Robin, Least Connections, IP Hash; health checks removem instâncias caídas automaticamente.
5. **L4 vs L7 é uma escolha de trade-off** — L4 é rápido (só IP/porta); L7 é flexível (roteia por URL, headers, cookies).
6. **CDN é o cache global da camada web** — roteia usuário para o servidor mais próximo geograficamente; escala com zero código.
7. **Banco de dados é o gargalo real** — aplicação escala fácil; banco é stateful por natureza; replicação e sharding são estratégias, mas têm trade-offs.
8. **Cache é o melhor amigo antes de escalar** — quanto menos bater no banco, melhor.
9. **Não escale prematuramente** — identifique o gargalo antes de agir; escalar não é desculpa para banco travar com 100 usuários.

## Entidades Mencionadas

- Nginx, HAProxy, AWS ALB/NLB, Cloudflare (ferramentas de Load Balancer)
- Redis (sessão externa, cache distribuído)
- S3 / object storage (arquivos em servidores stateless)
- CDN (camada web)
- Auto Scaling (AWS/cloud — camada de aplicação)
- Teorema CAP (mencionado; vídeo dedicado referenciado)

## Conceitos Tocados

- [[escalabilidade-vertical]]
- [[escalabilidade-horizontal]]
- [[load-balancer]]
- [[stateless]]
- [[sticky-session]]
- [[cdn]]
- [[auto-scaling]]
- [[sharding]]
- [[replicacao-de-banco]]
- [[cap-theorem]]
- [[cache]]
- [[gargalo]]
- [[redis]]
- [[cache-aside]]

## Open Questions

- O vídeo menciona sharding e replicação mas adia para "outro vídeo" — esses conceitos precisam de fonte específica para profundidade.
- O Teorema CAP é mencionado superficialmente — necessita ingest de fonte dedicada.
- Auto Scaling é descrito de forma genérica (AWS-flavored); variações em Kubernetes (HPA/VPA) não são cobertas.

## Raw Quotes

> "A regra de ouro é: se você quer escalar horizontalmente, seu servidor precisa ser stateless."

> "Antes de escalar, veja se não dá para cachear. Quanto menos você bater no banco, melhor."

> "Não escale prematuramente. Esteja pronto para quando precisar. Arquitetura boa é a que permite escalar sem reescrever tudo."

> "Na maioria dos sistemas, o banco é o gargalo. A aplicação costuma escalar fácil, mas o banco não."
