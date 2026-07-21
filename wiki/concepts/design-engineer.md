---
type: concept
title: "Design Engineer"
aliases: ["design engineering", "dev com visão de design", "frontend designer"]
date_created: 2026-04-22
date_updated: 2026-07-21
source_count: 2
tags: [design, frontend, cargo, design-engineer, workflow]
skill: tech-mentor-frontend
status: stable
---

# Design Engineer

Cargo/perfil emergente — especialmente no Vale do Silício — de profissionais que têm **conhecimento de design aplicado diretamente no código**. A fronteira entre designer e frontend dev é fluida ou inexistente.

## Características

- Experimenta layouts e interações **diretamente no código**, não no Figma primeiro
- Usa o Figma mais como ferramenta de teste e validação do que como fonte de verdade
- Cuida de detalhes que devs puros ignoram: micro-animações, timing, feedback visual, percepção de velocidade
- Tem repertório visual forte — consome referências ativamente ([[dribbble]], [[linear-app]], X/Twitter)

## Por que o cargo surgiu

Em times pequenos ou produtos que exigem alta qualidade de UI/UX, manter dois papéis separados (designer + dev) cria atrito:
- Figma desatualizado (ver [[design-first]])
- Handoff entre designer e dev perde nuances
- Iterações lentas

O Design Engineer colapsa esse atrito sendo fluente nos dois lados.

## Ferramentas típicas

- **Código**: React, Framer Motion, CSS animations, Tailwind
- **Design**: Figma (como teste), Hype (animações), Rive
- **Referências**: Dribbble, X/Twitter (perfis de design engineers), Linear como benchmark

## Referências de Design Engineers notáveis (X/Twitter)

| Pessoa | Contexto |
|---|---|
| RA | Staff Design Engineer na Vercel — site "craft" com experimentações |
| Stephen | Founder do Paper (Figma para Design Engineers) |
| Pedro (Radix) | Co-founder Radix UI, trabalha na Raycast |
| Paul McGregor | Designer no Linear |
| Gavin | Designer na OpenAI |
| Ned | Founder do Lovable |

## Fundamentos que a IA não aplica sozinha

Ferramentas de geração de UI por IA (ex.: [[wiki/entities/ux-pilot]], Cursor) produzem resultados sensivelmente melhores quando o prompt declara explicitamente princípios clássicos de design que um Design Engineer aplicaria por repertório: [[wiki/concepts/hierarquia-visual]], [[wiki/concepts/lei-da-proximidade-gestalt]] e [[wiki/concepts/affordance]]. Sem isso, a IA tende a gerar CTAs concorrentes, elementos "soltos" sem agrupamento visual, e botões sem sinalização de clicabilidade (`cursor: pointer`, hover) — os mesmos erros que um Design Engineer aprende a evitar por conhecimento de design, não de código.

## Ver também

- [[design-first]] — workflow que Design Engineers tendem a adaptar/hibridizar
- [[code-first]] — ponto de partida natural de muitos Design Engineers
- [[fake-delay]] — exemplo de detalhe de UX que Design Engineers se importam
- [[wiki/concepts/hierarquia-visual]] — princípio de design aplicável tanto no código quanto em prompts de geração de UI
- [[wiki/concepts/affordance]] — sinalização de interatividade, um dos detalhes que Design Engineers cuidam por padrão

## Key Sources

- [[wiki/sources/design-first-vs-code-first-referencias]]
- [[wiki/sources/5-boas-praticas-uiux-ux-pilot]]
