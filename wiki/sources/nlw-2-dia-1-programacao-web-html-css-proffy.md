---
type: source
title: "NLW #2, dia 1: introdução à programação web, HTML e CSS na página inicial do Proffy"
aliases: ["NLW 2 dia 1", "Next Level Week 2 dia 1", "Proffy dia 1", "aula Proffy HTML CSS"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [frontend, html, css, box-model, box-sizing, display, flexbox, seletores-css, especificidade, heranca-css, variaveis-css, unidades-de-medida-css, rem, em, mobile-first, google-fonts, vs-code, emmet, live-server, devtools, caminho-de-arquivo, cliente-servidor, http, algoritmo, logica-de-programacao, javascript, rocketseat, proffy, iniciante]
skill: tech-mentor-frontend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-2-dia-1-programacao-web-html-css-proffy.md"
source_url: ""
author: "Mayk Brito"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #2, dia 1: introdução à programação web, HTML e CSS na página inicial do Proffy

## TL;DR

Primeira aula (cerca de 2h19) da [[wiki/entities/next-level-week|Next Level Week]] em que o projeto é o **Proffy**, "nossa plataforma de estudos online" para estudar ou dar aulas, feita para a semana do "dia dos profissionais da educação". O instrutor é [[wiki/entities/mayk-brito|Mayk Brito]], que se apresenta pelo nome ("Mayk Brito na área"); o layout é de Thiago, da [[wiki/entities/rocketseat]]. A transcrição só diz "NLW"; que é a **NLW #2** foi confirmado pelo usuário. A data (agosto de 2020) segue inferida `[external, não verificado]`.

O roteiro repete o do [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta|dia 1 da NLW #1]], também de Mayk: algoritmo, lógica e sintaxe; por que JavaScript; cliente-servidor com garçom e cozinheiro; HTTP e URL; [[wiki/entities/vs-code]] com Emmet e Live Server. A diferença está na segunda metade. O projeto não sai do esqueleto (um `h1` "Proffy", um `p` e dois botões centralizados), e o tempo vai para fundamentos que a NLW #1 só tocou: [[wiki/concepts/especificidade-css|força dos seletores]] (id > classe > tag), pais e filhos com cor herdada, caminho com `/` a partir da raiz do servidor, [[wiki/concepts/variaveis-css|variáveis CSS]] copiadas do [[wiki/entities/figma]], `px` x `%` x `rem` x `em` com `:root { font-size: 60% }`, [[wiki/concepts/mobile-first]], [[wiki/concepts/box-model]] com shorthand em sentido horário e `box-sizing: border-box`, block x inline x flex, Poppins do [[wiki/entities/google-fonts]] e `width: 90vw; max-width: 700px`.

## Key Claims

### Programar é ensinar o computador

- **Três elementos.** Algoritmo é "um passo a passo, é um conjunto de regras", não o logaritmo do ensino médio. O exemplo é a rotina matinal, e o computador precisa dela "muito detalhada": não sabe onde está o café nem o que é escovar os dentes. Ver [[wiki/concepts/algoritmo]].
- **Lógica é a ordem.** Escovar os dentes antes do café deixa o café "com um gosto meio de pasta de dente"; depois, "deixa os dentes limpos". "Cada maneira de pensar trará resultados diferentes." Ver [[wiki/concepts/logica-de-programacao]].
- **Sintaxe quebra o programa.** No português dá para escrever "pq" e "vc"; na linguagem de programação, "se você não escrever da maneira correta, você simplesmente vai quebrar a sua aplicação". Ele estima "80% ou mais de erros" de escrita.
- **"Ser programador é resolver erros."** Quanto mais você souber lidar com os erros, melhor a carreira.
- **0 e 1.** "A máquina só entende 0 e 1"; a linguagem fica "mais perto do lado humano" e é traduzida para a máquina.
- **Por que JavaScript.** Mobile, web e desktop; "inevitavelmente, enquanto você programar para a web, você vai encontrar o JavaScript"; comunidade forte e linguagem "super, super moderna".

### Ambiente

- **Navegador:** Edge no Windows e Mac, Chrome no Linux ("no Linux ainda não tem o Edge"), porque os dois usam o mesmo motor de JavaScript e o mesmo DevTools (F12). Outro navegador pode dar "um errinho ou outro".
- **Editor:** [[wiki/entities/vs-code]], extensível por plugins. Ele esconde a status bar e o minimap e instala o tema dito "launch base".
- **Suporte:** Discord da NLW, com a equipe e os outros alunos.
- **Pasta:** `C:\nlw`, com as imagens do Notion. "Muito importante": abrir a pasta pelo Open Folder, senão o Live Server não funciona.

### Cliente-servidor, HTTP e URL

- **Restaurante.** O cliente pede ao garçom, o garçom leva à cozinha, o cozinheiro prepara e o garçom traz "a resposta do seu pedido". Front-end é o cliente, back-end é a cozinha. Ver [[wiki/concepts/arquitetura-cliente-servidor]].
- **HTTP** é "um conjunto de regras para transferência de hipertexto"; o S "é secure". Ver [[wiki/concepts/http-vs-https]].
- **URL** "significa Universal Resource Location" (ver Tensões). youtube.com é único: "só existe um lugar no mundo disponível esse nome". Clicar num vídeo é pedir e receber: "tá rolando uma troca de dados". Ver [[wiki/concepts/url]].
- **HTML, CSS e JavaScript** estão "sempre" em toda página. No site do VS Code: o código-fonte (Ctrl+U) é HTML; o botão azul, as fontes e o posicionamento são CSS; a animação ao clicar é JavaScript, "a parte inteligente".

### Arquivo, tags e o hard reload

- **Extensão:** `.html` faz o arquivo "ser entendido como um HTML". Ele mostra o nome "introdução à programação" e pede: nada de cedilha, til ou espaço ("coloca um underline [...] coloque tracinhos"), porque "esse caractere especial não existe na língua do inglês" e o espaço pode ser interpretado de outro jeito.
- **index.html** é o nome certo para o primeiro arquivo: "o primeiro arquivo que ele vai procurar é o index.html".
- **Bolinha na aba** = arquivo não salvo.
- **Doctype** de HTML5; no HTML 4 seria "de uma maneira bem esquisita até".
- **Tag:** sinal de menor, nome, sinal de maior. "Toda tag aberta deverá ser fechada", com exceções que vêm depois: `img` e `link` "se fecham" (*self-closing*).
- **Hard reload (Ctrl+Shift+R):** o navegador guarda coisas em cache e às vezes mostra "a informação que estava no cache e não a informação que a gente alterou"; o *hard* manda pegar tudo de novo.
- **Comentário** `<!-- -->` some da página e aparece no View Page Source. Ele o usa como caderno de aula.

### HTML: hipertexto, head e body

- **Não é programação.** "HTML não é programação, HTML é uma linguagem de marcação de hipertexto". Hipertexto é "um texto com mais força": nasceu com a tag `a` (links que levam a outra página) e depois ganhou imagens e vídeos. Ver [[wiki/concepts/html-hipertexto]].
- **head x body:** "Todo o conteúdo visível na página deverá vir na tag body"; no head ficam "configurações do meu documento". Texto solto no head aparece, e um HTML sem head e body também aparece, mas "está mal escrito" e dará problema com CSS e JavaScript.
- **Emmet:** `!` + Enter gera a base. Ver [[wiki/entities/vs-code]].
- **Atributo** é "alguma coisa no meio da tag": `lang="pt-BR"`, `meta charset` UTF-8, `meta viewport` (adapta "para telas maiores ou menores"), `title` (o título da aba passa de "Document" para Proffy e "sua plataforma de estudos online"). Ver [[wiki/concepts/head-html-metadados]] e [[wiki/concepts/charset]].
- **Inglês:** a documentação que aparece ao passar o mouse vem em inglês; "quanto melhor for o inglês, mais fácil o entendimento das tecnologias". Ver [[wiki/concepts/ingles-para-desenvolvedores]].

### Live Server

- **Por quê:** salvar e ver a página atualizar sozinha. A extensão "criou um servidor pra gente", e a URL deixa de ser `C:` e passa a ser `127.0.0.1:5500`.
- **Regra:** "Nunca mais eu vou dar dois cliques nesse arquivo para abrir ele." Só Open with Live Server. Ver [[wiki/concepts/setup-live-reload-debug-testes]].

### Marcação e estrutura

- **Estrutura** é "a estrutura óssea" do corpo; a beleza vem do CSS. As marcações são feitas com tags.
- **`h1` a `h6`** são títulos com estilo do navegador; **`p`** é parágrafo e quebra a linha. Espaços e quebras no código-fonte não aparecem como no Word.
- **`img`:** `src` é "a fonte, a origem do arquivo" (ele cola a URL de uma maçã). `alt` é "uma alternativa ao source que não existe" e serve a leitores de tela: "ele vai ler maçã". Ver [[wiki/concepts/texto-alternativo]].
- **`button`:** "Estudar" e "Dar aulas".
- **Por que estruturar bem:** leitura do código, "motores de busca" e acessibilidade.
- **Atributos** podem ser específicos (`src` só em imagem) ou globais (`class`, `id`).

### CSS: onde escrever e como selecionar

- **Três lugares:** atributo `style` (rejeitado: "imagina um HTML tudo cheio dessas tags style"), tag `<style>` no head e `<link rel="stylesheet" href="style.css">`. Ver [[wiki/concepts/css]].
- **Regra:** seletor, chaves, "chave, dois pontos, valor, ponto e vírgula". "Se não tiver ponto e vírgula no final, poderemos ter muitos problemas."
- **Seletores:** de tag (`h1`), de classe (`.red`, "eu coloco um pontinho") e de id (`#page-landing`, "o hashtag"). Classe se repete; id "não pode se repetir": "Vai dar certo, mas você não vai conseguir depois trabalhar com CSS ou com JavaScript". Ver [[wiki/concepts/seletores-css]].
- **Ctrl+/** comenta a linha; Ctrl+Shift+P → Keyboard Shortcuts lista os atalhos.

### Pais, filhos, cascata e força

- **Pais e filhos** servem "para o CSS, para o HTML e para o JavaScript". `color: red` em `#page-landing` (o body) pinta `h1`, `p` e `img`; o botão fica de fora porque "tem uma força diferente" (ver Tensões e [[wiki/concepts/heranca-css]]).
- **O filho direto vence o pai.** `h1 { color: green }` ganha do vermelho do body "não importa o posicionamento" no arquivo.
- **"Cascata"** para ele é o caminho descendente: `#page-landing h1` "tem uma força maior, porque ele tem uma força de cascata". CSS = Cascading Style Sheet, "folha de estilo em cascata".
- **Ordem de força:** "o seletor de hashtag é o seletor mais forte", depois a classe, depois a tag. Com o id no próprio `h1`, `#page-landing` vence `.body h1`; `.body #page-landing` vence `#page-landing`, porque "está aplicando a cascata além dos seletores fortes". Ver [[wiki/concepts/especificidade-css]] e [[wiki/concepts/cascata-css]].
- **Comentário em CSS:** `/* */`.

### Localização de arquivos

- **Sem barra:** `href="style.css"` funciona no `index.html` da raiz. Copiado para `page/page.html`, perde a cor; o console acusa `page/style.css`. O navegador "entendeu que estava no mesmo nível aonde está o page.html".
- **Com barra:** `/style.css` aponta para "a raiz do meu projeto", ou seja, `127.0.0.1:5500/`. "Por causa de uma barra eu poderia estar dias descobrindo o porquê". Ver [[wiki/concepts/caminho-relativo]].

### Figma, cores e variáveis

- **[[wiki/entities/figma]]:** é preciso fazer login para pegar as cores. O painel de CSS "são só sugestões".
- **Variáveis em `:root`:** "dois tracinhos" definem variáveis lidas com `var(--color-background)`, `var(--color-primary-darker)`. A vantagem: mudar uma cor "no documento inteiro" de uma vez. Ver [[wiki/concepts/variaveis-css]].
- **Formatos de cor:** hexadecimal ("só isso que você precisa saber"), HSL, RGB e por extenso (`red`, `white`, `black`); o seletor de cor do VS Code alterna entre eles. Ver [[wiki/concepts/sistema-hexadecimal]] e [[wiki/concepts/modelos-de-cor]].

### Unidades de medida

- **Padrão:** `font-size` 100% = 16 px = 1 rem.
- **`%`** é relativo ao pai: `h1` com 50% dentro de um body 100% de um root 50% fica com 25% do padrão.
- **`rem`** é relativo ao `:root`; **`em`**, ao elemento pai. Um `span` com `0.2em` dentro de um `h1` de `3em` fica "0.2 de 3 de 100 de 50"; com `0.2rem`, pula os intermediários.
- **`px`** é fixo: "num dispositivo pequeno, 16 pixels é uma coisa muito grande. Num dispositivo enorme, uma tela de 4K, 16 pixels não é nada" (ver Tensões). Ver [[wiki/concepts/unidades-de-medida-css]].
- **`:root { font-size: 60% }`** é o ponto de partida do projeto: "a gente vai começar tudo um pouquinho menor". O texto do body fica com `1.6rem`.

### Responsividade e mobile first

- **Responsividade:** "não importa o tamanho do meu dispositivo, esse site vai ficar bonito nele". Ver [[wiki/concepts/design-responsivo]].
- **Mobile first:** "primeiro eu vou focar nesses dispositivos [pequenos] [...] e depois eu vou arrumar essa página para o desktop". Ver [[wiki/concepts/mobile-first]].
- **Unidades da semana:** "todo o controle de medida que eu vou fazer daqui pra frente, eu vou usar rem [...] ou porcentagens, que são unidades flexíveis"; pixel "só quando eu for mexer no desktop".

### Box model

- **"Todo e qualquer elemento HTML, quando trabalhado com o CSS, ele está sendo uma caixa."** Toda caixa tem largura, altura, conteúdo, espaço dentro e fora, e limites. Ver [[wiki/concepts/box-model]].
- **`div`** é "uma caixa que não tem significado nenhum no HTML", só para estilizar. Vira `#container`, com o id `page-landing` passando para o body.
- **`border: 1px solid red`** mostra os limites da caixa.
- **Shorthand:** quatro valores em "sentido horário" (meio-dia, 3, 6, 9: top, right, bottom, left); um valor para os quatro lados; dois para vertical e horizontal; três para topo, laterais e base. Ele também mostra as propriedades soltas (`padding-left`, `padding-bottom`) para quando só um lado muda. Ver [[wiki/concepts/shorthand-css]].
- **`width: 300px`** maior que a janela gera barra de rolagem: "o pixel não vai respeitar o tamanho do seu dispositivo".
- **Reset:** `* { margin: 0; padding: 0; box-sizing: border-box }`. No DevTools, o `margin: 8px` que o *user agent* põe no body aparece riscado. Ver [[wiki/concepts/estilos-padrao-do-navegador-e-reset]].
- **`box-sizing`:** o padrão é `content-box` (width mede o conteúdo e o padding soma por fora); `border-box` mede pela borda. Uma caixa de 100 px com 50 px de padding cresce no padrão e fica com 100 px no `border-box`, com o conteúdo "vazando".

### Display

- **block x inline:** "por fora da caixa". `h1`, `p`, `div` são block e ocupam "toda a linha"; `a`, `span`, `strong` são inline e ficam "um ao lado do outro". Display é "a exibição do elemento". Ver [[wiki/concepts/display-css]].
- **flex e grid:** "regras para dentro da caixa". `display: flex` no body põe os filhos lado a lado; `align-items: center` e `justify-content: center` só funcionam com flex ou grid. Ver [[wiki/concepts/flexbox]].
- **Centralizar na tela:** `height: 100vh` ("quebra ela em 100 pedacinhos"), movido para `html, body` como "boa prática". Ver [[wiki/concepts/unidades-de-viewport]].
- **`display: inline-block`** fica para outro dia.

### Fontes e container

- **Google Fonts:** o `<link>` traz a Poppins. A regra vai em `body, input, button, textarea`, porque o `button` não pega a fonte nem a cor do body: "esse aqui não pegou, ó. Nem cor, nem fonte". Ver [[wiki/entities/google-fonts]] e [[wiki/concepts/webfonts]].
- **`font: 500 1.6rem Poppins`** agrupa `font-weight` (100 leve, 700 "como bold"; *weight* "no inglês, peso"), `font-size` e `font-family`. Ver [[wiki/concepts/peso-tipografico]].
- **`#container { width: 90vw; max-width: 700px }`**: abaixo de 700 px acompanha a tela; acima, para em 700.
- **Resultado do dia:** título, subtítulo e dois botões centralizados no fundo da cor do layout. JavaScript, espaçamento, alinhamento e posicionamento ficam para o dia seguinte.

## Tensões e precisões

- **URL.** A sigla é *Uniform Resource Locator* `[external]` (https://datatracker.ietf.org/doc/html/rfc3986). Mesmo erro da NLW #1. Confiança alta.
- **Força de "cascata" é especificidade.** `.body #page-landing` vence `#page-landing` porque soma (1,1,0) contra (1,0,0), não por "força de cascata". Cascata é o algoritmo inteiro: origem, especificidade e, no empate, a ordem `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity). "Não importa o posicionamento" só vale com especificidades diferentes: no empate, a última regra vence. A ordem id > classe > tag está certa. Contradiz de novo [[wiki/concepts/cascata-css]], que traz a definição correta. Confiança alta.
- **O `h1` verde vence o body vermelho por herança, não por força.** Cor declarada no pai só chega ao filho por herança, e qualquer regra que mire o filho vence um valor herdado, mesmo uma regra de tag contra um id `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/Inheritance). Ver [[wiki/concepts/heranca-css]].
- **O botão não tem "força diferente".** A folha do navegador dá a `button` (e a `input` e `textarea`) cor e fonte próprias, então ele não herda as do body. É o mesmo motivo de a Poppins precisar de `body, input, button, textarea`; `font: inherit` nos controles resolveria. Inferência do agente com base na folha do *user agent*; confiança média.
- **`rem` não acompanha o tamanho da tela.** `rem` segue o `font-size` do root, que só muda se uma media query mudar. O que ele traz é respeito à fonte que o usuário escolheu no navegador, e isso o `px` no root anula. "Vão corresponder ao tamanho que eu tiver na página" vale para `%` de largura e `vw`, não para `rem`. Confiança alta.
- **Pixel do CSS não é pixel do monitor.** O `px` do CSS é uma unidade de referência, escalada pela densidade da tela; num monitor 4K com escala do sistema, 16 px não é "um pontinho" `[external]` (https://developer.mozilla.org/en-US/docs/Glossary/CSS_pixel). Ver [[wiki/concepts/densidade-de-pixels]].
- **60% e 1.6rem dão 15,36 px, não 16.** A conta usual para `1.6rem` = 16 px é `62.5%` (10 px na raiz). A aula diz "faz um cálculo aqui de 1.6 do 60%" sem dar o número. Confiança alta (aritmética).
- **Mobile first é ordem de CSS, não só de foco.** Na prática, estilos base para o celular e `@media (min-width: ...)` para telas maiores. `[skill: tech-mentor-frontend]` A aula só anuncia o conceito; o dia 1 não tem media query. Ver [[wiki/concepts/mobile-first]].
- **`100vh` no celular** inclui a área sob a barra de endereço que some e volta. `100dvh` (ou `svh`) resolve `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/length#viewport-percentage_lengths). Em 2020 essas unidades não existiam.
- **Caminho com `/` depende do servidor.** Aberto com dois cliques (`file://`), `/style.css` aponta para a raiz do disco. É mais um motivo para o "nunca mais dois cliques", que a aula não explica. Inferência do agente.
- **"Self-closing"** em HTML se chama elemento vazio (*void element*): `img`, `link`, `meta`, `br` não têm conteúdo nem tag de fechamento `[external]` (https://developer.mozilla.org/en-US/docs/Glossary/Void_element).
- **Edge no Linux.** Saiu em versão estável em 2021; a fala é de 2020. "Mesmo motor" vale porque o Edge passou a usar o Chromium (e o V8) em 2020 `[external, não verificado]`.
- **`font` shorthand** também redefine o que não é dito (`line-height` volta a `normal`, `font-style`, `font-variant`). "Agrupamento dessas três propriedades" é incompleto `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/font).
- **Id repetido** deixa o HTML inválido; o CSS ainda pinta todos, mas `getElementById` devolve só o primeiro. "Vai dar certo" é só para o CSS.
- **Comentário em CSS** é `/* ... */`; "barra, asterisco, barra, asterisco" foi lapso de fala.

## Entidades

- [[wiki/entities/mayk-brito]]: instrutor, que se apresenta pelo nome
- [[wiki/entities/rocketseat]]: organizadora; Thiago, do layout, é "nosso colaborador aqui da Rocketseat"
- [[wiki/entities/next-level-week]]: o evento; o Proffy é o projeto da semana
- [[wiki/entities/vs-code]]: editor, Emmet, Live Server, color picker, atalhos
- [[wiki/entities/google-fonts]]: Poppins
- [[wiki/entities/figma]]: de onde saem as cores

Citados sem página: Thiago (designer do Proffy), Edge, Chrome, Notion (layout e imagens), Discord da NLW, YouTube, Twitter, Instagram e GitHub (exemplos), Google Tradutor, WinRAR.

## Conceitos

[[wiki/concepts/algoritmo]] · [[wiki/concepts/logica-de-programacao]] · [[wiki/concepts/arquitetura-cliente-servidor]] · [[wiki/concepts/url]] · [[wiki/concepts/http-vs-https]] · [[wiki/concepts/html-hipertexto]] · [[wiki/concepts/head-html-metadados]] · [[wiki/concepts/charset]] · [[wiki/concepts/texto-alternativo]] · [[wiki/concepts/ingles-para-desenvolvedores]] · [[wiki/concepts/setup-live-reload-debug-testes]] · [[wiki/concepts/css]] · [[wiki/concepts/seletores-css]] · [[wiki/concepts/especificidade-css]] · [[wiki/concepts/cascata-css]] · [[wiki/concepts/heranca-css]] · [[wiki/concepts/caminho-relativo]] · [[wiki/concepts/variaveis-css]] · [[wiki/concepts/sistema-hexadecimal]] · [[wiki/concepts/modelos-de-cor]] · [[wiki/concepts/unidades-de-medida-css]] · [[wiki/concepts/unidades-de-viewport]] · [[wiki/concepts/densidade-de-pixels]] · [[wiki/concepts/design-responsivo]] · [[wiki/concepts/mobile-first]] · [[wiki/concepts/box-model]] · [[wiki/concepts/shorthand-css]] · [[wiki/concepts/estilos-padrao-do-navegador-e-reset]] · [[wiki/concepts/display-css]] · [[wiki/concepts/flexbox]] · [[wiki/concepts/webfonts]] · [[wiki/concepts/peso-tipografico]]

## Open Questions

- A edição (#2) foi confirmada pelo usuário; a data (agosto de 2020) segue inferida pelo Proffy e pelo "dia 6, dia dos profissionais da educação" `[external, não verificado]`.
- O tema "launch base" do VS Code, também citado na NLW #1, segue sem confirmação.
- O código final do dia mostrado na aula não aparece na transcrição; os valores (`60%`, `1.6rem`, `90vw`, `700px`) vêm da fala.
- Comparado com o [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta|dia 1 da NLW #1]]: aqui `box-sizing: border-box` entra no reset desde o primeiro dia, e o mobile first é anunciado. Falta ver nos dias seguintes se as media queries do Proffy usam `min-width`, o que a NLW #1 nunca fez.

## Raw quotes

- "Afinal de contas, ser programador é resolver erros."
- "HTML não é programação, HTML é uma linguagem de marcação de hipertexto."
- "Nunca mais eu vou dar dois cliques nesse arquivo para abrir ele, nunca mais, tudo bem?"
- "Por causa de uma barra eu poderia estar dias descobrindo o porquê."
- "Todo e qualquer elemento HTML, quando trabalhado com o CSS, ele está sendo uma caixa."
