---
type: concept
title: "Dois Chapéus (Kent Beck)"
aliases: ["two hats", "two hats metaphor", "chapéu de refatoração", "chapéu de funcionalidade"]
date_created: 2026-07-15
date_updated: 2026-07-15
source_count: 1
tags: [refactoring, craftsmanship, kent-beck, extreme-programming]
skill: tech-mentor-backend
status: stub
---

# Dois Chapéus (Kent Beck)

Metáfora de [[wiki/entities/kent-beck]]: ao desenvolver software, o tempo se divide em duas atividades distintas e mutuamente exclusivas — **adicionar funcionalidades** e **refatorar**. Cada uma usa um "chapéu" diferente, e os dois nunca devem ser usados ao mesmo tempo.

- **Chapéu de funcionalidade:** o progresso é avaliado acrescentando testes e fazendo-os passar. Comportamento do sistema muda.
- **Chapéu de refatoração:** o objetivo é só reestruturar código, preferencialmente sem alterar nenhum resultado esperado nos testes já existentes. Comportamento do sistema não muda.

A troca de chapéu pode acontecer em minutos ou durar horas — o que importa é ter consciência explícita de qual chapéu está sendo usado num dado momento, porque cada um exige uma disciplina diferente (num, você prova que algo novo funciona; no outro, você prova que nada mudou).

## Relacionado

[[wiki/concepts/refatoracao]] — esse princípio é a base do primeiro pilar da definição de refatoração (comportamento externo intacto).

## Key Sources

- [[wiki/sources/o-que-e-refatoracao-quando-usar]]
