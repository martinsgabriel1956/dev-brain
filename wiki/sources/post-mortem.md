---
type: source
title: "Post-mortem"
aliases: ["Post Mortem", "Postmortem", "Blameless Post-mortem"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_file: /home/nemomartins/Documentos/new/dev-study/raw/post-mortem.md
source_url: ""
author: "tech-mentor-infra"
date_published: 2026-05-17
date_ingested: 2026-05-17
tags: [infra, ops, incident-response, post-mortem, sre]
skill: tech-mentor-infra
status: stable
---

# Post-mortem

## TL;DR

Post-mortem é análise retrospectiva **blameless** de um incidente após a resolução. Responde três perguntas: o que aconteceu, por que aconteceu (5 Porquês até a causa sistêmica) e como evitar. Deve ser escrito em até 48h enquanto o contexto está fresco. Transforma falhas em aprendizado sistêmico.

## Key Claims

- **Blameless é o princípio central:** erros humanos são sintomas de falhas de sistema — nunca culpar pessoas. [[wiki/concepts/post-mortem]]
- **5 Porquês:** técnica para ir além do sintoma até a causa sistêmica (ex: NOT NULL sem default em tabela de 8M rows → não existe processo de validar migrations com volume de prod)
- **Estrutura:** Severidade/Duração/Impacto → Linha do Tempo → Causa Raiz → Fatores Contribuintes → O que foi bem → Action Items com dono e prazo → Lições
- **48h de prazo:** deve ser escrito enquanto o contexto ainda está fresco
- **Action items sem acompanhamento ficam no papel:** o valor real do post-mortem está nos action items executados
- **Nunca evitar por constrangimento:** isso destrói a cultura psicológica segura

## Concepts

- [[wiki/concepts/post-mortem]]
- [[wiki/concepts/playbook]]
- [[wiki/concepts/runbook]]

## Open Questions

- Como garantir que os action items de post-mortem sejam executados e não apenas documentados?

## Raw Quotes

> "O princípio central é blameless: o foco é em sistemas, processos e ferramentas — nunca em culpar pessoas. Erros humanos são sintomas de falhas de sistema."

> "Deve ser escrito em até 48h após a resolução, enquanto o contexto ainda está fresco."
