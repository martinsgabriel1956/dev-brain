---
type: source
title: "@mixin e @content no Sass: mixin de responsividade (FrontPUSH)"
aliases: ["Propriedades @mixin & @content", "mixin Sass FrontPUSH", "módulo de CSS Sass, aula 06", "mixin responsive"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, sass, scss, mixin, content, include, media-query, responsividade, tipografia, breakpoint, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-mixin-e-content-sass.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-16
---

# @mixin e @content no Sass (FrontPUSH)

## TL;DR

Aula 06 do módulo de CSS Sass do [[wiki/entities/frontpush|FrontPUSH]] (instrutor inferido: [[wiki/entities/nasser|Násser]]). Assunto: [[wiki/concepts/mixin-sass]].

- **Mixin:** "entenda mixin como se fosse uma função", com ou sem argumentos e com valor padrão. Serve para reaproveitar código, montar bibliotecas, pôr prefixos e fazer responsividade.
- **Slide:** `@mixin nome_mixin($cor: #FAFAFA) { font-size: 36px; color: $cor; @content; }` e `h1 { @include nome_mixin(#FFF) { line-height: 110%; } }` → `h1` com 36 px, `#FFF` e `line-height` 110%.
- **`@content`:** "o que ele colocar dentro [...] vai aparecer aqui, é meio que um copia e cola".
- **Demo:** `h1` de 72 px e parágrafo de 24 px. Em CSS puro, uma media query `max-width: 960px` no fim do arquivo reduz para 48 e 16; o problema é ficar "em dois lugares diferentes". Com `@mixin responsive { font-variant: small-caps; @media screen and (max-width: 960px) { @content; } }`, o `h1` faz `@include responsive { font-size: 48px; }` dentro da própria regra. Depois, `responsive-tablet` (960) e `responsive-mobile` (720, 36 px). Ver [[wiki/concepts/design-responsivo]] e [[wiki/concepts/breakpoint]].
- Ele usa o mesmo padrão no projeto do [[wiki/entities/nubank]], "vinculado a estruturas encadeadas de ifs".

## Key Claims

### O que é

- "Com esse recurso de mixin, eu tenho a capacidade de criar funções pré-definidas ou até com argumentos [...] um trecho de código que eu posso personalizar ou então pré-definir para poder utilizar em vários outros projetos e criar bibliotecas."
- Slide: "criação de funções pré-definidas", "aproveitamento de código", "criação de sistemas mais completos", "facilidade para adicionar prefixos", "facilita na criação de função de responsividade".
- "Você vai abrir com arroba mixin, aqui é o nome do seu mixin [...] Aqui você pode, ou não, passar argumentos. [...] o argumento de cor com um default de cor FA, FA, FA."
- `@include` "o nome do mixin, com a cor que eu quero, e [...] o conteúdo que eu coloquei aqui dentro, que é o content, ele vai ser carregado para cá automaticamente".

### Responsividade em CSS puro

- "Se eu fosse diminuindo essa tela [...] e chegasse à tela de um celular [...] o tamanho desse título e desse texto [...] está grande demais [...] adeque o tamanho da tipografia ao tamanho da tela. Então, isso é um básico de UI Design alinhado à responsividade" ([[wiki/concepts/escala-tipografica]]).
- `@media screen and (max-width: 720px)` = "quando o tamanho da tela for menor ou igual a 720 pixels". Teste com fundo vermelho; troca para 960.
- O incômodo: "quando você tem um trecho muito grande de código, você precisa sempre ver: 'eu coloquei quanto no modo de tela desktop?', e depois você tem que descer novamente [...] fica um pouco desconexo."

### Mixin responsive

- `responsive` no começo do arquivo, com a media query de 960 px e `@content` dentro.
- Parte fixa × variável: "se eu colocar fixo, eu posso colocar alguma característica aqui fora, então colocar font-variant small caps [...] quando eu quero uma função mais variável [...] eu coloco um content."
- `@include responsive` sem bloco só aplica o fixo: "a minha tipografia ficou com o small caps, mas ela continua sem ficar responsiva".
- Com bloco: "ele já vai carregar dentro do media query [...] aqui fora eu aplico para desktop, e aqui dentro eu aplico para dispositivos tablets ou mobile."
- Dois mixins, `responsive-tablet` (960) e `responsive-mobile` (720): o `h1` vai de 72 para 48 e depois 36; o parágrafo, de 24 para 18 e 16; no mobile, o parágrafo também muda de cor.
- Outras partes fixas: `text-transform: capitalize` ou `uppercase`; um mixin `title` com uppercase, small caps e peso maior.
- "Esse aqui é um recurso importantíssimo que eu uso para a responsividade dos meus projetos, vinculado a estruturas encadeadas de ifs, para deixar isso aqui ainda mais elástico."

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/frontpush]]: curso; aula 06 do módulo de CSS Sass.
- [[wiki/entities/nubank]]: projeto onde o mixin de responsividade já foi usado.

## Concepts

- [[wiki/concepts/mixin-sass]]
- [[wiki/concepts/pre-processador-css]]
- [[wiki/concepts/variaveis-sass]]
- [[wiki/concepts/aninhamento-css]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/breakpoint]]
- [[wiki/concepts/mobile-first]]
- [[wiki/concepts/escala-tipografica]]
- [[wiki/concepts/unidades-de-medida-css]]
- [[wiki/concepts/prefixo-de-fornecedor]]
- [[wiki/concepts/cascata-css]]
- [[wiki/concepts/dry]]

## Precisões e tensões com a wiki

- **Mixin não devolve nada.** A frase "colocar argumentos e ele devolve alguma resposta" é de `@function`, que tem `@return` e devolve um valor. O mixin despeja declarações e regras no lugar do `@include`. Já anotado na [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss|aula 01]].
- **Um mixin com parâmetro no lugar de dois.** `[skill: tech-mentor-frontend]` Em vez de `responsive-tablet` e `responsive-mobile` copiados, o usual é um mapa de breakpoints e um mixin só: `$bps: (tablet: 960px, mobile: 720px); @mixin bp($nome) { @media (max-width: map.get($bps, $nome)) { @content; } }`. Ver [[wiki/concepts/mixin-sass]].
- **A ordem dos dois includes importa.** Abaixo de 720 px, as duas media queries valem ao mesmo tempo, e a especificidade é a mesma; vence a que vem depois no CSS gerado. O `responsive-mobile` precisa ficar depois do `responsive-tablet` ([[wiki/concepts/cascata-css]]). Funcionou na demo porque ele escreveu nessa ordem.
- **Desktop-first.** `max-width` diminui a partir do desktop, o mesmo padrão das aulas de Flexbox e Grid do curso, oposto ao [[wiki/concepts/mobile-first]] da NLW #2 (`min-width`).
- **Sass gera uma media query por `@include`.** O CSS final repete `@media (max-width: 960px)` em cada seletor que usou o mixin. Funciona, e o gzip absorve a repetição.
- **O CSS nativo já faz isso sem mixin.** `[skill: tech-mentor-frontend]` Com o aninhamento nativo, `h1 { font-size: 72px; @media (width <= 960px) { font-size: 48px; } }` funciona nos navegadores atuais, e a sintaxe de intervalo (`width <= 960px`) dispensa o `screen and` ([[wiki/concepts/aninhamento-css]]).
- **Tipografia fluida.** `[external]` `font-size: clamp(2.25rem, 1.5rem + 3vw, 4.5rem)` escala o título continuamente, sem degraus em 960 e 720 (https://developer.mozilla.org/en-US/docs/Web/CSS/clamp). Em `rem`, e não em `px`, respeita o tamanho de fonte que o usuário escolheu no navegador ([[wiki/concepts/unidades-de-medida-css]], [[wiki/concepts/escala-tipografica]]).
- **Mixin de prefixo é coisa do passado.** Prefixos ficam com o Autoprefixer ([[wiki/concepts/prefixo-de-fornecedor]]).
- **"Estruturas encadeadas de ifs"** promete `@if`/`@else` dentro de mixins; ainda não aparece no curso ingerido.

## Open Questions

- "No mobile um dia menor": "um bem menor"? Mantido.
- "Text transform capitalized": o valor CSS é `capitalize`; não dá para saber o que foi digitado.
- O mixin `responsive` original ficou com o `small-caps` depois de virar `responsive-tablet`?

## Raw quotes

- "entenda mixin como se fosse uma função de fato, mas aqui o nome é mixin"
- "por ser em dois lugares diferentes, fica um pouco desconexo"
- "aqui fora eu aplico para desktop, e aqui dentro eu aplico para dispositivos tablets ou mobile"
