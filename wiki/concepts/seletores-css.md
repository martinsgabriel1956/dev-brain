---
type: concept
title: "Seletores CSS"
aliases: [seletor CSS, seletores, classe e ID, class e id, seletor de classe, seletor de ID, seletor universal, CSS selectors, combinadores CSS, seletor descendente, seletor filho, seletor adjacente, seletor de atributo]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 6
tags: [css, html, seletores, classe, id, frontend, seletores-css, combinadores]
skill: tech-mentor-frontend
status: draft
---

# Seletores CSS

A parte da regra [[wiki/concepts/css|CSS]] que diz **a quais elementos** as declarações se aplicam. Seletores andam pela árvore do [[wiki/concepts/dom]] (pai, filho, irmão), por isso bem usados evitam criar uma classe "só por causa de um elemento" ([[wiki/sources/seletores-e-pseudo-elements-css]]).

## Os quatro básicos

| Seletor | Sintaxe | Alcança | Exemplo da aula |
|---|---|---|---|
| Universal | `*` | todo elemento | reset de margin, padding e `box-sizing: border-box` |
| Tipo (tag) | `h1`, `a`, `p` | toda tag daquele tipo | h1 branco, parágrafo `#333` |
| Classe | `.btn` | todo elemento com `class="btn"` | botões primário e secundário |
| ID | `#btn-checkout` | o elemento com `id="btn-checkout"` (único) | botão de checkout maior e azul |

Fonte: [[wiki/sources/classes-e-ids-no-css]].

## Combinadores e atributos

| Seletor | Exemplo | Pega |
|---|---|---|
| Elemento + classe | `p.intro` | só os `p` com a classe |
| Agrupamento (vírgula) | `h1, p` | cada um da lista, mesmo estilo |
| Descendente (espaço) | `div p` | `p` em qualquer nível dentro de `div` |
| Filho (`>`) | `div > p` | só `p` filho direto de `div` |
| Adjacente (`+`) | `ul + p` | o `p` logo depois de um `ul`, mesmo pai |
| Atributo | `[id=my-Address]`, `input[type="text"]` | pelo valor de um atributo; base para formulários |

Fonte: [[wiki/sources/seletores-e-pseudo-elements-css]], percorrendo o Try CSS Selector do [[wiki/entities/w3schools]] (a aula também passa por tipo, classe `.intro`, ID `#Lastname` e universal). `[external]` Falta na aula o irmão geral (`~`): `p ~ ul` pega todo `ul` que vem depois de um `p` no mesmo pai.

Estados e posições (`:hover`, `:nth-child`) ficam em [[wiki/concepts/pseudo-classe-css]]; partes do elemento (`::first-letter`) em [[wiki/concepts/pseudo-elemento-css]].

## Classe x ID

Em [[wiki/sources/classes-e-ids-no-css]], [[wiki/entities/nasser|Násser]] define os dois como "ganchos" usados no CSS e no JavaScript ([[wiki/concepts/dom]]), que "funcionam de uma mesma forma" e diferem na semântica:

- **ID** identifica um elemento só, "como se fosse o seu CPF". Repetir "vai dar conflito", mas o navegador não avisa.
- **Classe** vale para vários elementos: crie uma quando o estilo se repete. Um elemento pode ter várias, separadas por espaço (`class="btn btn-primary"`).

`[external]` `class` e `id` são atributos globais do HTML (a aula diz "tags"). `class` é uma lista separada por espaços e sensível a maiúsculas; `id` precisa ser único no documento: https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id.

## Quantas classes usar

As duas aulas puxam para lados diferentes:

- [[wiki/sources/classes-e-ids-no-css]]: crie uma classe quando o estilo se repete; o ID tem [[wiki/concepts/especificidade-css|especificidade]] alta (uma regra por ID vence qualquer número de classes), então estilize por classe.
- [[wiki/sources/seletores-e-pseudo-elements-css]]: use seletores para ter "a menor quantidade de classes possíveis".

`[skill: tech-mentor-frontend]` Em CSS global grande, BEM (`.card__title--truncated`) e ITCSS estilizam só por classe, com especificidade baixa e plana, e deixam o ID para âncoras, `label for` e JavaScript; `@layer` decide a precedência entre camadas, independente da especificidade do seletor. A ordem da aula de classes (reset `*` → tags → classes) é a mesma das camadas Generic → Elements → Components do ITCSS. Seletores longos que copiam a estrutura do HTML quebram quando ela muda. Inferência do agente: combinadores e pseudo-classes rendem mais em padrões estruturais (zebra de tabela, estados de formulário) do que em componentes.

`[external]` Especificidade: ID > classe/atributo/pseudo-classe > tipo/pseudo-elemento; o universal e os combinadores não somam: https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity.

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa seletor de tag, de classe ("pontinho é a referência para uma classe"), de id (`#page-home`), descendente (`#page-home header a span`, conferido pelo hover do VS Code), universal `*` ("um atalho para todos"), agrupado `h1, h2, h3...` e `:root`. Class "eu posso repeti-lo em diversos elementos"; id "não pode ser repetido".

## Na NLW #1, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa o combinador de irmão adjacente: `.field-group .field + .field` pega só o campo "que vier seguido de um field", para dar `margin-left` ao segundo. Também agrupa com vírgula (`form input, form select`) para dividir regras.

## Tag, classe e ID no módulo de front-end do FrontPUSH

Em [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]], [[wiki/entities/nasser|Násser]] mostra os "seletores padrões": de tag (`header`, `nav`), de classe (`.nav`, `.nav-link`) e de ID (`#nav-menu`). Trocar `header` e `nav` por `div` faz o CSS "perder a referência", e é aí "que vem a class e o id". A classe serve também ao JavaScript, "para poder eu elencar ali e puxar e manipular esses elementos". Mesma divisão de [[wiki/sources/classes-e-ids-no-css]], com outra demonstração.

## No módulo de front-end do FrontPUSH (aula 04)

Em [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]], [[wiki/entities/nasser|Násser]] mostra na prática: `section > p` (filho direto, "não é neto, ele não é tataraneto") x `section p` (qualquer nível); `p + span` (só o `span` logo depois de um `p`); `*` para "generalizar, aplicar tudo e depois só [...] fazer tratamentos pequenos" com classes; `input[type="text"]`; `h1, h2, h3` como forma "mais compressa" de repetir a regra. Selecionar no CSS "é muito similar ou deveras igual" ao JavaScript (`querySelector` usa os mesmos seletores). O irmão geral `~` continua de fora.

## Key sources

- [[wiki/sources/classes-e-ids-no-css]] — classe x ID (CPF), `#` e `.`, reset universal, estilos por tag, `.btn` com variações, ID de checkout
- [[wiki/sources/seletores-e-pseudo-elements-css]] — tour pelo W3Schools: classe, ID, vírgula, descendente, filho, adjacente, universal, atributo
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: seis tipos de seletor no Ecoleta
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: irmão adjacente `+`; vírgula em input e select
- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: tag, classe e ID; trocar tags por div quebra o seletor de tag
- [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]]: filho direto x descendente, `+`, `*`, atributo e vírgula na prática
