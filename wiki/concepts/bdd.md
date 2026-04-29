---
type: concept
title: "BDD — Behavior-Driven Development"
aliases: ["behavior driven development", "gherkin", "cucumber", "specs executáveis"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [testes, bdd, gherkin, cucumber, especificação, living-docs]
skill: tech-mentor-testing
status: stable
---

# BDD — Behavior-Driven Development

Extensão do [[tdd]] que usa **linguagem de domínio (Gherkin)** para descrever comportamentos como especificações executáveis — simultaneamente documentação e testes. Elimina o gap entre o que o negócio especifica e o que o time implementa.

## Fluxo

```
PO/QA escreve cenário em Gherkin
         ↓
Dev mapeia steps para código (step definitions)
         ↓
Testes executam os cenários no CI
         ↓
Relatório vira living documentation — sempre sincronizada com o código
```

## Gherkin — Given / When / Then

```gherkin
Feature: Checkout com cupom de desconto

  Scenario: Cupom válido aplica desconto
    Given tenho itens no carrinho no valor de R$ 250,00
    When aplico o cupom "SAVE10"
    Then o total deve ser R$ 225,00
    And vejo a mensagem "Cupom aplicado com sucesso"

  Scenario: Cupom expirado é rejeitado
    Given o cupom "EXPIRED20" está vencido
    When tento aplicar o cupom "EXPIRED20"
    Then vejo o erro "Cupom expirado"
```

- `Background` → executa antes de cada cenário (equivalente ao `beforeEach`)
- `Scenario Outline` + `Examples` → gera um teste por linha da tabela

## BDD vs TDD

| | TDD | BDD |
|---|---|---|
| Linguagem | Código | Gherkin (natural) |
| Autor | Dev | PO/QA/Dev |
| Granularidade | Unitário/integração | Comportamento de negócio |
| Documentação | Não | Sim — living docs |
| Overhead | Baixo | Médio-alto |

BDD não substitui TDD — são complementares. TDD para o design interno, BDD para os contratos de comportamento visíveis ao negócio.

## Armadilha crítica

BDD sem engajamento do negócio = testes com sintaxe mais verbosa. Se só o dev escreve os `.feature` files, você tem o overhead sem o benefício de alinhamento.

## Quando usar / evitar

**Use:** domínio complexo com regras mal-entendidas, time com QA dedicado, produto regulado (fintech, healthtech).
**Evite:** times de 2-3 devs, sistemas técnicos sem regras de negócio visíveis, PO não disposto a revisar cenários.

## Ver também

- [[tdd]] — base do BDD
- [[living-documentation]] — output natural do BDD via CI
- [[piramide-de-testes]] — BDD vive no topo/meio da pirâmide

## Key Sources

- [[wiki/sources/bdd]]
