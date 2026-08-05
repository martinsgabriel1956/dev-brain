---
type: concept
title: "BDD — Behavior-Driven Development"
aliases: ["behavior driven development", "gherkin", "cucumber", "specs executáveis"]
date_created: 2026-04-22
date_updated: 2026-08-04
source_count: 4
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

Vale notar: BDD é frequentemente citado como boa prática por pessoas que admitem ter pouca experiência prática com ele — reforça a "armadilha crítica" acima, já que é fácil recomendar BDD em tese sem ter sentido o overhead na prática.

## Given/When/Then sem Gherkin — uso pessoal de planejamento

[[wiki/concepts/mapear-entrada-processamento-saida]] usa a mesma sintaxe dado/quando/então do Gherkin acima, mas como anotação pessoal de um dev antes de codificar — sem `.feature` files, step definitions ou engajamento de PO/QA. Não é BDD (falta o ritual completo de spec compartilhada e viva no CI), mas mostra que o valor do formato Given/When/Then como ferramenta de *pensamento* é separável do valor de BDD como *processo* de alinhamento com o negócio.

## Gherkin Pega o Erro que Testes Unitários Não Pegam: Construir a Coisa Errada

[[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] posiciona Gherkin/BDD dentro de uma lista de cinco verificações que [[wiki/entities/uncle-bob]] usa em vez de ler código gerado por agentes (junto com teste unitário, cobertura, [[wiki/concepts/teste-de-mutacao|mutation testing]] e métrica de qualidade). O papel específico atribuído ao Gherkin nessa lista: pega o pior tipo de erro de todos — construir a coisa errada, mesmo que construída certo. Teste unitário confirma que o código faz o que diz que faz; Gherkin confirma que o que ele faz é, de fato, o que deveria ser feito. A fonte também liga isso diretamente a [[wiki/concepts/spec-driven-development]]: escrito antes da implementação, o Gherkin funciona como a spec — a única peça do sistema que o agente não derivou da própria cabeça, usada depois para validar implementação e testes contra a mesma fonte da verdade.

## Key Sources

- [[wiki/sources/bdd]]
- [[wiki/sources/tdd-sdd-bdd-era-ia]] — cobertura mais rasa, autor declara pouca prática com BDD
- [[wiki/sources/3-pilares-testes-automatizados-produtividade]] — Given/When/Then usado como anotação pessoal de planejamento, fora do contexto formal de BDD
- [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] — Gherkin como o item que pega "construir a coisa errada", e sua função de spec imutável equivalente ao Spec-Driven Development
