---
type: concept
title: "Component Library"
aliases: ["biblioteca de componentes", "UI library", "shadcn", "radix ui", "headless ui"]
date_created: 2026-06-11
date_updated: 2026-06-11
source_count: 1
tags: [frontend, design, componentes, ux, code-first]
skill: tech-mentor-frontend
status: stable
---

# Component Library

Conjunto de componentes de UI pré-construídos e pré-estilizados que aceleram o desenvolvimento frontend. São o principal facilitador da abordagem [[concepts/code-first]].

---

## Exemplos Modernos

| Biblioteca | Tipo | Nota |
|---|---|---|
| Shadcn/UI | Componentes com estilo + headless | Cópia para o projeto, não dependência |
| Radix UI | Headless (sem estilo) | Fundação acessível — ver [[entities/radix-ui]] |
| Headless UI | Headless | Da Tailwind Labs |
| Vercel AI Elements | Componentes de AI UI | Para interfaces de LLM e chat |

---

## O Problema do "Frankenstein"

Componentes de library são construídos de forma isolada, sem o contexto da aplicação que você está criando. Sem uma visão coesa de design:
- Componentes de diferentes origens coexistem sem coerência visual
- O resultado parece uma colagem de partes que não conversam entre si

**Mitigação:** usar uma única library como base + ter referências visuais antes de começar (ex: [[concepts/design-first]] ou Dribbble).

---

## Headless vs Estilizadas

| | Headless (Radix, Headless UI) | Estilizadas (Shadcn, MUI) |
|---|---|---|
| Controle visual | Total | Limitado ao tema |
| Velocidade | Menor (precisa estilizar) | Maior |
| Risco de Frankenstein | Menor | Maior |
| Acessibilidade | Alta (built-in) | Variável |

---

## Relação com Outros Conceitos

- [[concepts/code-first]] — component libraries são a ferramenta central da abordagem code-first
- [[concepts/design-engineer]] — Design Engineers usam libraries mas mantêm visão coesa via referências
- [[concepts/design-first]] — alternativa que define a coerência visual antes de escolher componentes

## Key Sources

- [[sources/design-first-vs-code-first-referencias]]
