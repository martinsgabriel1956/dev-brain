---
type: concept
title: "Evento Enxuto vs. Evento Gordo"
aliases: ["thin event", "fat event", "event-carried state transfer", "event notification"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [event-driven, versionamento, acoplamento, lgpd]
skill: tech-mentor-backend
status: draft
---

# Evento Enxuto vs. Evento Gordo

| | Enxuto (notificação) | Gordo (transferência de estado) |
|---|---|---|
| Conteúdo | só identificadores | estado completo |
| Acoplamento | baixo: o banco muda sem mudar o evento | alto: o evento espelha o modelo/banco |
| Consumo | consulta posterior (ex.: HTTP) | tudo no evento |
| Governança/LGPD | ID não é sensível; dado completo passa pela gestão de API (sabe-se quem consome o quê) | produtor pode nem mapear quem lê dado pessoal |
| Custo | carga de rede; resiliência vem da fila (retry/DLQ) | menos rede |
| Versionamento | menos dor | muita dor |

Posição da fonte ([[wiki/sources/arquitetura-orientada-a-eventos-luiz-gago-faria-otavio-santana-eduardo-macris]]): **começar pelo enxuto**; o gordo é a segunda opção e exige provar que a primeira não serve (casos de sincronização, rede cara). Mudança frequente de evento sugere problema de design.

**Fim de vida (EOL):** manter ≥2 versões em paralelo só funciona com prazo definido (1–2 anos) e respeitado; sem isso, a independência vira gargalo (relatos de queda de diretoria/gerência). Ver [[wiki/sources/event-versioning]] e [[wiki/concepts/api-versioning]].

Relacionados: [[wiki/concepts/event-driven-architecture]], [[wiki/concepts/lgpd]], [[wiki/concepts/api-gateway]], [[wiki/concepts/evento-vs-comando]].

## Key sources

- [[wiki/sources/arquitetura-orientada-a-eventos-luiz-gago-faria-otavio-santana-eduardo-macris]]
