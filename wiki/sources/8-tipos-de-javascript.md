---
type: source
title: "Os 8 Tipos de JavaScript"
aliases: ["8 tipos de javascript", "typeof vs Object.prototype.toString"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_count: 0
tags: [javascript, tipagem, type-checking, fundamentos]
skill: lang-dynamic
status: stable
source_file: raw/8-tipos-de-javascript.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-10
---

# Os 8 Tipos de JavaScript

## TL;DR

Vídeo cobre os oito tipos de valor em JavaScript (`null`, `undefined`, `boolean`, `number`, `bigint`, `string`, `symbol`, `object`) e compara duas formas de checar tipo: `typeof` (rápida, mas imprecisa em casos como `null`) e `Object.prototype.toString.call()` (mais precisa, usada historicamente em bibliotecas como Underscore). Também cobre a diferença entre `==` (com conversão de tipo) e `===` (estrita), e a distinção entre `undefined` (aciona parâmetros default de função) e valores falsy em geral (acionam fallback via `||`).

## Afirmações-chave

| Afirmação | Evidência | Confiança |
|---|---|---|
| `typeof null` retorna `"object"`, não `"null"` — porque tudo em JS deriva de `Object` | Demonstração no vídeo | Alta (comportamento documentado e bem conhecido da linguagem) |
| `Object.prototype.toString.call(valor)` é mais preciso que `typeof` para type-checking | Demonstração no vídeo, citado uso histórico em Underscore | Alta |
| `==` faz conversão de tipo (truthy comparison); `===` não converte nada | Demonstração no vídeo (`null == undefined` → `true`) | Alta |
| Parâmetros default de função só reagem a `undefined`, não a `null` | Demonstração no vídeo (`bar(null)` retorna `null`, não o default) | Alta |
| Expressões com `\|\|` reagem a qualquer valor falsy, não só `undefined` | Demonstração no vídeo (`bar(0)` com `a = a \|\| [1,2,3]` retorna `[1,2,3]`) | Alta |
| `string + number` sempre concatena como string, independente da ordem | Demonstração no vídeo | Alta |
| JavaScript tem exatamente 8 tipos primitivos | Afirmação central do vídeo | Alta (consistente com a especificação ECMAScript) |

## Os 8 Tipos (resumo)

Ver detalhamento completo em [[wiki/concepts/tipos-primitivos-javascript]].

| # | Tipo | `typeof` | `Object.prototype.toString.call()` |
|---|---|---|---|
| 1 | `null` | `"object"` | `"[object Null]"` |
| 2 | `undefined` | `"undefined"` | `"[object Undefined]"` |
| 3 | `boolean` | `"boolean"` | `"[object Boolean]"` |
| 4 | `number` | `"number"` | `"[object Number]"` |
| 5 | `bigint` | `"bigint"` | `"[object BigInt]"` |
| 6 | `string` | `"string"` | `"[object String]"` |
| 7 | `symbol` | `"symbol"` | `"[object Symbol]"` |
| 8 | `object` | `"object"` (varia por subtipo) | `"[object Object]"`, `"[object Array]"`, etc. |

## Conceitos Introduzidos/Reforçados

- [[wiki/concepts/tipos-primitivos-javascript]] — página nova, central para este conteúdo
- [[wiki/concepts/pitfalls-de-linguagem]] — reforça `typeof null` e `==` vs `===` já citados ali, com o mecanismo detalhado
- [[wiki/concepts/sistema-de-tipos]] — tipagem fraca (conversão implícita) como eixo distinto de tipagem estática/dinâmica

## Entidades Mencionadas

- Nenhuma entidade identificável com segurança — ver open question abaixo.

## Questões em Aberto

- **Autoria não identificada com confiança.** A transcrição de origem tem qualidade baixa (erros de reconhecimento de fala) e o apresentador se identifica de forma ambígua ("eu souer"/"eu sou o Elder"?). Não foi criada página de entidade para evitar atribuição incorreta. Se o autor/canal for identificado com mais confiança futuramente, criar `wiki/entities/<nome>.md` e linkar aqui.
- Transcrição contém diversos erros de reconhecimento de fala (ex.: "true string" → `toString`, "TR" → `to`) corrigidos por inferência de contexto ao limpar o texto em `raw/8-tipos-de-javascript.md`; alguns trechos foram parafraseados para legibilidade mantendo o conteúdo técnico original.
