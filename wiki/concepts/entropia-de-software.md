---
type: concept
title: "Entropia de Software"
aliases: ["software entropy", "software decay", "degradação de código"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 1
tags: [refactoring, tech-debt, craftsmanship, design-de-software]
skill: tech-mentor-backend
status: stub
---

# Entropia de Software

Tendência natural de um sistema de software degradar estruturalmente com o tempo, mesmo sem qualquer erro deliberado — cada nova funcionalidade, cada correção sob pressão de prazo, empurra o design um pouco para longe da organização original. Em inglês, o termo usado é *decay* ("o código vai degradando").

## Relação com refatoração

[[wiki/concepts/refatoracao]] é apresentada em [[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]] como o mecanismo prático para conter essa entropia: cada pequena refatoração — comparada a podar plantas daninhas e galhos em excesso num jardim — reduz a chance do sistema degradar further ao longo do tempo. A fonte usa a analogia de jardinagem do *Pragmatic Programmer*, em contraste deliberado com a analogia mais comum de construção civil: diferente de um prédio, o código é "vivo" e precisa de manutenção contínua, não apenas construção inicial correta.

Essa é a mesma dinâmica descrita, com outro vocabulário, em [[wiki/concepts/god-object]] (como uma classe limpa vira uma God Class sprint a sprint) e em [[wiki/concepts/tech-debt-como-ferramenta]] (débito técnico acumulado sem pagamento).

## Relacionado

[[wiki/concepts/refatoracao]] · [[wiki/concepts/tech-debt-como-ferramenta]] · [[wiki/concepts/god-object]]

## Key Sources

- [[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]]
