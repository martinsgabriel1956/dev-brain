---
type: concept
title: "Comunicação Síncrona"
aliases: ["synchronous communication", "chamada síncrona", "request-response bloqueante"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [comunicacao-sincrona, rest, acoplamento, resiliencia, arquiteturas-distribuidas]
skill: tech-mentor-backend
status: stub
---

# Comunicação Síncrona

Modelo em que um serviço chama outro e **espera (bloqueado)** a resposta para prosseguir. Resposta imediata, simples e intuitiva (ex.: REST/HTTP entre microsserviços).

**Armadilhas apontadas** em [[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]]: (1) **alto acoplamento** — alteração num lado afeta o outro; (2) **baixa resiliência** — se o serviço chamado cair ou ficar lento, o chamador degrada junto. Exemplo do vídeo: serviço externo de autenticação/autorização consultado a cada requisição.

É a forma concreta de [[wiki/concepts/temporal-coupling]] (A precisa que B esteja no ar *agora*). Mitigações sem trocar de modelo (timeout, [[wiki/concepts/circuit-breaker]]) [skill: tech-mentor-backend] não são discutidas no vídeo. O autor promete um vídeo dedicado aos benefícios da síncrona — não ingerido.

**Regra prática** [skill: tech-mentor-backend, `references/architecture-eda-patterns.md`]: se o usuário precisa do resultado para continuar, síncrono; se pode seguir sem ele, assíncrono.

Contraste: [[wiki/concepts/comunicacao-assincrona]].

## Key sources

- [[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]] — definição, exemplo de autenticação e tabela comparativa com a assíncrona
