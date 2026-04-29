---
type: concept
title: "Abstraction Illusion"
aliases: ["abstraction illusion", "ilusão de abstração", "padrão acessível não apropriado"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 3
tags: [ia, arquitetura, over-engineering, constraints, decisao]
skill: tech-mentor-backend
status: stable
---

# Abstraction Illusion

Conceito cunhado pelo Super Productivity Blog: a IA torna padrões sofisticados *acessíveis* sem torná-los *apropriados*. A barreira mudou de "você consegue construir?" para "você deveria construir?" — e a IA não ajuda com a segunda pergunta.

## O Exemplo Canônico

> "Você pediu ao assistente de IA como estruturar um novo serviço. Ele sugeriu Event Sourcing com CQRS, arquitetura hexagonal com ports e adapters, e saga pattern para transações distribuídas. Seis meses depois, seu time de três mantém uma infraestrutura de Event Sourcing para um sistema com 200 requests por dia. Cada feature leva três vezes mais tempo."

## O Filtro Natural que Desapareceu

Antes da IA, implementar Event Sourcing exigia:
- Ler livros sobre o padrão
- Estudar exemplos reais
- Construir incrementalmente

Esse processo filtrava naturalmente os times que não precisavam do padrão. Hoje: CQRS completo em uma tarde. O filtro desapareceu. Você ainda paga o custo de manutenção indefinidamente.

## Relação com Abstraction Bloat

[[concepts/abstraction-bloat]] é o efeito prático da abstraction illusion: o agente gera a complexidade desnecessária porque foi pedido a "fazer bem" e "bem" é a média ponderada de blog posts de tech.

## Como Evitar

A resposta é constraints-first:
1. Escreva suas constraints reais *antes* de perguntar qualquer coisa à IA
2. Use a IA para explorar opções, não para tomar a decisão
3. Aplique o teste de adequação: "esse padrão resolve um problema *real* no *meu* contexto?"
4. Prefira a opção mais reversível quando empatado

Ver [[sources/super-productivity-ai-architecture-guide]] — workflow de 7 passos e 10 perguntas de adequação.

## Key Sources

- [[sources/super-productivity-ai-architecture-guide]]
- [[sources/clean-architecture-ia-custo-real]]
- [[sources/overengineering-carol-ate-quinta]]
