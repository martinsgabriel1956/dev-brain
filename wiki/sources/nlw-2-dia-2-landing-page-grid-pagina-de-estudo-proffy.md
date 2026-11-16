---
type: source
title: "NLW #2, dia 2: landing page responsiva com grid e página de estudo do Proffy"
aliases: ["NLW 2 dia 2", "Next Level Week 2 dia 2", "Proffy dia 2", "Proffy landing page e study"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [frontend, html, css, mobile-first, media-query, css-grid, grid-template-areas, flexbox, border-radius, transition, opacity, text-align, formulario-html, label, select, input, pseudo-elemento, focus-within, css-position, html-semantico, refatoracao, devtools, acessibilidade, rocketseat, proffy, iniciante]
skill: tech-mentor-frontend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy.md"
source_url: ""
author: "Mayk Brito"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #2, dia 2: landing page responsiva com grid e página de estudo do Proffy

## TL;DR

Segunda aula (cerca de 2h38) da [[wiki/entities/next-level-week|NLW #2]], de novo com [[wiki/entities/mayk-brito|Mayk Brito]] (chamado de "Mayk" e "Maykão" na fala; a transcrição automática dizia Mike, Michael, Maicão). A transcrição termina cortada ("que aman[hã]"). A aula faz duas telas do **Proffy**, cada uma primeiro para o celular e depois para o desktop.

- **Landing page.** O CSS vira `styles/main.css` + `styles/partials/page-landing.css`. Mobile: logo, hero image com `width: 100%`, dois botões (`a`) com `border-radius`, `:hover` e `transition`, e o "total de 200 conexões" com o coração. Desktop (`@media (min-width: 1100px)`): [[wiki/concepts/css-grid|grid]] com `grid-template-columns: 2fr 1fr 2fr`, `grid-template-rows: 350px 1fr`, `grid-template-areas` e `grid-area`, `gap`, `align-self` e `justify-self`. Entre 700 e 1100 px, a raiz passa a `62.5%`.
- **Página study.** `study.html` duplica o index: `header.page-header` com barra de topo (voltar + logo), título em `strong` e um [[wiki/concepts/formulario-html|formulário]] de filtros (`label`, `select` de matéria e dia da semana, `input type="time"`, botão `submit`). Depois `main` com `article.teacher-item` (avatar do GitHub de [[wiki/entities/diego-fernandes|Diego Fernandes]], descrição, preço por hora, botão de WhatsApp). O foco do input vira uma linha feita com `:focus-within::after` e `position: absolute` dentro de um pai `relative`. No desktop (`min-width: 700px`), os filtros vão para um grid `repeat(4, 1fr)` posicionado sobre a borda do header.

## Key Claims

### Revisão e organização

- **Revisão do dia 1:** head (meta, title, link, style), body, div sem significado semântico, h1–h6, p, a, img, box model, display por fora (block, inline) e por dentro (flex, grid).
- **Erro de digitação corrigido:** a variável estava escrita `--color-secundary` "com U"; Mayk corrigiu depois da aula, com ajuda de Camila, "nossa professora de inglês aqui na Rocketseat" (a transcrição dizia "Rocket City").
- **Reestruturar é livre:** "Você tem toda a liberdade no seu HTML de mudar ele quantas vezes forem necessárias, até que você atinja o layout que você deseja." Ver [[wiki/concepts/refatoracao]].
- **Emmet:** `.logo-container` + Tab gera `<div class="logo-container">`; `p.total-connections` gera o `p` com classe.
- **Pastas:** mover `style.css` para `styles/` quebra o link ("ele não vai achar porque agora não está nesse local"); vira `/styles/main.css` e `/styles/partials/page-landing.css`, "pra gente treinar bastante como que funciona navegar entre arquivos". Ver [[wiki/concepts/caminho-relativo]].
- **Landing page** é "essa página inicial, quando você entra num site".

### Landing page no celular

- **Raiz menor:** em `page-landing.css`, `:root { font-size: 40% }`: "as fontes já ficaram menores, isso vai ser muito legal pro nosso dispositivo mobile" (ver Tensões).
- **Logo:** `.logo-container img { height: 10rem }`, `text-align: center` e `margin-bottom: 3.2rem`. O `h2` ganha `font-weight: 500` (o navegador dá bold), `font-size: 3.6rem`, `line-height: 4.6rem` e `margin-top: 0.8rem`. "Diferente da altura somente height, que é a altura da caixa, line height é a altura da linha do texto." Ver [[wiki/concepts/altura-de-linha]].
- **text-align centraliza a imagem:** "o image ele vai herdar algumas propriedades [de texto]" (ver Tensões). Ver [[wiki/concepts/alinhamento-de-texto]].
- **Hero image:** `width: 100%` é 100% do pai, o `#container` com `90vw` e `max-width: 700px`. "O porcentagem, ele sempre tem que saber a base, a referência."
- **Ponto e vírgula esquecido:** o VS Code acusa o erro, mas na linha seguinte: "Ele não soube interpretar que o erro, na verdade, estava aqui."

### Botões

- **`a` com `href`:** `https://google.com` para mostrar o hyperlink; os dois botões vão para `/study` e `/give-classes`, que "ainda não existe[m]".
- **`.buttons-container`:** `display: flex; justify-content: center` e `margin: 3.2rem 0`. "Se eu não tiver o display flex, ele não vai funcionar."
- **Cada `a`:** `width: 30rem`, `height: 10.4rem`, `border-radius: 0.8rem`, `font: 700 2.4rem Archivo`, `display: flex; align-items: center; justify-content: center`, `text-decoration: none` (o sublinhado "o navegador coloca para a gente") e `color: var(--color-button-text)`.
- **border-radius:** mostrado com fundo vermelho e `2rem`. Com vários valores, os cantos seguem uma ordem, "meio que parecido aqui com o margin padding". Pôr raio em um canto só fica "como um desafio". Ver [[wiki/concepts/border-radius]].
- **Cores:** `.study` com `background: var(--color-primary-lighter)`; `.give-classes` com `var(--color-secondary)`. `background` é "a versão curta" de `background-color`. Ver [[wiki/concepts/variaveis-css]].
- **Margem que sobra:** o `margin-right: 1.6rem` dos dois desalinha o conjunto, porque o último "não tem nenhum elemento depois dele". Ele vê no DevTools (a faixa amarela) e zera a margem do `.give-classes`.
- **`:hover` + `transition: background 0.2s`:** o hover troca para `primary-light` e `secondary-dark`. "Um segundo é muito, eu quero só aquele detalhezinho." `transition` é shorthand de `transition-duration` e outras. Ver [[wiki/concepts/pseudo-classe-css]] e [[wiki/concepts/transition-e-transform-css]].
- **Ícones:** `img { width: 4rem; margin-right: 2.4rem }`.

### Total de conexões e Device Toolbar

- **`p.total-connections`** com "Total de 200 conexões já realizadas" e `purple-heart.svg`; `display: flex; align-items: center; justify-content: center` para pôr o coração "bem na linha" e o conjunto no meio.
- **Device Toolbar:** no DevTools, testar 320, 375, Moto G4, iPhone X e iPad. "Nós já temos uma landing page que já está tranquilo para os dispositivos mobile."

### Desktop com media query e grid

- **Media query** é "uma regra CSS que será aplicada somente quando ele cumprir certo padrão": `@media (min-width: 1100px)` vale "de 1100 pixels para cima". Ver [[wiki/concepts/breakpoint]].
- **Container:** acima de 1100, `max-width: 1100px` em vez dos 700. No DevTools, a 1099 px nada muda; a 1100 px, "Puf!", o layout alarga.
- **Aprender x entender:** "O aprendizado, ele é uma junção do seu tempo dedicado com a prática"; "na minha aula você está entendendo as coisas". Ver [[wiki/concepts/entender-vs-aprender]].
- **Grid:** "ele fatia pra gente no eixo Y [...] e pra cá, no eixo X". O Proffy usa três colunas e duas linhas: logo em uma coluna e imagem em duas; botões em duas e texto em uma. Ver [[wiki/concepts/css-grid]].
- **Colunas:** 33% cada não fica exato ("100% dividido por 3, com fração"); `fr` é "uma unidade de medida [...] chamada de frações"; px fixos (100, 300, 500) deixam sobra dentro do `max-width`. Fica `grid-template-columns: 2fr 1fr 2fr`.
- **Linhas:** `grid-template-rows: 350px 1fr`; a segunda "fica flexível" e cresce com o conteúdo.
- **Sem áreas, o grid se vira:** "o grid vai tentando se ajustar, pegando os caras que ele tem lá e colocar onde ele acha".
- **Áreas:** `grid-template-areas: "proffy image image" "button button texting"` e `grid-area` em `.logo-container`, `.hero-image`, `.buttons-container` e `.total-connections`.
- **DevTools mostra o grid** ao passar o mouse no container: as frações e os 350 px de altura.
- **gap: 60px.** No desktop ele usa px: "vai fazer mais sentido pixels porque ele vai ser uma coisa mais fixa mesmo". `column-gap` e `row-gap` separam os dois eixos.
- **Alinhamentos:** `text-align: initial` desfaz o center no logo; `.logo-container img { height: 100% }` "não está respeitando o grid" até `align-self: center` no item; `.buttons-container { justify-content: flex-start }` sobrescreve o center do flex; `.total-connections { justify-self: end }` é "o justify do grid". "Talvez fique um pouco confuso [...] se é o align do grid, se é o align do flex."

### Raiz em 62,5% e o bug da sobrescrita

- **62,5%:** acima de 700 px, `:root { font-size: 62.5% }`, porque "o font-size padrão dos navegadores é de 16 pixels", então "1rem equivale a 10 pixels" (0.8rem = 8 px, 2.4rem = 24 px).
- **Por que estava riscado:** no DevTools o `62.5%` aparece riscado. A causa era o `:root` sem media query, deixado "já pra começar", que "pega e sobrescreve o outro que não deveria". A solução foi pôr esse root dentro de `@media (max-width: 699px)` (ver Tensões e [[wiki/concepts/cascata-css]]).
- **Ajustes finos contra o Figma** (layout de Thiago, 1440 × 820): botões sem margem no desktop, gaps de 86–87 px no Figma ("não precisa dessa minúcia toda"), `.total-connections` em 1.2rem, `height` fixo de 127 px no logo e 350 px na ilustração, `margin: 0` no logo.

### Página study: estrutura

- **Duplicar o index:** copiar `index.html` como `study.html` e trocar `landing` por `study` com Ctrl+D (seleciona a próxima ocorrência), três vezes.
- **Blocos:** "a gente pode pensar como se fosse blocos de montagem da nossa página". `header.page-header` > `.top-bar-container` com `a href="/"` (a barra "significa que ele vai voltar pra página inicial") com `back.svg`, e o logo.
- **`.header-content`** com `strong` ("já vem com o bold") "Esses são os proffys disponíveis" e o `form#search-teachers` (a transcrição dizia "search features"). O `action` fica para o back-end.
- **label:** "ajuda visualmente" e "vai ajudar muito a acessibilidade"; liga-se ao campo pelo `for`, que segundo a aula procura "o name igual o for" (ver Tensões).
- **name e id:** o `id` é para JavaScript e CSS; o `name` é o que o back-end recebe no envio: "se a gente não tiver um name muito bem certinho [...] eu não consigo depois no back-end pegar".
- **select e option:** cada `option` tem `value` (Artes = 1, Física = 5); a primeira, sem valor, é `disabled` e serve de "selecione uma opção". Ver [[wiki/concepts/formulario-html]].
- **label é inline:** no DevTools, aba Computed, filtro display: "ele já vem com o display inline padrão".
- **input:** "fecha automaticamente nela mesmo", com ou sem barra no fim. `type="number"` recusa letras, `min="0"` e `max="24"`; `type="text"` aceita tudo; `type="time"` mostra hora e minuto.
- **Botão submit:** dentro do `form`, envia o formulário. Sem `action`, "esse algum lugar é a própria página": a página recarrega e os dados aparecem na URL.
- **Pastas, de novo:** "muitos erros que eu vejo os alunos cometendo [...] o aluno não colocou dentro da pasta partials".

### Página study: CSS mobile

- **Container da página:** `width: 100vw` e `height: 100vh` ("todo espaço visível").
- **Header:** `background: var(--color-primary)`, `display: flex; flex-direction: column` ("é importante eu deixar esse flex aqui, porque mais para frente eu consigo fazer modificações").
- **Top bar:** `width: 90%`, `display: flex; align-items: center; justify-content: space-between` ("between significa entre"), `margin: 0 auto`, `padding: 1.6rem 0`, logo com `height: 1.6rem`, link com `height: 3.2rem`.
- **Opacidade:** vai de 0 a 1; `transition: opacity 0.2s` e `:hover { opacity: 0.6 }`: "parece que ele tá tipo dando uma respirada".
- **Título:** `font: 700 3.6rem Archivo`, `color: var(--color-title-in-primary)`, `line-height: 4.2rem` (com 8 rem dá para ver a diferença).
- **Ponto e vírgula:** o último não é obrigatório, "mas a minha dica é [...] coloca ponto e vírgula em tudo".
- **Botão de busca:** `width: 100%`, `height: 5.6rem`, verde `secondary`, `border: 0`, `border-radius`, `cursor: pointer` ("ele é a mãozinha"), flex centralizado e `:hover` mais escuro.
- **Campos:** `label` com `font-size: 1.4rem` e `color-text-complement`; `input` e `select` com `width: 100%`, `height: 5.6rem`, fundo, `border: 1px solid` e `outline: 0`.
- **Outline:** tirar "não é uma prática muito, muito adequada, porque a gente precisa desse outline de uma maneira visual pra ajudar quem precisa de acessibilidade". A compensação vem a seguir. Ver [[wiki/concepts/indicador-de-foco]].
- **`.input-block:focus-within::after`:** quando o input interno está em foco, o CSS cria um pseudo-elemento ("o CSS vai criar um elemento HTML aqui"), com `content: ''` obrigatório, `width: calc(100% - 3.2rem)`, `height: 2px` e `background: var(--color-primary-light)`. "Isso é um avanço CSS maravilhoso [...] a gente tinha que fazer essas ideias todas com JavaScript." Ver [[wiki/concepts/pseudo-elemento-css]].
- **`position: absolute`:** "uma folha de papel nova em cima da folha de papel antiga", absoluto "na página inteira" até o pai ganhar `position: relative`; então `bottom: 0; left: 1.6rem` põe a linha sob o campo. Ver [[wiki/concepts/css-position]].
- **No select não precisa:** "quando a gente clica nele automaticamente ele abre", "de maneira visual a gente já tá tranquilo".
- **Descansos:** ele passa a pedir pausas de cinco minutos.

### Card do professor

- **Semântica:** `main` é "o conteúdo principal da página"; `article` é "um tipo de conteúdo que vai se repetir aqui várias vezes", com `header`, `p` e `footer`. Ver [[wiki/concepts/html-semantico]].
- **Avatar:** copiar o link da imagem do perfil do GitHub (Copy Image Link). `alt="Diego Fernandes"`. Ver [[wiki/entities/github]].
- **Classe em vez de tag:** `.teacher-item` em vez de `article`, porque outro `article` na página "poderia ter algum problema". Alt + clique cria vários cursores.
- **Header do card:** `padding: 3.2rem 2rem`, flex com `align-items: center`; a imagem vira "bolinha" com `width` e `height` iguais (8rem) e `border-radius: 50%`, mas só "quando essa imagem é um quadrado perfeito".
- **margin-top em inline não vale:** o `span` com a matéria só aceita `margin-top` com `display: block`; "quando ele é inline ele não aceita". O `strong` do nome também vira block. Ver [[wiki/concepts/display-css]].
- **Footer do card:** `background: var(--color-box-footer)`, `border-top`, flex com `space-between`; preço em `strong` block para não quebrar feio a 320 px.
- **Botão do WhatsApp:** `width: 20rem`, `height: 5.6rem`, `justify-content: space-evenly` ("os espaçamentos [...] são meio que constantes"), `transition` e hover `secondary-dark`.

### Página study no desktop

- **`@media (min-width: 700px)`:** `#page-study` com `max-width: 100vw`; header e footer do card com `padding: 32px`.
- **Filtros em grid:** `grid-template-columns: repeat(4, 1fr)` ("quando tudo no grid as colunas forem iguais") e um espaço de 16 px entre as colunas; o form vira `position: absolute; bottom: -28px` dentro do `.header-content`, que recebe `position: relative`.
- **Header:** `height: 340px`; top bar com `max-width: 1100px`; `.header-content` com `max-width: 740px`, `flex: 1 1`, `padding-bottom: 48px`, `display: flex; flex-direction: column; justify-content: center` e `margin: 0 auto`. O título ganha `max-width: 350px` para quebrar a linha.
- **`flex: 1 1`** parecia não fazer nada; "agora você consegue ver toda a diferença".
- **main:** `padding: 32px 0`, `max-width: 740px`, `margin: 0 auto`. "Vou pegar o main aqui e vou tirar o padding pra ver o que acontece": é "assim que você vai também tirando suas dúvidas".
- **Margem que empurrava o after:** `select-block { margin-bottom: 0 }`.
- **Preço em linha de novo:** `display: initial` e `margin-left: 16px`.
- **Filho direto:** `.teacher-item > p` em vez de `.teacher-item p`, porque o padding pegava também o `p` do footer: "eu coloco uma setinha assim". Ver [[wiki/concepts/seletores-css]].
- **Botão final:** `width: 245px`, `font-size: 16px`, `justify-content: center` e `img { margin-right: 16px }`.
- **font-weight 600:** o Archivo foi importado só em 400 e 700; pôr 600 no import muda "tão ínfima" a forma que "não vale a pena". Ver [[wiki/concepts/peso-tipografico]] e [[wiki/entities/google-fonts]].

## Tensões e precisões

- **`for` aponta para o `id`, não para o `name`.** O `<label for>` liga-se ao elemento cujo `id` é igual ao valor do `for` `[external]` (https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label). Na aula funciona porque `id` e `name` têm o mesmo valor (`subject`, `weekday`, `time`). Com id diferente, o clique no label e o nome lido pelo leitor de tela param de funcionar. Confiança alta.
- **Raiz em 40% deixa o texto pequeno demais.** 40% de 16 px dá 6,4 px; o corpo com `1.6rem` fica em cerca de 10 px no celular. `[skill: tech-mentor-frontend]` A base recomendada é 16 px e a raiz em `100%`, para respeitar a fonte que o usuário escolheu. No iOS, `input` com fonte abaixo de 16 px faz o Safari dar zoom ao focar `[external, não verificado]`. Pelo ajuste dos 700 px, o `main.css` usa 60% até 699 px; a transcrição não deixa claro se o 40% da landing continuou. Confiança média.
- **Media query não dá força.** O `62.5%` riscado é cascata: regras de mesma especificidade, e a que vem depois vence, esteja ou não dentro de `@media`. A correção (pôr o root sem condição dentro de `max-width: 699px`) funciona, mas o motivo é a ordem, e mover a regra incondicional para antes da media query também resolveria. Ver [[wiki/concepts/cascata-css]]. Confiança alta.
- **62,5% = 10 px só com o padrão de 16 px.** Se o usuário aumentar a fonte do navegador, 1rem cresce junto, e é esse o ponto de usar % e não px. "1rem equivale a 10 pixels" é verdade só no padrão. Confiança alta.
- **text-align centraliza a img porque ela é inline, não porque herda.** `img` é um elemento inline (substituído) e fica na linha de texto do bloco; `text-align` alinha o conteúdo inline das linhas `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/text-align). A `text-align` é herdada, mas isso não explica a imagem. "Vai herdar a largura do pai" no `width: 100%` também não é herança: porcentagem de largura é calculada contra o bloco que contém. Ver [[wiki/concepts/heranca-css]].
- **`::after` não é um elemento HTML.** É um pseudo-elemento: não entra no DOM, o JavaScript não o seleciona e o conteúdo dele não é confiável para leitores de tela `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/::after). "Todo elemento HTML precisa ter um conteúdo" vale para o `content` de pseudo-elementos, não para elementos HTML (`<div></div>` vazio é válido). Confiança alta.
- **Select sem indicador de foco.** A linha do `:focus-within::after` foi feita só no `.input-block`. Os `select` também ficaram com `outline: 0` e sem substituto; "quando a gente clica nele automaticamente ele abre" vale para o mouse, não para quem navega com Tab. Isso falha no critério 2.4.7 (Focus Visible) da WCAG `[external]` (https://www.w3.org/WAI/WCAG22/Understanding/focus-visible). `[skill: tech-mentor-frontend]` Usar `:focus-visible` e manter um outline próprio. Ver [[wiki/concepts/indicador-de-foco]]. Confiança alta.
- **"Absoluto na página inteira" e "novo contexto".** Um elemento absoluto se posiciona pelo ancestral posicionado mais próximo (o primeiro com `position` diferente de `static`); sem nenhum, pelo bloco inicial, que tem o tamanho da viewport. `position: absolute` sozinho, sem `z-index`, não cria contexto de empilhamento `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Understanding_z-index/Stacking_context). A "folha de papel" serve como imagem, mas "contexto" não é o termo técnico.
- **`align-self` não "prende" o conteúdo.** Ele alinha o item dentro da área do grid no eixo das linhas; o padrão `stretch` estica o item até a altura da linha. Que a imagem com `height: 100%` "saiu do grid" e voltou com `center` tem a ver com como a porcentagem de altura é resolvida, que a aula não explica. Inferência do agente; confiança média.
- **`rem` "nunca é fixo, ele é fluido".** `rem` é relativo à fonte da raiz, não ao tamanho da tela. Ele só muda quando uma media query muda a raiz, o que esta aula de fato faz em 700 px. Mesma imprecisão do [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy|dia 1]].
- **Font-size em px no desktop.** `font-size: 16px` no botão do card (dentro da media query) volta a ignorar a preferência de fonte do usuário. Para gap e padding, px é inofensivo. `[skill: tech-mentor-frontend]`
- **`justify-content` não exige flex.** Funciona também em grid (e, desde a especificação de alinhamento, em multicoluna). "Se eu não tiver o display flex, ele não vai funcionar" vale para o caso da aula, que usa `display: block` como alternativa.
- **space-evenly:** espaços iguais entre os itens e também nas pontas; "constante" é uma boa leitura.
- **Formulário sem `action`** envia para a própria URL com `method="get"` por padrão, por isso os campos aparecem na query string. Ver [[wiki/concepts/query-string]].
- **Peso 600 não importado.** Sem o arquivo, o navegador usa o peso mais próximo ou sintetiza um negrito, o que explica a diferença "ínfima".
- **Mobile first agora é de fato.** Os estilos base são do celular e as telas maiores usam `min-width` (700 e 1100 px). Isso responde à pergunta aberta do dia 1; a exceção é o `:root` em `max-width: 699px`, que está ali só para corrigir a ordem da cascata.

## Entidades

- [[wiki/entities/mayk-brito]]: instrutor
- [[wiki/entities/next-level-week]]: NLW #2, projeto Proffy
- [[wiki/entities/rocketseat]]: organizadora; Camila, professora de inglês (a transcrição dizia "Rocket City")
- [[wiki/entities/diego-fernandes]]: avatar e nome de exemplo no card do professor
- [[wiki/entities/github]]: de onde sai o link do avatar
- [[wiki/entities/vs-code]]: Emmet, Ctrl+D, Alt + clique, Ctrl+F, Alt+Z, avisos de sintaxe
- [[wiki/entities/figma]]: layout de Thiago, medidas e espaçamentos
- [[wiki/entities/google-fonts]]: Archivo (400 e 700) e Poppins

Citados sem página: Camila (professora de inglês da Rocketseat), Thiago ("Thiagão", designer do Proffy), Google (exemplo de link), Notion (onde fica o código), WhatsApp (botão do card).

## Conceitos

[[wiki/concepts/refatoracao]] · [[wiki/concepts/caminho-relativo]] · [[wiki/concepts/mobile-first]] · [[wiki/concepts/unidades-de-medida-css]] · [[wiki/concepts/breakpoint]] · [[wiki/concepts/css-grid]] · [[wiki/concepts/flexbox]] · [[wiki/concepts/alinhamento-de-texto]] · [[wiki/concepts/altura-de-linha]] · [[wiki/concepts/border-radius]] · [[wiki/concepts/variaveis-css]] · [[wiki/concepts/pseudo-classe-css]] · [[wiki/concepts/transition-e-transform-css]] · [[wiki/concepts/cascata-css]] · [[wiki/concepts/heranca-css]] · [[wiki/concepts/formulario-html]] · [[wiki/concepts/query-string]] · [[wiki/concepts/indicador-de-foco]] · [[wiki/concepts/acessibilidade]] · [[wiki/concepts/pseudo-elemento-css]] · [[wiki/concepts/css-position]] · [[wiki/concepts/html-semantico]] · [[wiki/concepts/display-css]] · [[wiki/concepts/seletores-css]] · [[wiki/concepts/peso-tipografico]] · [[wiki/concepts/entender-vs-aprender]]

## Open Questions

- O `:root { font-size: 40% }` da landing ficou no código final? A fala não deixa claro qual root foi movido para o `max-width: 699px`.
- A transcrição acaba no meio de "amanhã"; o conteúdo do dia 3 não está aqui.
- Desafios deixados: `border-radius` em um canto só e o select "ativado" do layout (com a linha de foco), que "não vamos construir nessa semana".
- Os nomes `texting` e `proffy` nas áreas do grid vêm da fala; o código publicado no Notion não está na transcrição.

## Raw quotes

- "Você tem toda a liberdade no seu HTML de mudar ele quantas vezes forem necessárias."
- "O aprendizado, ele é uma junção do seu tempo dedicado com a prática."
- "Isso não é uma prática muito, muito adequada, porque a gente precisa desse outline."
- "Eu insisto em colocar como se fosse classe."
- "Não precisa dessa minúcia toda, tá, gente?"
