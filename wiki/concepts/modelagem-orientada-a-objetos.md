---
type: concept
title: "Modelagem Orientada a Objetos"
aliases: ["OOP modeling", "modelagem OO", "object-oriented modeling", "modelagem de domínio"]
date_created: 2026-06-09
date_updated: 2026-08-13
source_count: 2
tags: [oo, modelagem, fundamentos, design-patterns, arquitetura, encapsulamento, modelo-de-dominio-anemico]
skill: tech-mentor-leadership
status: stable
---

## Definição

Habilidade de representar um domínio de negócio em termos de objetos, seus atributos e os relacionamentos entre eles. É o pré-requisito obrigatório para usar design patterns e arquitetura orientada a objetos com eficácia.

Saber modelar não é saber uma linguagem — é saber **pensar o domínio antes de codificá-lo**.

---

## As Perguntas da Modelagem

Para qualquer domínio, o modelador precisa responder:

1. **O que vira classe?** — Quais entidades do domínio têm identidade e comportamento próprios?
2. **O que vira atributo?** — Que dados cada objeto precisa manter para operar?
3. **Como os objetos se associam?** — Quais são os relacionamentos? São associações simples, composições ou dependências?
4. **Que tipo de relacionamento existe?** — É uma hierarquia (herança), uma composição (o todo tem as partes) ou uma colaboração (objeto usa outro objeto)?

---

## Por Que É Pré-Requisito para Design Patterns

[[design-patterns]] são soluções para problemas recorrentes em modelos orientados a objetos. Se o desenvolvedor não souber modelar, não consegue:

- Identificar qual problema o pattern resolve
- Saber quando um pattern é adequado
- Evitar o [[over-engineering]] de aplicar patterns onde não há problema correspondente

O resultado de pular esse pré-requisito é o "verde neném": patterns aplicados em todo lugar sem critério, tornando o código mais complexo sem melhorá-lo.

---

## Progressão de Aprendizado

A modelagem OO é o **estágio 2** de uma progressão incremental:

| Estágio | Conteúdo |
|---|---|
| 1 | [[logica-de-programacao]], algoritmos, dominar uma linguagem |
| **2** | **Modelagem OO** — classes, atributos, relacionamentos |
| 3 | [[design-patterns]], TDD, arquitetura |

Tentar ir direto do estágio 1 para o 3 é a causa mais comum de [[over-engineering]] em quem está aprendendo.

---

## Conexões

- [[design-patterns]] — depende de modelagem OO como pré-requisito
- [[over-engineering]] — consequência de pular este estágio
- [[fundacao-tecnica]] — modelagem OO é parte da fundação do desenvolvedor OO
- [[logica-de-programacao]] — estágio anterior; precisa estar sólido antes da modelagem
- [[ddd]] — Domain-Driven Design estende a modelagem OO para domínios complexos
- [[wiki/concepts/encapsulamento]] — modelar bem é pôr as regras dentro do objeto que as possui; encapsulamento protege as invariantes desse modelo
- [[wiki/concepts/modelo-de-dominio-anemico]] — o que acontece quando a modelagem para nos atributos e deixa o comportamento de fora: dados sem regras

---

## Key Sources

- [[wiki/sources/aprender-antes-de-aplicar-fundamentos-e-otimizacao-prematura]]
- [[wiki/sources/encapsulamento-proteger-estado-invalido]] — exemplo prático de modelagem de domínio: regras de negócio (preço > 0, estoque não negativo) viram invariantes da classe `Product`
