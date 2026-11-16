---
type: concept
title: "Especificidade no CSS"
aliases: ["especificidade", "CSS specificity", "specificity"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 6
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

## "A classe está em uma hierarquia maior que o seletor"

Em [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]], `a { background-color: red }` perde para `.nav-link { background-color: #FFF }` no link com a classe, e tirar a classe devolve o estilo de `a`. [[wiki/entities/nasser|Násser]] resume: "a classe está em uma hierarquia maior que o seletor". É especificidade (0,1,0 contra 0,0,1), embora a classe também seja seletor e a aula não use o termo.

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], [[wiki/entities/mayk-brito|Mayk]] ensina a ordem certa ("o seletor de hashtag é o seletor mais forte", depois classe, depois tag) e mostra `#page-landing` vencendo `.body h1`. Mas chama de "força de cascata" o que é soma de especificidade: `.body #page-landing` (1,1,0) vence `#page-landing` (1,0,0). E o `h1 { color: green }` que vence o vermelho do body não ganha por força, e sim porque o valor do pai era só herdado (ver [[wiki/concepts/heranca-css]]).

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], um `margin-top: 0` riscado no DevTools perde para um seletor mais longo ("uma profundidade de cascata muito mais forte"). `!important` resolve, mas Mayk o desaconselha: "você fica por tempos procurando por que não está aplicando algum CSS". Ele copia o seletor específico e o restringe a `#schedule-items`. `!important` não é especificidade maior: é outra etapa da cascata.

## Aninhamento soma especificidade (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-nesting-aninhamento-sass]], o slide diz que o nesting "pode emendar n cascatas". `[skill: tech-mentor-frontend]` Cada nível entra no seletor final: `.list li a:hover` = (0,2,2), contra (0,2,0) de um `.list__link:hover`. Quanto mais fundo, mais difícil sobrescrever depois; regra comum: até três níveis.

## Key Sources

- [[wiki/sources/classes-e-ids-no-css]]: estilo por ID sem tratar de especificidade (tensão registrada na fonte)
- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: classe vence seletor de tag ("hierarquia maior")
- [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]]: `*` como base, classes e IDs "com importâncias diferentes" por cima; o universal tem especificidade zero
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: id > classe > tag; "força de cascata" é especificidade
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: !important e a alternativa por seletor
- [[wiki/sources/frontpush-nesting-aninhamento-sass]]: Sass aula 05: especificidade de seletores aninhados
