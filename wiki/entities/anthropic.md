---
type: entity
title: "Anthropic"
aliases: ["Anthropic", "Antrópica"]
date_created: 2026-06-02
date_updated: 2026-07-19
source_count: 9
tags: [anthropic, claude, llm, harness, mcp, ia-para-devs, custo-de-ia]
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

## Custo do Ultra Review / Ultra Plan em Teste Pessoal

[[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] relata um teste pessoal do autor com o Ultra Review e o Ultra Plan da Anthropic: gastou cerca de 150 (unidade monetária não especificada na fonte) só testando, com o Ultra Review consumindo ~30 por execução — e um bug fazia a ferramenta crashar depois de já ter consumido o saldo disponível, sem entregar resultado, obrigando a adicionar mais crédito para completar e ver o output. Tratado como relato de experiência individual, não como benchmark de custo oficial da Anthropic.

## Key Sources

- [[wiki/sources/html-vs-markdown-para-agentes-de-ia]] — citada de passagem como tendo "divulgado algo parecido" sobre preferir HTML a Markdown na saída de agentes; a fonte não linka o material original, então tratar como não verificado
- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]
- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
- [[wiki/sources/custo-tokens-portugues-vs-ingles]]
- [[wiki/sources/tokens-llm-fundamentos-typescript]]
- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
- [[wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam]] — citada de passagem: erros `503` frequentes da API do Claude ("modelo ocupado, tente novamente") como exemplo do "novo normal" de sistemas caindo, exigindo estratégias de retry no lado do cliente
- [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] — custo elevado do Ultra Review/Ultra Plan em teste pessoal, incluindo bug de crash que consumiu saldo sem entregar resultado
