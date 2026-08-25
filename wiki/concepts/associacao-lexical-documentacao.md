---
type: concept
title: "Associação Lexical na Documentação (Português → Inglês)"
aliases: ["traduzir necessidade para nome de método", "achar o método certo na doc"]
date_created: 2026-08-24
date_updated: 2026-08-24
source_count: 1
tags: [aprendizado, documentacao, ingles, java]
skill: tech-mentor-leadership
status: stub
---

# Associação Lexical na Documentação (Português → Inglês)

Técnica prática para navegar uma [[wiki/concepts/javadoc-api-reference|API reference]] em inglês: em vez de ler a documentação inteira de cima para baixo, traduzir mentalmente a necessidade em português para o verbo/substantivo em inglês mais provável e buscar esse nome entre os métodos disponíveis.

## Exemplos do mapeamento

| Necessidade em português | Método provável (Java `String`) |
|---|---|
| "Cortar em pedaços" | `split` |
| "Verificar se contém um trecho" | `contains` |
| "Saber o tamanho" | `length` |
| "Verificar se dois textos são iguais" | `equals` |

## Por que funciona

APIs de linguagens maduras nomeiam métodos por verbos de domínio geral (cortar → split, conter → contains), então a barreira real não é o inglês técnico da documentação em si, mas o vocabulário de ~20-30 verbos comuns usados para nomear operações. Dominar esse vocabulário reduz a leitura de documentação a uma busca dirigida (Ctrl+F mental) em vez de leitura linear.

## Ver Também

- [[wiki/concepts/javadoc-api-reference]] — onde a técnica é aplicada
- [[wiki/concepts/padrao-de-secoes-de-documentacao-tecnica]] — contexto mais amplo de como navegar documentação técnica

## Key Sources

- [[wiki/sources/como-ler-documentacao-de-uma-linguagem-de-programacao]]
