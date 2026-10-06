---
type: source
title: "Harness Engineering — Dicionário do Programador (guias, sensores e o de-para do harness)"
aliases: ["Dicionário do Programador: Harness Engineering"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 0
tags: [harness, harness-engineering, guias, sensores, feed-forward, feedback, agents-md, claude-md, skills, sandbox, mcp, loop-engineering, graph-engineering, deepseek]
skill: tech-mentor-ai
status: stable
source_file: raw/harness-engineering-dicionario-do-programador-guias-sensores.md
source_url: ""
author: "não identificado na transcrição (série \"Dicionário do Programador\")"
date_published: "não determinado na transcrição"
date_ingested: 2026-10-06
---

## TL;DR

Vídeo curto em português que define **harness engineering** como tudo que compõe um agente exceto o modelo: o LLM dá raciocínio, o harness dá ambiente, ferramentas, limites, contexto e execução. Atribui a formalização do termo a Mitchell Hashimoto, Birgitta Böckeler e Vivek Trivedy. Traz três ideias úteis: (1) o **princípio de Hashimoto** — a cada erro do agente, construir uma **trava determinística** no harness em vez de só remendar o prompt; (2) a divisão de Böckeler em **guias** (feed-forward: `AGENTS.md`, `CLAUDE.md`, skills) e **sensores** (feedback: testes, linters, type checkers, logs, observabilidade); (3) o **de-para de Trivedy** entre comportamento desejado e componente de harness. Fecha com as três camadas (modelo / harness da ferramenta / user harness), o DeepSeek Harness ("everything is a plugin") e um exemplo fora de software (crédito financeiro).

## Key Claims

1. **Harness = tudo menos o modelo** — o modelo contém a inteligência; o harness a torna útil. Um modelo cru só vira agente quando o harness dá controle, injeção de contexto, consistência, ação, observação e verificação. → [[wiki/concepts/harness]]
2. **Princípio de Hashimoto** — erro do agente ⇒ planejar uma trava determinística no harness, não apenas corrigir o prompt. → [[wiki/concepts/trava-deterministica-no-harness]]
3. **Dois propósitos do harness** — aumentar a chance de acertar de primeira e prover ciclo de feedback que corrija o máximo de problemas.
4. **Guias (feed-forward) vs. sensores (feedback)** (Böckeler) — guias agem antes da ação (regras no prompt do sistema); sensores agem depois (validam, acionam hooks de correção). → [[wiki/concepts/sensores-vs-guias]]
5. **`AGENTS.md` é o "README para agentes"**; um na raiz com regras globais + outros em subpastas/módulos; `CLAUDE.md` costuma importar o `AGENTS.md` e só acrescentar o específico do Claude Code. → [[wiki/concepts/agents-md-vs-claude-md]]
6. **Skills evitam encher o contexto de entrada** — biblioteca de habilidades carregadas sob demanda; exemplo: skill que valida migração de banco (detecta locks/drop de coluna, roda validação de sintaxe, emite relatório aprovando/bloqueando). → [[wiki/concepts/skills-agente]]
7. **De-para de Trivedy** — persistência = file system + Git; executar código = Bash + ambiente de execução; segurança = sandbox + tooling; memória = arquivos + web search + MCPs; contexto longo = compactação + tool-offloading + skills; trabalho longo = loops + planejamento + verificação. → [[wiki/concepts/harness-componentes-por-capacidade]]
8. **Três camadas** — modelo (núcleo), harness da ferramenta (system prompt, terminal, orquestração, contexto; embutido, pouco controle) e user harness (feed-forward + feedback configurados pelo dev). → [[wiki/concepts/harness]]
9. **A diferença entre respostas depende mais do harness que do modelo** (afirmação do autor, sem dado empírico no vídeo).
10. **DeepSeek Harness** — open source, "everything is a plugin" (modelos, tools, skills, sessões, sandbox, storage, interface trocáveis); em *developer preview* na gravação. → [[wiki/entities/deepseek-harness]]
11. **Harness vale fora de software** — em crédito: teto de aprovação automática, explicação auditável por recusa, conformidade com regras do Banco Central. → [[wiki/concepts/harness-em-dominios-regulados-credito]]
12. **Taxonomia em expansão** — meta harness, [[wiki/concepts/loop-engineering]], graph engineering; "muitas técnicas vão surgir e morrer".

## Entidades

- [[wiki/entities/mitchell-hashimoto]] — criador do Terraform; princípio da trava determinística
- [[wiki/entities/birgitta-bockeler]] — [[wiki/entities/thoughtworks]]; guias vs. sensores
- [[wiki/entities/vivek-trivedy]] — [[wiki/entities/langchain]]; de-para modelo→harness
- [[wiki/entities/deepseek-harness]] — harness open source da [[wiki/entities/deepseek]]
- [[wiki/entities/claude-code]], [[wiki/entities/codex-openai]], [[wiki/entities/cursor]], [[wiki/entities/replit]], [[wiki/entities/lovable]] — citados como ferramentas que já trazem harness próprio

## Conceitos

[[wiki/concepts/harness]], [[wiki/concepts/sensores-vs-guias]], [[wiki/concepts/trava-deterministica-no-harness]], [[wiki/concepts/harness-componentes-por-capacidade]], [[wiki/concepts/harness-em-dominios-regulados-credito]], [[wiki/concepts/skills-agente]], [[wiki/concepts/agents-md-vs-claude-md]], [[wiki/concepts/rules-agente]], [[wiki/concepts/harness-de-qualidade]], [[wiki/concepts/loop-engineering]], [[wiki/concepts/context-compaction]], [[wiki/concepts/ai-safety-guardrails]], [[wiki/concepts/hooks-agente]], [[wiki/concepts/model-context-protocol]], [[wiki/concepts/determinismo-vs-probabilismo-em-ia]]

## Open Questions

- O vídeo não cita fontes primárias (post de Hashimoto, artigo de Böckeler no site de Martin Fowler, texto de Trivedy no blog da LangChain); atribuições e o de-para são relato do áudio `[external, não verificado]`.
- "(Ralph?) loops" na última linha do de-para é leitura incerta do ASR ("half loops"); ver [[wiki/concepts/ralph-loop]].
- Existência e escopo do **DeepSeek Harness** não verificados; "diferente e mais flexível que Claude Code/Codex" é opinião do autor.
- "A diferença está mais no harness do que no modelo" é afirmação sem medição.

## Quotes

> "O modelo contém a inteligência e o harness torna essa inteligência útil."
> "Toda vez que um agente comete um erro, [...] planejar uma trava determinística no harness para que o agente seja incapaz de cometer aquele erro novamente."
