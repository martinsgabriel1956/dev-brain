---
type: entity
title: "Verdent AI"
aliases: ["verdent", "verdent ai ide"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 1
tags: [ide, coding-agents, plan-mode, skills, ferramenta-ia]
skill: tech-mentor-ai
status: stub
---

# Verdent AI

IDE com IA nativa/integrada (uma ferramenta de desenvolvimento com agentes embutidos), em beta na época da fonte. Apresentada em [[wiki/sources/extrair-melhor-codigo-de-agentes-ia-planejamento-plan-mode-skills]] como o ambiente usado para demonstrar boas práticas de uso de agentes.

## Recursos citados

- **Múltiplos agentes em paralelo.**
- **Modo plan** ([[wiki/concepts/plan-mode]]): a IA mapeia dependências, gera uma especificação técnica com diagrama Mermaid, pergunta em pontos ambíguos e só codifica após o plano ser revisado e comentado (botão "build").
- **Skills** ([[wiki/concepts/skills-agente]]): criação (inclui um *Skill Creator* — uma skill que cria skills, ver [[wiki/concepts/meta-prompting]]), instalação e importação de skills da comunidade. As skills são empacotadas como arquivo `.skill` (contendo `SKILL.md` + `references/`).
- Interface de acompanhamento de tarefas (todos) durante a execução.

## Nota

Fonte única e de caráter demonstrativo/patrocinado — os recursos descritos (plan mode, skills) são padrões gerais de harnesses de coding agents, não exclusivos da Verdent. Ver [[wiki/concepts/plan-mode]] e [[wiki/concepts/skills-agente]] para o conceito independente da ferramenta.

## Key Sources

- [[wiki/sources/extrair-melhor-codigo-de-agentes-ia-planejamento-plan-mode-skills]]
