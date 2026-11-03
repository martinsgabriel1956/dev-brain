---
type: concept
title: "Mapa de Transições"
aliases: ["tabela de transições", "transition map", "máquina de estados com dicionário"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 1
tags: [fsm, state-machine, modelagem, validacao, pedidos, agentes]
skill: tech-mentor-backend
status: stub
---

# Mapa de Transições

Forma de implementar uma [[wiki/concepts/finite-state-machine|máquina de estados]] como dado: um mapa diz, para cada estado, para quais outros ele pode ir. Toda transição é validada contra esse mapa, no lugar de `if`s espalhados pelo código.

## Passos

1. Definir os estados válidos.
2. Definir o mapa de transições.
3. Validar cada tentativa de transição contra o mapa.

```python
TRANSITIONS = {
    "pending": {"paid", "cancelled"},
    "paid": {"shipped"},
    "shipped": {"delivered"},
    "delivered": set(),
    "cancelled": set(),
}

def can_transition(current, new):
    return new in TRANSITIONS[current]
```

O código acima é uma ilustração da wiki: o vídeo descreve um dicionário e cita pattern matching em Elixir, mas o código da tela não está na transcrição. O autor diz que a tecnologia importa pouco.

## Diferença do State Pattern

O [[wiki/concepts/state-pattern]] modela cada estado como uma classe, com comportamento próprio. O mapa só guarda as regras de transição, e por isso é mais simples quando os estados não mudam o comportamento do objeto (inferência da wiki).

## Uso com agentes de IA

A fonte sugere o mesmo desenho para orquestrar agentes, com requisitos, validação e gatilhos em cada transição. É o papel das arestas determinísticas em [[wiki/concepts/grafo-como-abstracao-de-agentes]].

## Key Sources

- [[wiki/sources/cinco-design-patterns-strategy-observer-adapter-state-machine-retry-circuit-breaker]]
