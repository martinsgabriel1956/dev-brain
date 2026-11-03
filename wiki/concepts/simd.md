---
type: concept
title: "SIMD"
aliases: ["single instruction multiple data", "SIMT", "single instruction multiple threads", "instruções vetoriais"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 1
tags: [cs-fundamentals, hardware, paralelismo, simd, simt, gpu, cpu]
skill: cs-fundamentals
status: stub
---

# SIMD

*Single Instruction, Multiple Data*: uma instrução age sobre vários dados ao mesmo tempo. [[wiki/sources/por-que-cpus-nao-evoluem-como-antes-power-wall-gpus]] o apresenta como a filosofia da [[wiki/concepts/gpu|GPU]]: em vez de executar mais instruções, cada uma faz mais trabalho.

## Não é exclusivo da GPU

[skill: cs-fundamentals] A CPU também tem SIMD, com AVX e NEON, e compiladores tentam vetorizar loops automaticamente (`parallel-distributed-computing.md`, `hardware-for-engineers.md`). O SIMD sozinho, portanto, não distingue CPU de GPU. A fonte não faz essa ressalva.

## SIMT

As GPUs da NVIDIA executam threads em grupos de 32 ([warps](https://cacm.acm.org/research/understanding-throughput-oriented-architectures)). [external] [skill: cs-fundamentals] Quando as threads divergem num `if/else`, a GPU executa os dois caminhos e mascara as threads de cada um, o que custa eficiência. Por isso, código com muitos desvios rende pouco em GPU.

## Relação com outros conceitos

- [[wiki/concepts/paralelismo]]: SIMD é uma das formas de paralelismo listadas lá.
- [[wiki/concepts/multicore]]: paralelismo entre núcleos, que pode ser combinado com SIMD dentro de cada um.

## Key sources

- [[wiki/sources/por-que-cpus-nao-evoluem-como-antes-power-wall-gpus]]
