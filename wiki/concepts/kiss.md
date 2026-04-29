---
type: concept
title: "KISS — Keep It Simple"
aliases: ["kiss", "keep it simple", "pensar simples", "simplicidade intencional"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
tags: [kiss, over-engineering, principios, qualidade, design-patterns]
skill: tech-mentor-backend
status: stable
---

## Definição

KISS (Keep It Simple, Stupid / Keep It Simple and Stupid) é o princípio de evitar aumentar a complexidade de uma solução além do necessário para resolver o problema. Não é limitação de conhecimento — é disciplina intencional de suprimir complexidade desnecessária.

## O paradoxo da expertise

Pensar simples é fácil quando você sabe pouco — você está limitado pelo próprio conhecimento.

Pensar simples é difícil quando você sabe muito — você precisa ativamente escolher não aplicar tudo que sabe. O viés de complexidade cresce com a experiência.

> "Lá na frente pensar simples é uma das coisas mais difíceis na programação quando você tem bagagem e conhecimento."
> — Carol (Até Quinta)

## O que KISS não é

- **Não é defender código bagunçado.** Código simples ≠ código feio ≠ gambiarra.
- **Não é ignorar padrões.** É saber quando aplicá-los.
- **Não é anti-escabilidade.** É distinguir escalabilidade real de escalabilidade hipotética.

## Teste KISS

Antes de adicionar uma abstração, padrão ou camada:
1. Qual requisito real justifica isso agora?
2. Qual dev do time consegue manter isso sem o meu contexto?
3. Quantos arquivos preciso alterar para mudar um comportamento?
4. A explicação da solução é mais complexa que o problema?

Se qualquer resposta for "nenhum", "ninguém", ">3" ou "sim" — reavalie.

## Relação com outros princípios

- **YAGNI** (You Aren't Gonna Need It) — complementar: não adicione o que não é necessário agora.
- **[[concepts/over-engineering]]** — KISS é o antídoto.
- **[[concepts/accidental-complexity]]** — KISS é a prática que previne complexidade acidental.

## Key Sources

- [[sources/overengineering-carol-ate-quinta]]
