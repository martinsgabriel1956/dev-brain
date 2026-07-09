---
type: concept
title: "Gramática Formal e EBNF"
aliases: ["EBNF", "Extended Backus-Naur Form", "gramática de linguagem de programação", "precedência de operadores", "associatividade"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [cs-fundamentals, linguagens-de-programacao, gramatica, parsers, compiladores]
skill: cs-fundamentals
status: draft
---

# Gramática Formal e EBNF

Toda linguagem de programação precisa de regras formais que definam quais sequências de tokens são válidas — sua **gramática**. Assim como uma frase em português segue uma estrutura esperada (sujeito, verbo, objeto), uma declaração de variável precisa seguir uma forma definida (palavra-chave, identificador, valor).

## EBNF (Extended Backus-Naur Form)

Notação usada para descrever formalmente a estrutura de uma linguagem. Exemplo mínimo:

```
statement  ::= assignment | print
assignment ::= "variável" identifier "=" expression
expression ::= number | string | identifier | expression operator expression
```

Essas poucas regras já derivam `variável x = 1 + 2` ou `variável nome = "João"`.

A gramática funciona como uma receita: para validar um trecho de código, o parser tenta *derivar* esse código a partir das regras. Se conseguir, a estrutura é válida; se não, é erro de sintaxe.

## Ambiguidade, precedência e associatividade

Uma gramática mal definida pode admitir mais de uma leitura para a mesma expressão — `1 + 2 * 3` é ambíguo se a gramática não especificar qual operador "agrupa primeiro". Isso é resolvido com:

- **Precedência**: multiplicação agrupa antes de soma, então `2 * 3` é avaliado primeiro em `1 + 2 * 3`.
- **Associatividade**: para operadores de mesma precedência, define se agrupam da esquerda para a direita ou o inverso.

Essas regras, apesar de parecerem detalhes pequenos, determinam como *todo* código escrito na linguagem será interpretado.

## Relação com outros conceitos

- [[wiki/concepts/compilador]] — a gramática é o contrato que o parser aplica para transformar tokens numa AST válida
- [[wiki/concepts/sistema-de-tipos]] — a gramática define o que é sintaticamente válido; o sistema de tipos define, depois, o que é semanticamente válido

## Key sources

- [[wiki/sources/como-criar-uma-linguagem-de-programacao]]
