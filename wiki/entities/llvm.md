---
type: entity
title: "LLVM"
aliases: ["Low Level Virtual Machine"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [cs-fundamentals, linguagens-de-programacao, compiladores, infraestrutura]
skill: cs-fundamentals
status: stub
---

# LLVM

Infraestrutura de compilador reutilizável. Uma linguagem nova pode gerar sua própria IR (representação intermediária) e delegar ao LLVM a otimização e a geração de código de máquina para múltiplas arquiteturas de CPU, em vez de implementar um backend de compilação nativo do zero. Usado como backend por Rust e Swift, entre outras linguagens.

## Relação com outros conceitos

- [[wiki/concepts/compilador]] — LLVM entra na etapa de otimização + geração de código do pipeline de compilação, como alternativa a escrever esse backend manualmente
- [[wiki/concepts/pipeline-de-compilacao]] — modelo de fases plugáveis (frontend gera IR → LLVM assume da IR em diante) é o mesmo princípio de pipeline discutido nessa página, aplicado numa ferramenta real

## Key sources

- [[wiki/sources/como-criar-uma-linguagem-de-programacao]]
