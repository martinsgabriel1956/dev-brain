---
type: concept
title: "JavaSpaces"
aliases: ["Java Spaces"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_count: 1
tags: [java, jini, sistemas-distribuidos, coordenacao, tuple-space]
skill: tech-mentor-backend
status: stub
---

# JavaSpaces

Especificação de serviço que implementa o modelo [[wiki/concepts/tuple-space|tuple space]]/[[wiki/concepts/object-space|Object Space]] para objetos Java: um mecanismo de troca e coordenação de objetos distribuído, onde peers se comunicam e coordenam compartilhando estado. Parte da tecnologia **Jini** da Sun Microsystems ([[wiki/entities/ken-arnold|Ken Arnold]] foi o engenheiro líder), que não foi um sucesso comercial — JavaSpaces sobrevive como tecnologia de **nicho**, usada principalmente em serviços financeiros e telecomunicações, focada em baixa latência/alta performance mais do que cache confiável de objetos.

## API mínima

Três operações sobre uma `Entry` (objeto compartilhável):

- `write(entry, txn, lease)` — publica a entry no espaço, com um *lease* (TTL)
- `read(template, txn, timeout)` — lê uma entry que casa com o template, **sem remover**
- `take(template, txn, timeout)` — lê e **remove** — é essa operação atômica que produz [[wiki/concepts/object-space#exclusão mútua embutida|exclusão mútua]]

## Padrão de uso: Master-Worker

O padrão de software mais comum em JavaSpaces é o [[wiki/concepts/master-worker-pattern|Master-Worker]]: um Master distribui unidades de trabalho para o espaço, e Workers genéricos leem, processam e escrevem os resultados de volta. Ambientes típicos têm múltiplos espaços, masters e workers.

## Key sources

- [[wiki/sources/tuple-space-wikipedia]] — especificação, exemplo de código completo (write/read/take), contexto Jini/Sun, citação de Bill Joy
