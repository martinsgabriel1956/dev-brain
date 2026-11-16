---
type: concept
title: "Style guide (guia de estilo)"
aliases: ["guia de estilo", "styleguide", "style guide de UI", "guia de estilo de interface"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, style-guide, design-system, documentacao, handoff, design-tokens]
skill: ux-ui-mentor
status: stub
---

# Style guide (guia de estilo)

Documento que padroniza o estilo de um produto e o entrega ao time de desenvolvimento. Cobre duas coisas: o **design** (cores, tipografia, cards, border-radius, marca, elementos de composição) e o **comportamento** (telas, especificações, guia de interação, flow, jornada) ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]).

## Onde fica no processo

No curso de [[wiki/entities/nasser|Násser]], vem depois de pesquisa, [[wiki/concepts/wireframe]] e [[wiki/concepts/grid-de-colunas|grids]], no protótipo final. É o momento de "passar o bastão" para o dev, por isso carrega "documentação, entrega, colaboração, comunicação".

## O que entra

Depende do **level de complexidade** do projeto e do tamanho do time. A lista da aula:

- Versão light e dark
- Paleta de cores, com os hexadecimais prontos para Sass ou variáveis CSS
- [[wiki/concepts/tipografia]] de h1 a span, desktop x mobile
- [[wiki/concepts/familia-de-icones|Família de ícones]] ou ícones próprios para download
- Cards e [[wiki/concepts/botoes-em-interfaces|botões]] com estados (normal, hover, selecionado) e a transição entre eles
- Inputs com hover, focus, erro, warning e sucesso ([[wiki/concepts/feedback-do-sistema]])
- [[wiki/concepts/elementos-de-composicao]]
- Animações e comportamento, com nota, descrição e link de apoio

Regra para decidir: "se coloque no papel do desenvolvedor. Se você perceber que ele precisa, documente!". O dev pode não abrir o [[wiki/entities/figma]], então tudo precisa estar escrito, até num PDF.

## Documento vivo

Não esperar ficar perfeito: compartilhar o arquivo do Figma por link e evoluí-lo; quem tem o link recebe as mudanças. É a mesma ideia de [[wiki/concepts/living-documentation]], aplicada a design.

## Nomes que o dev entende

Labels iguais às do código (`card-hover`, `$orange`) reduzem tradução entre design e dev. Ver [[wiki/concepts/design-tokens]].

## Style guide x design system

`[skill: ux-ui-mentor]` A skill define design system como "acordo compartilhado entre design e dev", em camadas: design tokens, componentes base, componentes compostos, patterns e guidelines. O style guide da aula cobre os tokens (cor, tipografia, sombra), os estados de componentes e parte das guidelines de comportamento. Falta o que a skill põe num componente bem documentado: variantes com regra de uso, estados completos (focus, active, disabled, loading) e acessibilidade. `[external]` Um "style guide" costuma ser a parte visual e de marca de um design system, que também inclui a biblioteca de componentes e a documentação de uso (https://www.nngroup.com/articles/design-systems-101/).

## Key Sources

- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]: definição, levels de complexidade, lista de padronização, evolução por link, inspect, labels
