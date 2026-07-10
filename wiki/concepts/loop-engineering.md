---
type: concept
title: "Loop Engineering"
aliases: ["loop engineering", "engenharia de loop", "loop de harness"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_count: 1
tags: [loop-engineering, harness, agente, automacao, planner-executor-critic]
skill: tech-mentor-ai
status: draft
---

# Loop Engineering

Prática de desenhar o **ciclo completo** ao redor de um ou mais agentes — desde a entrada até a resposta final — como uma estrutura reutilizável e disparável automaticamente, em vez de escrever prompts manuais para cada tarefa. É o degrau seguinte a [[wiki/concepts/harness|harness engineering]] na progressão de abstração: prompt engineering melhora uma chamada, [[wiki/concepts/context-engineering-harness|context engineering]] melhora o contexto de uma chamada, harness engineering melhora o ambiente ao redor do modelo como um todo, e loop engineering melhora o ciclo inteiro que se repete.

## A Frase que Resume a Ideia

"Você não faz o prompt no agente, você desenha o sistema que faz o prompt." O trabalho de quem constrói o loop deixa de ser escrever instruções por tarefa e passa a ser desenhar a estrutura que gera instruções (e critérios de validação) para N tarefas, indefinidamente.

## Componentes de um Loop

Um loop de harness combina, tipicamente:

1. **[[wiki/concepts/planner-executor-critic|Planner]]** — LLM que decompõe a entrada em subtarefas, gerando prompt e [[wiki/concepts/rubrica-de-verificacao|rúbrica]] para cada uma
2. **Subagentes executores** — cada um recebe seu prompt gerado dinamicamente e produz um resultado (ver [[wiki/concepts/subagentes]])
3. **Verificador** — um modelo diferente do executor, que julga o resultado contra a rúbrica e aprova ou gera follow-up
4. **[[wiki/concepts/grafo-como-abstracao-de-agentes|Grafo]]** — a estrutura que controla o fluxo entre esses componentes, com condições de parada definidas por quem constrói o sistema (não pela LLM)

## Diferença para Harness Engineering

Harness engineering melhora o ambiente de uma única execução (tools disponíveis, contexto, memória — ver [[wiki/concepts/harness]]). Loop engineering trata a execução inteira como uma unidade repetível: o mesmo loop pode ser disparado por um prompt do usuário, por um schedule (ex.: rodar toda meia-noite verificando queda de vendas) ou por um evento externo, sem alterar a estrutura.

## Mudança de Nível de Abstração

Em vez de "eu crio código para resolver um problema", o loop resolve "uma categoria de problemas": o mesmo sistema (planner + subagentes + verificador) se adapta a diferentes entradas dentro do mesmo domínio, gerando harnesses dinamicamente para cada instância do problema.

## Risco Reconhecido: Não é o AutoGPT de Novo

Loops totalmente autônomos sem verificação (padrão AutoGPT/"AFF Loop") historicamente não avançaram — viravam sistemas rodando sem controle e sem garantia de qualidade. O que diferencia loop engineering, como descrito nesta fonte, é a combinação de rúbrica explícita + verificador com modelo distinto do executor + critério de parada definido pelo autor do sistema.

## Quando Vale a Pena

Para trabalho corporativo, pesquisa interna e entendimento de cliente (knowledge work), o padrão é descrito como altamente vantajoso. Para produção de codebase onde qualidade importa e token não é ilimitado, ainda é necessário um engenheiro por perto nos momentos de decisão — ver tensão equivalente em [[wiki/sources/vibe-coding-limites-maturidade-profissional]].

## Key Sources

- [[wiki/sources/loop-engineering-planner-critic-grafo]]
