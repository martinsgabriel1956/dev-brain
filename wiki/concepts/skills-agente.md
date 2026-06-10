---
type: concept
title: "Skills (Padrão de Harness)"
aliases: ["skills harness", "agents skills", "skill pattern ia", "skills.sh"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 2
tags: [skills, harness, context-engineering, lazy-loading, system-prompt]
skill: tech-mentor-ai
status: stable
---

# Skills (Padrão de Harness)

Padrão de harness criado pela Anthropic em novembro de 2025. Uma skill é uma **pasta auto-contida** com instruções para uma tarefa ou domínio específico. Diferente das rules, só o cabeçalho (front-matter) entra no system prompt; o corpo é carregado por **tool call sob demanda**.

## Estrutura

```
.claude/skills/          (Anthropic)
.agents/skills/          (todos os outros harnesses)
  minha-skill/
    SKILL.md             ← obrigatório
    references/          ← opcional
    templates/           ← opcional
    scripts/             ← opcional (risco de código malicioso)
```

### Formato da SKILL.md

```yaml
---
name: react
description: "Boas práticas React + TypeScript — componentes, hooks, performance, arquitetura"
version: 1.0.0
---

[Corpo da skill — instruções detalhadas, exemplos, referências]
[Carregado por tool call, não no system prompt]
```

## Ciclo de Carregamento

```
Sistema inicia
→ Só name + description entram no system prompt (todos os harnesses)
→ LLM recebe lista: "você tem skills disponíveis: react, vitest, express…"

Task chega
→ LLM decide (ou você instrui): "carregue skill react"
→ Tool call: load_skill("react")
→ Corpo da SKILL.md entra no contexto
→ LLM executa com instruções completas
```

## Vantagens sobre Rules

1. **Lazy loading:** corpo não ocupa contexto quando não é necessário
2. **Auto-contida:** pode ser zipada e compartilhada — self-contained
3. **Padronização:** todos os harnesses implementaram igual (exceto caminho: Anthropic usa `.claude/skills/`, outros usam `.agents/skills/`)
4. **Reutilizável:** mesma skill usada em múltiplos projetos

## Dois Usos

**Como guardrail contextual (substitui rule):**
Instrução de como escrever React — só carregada quando a task é front-end.

**Como processo:**
Criar slide, gerar proposta comercial, executar QA — um workflow completo empacotado.

## Como Garantir o Carregamento

Modelos ainda não carregam skills de forma confiável sem sinalização. Estratégias:

1. **Referenciar no prompt:** `Use /react /vitest` (Claude Code) ou `$react $vitest` (Codex)
2. **Mapear no agents.md:** "Quando criar componente React, carregue skill react"
3. **Ambos:** garantia máxima

## Repositório Público: skills.sh

- ~100k skills disponíveis
- Criado pela Vercel
- CLI: `npx skills add <owner>/<repo>`
- Instala para múltiplos harnesses simultaneamente
- Repositório auditado do Pedro Nauke: `github.com/pedronok/skills`

## Aviso de Segurança

Skills podem conter scripts executáveis. **Skills de terceiros não verificadas podem conter código malicioso** (roubar `.env`, etc.). Verificar antes de instalar.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-03-skills]]
- [[wiki/sources/formacao-ia-devs-aula-02-rules]]
