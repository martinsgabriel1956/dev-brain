---
type: source
title: "Wardley Maps"
aliases: ["wardley maps", "wardley mapping", "value chain mapping", "evolution axis", "genesis commodity"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/wardley-maps.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [wardley-maps, strategy, value-chain, evolution, system-design, architecture-decision]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Wardley Maps: ferramenta de estratégia que visualiza componentes de um sistema em dois eixos — Visibilidade (Y: âncora no usuário até infraestrutura invisível) e Evolução (X: Genesis → Custom → Product → Commodity). Permite identificar onde investir (Genesis/Custom = diferenciar), onde terceirizar (Commodity = buy, não build), e onde o mercado vai commoditizar antes de você perceber. Complemento de ADR e C4 Model para decisões arquiteturais com contexto estratégico.

## Key Claims

**Claim:** O eixo de Evolução (Genesis → Commodity) é o elemento central de decisão estratégica — posição no eixo determina se você deve build, buy ou rent.
**Evidence:** Genesis: novo, incerto, diferenciador — build internamente. Custom-built: entendido mas não padronizado — ainda build se for core. Product: mercado tem soluções maduras — buy/license. Commodity/Utility: padronizado, sem diferenciação — use cloud/SaaS. Erro clássico: tratar um componente Commodity como Genesis (reinventar autenticação, logging, storage) desperdiça engenharia no que não diferencia.
**Confidence:** alta

**Claim:** O eixo de Visibilidade (Y) ancora o mapa no usuário — componentes invisíveis ao usuário ainda precisam ser mapeados porque suportam o que é visível.
**Evidence:** Topo do mapa: o que o usuário vê e valoriza diretamente (UI, features). Base: infraestrutura que o usuário nunca vê mas que tudo depende (rede, compute, storage). A âncora no topo é sempre uma necessidade do usuário (User Need), não uma tecnologia. Componentes sem visibilidade mas com alta dependência são os mais arriscados para ignorar.
**Confidence:** alta

**Claim:** Wardley Maps revelam onde o mercado vai commoditizar — antecipar essa movimentação é o uso estratégico principal.
**Evidence:** Em 2005, compute era Custom/Product (comprava servidor). Em 2010, AWS tornou compute Commodity (aluga sob demanda). Times que perceberam isso antes se desfizeram de data centers. O mapa permite perguntar: "quais dos nossos componentes Custom-built o mercado está tornando Produto/Commodity?" e ajustar o investimento antes de ser forçado a fazê-lo.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/wardley-maps]]
- [[concepts/value-chain]]
- [[concepts/evolution-axis]]
- [[concepts/genesis-to-commodity]]
- [[concepts/build-vs-buy]]
- [[concepts/strategic-architecture]]

## Open Questions

- Wardley Maps em equipes pequenas — o overhead de manter mapas atualizados compensa para times < 10 engenheiros?
- Como combinar Wardley Maps com Domain-Driven Design (Core Domain vs Supporting Domain) — os eixos se alinham?
