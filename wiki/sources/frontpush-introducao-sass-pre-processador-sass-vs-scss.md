---
type: source
title: "Introdução ao Sass: o que é, vantagens, prefixos e Sass vs SCSS (FrontPUSH)"
aliases: ["Introdução SASS", "FrontPUSH introdução Sass", "Sass vs SCSS FrontPUSH", "módulo de CSS Sass, aula 01"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, sass, scss, pre-processador, mixin, variaveis, vendor-prefix, can-i-use, compatibilidade, aninhamento, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-introducao-sass-pre-processador-sass-vs-scss.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Introdução ao Sass (FrontPUSH)

## TL;DR

Aula 01 do módulo de CSS Sass do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] (ele se chama pelo nome duas vezes: "Násser, como assim...?"). O [[wiki/concepts/pre-processador-css|Sass]] é o mesmo usado nos projetos do [[wiki/entities/spider-man-projeto-nasser|Homem-Aranha]] e do [[wiki/entities/nubank]].

- **O que é:** um pré-processador que compila para CSS e traz "skills de linguagem de programação". Não faz "algo além do que o CSS já é capaz de fazer"; o navegador nunca lê Sass.
- **Pré-requisitos:** HTML, CSS e noção de programação (loop, `if/else`, variáveis, funções); JavaScript não é exigido. Ver [[wiki/concepts/logica-de-programacao]].
- **Vantagens (slide):** funções (que ele chama de mixins) para montar bibliotecas reaproveitáveis; variáveis com valores inteiros, como um `box-shadow` de várias camadas; facilidades com pseudo-elementos e estados; melhor compatibilidade entre navegadores.
- **Compatibilidade:** demonstra o Can I use com `transform` e os prefixos `-moz-`, `-ms-`, `-webkit-` e `-o-`; o CSS gerado do projeto já sai com `-webkit-` nos `@keyframes`. Ver [[wiki/concepts/prefixo-de-fornecedor]] e [[wiki/concepts/compatibilidade-entre-navegadores]].
- **Por que Sass:** há outros, como o Less, mas o Sass é o mais difundido e tem a maior comunidade.
- **Sass vs SCSS:** no [[wiki/entities/codepen]], a sintaxe indentada (sem chaves nem ponto e vírgula, "próximo da linguagem Python") é "prejudicial" porque afasta do CSS puro; o curso usa SCSS, "muitíssimo parecido com o CSS puro", com tags "uma dentro da outra" ([[wiki/concepts/aninhamento-css]]). "A tecnologia é maior que a ferramenta."
- **Próxima aula:** instalar o Sass no computador.

## Key Claims

### O que é e o que não é

- "O Sass é um pré-processador de CSS, significa que ele é simplesmente um programa que vai dar recursos para o nosso CSS, do que o CSS normal, padrão, uma linguagem de estilização não tem."
- "Não é que ele vai fazer algo além do que o CSS já é capaz de fazer, mas ele é um pré-processador que compila o CSS [...] o que melhora demais a nossa produtividade, a nossa organização no código."
- "O Sass não é lido pelo browser, isso não acontece, o browser sempre vai entender HTML, CSS e JavaScript. Ele nada mais é do que um meio de campo, que ele cospe já o arquivo CSS, só que otimizado."
- O slide resume: "dá um boost no CSS com skills de linguagem de programação. Mas não faz nada além que o CSS puro não faça!"; "Você vai ser capaz de construir suas próprias bibliotecas CSS e aproveitar em outros projetos".

### Módulo e pré-requisitos

- Os projetos do módulo são "projetinhos mais pontuais" para mostrar os recursos; a aplicação em projeto real fica nos práticos: "o Nubank é uma ótima vitrine [...] eu utilizo o Sass para poder melhorar a produtividade".
- Módulo "mais intermediário": "você não precisa, por exemplo, saber de fato JavaScript, mas você precisa saber o que é um loop, [...] uma estrutura encadeada if, else, como se declara variáveis, para que serve uma função".

### Vantagens

- **Funções / mixins:** "uma função sempre tem um caráter mais generalista, de forma que eu possa construir, por exemplo, bibliotecas, onde eu possa utilizar essas funções, que são chamadas mixins lá no Sass [...] eu tenho trabalho uma vez e eu consigo replicar isso em outros projetos".
- **Variáveis de propriedade inteira:** um `box-shadow` com várias camadas, usado no arquivo todo, muda num lugar só ([[wiki/concepts/sombra-em-interfaces]]). Para ele, "no CSS puro você só tem como criar variáveis com cores, com hexadecimais".
- **Pseudo-elementos e estados:** citados no slide e prometidos para depois ([[wiki/concepts/pseudo-elemento-css]], [[wiki/concepts/pseudo-classe-css]]).

### Can I use e prefixos

- O Can I use é um site "onde todo desenvolvedor web tem que sempre estar visitando": os navegadores demoram "a se alinhar com a tecnologia", então nem todo recurso novo é suportado em toda parte.
- Legenda: verde é suportado, vermelho não, verde escuro é parcial e cinza é desconhecido.
- Para `transform` ([[wiki/concepts/transition-e-transform-css]]): IE 6–8, 9, 10, 11; Edge "do 12 ao 16, 17, 88 e 89"; versões antigas de Firefox, IE e Safari pedem `-moz-`, `-ms-` e `-webkit-`. "Aceitação de 98% e sem prefixo de 96%."
- "Fica chato às vezes você digitar [...] o mesmo comando com o traço webkit, [...] moz, [...] ms, [...] o do Opera, e o Sass já adiciona isso aqui automaticamente no seu código."
- No projeto, o `.scss` gera um `.css` em que a animação `Flipcard` dos `@keyframes` aparece com `-webkit-` e sem prefixo; "você pode configurar isso para poder trazer mais compatibilidade".

### Sass vs SCSS

- "Aqui nos nossos arquivos, eles se chamam .SCSS e não .Sass. 'Então por que sempre, Násser, você fala Sass?'"
- Demo no CodePen: `section` com `h1` "hello world com Sass" e um `span`; `h1 span` estiliza só o span dentro do h1 ([[wiki/concepts/seletores-css]]).
- Sintaxe indentada: "eu simplesmente digito body, e aqui embaixo eu não preciso abrir e fechar chaves". "Próximo da linguagem Python, onde a própria indentação faz essa separação."
- "Essa sintaxe é prejudicial, porque, pelo fato dela ter simplificado muito, ela se distancia do CSS puro [...] Lembre-se que a tecnologia é maior que a ferramenta." Ver [[wiki/concepts/apego-a-ferramentas]].
- SCSS: "muitíssimo parecido com o CSS puro que a gente sempre conhece, adicionado de algumas skills". Aninhamento: "eu posso colocar as tags uma dentro da outra [...] melhora o meu entendimento do que está dentro de determinada tag".

## Entities

- [[wiki/entities/nasser]]: instrutor (nome dito na aula).
- [[wiki/entities/frontpush]]: curso; abertura do módulo de CSS Sass.
- [[wiki/entities/codepen]]: demonstração de Sass e SCSS.
- [[wiki/entities/nubank]]: projeto prático em que o Sass é usado de verdade.
- [[wiki/entities/spider-man-projeto-nasser]]: "o Homem-Aranha", outro projeto com Sass.
- [[wiki/entities/live-sass-compiler]]: extensão que gera o CSS com `-webkit-` (detalhada na [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app|aula 02]]).

## Concepts

- [[wiki/concepts/pre-processador-css]]
- [[wiki/concepts/prefixo-de-fornecedor]]
- [[wiki/concepts/aninhamento-css]]
- [[wiki/concepts/compatibilidade-entre-navegadores]]
- [[wiki/concepts/variaveis-css]]
- [[wiki/concepts/css]]
- [[wiki/concepts/transition-e-transform-css]]
- [[wiki/concepts/pseudo-elemento-css]]
- [[wiki/concepts/pseudo-classe-css]]
- [[wiki/concepts/seletores-css]]
- [[wiki/concepts/sombra-em-interfaces]]
- [[wiki/concepts/apego-a-ferramentas]]
- [[wiki/concepts/logica-de-programacao]]

## Precisões e tensões com a wiki

- **Quem põe o `-webkit-` não é o Sass.** `[external]` O compilador (Dart Sass) não acrescenta prefixos. Quem faz isso é o Autoprefixer (PostCSS), que lê os dados do Can I use e o alvo do `browserslist` (https://github.com/postcss/autoprefixer). A extensão Live Sass Compiler, usada no curso ([[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]), tem a opção `liveSassCompile.settings.autoprefix`, que roda o Autoprefixer depois de compilar (https://github.com/glenn2223/vscode-live-sass-compiler). É isso que explica o "você pode configurar isso". Confiança alta de que o prefixo veio da extensão; a aula não mostra a configuração.
- **Custom properties não são só cores.** `[external]` Uma variável CSS guarda qualquer sequência de tokens: `--sombra: 0 1px 2px #0003, 0 4px 8px #0002;` e depois `box-shadow: var(--sombra)` funciona (https://developer.mozilla.org/en-US/docs/Web/CSS/--*). A diferença real é outra: `$variável` do Sass some na compilação, custom property vive no navegador, herda e pode mudar em tempo de execução ([[wiki/concepts/variaveis-css]]).
- **Mixin não é função.** `[external]` No Sass, `@mixin` + `@include` despejam declarações no lugar; `@function` + `@return` devolvem um valor (https://sass-lang.com/documentation/at-rules/mixin/, https://sass-lang.com/documentation/at-rules/function/). A frase "ele sempre me retorna alguma coisa [...] que são chamadas mixins" mistura as duas.
- **O aninhamento já é CSS nativo.** `[skill: tech-mentor-frontend]` Nesting chegou ao Chrome 112, Firefox 117 e Safari 16.5 (2023). Na gravação, "não é permitido no CSS puro" era verdade; hoje não é mais ([[wiki/concepts/aninhamento-css]]).
- **Prefixos hoje.** `[external]` `transform` funciona sem prefixo em todos os navegadores atuais. Os fabricantes trocaram os prefixos por flags (https://developer.mozilla.org/en-US/docs/Glossary/Vendor_Prefix). O `-o-` é do Opera antigo (Presto); desde 2013 o Opera é Chromium e usa `-webkit-`. Ver [[wiki/concepts/prefixo-de-fornecedor]].
- **"Melhora a nossa performance"** quer dizer produtividade de quem escreve. O CSS gerado não fica mais rápido por ter vindo do Sass.
- **"Acessibilidade"** aparece no sentido de "disponibilidade em mais navegadores", não de [[wiki/concepts/acessibilidade]] (a11y).
- **SCSS é superconjunto do CSS.** `[external]` Todo CSS válido é SCSS válido; por isso a sintaxe é tão próxima. A indentada (`.sass`) é a original (https://sass-lang.com/documentation/syntax/).
- **"Isso aqui já é um recurso do CSS que não é permitido no CSS puro"** deve ser "do SCSS": ele está falando do aninhamento.
- **Data da gravação.** Edge 88 e 89 como versões atuais no Can I use apontam para o começo de 2021 (inferência). `[external]` O LibSass foi descontinuado em 2020; a implementação mantida é o Dart Sass (https://sass-lang.com/blog/libsass-is-deprecated/), relevante para a aula de instalação.

## Open Questions

- "Eles são mais focados na TUI": "na UI"? "na teoria"? A legenda está assim e o contexto não decide.
- Antes de "Hashtag 0c, 0c, 0c" há 9 segundos sem legenda: a parte em que ele digita o seletor `body` e o `background-color` sumiu. A cor bate com o `#0c0c0c` da [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html|prática 1 de Flexbox]].
- "No CodePen [...] tem o CSS, CSS": provavelmente "Sass, SCSS" no seletor de pré-processador; a legenda não deixa claro.
- Qual configuração gerou o `-webkit-` no projeto? Live Sass Compiler com autoprefix, ou um passo de PostCSS?

## Raw quotes

- "a tecnologia é maior que a ferramenta"
- "o Sass não é lido pelo browser"
- "ele cospe já o arquivo CSS, só que otimizado"
