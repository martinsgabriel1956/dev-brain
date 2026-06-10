---
type: entity
title: "Anthropic"
aliases: ["Anthropic", "Antrópica"]
date_created: 2026-06-02
date_updated: 2026-06-09
source_count: 5
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
- **Subagents**

## Relação com Google

Google fez investimento bilionário na Anthropic (cifra não confirmada na fonte; sugestão de verificar). Irônico dado que a Google também tem seu próprio harness (AntiGravity) e modelos (Gemini).

## Preços Históricos

Opus caiu de $15.75/M (input) para ~$5/M — movimento que tornou o uso do Opus mais acessível e aumentou sua adoção.

## Tokenizador e Token Tax

O tokenizador do Claude usa [[byte-pair-encoding]] com foco em inglês, resultando no pior multiplicador de custo para idiomas não-ingleses entre os principais provedores (OpenAI, Google). Português paga ~1.62× mais tokens que inglês — ver [[token-tax-multilingual]]. Não é intenção maliciosa; é consequência do corpus de treinamento ser predominantemente em inglês.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]
- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
- [[wiki/sources/custo-tokens-portugues-vs-ingles]]
