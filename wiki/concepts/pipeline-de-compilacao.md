---
type: concept
title: "Pipeline de Compilação"
aliases: ["compilation pipeline", "fases do compilador", "GCC phases"]
date_created: 2026-05-02
date_updated: 2026-05-02
source_count: 1
tags: [compilacao, gcc, toolchain, sistemas, assembly]
skill: lang-systems
status: stable
---

# Pipeline de Compilação

O que chamamos de "compilar um programa" é na verdade um pipeline de 4 fases distintas. Compiladores como o GCC expõem cada fase individualmente — é possível entrar ou sair do pipeline em qualquer ponto.

## As 4 Fases (GCC como referência)

```
Código Fonte (.c)
      │
      ▼
┌─────────────────┐
│ 1. Pré-processamento │  → Remove comentários, expande macros,
│    (cpp)         │     resolve #include (copia o conteúdo do header)
└─────────────────┘
      │ (.i — ainda C, mas processado)
      ▼
┌─────────────────┐
│ 2. Compilação    │  → Traduz C pré-processado para assembly
│    (cc1)         │     (instruções legíveis, não código de máquina)
└─────────────────┘
      │ (.s — assembly)
      ▼
┌─────────────────┐
│ 3. Montagem      │  → Traduz assembly para código de máquina (0s e 1s)
│    (as)          │     Resultado: object file — ainda não executável
└─────────────────┘
      │ (.o — object file)
      ▼
┌─────────────────┐
│ 4. Linking       │  → Combina múltiplos object files num executável
│    (ld)          │     Resolve endereços de funções externas
└─────────────────┘
      │ (executável)
```

## Mito Derrubado

Um compilador não converte necessariamente código-fonte direto para código de máquina. Muitos compiladores geram representações intermediárias — assembly, bytecode, ou até outra linguagem. O GCC passa por assembly antes de chegar a código de máquina.

## Plugabilidade

Cada fase é um programa separado e plugável. Isso permite:

- Alimentar o pipeline com um arquivo `.s` (assembly escrito à mão) — o GCC monta e linka normalmente
- Parar o processo numa fase específica (`-S` para parar em assembly, `--save-temps` para ver todos os intermediários)
- Misturar languages: C e Fortran geram object files separados → linker une tudo

## Relevância para Multi-Linguagem

O ponto de encontro entre linguagens é o [[concepts/object-file]] — formato binário neutro que o linker entende. Linguagens diferentes geram object files compatíveis para a mesma arquitetura, permitindo que o [[concepts/toolchain]] as combine.

## Key Sources

- [[sources/como-multiplas-linguagens-vivem-num-unico-binario]]
