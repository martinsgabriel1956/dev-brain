---
type: concept
title: "Tech Debt como Ferramenta"
aliases: ["tech debt deliberado", "dívida técnica estratégica", "ship with debt"]
date_created: 2026-04-26
date_updated: 2026-07-09
source_count: 5
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

## Pagando o Debt Inadvertido — Boy Scout Rule

O quadrante de Fowler descreve como *tomar* debt conscientemente. Para o debt inadvertido que se acumula de qualquer forma (código que degrada com o tempo mesmo sem decisão explícita), a estratégia de pagamento contínuo mais citada é a [[wiki/concepts/boy-scout-rule]]: deixar o código um pouco mais limpo a cada mudança, em vez de esperar por um projeto de refactoring dedicado.

## Leitura via Tríade Retorno-Risco-Liquidez

O [[wiki/concepts/avaliar-hype-tecnologico]] descreve o mesmo raciocínio com outro vocabulário: tomar tech debt (ou over-engineering, ou adotar uma tecnologia hype) sempre significa aceitar risco alto e liquidez baixa — a decisão só é boa se a rentabilidade esperada compensar esses dois eixos ruins. Uma dívida tomada sem retorno proporcional é, nesse modelo, simplesmente um mau negócio, e é isso que separa debt Prudente+Deliberado de debt Imprudente.

## Relacionado

[[concepts/observabilidade]] · [[sources/conceitos-que-ninguem-ensina]] · [[wiki/concepts/boy-scout-rule]] · [[wiki/concepts/avaliar-hype-tecnologico]]

## Key Sources

- [[sources/5-principios-programador]]
- [[wiki/sources/5-principles-that-changed-me-as-a-programmer]]
- [[wiki/sources/5-principios-que-mudaram-como-programador]]
- [[wiki/sources/como-identificar-o-proximo-hype-tecnologico]]
