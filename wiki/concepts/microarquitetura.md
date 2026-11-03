---
type: concept
title: "Microarquitetura"
aliases: ["microarchitecture", "uarch", "arch", "execução fora de ordem", "out-of-order execution"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 1
tags: [cs-fundamentals, hardware, cpu, pipeline, cache, performance]
skill: cs-fundamentals
status: stub
---

# Microarquitetura

Como um processador implementa uma [[wiki/concepts/isa-instruction-set-architecture|ISA]]. A ISA define o conjunto de instruções; a microarquitetura é a estratégia interna para executá-lo: cache, pipeline, front end, back end e execução fora de ordem ([[wiki/sources/por-que-cpus-nao-evoluem-como-antes-power-wall-gpus]]). Por isso, dois chips Arm ou dois x86 podem ter desempenho muito diferente rodando o mesmo binário (inferência da wiki).

## Onde estaria a inovação

Com a frequência limitada pelo [[wiki/concepts/power-wall]], a fonte coloca a inovação de CPU aqui, com a Apple de exemplo, e diz que o processo fabril muda pouco. O autor avisa que não sabe os detalhes. [external] A comparação mistura papéis diferentes: a [Arm só licencia propriedade intelectual](https://en.wikipedia.org/wiki/Arm_Holdings) e a Apple [fabrica na TSMC](https://www.iphoneincanada.ca/2022/12/29/apple-supplier-tsmc-starts-making-next-gen-3nm-chips/). Quanto do ganho vem de cada fator continua em aberto.

## Relação com outros conceitos

- [[wiki/concepts/arquitetura-de-computadores]]: área mais ampla, com pipeline, caches e branch prediction.
- [[wiki/concepts/multicore]]: a outra resposta da CPU ao mesmo limite.
- [[wiki/concepts/retrocompatibilidade-x86]]: a ISA fica estável enquanto a implementação muda por baixo (inferência da wiki).

## Key sources

- [[wiki/sources/por-que-cpus-nao-evoluem-como-antes-power-wall-gpus]]
