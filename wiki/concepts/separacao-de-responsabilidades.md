---
type: concept
title: "Separação de Responsabilidades"
aliases: ["separation of concerns", "SoC", "cada parte cuida de uma coisa só"]
date_created: 2026-05-13
date_updated: 2026-05-13
source_count: 1
tags: [separacao-de-responsabilidades, arquitetura, fundamentos, cs-fundamentals]
skill: cs-fundamentals
status: draft
---

# Separação de Responsabilidades

Princípio de design onde cada módulo, função ou componente do sistema cuida de **uma coisa só**. Módulos diferentes não precisam conhecer os detalhes internos uns dos outros.

## Por que importa

- Facilita testar cada parte isoladamente
- Reduz o impacto de mudanças (alterar autenticação não quebra verificação de saldo)
- Torna o sistema mais fácil de entender e manter

## Exemplo concreto

No caixa eletrônico, o módulo de autenticação não precisa saber nada sobre saldo. O módulo de validação do saque não precisa saber nada sobre como a autenticação funciona. Cada um tem uma fronteira clara.

## Relação com outros conceitos

- É o resultado natural de uma boa [[decomposicao-de-problemas]]
- Aparece em escalas diferentes: funções, módulos, serviços, microsserviços
- Base do princípio Single Responsibility (SOLID)

## Key sources

- [[wiki/sources/logica-de-programacao-quatro-passos]]
