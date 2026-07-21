---
type: concept
title: "Design First"
aliases: ["design-first approach", "design antes do código"]
date_created: 2026-04-22
date_updated: 2026-07-21
source_count: 2
tags: [design, processo, workflow, figma, times]
skill: tech-mentor-frontend
status: stable
---

# Design First

Abordagem onde o **layout é desenhado antes de qualquer código ser escrito**. O Figma (ou similar) é a fonte de verdade, e o código implementa o que foi desenhado.

## Quando funciona bem

✅ Times com separação clara entre designers e devs frontend
✅ Produtos com múltiplas superfícies que precisam de consistência visual
✅ Empresas grandes com design system estabelecido

## Problema central em times pequenos

Se a mesma pessoa (ou time pequeno) faz design e código, **o Figma fica desatualizado rapidamente** conforme o código evolui. Cada ajuste no código que não volta para o Figma cria divergência.

```
Design no Figma → Implementação em código
                ↓
         Ajustes no código → Figma não atualizado
                ↓
         Figma vira arqueologia, não documentação
```

## Comparação com Code First

| | Design First | Code First |
|---|---|---|
| Quando usar | Times grandes com designers dedicados | Times pequenos, MVPs, protótipos |
| Consistência | Alta (se mantida) | Depende da visão de design do dev |
| Velocidade inicial | Lenta (design antes) | Rápida (sai codando) |
| Risco principal | Figma desatualizado | "Frankenstein" visual sem coesão |

## Variante com IA: geração de conceito antes do Figma

Ferramentas como [[wiki/entities/ux-pilot]] adicionam uma etapa antes do Figma clássico: geram o conceito de UI/UX (ou wireframe) a partir de prompt, exportam para o Figma, e de lá conectam via MCP a uma IA de código. O Figma continua sendo o ponto de handoff entre design e implementação, mas deixa de ser onde o design nasce — nasce no prompt, aplicando princípios como [[wiki/concepts/hierarquia-visual]] e [[wiki/concepts/lei-da-proximidade-gestalt]] diretamente na geração.

## Ver também

- [[code-first]] — abordagem oposta
- [[design-engineer]] — papel que dissolve a separação entre as duas abordagens
- [[figma]] — ferramenta central no workflow design first
- [[wiki/entities/ux-pilot]] — ferramenta de geração de UI/UX por IA que antecede o Figma nesse pipeline

## Key Sources

- [[wiki/sources/design-first-vs-code-first-referencias]]
- [[wiki/sources/5-boas-praticas-uiux-ux-pilot]]
