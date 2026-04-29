---
type: concept
title: "Usuários Como Agentes do Caos"
aliases: ["usuarios quebram tudo", "edge cases de usuarios", "chaos agents"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
tags: [testes, edge-cases, qa, usuarios, craftsmanship]
skill: tech-mentor-leadership
status: stub
---

## TL;DR

Toda suposição não testada será quebrada por algum usuário. Inputs impossíveis tornam-se comuns assim que alguém real começa a usar o sistema.

## Exemplos Reais

- Emoji em campo de nome → formulário quebrado
- SQL injection em campo de busca
- String vazia em campo obrigatório
- Spam de 50 cliques por ausência de feedback visual
- Browser legado com comportamento diferente

> *"O impossível se torna possível no segundo em que alguém chamado Dave começa a digitar."*

## O que Testar

Strings vazias, null, valores negativos, caracteres especiais (emoji, aspas, barras), inputs gigantes, requests concorrentes, e qualquer coisa que você acha que ninguém faria.

## Relacionado

- [[property-based-testing]] — gera automaticamente inputs caóticos para encontrar edge cases
- [[n-plus-um-detector]] — usuários em escala revelam problemas de performance invisíveis em dev

## Key Sources

- [[sources/5-principios-programador]]
