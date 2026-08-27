---
type: source
title: "Harness: a Anatomia Técnica Por Trás do Claude Code, Cursor e Codex"
aliases: ["Você Não Entende o Que é Harness"]
date_created: 2026-08-27
date_updated: 2026-08-27
source_count: 0
tags: [harness, agente-ia, agent-loop, guardrails, observabilidade, agent-memory, claude-code, cursor, codex-openai, open-claw, opencode, mcp]
skill: tech-mentor-ai
status: stable
source_file: raw/harness-anatomia-tecnica-alem-do-claude-md.md
source_url: ""
author: "não identificado na transcrição (canal de vídeo em português, Fernanda Kipper — citação a fernandakipper.com no encerramento)"
date_published: "não determinado na transcrição"
date_ingested: 2026-08-27
---

## TL;DR

Vídeo em português que define harness de forma técnica: tudo que envolve o modelo tentando extrair eficiência e resultado previsível dele. Distingue **user harness** (rules, skills, CLAUDE.md/AGENTS.md — o que o usuário controla) da camada invisível de harness embutida nas próprias ferramentas (Claude Code, Cursor, Codex etc.), e detalha cinco componentes de um agent run: assemble de contexto (rules, skills, user/episodic/semantic/procedural memory — no fundo um RAG), tools, agent loop (com limites e timeouts), guardrails (filtros de segurança e policy check) e observabilidade (logs, custo por token, retries, evals). Fecha com o grau de controle variável por ferramenta (OpenClaw ≫ Codex/Claude Code ≫ Cursor) e a revelação de que o Claude Code é open source no GitHub após um vazamento na Anthropic.

## Key Claims

1. **Harness é tudo ao redor do modelo** — aparatos, ferramentas, frameworks e técnicas usados para extrair melhor eficiência e resultado do modelo de IA.
2. **User harness é só uma fração do harness total** — rules, skills, AGENTS.md/CLAUDE.md, hooks são a parcela que o usuário consegue manipular; existe uma camada adicional, construída pela própria ferramenta de agentic coding, que o usuário normalmente não enxerga.
3. **As ferramentas de agentic coding são, elas mesmas, harness** — Claude Code é "o harness da Anthropic"; o mesmo vale para Codex (OpenAI), Cursor, Trae, Hermes, OpenCode, OpenClaw. O modelo (GPT, Kimi, GLM, Opus, Fable) é o "miolo" comum; o que muda entre ferramentas é a camada construída ao redor.
4. **Assemble de contexto é um RAG** — rules, skills, user memory (fatos duráveis), episodic memory (linha do tempo de descobertas anteriores), semantic memory (preferências de usuário/projeto) e procedural memory (arquivos markdown/playbooks) são filtrados e agregados antes de chegar ao modelo, usando dados em banco vetorial, markdown e SQL.
5. **Nem toda ferramenta implementa todas as camadas de memória** — algumas oferecem memória episódica nativamente, outras exigem configuração manual, outras não têm nenhuma forma de "self-improving" sobre o usuário.
6. **Agent loop controla limites de execução** — número máximo de tool calls, timeout por tool, fail checks — para evitar que o modelo entre em loop infinito pedindo mais informação antes de finalizar.
7. **Guardrails filtram input, output e comportamento de tools** — proteção contra tools maliciosas que podem retornar conteúdo perigoso, além de policy check de segurança/ética.
8. **Observabilidade é a camada menos universal** — mais comum em agentes customizados (ex.: construídos sobre OpenClaw) do que em ferramentas comerciais fechadas; inclui logs, custo por token, retries e evals ("how we know it works").
9. **Grau de controle do usuário sobre o harness varia por ferramenta**: OpenClaw permite quase controle total (inclusive plugar Mem0/memzero como memória episódica própria); Cursor mantém a maior parte do harness fechado, deixando ao usuário só a parcela de user harness; Codex e Claude Code ficam num meio-termo.
10. **Claude Code é open source no GitHub** — segundo a fonte, após um vazamento na Anthropic, o código do harness que a Anthropic constrói em volta dos próprios modelos ficou publicamente disponível, permitindo a qualquer um clonar/adaptar a própria versão. *Confiança: não verificado nesta ingestão contra fonte primária (ex.: anúncio oficial da Anthropic ou repositório específico) — tratar como claim do autor do vídeo.*

## Entidades

- [[wiki/entities/anthropic]] — autora do Claude Code, citada como tendo "vazado" o próprio harness, que se tornaria open source
- [[wiki/entities/claude-code]] — harness da Anthropic; central ao claim de open source pós-vazamento
- [[wiki/entities/codex-openai]] — citado como meio-termo de controle de harness (mais flexível que Cursor, menos aberto que OpenClaw)
- [[wiki/entities/cursor]] — citado como o extremo de menor controle de harness para o usuário final
- [[wiki/entities/open-claw]] — citado como o extremo de maior controle; exemplo de conexão de memória episódica própria via Mem0/memzero
- [[wiki/entities/opencode]] — citado, junto do Hermes, como harness que aceita qualquer modelo (Anthropic, GLM, etc.)
- [[wiki/entities/hermes-agent]] — citado no mesmo grupo do OpenCode como harness multi-modelo

## Conceitos

- [[wiki/concepts/harness]] — conceito central; fonte reforça a distinção user harness vs. harness embutido na ferramenta, e detalha componentes não totalmente cobertos antes (agent loop com limites, guardrails, observabilidade com retries/evals)
- [[wiki/concepts/ciclo-agente]] — descrição do agent loop como mecanismo que impõe limites (máximo de chamadas, timeout) para evitar loop infinito
- [[wiki/concepts/ai-safety-guardrails]] — guardrails como filtro de input/output/tool-result e policy check, no contexto específico do agent run
- [[wiki/concepts/llm-evals-testing]] — evals como parte da camada de observabilidade do harness, mecanismo de "how we know it works"
- [[wiki/concepts/agent-memory-tres-camadas]] — nomenclatura paralela (user/episodic/semantic/procedural memory) para o mesmo padrão de memória em camadas já documentado na wiki
- [[wiki/concepts/model-context-protocol]] — mencionado en passant como parte do aparato de harness (não detalhado nesta fonte)
- [[wiki/concepts/rules-agente]] — rules como parte do assemble de contexto e do user harness
- [[wiki/concepts/skills-agente]] — skills como parte do assemble de contexto e do user harness

## Open Questions

- O claim de que o Claude Code se tornou open source após um vazamento na Anthropic não foi verificado contra fonte primária nesta ingestão — nem data, nem escopo exato (código completo vs. parcial) foram especificados na transcrição.
- A transcrição não identifica explicitamente a autora/o autor do vídeo, mas o encerramento cita um portal de cursos gratuitos em "fernandakeiper.com" (grafia incerta por ASR) com artigos e resumos em vídeo sobre IA — possível autoria de Fernanda Kipper, não confirmada.
- Não fica claro se "OpenClaw" no encerramento é o mesmo projeto documentado em [[wiki/entities/open-claw]] (adquirido, segundo outra fonte já na wiki, pelo time por trás do OpenAI) ou uma ferramenta homônima diferente — tratar como o mesmo projeto por default, dado o contexto de agente customizável com learning loop.

## Quotes

> "Harness é tudo que está por volta do modelo, tentando controlar o resultado, tentando ter resultados mais previsíveis."

> "O modelo é só o miolinho ali da cebola, mas por volta disso a gente tem um monte de coisa."

> "Não é toda ferramenta de agentic coding que vai ter memória episódica — algumas oferecem, outras não; às vezes você vai ter que configurar manualmente."

> "O Cloud Code, na verdade, nada mais é do que o harness da Antropic."

## Raw Source

[[raw/harness-anatomia-tecnica-alem-do-claude-md]]
