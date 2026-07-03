---
type: concept
title: "Complexidade Acidental"
aliases: ["accidental complexity", "essential complexity"]
date_created: 2026-05-31
date_updated: 2026-07-03
source_count: 2
tags: [complexidade-acidental, programacao-funcional, out-of-the-tar-pit, arquitetura]
skill: tech-mentor-backend
status: stable
---

# Complexidade Acidental

## TL;DR

Distinção do paper *"Out of the Tar Pit"* (Moseley & Marks): **complexidade essencial** vem do problema em si (inevitável); **complexidade acidental** vem das escolhas de implementação (evitável). [[Imutabilidade]] e controle de [[efeitos-colaterais]] eliminam a maior parte da complexidade acidental.

## Definição

> *"Mutable state and effects are the source of most of the accidental complexity in large systems."*
> — Out of the Tar Pit

| Tipo | Definição | Exemplo |
|------|-----------|---------|
| Essencial | Inerente ao problema | Regras de cálculo de juros compostos |
| Acidental | Vem da implementação | Bugs de estado mutável compartilhado |

## Fontes Principais de Complexidade Acidental

1. **Estado mutável compartilhado** — múltiplos componentes modificam o mesmo objeto
2. **[[Efeitos-colaterais]] implícitos** — funções que fazem mais do que prometem
3. **Acoplamento temporal** — ordem de execução importa de forma não declarada
4. **Concorrência sem estrutura** — threads acessando estado compartilhado

## Como Eliminar

- [[Programacao-funcional]]: imutabilidade por default, efeitos explícitos
- [[Ddd]]: domínio puro, efeitos nas periferias
- [[Event-sourcing]]: estado derivado de eventos imutáveis, não de mutações

## O Paper

*"Out of the Tar Pit"* (2006, Moseley & Marks) é o texto fundacional que influenciou as escolhas técnicas do [[nubank]]. O paper argumenta que a maioria dos bugs e da dificuldade de manutenção em sistemas grandes vem de estado mutável e efeitos colaterais — não da complexidade inerente do domínio.

## Segunda fonte da distinção: The Mythical Man-Month

[[wiki/sources/engenheiro-vs-programador-mercado-ia|A fonte]] cita a mesma dicotomia essencial/acidental a partir de *The Mythical Man-Month* (Frederick Brooks, 1975), independente de "Out of the Tar Pit": o programador lida com complexidade acidental o dia inteiro (configurar ferramenta, framework, dependências); o engenheiro foca em minimizar a complexidade acidental para lidar com a complexidade essencial do problema real. Ver [[wiki/concepts/engenheiro-vs-programador]].

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[wiki/sources/engenheiro-vs-programador-mercado-ia]] — mesma distinção essencial/acidental via Frederick Brooks (Mythical Man-Month), não Out of the Tar Pit
