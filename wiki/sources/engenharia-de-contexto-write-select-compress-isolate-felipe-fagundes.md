---
type: source
title: "Engenharia de contexto na prática: Write, Select, Compress, Isolate — Felipe Fagundes"
aliases: ["write select compress isolate", "reduzir tokens de agente em 71%", "engenharia de contexto agente SRE"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_count: 1
tags: [tech-mentor-ai, context-engineering, agentes, memoria, subagentes, tokens, langchain]
skill: tech-mentor-ai
status: draft
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/engenharia-de-contexto-write-select-compress-isolate-felipe-fagundes.md
source_url:
author: "[[wiki/entities/felipe-fagundes]]"
date_published:
date_ingested: 2026-10-07
---

## TL;DR

[[wiki/entities/felipe-fagundes]] argumenta que janelas de milhões de tokens não resolvem o problema de contexto: o que importa é **o que entra na janela**. Com um agente SRE fictício que precisava de **8.339 tokens** para um resumo final, ele aplica as quatro estratégias — **Write, Select, Compress, Isolate** ([[wiki/concepts/write-select-compress-isolate]]) — e chega a **2.426 tokens** (~71% menos), com ferramentas filtradas por turno e subagentes devolvendo uma linha. Começa pela **análise** ([[wiki/concepts/inspecao-de-contexto-antes-de-otimizar]]) e fecha com a tese de que o ganho real é **menos ruído** ([[wiki/concepts/superficie-probabilistica-do-agente]]), não só menos token.

Tudo abaixo é a demo do autor com dados fictícios `[external, não verificado]`; n=1 agente, sem benchmark de qualidade das respostas.

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| O problema de contexto é o que se coloca na janela, não o tamanho dela | Argumento + demo | Média — coerente com [[wiki/concepts/degradacao-de-contexto]] e [[wiki/concepts/context-engineering-harness]] |
| Engenharia de contexto começa por medir (mensagens, tokens estimados, tools por turno) | Função inspetora da demo | Média-alta (ver [[wiki/concepts/context-compaction]] sobre `/context`) |
| Baseline: 8.339 tokens no último turno; reformulado: 2.426 (~−71%) | Logs da demo fictícia | Média — número real, mas de um cenário montado pelo autor |
| Ferramentas irrelevantes no contexto aumentam decisões e a "superfície probabilística" | Opinião + demo | Média-baixa — termo do autor, sem métrica |
| Write: salvar em memória (namespace + id + conteúdo) em vez de apagar; tipos semântica/episódica/procedural | Código da demo | Média — ver [[wiki/concepts/escrever-memoria-fora-da-janela]], [[wiki/concepts/tipos-de-memoria-de-agente]] |
| Select: filtrar memória por janela de tempo, importância (0–1) e meia-vida (72 h), ou por RAG/palavras-chave; memória não é "fonte completa da verdade" | Código da demo | Média — ver [[wiki/concepts/selecao-de-memoria-e-tools-por-turno]] |
| Select de **tools** por turno via palavras-chave da última mensagem do usuário | Código da demo (domínios fictícios) | Média — heurística simples; o autor diz que é ilustrativa |
| Compress em duas camadas: sumarizar ao passar de 3.500 tokens; clip + offload acima de 1.200 (mantém linhas error/warn, salva o original) | Código da demo | Média — ver [[wiki/concepts/clip-e-offload-de-tool-output]] |
| Isolate: subagente processa ~2,5k tokens e devolve ~180–200; contexto principal sobe só de 1.815 para 1.999 | Logs da demo | Média — coerente com [[wiki/concepts/subagentes]] |
| Menos tokens permitem modelo menor e custo menor | Afirmação do autor | Baixa-média — não medido na demo |
| Subagentes têm custo adicional, aceito para preservar o contexto principal | Autor reconhece | Alta (admitido explicitamente) |

## Conceitos

- [[wiki/concepts/write-select-compress-isolate]] — hub das quatro estratégias
- [[wiki/concepts/inspecao-de-contexto-antes-de-otimizar]]
- [[wiki/concepts/superficie-probabilistica-do-agente]]
- [[wiki/concepts/escrever-memoria-fora-da-janela]]
- [[wiki/concepts/selecao-de-memoria-e-tools-por-turno]]
- [[wiki/concepts/clip-e-offload-de-tool-output]]
- [[wiki/concepts/tipos-de-memoria-de-agente]]
- Tocados: [[wiki/concepts/context-engineering-harness]], [[wiki/concepts/context-compaction]], [[wiki/concepts/subagentes]], [[wiki/concepts/agent-memory-tres-camadas]], [[wiki/concepts/janela-de-contexto]], [[wiki/concepts/degradacao-de-contexto]], [[wiki/concepts/memoria-de-longo-prazo-ia]], [[wiki/concepts/tool-use-agents]], [[wiki/concepts/memory-rot]], [[wiki/concepts/separacao-de-contextos]], [[wiki/concepts/capital-de-tokens]], [[wiki/concepts/harness]]

## Entidades

[[wiki/entities/felipe-fagundes]], [[wiki/entities/langchain]], [[wiki/entities/claude-code]], [[wiki/entities/codex-openai]].

## Open Questions

- A qualidade das respostas melhorou, ou só caiu o custo? O vídeo mostra tokens, não avaliação (ver [[wiki/concepts/evals-llm]]).
- O filtro de tools por palavra-chave falha quando a pergunta não contém o termo do domínio (não discutido). `[inferência]`
- Quem decide a **importância** (0–1) na escrita é o próprio LLM; o vídeo não discute calibração nem viés dessa nota.
- A API `store.put` citada como "LangChain" provavelmente é o store do LangGraph/LangChain `[inferência]`; não verificado contra a documentação.
- Clip por "últimas linhas com error/warn" perde contexto anterior ao erro; o autor diz que deve ser adaptado.

## Quotes

> "O problema sempre foi o que você coloca dentro da janela de contexto e não o tamanho dela."

> "A engenharia de contexto começa na análise e não de fato na melhora."

> "Não é apenas menos token, é que o agente recebe menos ruído."
