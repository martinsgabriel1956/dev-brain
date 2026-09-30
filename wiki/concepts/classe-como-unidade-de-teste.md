---
type: concept
title: "Classe como Unidade de Teste"
aliases: ["menor unidade a testar", "testar a classe, não o método", "unit = class"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [testes, tdd, teste-unitario, oop, design]
skill: tech-mentor-testing
status: stub
---

# Classe como Unidade de Teste

Posição defendida em [[wiki/sources/como-ser-otimo-programador-sem-usar-o-cerebro]]: em programação orientada a objetos, "a menor unidade certa para testar é geralmente **a classe**", não o método.

**Argumento:** raramente se conhecem os detalhes internos de um método antes de escrevê-lo; testes escritos por método acabam **reescritos** (e em sua maioria inúteis) quando o design interno muda. Já as classes podem ser previstas ao decompor a tarefa em etapas ([[wiki/concepts/atomic-commits]]), então os testes de classe sobrevivem à refatoração.

**Crítica ao TDD feita pela fonte:** não é "não sei a especificação" (ridículo), mas "não sei os passos até cumpri-la" — o problema é o *grão* do teste unitário. Ver [[wiki/concepts/tdd]].

## Ligações e ressalvas

- Alinha-se ao espírito de testar comportamento pela interface pública e ao estilo sociável de [[wiki/concepts/unit-test-solitario-vs-sociavel]]; a fonte não usa esses termos (**inferência**).
- Testar só a classe pode dificultar localizar o defeito ([[wiki/concepts/frequent-debugging]]) — trade-off não discutido pela fonte (**inferência**).
- É opinião ("na minha opinião"), sem evidência empírica na fonte.

## Key Sources

- [[wiki/sources/como-ser-otimo-programador-sem-usar-o-cerebro]]
