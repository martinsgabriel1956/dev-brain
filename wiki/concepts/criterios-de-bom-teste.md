---
type: concept
title: "Critérios de Bom Teste"
aliases: ["determinístico conciso relevante", "o que faz um teste bom", "qualidade de testes"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_count: 1
tags: [testes, qualidade, flaky, relevância, craftsmanship]
skill: tech-mentor-testing
status: stable
---

# Critérios de Bom Teste

Cinco critérios para avaliar se um teste (de qualquer camada — unitário, integração ou E2E) vale o custo de mantê-lo.

## Os cinco critérios

| Critério | O que significa | Falha comum |
|---|---|---|
| **Determinístico** | Mesmo input, mesmo resultado, sempre | Flaky test — passa e falha aleatoriamente; se não é determinístico, não vale nada, delete |
| **Conciso** | Testa uma coisa, um comportamento | Teste "gordo" que quebra por qualquer motivo, obrigando reescrita inteira |
| **Relevante** | Cobre um caso de uso ou regra de negócio real | Testes "de livro" — `add(2,3) === 5` — que não protegem nada que de fato quebraria |
| **Compreensível** | Dá para entender o que e por que está sendo testado só de ler | Setup complexo, asserções obscuras, nomes genéricos |
| **Durável** | Continua útil e passando enquanto o comportamento não muda | Teste acoplado a detalhe de implementação ou UI que muda com frequência |

## Coverage 100% não é o objetivo

Cobrir uma linha de código cinco vezes com testes não garante ausência de bug — só garante que os comportamentos *que alguém pensou em testar* não regridem silenciosamente. Não existe forma de escrever um teste para um bug que ninguém imaginou que pudesse existir (ex.: integer overflow, um edge case de input malicioso). É possível ter "500% de testagem" e zero testes relevantes.

```
100% coverage ≠ ausência de bugs
100% coverage = toda linha foi executada nos testes
                 (não diz nada sobre quais valores/casos foram exercitados)
```

## Relevância acima de concisão

Na prática, relevância tende a importar mais que concisão — um teste levemente "gordo" que valida uma regra de negócio real vale mais que dez testes concisos e irrelevantes.

## Ver também

- [[piramide-de-testes]] — esses critérios valem para as três camadas, mas se aplicam com dificuldade crescente (E2E é o mais difícil de manter conciso e durável)
- [[testar-proprio-codigo]] — relevância implica testar além do happy path
- [[gaming-de-testes-por-ia]] — um teste não-determinístico ou irrelevante é terreno fértil para a IA "resolver" o problema enfraquecendo o teste em vez do código

## Key Sources

- [[wiki/sources/teste-unitario-integracao-e2e-opiniao]]
