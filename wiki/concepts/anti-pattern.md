---
type: concept
title: "Anti-Pattern"
aliases: ["antipattern", "anti-padrão"]
date_created: 2026-05-16
date_updated: 2026-08-14
source_count: 2
tags: [padroes, codigo, design, anti-patterns]
skill: tech-mentor-leadership
status: stub
---

# Anti-Pattern

Um [[wiki/concepts/pattern-recognition|pattern]] (repetição observada) que parece uma solução mas na prática cria problemas. A diferença entre pattern e anti-pattern não está na frequência de ocorrência — ambos são repetições — mas no resultado que produzem.

## Por que é fácil confundir

O sistema de [[wiki/concepts/pattern-recognition|reconhecimento de padrões]] humano detecta repetições, mas não avalia automaticamente se são boas. Uma coisa muito repetida pode ser um anti-pattern amplamente adotado. "Todo mundo faz assim" não é evidência de que é correto.

## Exemplos catalogados no wiki

Família das "massas" de código: [[wiki/concepts/code-espaguete|espaguete]] (fluxo de controle convoluto), [[wiki/concepts/lasagna-code|lasagna]] (camadas entrelaçadas), [[wiki/concepts/ravioli-code|ravioli]] (fragmentação excessiva) e, no nível arquitetural, [[wiki/concepts/big-ball-of-mud|Big Ball of Mud]]. Também [[wiki/concepts/god-object|God Object]]. Todos ilustram a tese central: são repetições *comuns* — a Big Ball of Mud é descrita como o estado *default* na prática — mas produzem mau resultado.

## Key Sources

- [[wiki/sources/akita-como-aprender-programacao]] — mencionado em contraposição a patterns válidos; alerta contra confundir frequência com qualidade
- [[wiki/sources/codigo-espaguete-wikipedia]] — catálogo de anti-padrões de código (espaguete, lasagna, ravioli, Big Ball of Mud)
