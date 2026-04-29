---
type: concept
title: "Naming"
aliases: ["nomeação", "naming things", "nomear variáveis", "nomes ruins"]
date_created: 2026-04-26
date_updated: 2026-04-29
source_count: 2
tags: [naming, clean-code, craftsmanship, legibilidade, carreira]
skill: tech-mentor-leadership
status: draft
---

# Naming

Nomear bem é uma das habilidades mais subestimadas em desenvolvimento. Nomes ruins compõem **dívida cognitiva permanente** — cada leitura futura do código custa mais do que custaria ter passado 5 minutos pensando no nome certo.

## Por que é difícil

Phil Karlton: *"There are only two hard things in Computer Science: cache invalidation and naming things."*

Nomear bem exige entender completamente o que o código faz. Se você não consegue nomear claramente, é sinal de que não entende o suficiente ainda.

## Anti-padrões comuns

| Nome ruim | Problema | Alternativa |
|---|---|---|
| `doStuff()` | Nenhuma informação sobre o que faz | `processPaymentWebhook()` |
| `data`, `data2` | Genérico — qualquer coisa é dado | `validatedUserInput`, `rawApiResponse` |
| `manager` | Faz tudo, não diz nada | `SessionStore`, `PermissionChecker` |
| `handler` | Qual evento? Qual entidade? | `handleUserCreatedEvent` |
| `info` | De quem? Sobre o quê? | `userProfileMetadata` |

## Regra prática

> Gaste 5 minutos no nome → economize 5 horas depois.

Se 6 meses atrás você não entende o que `data2` significa, nomeie agora. Se você não consegue nomear algo de forma clara, é um sinal de que você deve refatorar antes de nomear.

## Relacionado

[[sources/habitos-ruins-de-programador]] · [[concepts/testar-proprio-codigo]]

## Key Sources

- [[sources/5-principios-programador]]
