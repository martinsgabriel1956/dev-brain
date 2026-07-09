---
type: concept
title: "Sistema de Tipos"
aliases: ["type system", "tipagem estática", "tipagem dinâmica", "inferência de tipos", "static vs dynamic typing"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [cs-fundamentals, linguagens-de-programacao, tipagem, compiladores]
skill: cs-fundamentals
status: draft
---

# Sistema de Tipos

Conjunto de regras que decide o que uma linguagem considera um valor válido de determinado tipo, e o que acontece quando tipos diferentes interagem (ex.: somar um número com uma string). A decisão central é **quando** essas regras são verificadas.

## Estática vs. Dinâmica

| | Tipagem Estática | Tipagem Dinâmica |
|---|---|---|
| **Quando verifica** | Em tempo de compilação, antes do código rodar | Em tempo de execução |
| **Vantagem** | Erros de tipo pegos cedo; editor consegue oferecer autocomplete melhor | Mais rápida de escrever; menos verbosidade |
| **Custo** | Mais informação explícita no código (tipos de parâmetro, genéricos, tratamento de nulos) | Erros só aparecem quando aquele caminho de código executa — às vezes em produção |
| **Exemplos** | Rust, Java, TypeScript, C | Python, JavaScript, Ruby |

Exemplo do trade-off prático: somar um número com uma string. Em JavaScript (dinâmica), o número é convertido e concatenado silenciosamente. Em Python (dinâmica), lança erro em runtime. Numa linguagem estaticamente tipada como Rust, essa operação inválida nem passa pela compilação.

## Inferência de tipos — o meio-termo

Linguagens como TypeScript e Rust deduzem o tipo sem exigir declaração explícita: `let x = 42` já é reconhecido como número pelo compilador. Mantém boa parte da segurança da tipagem estática com a concisão da dinâmica.

## Além de número vs. string

Um sistema de tipos completo também precisa decidir: se uma função pode retornar tipos diferentes, se variáveis podem mudar de tipo, como genéricos funcionam, e como representar a ausência de valor (null, `Option`/`Maybe`, `undefined`). Cada uma dessas decisões afeta diretamente a segurança e a ergonomia da linguagem.

## Relação com outros conceitos

- [[wiki/concepts/compilador]] — o sistema de tipos é validado sobre a AST que o parser produz, antes (estática) ou depois (dinâmica) da geração de código
- [[wiki/concepts/gerenciamento-de-memoria]] — em Rust, o *type checker* e o *borrow checker* trabalham juntos: ownership é, em parte, verificação de tipos em tempo de compilação

## Key sources

- [[wiki/sources/como-criar-uma-linguagem-de-programacao]]
