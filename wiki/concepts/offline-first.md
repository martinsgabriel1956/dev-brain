---
type: concept
title: "Offline-First"
aliases: ["offline first", "servidor como fonte da verdade"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_count: 1
tags: [offline-first, local-first, cache, system-design, arquitetura]
skill: tech-mentor-system-design
status: draft
---

# Offline-First

**Padrão arquitetural em que o aplicativo funciona sem rede, mas o servidor continua sendo a autoridade sobre o dado.** O local (ex.: IndexedDB) é apenas um cache subordinado: a aplicação grava ali para permitir edição/leitura offline, mas a escrita só é considerada definitiva quando a requisição chega ao servidor e é aceita. Se a rede cai, o usuário edita normalmente; quando a rede volta, a aplicação envia a mudança pro servidor, que valida e persiste.

Não confundir com [[wiki/concepts/local-first]] — as duas arquiteturas funcionam sem rede, o que não diferencia uma da outra. A diferença real é qual cópia do dado é a autoridade: no offline-first, é o servidor; no local-first, é o próprio dispositivo (réplica primária).

## Consequência prática: o que sobra se o serviço acabar

Se a empresa dona do aplicativo fecha, o cache local não tem mais nenhuma fonte para sincronizar — o dado efetivamente se perde, mesmo que ainda esteja fisicamente no disco do usuário, porque ele nunca foi tratado como autoritativo por si só.

## Quando é a escolha certa

Domínios que dependem de uma autoridade central por natureza do próprio negócio: aplicação bancária, e-commerce, rede social, app de corrida. Nesses casos, quer-se resiliência a queda de rede — não posse do dado pelo usuário.

## Relação com outros conceitos

- [[wiki/concepts/local-first]] — arquitetura oposta: dispositivo local como réplica primária e autoritativa
- [[wiki/concepts/cap-theorem]] — offline-first prioriza que a escrita definitiva dependa do servidor, análogo a priorizar consistência (C) sobre disponibilidade de escrita imediata

## Key sources

- [[wiki/sources/local-first-vs-offline-first]]
