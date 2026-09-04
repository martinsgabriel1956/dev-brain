---
type: concept
title: "Requisitos Funcionais e Não Funcionais"
aliases: ["requisitos funcionais", "requisitos não funcionais", "RNF", "functional requirements", "non-functional requirements", "levantamento de requisitos"]
date_created: 2026-09-03
date_updated: 2026-09-03
source_count: 2
tags: [system-design, requisitos, arquitetura, entrevistas, escopo]
skill: tech-mentor-system-design
status: stub
---

# Requisitos Funcionais e Não Funcionais

Os dois eixos que precisam ser levantados **antes** de qualquer decisão de arquitetura — e a etapa que candidatos pulam com mais frequência em [[wiki/concepts/entrevista-system-design|entrevistas de system design]].

- **Requisitos funcionais** definem *como o negócio funciona*: quais features existem, quais regras as governam, quais limites se aplicam, o que está dentro e o que está fora do escopo.
- **Requisitos não funcionais (RNF)** definem *sob que condições o sistema precisa operar*: latência, disponibilidade, consistência, retenção de dados, volume de tráfego, constraints de custo e prazo.

## Por que a ordem importa

Requisitos funcionais vêm primeiro porque delimitam o que existe; RNFs vêm depois porque qualificam aquilo que já foi delimitado. Mas são os **RNFs que separam uma solução de brinquedo de uma solução de escala** — a mesma lista de features roda numa VPS barata para mil usuários e exige cache, replicação e particionamento para milhões ([[wiki/sources/anatomia-entrevista-system-design-bigtech]]).

## As perguntas mínimas

[[wiki/sources/tres-mentiras-que-te-reprovam-em-entrevistas-de-arquitetura-de-sistemas]] reduz o levantamento a três perguntas obrigatórias diante de um enunciado vago ("construa a arquitetura de um e-commerce"):

1. **Quem vai usar isso, e quantos usuários a gente espera?** → alimenta as [[wiki/concepts/estimativas-back-of-envelope|estimativas back-of-envelope]].
2. **Quais são as funcionalidades principais?** → separa core de auxiliar; o desenho foca nas core.
3. **Tem algum requisito não funcional crítico?** → é o que muda a arquitetura, não a lista de features.

Cada uma leva a uma decisão de arquitetura diferente. Não perguntá-las e sair desenhando componentes é o antipadrão nº 1 da sessão.

O framework de 4 etapas da skill de system design formaliza o mesmo passo como *Clarify Requirements* (~5 min): escopo (IN/OUT), escala (usuários, RPS, volume), RNFs (latência, disponibilidade, consistência) e constraints técnicas (stack existente, budget, prazo). `[skill: tech-mentor-system-design → references/system-design.md]`

## Relação com escopo aberto

Um enunciado de entrevista é, por construção, um [[wiki/concepts/problema-de-escopo-aberto]]: o entrevistador entrega vagueza de propósito. Levantar requisitos é o ato de operacionalizá-lo — transformar o problema aberto em um conjunto de problemas fechados que podem ser resolvidos e defendidos.

## Key Sources

- [[wiki/sources/tres-mentiras-que-te-reprovam-em-entrevistas-de-arquitetura-de-sistemas]] — as três perguntas mínimas; pular esta etapa é a "mentira nº 1" (achar que o enunciado já define o problema)
- [[wiki/sources/anatomia-entrevista-system-design-bigtech]] — funcionais antes de não funcionais; RNFs como o que separa solução de VPS de solução de bigtech
