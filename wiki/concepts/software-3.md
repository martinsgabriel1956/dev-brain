---
type: concept
title: "Software 3.0"
aliases: ["software 3.0", "Software 2.0", "programação por prompts"]
date_created: 2026-05-17
date_updated: 2026-06-01
source_count: 2
tags: [prompt-engineering, llm, software-3, karpathy, paradigma]
skill: tech-mentor-ai
status: stable
---

# Software 3.0

## Definição

Conceito cunhado por **Andrej Karpathy** (ex-head de IA da Tesla, fundador da Eureka Labs) para descrever a terceira geração de programação — onde a lógica é especificada em **linguagem natural via prompts**, não em código imperativo ou pesos de redes neurais.

Origem: [Twitter exchange com Chris Olah](https://twitter.com/karpathy/status/1273788774422441984), 2020.

## As Três Gerações

| Geração | Paradigma | Como se programa |
|---|---|---|
| **Software 1.0** | Código imperativo | Escrever instruções explícitas em linguagem de programação |
| **Software 2.0** | Pesos de redes neurais | Definir arquitetura + loss function; otimização encontra os pesos |
| **Software 3.0** | Prompts em linguagem natural | Descrever o comportamento desejado em texto; o LLM executa |

## Implicações

- [[prompt-engineering]] é uma skill de engenharia de software — não é "apenas escrever texto".
- A qualidade do output depende da qualidade do prompt assim como a qualidade de um software 1.0 depende da qualidade do código.
- Prompt engineering é iterável: ciclo de feedback muito mais rápido que treinar um modelo.
- O "programa" é o prompt — deve ser versionado, testado e mantido como código.

## Limitações do Conceito

- Prompts não têm garantias formais de correção — outputs são probabilísticos.
- Debugging é mais difícil: não há stack trace, só observação empírica.
- Em 2026, reasoning models (o1, o3, Claude extended thinking) internalizam parte do raciocínio — o papel do prompt muda para especificação de objetivo mais do que de processo.

## Relação com Outros Conceitos

- [[prompt-engineering]] — a prática central do Software 3.0
- [[in-context-learning]] — o mecanismo que torna o Software 3.0 possível
- [[foundation-model]] — o substrato sobre o qual o Software 3.0 opera

## Entidades

- [[wiki/entities/andrej-karpathy]] — cunhou o conceito

## Programação = Descrição Inambígua (Dijkstra)

A conexão entre Software 3.0 e a crítica de [[wiki/entities/edsger-dijkstra]] é direta: se "o ato de descrever um programa de forma inambígua e o ato de programar são a mesma coisa", então a LLM como executor de descrições em linguagem natural é a realização literal dessa ideia.

O limite prático: **a LLM replicará as ambiguidades da descrição**. Se o prompt não especifica validação, mutabilidade ou paralelismo, o código gerado também não especificará. Verificado empiricamente com GPT-4.1 — a descrição em português produziu o mesmo código Python com as mesmas omissões.

## Fontes

- [[wiki/sources/microsoft-prompt-engineering-guide]]
- [[wiki/sources/logica-de-programacao-o-que-e-de-verdade]] — demonstração empírica de que LLM replica ambiguidades do prompt; crítica de Dijkstra como fundamento teórico
