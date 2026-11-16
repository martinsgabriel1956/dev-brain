---
type: source
title: "A propriedade @import e os partials no Sass (FrontPUSH)"
aliases: ["Propriedade @import", "FrontPUSH @import Sass", "módulo de CSS Sass, aula 03", "partials Sass FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, sass, scss, import, partials, variaveis, organizacao, http, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-import-e-partials-sass.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-16
---

# A propriedade @import e os partials no Sass (FrontPUSH)

## TL;DR

Aula 03 do módulo de CSS Sass do [[wiki/entities/frontpush|FrontPUSH]] e primeira dos "fundamentos do Sass" (instrutor inferido: [[wiki/entities/nasser|Násser]]). Assunto: [[wiki/concepts/import-e-partials-sass]].

- **`@import`** traz um arquivo Sass para dentro de outro, e tudo compila "em um arquivo só". Os recursos do Sass "sempre começa[m] com um arroba".
- **Vantagens (slide):** organização por categoria (cores, tipografia, layout, botões), "mais ou menos o conceito de componentes"; menos requisições, porque sai um CSS só ([[wiki/concepts/pipeline-de-assets]]).
- **A ordem importa:** um mixin definido em `layout.scss` tem de ser importado antes do arquivo que o usa; senão, erro.
- **Demo:** `colors.scss` com variáveis `branco` (`#fff`), `cinza` e `preto` (`#0c0c0c`), importado no topo do `style.scss`; o `h1` e o `span` aninhado usam as variáveis ([[wiki/concepts/variaveis-css]], [[wiki/concepts/aninhamento-css]]).
- **Partials:** o `colors.scss` também virou `colors.css` + `.map`. Renomeado para `_colors.scss` ("o underline no começo do arquivo"), não gera mais CSS próprio; `@import "colors"` sem underline e sem extensão.

## Key Claims

### O que é

- "Como o próprio nome sugere, ele possibilita você importar arquivo Sass dentro de outros arquivos Sass e compilar isso tudo em um arquivo só."
- Slide: "@import 'colors.scss'; @import 'typography.scss'" e, como partials, "@import '_layout.scss'", "@import '_buttons.scss'".

### Organização e requisições

- "Você pode criar um arquivo só de cores, outro só de tipografia, outro só de layout, outro só de botões", para não se perder "naquele arquivo gigantesco que ficaria de CSS". Ver [[wiki/concepts/componentizacao]].
- "Ele vai compilar isso tudo em um arquivo só, que é a maneira mais otimizada de você colocar o CSS nos seus websites quando estiverem em produção, porque tem menos arquivos para carregar."
- "Se eu vincular vários arquivos em CSS, prejudica a otimização do website, porque vai ter vários requests de arquivo CSS."

### A ordem importa

- "Lembre-se que o CSS lê linha a linha. Então, se tem um arquivo que você definiu um mixin [...] em layout.scss, e você declarou ele depois de tipografia, onde você utiliza essa função aqui, ele vai dar erro."
- "Ele está meio que pegando esse trecho, copiando, colando bem aqui onde está o import, por isso que a ordem importa."

### Demonstração

- Base: `margin: 0`, `box-sizing: border-box`, `body` com 100%, fundo `#0c0c0c`, flex centralizado; `h1` branco ([[wiki/concepts/estilos-padrao-do-navegador-e-reset]], [[wiki/concepts/flexbox]]).
- `colors.scss` no mesmo diretório; numa subpasta, "colocar o caminho dela".
- Nomes de variável: ele começou com `gray` e corrigiu para `cinza`: "até misturei em inglês com português, então não é legal". Cinza ajustado de `#ccc` para `#555` e depois `#444`.
- `span` dentro do `h1`, aninhado no SCSS; o CSS gerado sai como seletor descendente ([[wiki/concepts/seletores-css]]). "No Sass ele fica mais organizado, porque tem essa seção de hierarquia."

### Partials

- "Foi também gerado um colors e um colors.css.map, e isso aqui não é muito interessante. O legal é eu gerar apenas esse arquivo CSS."
- "Quando você coloca esse underline no começo do arquivo, você já está dizendo para o Sass o seguinte: 'apenas copie e cole o Sass, mas gere apenas um arquivo final'."
- "Posso simplesmente fazer um import colors, não necessariamente aqui eu preciso colocar .scss, que já vai funcionar."

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/frontpush]]: curso; aula 03 do módulo de CSS Sass.
- [[wiki/entities/live-sass-compiler]]: o compilador da demo; gerou `colors.css` e `.map` até o arquivo virar partial.

## Concepts

- [[wiki/concepts/import-e-partials-sass]]
- [[wiki/concepts/pre-processador-css]]
- [[wiki/concepts/mixin-sass]]
- [[wiki/concepts/variaveis-sass]]
- [[wiki/concepts/variaveis-css]]
- [[wiki/concepts/aninhamento-css]]
- [[wiki/concepts/seletores-css]]
- [[wiki/concepts/cascata-css]]
- [[wiki/concepts/pipeline-de-assets]]
- [[wiki/concepts/http2]]
- [[wiki/concepts/critical-rendering-path]]
- [[wiki/concepts/componentizacao]]
- [[wiki/concepts/estilos-padrao-do-navegador-e-reset]]
- [[wiki/concepts/flexbox]]

## Precisões e tensões com a wiki

- **`@import` do Sass está obsoleto.** `[external]` O Dart Sass 1.80 (outubro de 2024) passou a avisar que `@import` está deprecado, e a remoção está marcada para o Dart Sass 3.0. O substituto é o sistema de módulos: `@use "colors";` e depois `colors.$branco`, ou `@use "colors" as *;`, mais `@forward` para reexportar (https://sass-lang.com/documentation/breaking-changes/import/, https://sass-lang.com/documentation/at-rules/use/). Com `@use`, cada arquivo carrega uma vez só e as variáveis ficam com namespace, o que resolve dois problemas do `@import`: CSS duplicado e nomes globais que colidem. Na época da gravação (2021), `@import` ainda era o padrão ensinado.
- **"A ordem importa" é do Sass, não da cascata.** O erro com mixin fora de ordem é **de compilação**: o Sass lê de cima para baixo e não conhece o que ainda não foi definido. A frase "o CSS lê linha a linha" mistura isso com a [[wiki/concepts/cascata-css|cascata]], em que a ordem só desempata regras de mesma especificidade e nunca dá erro.
- **Variável do Sass leva `$`.** `[external]` `$branco: #fff;` e `color: $branco;`. A fala não cita o cifrão; o código precisa dele.
- **`@import "x.css"` não importa nada para o Sass.** `[external]` Se o caminho termina em `.css`, começa com `http://`, usa `url()` ou tem media query, o Sass deixa um `@import` de CSS puro no resultado, e o navegador faz outra requisição em série (https://sass-lang.com/documentation/at-rules/import/#plain-css-imports). Daí a importância de escrever `.scss` ou nada.
- **Um arquivo só é mais rápido?** `[skill: tech-mentor-frontend]` Era a regra no HTTP/1.1, com poucas conexões por domínio e cada arquivo custando ida e volta. No [[wiki/concepts/http2|HTTP/2]], a multiplexação barateia vários arquivos, e um CSS gigante também atrasa a primeira renderização, porque CSS bloqueia o render ([[wiki/concepts/critical-rendering-path]]). Hoje o comum é um CSS por página ou rota, com o crítico inline. Agrupar com o Sass continua bom; "um arquivo é sempre melhor" é que ficou datado. O pior caso, que a aula não cita, é o `@import` nativo do CSS: o navegador só descobre o segundo arquivo depois de baixar o primeiro.
- **Por que o `colors.css` apareceu.** Todo compilador de pasta (Live Sass Compiler, `sass --watch scss:css`) gera um CSS para cada `.scss` que não é partial. O underline é a convenção que diz "só serve para ser importado".
- **Hierarquia × especificidade.** O aninhamento deixa o SCSS legível, mas gera seletores mais específicos; ver [[wiki/concepts/aninhamento-css]].

## Open Questions

- "Vamos rodar o Sass aqui, olhei": "olha aí"? Mantido como está na legenda.
- "Se eu vir aqui e modificar, por exemplo, a red, essa cor": trocou uma cor para `red` na demo? A legenda não deixa claro.
- "Olha só como o meu style.css está sendo plotado" pode ser o `.scss` sendo editado ou o `.css` gerado; mantido como `.css`.

## Raw quotes

- "a ordem importa"
- "apenas copie e cole o Sass, mas gere apenas um arquivo final"
- "até misturei em inglês com português, então não é legal"
