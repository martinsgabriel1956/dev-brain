---
type: concept
title: "Tool Call"
aliases: ["function calling", "tool use", "chamada de ferramenta"]
date_created: 2026-06-02
date_updated: 2026-08-13
source_count: 7
tags: [tool-call, harness, agente, llm, function-calling, tool-overload]
skill: tech-mentor-ai
status: stable
---

# Tool Call

Mecanismo introduzido pela OpenAI em 2023 que permite a um LLM requisitar a execução de funções externas registradas no [[wiki/concepts/harness]]. Considerado o segundo grande game changer da história dos LLMs (o primeiro foi a abertura como API). Deu ao modelo a capacidade de agir sobre o mundo real em vez de apenas gerar texto.

## Como Funciona

1. O harness registra um conjunto de tools disponíveis (nomes + descrições + schemas de parâmetros) no contexto enviado ao modelo.
2. O modelo, em vez de responder diretamente, pode emitir uma "chamada de ferramenta" indicando qual tool invocar e com quais parâmetros.
3. **O harness recebe essa chamada e executa a tool na máquina do usuário** — não nos servidores do provider.
4. O resultado da execução é injetado de volta no contexto como mensagem do sistema.
5. O modelo decide: mais tool calls ou resposta final ao usuário.

## Tools Fundamentais

| Tool | O que faz |
|---|---|
| `read_directory` | Lista arquivos de um diretório |
| `read_file` | Lê conteúdo de um arquivo |
| `write_file` | Cria ou sobrescreve um arquivo |
| `edit_file` | Aplica patches em arquivo existente |
| `execute_bash` | Roda comandos shell (npm, git, make…) |
| `web_search` | Busca na internet |
| `browser` | Abre URL, tira screenshot, inspeciona DOM |

## Por Que Importa Para o Dev

- **1 prompt → N tool calls**: uma instrução vaga pode gerar dezenas de ciclos internos, cada um consumindo tokens. Contexto explícito reduz ciclos e custo.
- **Qualidade do tool call = qualidade do harness**: dois harnesses com o mesmo modelo entregam resultados diferentes porque implementam as tools de formas diferentes (ex: um usa grep, outro usa RAG para busca de arquivo).
- **Modelos treinados em tool call**: GPT-5.x, Opus 4.7, Kimi K2.6 têm fine-tuning específico para continuar executando loops de tool calls sem parar prematuramente. Modelos antigos (GPT-4.1) paravam no meio do loop.
- **Segurança**: tools rodam na sua máquina. Uma skill ou MCP malicioso pode usar tool calls para exfiltrar dados, deletar arquivos, etc.

## Tools Nativas do Claude Code

| Tool | O que faz |
|---|---|
| `Agent`/`Task` | Lança [[wiki/concepts/subagentes]] em paralelo |
| `AskUserQuestion` | Faz perguntas ao usuário antes de prosseguir |
| `Bash` | Executa comandos shell |
| `Glob` | Acha arquivos por pattern matching (nome/path) |
| `Grep` | Acha conteúdo dentro de arquivos por pattern matching |
| `Read`/`Write`/`Edit` | Lê, cria/sobrescreve e edita arquivos |

Restringir as tools disponíveis a um [[wiki/concepts/subagentes|subagente]] (ex.: um "code reviewer" só com `Read`/`Grep`/`Glob`/`Bash`, sem `Write`/`Edit`) reduz o system prompt desse subagente e, com isso, o consumo de tokens — a mesma lógica de "escolher a tool certa para a tarefa certa" descrita acima.

## Menos Ferramentas Pode Ser Melhor que Mais (Caso Vercel)

Contraintuitivo: mais ferramentas disponíveis não significa menos erro. A [[wiki/entities/vercel]] testou um agente interno com muitas ferramentas e performance ruim; em vez de adicionar mais, **removeu 80% das ferramentas disponíveis**, e a performance melhorou — cada etapa passou a exigir escolher entre menos opções, reduzindo o espaço de decisão e a chance de escolha errada ([[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]]). Reforça a mesma lógica já descrita acima para subagentes restritos: harness não é sobre maximizar capacidade, é sobre otimizar o caminho até o resultado certo.

## Tool Call Como Mitigação de Alucinação

Forçar o modelo a usar `web_search` antes de responder (em vez de confiar na resposta crua do treinamento) ancora a resposta numa fonte verificável em tempo real, reduzindo [[wiki/concepts/alucinacao-llm]] na prática — mesmo princípio ao pedir para o modelo rodar testes (`execute_bash`) antes de declarar código como correto, em vez de aceitar a alegação do próprio modelo. Ver [[wiki/sources/porque-nunca-confiar-em-llm-alucinacao]].

## Analogia

Assim como um programa em JavaScript não sabe que horas são e faz uma syscall ao OS para obter o timestamp, o LLM não sabe o que tem no seu filesystem e faz uma "syscall" ao harness para descobrir.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
- [[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]] — caso Vercel: remover 80% das ferramentas disponíveis melhorou performance do agente
- [[wiki/sources/porque-nunca-confiar-em-llm-alucinacao]] — `web_search` e execução de testes como mitigação prática de alucinação em uso pessoal
- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]] — as tool calls de manipulação de arquivo são, na prática, comandos de shell (`cat`/`echo`/`grep`/`sed`) executados pela harness na máquina
- [[wiki/sources/harness-explicado-function-calling-hag-evals]] — demo ao vivo do ciclo completo com uma harness Python mínima: `ls`/`sed` pedidos via `function_call`, executados localmente, resultado reinjetado no contexto até a resposta final (`output_text`); histórico do workaround via tags XML antes do function calling nativo existir em todo provider
