---
type: concept
title: "Reconhecimento de Padrões (Pattern Recognition)"
aliases: ["pattern recognition", "detecção de padrões", "reconhecimento de padrão"]
date_created: 2026-05-16
date_updated: 2026-05-16
source_count: 1
tags: [aprendizado, cognicao, padroes]
skill: tech-mentor-leadership
status: stable
---

# Reconhecimento de Padrões (Pattern Recognition)

Capacidade humana de detectar repetições e regularidades via os sentidos, sem necessidade de instrução explícita. É o mecanismo primário pelo qual aprendemos linguagem, comportamentos sociais e habilidades motoras. Em programação, é a base do [[wiki/concepts/aprendizado-por-exposicao|aprendizado por exposição]].

## Distinção entre os três "padrões" em inglês

| Palavra | Tradução aproximada | Significado |
|---|---|---|
| **Standard** | Padrão-regulamento | Regra a seguir (ex: "padrão da indústria") |
| **Default** | Padrão-default | Opção escolhida quando nenhuma outra é especificada |
| **Pattern** | Padrão-repetição | Algo que se repete — não implica que seja bom |

Em tecnologia, usamos *pattern* quase sempre. É importante entender que um pattern **não é uma regra** — é apenas uma repetição observada. Pode ser uma boa prática ou um [[wiki/concepts/anti-pattern|anti-pattern]].

## Faca de dois gumes

O sistema de reconhecimento de padrões humano é poderoso mas falível:
- **Ilusões de ótica** exploram bugs nesse sistema.
- **Superstições** surgem de correlações falsas detectadas pelo sistema (passar embaixo de uma escada → azar).
- **Viés de confirmação** é uma falha de correlação — o sistema detecta padrões que confirmam crenças existentes.

## Relação com Design Patterns

[[wiki/concepts/design-patterns|Design Patterns]] são patterns *nomeados* — repetições que já foram observadas por muitas pessoas e receberam um nome para facilitar a comunicação. Quem aprende os nomes *antes* de ver os padrões na prática tende a aplicar os patterns errado. A sequência correta é: exposição → reconhecimento espontâneo → nomeação via estudo formal.

## Key Sources

- [[wiki/sources/akita-como-aprender-programacao]] — distinção entre standard/default/pattern; faca de dois gumes; relação com aprendizado de português
