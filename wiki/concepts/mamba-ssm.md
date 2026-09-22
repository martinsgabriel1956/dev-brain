---
type: concept
title: "Mamba Ssm"
aliases: []
date_created: 2026-09-22
date_updated: 2026-09-22
source_count: 0
tags: [mamba-ssm]
skill: tech-mentor-ai
status: stub
---

# Mamba Ssm

Stub criado durante sweep de lint (links quebrados) a partir de referências em 2 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/concepts/self-attention]]: Para n tokens, a matriz de atenção é n×n — custo quadrático no comprimento da sequência. Ver [[transformer-architecture]] para o impacto disso em context window e as otimizações ([[concepts/flash-attention]], [[mamba-ssm]]) que existem para mitigar.
- Em [[wiki/concepts/transformer-architecture]]: Self-attention é O(n²) no comprimento da sequência — para n tokens, a matriz de atenção é n×n. Isso é o gargalo físico por trás do limite de [[context-window|context window]] e motivou arquiteturas alternativas como [[mamba-ssm]] (O(n)) e otimizações como [[concepts/flash-attention]] (mesmo resultado matemático, muito mais eficiente em memória).

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

## Key sources

- [[wiki/concepts/self-attention]]
- [[wiki/concepts/transformer-architecture]]
