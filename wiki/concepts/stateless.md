---
type: concept
title: "Stateless"
aliases: ["servidor stateless", "sem estado", "stateless server", "stateless architecture"]
date_created: 2026-06-26
date_updated: 2026-08-14
source_count: 4
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

## Access Token Stateless vs. Refresh Token Stateful

O mesmo trade-off aparece na dupla access token / refresh token: manter o access token stateless evita validação central a cada requisição (essencial em alto volume — 1000 req/s significaria 1000 validações no banco por segundo se fosse stateful), enquanto o refresh token compensa isso sendo stateful (verificável e revogável no authorization server), pois é usado com frequência muito menor. Ver [[wiki/concepts/refresh-token-rotation]].

## Relação com outros conceitos

- [[escalabilidade-horizontal]] — stateless é o pré-requisito arquitetural
- [[load-balancer]] — distribui livremente quando os servidores são stateless
- [[sticky-session]] — solução paliativa que adia o problema de estado; antônimo da solução correta
- [[redis]] — destino natural para sessões e dados temporários
- [[wiki/concepts/jwt]] — access token stateless vs. refresh token stateful como aplicação do mesmo trade-off em autenticação

## Key sources

- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
- [[wiki/sources/10-conceitos-fundamentais-backend]] — mesmo argumento com exemplo de sessão e job em andamento: "uma sessão que existia na máquina A não vai existir na máquina B"
- [[wiki/sources/escalar-para-um-milhao-de-usuarios]] — se o login fica num servidor e o próximo request cai em outro, o usuário aparece deslogado; sessões e preferências vão para um NoSQL externo, que não pode viver dentro de nenhum servidor web
- [[wiki/sources/refresh-token-pattern-access-token-de-curta-duracao]] — access token stateless vs. refresh token stateful como o mesmo trade-off aplicado à autenticação
