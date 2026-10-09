---
type: concept
title: "Contenção de Lock entre Leitura e Escrita"
aliases: ["lock contention", "consultas presas por transação aberta", "desbalanço leitura/escrita"]
date_created: 2026-09-30
date_updated: 2026-10-09
source_count: 2
tags: [banco-de-dados, lock, concorrencia, cqrs, escalabilidade]
skill: tech-mentor-backend
status: stub
---

# Contenção de Lock entre Leitura e Escrita

## TL;DR

Quando leitura e escrita disputam o mesmo banco e a proporção de carga é muito desbalanceada (muito mais consulta que alteração, ou picos de um dos lados em certos períodos do dia/mês), consultas podem ficar presas esperando **locks** liberados por transações abertas, degradando o banco e, por consequência, a aplicação. É o problema motivador apresentado para adotar [[wiki/concepts/cqrs]] em [[wiki/sources/cqrs-desbalanco-leitura-escrita-banco-de-leitura-eventos]].

## Por que acontece

- Uma única solução trata leitura e escrita de forma unificada, no mesmo banco e mesma estrutura: para escalar é preciso escalar **tudo**, não só o lado sobrecarregado (segundo a fonte).
- Transações de escrita longas seguram locks; consultas que precisam dos mesmos dados esperam.

## Ressalva [skill]

O quanto leitura bloqueia de fato depende do SGBD e do nível de isolamento: bancos com MVCC (ex.: [[wiki/concepts/postgresql]]) normalmente não fazem leitores esperarem escritores; o cenário descrito é mais típico de leitura por lock (ex.: [[wiki/concepts/sql-server]] em `READ COMMITTED` sem snapshot). Ver [[wiki/concepts/isolation-levels]]. Antes de separar bancos, vale considerar isolamento por snapshot, [[wiki/concepts/read-replicas]], índices e transações mais curtas; CQRS com banco separado é a opção de maior custo ([[wiki/sources/cqrs-martin-fowler]]).

## Saída apresentada

Separar o modelo de escrita (banco relacional, regras de domínio) do de leitura ([[wiki/concepts/read-model]] desnormalizado), sincronizados por eventos ([[wiki/concepts/event-handler]]) com [[wiki/concepts/eventual-consistency]].

## Key sources

- [[wiki/sources/cqrs-desbalanco-leitura-escrita-banco-de-leitura-eventos]] — enuncia o problema (consultas presas por transação aberta) e a saída via CQRS com banco de leitura separado

## Key sources (adição 2026-10-09)

- [[wiki/sources/cqrs-quando-faz-sentido-cqs-bernardo-lobato]] — exemplo do contador de views: tabela travada por escrita impedindo o acesso de quem quer ver o vídeo; modelo de escrita para alta frequência + modelo de leitura simples
