---
type: entity
title: "Anthropic"
aliases: ["Anthropic", "Antrópica"]
date_created: 2026-06-02
date_updated: 2026-07-03
source_count: 7
tags: [anthropic, claude, llm, harness, mcp, ia-para-devs]
skill: tech-mentor-ai
status: stable
---

# Anthropic

Empresa de IA fundada em 2021, criadora da família de modelos Claude e do harness Claude Code. Responsável por diversas specs que viraram padrão de mercado: rules, skills, MCP (Model Context Protocol), subagents.

## Modelos Principais (2026)

| Modelo | Uso recomendado |
|---|---|
| Opus 4.7 | Frontend, design, review de código; o mais capaz da família |
| Sonnet 4.6 | Uso geral — menos recomendado para tarefas exigentes por Nauke |
| Haiku | Tarefas simples, custo baixo |

## Harness: Claude Code

Ver [[wiki/entities/claude-code]]. Principal harness de codificação da Anthropic; considerado o mais inovador do mercado em 2026 com features como: dream consolidation, scheduler, tool search lazy load, memória, worktrees.

## Specs que Viraram Padrão

- **Rules** (CLAUDE.md / project rules)
- **Skills** (conjuntos de instruções reutilizáveis)
- **MCP** (Model Context Protocol) — protocolo aberto para tools/resources
- **Subagents** — ver [[wiki/concepts/subagentes]]

## Relação com Google

Google fez investimento bilionário na Anthropic (cifra não confirmada na fonte; sugestão de verificar). Irônico dado que a Google também tem seu próprio harness (AntiGravity) e modelos (Gemini).

## Preços Históricos

Opus caiu de $15.75/M (input) para ~$5/M — movimento que tornou o uso do Opus mais acessível e aumentou sua adoção.

## Tokenizador e Token Tax

O tokenizador do Claude usa [[byte-pair-encoding]] com foco em inglês, resultando no pior multiplicador de custo para idiomas não-ingleses entre os principais provedores (OpenAI, Google). Português paga ~1.62× mais tokens que inglês — ver [[token-tax-multilingual]]. Não é intenção maliciosa; é consequência do corpus de treinamento ser predominantemente em inglês.

Demonstração via [[entities/vercel-ai-sdk]] com Claude 3.5 Haiku: o prompt `"Hello World"` (2 palavras) já consome 11 tokens de entrada — contra apenas 4 no Gemini 2.0 Flash Lite do Google para o mesmo prompt. Contagens de tokens de entrada/saída não são comparáveis entre provedores porque cada um usa um vocabulário de tokenizer próprio — ver [[tokenizacao]].

## Key Sources

- [[wiki/sources/html-vs-markdown-para-agentes-de-ia]] — citada de passagem como tendo "divulgado algo parecido" sobre preferir HTML a Markdown na saída de agentes; a fonte não linka o material original, então tratar como não verificado
- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]
- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
- [[wiki/sources/custo-tokens-portugues-vs-ingles]]
- [[wiki/sources/tokens-llm-fundamentos-typescript]]
- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
