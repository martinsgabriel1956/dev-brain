---
type: concept
title: "Escolha de Stack"
aliases: ["escolher stack", "stack choice", "framework batteries included", "escolha de framework"]
date_created: 2026-07-07
date_updated: 2026-09-03
source_count: 4
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

## A Dicotomia Formalizada pela Tríade Retorno-Risco-Liquidez

O [[wiki/concepts/avaliar-hype-tecnologico]] explica *por que* essa dicotomia aprender-vs-monetizar existe: aprender tecnologia nova é uma aposta de retorno-conhecimento, viável com risco controlado (ex.: projeto pessoal sem expectativa financeira); monetizar exige retorno financeiro real, o que empurra a escolha para tecnologia já dominada, de risco/liquidez conhecidos.

## Resistir a Pressão Externa de Troca de Stack

Em [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]], o autor do Find My SaaS (feito em Ruby) recebe, sem solicitar, um e-mail sugerindo reescrever o projeto em TypeScript com a justificativa de que Ruby é "fracamente tipado". Rejeita a sugestão: se a troca fosse mesmo por tipagem forte, a escolha não seria TypeScript, e trocar de stack só por preferência alheia — sem avaliação real de custo/benefício para o projeto em questão — coloca em risco a execução. Ver [[wiki/concepts/especialista-de-powerpoint]] para o padrão mais amplo de feedback não solicitado de quem nunca lançou um produto.

## Ver Também

- [[wiki/concepts/checklist-primeiro-dia-projeto]] — a escolha de stack é o primeiro passo do checklist
- [[wiki/concepts/mvp]] — a stack escolhida deve servir o MVP, não o produto final imaginado
- [[wiki/concepts/avaliar-hype-tecnologico]] — modelo de decisão para adotar tecnologia emergente/hype

## Key Sources

- [[wiki/sources/5-ou-6-dicas-para-projetos-novos]]
- [[wiki/sources/como-identificar-o-proximo-hype-tecnologico]]
- [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]] — rejeição de pressão externa para trocar de stack (Ruby → TypeScript) sem justificativa técnica real
- [[wiki/sources/tres-mentiras-que-te-reprovam-em-entrevistas-de-arquitetura-de-sistemas]] — escolha de tecnologia reposicionada como exercício de tradeoff contextual (caso de uso × prós e contras), não de repertório memorizado
