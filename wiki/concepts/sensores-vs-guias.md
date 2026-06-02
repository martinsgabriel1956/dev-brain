---
type: concept
title: "Sensores vs Guias (User Harness)"
aliases: ["sensores harness", "guias harness", "sensors guides ai", "feedback loop ia"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 2
tags: [harness, sensores, guias, feedback-loop, context-engineering, autocorrecao]
skill: tech-mentor-ai
status: stable
---

# Sensores vs Guias (User Harness)

Dicotomia central do **user harness**: o que você fornece além do que vem do provider (Claude Code, Cursor, Codex). Guias direcionam o comportamento da LLM antes da execução; sensores fornecem feedback para autocorreção durante a execução.

## Guias

Antecipam o comportamento e aumentam a chance de acerto na primeira tentativa.

**O que são:**
- Code standards e anti-patterns
- Estrutura de pastas e blueprints de arquitetura
- Convenções de commit e PR
- Conhecimento de negócio estático
- Comandos e portas disponíveis no projeto

**Como são implementados:**
- Rules (`agents.md`, `CLAUDE.md`, `.cursorrules`)
- Skills (carregadas sob demanda)
- MCPs de documentação/configuração

> "Guias = Rules + Skills" — tudo que orienta antes de executar.

## Sensores

Fornecem ciclos de feedback durante a execução. A LLM observa o resultado do sensor e decide se autocorrige.

**Exemplos de sensores:**
- Testes automatizados (unitários, integração, E2E) — se falha, LLM corrige
- Linter e compilador — output de erro é feedback imediato
- Browser / Playwright — screenshot, DOM, console errors
- Banco de dados — queries, constraints, erros de persistência
- Bash execute — output do terminal, exit code
- LLM de revisão de código — sensor não-determinístico para qualidade

**Propriedade:** Quanto mais sensores úteis e relevantes, mais autocorreção ocorre e menos supervisão humana é necessária.

## A Relação entre Sensores e Qualidade

```
Nenhum sensor → LLM executa sem feedback → resultado pode estar errado
1 sensor (bash) → LLM executa, observa output, corrige se falhou
N sensores → LLM testa múltiplas dimensões de qualidade → resultado mais confiável
```

## O Problema da Escassez de Sensores

Em projetos com 1 milhão de linhas de código, não é possível fazer `node hello-world.js`. Precisa de testes automatizados como sensor. Sem sensores adequados:
- LLM não sabe se o que fez funcionou
- Cada iteração aumenta a janela de contexto (custo)
- Usuário precisa supervisionar manualmente (L1/L2)

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-01-context-harness-engineering]]
- [[wiki/sources/formacao-ia-devs-aula-02-mcp-parte2]]
