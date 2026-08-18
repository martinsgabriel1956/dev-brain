---
type: concept
title: "Admission Control"
aliases: ["controle de admissão", "load shedding na entrada", "low watermark high watermark"]
date_created: 2026-08-14
date_updated: 2026-08-14
source_count: 1
tags: [admission-control, back-pressure, filas, rate-limiting, resiliencia, system-design]
skill: tech-mentor-system-design
status: stub
---

# Admission Control

Mecanismo que decide se um novo item de trabalho **entra** no sistema (numa fila, num serviço) ou é rejeitado, com base na capacidade atual. É uma das respostas estruturais ao [[wiki/concepts/back-pressure]]: em vez de deixar a fila crescer sem limite, o próprio ponto de entrada nega admissão quando o sistema está sobrecarregado.

Pode ser implementado no próprio produtor ou como um middleware que intercepta a tentativa de enfileirar um job.

## Técnica: Low Watermark / High Watermark

Uma forma concreta de admission control observada em [[wiki/sources/back-pressure-producer-consumer-filas-bounded-admission-control]]: o produtor monitora periodicamente o tamanho da fila.

- Quando o tamanho ultrapassa o **high watermark** (ex.: 100 jobs), o produtor **pausa** completamente — para de enfileirar novos itens.
- Quando o tamanho cai abaixo do **low watermark** (ex.: 30 jobs), o produtor **retoma** a produção.

Ter dois limiares em vez de um único ponto de corte evita oscilação rápida (*flapping*) entre pausar e retomar — o produtor só volta a produzir quando a fila já drenou uma margem confortável, não assim que cruza de volta o mesmo limite que o pausou.

Na demo com BullMQ + Redis, essa técnica manteve o tamanho da fila oscilando entre ~30 e ~93 itens, evitando o crescimento sem limite observado no exemplo sem controle (lag de 799 itens).

## Relação com outros conceitos

- [[wiki/concepts/back-pressure]] — admission control é uma das estratégias de controle de back pressure, ao lado de bufferizar com limite e descarte com política.
- [[wiki/concepts/rate-limiting]] — rate limit no produtor é uma forma complementar de controle: em vez de rejeitar admissão com base no tamanho da fila, trava a taxa de produção na capacidade do consumidor.
- [[wiki/concepts/fila]] — admission control é o mecanismo que mantém uma fila **bounded** (limitada) em vez de crescer indefinidamente.
- [[wiki/concepts/gargalo]] — decidir o limiar de admission control exige antes identificar corretamente onde está o gargalo do sistema.

## Key Sources

- [[wiki/sources/back-pressure-producer-consumer-filas-bounded-admission-control]] — origem da técnica de low/high watermark demonstrada com BullMQ + Redis
