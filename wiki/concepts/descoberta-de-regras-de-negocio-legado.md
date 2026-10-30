---
type: concept
title: "Descoberta de Regras de Negócio em Legado"
aliases: ["business rule discovery", "recuperação de regras de negócio", "discovery de legado"]
date_created: 2026-10-06
date_updated: 2026-10-30
source_count: 2
tags: [legado, modernizacao, regras-de-negocio, mainframe, ia]
skill: tech-mentor-ai
status: draft
---

# Descoberta de Regras de Negócio em Legado

Fase **anterior** à reescrita de um sistema legado: extrair do código-fonte as regras de negócio acumuladas (legislação, processos) e escrevê-las em linguagem humana, para só então decidir o que migrar. No caso do [[wiki/entities/california-dmv]], ~6M de linhas de [[wiki/concepts/cobol]]/Assembly; análise manual estimada em ~5 anos, feita em 15 meses com IA + revisão humana ([[wiki/sources/dmv-california-ia-descoberta-regras-negocio-mainframe-cobol]]).

## Pipeline do caso DMV

1. Análise estática determinística ([[wiki/entities/ibm-arc]]): estrutura, chamadas, campos/arquivos, dependências, ordem de execução.
2. LLM ([[wiki/entities/watsonx]]) converte esses fatos em regras em linguagem humana — ver [[wiki/concepts/analise-estatica-como-ancora-de-llm]].
3. Revisão **técnica** (COBOL/mainframe) e **de negócio** (área usuária, legislação), em paralelo.
4. A revisão realimenta o ciclo seguinte — [[wiki/concepts/human-in-the-loop]].

## Por que não traduzir direto

Traduzir sem entender replica regras erradas ou perde regras implícitas; num sistema que se integra a outros órgãos, um erro de interpretação se propaga. O resultado do discovery é uma **base de regras**, não código novo.

Relacionados: [[wiki/concepts/conhecimento-perdido-em-legado]], [[wiki/concepts/engenharia-reversa]], [[wiki/concepts/modernizacao-de-mainframe]].

## Por que as Regras São o Difícil

[[wiki/sources/spec2cobolrot-envelhecer-cobol-com-ia-complexidade-vs-entropia-historica]] reforça o argumento por outro ângulo: até um benchmark sintético de COBOL, que bate as métricas estruturais de legado real, falha em reproduzir a evolução das regras de negócio. É essa evolução que a fase de descoberta tenta recuperar ([[wiki/concepts/entropia-historica-vs-complexidade-estrutural]]).

## Key sources

- [[wiki/sources/dmv-california-ia-descoberta-regras-negocio-mainframe-cobol]]

## Key sources (adição 2026-10-30)

- [[wiki/sources/spec2cobolrot-envelhecer-cobol-com-ia-complexidade-vs-entropia-historica]] — regras de negócio acumuladas são o que nem benchmark sintético reproduz
