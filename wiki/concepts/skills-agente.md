---
type: concept
title: "Skills (Padrão de Harness)"
aliases: ["skills harness", "agents skills", "skill pattern ia", "skills.sh"]
date_created: 2026-06-02
date_updated: 2026-07-16
source_count: 4
tags: [skills, harness, context-engineering, lazy-loading, system-prompt, grill-me, rfc]
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

## Skill vs. Subagente

Formato de arquivo quase idêntico (front-matter + corpo Markdown), mas propósito diferente. Uma skill não aceita `model` nem `tools` customizados — é só um prompt reutilizável carregado sob demanda. Um [[wiki/concepts/subagentes|subagente]] roda em paralelo, com processo e janela de contexto próprios, e pode fixar modelo e restringir tools. Ver comparação completa em [[wiki/concepts/subagentes]].

**Risco de sobreposição:** acumular muitas skills (inclusive baixadas de repositórios públicos como "awesome claude skills") junto com muitos subagentes customizados tende a confundir o roteamento automático do próprio modelo — ele pode acionar uma skill genérica quando o usuário esperava um subagente específico, porque as descrições se sobrepõem. Curadoria (poucas skills/agentes bem descritos) supera acúmulo.

## Caso: Workforce Multiagente com Skills Curtas (<70 linhas)

[[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] relata um padrão (atribuído a "Conrado", discutido no Stubborn Club) de separar um workforce de agentes por papel — dev, QA, PO — cada um com uma skill curta (menos de 70 linhas) baseada em especificações técnicas, em vez de um prompt genérico único. O efeito prático: o agente coder passa a fazer uma fatia menor do trabalho total (de ~15% para ~10%), porque skills de outros papéis (ex.: QA) absorvem quality gates que antes ficavam implícitos no prompt do coder.

## Caso: Grill Me (Matt Pocock) — a skill que audita o entendimento do dev, não o código da IA

A mesma fonte descreve a skill **Grill Me**, de [[wiki/entities/matt-pocock]]: um arquivo `.md` com instrução para a IA "entrevistar incansavelmente" o usuário sobre um plano ou design até alcançar entendimento compartilhado, resolvendo cada ramo da árvore de decisão. O autor do vídeo adaptou o prompt para focar em decisões de implementação relevantes ao domínio (cada `if`/cláusula de regra de negócio relevante vira uma pergunta), invertendo o fluxo usual de revisão: em vez do dev ler linha a linha o código gerado, é a IA que questiona o dev até garantir que ele entendeu o que foi construído. Ver também [[wiki/concepts/vibe-coding]] e [[wiki/concepts/rfc-request-for-comments]] para o contexto mais amplo de perda de janela de revisão incremental que motiva essa skill.

## Aviso de Segurança

Skills podem conter scripts executáveis. **Skills de terceiros não verificadas podem conter código malicioso** (roubar `.env`, etc.). Verificar antes de instalar.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-03-skills]]
- [[wiki/sources/formacao-ia-devs-aula-02-rules]]
- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
- [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] — skill Grill Me (Matt Pocock) e workforce multiagente com skills curtas (<70 linhas) por papel
