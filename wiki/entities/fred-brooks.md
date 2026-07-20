---
type: entity
title: "Fred Brooks"
aliases: ["fred brooks", "Frederick Brooks", "No Silver Bullet", "Mythical Man-Month"]
date_created: 2026-04-23
date_updated: 2026-07-20
source_count: 3
tags: [fred-brooks, essential-complexity, accidental-complexity, software-engineering, mythical-man-month, design-concept]
skill: tech-mentor-system-design
status: stable
---

## Quem é

Frederick P. Brooks Jr. (1931–2022) — cientista da computação americano, gerente do projeto OS/360 da IBM, professor na UNC Chapel Hill. Vencedor do Prêmio Turing (1999).

## Contribuições relevantes para o wiki

**"The Mythical Man-Month" (1975)** — argumenta que adicionar pessoas a um projeto de software atrasado o atrasa ainda mais (Lei de Brooks). Conceitos de comunicação exponencial e integridade conceitual de sistema.

**"No Silver Bullet — Essence and Accident in Software Engineering" (1986)** — artigo seminal que introduz a distinção entre:
- [[concepts/essential-complexity]] — inerente ao problema, não pode ser eliminada
- [[concepts/accidental-complexity]] — introduzida pelo time, pode e deve ser eliminada

Argumento central: não existe bala de prata em software porque a maior parte da dificuldade é complexidade essencial — nenhuma linguagem, ferramenta ou metodologia pode remover o que é inerente ao domínio.

**"The Design of Design" (2010)** — introduz a ideia de **design concept**: quando mais de uma pessoa projeta algo junto, existe uma teoria compartilhada e invisível do que está sendo construído flutuando entre elas — não é um artefato, não cabe num documento, mas precisa ser genuinamente compartilhada antes de qualquer plano fazer sentido. [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] aplica essa ideia à colaboração humano-IA: a causa de "a IA não fez o que eu queria" é a ausência de um design concept compartilhado entre dev e IA, resolvida forçando uma fase de entrevista adversarial (percorrendo "cada ramo da árvore de decisão de design") antes de qualquer PRD ou plano.

## Coordenação e agentes de IA

[[wiki/sources/cognitive-debt-margaret-storey]] estende a Lei de Brooks (adicionar pessoas a um projeto atrasado o atrasa mais) para agentes de IA: adicionar mais agentes a um projeto aumenta sobrecarga de coordenação e decisões invisíveis, esticando a capacidade cognitiva humana — o mesmo mecanismo de comunicação exponencial de *The Mythical Man-Month*, agora com agentes no lugar de pessoas.

## Citação central

> "The hardest single part of building a software system is deciding precisely what to build. No other part of the conceptual work is so difficult to establish, or so prone to causing the disaster if not done right."

## Relação com outros conceitos

- [[concepts/accidental-complexity]] — conceito cunhado por Brooks
- [[concepts/essential-complexity]] — conceito cunhado por Brooks
- [[concepts/ddd-strategic]] — DDD é uma metodologia para lidar com complexidade essencial de domínio

## Key Sources

- [[sources/conceitos-que-ninguem-ensina]]
- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
- [[wiki/sources/cognitive-debt-margaret-storey]] — coordenação/sobrecarga cognitiva aplicada a agentes de IA
