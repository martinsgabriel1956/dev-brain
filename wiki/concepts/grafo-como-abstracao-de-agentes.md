---
type: concept
title: "Grafo Como Abstração de Agentes"
aliases: ["grafo de agentes", "G = (V, E) agentes", "nós e arestas de harness"]
date_created: 2026-07-10
date_updated: 2026-08-05
source_count: 2
tags: [grafo, abstracao, agentes, langgraph, controle-de-fluxo, determinismo, graph-engineering, ltv-cac]
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

## "Graph Engineering": o Mesmo Argumento a Partir de Métricas de Negócio

[[wiki/sources/graph-engineering-do-loop-ao-grafo]] chega à mesma tese por um caminho diferente — não subtarefas de código, mas **métricas de negócio interdependentes**. O argumento (atribuído a um tweet de [[wiki/entities/peter-steinberger]]): um loop de IA otimizando uma única métrica (ex.: CAC de uma campanha de marketing) pode melhorar essa métrica enquanto piora outra não observada (churn), derrubando o LTV e invalidando o próprio ganho — "uma métrica nunca é suficiente" (ver [[wiki/concepts/ltv-cac]]). Quando é preciso rodar múltiplos agentes otimizando múltiplas métricas que se afetam entre si, a estrutura necessária para representar essas relações para a IA é o grafo — os nós continuam sendo onde a computação (LLM) acontece, e as arestas passam a representar não só condição de fluxo determinística, mas a **relação causal entre métricas** (ex.: aresta entre "campanha" e "churn" com peso variável conforme a qualidade do lead).

Essa fonte também documenta o **peso da aresta como checklist de conclusão**, que "em algum momento envolve a aprovação de um ser humano" — reforçando, de outro ângulo, a mesma separação entre computação (nó/LLM) e controle determinístico (aresta) já defendida acima.

## Estruturas Não-Técnicas Que Já São Grafos

Gestão de projeto (épico → história → tarefa → subtarefa) é citada em [[wiki/sources/graph-engineering-do-loop-ao-grafo]] como exemplo de que uma estrutura pode parecer árvore e não ser: dependências cruzadas entre itens (uma história depende de outra, uma subtarefa bloqueia outra) quebram a propriedade de árvore e determinam quantos devs/agentes podem trabalhar em paralelo sem se bloquear — o mesmo raciocínio de nós e arestas aplicado antes mesmo de existir um agente de IA no processo.

## Key Sources

- [[wiki/sources/loop-engineering-planner-critic-grafo]]
- [[wiki/sources/graph-engineering-do-loop-ao-grafo]] — mesma tese (grafo como abstração correta para agentes) aplicada a métricas de negócio interdependentes em vez de subtarefas de código
