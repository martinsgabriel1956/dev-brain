---
type: concept
title: "Ego-Driven Development"
aliases: ["ego-driven development", "ego na engenharia", "desenvolvimento guiado por ego"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
tags: [ego, over-engineering, carreira, qualidade, comportamento, soft-skills]
skill: tech-mentor-backend
status: stable
---

## Definição

Ego-Driven Development é quando decisões técnicas são guiadas pela necessidade de demonstrar conhecimento ou impressionar, em vez de serem guiadas pelos requisitos do projeto. A abstração vira troféu, não ferramenta.

Não é um diagnóstico moral — é um padrão comportamental documentado, especialmente em devs em transição do nível júnior/pleno para sênior.

## Como se manifesta

- Escolher um padrão por ser "o que o dev que eu admiro usaria" em vez de por adequação ao problema.
- Abstrair antecipando requisitos fictícios ("e se um dia precisarmos disso?").
- Justificar complexidade com o nome do padrão em vez de com o problema que ele resolve.
- Resistência a simplificar porque "ficaria feio".
- Comparar o próprio código ao código do sênior e concluir que simples = ruim.

## A progressão típica

1. **Júnior:** Pensa simples por limitação de conhecimento.
2. **Pleno:** Aprende padrões, arquitetura, design patterns. Começa a aplicar tudo que sabe.
3. **Transição para sênior:** Aplica padrões sem ancoragem nos requisitos — ego-driven development.
4. **Sênior real:** Aprende a suprimir o viés de complexidade. Usa padrões por necessidade, não por demonstração.

## Consequência sistêmica

Ego-driven development não é só um problema individual. Quando o código resultante exige conhecimento restrito, o time ao redor cria gambiarras para contornar o que não entende. O resultado final pode ser pior do que uma gambiarra direta — um Frankenstein com arquitetura bonita por fora e remendos por dentro.

## Relação com outros conceitos

- [[concepts/over-engineering]] — ego-driven development é o mecanismo psicológico que produz over-engineering
- [[concepts/kiss]] — o antídoto comportamental
- [[concepts/abstraction-bloat]] — efeito análogo com IA como vetor (viés de treinamento vs viés de ego)

## Key Sources

- [[sources/overengineering-carol-ate-quinta]]
