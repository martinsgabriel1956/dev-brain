---
type: concept
title: "Comunicação Síncrona"
aliases: ["synchronous communication", "chamada síncrona", "request-response bloqueante"]
date_created: 2026-09-30
date_updated: 2026-10-06
source_count: 5
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

## Custo: monolito distribuído

Cadeia de HTTP entre serviços com dependências externas vira [[wiki/concepts/monolito-distribuido]]; quando ainda vale: [[wiki/concepts/quando-usar-mensageria]]. [[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]]

## Key sources

- [[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]] — definição, exemplo de autenticação e tabela comparativa com a assíncrona
- [[wiki/sources/arquitetura-distribuida-introducao-historico-desafios-bernardo-lobato]] — escolha síncrono vs. assíncrono apontada como decisão a tomar 'o quanto antes' em arquitetura distribuída
- [[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]] — cadeia HTTP Pedidos→Pagamentos→Nota→Estoque→E-mail
- [[wiki/sources/rag-spring-ai-microagente-recomendacao-michele-brito]] — gatilho HTTP síncrono de um [[wiki/concepts/microagente]], alternativa à via por eventos

## Key sources (adição 2026-10-06)

- [[wiki/sources/introducao-arquitetura-de-software-conceitos-decisoes-kiper-academy]] — pergunta-guia "preciso do resultado agora?"; verificação de CNH/CPF de até 30 min força o assíncrono.
