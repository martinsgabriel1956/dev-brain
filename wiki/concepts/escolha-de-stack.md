---
type: concept
title: "Escolha de Stack"
aliases: ["escolher stack", "stack choice", "framework batteries included", "escolha de framework"]
date_created: 2026-07-07
date_updated: 2026-07-07
source_count: 1
tags: [stack, framework, projetos, mvp, saas, carreira]
skill: tech-mentor-leadership
status: stable
---

# Escolha de Stack

A escolha de stack para um projeto novo está sempre atrelada àquilo que o profissional já conhece — mas o **objetivo do projeto** muda qual lado dessa relação pesa mais.

## Duas Motivações, Duas Escolhas

| Objetivo | Escolha típica | Por quê |
|---|---|---|
| **Aprender algo novo** | Tecnologia que você ainda não domina (Elixir, Go, Rust...) | O foco é a tecnologia em si, não o resultado financeiro |
| **Ganhar dinheiro** | Tecnologia que você já domina (na prática, majoritariamente JavaScript) | O foco é entregar valor rápido, não aprender ferramenta nova |

Hoje em dia vale conversar com uma IA para levantar possibilidades e discutir trade-offs antes de decidir — mas a decisão final ainda reflete essa dicotomia objetivo-aprender vs. objetivo-monetizar.

## Framework "Batteries Included" para Solo Dev / SaaS

Quando você é um desenvolvedor solo tentando sair do zero para encontrar os primeiros usuários, um framework **batteries included** costuma acelerar mais do que um setup minimalista:

- **Django** (Python) — painel de admin, models e convenções prontas
- **Rails** (Ruby)
- **Laravel** (PHP)

Comparados a um setup mais nu como **Node + Express**, que entrega menos coisas out-of-the-box — exigindo agregar plugins e montar peças manualmente — esses frameworks saem do zero de forma mais rápida, porque a maior parte das decisões de estrutura já vem tomada.

## Escolha Também Depende da Natureza do Projeto

- **Single-page application** → um framework como Next.js pode fazer mais sentido
- **Backend computacionalmente pesado** → Python ou JavaScript podem não ser a escolha ideal

## Ver Também

- [[wiki/concepts/checklist-primeiro-dia-projeto]] — a escolha de stack é o primeiro passo do checklist
- [[wiki/concepts/mvp]] — a stack escolhida deve servir o MVP, não o produto final imaginado

## Key Sources

- [[wiki/sources/5-ou-6-dicas-para-projetos-novos]]
