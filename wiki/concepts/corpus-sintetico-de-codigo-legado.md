---
type: concept
title: "Corpus Sintético de Código Legado"
aliases: ["synthetic legacy corpus", "envelhecimento de código com IA", "degradation loop", "benchmark de modernização"]
date_created: 2026-10-30
date_updated: 2026-10-30
source_count: 1
tags: [legado, cobol, benchmark, agentes-ia, pesquisa, modernizacao]
skill: tech-mentor-backend
status: stub
---

# Corpus Sintético de Código Legado

Conjunto de programas gerado artificialmente para testar ferramentas de modernização quando o legado real não pode ser usado (é de banco, seguradora, governo). O problema clássico: código escrito para o teste é limpo e "didático" demais.

## Abordagem Spec2COBOLRot

`[external]` Em [[wiki/entities/spec2cobolrot]] ([[wiki/sources/spec2cobolrot-envelhecer-cobol-com-ia-complexidade-vs-entropia-historica]]):

1. Especificação em linguagem natural (bancário, folha, seguros), validada por especialista.
2. Agente gerador produz COBOL; compila e executa no GnuCOBOL até 5 vezes.
3. Agente de degradação injeta padrões de um catálogo de 26 (8 *idioms*, 15 *smells*, 3 *mismatches*) até 5 vezes.
4. Para quando as métricas (SLOC, parágrafos, CC, GO TO, uso de variáveis…) caem na faixa derivada de 14 programas reais.

## Limites

- Comportamento preservado em só 5 de 9 execuções no nível mais simples.
- Em escala, o LLM infla o tamanho duplicando parágrafos.
- Bate métrica sem reproduzir história: ver [[wiki/concepts/entropia-historica-vs-complexidade-estrutural]].

Útil para testar robustez estrutural de um tradutor; insuficiente para testar se ele preserva regras de negócio [inferência]. Paralelo com [[wiki/concepts/golden-dataset]]: o valor do conjunto depende de quão bem ele representa a produção.

## Key Sources

- [[wiki/sources/spec2cobolrot-envelhecer-cobol-com-ia-complexidade-vs-entropia-historica]]
