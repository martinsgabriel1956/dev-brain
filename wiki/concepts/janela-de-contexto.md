---
type: concept
title: "Janela de Contexto"
aliases: ["context window", "context length", "janela de tokens"]
date_created: 2026-05-18
date_updated: 2026-05-18
source_count: 1
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

## Key Sources

- [[wiki/sources/token-anxiety-agentes-ia-comportamento-devs]]
