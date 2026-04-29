---
type: concept
title: "Complexidade como Estratégia"
aliases: ["complexidade intencional", "job security pelo código", "código refém", "complexidade artificial"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [anti-pattern, cultura, carreira, legado, qualidade]
skill: tech-mentor-leadership
status: stable
---

# Complexidade como Estratégia

Anti-pattern onde um desenvolvedor aumenta artificialmente a complexidade do código como mecanismo de proteção de emprego ou como forma de aparentar habilidade.

## Os Três Estágios

**Estágio 1 — Inconsciente** (tolerável)
- Complexidade por falta de compreensão do problema de negócio
- Ou por escopo mal definido
- Não é malícia — é inexperiência

**Estágio 2 — Ego** (prejudicial)
- Complica para impressionar, para "aparecer que sabe fazer coisas difíceis"
- Para se provar tecnicamente perante o time
- Ativo no ego, passivo no resultado do produto

**Estágio 3 — Sabotagem** (danoso à equipe e ao produto)
- Cria código que somente ele consegue dar manutenção
- Elimina qualquer alternativa que ameace essa dependência
- É o mais difícil de detectar porque o código "funciona"

## Custo Real

- Onboarding mais lento para novos membros
- Refatoração futura exponencialmente mais cara
- Bus factor = 1 (toda operação crítica depende de uma pessoa)
- Cultura de medo: ninguém toca o código porque não entende

## A Direção Oposta

Código de alta qualidade é aquele que qualquer membro do time consegue modificar com confiança. Facilidade de deleção é uma virtude arquitetural.

> "Bom código significa: fácil de entender, fácil de deletar, resolve o negócio."

## Ver também

- [[concepts/principio-da-inversao]] — hábito ruim nº 2
- [[concepts/tech-debt]] — complexidade artificial acumula como dívida técnica
- [[concepts/ciclo-da-desgraca-software]] — complexidade acumulada dispara o ciclo de reescrita

## Key Sources

- [[sources/principio-da-inversao-programador]]
