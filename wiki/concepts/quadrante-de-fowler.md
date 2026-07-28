---
type: concept
title: "Quadrante de Fowler (Tech Debt)"
aliases: ["quadrante fowler", "fowler tech debt quadrant", "tech debt quadrant"]
date_created: 2026-06-02
date_updated: 2026-07-28
source_count: 2
tags: [tech-debt, fowler, planejamento, engenharia, decisao]
skill: tech-mentor-leadership
status: stable
---

# Quadrante de Fowler (Tech Debt)

## TL;DR

Framework de [[wiki/entities/martin-fowler]] para categorizar tech debt em dois eixos: Deliberado vs. Inadvertido e Prudente vs. Imprudente. Apenas o debt Prudente+Deliberado é aceitável como ferramenta consciente de engenharia.

## Os Quatro Quadrantes

|  | **Deliberado** | **Inadvertido** |
|--|---------------|-----------------|
| **Prudente** | "Precisamos lançar agora, refatoramos depois" | "Agora sabemos como deveríamos ter feito" |
| **Imprudente** | "Não temos tempo para design" | "O que é design?" |

## O Único Debt Aceitável

Apenas o **Prudente + Deliberado** é uma ferramenta válida:
- Você conhece o custo
- Você escolhe conscientemente aceitar
- Você tem plano (condicional) de pagar

Os outros três quadrantes são falhas de processo ou competência.

## Relação com Velocidade de Validação

Na fase de validação de um produto/feature:
- A maioria das features falha
- Construir com arquitetura perfeita para algo que será descartado é desperdício
- Tech debt Prudente+Deliberado permite validar a ideia rapidamente

> "Faça o deploy com debt. Pague depois. **Se** sobreviver. Palavra-chave: se." — [[wiki/sources/5-principles-that-changed-me-as-a-programmer]]

## Quando Pagar o Debt

Se a feature sobreviver à validação e entrar em manutenção ativa, o debt deve ser pago antes que:
- O time cresça e o custo cognitivo se multiplique
- A complexidade impeça novas features
- O debt inadvertido se acumule em cima do deliberado

## Depois de Categorizar: Medir e Priorizar

O quadrante decide *se* tomar dívida conscientemente, mas não diz quanto tempo alocar para pagá-la nem por onde começar. [[wiki/sources/tech-debt-guia-completo-gestao-metricas]] cobre essa camada seguinte, hoje ausente desta página: modelos concretos de alocação de tempo (regra dos 20%, regra dos 25% do Shopify), mensuração formal via [[wiki/concepts/debt-ratio-sqale]] e priorização via [[wiki/concepts/hotspot-analysis]] e [[wiki/concepts/paid-framework]] — ver detalhamento em [[wiki/concepts/tech-debt-como-ferramenta]].

## Key Sources

- [[wiki/sources/5-principles-that-changed-me-as-a-programmer]]
- [[wiki/sources/tech-debt-guia-completo-gestao-metricas]] — modelos de alocação de tempo e mensuração formal, camada complementar ao quadrante
