---
type: concept
title: "Design First"
aliases: ["design-first approach", "design antes do código"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
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

## Ver também

- [[code-first]] — abordagem oposta
- [[design-engineer]] — papel que dissolve a separação entre as duas abordagens
- [[figma]] — ferramenta central no workflow design first

## Key Sources

- [[wiki/sources/design-first-vs-code-first-referencias]]
