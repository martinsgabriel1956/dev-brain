---
type: concept
title: "Ciclo do Agente (Agent Loop)"
aliases: ["agent loop", "ciclo agentico", "prompt tool call loop"]
date_created: 2026-06-02
date_updated: 2026-07-28
source_count: 7
tags: [agente, tool-call, harness, ciclo, loop, ralph-loop]
skill: tech-mentor-ai
status: stable
---

# Ciclo do Agente (Agent Loop)

O padrão de execução fundamental de qualquer agente baseado em LLM: receber input, decidir entre responder ou invocar ferramentas, executar ferramentas, acumular resultados no contexto, e repetir até ter condições de produzir uma resposta final ao usuário. É a implementação prática do padrão **ReAct** (Reason + Act, 2022/2023) — um ciclo que agrega a resposta anterior ao contexto e repete até concluir a tarefa. É a base sobre a qual [[wiki/concepts/harness|harness]] e [[wiki/concepts/loop-engineering|loop engineering]] foram construídos, não um conceito à parte deles ([[wiki/sources/loop-engineering-harness-e-a-frase-que-viralizou]]).

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

## Sistematizando o Brute-Force com Rúbrica e Verificador

[[wiki/concepts/planner-executor-critic|Planner-Executor-Critic]] adiciona estrutura a esse brute-force: em vez de o ciclo repetir tool calls até o próprio executor "achar" que terminou, uma [[wiki/concepts/rubrica-de-verificacao|rúbrica]] explícita e um verificador (modelo diferente do executor) decidem objetivamente quando parar. Não elimina a natureza iterativa do ciclo, mas torna o critério de parada determinístico em vez de implícito.

## Erros se Compõem ao Longo do Brute-Force

O "brute-force até funcionar" tem um custo matemático explícito: um processo de N etapas, cada uma com 99% de sucesso individual, não tem 99% de chance de sucesso completo — tem 0,99ᴺ (≈90,4% em 10 etapas, ≈60% em 50). Ver [[wiki/concepts/harness]] para os quatro mecanismos que atacam essa composição de erros ([[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]]).

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-01-context-harness-engineering]]
- [[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]] — matemática de erros compostos (0,99ᴺ) aplicada ao ciclo de múltiplas etapas
- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
- [[wiki/sources/loop-engineering-planner-critic-grafo]] — critério de parada explícito (rúbrica + verificador) para o ciclo agêntico
- [[wiki/sources/loop-engineering-harness-e-a-frase-que-viralizou]] — nomeia o ciclo como implementação do padrão ReAct (2022/2023), origem histórica anterior ao termo "loop engineering"
