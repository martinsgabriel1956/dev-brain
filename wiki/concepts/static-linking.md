---
type: concept
title: "Static Linking"
aliases: ["linkagem estática", "static library", "biblioteca estática"]
date_created: 2026-05-02
date_updated: 2026-05-02
source_count: 1
tags: [linking, compilacao, sistemas]
skill: lang-systems
status: stable
---

# Static Linking

Estratégia de linking onde o código de máquina das funções de bibliotecas externas é **copiado diretamente para dentro do executável final**. O resultado é um binário autocontido.

## Como funciona

O linker localiza cada função referenciada nas bibliotecas estáticas (`.a` / `.lib`), extrai o código correspondente e o insere no executável. O binário resultante não depende de nada externo para rodar.

## Vantagens

- **Portabilidade total:** o executável roda em qualquer máquina da mesma arquitetura, sem dependências externas
- **Sem conflito de versão:** a versão da biblioteca usada na compilação é exatamente a que roda em produção
- **Startup instantâneo:** nada a carregar do disco em runtime

## Desvantagens

- **Tamanho maior:** cada binário carrega sua cópia de cada função que usa
- **Atualização custosa:** corrigir uma vulnerabilidade numa biblioteca exige recompilar e redistribuir todos os programas que a usam
- **Múltiplas cópias em memória:** se 100 processos usam a mesma lib, 100 cópias idênticas ficam na RAM

## Quando usar

- Binários de distribuição que precisam ser autocontidos (containers FROM scratch, binários Alpine musl)
- Tooling de CLI onde portabilidade é prioridade
- Rust com `CGO_ENABLED=0` / Go com `CGO_ENABLED=0` para builds estáticos

## Contraste

Ver [[concepts/dynamic-linking]] para a alternativa que compartilha o código entre processos.

## Key Sources

- [[sources/como-multiplas-linguagens-vivem-num-unico-binario]]
