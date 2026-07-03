---
type: concept
title: "Ciclo do Agente (Agent Loop)"
aliases: ["agent loop", "ciclo agentico", "prompt tool call loop"]
date_created: 2026-06-02
date_updated: 2026-07-03
source_count: 4
tags: [agente, tool-call, harness, ciclo, loop]
skill: tech-mentor-ai
status: stable
---

# Ciclo do Agente (Agent Loop)

O padrão de execução fundamental de qualquer agente baseado em LLM: receber input, decidir entre responder ou invocar ferramentas, executar ferramentas, acumular resultados no contexto, e repetir até ter condições de produzir uma resposta final ao usuário.

## O Loop

```
[Usuário envia prompt]
        ↓
[Harness monta contexto completo]
   ├── System prompt (rules, skills, CLAUDE.md)
   ├── Tools disponíveis (schemas)
   ├── Histórico da conversa
   └── Resultados de tool calls anteriores
        ↓
[LLM processa e decide]
   ├── → Resposta final (sai do loop)
   └── → Tool call request (continua o loop)
        ↓
[Harness executa a tool na máquina do usuário]
        ↓
[Resultado entra no contexto]
        ↓
[Volta para LLM processar]
```

## Implicações Práticas

### Custo Não Linear
Um único prompt pode disparar N ciclos. Cada ciclo = mais tokens no contexto (acúmulo). Prompt impreciso → mais ciclos de exploração → custo maior.

**Exemplo** (Branas, Aula 04):
- Prompt: "o código não funciona, corrija"
- Sem contexto: 7 tool calls (list_dir → read 4 arquivos → localizar bug → editar → executar)
- Com contexto ("em coupon.ts, no calculateDiscount"): 1 tool call

### 40+ Ciclos por Prompt
Tarefas complexas podem gerar dezenas de iterações de tool call→contexto→decisão antes da resposta final. O usuário só vê o resultado; o ciclo interno é invisível (a menos que o harness exponha um log).

### Onde Ocorre a Inteligência
O LLM decide a sequência de ações. A qualidade da sequência depende de:
1. Qualidade do prompt/spec (contexto de domínio)
2. Qualidade das tools disponíveis
3. Qualidade do treinamento do modelo para tool calling

## Diferença de Chatbot Simples

| Chatbot | Agente |
|---|---|
| 1 turn: prompt → resposta | N turns internos antes da resposta final |
| Stateless (sem memória) | Contexto acumulado com tool results |
| Não executa código | Executa código, lê arquivos, etc. |
| Baixo custo por interação | Custo variável e potencialmente alto |

## Sensores Reduzem Iterações

Cada sensor (teste, linter, bash execute) que fornece feedback reduz o número de ciclos necessários para a LLM chegar ao resultado correto. Sem sensores → LLM executa às cegas → mais iterações → mais custo. Ver [[wiki/concepts/sensores-vs-guias]].

## Conter o Crescimento do Ciclo com Subagentes

Delegar parte do ciclo a um [[wiki/concepts/subagentes|subagente]] evita que os tool calls intermediários dessa sub-tarefa acumulem na janela de contexto do agente pai — só o resultado final retorna. É uma forma de manter o loop principal curto mesmo quando a tarefa geral exige muitos ciclos internos (ex.: pesquisa em múltiplas fontes em paralelo).

## É um Brute-Force Até Funcionar

> "É um baita brute-force. É um brute-force até funcionar." — Rodrigo Branas

O loop agêntico não é elegante — é iterativo e incremental. A qualidade dos guias e sensores determina quantas iterações são necessárias.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-01-context-harness-engineering]]
- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
