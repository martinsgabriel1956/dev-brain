---
type: concept
title: "Edge Case"
aliases: ["caso de borda", "cenário de erro", "caso extremo"]
date_created: 2026-05-13
date_updated: 2026-05-13
source_count: 1
tags: [edge-case, caso-de-borda, fundamentos, cs-fundamentals]
skill: cs-fundamentals
status: draft
---

# Edge Case

Cenário que ocorre fora do fluxo principal ([[caminho-feliz]]) — entradas inválidas, falhas externas, estados inesperados, limites de sistema. São os casos que o sistema precisa tratar explicitamente para não falhar de forma imprevisível.

## Por que importam

Edge cases são onde os sistemas falham em produção. Mapear edge cases no início do projeto é o que separa sistemas robustos de sistemas frágeis.

## Perguntas para identificar edge cases

1. O que pode dar errado?
2. Quais entradas inválidas o usuário pode fornecer?
3. O que acontece se um sistema externo falhar?
4. Quais são os limites (tempo, tentativas, tamanho, valor)?

## Exemplo: caixa eletrônico

| Edge case | Resposta do sistema |
|---|---|
| Senha incorreta | Permite nova tentativa (até 3x) |
| Saldo insuficiente | Mostra saldo e oferece valor menor |
| Caixa sem dinheiro | Avisa e encerra |
| Cartão bloqueado | Avisa e encerra sessão |

## Relação com outros conceitos

- Complemento do [[caminho-feliz]]
- Devem ser mapeados no passo 1 de [[logica-de-programacao]] antes de qualquer código
- Cada edge case vira uma ramificação no [[fluxo-logico]]

## Key sources

- [[wiki/sources/logica-de-programacao-quatro-passos]]
