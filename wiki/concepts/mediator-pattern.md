---
type: concept
title: "Mediator Pattern"
aliases: ["mediator", "padrão mediador"]
date_created: 2026-05-05
date_updated: 2026-11-03
source_count: 3
tags: [design-patterns, behavioral, mediator, gof]
skill: tech-mentor-backend
status: stub
---

# Mediator Pattern

Padrão [[behavioral-patterns|comportamental]] que define um objeto que encapsula como um conjunto de objetos interage. O Mediator promove o desacoplamento ao evitar que objetos se refiram uns aos outros explicitamente — eles se comunicam apenas através do mediador.

## Distinção do Facade

| | [[facade-pattern]] | Mediator |
|---|---|---|
| Propósito | Simplificar acesso a subsistema | Centralizar comunicação entre componentes |
| Subsistema ciente? | Não | Sim — componentes conhecem o mediador |
| Nova funcionalidade? | Não | Pode adicionar lógica de coordenação |
| Comunicação interna | Objetos se comunicam diretamente | Tudo passa pelo mediador |

## Casos de uso típicos

- Sistema de chat (usuários não se comunicam diretamente — passam pelo servidor)
- Formulários complexos com campos interdependentes
- Sistemas de controle de tráfego aéreo

## Mediator como camada a justificar

[[wiki/sources/como-evitar-overengineering-kiss-yagni-decisoes-embasadas-abordagem-evolutiva]] cita o Mediator como exemplo de camada extra no código, que precisa ter vantagens, desvantagens e impacto avaliados antes da adoção. Ver [[wiki/concepts/decisao-tecnica-embasada-em-metricas]].

## Key Sources

- [[wiki/sources/design-pattern-facade]] — mencionado nas relações com outros padrões
- [[wiki/sources/design-pattern-observer]] — distinção Mediator vs Observer aprofundada; podem ser usados juntos
- [[wiki/sources/como-evitar-overengineering-kiss-yagni-decisoes-embasadas-abordagem-evolutiva]] — camada extra a justificar antes de adotar
