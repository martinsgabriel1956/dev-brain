---
type: concept
title: "Módulo Profundo (Deep Module)"
aliases: ["deep module", "shallow module", "módulo raso", "caixa cinza"]
date_created: 2026-07-09
date_updated: 2026-07-10
source_count: 2
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

## Origem no enquadramento geral do livro

[[wiki/sources/filosofia-do-design-de-software-introducao]] (fonte primária, capítulo 1) enquadra módulos profundos como a elaboração da segunda das duas estratégias gerais contra complexidade que abrem o livro: **eliminar** complexidade (código mais simples/óbvio) vs. **encapsular** complexidade (design modular). Módulo profundo é a forma de fazer um módulo encapsular bem — módulo raso é encapsulamento malfeito. O texto também cita "classes devem ser profundas" como exemplo do tipo de princípio filosófico (não receita mecânica) que o livro inteiro oferece — reforçando que é uma heurística de comparação entre alternativas, não uma regra absoluta. Ver também [[wiki/concepts/red-flags-de-design]]: módulo raso é um dos red flags mais citados no livro.

## Relação com outros conceitos

- [[wiki/concepts/complexidade-acidental]] — módulos rasos são uma forma comum de complexidade acidental: a estrutura, não o problema em si, é o que dificulta entender o sistema.
- [[wiki/concepts/arquitetura-de-software]] — decisão de estrutura que escala bem (poucos módulos profundos) vs. que gera bola de neve (muitos módulos rasos).
- [[wiki/concepts/tdd]] — interfaces simples de módulos profundos são o que torna o ciclo RED-GREEN-REFACTOR sustentável.
- [[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental]] — módulos profundos como estratégia de encapsulamento se aplicam melhor sob design incremental, onde a interface pode ser revisada e ajustada a cada iteração.
- [[wiki/concepts/red-flags-de-design]] — módulo raso é o red flag concreto correspondente a este conceito.

## Key Sources

- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
- [[wiki/sources/filosofia-do-design-de-software-introducao]]
