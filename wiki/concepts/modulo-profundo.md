---
type: concept
title: "Módulo Profundo (Deep Module)"
aliases: ["deep module", "shallow module", "módulo raso", "caixa cinza"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [arquitetura, complexidade, design, ousterhout, interface, encapsulamento]
skill: tech-mentor-backend
status: draft
---

# Módulo Profundo (Deep Module)

## TL;DR

Conceito de [[wiki/entities/john-ousterhout]] (*A Philosophy of Software Design*): um **módulo profundo** esconde muita funcionalidade atrás de uma interface simples — a complexidade fica encapsulada dentro. Um **módulo raso** faz o oposto: expõe pouca funcionalidade atrás de uma interface relativamente complexa, multiplicando o número de peças que quem lê o código precisa rastrear ao mesmo tempo.

## Profundo vs. raso

| | Módulo Profundo | Módulo Raso |
|---|---|---|
| Funcionalidade | Muita, escondida | Pouca, exposta |
| Interface | Simples | Complexa |
| Consumidor precisa olhar por dentro? | Não (mas pode) | Praticamente sim |
| Custo cognitivo de leitura | Baixo — poucos blocos grandes | Alto — muitos blocos pequenos para navegar |

Poucos módulos grandes e profundos, com interfaces bem projetadas, tendem a produzir bases de código mais fáceis de entender do que muitos módulos pequenos que só delegam uns aos outros.

## Por que importa na era da IA

Agentes de IA são bons em produzir módulos rasos por padrão — muitas funções pequenas, cada uma fazendo pouco. Isso é ruim para a própria IA: ao explorar a base de código depois, ela precisa navegar por um número maior de peças, tem mais chance de não encontrar a dependência certa a tempo, e frequentemente falha em entender o sistema como um todo.

Módulos profundos, por outro lado, permitem tratar a implementação como **caixa cinza**: o humano projeta e revisa cuidadosamente a **interface** (que deve ter alto controle humano, pois um erro de design aí se propaga), mas pode delegar a **implementação** por trás dela à IA sem revisar linha a linha — desde que a fronteira seja testável e o propósito do módulo esteja claro. Ver [[wiki/concepts/tdd]] — módulos profundos são o que torna uma base de código genuinamente testável, porque a fronteira de teste é a própria interface, simples por definição.

Existe uma skill de refatoração citada na fonte ("improve codebase architecture") cujo objetivo é migrar uma base de código de módulos rasos para módulos profundos: explorar o código em busca de blocos relacionados e envolvê-los dentro de uma fronteira única com interface simples.

## Relação com outros conceitos

- [[wiki/concepts/complexidade-acidental]] — módulos rasos são uma forma comum de complexidade acidental: a estrutura, não o problema em si, é o que dificulta entender o sistema.
- [[wiki/concepts/arquitetura-de-software]] — decisão de estrutura que escala bem (poucos módulos profundos) vs. que gera bola de neve (muitos módulos rasos).
- [[wiki/concepts/tdd]] — interfaces simples de módulos profundos são o que torna o ciclo RED-GREEN-REFACTOR sustentável.

## Key Sources

- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
