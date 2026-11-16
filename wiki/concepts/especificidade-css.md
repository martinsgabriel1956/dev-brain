---
type: concept
title: "Especificidade no CSS"
aliases: ["especificidade", "CSS specificity", "specificity"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [css, cascata, seletores, especificidade, frontend]
skill: tech-mentor-frontend
status: stub
---

# Especificidade no CSS

Peso que o navegador dá a um seletor para decidir qual regra vence quando várias se aplicam ao mesmo elemento e à mesma propriedade. É um dos critérios da cascata do [[wiki/concepts/css]], depois da origem e do `!important` e antes da ordem no arquivo. `[external]` https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity

O peso se conta em três colunas, comparadas da esquerda para a direita:

| Coluna | Conta | Exemplo |
|---|---|---|
| ID | seletores `#id` | `#btn-checkout` → (1,0,0) |
| Classe | `.classe`, atributos, pseudo-classes | `.btn.btn-primary` → (0,2,0) |
| Tipo | tags e pseudo-elementos | `a` → (0,0,1) |

O universal `*` vale (0,0,0). Por isso o reset `* { margin: 0 }` perde para qualquer outra regra.

## Na aula de classes e IDs

[[wiki/sources/classes-e-ids-no-css]] não fala de especificidade: estiliza o botão de checkout pelo ID, e ID e classe aparecem como equivalentes para estilo. A consequência que a aula não mostra: se o checkout também tivesse `class="btn btn-primary"`, as cores do `#btn-checkout` venceriam as das classes, seja qual for a ordem no arquivo. Inferência do agente com base na regra acima.

`[skill: tech-mentor-frontend]` O ITCSS organiza o CSS por especificidade crescente (settings → reset → elements → objects → components → utilities), e BEM mantém tudo numa classe só para a especificidade ficar plana. Ver [[wiki/concepts/seletores-css]].

## Key Sources

- [[wiki/sources/classes-e-ids-no-css]]: estilo por ID sem tratar de especificidade (tensão registrada na fonte)
