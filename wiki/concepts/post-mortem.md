---
type: concept
title: "Post-mortem"
aliases: ["Postmortem", "Blameless Post-mortem", "Post Mortem"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 1
tags: [infra, ops, incident-response, sre]
skill: tech-mentor-infra
status: stable
---

# Post-mortem

**TL;DR:** Análise retrospectiva **blameless** de um incidente após a resolução. Responde: o que aconteceu, por que aconteceu (5 Porquês), como evitar. Escrito em até 48h enquanto o contexto está fresco.

## O Que É

Documento que transforma falhas em aprendizado sistêmico. Peça mais importante do ciclo operacional porque erros humanos são sintomas de falhas de sistema — nunca de pessoas.

## Três Perguntas Centrais

1. **O que aconteceu?** — fatos, linha do tempo, impacto
2. **Por que aconteceu?** — causa raiz + fatores contribuintes (5 Porquês)
3. **Como evitar?** — action items concretos com dono e prazo

## Técnica dos 5 Porquês

```
Sintoma: API fora por 45 min
Por quê? → Migration travou o banco
Por quê? → NOT NULL sem default em tabela de 8M rows
Por quê? → Não testada com volume de produção
Por quê? → Staging tem apenas 10k rows
Por quê? → Sem processo de validar migrations com dump de prod
                        ↑ Causa raiz sistêmica
```

## Princípio Blameless

Foco em sistemas, processos e ferramentas — nunca em pessoas. Requer maturidade da liderança para não virar caça às bruxas. Sem segurança psicológica, post-mortems não são escritos honestamente.

## Quando Usar

Qualquer incidente P1 ou P2. Incidente P3 com causa nova ou recorrente. Near-miss que poderia ter sido grave.

## Key Sources

- [[wiki/sources/post-mortem]]

## Conceitos Relacionados

[[runbook]] · [[playbook]]
