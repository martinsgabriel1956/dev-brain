---
type: concept
title: "IA gerando binário direto (sem linguagem-fonte)"
aliases: ["ia gera opcode", "ia gera assembly direto", "pular a linguagem"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [ia, codigo-gerado-por-ia, assembly, opcode, compilador, abstracao, hipotese]
skill: lang-systems
status: stub
---

# IA gerando binário direto (sem linguagem-fonte)

Extensão lógica de [[wiki/concepts/c-como-linguagem-alvo-de-codigo-gerado-por-ia]] levantada em [[wiki/sources/c-linguagem-do-futuro-ia-assembly-opcode-safe-source-ricardo-albuquerque]]: se abstrações servem só ao humano, **não há razão para parar no C** — a IA poderia emitir [[wiki/concepts/assembly]] ou opcode e dispensar o [[wiki/concepts/compilador]]. Hoje isso não ocorre porque as LLMs aprenderam com código-fonte humano; o autor vê isso como "questão de tempo" de treinamento.

## Contrapontos [inferência, não da fonte]

- O compilador dá otimização madura, portabilidade entre arquiteturas e checagens de tipo/UB; a IA teria de reproduzi-las ou perderia essas garantias.
- Remove a auditabilidade: ver [[wiki/concepts/legibilidade-humana-do-codigo-gerado-por-ia]] (contra-argumento central do autor).
- Relacionado: [[wiki/concepts/linguagem-de-programacao-pensada-para-ia]] (outro caminho: linguagem nova, legível, com checagens para erros de IA).

## Key sources

- [[wiki/sources/c-linguagem-do-futuro-ia-assembly-opcode-safe-source-ricardo-albuquerque]] — "por que não assembly/opcode direto?"
