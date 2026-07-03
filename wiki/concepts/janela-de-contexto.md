---
type: concept
title: "Janela de Contexto"
aliases: ["context window", "context length", "janela de tokens"]
date_created: 2026-05-18
date_updated: 2026-07-03
source_count: 3
tags: [llm, tokens, agentes-ia, llmops]
skill: tech-mentor-ai
status: draft
---

## Definição

Quantidade máxima de tokens que um modelo de linguagem consegue processar em uma única chamada — incluindo o histórico de conversa, instruções de sistema, resultados de ferramentas e a resposta gerada. Define o "alcance de memória ativa" do modelo.

---

## Relevância para Agentes

Em ferramentas como Claude Code, a janela de contexto acumula ao longo de uma sessão. Quando esgotada (ou após um período configurado — ex.: 3–5h), ocorre um **reset**: o contexto é zerado e o agente perde a "memória" da sessão.

Esse mecanismo de reset é o gatilho principal para o fenômeno [[token-anxiety]]: a janela finita cria urgência para maximizar o uso antes do próximo reset.

## Trade-offs

| Janela menor | Janela maior |
|---|---|
| Mais barato por chamada | Mais caro por chamada |
| Reset mais frequente | Sessões mais longas sem interrupção |
| Menos contexto retido | Risco de "perda de foco" do modelo em sessões longas |

## Evolução

Modelos mais recentes têm expandido consistentemente o tamanho da janela (de 4k → 8k → 100k → 200k+ tokens). Paradoxalmente, janelas maiores não eliminam a ansiedade — ver [[token-anxiety]] sobre o paradoxo dos modelos mais capazes.

---

## Economizando Janela com Multi-Agent

Duas estratégias reduzem a pressão sobre a janela de contexto do agente principal: [[wiki/concepts/subagentes]] (delega sub-tarefas a janelas de contexto separadas, só o resultado final retorna) e [[wiki/concepts/worktree-paralelismo]] (paraleliza a nível de file system, sem nem compartilhar contexto entre agentes). Restringir as `tools` disponíveis a um subagente também reduz o tamanho do seu system prompt.

## Idioma Afeta o Consumo da Janela

O custo em tokens de um texto não é neutro em relação ao idioma. Devido ao [[byte-pair-encoding]], escrever em português consome **62% mais tokens** do que o equivalente em inglês — ver [[token-tax-multilingual]].

Na prática: um `CLAUDE.md` de 500 linhas em português esgota 62% mais contexto por sessão do que em inglês. Em uso intenso com [[spec-driven-development]], esse multiplicador é um custo real.

---

## Key Sources

- [[wiki/sources/token-anxiety-agentes-ia-comportamento-devs]]
- [[wiki/sources/custo-tokens-portugues-vs-ingles]]
- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
