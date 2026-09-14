---
type: concept
title: "Everyone Ships"
aliases: ["everyone ships", "todo mundo entrega código", "barreira de shipping caiu"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_count: 1
tags: [claude-code, cultura-organizacional, sdlc, governanca-de-ia, non-technical-shipping]
skill: tech-mentor-ai
status: draft
---

# Everyone Ships

## TL;DR

Padrão organizacional descrito num playbook da [[wiki/entities/anthropic|Anthropic]] sobre startups de rápido crescimento (ver [[wiki/sources/guia-claude-code-para-startups-anthropic-ai-native-sdlc]]): a barreira técnica para colocar código em produção caiu com agentes como o [[wiki/entities/claude-code|Claude Code]] — pessoas não técnicas (advogados, PMs, designers) conseguem modificar código e abrir pull requests porque **entendem o problema de negócio**, não porque entendem profundamente o código.

## O Mecanismo

Antes, a distância entre "quem entende o problema" (PM, designer, usuário final) e "quem escreve o código" (engenheiro) criava um jogo de telefone sem fio: a ideia levava semanas para chegar ao ar e chegava alterada. Com agentes de codificação suficientemente capazes, quem tem o contexto de negócio consegue abrir o PR diretamente.

**Depoimentos citados na fonte:**
- Um advogado interno de uma empresa (Crossby) é descrito como tendo "o melhor insight de produto porque é o usuário" do próprio sistema jurídico.
- Uma empresa (Heid) descreve isso como resolver o "broken telephone problem" — o telefone sem fio entre PM/designer/engenheiro.

## O Deslocamento da Expertise do Engenheiro

Se PMs e pessoas não técnicas escrevem código, a expertise diferencial do engenheiro deixa de ser "escrever" e passa a ser **revisar e julgar** o que é gerado — ver [[wiki/concepts/governanca-de-codigo-gerado-por-ia]]. Isso reforça a crítica já documentada em [[wiki/concepts/ia-como-amplificador]]: a IA amplifica o julgamento de quem a supervisiona, não o substitui.

## Risco: Quem Faz o Shipping Importa

A fonte que introduziu este conceito levanta um contraponto de risco: há diferença entre um fundador/CEO **com background técnico forte** fazendo mudanças diretas em código (exemplo citado: Tobi Lütke, CEO da [[wiki/entities/shopify|Shopify]]) e um fundador/CEO **sem background técnico** entrando na "vibe" de shipar features diretamente em produção sem entender as implicações arquiteturais. O primeiro caso tende a ser mais seguro porque o julgamento técnico ainda está presente na decisão; o segundo caso é descrito como potencialmente perigoso — o mesmo risco central de [[wiki/concepts/vibe-coding]] aplicado a decisores de negócio, não só a devs juniores.

## Ressalva do Próprio Relatório

Mesmo a fonte original reconhece que ainda existe divisão de trabalho na prática — marketing continua fazendo marketing, dev continua sendo dev. O que de fato abriu para "todo mundo" foi o "tweet de zero a um": transformar uma ideia em protótipo funcional, não necessariamente entregar features de produção sem revisão de engenharia. "Everyone ships" é descrito como um slogan melhor para LinkedIn do que uma descrição literal e universal da prática nas empresas entrevistadas.

## Relação com Outros Conceitos

- [[wiki/concepts/governanca-de-codigo-gerado-por-ia]] — a resposta organizacional necessária a este padrão: mais revisão, não menos
- [[wiki/concepts/novo-perfil-dev-ia]] — o engenheiro se move de "escrever" para "arquitetar e revisar"
- [[wiki/concepts/vibe-coding]] — risco equivalente quando aplicado por decisores sem julgamento técnico
- [[wiki/concepts/sdlc-nativo-de-ia]] — esta é a primeira das cinco regras do framework mais amplo

## Key Sources

- [[wiki/sources/guia-claude-code-para-startups-anthropic-ai-native-sdlc]]
