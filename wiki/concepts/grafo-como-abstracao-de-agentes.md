---
type: concept
title: "Grafo Como Abstração de Agentes"
aliases: ["grafo de agentes", "G = (V, E) agentes", "nós e arestas de harness"]
date_created: 2026-07-10
date_updated: 2026-08-19
source_count: 4
tags: [grafo, abstracao, agentes, langgraph, controle-de-fluxo, determinismo, graph-engineering, ltv-cac, langchain, boris, erro-composto, graphrag]
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

## Terceira Fonte: LangChain Batiza o Termo, Boris Discute Publicamente

[[wiki/sources/ia-2026-nao-e-so-prompt-nem-so-agente-codigo-fonte-tv]] atribui de forma mais explícita a cunhagem do termo "graph engineering" à [[wiki/entities/langchain|LangChain]] (2026) — a mesma empresa por trás do [[wiki/concepts/langgraph|LangGraph]] — e cita [[wiki/entities/boris|Boris]], criador do [[wiki/entities/claude-code|Claude Code]], como voz recorrente discutindo graph engineering publicamente. Não contradiz a atribuição anterior (tweet de [[wiki/entities/peter-steinberger]] como origem prática da ideia) — a leitura consistente entre as duas fontes é: Steinberger e Boris discutiram/popularizaram a ideia, a LangChain formalizou o termo. Nenhuma das fontes traz link direto para verificação primária.

## Formalização com Quatro Componentes: Nós, Arestas, Estado, Verificação

[[wiki/sources/graph-engineering-matematica-do-erro-composto]] formaliza a definição já usada nesta página com dois componentes nomeados à parte, além de nós e arestas: **estado** (a informação que flui entre os nós — ex.: distância, num problema de caminho mais curto) e **verificação** (em cada nó, decide se o fluxo segue, volta para refazer ou para). A mesma fonte defende explicitamente que o grafo precisa ser **cíclico**, não unilateral — contraste citado com o Git, onde commits só avançam: um agente precisa poder dizer "esse valor veio errado, volta pro research e busca de novo", um retry de tool, sem que isso equivalha a abortar o fluxo.

## Verificador por Nó, Não um Único Gargalo

Extensão direta do argumento central de [[wiki/concepts/loop-engineering]] ("o gargalo de um loop é quem verifica"): num grafo, não existe um único verificador — é preciso um **verificador por nó**. Um nó sem verificação própria não é organização de agentes de verdade, é execução sem freio queimando token. Essa mudança de "um gargalo" para "N gargalos distribuídos" é o que aproxima grafos de agentes de sistemas distribuídos, com as complexidades já conhecidas dessa área ([[wiki/sources/graph-engineering-matematica-do-erro-composto]]).

## Erro Composto Também Entre Agentes (Não Só Dentro de Um Agente)

[[wiki/sources/graph-engineering-matematica-do-erro-composto]] estende a matemática de composição de erro já documentada em [[wiki/concepts/loop-engineering]] (95%/etapa × 50 etapas ≈ 60% de sucesso) para os **handoffs entre agentes**: se cada salto de informação entre agentes (ex.: planner → researcher → builder) preserva 85% da informação, a composição dá 85% em 1 salto, 72% em 2, 61% em 3 e 44% em 5 saltos — chamado de "telefone sem fio" acontecendo em milissegundos, com custo em tokens a cada rodada. O número 85% é hipotético/ilustrativo, não medido, mas o argumento estrutural reforça a mesma lição do vídeo anterior por um segundo ângulo: erro se compõe tanto dentro de um agente (etapa a etapa) quanto entre agentes (salto a salto).

## Contraponto: GraphRAG Não é Upgrade Automático

A mesma fonte cita um paper (não identificado por título/link) sobre GraphRAG que "frequentemente perde" para RAG vetorial simples em tarefas do mundo real, usado como aviso de que estrutura de grafo não é superioridade garantida em nenhum domínio — só compensa quando o problema realmente exige. A skill `tech-mentor-ai` [skill: tech-mentor-ai] (`references/ai/rag-advanced.md`) não confirma essa frase específica, mas confirma o padrão geral: GraphRAG tem custo de indexação alto e ganho concentrado em queries multi-hop, sem ser superior por padrão a RAG vetorial — consistente com a tese de que grafo tem custo real e só se paga em certas condições, já central nesta página.

## Data Concreta do Tweet-Origem: 18 de Julho

[[wiki/sources/graph-engineering-matematica-do-erro-composto]] é a primeira fonte na wiki a citar uma data concreta para o tweet de [[wiki/entities/peter-steinberger]] que teria disparado o termo — 18 de julho — ainda não verificada contra o tweet original.

## Estruturas Não-Técnicas Que Já São Grafos

Gestão de projeto (épico → história → tarefa → subtarefa) é citada em [[wiki/sources/graph-engineering-do-loop-ao-grafo]] como exemplo de que uma estrutura pode parecer árvore e não ser: dependências cruzadas entre itens (uma história depende de outra, uma subtarefa bloqueia outra) quebram a propriedade de árvore e determinam quantos devs/agentes podem trabalhar em paralelo sem se bloquear — o mesmo raciocínio de nós e arestas aplicado antes mesmo de existir um agente de IA no processo.

## Key Sources

- [[wiki/sources/loop-engineering-planner-critic-grafo]]
- [[wiki/sources/graph-engineering-do-loop-ao-grafo]] — mesma tese (grafo como abstração correta para agentes) aplicada a métricas de negócio interdependentes em vez de subtarefas de código
- [[wiki/sources/ia-2026-nao-e-so-prompt-nem-so-agente-codigo-fonte-tv]] — atribuição explícita da cunhagem do termo à LangChain (2026); Boris (Claude Code) citado como voz pública sobre o tema
- [[wiki/sources/graph-engineering-matematica-do-erro-composto]] — formalização com estado e verificação como componentes nomeados; exigência de ciclicidade; verificador por nó (não um único gargalo); erro composto também nos handoffs entre agentes (85%→44% em 5 saltos); contraponto do paper de GraphRAG; data do tweet-origem (18 de julho)
