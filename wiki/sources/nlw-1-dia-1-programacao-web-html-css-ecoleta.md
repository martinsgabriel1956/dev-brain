---
type: source
title: "NLW #1, dia 1: introdução à programação web, HTML e CSS na página inicial do Ecoleta"
aliases: ["NLW 1 dia 1", "Next Level Week 1 dia 1", "Ecoleta página inicial", "aula Ecoleta HTML CSS"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [frontend, html, css, flexbox, box-model, display, seletores-css, variaveis-css, media-query, google-fonts, vs-code, emmet, live-server, devtools, cliente-servidor, http, algoritmo, logica-de-programacao, javascript, rocketseat, ecoleta, iniciante]
skill: tech-mentor-frontend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-1-dia-1-programacao-web-html-css-ecoleta.md"
source_url: ""
author: "Mayk Brito (inferido)"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #1, dia 1: introdução à programação web, HTML e CSS na página inicial do Ecoleta

## TL;DR

Primeira aula (cerca de 1h53) da [[wiki/entities/next-level-week|Next Level Week #1]] da [[wiki/entities/rocketseat]], dada por [[wiki/entities/mayk-brito|Mayk Brito]] (autoria inferida: o instrutor é chamado de "Mayk" e "Maykão" ao longo da aula; o nome completo não aparece). O público é quem nunca programou. A aula tem duas metades. A primeira é conceitual: programar é "ensinar o computador", com [[wiki/concepts/algoritmo|algoritmo]] (o passo a passo), [[wiki/concepts/logica-de-programacao|lógica]] (a maneira de pensar) e sintaxe ("cruel e destruidora"), JavaScript como a linguagem da semana, e o modelo [[wiki/concepts/arquitetura-cliente-servidor|cliente-servidor]] explicado com garçom e cozinheiro, HTTP e [[wiki/concepts/url|URL]]. A segunda é prática: no [[wiki/entities/vs-code]], com Emmet e Live Server, ele monta a página inicial do **Ecoleta**, um marketplace de pontos de coleta de resíduos feito para a semana do meio ambiente. Passa por estrutura do HTML5, `<link>` do [[wiki/entities/google-fonts]], arquivo CSS externo, [[wiki/concepts/box-model]], [[wiki/concepts/display-css|block x inline]], [[wiki/concepts/flexbox]], classes e ids, `max-width` + `margin: 0 auto`, imagem de fundo SVG, [[wiki/concepts/variaveis-css|variáveis CSS]], reset com `*`, `:hover` + `transition`, `::after` e uma media query de 900 px.

## Key Claims

### Programar é ensinar o computador

- **Três ingredientes.** Algoritmo é "o passo a passo das coisas que você está fazendo", não "aquele log de 10" da escola. Exemplo: acordar, lavar o rosto, escovar os dentes, tomar café. Lógica de programação é "a maneira de pensar as coisas": trocar a ordem dos mesmos passos (café antes de escovar) muda o resultado. Ver [[wiki/concepts/algoritmo]] e [[wiki/concepts/logica-de-programacao]].
- **Sintaxe "cruel e destruidora".** "Se você errar uma vírgula, um pontinho [...] você pode quebrar toda a sua aplicação". Ele estima que "80% a mais dos seus erros" na semana virão de escrita, porque lógica e algoritmo estarão na tela e "a sintaxe é toda com você". Mais tarde demonstra: uma aspa faltando no `font-family` e "não aparece nada".
- **Por que JavaScript.** "Toda página web que você abrir terá JavaScript", serve a front-end e back-end, tem comunidade forte e faz web, mobile, desktop e games.
- **Erros são comuns.** Depois de corrigir um link de fonte errado: "Nós somos pagos como programadores pra resolver problemas".

### Cliente-servidor, HTTP e URL

- **O garçom.** Você (cliente) pede ao garçom, que leva ao cozinheiro e volta com a comida. "Tudo que for do garçom pra lá" é o servidor, que responde mesmo que seja "não tenho tal coisa". Ver [[wiki/concepts/arquitetura-cliente-servidor]].
- **Protocolo é conjunto de regras.** HTTP é o "protocolo de transferência de hipertextos" e o S "significa que é seguro". Ver [[wiki/concepts/http-vs-https]].
- **URL é o endereço.** Digitar youtube.com faz um pedido; clicar num vídeo acrescenta "mais propriedades" à URL, "o pedido mudou", "logo as respostas também mudaram". Ele expande a sigla como "Universal Resource Location" (ver Tensões).
- **Front-end x back-end.** Front-end é "tudo o que você vê aqui bonito", estrutura, dados, palavras; ao clicar em download "ele está indo lá no back-end", onde o arquivo está guardado.

### HTML, CSS e JavaScript como corpo humano

- **HTML** é "uma linguagem de marcação de texto", não de programação; vê-se em View Page Source. A sigla: hypertext são os links, markup é a marcação e language a linguagem. Ver [[wiki/concepts/html-hipertexto]].
- **CSS** é "a beleza", "o estilo"; o slide da aula compara o HTML a ossos e músculos (a transcrição só capta "seriam os músculos desse corpo").
- **JavaScript** é "a parte inteligente, o cérebro", visto numa tag `<script type="text/javascript">` no fim do código-fonte.

### Ambiente

- **Navegador:** Chrome ou o Edge novo ("não o Edge que veio nos Windows mais antigos"), porque "ambos estão compartilhando o mesmo motor" e têm o mesmo DevTools (F12).
- **Editor:** [[wiki/entities/vs-code]] com o tema "Launch Base Theme" (nome dito assim) e a extensão Live Server.
- **Nome de arquivo:** `.html` é obrigatório; minúsculas, sem acento, sem cedilha, sem espaço, "de preferência, o próprio index.html".
- **Salvar:** a bolinha na aba indica arquivo não salvo, "um dos motivos da gente às vezes não conseguir acompanhar a aula".

### Estrutura do HTML

- **Doctype curto:** "antigamente [...] eu precisava escrever isso daqui de uma maneira muito grande"; hoje `<!DOCTYPE html>` identifica o HTML5.
- **Tags** abrem com `<nome>` e fecham com `</nome>`; "não são todas as tags que tem essa maneira de abrir e fechar, mas a maioria".
- **head e body:** sem eles o Live Server avisa que "live reload não é possível". Com Emmet, `!` + Enter gera tudo.
- **head = configurações:** `lang="pt-BR"`, `<title>`, `meta charset` UTF-8 ("cedilha, til, acentuações especiais") e `meta viewport` (para caber "em telas de diversos tamanhos", base da media query no fim da aula).
- **Comentários** `<!-- -->` somem da página e do DevTools mas ficam no código-fonte.
- **Primeiras marcações:** `h3`, `a` com `href` ("esse href não vai funcionar no h1, porque ele é um atributo da tag a"), `h1`, `p`, `button` (depois trocado por `a` com `span` e `strong`), `img` com `src` e `alt` ("alternativa à imagem" e acessibilidade para leitores de tela).
- **Semântica:** `header` e `main` dão significado "tanto para quem for da manutenção do meu código, quanto para robozinhos do Google". `div` é "uma caixa que não tem muito significado". Ver [[wiki/concepts/html-semantico]].

### CSS: fontes, arquivo externo e seletores

- **Google Fonts:** escolhe Roboto 300 e 700, copia o `<link>` do embed e a regra `font-family: 'Roboto', sans-serif`. Mais tarde junta Ubuntu 700 no mesmo link ("ele faria duas chamadas lá no servidor do Google, isso não é muito legal"). Ver [[wiki/entities/google-fonts]] e [[wiki/concepts/webfonts]].
- **Aspas na fonte:** "se eu tenho só um nome, eu não preciso colocar a aspas"; com dois nomes, sim.
- **`<style>` → `styles/main.css`:** "é melhor que cada arquivo esteja no seu lugar". O caminho `/styles/main.css` parte da raiz servida pelo Live Server (127.0.0.1:5500).
- **Seletores:** de tag (`html`, `body`, `a`), de classe (`.red`, "pontinho é a referência para uma classe"), de id (`#page-home`), descendente (`#page-home .content`), universal (`*`), agrupado (`h1, h2, h3...`) e `:root`. Ver [[wiki/concepts/seletores-css]].
- **class x id:** class "eu posso repeti-lo em diversos elementos", é "uma classificação"; id "não pode ser repetido de nome". O nome da classe, "quanto mais semântico melhor".
- **Cascata como encadeamento:** "é uma forma de cascata. É por isso que chama-se Cascading Style Sheet", dito sobre o seletor descendente (ver Tensões e [[wiki/concepts/cascata-css]]).
- **Sobrescrita:** a cor dos títulos definida no grupo `h1...h6` aparece riscada no DevTools porque "lá na frente, depois no meu documento" o `#page-home main h1` define outra.

### Box model e display

- **Toda caixa tem** largura, altura, padding, border, margin, cor e fundo. Caixas cabem dentro de caixas. Ver [[wiki/concepts/box-model]].
- **block x inline:** block "pega toda a linha e joga o próximo elemento para baixo"; inline "fica do tamanho dela" e só fica ao lado de outro inline. `a` e `span` são inline; o display aparece na aba Computed do DevTools. Ver [[wiki/concepts/display-css]].
- **Por fora e por dentro:** block e inline são "para as caixas pelo seu lado de fora"; `display: flex` muda os filhos "pelo lado de dentro". Um elemento flex "por fora, ela vai ser a propriedade block".
- **Não decorar:** "nada daqui a gente decora, a gente aprende"; o CSS tem "diversos tricks".

### Flexbox

- **Header:** `display: flex` põe logo e link lado a lado; `align-items: center` alinha; `justify-content: space-between` joga um para cada canto. "Você não sabe o tanto que a gente sofreu no passado para fazer esse tipo de alinhamento". Ver [[wiki/concepts/flexbox]].
- **Coluna:** `.content` e `main` viram `display: flex; flex-direction: column`; `main` recebe `flex: 1` ("preenche automaticamente todo o espaço que ele tiver") e `justify-content: center`, que no eixo de coluna centraliza na vertical. Ele mostra a alternativa rígida (`height: 600px`, "pixel nunca é flexível") antes da dinâmica.
- **Botão:** `a` flex com um `span` de 72x72 e um `strong` com `flex: 1` e `text-align: center`; o `span` também é flex para centralizar o ícone.

### Larguras e centralização

- **% x px:** `width: 90%` acompanha a página; 900 px "sempre será 900". `max-width: 1100px` limita: "o máximo é o máximo".
- **`margin: 0 auto`:** com o block, as margens laterais automáticas dividem a sobra e deixam a caixa "sempre, sempre ao meio".
- **Shorthand de margin:** um valor para os quatro lados; dois (vertical, horizontal); três (topo, laterais, base); quatro "de uma maneira de relógio", top, right, bottom, left. Ver [[wiki/concepts/shorthand-css]].
- **`vh`:** `height: 100vh`, a viewport "dividida em 100 bloquinhos". Ver [[wiki/concepts/unidades-de-medida-css]].

### Fundo, cores e variáveis

- **Imagem de fundo:** `background: url("../assets/home-background.svg") no-repeat`, com `background-position: 35vw bottom`. `../` "sai dela, ou seja, vai uma pasta acima". O SVG "é todo escrito em formato de texto" e "se adapta a telas de diversos tamanhos". Ele escreve `background-url`, percebe depois ("não era não, era image") e usa `background-image` no ícone. Ver [[wiki/concepts/background-css]] e [[wiki/concepts/formato-svg]].
- **Ícone em `span` vazio** só aparece com `width`, `height` e `display: flex`; inline não mostra o fundo.
- **Hexadecimal:** pares de 00 a FF para vermelho, verde e azul (ele troca a ordem e se corrige: "Red, Green, Blue"). `#F0F0F5` é o fundo do `body`. Ver [[wiki/concepts/sistema-hexadecimal]].
- **`rgba(0, 0, 0, 0.08)`:** canais de 0 a 255 e alfa de 0 a 1, para escurecer o `span` sem que o hover o iguale ao fundo.
- **Variáveis em `:root`:** `--title-color: #322153` e `--primary-color: #34CB79`, usadas com `var()`. "Se algum dia eu quiser mudar essa cor aqui, eu não preciso ir em todos os lugares". Ver [[wiki/concepts/variaveis-css]].

### Texto, reset e interação

- **Reset:** `* { margin: 0; padding: 0 }` zera os espaços "que já vêm no navegador" (o *user agent stylesheet* que ele mostra no DevTools), e as margens passam a ser postas à mão.
- **Texto** segue outra lógica que o box model: tamanho, tipo, espaçamento (`line-height`) e alinhamento. `font-size: 24px`, `line-height: 38px`.
- **`text-decoration: none`** no seletor `a` global tira o sublinhado de todos os links.
- **`-webkit-font-smoothing: antialiased`** no `body` deixa a fonte "um pouco mais gostosa de se ver" (ver Tensões).
- **`border-radius`** é shorthand dos quatro cantos; com dois valores, alterna a partir do canto superior esquerdo. `border-top-left-radius` e `border-bottom-left-radius` arredondam só o `span` para não sobrar quina.
- **`:hover` + `transition: 400ms`:** o verde escurece para `#2FB86E` de forma suave. Ver [[wiki/concepts/pseudo-classe-css]].
- **`::after`:** "elementos que não tem aqui no HTML, mas a gente vai criar ele através do CSS"; precisa de `content` (vazio ou "blá blá") e recebe o ícone de busca como fundo. Ver [[wiki/concepts/pseudo-elemento-css]].

### Responsividade

- **`@media (max-width: 900px)`:** "a largura de 0 até 900 pixels aplica-se regras específicas". Depende da `meta viewport`. Ver [[wiki/concepts/breakpoint]].
- **O que muda abaixo de 900 px:** a imagem vai para `background-position-x: 70vw` para não encavalar no texto; `.content` e `main` ganham `align-items: center` e `text-align: center`.
- **Link absoluto centralizado:** `position: absolute; bottom: 48px; left: 50 [px, dito]; transform: translateX(-50%)`, "uma folha de papel em cima de outra". O `translateX(-50%)` "faz com que ele ache o ponto médio". Ver [[wiki/concepts/css-position]].

### Atitude

- **Maratona, não 100 metros:** "Uma das coisas que não dá certo para quem quer entrar no mundo da programação é a ansiedade e a pressa de conseguir resultados rápidos"; "tijolinho por tijolinho", todos os dias. Ver [[wiki/concepts/pratica-deliberada]].

## Tensões e precisões

- **URL.** A sigla é *Uniform Resource Locator*, não "Universal Resource Location" `[external]` (https://datatracker.ietf.org/doc/html/rfc3986). Ver [[wiki/concepts/url]]. Confiança alta.
- **O "S" do HTTPS** é HTTP sobre TLS: tráfego cifrado e servidor autenticado por certificado. "Seguro" não diz nada sobre o conteúdo do site `[external]` (https://developer.mozilla.org/en-US/docs/Glossary/HTTPS).
- **Cascata não é o seletor descendente.** Em CSS, *cascading* é o algoritmo que decide entre declarações conflitantes (origem, especificidade, ordem), não o encadeamento `#page-home .content` `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/Cascade). O próprio exemplo da cor sobrescrita no DevTools é que mostra a cascata. Contradiz o que [[wiki/concepts/cascata-css]] registra das aulas do FrontPUSH, que estão corretas.
- **`left: 50` deve ser 50%.** Com `left: 50px` o `translateX(-50%)` não centraliza; a técnica clássica é `left: 50%` + `translateX(-50%)` `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/translateX). Pode ser erro de ASR ou de fala; o vídeo não está disponível. Confiança média.
- **`flex: 1` não é só flex-grow.** É o shorthand de `flex-grow: 1; flex-shrink: 1; flex-basis: 0%` `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/flex). A aula diz "o flex growth".
- **`-webkit-font-smoothing`** não é padrão e só faz efeito no macOS `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/font-smooth). No Windows da aula, o ganho visual mostrado não vem dela. Confiança alta.
- **Aspas em `font-family`:** nomes com espaço sem aspas são válidos se forem identificadores, mas a especificação recomenda aspas `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/font-family). Roboto e Ubuntu de fato não precisam.
- **Desktop-first.** A media query é `max-width` (desktop primeiro, remendo para telas menores). `[skill: tech-mentor-frontend]` recomenda mobile-first com `min-width`: estilos base para o celular e acréscimos para telas maiores. Ver [[wiki/concepts/breakpoint]].
- **Reset.** O reset da aula zera margin e padding. `[skill: tech-mentor-frontend]` O reset usual hoje é `*, *::before, *::after { box-sizing: border-box; }` (camada "Generic" do ITCSS), que a aula não usa.
- **Hexadecimal "de zero até F"** vale por dígito; cada par vai de 00 a FF (0 a 255). A aula diz "as duas primeiras letrinhas, elas vão de zero até F".

## Entidades

- [[wiki/entities/mayk-brito]]: instrutor (autoria inferida)
- [[wiki/entities/rocketseat]]: organizadora da NLW (a transcrição dizia "Rocket City")
- [[wiki/entities/next-level-week]]: o evento; o Ecoleta é o projeto da semana
- [[wiki/entities/vs-code]]: editor, Emmet, Live Server
- [[wiki/entities/google-fonts]]: Roboto e Ubuntu

Citados sem página: Thiago (designer do layout do Ecoleta, "amigo nosso aqui da Rocketseat"), Chrome, Edge, Notion (onde ficam os links e os assets), YouTube (exemplo de URL), Google.

## Conceitos

[[wiki/concepts/algoritmo]] · [[wiki/concepts/logica-de-programacao]] · [[wiki/concepts/arquitetura-cliente-servidor]] · [[wiki/concepts/url]] · [[wiki/concepts/http-vs-https]] · [[wiki/concepts/html-hipertexto]] · [[wiki/concepts/html-semantico]] · [[wiki/concepts/css]] · [[wiki/concepts/seletores-css]] · [[wiki/concepts/cascata-css]] · [[wiki/concepts/box-model]] · [[wiki/concepts/display-css]] · [[wiki/concepts/flexbox]] · [[wiki/concepts/shorthand-css]] · [[wiki/concepts/unidades-de-medida-css]] · [[wiki/concepts/background-css]] · [[wiki/concepts/formato-svg]] · [[wiki/concepts/sistema-hexadecimal]] · [[wiki/concepts/variaveis-css]] · [[wiki/concepts/webfonts]] · [[wiki/concepts/pseudo-classe-css]] · [[wiki/concepts/pseudo-elemento-css]] · [[wiki/concepts/css-position]] · [[wiki/concepts/breakpoint]] · [[wiki/concepts/setup-live-reload-debug-testes]] · [[wiki/concepts/pratica-deliberada]]

## Open Questions

- O vídeo confirmaria `left: 50%` e o nome do tema do VS Code ("Launch Base Theme").
- A data não é dita; "semana do meio ambiente" e Ecoleta apontam para a NLW #1 de junho de 2020 `[external, não verificado]`.
- O CSS final é desktop-first e sem `box-sizing`. O [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta|dia 2]] aplica `* { box-sizing: border-box }` e acrescenta media queries `min-width` e `max-height`, mas continua sem mobile-first.

## Raw quotes

- "Sintaxe aqui é cruel e destruidora."
- "O JavaScript seria, dentro desse corpo humano, então, a parte inteligente, o cérebro."
- "Pixel nunca é flexível."
- "Nós somos pagos como programadores pra resolver problemas."
- "Não é uma corrida de 100 metros que você vai correr e vai parar e chegou no fim e acabou."
