---
type: concept
title: "Domínio Centralizado vs. Modelo por Slice"
aliases: ["modelo de domínio centralizado", "um usuário por slice", "múltiplas representações da mesma entidade"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_count: 1
tags: [dominio, vertical-slice, acoplamento, modelagem, bounded-context]
skill: tech-mentor-backend
status: draft
---

# Domínio Centralizado vs. Modelo por Slice

## TL;DR

Hábito herdado da orientação a objetos: uma camada de domínio única, com uma classe por entidade (`Usuario`) usada por todos os casos de uso. [[wiki/sources/vertical-slice-organizar-codigo-por-funcionalidade-bernardo-lobato]] argumenta que isso **infla** a classe (auth + perfil + seguidores + entregas), cria autoacoplamento e faz qualquer mudança arriscar módulos sem relação; e que times diferentes acabam editando as mesmas classes. No [[wiki/concepts/vertical-slice-architecture]], **cada slice tem sua própria representação** da entidade, só com os campos que a funcionalidade manipula (auth: username/senha/token; perfil: nome/documento/endereços).

## Comparação

| | Centralizado | Por slice |
|---|---|---|
| Classe `Usuário` | única, cresce com cada feature | uma por slice, enxuta |
| Alterar perfil | pode afetar autenticação | só a slice de perfil |
| Conflito entre times | mesmos arquivos | arquivos separados |
| Custo | acoplamento, testes de regressão amplos | duplicação de campos/regras |

## Relações

- Mesma ideia, no nível de contexto de negócio, de [[wiki/concepts/bounded-context]] (duas classes `Produto` em Vendas e Suporte) — a slice é uma fronteira ainda mais fina que o contexto. [inferência]
- Contraponto a reuso via [[wiki/concepts/shared-kernel]]: aqui a recomendação é **não** compartilhar o modelo.
- Risco registrado: dev novo "unifica" os modelos numa classe central; exige revisão rigorosa ([[wiki/concepts/acoplamento-entre-slices]]).
- Tensão aberta: invariantes realmente comuns acabam duplicados ou extraídos para shared.

## Key sources

- [[wiki/sources/vertical-slice-organizar-codigo-por-funcionalidade-bernardo-lobato]]
