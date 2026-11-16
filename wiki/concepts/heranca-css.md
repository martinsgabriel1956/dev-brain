---
type: concept
title: "Herança no CSS"
aliases: ["herança", "inheritance", "CSS inheritance", "inherit", "propriedade herdada"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [css, heranca, cascata, especificidade, frontend]
skill: tech-mentor-frontend
status: stub
---

# Herança no CSS

Algumas propriedades passam do elemento pai para os filhos quando o filho não declara um valor próprio. Herdam por padrão as de texto (`color`, `font-*`, `line-height`, `text-align`, `visibility`); não herdam as de caixa (`margin`, `padding`, `border`, `width`, `background`). `inherit` força a herança de qualquer propriedade, e `initial` e `unset` desfazem. `[external]` https://developer.mozilla.org/en-US/docs/Web/CSS/Inheritance

Um valor herdado não tem especificidade: qualquer regra que mire o filho, até um seletor de tag, vence a cor que veio do pai, mesmo que o pai tenha sido estilizado por id. Herança e [[wiki/concepts/especificidade-css|especificidade]] são etapas diferentes da [[wiki/concepts/cascata-css|cascata]]: a especificidade escolhe entre declarações para o mesmo elemento; a herança só entra quando não há nenhuma.

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], [[wiki/entities/mayk-brito|Mayk]] mostra a herança sem usar o nome. `#page-landing { color: red }` no body pinta `h1`, `p` e `img`, porque "eu estou aplicando ao pai", e o estilo "pode ou não se propagar para todos os elementos dentro dele". Depois `h1 { color: green }` vence o vermelho "não importa o posicionamento", o que ele atribui à "força" do seletor; o motivo é que o `h1` não tinha cor declarada, só herdada.

Duas exceções aparecem na mesma aula. O `button` não fica vermelho ("tem uma força diferente") e não pega a Poppins do body ("nem cor, nem fonte"), o que obriga a regra `body, input, button, textarea`. O motivo é a folha do navegador, que dá cor e fonte próprias aos controles de formulário (ver [[wiki/concepts/estilos-padrao-do-navegador-e-reset]]). `[skill: tech-mentor-frontend]` O reset usual põe `font: inherit` em `button, input, select, textarea`.

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], duas falas tratam como herança o que não é: a imagem centralizada pelo `text-align` (ela é inline) e a hero image que "vai herdar a largura do pai" com `width: 100%` (porcentagem calculada contra o bloco que contém).

## Key sources

- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: cor do body propagada aos filhos; filho com regra própria vence; botão que não herda cor nem fonte
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: text-align e width 100% não são herança
