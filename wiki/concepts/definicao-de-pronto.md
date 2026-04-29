---
type: concept
title: "Definição de Pronto"
aliases: ["definition of done", "DoD", "o que é pronto", "pronto de verdade"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [hábitos, qualidade, craftsmanship, código, entrega, carreira]
skill: tech-mentor-leadership
status: stable
---

# Definição de Pronto

O conjunto de critérios que uma entrega precisa satisfazer para ser considerada **realmente pronta** — não só "funciona na minha máquina".

## O engano mais comum

Marcar a task como "done" logo que o código funciona na primeira execução. Escrever código é apenas uma das muitas tarefas de um programador.

```
❌ Funciona na minha máquina = pronto
✅ Pronto de verdade:
   - Outro dev consegue entender sem me perguntar?
   - Testei o caminho feliz E os casos de erro?
   - A documentação reflete essa mudança?
   - Revisei pensando em regra de negócio, não só em estilo?
```

## Checklist mínimo de "pronto"

| Critério | Pergunta |
|---|---|
| Legibilidade | Outro dev entende sem contexto adicional? |
| Testes | Happy path + casos de erro cobertos? |
| Documentação | Algum doc precisa ser atualizado? |
| Regra de negócio | A lógica está correta, não só a sintaxe? |
| Revisão crítica | Me perguntei onde isso pode quebrar? |

## O rascunho disfarçado de entrega

Código que só você entende não está pronto — é um rascunho. A "maior imagem" (maior sinal) para refatorar é exatamente essa: se outro dev precisar perguntar o que aquilo faz, o código não está pronto.

## Code review focado no lugar errado

Outro sintoma: revisar o próprio PR focando em estilização e formatação em vez de regra de negócio. Estilo é mais fácil de checar — mas regra de negócio é o que importa.

## Ver também

- [[testar-proprio-codigo]] — um dos critérios de "pronto"
- [[atomic-commits]] — commits que representam unidades funcionais prontas

## Key Sources

- [[wiki/sources/habitos-ruins-de-programador]]
