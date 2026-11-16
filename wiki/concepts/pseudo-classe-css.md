---
type: concept
title: "Pseudo-classe CSS"
aliases: ["pseudo-classe", "pseudo-class", "pseudo-classes CSS", ":hover", ":focus", ":checked", ":nth-child", ":root"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 12
tags: [css, frontend, seletores-css, pseudo-classe, estados, formularios]
skill: tech-mentor-frontend
status: draft
---

# Pseudo-classe CSS

Palavra-chave com **um dois-pontos** que se junta a um [[wiki/concepts/seletores-css|seletor]] para pegar elementos por **estado** (o mouse em cima, marcado, em foco) ou por **posição** na árvore (primeiro filho, linha par), sem classe extra no HTML. `[external]` https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes

A aula [[wiki/sources/seletores-e-pseudo-elements-css]] as apresenta todas como "pseudo-elements"; a wiki separa: ver [[wiki/concepts/pseudo-elemento-css]].

## Grupos da aula

- **Interação:** `:hover` ("o efeito que eu mais utilizo"), `:active`, `:focus`, `:visited`.
- **Formulário:** `:checked` (radio e checkbox), `:disabled`, `:enabled`, `:in-range`, `:out-of-range`, `:valid`, `:invalid`. "Muito importante para [...] aprender a fazer o estilo de formulários."
- **Estrutura:** `:first-child`, `:last-child`, `:only-child`, `:first-of-type`, `:last-of-type`, `:nth-child(even | odd | n)`, `:nth-last-child(n)`, `:empty`.
- **Lógica:** `:not(p)` (só no slide).
- **Documento:** `:root`, onde se declaram as variáveis.

`[external]` `even` = pares, `odd` = ímpares (a aula hesita). `:first-child` é relativo ao pai: `p:first-child` é o `p` que é o primeiro filho, não o primeiro filho de um `p`. `:root` casa com `<html>`; custom properties declaradas ali valem na página toda ([[wiki/concepts/design-tokens]]).

## `:checked` como estado sem JavaScript

Násser usa `:checked` num hack de menu hambúrguer animado: um checkbox escondido guarda o estado aberto/fechado e o CSS reage a ele ([[wiki/sources/seletores-e-pseudo-elements-css]]). `[external]` O padrão funciona, mas o checkbox precisa de label e de teclado acessíveis; hoje `:has()` permite estilizar o pai a partir do estado do filho.

## Estados de design viram pseudo-classes

Os estados do [[wiki/concepts/style-guide]] (normal, hover, focus, disabled) chegam ao código como pseudo-classes; a aula de style guide chamava hover de pseudo-element ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]). Ver [[wiki/concepts/maquina-de-estados-ui]], [[wiki/concepts/affordance]] e [[wiki/concepts/botoes-em-interfaces]].

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa `a:hover` para escurecer o botão (`#34CB79` → `#2FB86E`) e `transition: 400ms` no `a` para a troca ficar "mais suave".

## Na NLW #1, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] percebe que `transition: 400ms` sem propriedade anima "tudo que aceita a transição" (o botão piscou no reload) e passa a escrever `transition: background-color 400ms`. "Não são todas as propriedades CSS que aceitam transição."

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], `:hover` muda o fundo dos botões com `transition` e a opacidade do link de voltar; `:focus-within` no `.input-block` reage ao foco do input que está dentro dele (ver [[wiki/concepts/indicador-de-foco]]).

## Estados no Sass (FrontPUSH)

Em [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]], "estados" entram na lista de vantagens do Sass; `[external]` no SCSS, `&:hover` dentro do bloco do botão gera `.botao:hover`.

## :hover com variável (FrontPUSH, Sass aula 04)

Em [[wiki/sources/frontpush-variaveis-sass]], o `:hover` do `.link` recebe `box-shadow: $box-shadow-purple`. O realce deveria valer também em `:focus-visible`, para teclado.

## &:hover (FrontPUSH, Sass aula 05)

Em [[wiki/sources/frontpush-nesting-aninhamento-sass]], o hover do link aninhado precisa de `&:hover`; sem o `&`, o Sass gera `a :hover` (com espaço), que mira os descendentes do `a`. Para o link da página atual, `.active`; `[external]` melhor junto com `aria-current="page"`.

## Na NLW #2, dia 1 (Diego Fernandes)

`:focus-within` no `.input-block` "vai verificar se dentro desse input block existe um input que tenha focus". Diego primeiro chamou de pseudo-elemento e corrigiu. Também `:hover`, `:first-child` e o irmão adjacente `.input-block + .input-block`. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Key sources

- [[wiki/sources/seletores-e-pseudo-elements-css]] — lista do W3Schools: checked, disabled, focus, hover, nth-child, root
- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]] — `card-hover` e estados de input no style guide
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: `:hover` + `transition` no botão
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: transition com propriedade explícita
- [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]]: `li:nth-child(1)`, `first-child`, `last-child`, pares e ímpares; dúvida "do li ou dele?" (é o `li` que é primeiro filho do pai)
- [[wiki/sources/frontpush-box-model-margin-padding-display-unidades]]: `.item:nth-child(1)` para dar `margin-top` só à primeira caixa
- [[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]]: `button:hover` (chamado de "pseudo-element" na aula) com `transform: scale` e `transition`
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: hover nos botões; focus-within
- [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]]: introdução ao Sass: estados como vantagem
- [[wiki/sources/frontpush-variaveis-sass]]: Sass aula 04: hover com sombra em variável
- [[wiki/sources/frontpush-nesting-aninhamento-sass]]: Sass aula 05: `&:hover`
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: :focus-within, :hover, :first-child
