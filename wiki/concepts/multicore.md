---
type: concept
title: "Multicore"
aliases: ["processador multicore", "multi-core", "múltiplos núcleos", "dual-core"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 1
tags: [cs-fundamentals, hardware, cpu, paralelismo, performance]
skill: cs-fundamentals
status: stub
---

# Multicore

Vários núcleos de execução no mesmo chip. Com a frequência travada pelo [[wiki/concepts/power-wall]], a ideia é aumentar as instruções por segundo com mais processadores, sem encurtar o tempo de cada instrução ([[wiki/sources/por-que-cpus-nao-evoluem-como-antes-power-wall-gpus]]).

## Origem

A fonte diz que o power wall impulsionou o multicore e, com ressalva do próprio autor, que antes tudo era single core. [external] A Intel [trocou o Tejas por dual-core em 2004](https://www.informationweek.com/it-leadership/intel-scraps-tejas-will-focus-on-dual-core-processors). O [IBM POWER4](https://en.wikipedia.org/wiki/POWER4) já tinha dois núcleos em 2001, então o movimento começou antes desse marco.

## Ressalva sobre a fonte

O vídeo diz que o multicore tenta diminuir o tempo de execução de uma instrução, o que contradiz a própria explicação de que ele soma instruções por segundo. Quem reduz o tempo de uma thread é a [[wiki/concepts/microarquitetura]]; mais núcleos só ajudam se o programa for paralelizável (ver Lei de Amdahl em [[wiki/concepts/paralelismo]]). Essa leitura é inferência da wiki.

## Multicore e GPU

| | Multicore | [[wiki/concepts/gpu\|GPU]] |
|---|---|---|
| **Núcleos** | Dezenas, complexos | Milhares, simples |
| **Foco** | Latência de cada thread | Throughput total |

Tabela conforme `parallel-distributed-computing.md`. [skill: cs-fundamentals]

## Key sources

- [[wiki/sources/por-que-cpus-nao-evoluem-como-antes-power-wall-gpus]]
