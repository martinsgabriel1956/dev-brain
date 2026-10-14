---
type: concept
title: "Três Passos para Lidar com Bug"
aliases: ["causa raiz, evidenciar, provar", "workflow de correção de bug"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [bugs, debugging, causa-raiz, testes, workflow, habitos]
skill: tech-mentor-testing
status: draft
---

# Três Passos para Lidar com Bug

Workflow de [[wiki/entities/andre-casciotti]] para sair do [[wiki/concepts/ciclo-de-bugs-e-retrabalho]]. Antes de tudo, **pare e respire** (não abrir o editor no reflexo). Depois:

1. **Identifique a causa raiz** ([[wiki/concepts/causa-raiz]]): não corrija o sintoma onde estourou o erro. Pergunte: o estado faz sentido aqui? como é o fluxo de negócio inteiro? por que o código está assim (talvez haja um motivo)? Meta: olhar o fluxo, não um ponto fixo.
2. **[[wiki/concepts/evidenciar-o-problema]]**: simule o erro antes de alterar (log, tela, print, conversa com QA/usuário); debug sozinho não basta.
3. **[[wiki/concepts/provar-que-corrigiu]]**: rode o mesmo teste antes e depois; em seguida faça a [[wiki/concepts/analise-de-impacto-da-correcao]]; teste unitário reforça a prova.

A ordem importa: sem causa raiz não se sabe se corrigiu; sem evidência não se sabe o que provar. O autor insiste que o difícil não é saber, é **fazer** (anotar e colar no monitor), em especial o dev experiente ([[wiki/concepts/armadilha-da-certeza-do-dev-experiente]]). É [[wiki/concepts/analise-de-requisitos-aplicada-a-bugs|análise de requisitos]] aplicada a bugs. [skill: tech-mentor-testing] equivale a "reproduzir com teste que falha, corrigir, ver passar" ([[wiki/sources/test-driven-bug-fixing-xunitpatterns]]).

## Key Sources

- [[wiki/sources/como-sair-do-ciclo-de-bugs-e-retrabalho-andre-casciotti]]
