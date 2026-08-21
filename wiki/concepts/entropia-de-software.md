---
type: concept
title: "Entropia de Software"
aliases: ["software entropy", "software decay", "degradação de código"]
date_created: 2026-07-27
date_updated: 2026-08-14
source_count: 3
tags: [refactoring, tech-debt, craftsmanship, design-de-software, code-rot, big-ball-of-mud]
skill: tech-mentor-backend
status: draft
---

# Entropia de Software

Tendência natural de um sistema de software degradar estruturalmente com o tempo, mesmo sem qualquer erro deliberado — cada nova funcionalidade, cada correção sob pressão de prazo, empurra o design um pouco para longe da organização original. Em inglês, o termo usado é *decay* ("o código vai degradando").

## Relação com refatoração

[[wiki/concepts/refatoracao]] é apresentada em [[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]] como o mecanismo prático para conter essa entropia: cada pequena refatoração — comparada a podar plantas daninhas e galhos em excesso num jardim — reduz a chance do sistema degradar further ao longo do tempo. A fonte usa a analogia de jardinagem do *Pragmatic Programmer*, em contraste deliberado com a analogia mais comum de construção civil: diferente de um prédio, o código é "vivo" e precisa de manutenção contínua, não apenas construção inicial correta.

Essa é a mesma dinâmica descrita, com outro vocabulário, em [[wiki/concepts/god-object]] (como uma classe limpa vira uma God Class sprint a sprint) e em [[wiki/concepts/tech-debt-como-ferramenta]] (débito técnico acumulado sem pagamento).

## Entropia como causa da Big Ball of Mud

[[wiki/sources/codigo-espaguete-wikipedia|Foote & Yoder]] listam a entropia de software — ao lado de pressão de negócio e rotatividade de desenvolvedores — como uma das três forças que tornam a [[wiki/concepts/big-ball-of-mud|Big Ball of Mud]] o estado *default* de sistemas de vida longa. A entropia não é o anti-padrão em si; é o vetor que empurra qualquer sistema em direção a ele na ausência de manutenção deliberada. É a mesma metáfora física da origem do [[wiki/concepts/code-espaguete|código espaguete]] ([[wiki/entities/richard-hamming|Hamming]]): a bagunça se acumula como subproduto de correções, não como decisão.

## Relacionado

[[wiki/concepts/refatoracao]] · [[wiki/concepts/tech-debt-como-ferramenta]] · [[wiki/concepts/god-object]]

## Key Sources

- [[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]]
- [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] — enumera as quatro forças da degradação (requisitos sobre arquitetura estática, perda de contexto entre equipes, hotfix sob pressão, casos não previstos) e propõe contramedidas majoritariamente organizacionais contra o code rot
- [[wiki/sources/codigo-espaguete-wikipedia]] — entropia como uma das três forças que geram a Big Ball of Mud
