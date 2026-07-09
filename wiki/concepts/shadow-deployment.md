---
type: concept
title: "Shadow Deployment"
aliases: ["shadow deploy", "shadow traffic", "dark launch"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [devops, deploy, cicd, observabilidade, infra]
skill: tech-mentor-infra
status: stable
---

# Shadow Deployment

100% dos usuários continuam sendo servidos pela v1. Em paralelo, os mesmos requests reais são duplicados/replicados para uma v2 que roda "nas sombras" — nenhum usuário vê ou depende da resposta dela.

## Fluxo

```
Request do usuário
      │
      ├──→ v1 responde ao usuário (produção real)
      │
      └──→ cópia do request → v2 processa em paralelo, resposta descartada
                                (monitorada: erro? latência? diferença de resultado?)
```

## Por que é valioso

Valida a v2 com **tráfego de produção real** — não um teste sintético, não um percentual limitado de usuários reais como no [[concepts/canary-release]]. Mede exatamente como o sistema se comporta sob a carga e os padrões de uso reais antes de qualquer usuário depender da resposta da v2. Zero risco para o usuário: se a v2 quebra, ninguém percebe.

## Por que é complicado e caro

- **Custo**: v2 roda em paralelo consumindo compute completo, sem nenhum benefício direto de tráfego servido — 2x custo de compute.
- **Side effects**: sistemas que enviam e-mail, cobram cartão, disparam webhooks — duplicar o request duplica o efeito colateral. Precisa mockar ou isolar side effects na v2.
- **Banco de dados**: se a v2 escreve, a escrita precisa ser isolada (banco espelhado, ou mock de escrita) para não corromper o estado real. Questão em aberto na fonte que introduziu o conceito: duplicar o banco inteiro ou mockar a camada de escrita — ambas trade-offs custosos.

## Quando usar

Migrações de sistemas críticos onde o custo de um bug em produção é muito maior que o custo de rodar dois sistemas em paralelo por um tempo (ex.: reescrever motor de cálculo de preço, motor de fraude, sistema de matching).

## Comparação com Canary e A/B

| | Quem vê a resposta da v2 | Objetivo |
|---|---|---|
| [[concepts/canary-release]] | Um percentual real de usuários | Reduzir risco técnico |
| [[concepts/ab-testing-deployment]] | Um percentual real de usuários | Validar hipótese de negócio |
| Shadow | Ninguém — resposta é descartada | Validar correção/performance com tráfego real, risco zero |

## Key Sources

- [[sources/tipos-de-deploy]]
