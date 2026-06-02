---
type: concept
title: "Tech Debt como Ferramenta"
aliases: ["tech debt deliberado", "dívida técnica estratégica", "ship with debt"]
date_created: 2026-04-26
date_updated: 2026-06-02
source_count: 3
tags: [tech-debt, carreira, craftsmanship, estrategia, velocidade]
skill: tech-mentor-leadership
status: draft
---

# Tech Debt como Ferramenta

Tech debt não é sinônimo de código ruim — é uma **decisão financeira consciente**: aceitar custo futuro em troca de velocidade presente. O erro não é ter debt; é não saber quando tomá-lo e quando pagá-lo.

## O Quadrante de Fowler

```
                    Deliberado            Inadvertido
                  ┌─────────────────┬──────────────────┐
   Imprudente     │ "Não temos tempo │ "O que é design  │
                  │ para design"     │ em camadas?"     │
                  ├─────────────────┼──────────────────┤
   Prudente       │ "Ship agora,     │ "Agora entendemos│
                  │ refatorar depois"│ como deveria ser"│
                  └─────────────────┴──────────────────┘
```

Único debt aceitável: **Prudente + Deliberado** — decisão consciente de ir rápido para validar, com plano de pagar se a feature sobreviver.

## Quando tomar debt deliberado

- Feature em fase de validação — pode ser descartada se não funcionar
- Prazo real com impacto de negócio mensurável
- O shortcut é localizado e reversível (não contamina arquitetura inteira)

## Quando NÃO tomar debt

- Código em módulo crítico que muda com frequência (hotspot)
- Ausência de testes em lógica financeira ou de segurança
- "Vamos reescrever depois" sem data e sem dono — isso é negligência, não debt

## A regra do if

> "Entregue com dívida. Pague de volta **se** sobreviver. Palavra-chave: *se*."

A maioria das features falha. Não construa uma catedral para algo que pode ser demolido no mês que vem.

## Relacionado

[[concepts/observabilidade]] · [[sources/conceitos-que-ninguem-ensina]]

## Key Sources

- [[sources/5-principios-programador]]
- [[wiki/sources/5-principles-that-changed-me-as-a-programmer]]
