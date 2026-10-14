---
type: concept
title: "ISA — Instruction Set Architecture"
aliases: ["ISA", "conjunto de instruções", "arquitetura de conjunto de instruções"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [lang-systems, cs-fundamentals, hardware, assembly, cpu]
skill: lang-systems
status: draft
---

# ISA — Instruction Set Architecture

Especificação do que a CPU faz e como: **conjunto de instruções, modelo de endereçamento, classes de registradores (ex.: vetoriais), extensões** (ex.: coprocessador de ponto flutuante, que nem toda CPU tem) — ou, no mínimo, o modelo mental necessário para escrever código para ela. [[wiki/concepts/assembly]] é a **representação mais baixa possível** da ISA e só é portável se a arquitetura também for (x86 32 bits roda em x64 por ser feito sobre ele; não roda em ARM ou RISC-V) — ver [[wiki/sources/por-que-c-e-alto-nivel-abstracao-portabilidade-hardware]].

Variar de ISA (x86, ARM, RISC, RISC-V) é o que torna necessária a [[wiki/concepts/portabilidade-de-codigo-entre-arquiteturas]] por meio de linguagens de [[wiki/concepts/alto-nivel-vs-baixo-nivel|alto nível]]; a compatibilidade entre gerações é tema de [[wiki/concepts/retrocompatibilidade-x86]]. Contexto: [[wiki/concepts/arquitetura-de-computadores]]. [skill: lang-systems] `systems-emerging-topics-2026.md` cobre RISC-V.

## Key sources

- [[wiki/sources/por-que-c-e-alto-nivel-abstracao-portabilidade-hardware]]
