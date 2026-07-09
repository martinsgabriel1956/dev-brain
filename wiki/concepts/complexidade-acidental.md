---
type: concept
title: "Complexidade Acidental"
aliases: ["accidental complexity", "essential complexity"]
date_created: 2026-05-31
date_updated: 2026-07-09
source_count: 4
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

## Terceira fonte: por que a indústria vendeu "aprenda o framework" como suficiente

[[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] usa a mesma dicotomia para explicar por que operadores de CRUD travam quando o sistema escala: aprender o framework da vez resolve só a complexidade acidental — e a indústria vendeu essa parte como a história toda (sobretudo até ~2022) porque era a necessidade imediata do mercado. A complexidade essencial (concorrência, consistência, falha, escala) só aparece quando o sistema cresce, a rede falha no meio de uma transação, ou duas requisições colidem — e é aí que quem só sabe CRUD fica refém do framework.

## Quarta fonte: definição de Ousterhout via estrutura, não implementação

[[wiki/entities/john-ousterhout]] (*A Philosophy of Software Design*) formula a mesma ideia com outro vocabulário: complexidade é "qualquer coisa relacionada à **estrutura** de um sistema que dificulta entender e modificar o sistema" — uma base de código ruim é a que é difícil de mudar sem causar bugs. [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] usa essa definição para argumentar que módulos rasos ([[wiki/concepts/modulo-profundo]]) são uma fonte estrutural de complexidade acidental — o problema não está no domínio, está em como o código foi organizado, e piora ciclicamente quando um agente de IA gera código sobre uma estrutura já ruim sem nunca reestruturar.

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[wiki/sources/engenheiro-vs-programador-mercado-ia]] — mesma distinção essencial/acidental via Frederick Brooks (Mythical Man-Month), não Out of the Tar Pit
- [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] — por que "aprenda o framework" foi vendido como suficiente até o sistema escalar
- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] — definição de Ousterhout (estrutura, não implementação) e módulos rasos como fonte de complexidade
