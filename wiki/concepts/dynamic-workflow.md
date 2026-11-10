---
type: concept
title: "Dynamic Workflow"
aliases: ["Dynamic Workflows", "workflow dinâmico", "workflows dinâmicos", "workflow spec"]
date_created: 2026-11-10
date_updated: 2026-11-10
source_count: 1
tags: [dynamic-workflow, orquestracao, agentes, subagentes, harness, langgraph, claude-code]
skill: tech-mentor-ai
status: draft
---

# Dynamic Workflow

Workflow cuja estrutura é gerada por um modelo para cada problema e depois executada com controle programático. Fica entre o workflow estático, com passos definidos de antemão, e o agente livre, que decide cada passo enquanto trabalha. Segundo [[wiki/sources/dynamic-workflows-langgraph-engenharia-reversa-ronald-hulk]], é "o melhor dos dois mundos".

## Quando usar

O workflow estático funciona quando o problema é fácil de definir. Perguntas abertas e pesquisas não têm essa forma, e um agente puro pode abrir subagentes sem método e acumular contexto. O workflow dinâmico impõe [[wiki/concepts/padroes-de-workflow-dinamico|padrões]] e dá a cada etapa um contexto próprio, o que responde à [[wiki/concepts/degradacao-de-contexto]].

## Duas implementações

| | Claude Code `[external]` | Versão de [[wiki/entities/ronald-hulk]] |
|---|---|---|
| Artefato gerado | Script JavaScript | Workflow spec (critério de parada e de síntese, fases, subagentes, prompts) |
| Execução | Runtime isolado; o script não acessa arquivos nem shell, quem age são os agentes | Grafo fixo em [[wiki/concepts/langgraph]], parametrizado pela spec |
| Subagentes | 16 concorrentes e 1.000 por execução, por padrão | Subgrafos, até 160, valor configurável |
| Modelos | Claude, por agente | Qualquer um da [[wiki/entities/openrouter]], por nó |
| Onde roda | Sessões locais, cloud, `-p`, Agent SDK | Local ou servidor, segundo o autor |

Fontes do lado Claude Code: [documentação](https://code.claude.com/docs/en/workflows) e [anúncio de 28/05/2026](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code).

A diferença de fundo, por inferência: o Claude Code gera **código**, que pode expressar qualquer controle de fluxo; a versão em grafo gera **dados** para uma estrutura pronta, que só faz o que o esqueleto prevê. A segunda abre mão de expressividade e ganha previsibilidade.

## Fluxo da versão em grafo

1. Nó de comando escolhe o modo (`/pesquisar` ou `/auditoria`, com pesquisa como padrão).
2. Planner, com modelo maior, planeja sobre as fontes de dados disponíveis.
3. Nó de montagem transforma o plano na workflow spec.
4. Subagentes executam em subgrafos, cada um com um verificador que manda refazer ou registra um warning.
5. Avaliador global confere o conjunto.
6. Síntese produz o relatório.

## Limites

- Repetibilidade vale para o controle de fluxo; o plano e as saídas das LLMs ainda variam (inferência, ver [[wiki/concepts/determinismo-vs-probabilismo-em-ia]]).
- O consumo de tokens é alto: o post da Anthropic alerta para "significantly more tokens" `[external]`.
- A implementação em LangGraph não é pública, e o vídeo não traz medições.

## Relações

[[wiki/concepts/planner-executor-critic]] · [[wiki/concepts/grafo-como-abstracao-de-agentes]] · [[wiki/concepts/subagentes]] · [[wiki/concepts/harness]] · [[wiki/concepts/camada-de-aplicacao-vs-modelo]] · [[wiki/concepts/modalidades-de-paralelismo-claude-code]]

## Key Sources

- [[wiki/sources/dynamic-workflows-langgraph-engenharia-reversa-ronald-hulk]]
