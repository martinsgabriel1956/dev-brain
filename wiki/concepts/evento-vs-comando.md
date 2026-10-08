---
type: concept
title: "Evento vs. Comando"
aliases: ["comando vs evento", "event vs command"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [event-driven, acoplamento, mensageria]
skill: tech-mentor-backend
status: draft
---

# Evento vs. Comando

**Comando** diz a outro componente o que fazer: quem envia precisa conhecer o destinatário e o formato que ele aceita (acoplamento direto). **Evento** diz o que aconteceu, pela ótica de quem publica; quem publica é o dono da informação e não se importa com quem consome (relação 1→N ou 1→0, inclusive publicar anos antes de existir um consumidor).

Consequências ([[wiki/sources/arquitetura-orientada-a-eventos-luiz-gago-faria-otavio-santana-eduardo-macris]]):
- O produtor ganha autonomia: pode mudar quando quiser (com prazo de migração, ver [[wiki/concepts/evento-enxuto-vs-evento-gordo]]).
- Meta prática: evitar comandos o máximo possível entre serviços.
- Armadilha: trocar chamadas por mensagens que ainda são comandos ("faça isso") mantém o acoplamento e só muda o transporte, ver [[wiki/concepts/mensageria-vs-eda]].

Relacionados: [[wiki/concepts/event-driven-architecture]], [[wiki/concepts/acoplamento]], [[wiki/concepts/command-pattern]], [[wiki/concepts/choreography]].

## Key sources

- [[wiki/sources/arquitetura-orientada-a-eventos-luiz-gago-faria-otavio-santana-eduardo-macris]]
