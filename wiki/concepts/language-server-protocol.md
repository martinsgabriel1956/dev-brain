---
type: concept
title: "Language Server Protocol (LSP)"
aliases: ["LSP", "language server"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [cs-fundamentals, linguagens-de-programacao, tooling, editores, microsoft]
skill: cs-fundamentals
status: stub
---

# Language Server Protocol (LSP)

Protocolo criado pela Microsoft que padroniza a comunicação entre editores de código e "servidores" específicos de cada linguagem. Antes do LSP, cada editor precisava implementar suporte dedicado para cada linguagem (combinação N editores × M linguagens); com o LSP, cada linguagem implementa um servidor uma única vez e qualquer editor compatível (VS Code, Neovim, IntelliJ) ganha suporte automaticamente.

## O que o LSP habilita

- Autocomplete
- Erros inline (diagnostics)
- "Ir para definição" / "Ir para referências"
- Refatoração assistida pelo editor

## Por que importa para uma linguagem nova

Uma linguagem tecnicamente sólida sem tooling de editor tem barreira de adoção alta — ninguém quer escrever código sem autocomplete ou detecção de erro em tempo real. O LSP reduz drasticamente o custo de dar essa experiência, porque a linguagem não precisa negociar suporte editor por editor.

## Relação com outros conceitos

- [[wiki/concepts/standard-library-e-ecossistema]] — LSP é uma peça do tooling que, junto com package manager, formatter e linter, determina a experiência de dia a dia de quem usa a linguagem

## Key sources

- [[wiki/sources/como-criar-uma-linguagem-de-programacao]]
