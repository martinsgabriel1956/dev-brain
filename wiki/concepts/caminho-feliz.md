---
type: concept
title: "Caminho Feliz"
aliases: ["happy path", "fluxo principal", "golden path"]
date_created: 2026-05-13
date_updated: 2026-11-24
source_count: 2
tags: [caminho-feliz, happy-path, fundamentos, cs-fundamentals]
skill: cs-fundamentals
status: draft
---

# Caminho Feliz

O fluxo de execução em que tudo ocorre conforme o esperado — sem erros, sem entradas inválidas, sem falhas externas. É o cenário ideal que o sistema foi projetado para servir.

## Por que não é suficiente

Descrever apenas o caminho feliz é uma descrição superficial do problema. Os sistemas falham nos [[edge-case]]s, não no fluxo principal. Projetar só o caminho feliz é a causa mais comum de bugs descobertos em produção.

## Exemplo: caixa eletrônico

**Caminho feliz:**
1. Usuário insere cartão
2. Digita senha correta
3. Escolhe valor disponível
4. Dinheiro sai
5. Operação finalizada

O que não está aqui: senha errada, saldo insuficiente, cartão bloqueado, caixa sem dinheiro. Esses são os [[edge-case]]s que precisam ser mapeados no passo 1 da [[logica-de-programacao]].

## Relação com outros conceitos

- Contraste direto com [[edge-case]]
- É o ponto de partida do passo 1 de [[decomposicao-de-problemas]], mas não o ponto final

## Em design de fluxos

Na [[wiki/sources/frontpush-dashboards-principios-parte-1|aula 04 do módulo de dashboards]], [[wiki/entities/nasser|Násser]] chama de "fluxo do sucesso" o caminho em que "o usuário não fez nada de errado" e pede para mapear os outros a partir da mesma tela: senha errada, esqueci a senha, criar conta, login social. Ver [[wiki/concepts/fluxos-bem-definidos]].

## Key sources

- [[wiki/sources/logica-de-programacao-quatro-passos]]
- [[wiki/sources/frontpush-dashboards-principios-parte-1]]: FrontPUSH, dashboards aula 04: "fluxo do sucesso" no login
