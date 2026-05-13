---
type: concept
title: "Decomposição de Problemas"
aliases: ["problem decomposition", "quebrar em partes menores"]
date_created: 2026-05-13
date_updated: 2026-05-13
source_count: 1
tags: [decomposicao, fundamentos, cs-fundamentals]
skill: cs-fundamentals
status: draft
---

# Decomposição de Problemas

Técnica de resolver um problema complexo quebrando-o em subproblemas menores e mais simples, cada um resolvível de forma (quase) independente.

## Por que funciona

Nenhum problema complexo é resolvido de uma única vez. Ao decompor, cada parte menor pode ser pensada, testada e corrigida sem afetar as outras.

## Exemplo: caixa eletrônico

| Módulo | Responsabilidade |
|---|---|
| Autenticação | Verificar cartão e senha |
| Verificação de saldo | Checar saldo disponível |
| Validação do saque | Checar limite diário e dinheiro no caixa |
| Execução do saque | Debitar e liberar dinheiro físico |
| Encerramento | Devolver cartão, comprovante, encerrar sessão |

A autenticação não precisa saber nada sobre saldo. Isso é [[separacao-de-responsabilidades]] na prática.

## Relação com outros conceitos

- Viabiliza [[separacao-de-responsabilidades]]
- É o passo 2 do framework de [[logica-de-programacao]]
- Cada subproblema gera seu próprio [[fluxo-logico]]

## Key sources

- [[wiki/sources/logica-de-programacao-quatro-passos]]
