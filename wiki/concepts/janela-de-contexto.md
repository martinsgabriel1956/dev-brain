---
type: concept
title: "Janela de Contexto"
aliases: ["context window", "context length", "janela de tokens"]
date_created: 2026-05-18
date_updated: 2026-08-20
source_count: 5
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

## Heurística de Campo: ~200k Tokens Mesmo com Janelas de 1M

Mesmo com janelas de contexto de até 1M de tokens disponíveis, a recomendação prática registrada em [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]] é manter o uso em torno de ~200k tokens — quanto maior a proporção da janela ocupada, maior a chance de alucinação. É a mesma lógica por trás de [[wiki/concepts/rpi-workflow]] e [[wiki/concepts/spec-driven-development]]: salvar research e planejamento em Markdown fora da janela, para que a implementação comece com contexto baixo mesmo em mudanças que tocam dezenas de arquivos.

## O Que Está Fora da Janela Não Existe

[[wiki/sources/engenharia-de-contexto-vs-prompt-engineering-gargalo-real-times-ia]] reforça, com um caso concreto, um ponto frequentemente subestimado: o modelo não "esquece" o que não está na janela — aquilo **nunca esteve lá**. Um projeto real acumula anos de regras de negócio e decisões de arquitetura que vivem, na melhor das hipóteses, na cabeça de duas ou três pessoas; se essas regras não foram transformadas em artefato dentro do repositório (ver [[wiki/concepts/context-engineering-harness]]), o prompt mais detalhado do mundo não as coloca na janela. A fonte ilustra com um serviço de cobrança recorrente gerado com um prompt caprichado (idempotência, formato de resposta, tratamento de erro especificados) que ignorou uma regra central — cobrança deve passar por fila de auditoria — documentada em um arquivo que a IA nunca leu. A analogia usada: instruções detalhadíssimas para uma pessoa vendada numa sala que ela nunca viu, seguidas da reclamação de que ela esbarrou no móvel.

## Key Sources

- [[wiki/sources/token-anxiety-agentes-ia-comportamento-devs]]
- [[wiki/sources/custo-tokens-portugues-vs-ingles]]
- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
- [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]] — heurística de ~200k tokens mesmo com janelas de 1M disponíveis
- [[wiki/sources/engenharia-de-contexto-vs-prompt-engineering-gargalo-real-times-ia]] — caso concreto de regra de negócio fora da janela (fila de auditoria de cobrança) e a analogia da pessoa vendada
