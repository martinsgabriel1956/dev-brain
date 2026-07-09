---
type: concept
title: "YAGNI — You Ain't Gonna Need It"
aliases: ["yagni", "you ain't gonna need it", "não vou precisar disso"]
date_created: 2026-04-23
date_updated: 2026-07-09
source_count: 4
tags: [arquitetura, principios, pragmatismo, over-engineering, xp]
skill: tech-mentor-backend
status: stable
---

# YAGNI — You Ain't Gonna Need It

Princípio do Extreme Programming (Kent Beck, 1999): não implemente algo até que você *precise* — não até que você *acha* que vai precisar.

## O Princípio

> "Tu não precisa de algo até precisar. E quando precisar, refatora — porque código simples é mais fácil de refatorar do que a abstração que tu tentou adivinhar ao futuro."

A maioria dos "e se um dia mudar X" nunca acontece. E quando acontece, a realidade é tão diferente do que foi imaginado que a abstração preventiva atrapalha em vez de ajudar.

## Por Que Fica Pior com IA

A IA escalou o problema do YAGNI. Antes, criar abstração preventiva levava dias de trabalho. Hoje: dois prompts e está lá. O custo de geração caiu. O custo de manutenção permanece igual — ou subiu, porque agora o codebase tem mais arquivos para agentes navegarem.

Ver [[concepts/abstraction-bloat]] — o agente gera 1000 linhas onde 100 bastariam por viés de treinamento.
Ver [[concepts/abstraction-illusion]] — a IA torna padrões acessíveis sem torná-los apropriados.

## Quando Aplicar

A abstração é justificada quando a dor é real:
- Você trocou essa dependência nos últimos 2 anos? Se não → não abstrai
- Tem um segundo caso de uso real agora? Se sim → extrai (após o segundo caso, nunca antes)
- O contrato de um serviço externo vai poluir seu domínio? → Anticorruption Layer

## Relação com Outros Princípios

YAGNI não contradiz DDD ou Clean Architecture — ele questiona a *implementação ritualística*. Os princípios estratégicos (bounded context, separação de domínio e infra) continuam válidos. O que YAGNI questiona é: interface para cada repositório com uma única implementação, use case para cada operação CRUD, mappers em todas as direções.

Ver também [[wiki/concepts/fazer-a-coisa-mais-simples-que-poderia-funcionar]] — mesmo espírito de XP/Kent Beck aplicado a um eixo diferente: YAGNI questiona *o que construir agora*, o outro questiona *quão complexa deve ser a solução do problema atual*.

## Key Sources

- [[sources/clean-architecture-ia-custo-real]]
- [[sources/super-productivity-ai-architecture-guide]]
- [[sources/addy-osmani-80-problem-agentic-coding]]
- [[wiki/sources/5-principios-que-mudaram-como-programador]]
