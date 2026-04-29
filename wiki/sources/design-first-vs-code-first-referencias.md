---
type: source
title: "Design First vs Code First — Abordagens e Referências de Design"
aliases: ["design first code first", "design engineer referências"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/nemomartins/Documentos/new/dev-study/raw/design-first-vs-code-first-referencias.md
source_url: ""
author: "Transcrição de vídeo/aula (speaker não identificado)"
date_published: 2026-04-22
date_ingested: 2026-04-22
source_count: 0
tags: [design, frontend, design-engineer, design-first, code-first, ux, referências]
skill: tech-mentor-frontend
status: stable
---

# Design First vs Code First — Abordagens e Referências de Design

## TL;DR

Transcrição de vídeo/aula sobre as duas abordagens de criação de UI (design first vs code first), o papel emergente do Design Engineer, e uma lista de referências de design para devs frontend. Aborda também o conceito de fake delay como técnica de UX.

---

## Claims Principais

| Claim | Evidência | Confiança |
|---|---|---|
| Code first com component libraries sem visão de design gera "Frankenstein" | Componentes isolados sem contexto da aplicação levam a inconsistência visual | Alta |
| Design first sem separação de times leva ao Figma desatualizado | Dev que faz design e código ao mesmo tempo não mantém o Figma sincronizado | Alta |
| Design Engineer é quem experimenta layout diretamente no código | Figma vira ferramenta de teste, não fonte de verdade | Alta |
| Fake delay de 300ms melhora percepção de qualidade da interação | Spinner visível mesmo em respostas rápidas dá sensação de feedback ao usuário | Alta (prática bem documentada em UX) |
| Design não é só visual — é usabilidade, onboarding, animações, velocidade percebida | Linear é referência porque é rápido e acessível, não só bonito | Alta |
| Dribbble como fonte de referências de layout sem copiar diretamente | Busca por "table design" web para pegar referências | Alta |

---

## Conceitos Abordados

- [[design-first]]
- [[code-first]]
- [[design-engineer]]
- [[fake-delay]]

## Entidades Abordadas

- [[linear-app]]
- [[figma]]
- [[dribbble]]
- [[lovable]]
- [[radix-ui]]

---

## Pessoas Mencionadas

- **RA** (Ra) — Staff Design Engineer na Vercel, site "craft" com experimentações de UI via código
- **Stephen** — Founder do Paper (Figma focado em Design Engineers)
- **Pedro** — Co-founder da Radix UI / Stitches, trabalha na Raycast
- **Paul McGregor** — Designer no Linear
- **Gavin** — Designer na OpenAI
- **Ned** — Founder do Lovable

## Ferramentas Mencionadas

- **Figma** — Design first; vira ferramenta de teste no workflow de Design Engineers
- **Hype** — Ferramenta para animações no workflow de Design Engineers
- **Paper** — Figma focado em devs/Design Engineers (em construção)
- **Dribbble** — Referências de layout (filtro por "web")
- **Shadcn/ui**, **Headless UI**, **Vercel AI Elements** — Exemplos de component libraries code-first

---

## Quotes Relevantes

> "Design first é a abordagem seguida em times maiores onde há separação clara de designers e devs. Quando você é a mesma pessoa, o Figma começa a ficar desatualizado."

> "O Design Engineer faz experimentações de layout diretamente no código. O Figma fica mais como ferramenta de testes."

> "Design não é só layouts bonitinhos. Tem muito a ver com usabilidade, onboarding, o primeiro contato, as animações."

> "O Linear é referência em aplicação rápida, acessível, com ótimo design."

---

## Questões Abertas

- Paper (o "Figma para devs") foi lançado/estabilizou? Vale adotar no workflow?
- Qual o threshold certo de fake delay por tipo de ação (form submit vs toggle vs navegação)?
