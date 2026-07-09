---
type: source
title: "Double Spend / Double Submit"
aliases: ["double spend", "double submit", "request duplicado"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 0
tags: [idempotencia, double-spend, double-submit, prg-pattern, unique-constraint, backend]
skill: tech-mentor-backend
status: draft
source_file: raw/double-spend-double-submit.md
source_url:
author:
date_published:
date_ingested: 2026-07-09
---

# Double Spend / Double Submit

## TL;DR

Double spend (transações) e double submit (formulários) são o mesmo problema visto por ângulos diferentes: um request se duplica por bug, duplo clique acidental, ou abuso deliberado, e o resultado final pode ser gravado duas vezes no banco. A solução robusta combina camadas: desabilitar o botão de submit no frontend (só resolve o caso acidental), redirect após POST (padrão PRG, também só cobre o usuário bem-intencionado), Idempotency Key gerada a partir de um hash dos campos do request e armazenada em storage compartilhado entre instâncias (Redis), e Unique Constraint no banco de dados quando existe um campo genuinamente único. Nenhuma camada isolada resolve o problema contra um atacante deliberado — só a combinação de servidor + banco de dados garante isso.

## Key Claims

| Claim | Evidência |
|---|---|
| Desabilitar o botão de submit no frontend não impede um usuário malicioso | Um atacante pode copiar o request de rede e reenviá-lo via script, ignorando o frontend inteiramente |
| Redirect após POST (303, padrão PRG) evita reenvio acidental porque o navegador não reenvia o POST original ao seguir o redirect | Padrão de UX já familiar (ex.: cadastro em lista de e-mail → página de agradecimento) |
| Idempotency Key pode ser gerada pelo servidor como hash dos campos do request, em vez de ser enviada pelo cliente | Se o cliente gera a chave, um atacante pode simplesmente reenviar com uma chave diferente e burlar a dedução |
| A janela de tempo que caracteriza duplicidade é uma decisão de negócio, não só técnica | Dois Pix de R$ 5 em segundos é suspeito; o mesmo valor um dia depois normalmente não é |
| A chave de idempotência não pode viver em memória de um único servidor | Aplicações modernas rodam em múltiplas instâncias/lambdas — o segundo POST pode cair numa instância diferente do primeiro |
| Unique Constraint no banco é a solução mais definitiva, mas só funciona quando existe um campo genuinamente único por regra de negócio | Ex.: `email UNIQUE NOT NULL` numa lista de e-mails; numa transação bancária não há campo naturalmente único — usa-se a própria idempotency key como constraint |

## Conceitos

- [[wiki/concepts/idempotencia]] — página já existente, atualizada com claims desta fonte (geração de chave no servidor vs. cliente, hash de campos, janela de tempo como decisão de negócio)
- [[wiki/concepts/post-redirect-get]] — novo stub criado a partir desta fonte
- [[wiki/concepts/retry-backoff]]

## Entidades Mencionadas

Nenhuma entidade nomeada relevante além do patrocínio do vídeo (Abacus AI), tangencial ao conteúdo técnico e não registrado como entidade da wiki.

## Open Questions

- A fonte não detalha qual mecanismo de lock (ex.: `SET NX`) evita que dois requests concorrentes com a mesma chave de idempotência processem simultaneamente antes do primeiro terminar — o vídeo trata só do caso de replay após a chave já estar armazenada. A referência da skill (`tech-mentor-backend/references/idempotency-patterns.md`) cobre isso com um lock key separado do cache key.
- Não fica claro na fonte como a TTL/expiração da chave de idempotência deveria variar por domínio (o vídeo menciona a necessidade de uma "expiration strategy" mas não propõe valores) — a referência da skill sugere TTLs diferenciados por tipo de operação (pagamento: 30 dias, pedido: 7 dias).

## Key Sources

_Este é o documento primário._
