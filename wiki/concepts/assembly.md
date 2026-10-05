---
type: concept
title: "Assembly"
aliases: ["linguagem de montagem", "assembler", "opcode"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [lang-systems, baixo-nivel, assembly, opcode, cs-fundamentals]
skill: lang-systems
status: stub
---

# Assembly

Representação textual (mnemônicos) das instruções de máquina de uma CPU; cada instrução corresponde diretamente a um **opcode** (os bytes que o processador executa), então assembly e opcode são **intercambiáveis** por montagem/desmontagem — ponto feito em [[wiki/sources/c-linguagem-do-futuro-ia-assembly-opcode-safe-source-ricardo-albuquerque]]. Dependente da arquitetura (x86, ARM…), ao contrário de [[wiki/concepts/linguagem-c]], que o [[wiki/concepts/compilador]] traduz para ele.

## Legibilidade (relato de [[wiki/entities/ricardo-albuquerque]])

Possível de inspecionar (device drivers, DLLs sem código-fonte, avaliação de segurança — [[wiki/concepts/engenharia-reversa]]), mas "pouquíssimas pessoas" conseguem; opcode cru é ilegível. Base do argumento em [[wiki/concepts/legibilidade-humana-do-codigo-gerado-por-ia]]. Usos atuais: drivers, kernels, boot, trechos críticos [skill: lang-systems, `c-cpp.md`: "hardware drivers → C/Assembly"].

## Key sources

- [[wiki/sources/c-linguagem-do-futuro-ia-assembly-opcode-safe-source-ricardo-albuquerque]] — assembly como degrau abaixo do C e relação com opcode
