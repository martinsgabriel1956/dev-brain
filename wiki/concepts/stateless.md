---
type: concept
title: "Stateless"
aliases: ["servidor stateless", "sem estado", "stateless server", "stateless architecture"]
date_created: 2026-06-26
date_updated: 2026-07-09
source_count: 2
tags: [system-design, stateless, escalabilidade, load-balancer, sessao]
skill: tech-mentor-system-design
status: draft
---

# Stateless

Um servidor **stateless** não guarda nenhuma informação do usuário em memória local. Cada requisição chega com tudo que o servidor precisa para processá-la — sem depender de contexto armazenado localmente.

## Stateful vs Stateless

| | Stateful | Stateless |
|---|---|---|
| **Sessão** | Guardada em memória do servidor | Guardada em Redis/cache externo |
| **Arquivos** | Disco local | S3 / object storage |
| **Dados** | Em memória | Banco de dados |
| **Load Balancer** | Precisa de sticky sessions | Distribui livremente para qualquer servidor |
| **Tolerância a falhas** | Servidor cai → sessões perdidas | Servidor cai → outro assume sem perda |
| **Escalabilidade** | Difícil — precisa sincronizar estado | Simples — sobe quantas instâncias quiser |

## Por que stateless é pré-requisito da escalabilidade horizontal

Se o servidor guarda sessão em memória, o [[load-balancer]] precisa mandar o mesmo usuário sempre para o mesmo servidor ([[sticky-session]]). Isso:

- Cria desequilíbrio de carga (um servidor sobrecarregado, outros ociosos)
- Perde as sessões se o servidor cair
- Impede que novas instâncias assumas a carga de servidores caídos

Com servidores stateless, qualquer instância atende qualquer requisição — o Load Balancer distribui livremente.

## Como tornar um servidor stateless

```
Sessão de usuário    → Redis (TTL configurado)
Upload de arquivo    → S3 / objeto storage
Estado de jobs       → Banco de dados ou fila
Cache local          → Redis / Memcached compartilhado
```

## A regra de ouro

> "Se você quer escalar horizontalmente, seu servidor **precisa** ser stateless."

Fazer a aplicação stateless desde o início é muito mais fácil do que migrar depois — o estado local tende a proliferar.

## Relação com outros conceitos

- [[escalabilidade-horizontal]] — stateless é o pré-requisito arquitetural
- [[load-balancer]] — distribui livremente quando os servidores são stateless
- [[sticky-session]] — solução paliativa que adia o problema de estado; antônimo da solução correta
- [[redis]] — destino natural para sessões e dados temporários

## Key sources

- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
- [[wiki/sources/10-conceitos-fundamentais-backend]] — mesmo argumento com exemplo de sessão e job em andamento: "uma sessão que existia na máquina A não vai existir na máquina B"
