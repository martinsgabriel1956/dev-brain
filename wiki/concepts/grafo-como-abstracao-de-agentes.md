---
type: concept
title: "Grafo Como Abstração de Agentes"
aliases: ["grafo de agentes", "G = (V, E) agentes", "nós e arestas de harness"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_count: 1
tags: [grafo, abstracao, agentes, langgraph, controle-de-fluxo, determinismo]
skill: tech-mentor-ai
status: draft
---

# Grafo Como Abstração de Agentes

Defesa de que o **grafo** — na definição clássica de teoria da computação, G = (V, E), vértices e arestas — é o nível de abstração correto para desenhar sistemas de agentes, porque separa com clareza o que deve ser decidido pela LLM do que deve ser decidido deterministicamente por quem constrói o sistema.

## A Divisão de Papéis

- **Nós (vértices)** — onde a computação acontece; tipicamente uma chamada de LLM, com custo computacional associado. É onde a LLM "trabalha bem": raciocínio, síntese, geração de texto/código.
- **Arestas** — condições de fluxo, definidas de forma **determinística** por quem projeta o sistema, não pela LLM. Decidem para onde o fluxo vai a seguir: aprovar/reprovar, repetir/seguir, rotear para qual subagente.

## Por Que Não Deixar a LLM Decidir Tudo

Existem decisões que são determinísticas por natureza (quantas tentativas de retry, qual critério de aprovação, quando parar um loop). Delegar essas decisões à LLM introduz variabilidade onde não é necessária e reduz o controle sobre o comportamento do sistema. A tese é: use computação de LLM nos nós, onde ela é insubstituível; use controle determinístico nas arestas, onde previsibilidade importa mais que criatividade.

## Independente de Framework

O grafo é uma ideia, não uma biblioteca. [[wiki/concepts/langgraph|LangGraph]] é uma implementação popular (nós tipados, checkpointing, state persistido), mas o mesmo desenho pode ser feito com scaffolding próprio, numa máquina de estado escrita à mão, ou até no papel. Quem já tem familiaridade com grafos de teoria da computação (ver [[wiki/concepts/algoritmos-de-grafo]]) reconhece o padrão sem depender de nenhuma ferramenta específica.

## Mudança de Nível de Abstração

Pensar em grafo desloca o trabalho de "escrever prompt para resolver este caso" para "desenhar a estrutura — nós e arestas — que resolve qualquer caso desta categoria". Essa é a mesma mudança de abstração central em [[wiki/concepts/loop-engineering]]: o engenheiro para de escrever instruções ad-hoc e passa a desenhar o sistema que gera e valida instruções.

## Key Sources

- [[wiki/sources/loop-engineering-planner-critic-grafo]]
