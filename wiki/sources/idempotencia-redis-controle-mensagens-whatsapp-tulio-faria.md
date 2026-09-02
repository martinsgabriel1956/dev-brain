---
type: source
title: "Idempotência com Redis — Controle de Mensagens WhatsApp (Tulio Faria, DevPleno)"
aliases: ["idempotencia redis whatsapp", "sendSms idempotente", "redis SET GET EX idempotencia"]
date_created: 2026-09-02
date_updated: 2026-09-02
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/idempotencia-redis-controle-mensagens-whatsapp-tulio-faria.md
source_url: ""
author: "Tulio Faria (DevPleno)"
date_published: ""
date_ingested: 2026-09-02
source_count: 0
tags: [idempotencia, redis, whatsapp, sms, notificacao, sistemas-distribuidos, ioredis, deduplicacao]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Tulio Faria (canal DevPleno) explica idempotência a partir da etimologia ("idem" + "potência") e do caso de uso real do seu SaaS: mensagens enviadas do backend para um bot de WhatsApp não-oficial, onde timeouts na comunicação levavam a reenvios sem confirmação se a mensagem original chegou. Demonstra em código (Node.js + `ioredis`) uma implementação usando `redis.set(key, value, "EX", ttl, "GET")` — o flag `GET` faz o Redis retornar o valor anterior da chave antes de sobrescrever, permitindo checar-e-marcar atomicamente numa única chamada. A chave de idempotência é composta por telefone + tipo de mensagem + hash da mensagem, com janela de deduplicação de minutos (5 min no caso real; 60s na demo).

## Key Claims

**Claim:** O trabalho central de implementar idempotência é identificar *quais características da requisição* a tornam única — não existe fórmula genérica.
**Evidence:** Exemplo da maquininha de cartão: mesma maquininha + mesmo valor + mesmo cartão identificam a transação como repetida. No bot de WhatsApp: telefone do destinatário + tipo da mensagem + hash do conteúdo. Em pagamentos (Stripe): um ID fornecido pelo serviço já cumpre esse papel.
**Confidence:** alta — consistente com o padrão geral já registrado em [[wiki/concepts/idempotencia]] (seção "Identidades de Negócio por Produto").

**Claim:** `redis.set(key, val, "EX", ttl, "GET")` resolve check-then-set atomicamente numa única chamada — mais simples que fazer `GET` seguido de `SET`.
**Evidence:** A flag `GET` do comando `SET` do Redis (desde Redis 6.2) retorna o valor anterior da chave enquanto sobrescreve/cria com o novo valor e TTL — dispensa uma chamada separada de leitura e evita a janela de corrida entre ler e escrever em duas operações distintas.
**Confidence:** alta — coerente com o padrão `SET NX EX` já documentado como base de locks/dedup no ecossistema Redis; aqui a variante troca `NX` (não sobrescreve se já existe) por `GET` (sempre escreve, mas devolve o valor antigo para decisão da aplicação).

**Claim:** A janela de tempo (TTL) que define "a mesma requisição" é uma decisão de produto, não puramente técnica — no caso do autor, 5 minutos para mensagens de WhatsApp.
**Evidence:** "não é para mandar de verdade essa mensagem... se chegar mais de uma mensagem com isso aqui tudo igual dentro de 5 minutos". Reforça claim já registrada em [[wiki/concepts/idempotencia]] ("A definição de quais campos entram no hash — e qual a janela de tempo... é uma decisão de negócio, não só técnica").
**Confidence:** alta, mas é relato de decisão de produto específica (não um valor universal).

**Claim:** Timeout de comunicação entre dois sistemas não garante saber se o efeito colateral (mensagem enviada) realmente não aconteceu — motivando idempotência em vez de apenas confiar no timeout.
**Evidence:** "a gente dava timeout, mas a mensagem ia" — o SaaS do autor não conseguia confirmar entrega via WhatsApp e por isso reenviava, arriscando duplicidade sem o controle de idempotência.
**Confidence:** alta — caso concreto do mesmo argumento já registrado em [[wiki/concepts/idempotencia]] ("Por que o Timeout Sozinho Não Basta").

**Claim:** Idempotência também serve para limitar volume de notificações a um mesmo usuário (rate-limit implícito), não só para deduplicar retries.
**Evidence:** Exemplo citado: controle de quantidade de SMS enviados a um usuário (usuários americanos recebem mais SMS) usando o mesmo mecanismo de chave+TTL para não "floodar" a pessoa.
**Confidence:** média — uso adjacente a idempotência estrita (mais próximo de rate limiting por destinatário do que de deduplicação de uma operação idêntica), mas apresentado pelo autor como a mesma técnica.

## Entities & Concepts Touched

- [[wiki/concepts/idempotencia]]
- [[wiki/concepts/retry-backoff]]
- [[wiki/concepts/notification-system]] (adjacente — controle de volume de SMS)
- [[wiki/entities/tulio-faria]]

## Open Questions

- O vídeo não aborda o caso de corrida entre duas requisições concorrentes chegando ao mesmo tempo (`SET ... GET` não é `NX` — sempre sobrescreve; não há lock explícito contra duas chamadas simultâneas). Isso é diferente da resolução por `INSERT ... ON CONFLICT` já registrada em [[wiki/concepts/idempotencia]] ("Resolvendo a Corrida"). Não fica claro se o autor considerou esse cenário no bot de WhatsApp.
- Como o autor lida com falhas do próprio Redis (SPOF) nesse fluxo — não mencionado no vídeo.

## Raw Quotes

> "O grande trabalho que você vai ter na hora de definir idempotência é exatamente identificar quais características você vai utilizar daquela requisição para saber se ela é repetida ou não."

> "A idempotência não é para mandar de verdade essa mensagem para o WhatsApp [se] chegar mais de uma mensagem com isso aqui tudo igual dentro de 5 minutos."

> "Ele [o Redis] dá um GET antes e seta depois" — descrevendo o flag `GET` do comando `SET`.
