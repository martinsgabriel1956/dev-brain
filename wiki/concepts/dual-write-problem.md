---
type: concept
title: "Dual Write Problem (Bug da Escrita Dupla)"
aliases: ["bug da escrita dupla", "dual write", "problema da escrita dupla"]
date_created: 2026-08-27
date_updated: 2026-09-14
source_count: 2
tags: [dual-write-problem, cqrs, event-driven-architecture, outbox-pattern, consistencia, sistemas-distribuidos]
skill: tech-mentor-backend
status: stub
---

# Dual Write Problem (Bug da Escrita Dupla)

Problema de atualizar dois sistemas (tipicamente: um banco de dados e um broker de eventos) de forma consistente sem uma transação distribuída. Se a escrita no banco e a publicação do evento não são atômicas, uma pode ter sucesso e a outra falhar — gerando inconsistência entre o estado persistido e o que foi comunicado a outros consumidores.

## Onde Aparece: Sincronização de CQRS via Eventos

[[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] nomeia esse risco diretamente ao descrever a sincronização write→read via [[wiki/concepts/event-driven-architecture|eventos]] em [[wiki/concepts/cqrs]]: o serviço de escrita grava na base **e** posta um evento — duas operações separadas. Se divergirem, o usuário passa a ver, na leitura, uma informação diferente da que ele efetivamente salvou. A fonte cita o problema nominalmente mas não detalha a solução, remetendo a outro vídeo do canal.

## Solução: Transactional Outbox

A solução padrão é o [[wiki/concepts/outbox-pattern]]: escrever o evento numa tabela outbox dentro da **mesma transação local** que grava o estado, e usar CDC (ex. Debezium) para publicar o evento a partir dessa tabela de forma assíncrona e garantida — eliminando a necessidade de uma transação distribuída entre banco e broker.

## Onde Também Aparece: Desafio Clássico de Entrevista de Programação

[[wiki/sources/transactional-outbox-pattern-entrevista-cadastro-usuario]] nomeia e detalha o mesmo problema a partir de um exemplo canônico de entrevista de backend — "cadastre um usuário e envie um e-mail de boas-vindas" — e mostra por que a correção intuitiva (envolver a chamada ao broker numa transação de banco) não resolve: a transação local não cobre a chamada externa, então a aplicação pode enviar a mensagem e cair antes do `COMMIT` no banco, deixando um usuário "fantasma" que recebeu e-mail mas não existe na base. A fonte generaliza o problema para qualquer par escrita-no-banco + outra-coisa (cache, Elasticsearch, mensageria, chamada a terceiros), não apenas CQRS.

## Key Sources

- [[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] — citação nominal do bug da escrita dupla como risco de sincronizar CQRS via eventos
- [[wiki/sources/transactional-outbox-pattern-entrevista-cadastro-usuario]] — versão didática completa do problema com exemplo de entrevista, incluindo por que uma transação de banco local não basta para cobrir a chamada externa
