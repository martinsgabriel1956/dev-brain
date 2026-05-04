---
type: concept
title: "Object File"
aliases: ["arquivo objeto", ".o file", "object code"]
date_created: 2026-05-02
date_updated: 2026-05-02
source_count: 1
tags: [compilacao, linking, sistemas]
skill: lang-systems
status: stable
---

# Object File

Produto da fase de montagem no [[concepts/pipeline-de-compilacao]]. Contém código de máquina para as funções do arquivo-fonte, mas **ainda não é executável** — os endereços finais das funções ainda não foram resolvidos.

## O que contém

- Código de máquina das funções definidas no arquivo
- Tabela de símbolos (nomes de funções e variáveis exportadas/importadas)
- Referências não resolvidas para funções externas (ex: `printf` da stdlib)
- Metadados de debug (quando compilado com `-g`)

## Por que não é executável ainda

O linker precisa resolver dois problemas:

1. **Endereços:** onde cada função ficará no binário final (determinado só quando todos os object files são combinados)
2. **Referências externas:** funções como `printf` vivem em outra biblioteca — o linker localiza e conecta

## Extensões

- Unix/Linux: `.o`
- Windows: `.obj`
- Bibliotecas estáticas são coleções de object files: `.a` (Unix) / `.lib` (Windows)

## Ponto de Interoperabilidade

O object file é o **formato neutro** que permite múltiplas linguagens coexistirem. C, Rust, Fortran e assembly escrito à mão todos geram object files para a mesma arquitetura. O [[concepts/static-linking]] e [[concepts/dynamic-linking]] operam sobre esses arquivos.

## Key Sources

- [[sources/como-multiplas-linguagens-vivem-num-unico-binario]]
