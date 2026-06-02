---
type: concept
title: "Design.md (Padrão Google)"
aliases: ["design md", "getdesign.md", "design spec markdown"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 1
tags: [design-md, design-system, harness, skills, ui-ux, google]
skill: tech-mentor-ai
status: stub
---

# Design.md (Padrão Google)

Padrão criado pelo Google (2026) para especificar design systems em Markdown. Um arquivo `.md` com tokens de design (cores, fontes, espaçamentos, animações) que a LLM usa para gerar UIs visualmente consistentes.

## Como Funciona

1. Gerar via CLI: `npx get-design <marca>` (ex: Ferrari, Apple, BMW, Airbnb)
2. Arquivo `design.md` é criado no projeto com a spec completa de design
3. Skill de design interpreta o `design.md` ao gerar componentes UI
4. Resultado: UI com identidade visual da marca sem instruções manuais por prompt

## Exemplo

```bash
npx get-design ferrari
# Gera design.md com: vermelho Ferrari, fontes, animações, espaçamentos
```

Combinado com a skill `design.md` do `skills.sh`:
```
Refatorie o front-end de acordo com as especificações do nosso design.md
```

## Disponível em skills.sh

Skill `design-md` no catálogo público analisa e gera spec de design semântica.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-03-skills]]
