---
type: concept
title: "SDLC Nativo de IA (5 Regras)"
aliases: ["ai native sdlc", "sdlc nativo de ia", "5 regras claude code startups", "ai natives working at the frontier"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_count: 1
tags: [claude-code, anthropic, sdlc, agentes-ia, startup, playbook]
skill: tech-mentor-ai
status: draft
---

# SDLC Nativo de IA (5 Regras)

## TL;DR

Framework de cinco princípios operacionais, atribuído a um playbook da [[wiki/entities/anthropic|Anthropic]] baseado em entrevistas com startups de rápido crescimento usando [[wiki/entities/claude-code|Claude Code]] (ver [[wiki/sources/guia-claude-code-para-startups-anthropic-ai-native-sdlc]]). Descreve como um ciclo de desenvolvimento de software ("SDLC") se reorganiza quando construído nativamente em torno de agentes de codificação, em vez de tê-los apenas como ferramenta auxiliar de um SDLC tradicional.

## As 5 Regras

1. **[[wiki/concepts/everyone-ships|Everyone ships]]** — a barreira para colocar código em produção cai; quem entende o problema de negócio consegue abrir o PR, não só quem entende profundamente o código.
2. **Automate the tedium** — automatizar etapas mecânicas e repetitivas do processo de desenvolvimento (ex. onboarding, triagem de bugs).
3. **Trust but verify** — nunca automatizar algo sem antes definir como verificar a qualidade do resultado (evals); a IA roda em loop contra um critério de verificação explícito até passar.
4. **Build for rebuilding** — o custo de escrever e descartar código caiu; reconstruir iterativamente (não só incrementar) virou padrão comum, e times costumam só entender o problema de fato depois de algumas reconstruções.
5. **Prototype, dog food, productionize** — testar em ambiente local com o próprio agente antes de produtizar, conectando fontes de dados confiáveis via [[wiki/concepts/mcp-server|MCP]]/CLI e criando um marketplace interno de plugins corporativos (ex. Jira, Figma, Drive, com SSO).

## Riscos Não Endereçados Explicitamente pelo Framework

A fonte que documenta este framework aponta três lacunas práticas que o playbook da Anthropic, segundo o autor, não trata com o devido peso:

- **Automação prematura de processo não validado** (regra 2): automatizar cedo demais impede a evolução orgânica do processo — a organização "deixa rodar" sem revisar, perdendo visibilidade sobre quantas automações estão ativas e por quê. Relacionado a [[wiki/concepts/finops-para-ia]] (falta de visibilidade de consumo/custo).
- **[[wiki/concepts/risco-de-outage-fornecedor-ia|Dependência de fornecedor único]]**: construir um SDLC inteiro em torno de um único provedor de IA expõe a organização a indisponibilidade do fornecedor.
- **Fragmentação de configuração entre agentes** ([[wiki/concepts/agents-md-vs-claude-md]]): o próprio relatório menciona compartilhamento de "skills"/configurações como uma dor recorrente entre as empresas entrevistadas, mas a Anthropic mantém uma posição (`CLAUDE.md` apenas) que, segundo o autor, agrava esse problema em vez de resolvê-lo.

## Relação com Outros Conceitos

- [[wiki/concepts/loop-engineering]] — a regra 3 (trust but verify) é uma instância do mesmo padrão de "gate verificável + loop até passar" já documentado em profundidade nesse conceito
- [[wiki/concepts/quality-gate]] — mecanismo técnico por trás de "trust but verify"
- [[wiki/concepts/tech-debt-como-ferramenta]] — "build for rebuilding" como forma de descarte deliberado de código, decisão financeira consciente
- [[wiki/concepts/mcp-arquitetura]] — infraestrutura técnica por trás da regra 5

## Key Sources

- [[wiki/sources/guia-claude-code-para-startups-anthropic-ai-native-sdlc]]
