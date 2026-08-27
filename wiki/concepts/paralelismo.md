---
type: concept
title: "Paralelismo"
aliases: ["parallelism", "execução paralela", "multicore", "multithreading"]
date_created: 2026-06-26
date_updated: 2026-08-27
source_count: 2
tags: [cs-fundamentals, lang-systems, paralelismo, concorrencia, multicore, performance, hpc]
skill: cs-fundamentals
status: draft
---

# Paralelismo

**Executar múltiplas tarefas ao mesmo tempo** — literalmente, em instantes físicos simultâneos. Requer múltiplos recursos de processamento (cores, CPUs, GPUs, máquinas).

## Diferença fundamental de [[concorrencia]]

| | [[concorrencia]] | Paralelismo |
|---|---|---|
| **O que faz** | Gerencia múltiplas tarefas | Executa múltiplas tarefas |
| **Momento** | Alterna entre tarefas | Simultâneo |
| **Requisito** | 1 processador basta | Múltiplos cores obrigatórios |
| **Analogia** | Cozinheiro sozinho | Dois cozinheiros |

Concorrência é sobre **estrutura**. Paralelismo é sobre **execução**.

## Formas de paralelismo

| Tipo | Exemplo | Onde aparece |
|---|---|---|
| **Thread-level** | Java threads em multicore | Servidores, processamento de dados |
| **SIMD** | Instrução processa 8 floats de uma vez | Álgebra linear, ML, codecs |
| **GPU** | Milhares de cores simples em paralelo | Treinamento de modelos, rendering |
| **Distributed** | Vários servidores processando shards | MapReduce, Spark |
| **Pipeline** | Estágios sobrepostos (decode+execute+write) | CPUs modernas |

## O limite: Lei de Amdahl

Se 90% do programa é paralelizável, o speedup máximo com infinitos processadores é 10×. O 10% serial cria um gargalo inevitável.

```
speedup = 1 / (serial_fraction + parallel_fraction / N)
```

## Paralelismo não resolve race conditions

Adicionar mais threads sem sincronização cria mais oportunidades de [[race-condition]]. Mais paralelismo → mais coordenação necessária ([[mutex]], [[deadlock]]).

## Computação de alto desempenho (HPC) como motivação para baixo nível

[[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]] cita **computação de alto desempenho (HPC)** — GPU, multicore, comunicação entre múltiplos nós via **MPI/OpenMPI** — como uma das motivações concretas para se aprofundar em programação de baixo nível e em [[wiki/concepts/arquitetura-de-computadores]], ao lado de [[wiki/concepts/sistemas-operacionais]] e [[wiki/concepts/sistemas-embarcados]]. A fonte não aprofunda tecnicamente o tema, mas o cita como área de atuação profissional do próprio autor, exigindo algoritmos paralelos e frameworks específicos.

## Relação com outros conceitos

- [[concorrencia]] — o par conceitual obrigatório; muita gente confunde os dois
- [[thread]] — o mecanismo que habilita paralelismo em um processo
- [[mutex]] — necessário quando threads paralelas compartilham estado
- [[deadlock]] — patologia que ocorre quando a coordenação de threads paralelas falha

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]] — HPC (GPU, multicore, MPI/OpenMPI) como motivação para baixo nível
