---
type: concept
title: "Fluxo de Controle"
aliases: ["control flow", "estruturas de controle", "if while for"]
date_created: 2026-05-13
date_updated: 2026-05-13
source_count: 1
tags: [fluxo-de-controle, control-flow, fundamentos, cs-fundamentals]
skill: cs-fundamentals
status: draft
---

# Fluxo de Controle

Mecanismos de linguagem que determinam a ordem em que as instruções são executadas: condicionais (`if/else`), loops (`while/for`) e chamadas de função. São a materialização em código do [[fluxo-logico]] desenhado antes.

## Mapeamento fluxo → código

Cada estrutura de decisão no fluxo lógico corresponde a uma estrutura de controle:

| Decisão no fluxo | Estrutura em código |
|---|---|
| "se X então Y, senão Z" | `if / else` |
| "repita enquanto condição" | `while` |
| "para cada item" | `for` |
| "retorne e pare" | `return` / `break` |

## Exemplo

```python
# Fluxo: "enquanto tentativas < 3, peça senha; se correta, autentique"
while tentativas < MAX_TENTATIVAS:
    if senha_correta(cartao, solicitar_senha()):
        return True
    tentativas += 1
```

O `while` captura "repita até chegar no limite". O `if` captura "senha correta?". O `return True` captura "autenticação concluída, encerre o loop".

## Relação com outros conceitos

- É a implementação concreta do [[fluxo-logico]]
- Usa [[estado]] para tomar decisões baseadas em histórico
- É parte central de [[traducao-logica-para-codigo]]

## Key sources

- [[wiki/sources/logica-de-programacao-quatro-passos]]
