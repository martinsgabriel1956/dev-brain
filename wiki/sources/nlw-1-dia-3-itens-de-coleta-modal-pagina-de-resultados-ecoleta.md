---
type: source
title: "NLW #1, dia 3: itens de coleta, modal de busca e página de resultados no Ecoleta"
aliases: ["NLW 1 dia 3", "Next Level Week 1 dia 3", "Ecoleta itens de coleta", "Ecoleta modal de busca"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [frontend, html, css, javascript, css-grid, flexbox, modal, data-attributes, classlist, array, findindex, filter, pointer-events, z-index, object-fit, acessibilidade, lang-dynamic, rocketseat, ecoleta, iniciante]
skill: tech-mentor-frontend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta.md"
source_url: ""
author: "Mayk Brito"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #1, dia 3: itens de coleta, modal de busca e página de resultados no Ecoleta

## TL;DR

Terceira aula (cerca de 1h55) da [[wiki/entities/next-level-week|Next Level Week #1]] da [[wiki/entities/rocketseat]]. Desta vez a autoria aparece na fala: "Mayk Brito na área" ([[wiki/entities/mayk-brito]]). A aula continua o [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta|dia 2]] e tem quatro partes:

1. **Correções na página de cadastro.**
   - Limpa as cidades ao trocar de estado, o bug que o dia 2 deixou.
   - Guarda o nome da cidade em vez do id.
   - Marca os campos com `required`.
2. **Os itens de coleta.**
   - Seis itens num [[wiki/concepts/css-grid|grid]] de três colunas, cada um com o id num [[wiki/concepts/atributos-data-html|atributo `data-id`]].
   - Um clique liga e desliga a classe `selected` com [[wiki/concepts/classlist-javascript|`classList.toggle`]].
   - `pointer-events: none` na imagem e no texto faz o clique sempre chegar ao `li`.
   - Um [[wiki/concepts/algoritmo|algoritmo]] escrito primeiro em comentários e depois em código: `findIndex`, `filter` e `push` sobre um [[wiki/concepts/array]]. O resultado vai para um `input hidden` chamado `items`.
3. **Um [[wiki/concepts/modal|modal]] de busca na home.**
   - Uma `div` com `position: fixed`, fundo em hexadecimal com transparência e uma classe `hide` (`display: none`).
   - JavaScript tira e põe essa classe para abrir e fechar.
4. **A página `search-results.html`.**
   - Cards num grid, com imagens do [[wiki/entities/unsplash]] e `object-fit: cover`.
   - Uma faixa de fundo feita com `body::after` e `z-index: -1`.
   - Uma coluna só abaixo de 900 px.

Fecha com o `action` do formulário de busca, uma "pitadinha" do back-end que vem depois.

## Key Claims

### Abertura: por que JavaScript

- **Sem guerra de tecnologia:** "não faz sentido a gente ficar discutindo tecnologia qual é melhor, todas têm as suas vantagens e desvantagens".
- **Critérios de escolha:** oportunidades de mercado, o momento da carreira, o contexto onde a tecnologia é usada e o alinhamento com os seus objetivos.
- **Na web, "não tem como fugir do JavaScript":** é "a linguagem que os navegadores entendem" e está por trás de [[wiki/entities/nodejs|Node]], [[wiki/entities/react|React]] e React Native.

### Corrigindo o dia 2

- **Cidades acumuladas.** Ao trocar de Rondônia para Roraima, as cidades de Rondônia continuavam no select. Mayk chama de bug "de lógica", que "pode causar um pouco de confusão" mas não quebra a aplicação.
  - **A correção:** antes do `fetch`, o select de cidade volta a ter só `<option value="">Selecione a cidade</option>` e fica `disabled` de novo.
  - **Por que antes do `fetch`:** a limpeza fica antes da chamada, e não na resposta. Se a resposta não chegar, o estado mudou mas as cidades seriam "do estado antigo". Ver [[wiki/concepts/debugging]].
- **Cidade pelo nome:** o `value` da option passa de `city.id` para `city.nome`, porque "no banco de dados eu vou querer guardar o nome da cidade".
- **`required`** em todos os inputs e nos dois selects. Com isso o navegador bloqueia o envio e mostra "por favor, preencha esse campo". Mayk se corrige ao vivo: "não é uma tag desculpa é um atributo". Ver [[wiki/concepts/formulario-html]].

### Itens de coleta: HTML

- **A estrutura:** um novo `fieldset` com `legend` > `h2` "Itens de coleta" e uma `div.items-grid` com seis `li`. Cada `li` tem uma `img` (SVG de `assets`, com `alt` igual ao nome) e um `span` com o nome: lâmpadas, pilhas e baterias, papéis e papelão, resíduos eletrônicos, resíduos orgânicos e óleo de cozinha.
- **Por que não `id="1"`:** "não é muito legal a gente deixar números" num `id`. Mayk usa `data-id="1"`, "um tipo de atributo especial do HTML": `data-` mais qualquer nome, e "a gente chama isso aqui de data set". Ver [[wiki/concepts/atributos-data-html]] e a seção de tensões.
- **Atalho do VS Code:** Ctrl+D seleciona a próxima ocorrência, e a edição vale para as duas ao mesmo tempo. Ver [[wiki/entities/vs-code]].

### Itens de coleta: CSS

- **Grid x flex:** o grid é "multidimensional, consigo criar linhas e colunas"; o flex é "unidimensional", ou tudo ao lado ou tudo abaixo. Ver [[wiki/concepts/css-grid]] e [[wiki/concepts/flexbox]].
- **`grid-template-columns`:**
  - `200px 200px 200px` dá três colunas fixas.
  - Com `800px` no meio, a coluna passa da tela.
  - `1fr 1fr 1fr` são frações: ele "vai fazer cálculos" para encaixar três colunas e joga os itens seguintes para a linha de baixo.
- **`gap: 16px`:** separa só entre os itens. Com `margin`, seria preciso tirar a margem das bordas, "um trabalho um pouco complexo".
- **O `li`:**
  - `list-style: none` tira "os bullets".
  - `border: 2px solid #f5f5f5`, `height: 180px`, `border-radius: 8px` e `padding: 32px 24px 16px`.
  - `display: flex; flex-direction: column; align-items: center; justify-content: space-between`. Com `column`, o `space-between` passa a agir na vertical: "como eu inverti o fluxo".
  - `text-align: center` e `cursor: pointer`, "a mãozinha".
- **O `span`:** `flex: 1` para "preencher o espaço" que a imagem deixou, mais `display: flex` e `align-items: center` para centralizar o texto na vertical. Leva `color: var(--title-color)` e `margin-top: 12px`.
- **`.items-grid li.selected`, sem espaço:** "procura dentro do items grid o li que tenha a classe selected". Com espaço, seria um elemento com `selected` dentro do `li`: "o tal do typo". Recebe fundo verde-claro (ditado "e1fac"; ver tensões) e `border: 2px solid #34cb79`.

### Itens de coleta: JavaScript

- **Um ouvidor para cada item:** `document.querySelectorAll(".items-grid li")` vai para `itemsToCollect`, e `for (const item of itemsToCollect)` liga `addEventListener("click", handleSelectedItem)` em cada um. Repetir a linha seis vezes funcionaria, mas não escala se a lista crescer. Ver [[wiki/concepts/event-listener-javascript]].
- **O alvo errado:** clicar na imagem ou no texto faz o `event.target` ser a `img` ou o `span`, porque o filho também recebe o clique (o "elemento pai e elemento filho"). A correção é no CSS: `pointer-events: none` em `.items-grid li img, .items-grid li span`, e "o target sempre será o li". Ver a seção de tensões.
- **`event.target.dataset.id`** lê o `data-id` ("o s é menorzinho"), guardado em `itemId`.
- **`classList`:** `add`, `remove` e `toggle`, que "olha lá o elemento" e põe ou tira a classe. Mayk pronuncia "togo" e soletra "t-o-g-g-l-e". Ver [[wiki/concepts/classlist-javascript]].

### O algoritmo da seleção

- **O problema:** a seleção era "só de uma maneira visual". Enviando o formulário, nenhum campo dizia quais itens estavam marcados. A saída é a mesma do estado no dia 2: um `<input type="hidden" name="items">`.
- **Primeiro em português, como comentários:**
  1. Verificar se existem itens selecionados e, se sim, pegá-los.
  2. Se o item já estiver selecionado, tirar da seleção.
  3. Se não estiver, adicionar à seleção.
  4. Atualizar o campo escondido.

  "Isso aqui chama-se algoritmo de programação." Ver [[wiki/concepts/algoritmo]].
- **`let selectedItems = []`** fica fora da função. É `let` porque vai ser reatribuído: "se eu deixasse ele como const, eu não ia conseguir sobrescrever esses valores". Ver [[wiki/concepts/var-let-const]].
- **`findIndex`:** recebe uma função que devolve verdadeiro ou falso (`const itemFound = item == itemId; return itemFound`) e roda "até que ele ache uma coisa verdadeira". Devolve o índice ou `-1`, o que ele mostra no console clicando nos itens. A condição pode ser `alreadySelected >= 0` ou `!= -1`. Ele fica com `>= 0` "para a clareza". Ver [[wiki/concepts/array]] e [[wiki/concepts/igualdade-javascript]].
- **`filter`:** monta um array novo com os itens para os quais a função devolve `true`, e o que dá `false` "tem que ser filtrado". A função é `const itemIsDifferent = item != itemId`. Depois vem a reatribuição `selectedItems = filteredItems`.
- **`push`** adiciona no `else` ("Elsie", na transcrição automática).
- **A arrow function enxuta:** `item => item == itemId` é mostrada e depois desfeita. "Eu acho legal para a gente que está começando deixar ele de uma maneira muito mais explícita." Ver [[wiki/concepts/funcoes-javascript]].
- **Campo escondido:** `collectedItems.value = selectedItems`. O `querySelector('input[name=items]')` fica fora da função para não buscar o elemento "toda hora". O DevTools mostra `4,6,2`. Enviado por GET, a vírgula vira `%2C` na URL, e "a gente vai, então, configurar [...] lá atrás do back-end".

### O modal de busca

- **Modal:** "quando eu clico aqui ele vai abrir só uma janela [...] dentro dessa própria página sem sair da página". Ver [[wiki/concepts/modal]].
- **HTML** no `index.html`:
  - `div#modal` > `div.content` > `div.header` (`h1` "Pontos de coleta" + `a` "Fechar") e um `form`.
  - No form, `label for="search"`, `div.search.field` com `input type="text" name="search"` e um `button` com `img alt="Buscar"`.
  - Ele troca os dois campos do Figma (cidade e estado) por um só e põe o botão ao lado: "espero que me perdoem especialmente quem construiu layout".
- **Label em vez de texto por dentro:** o layout tinha só o texto dentro do campo, e Mayk põe um `label` porque, para acessibilidade, esse texto "não consegue ser lido pelos leitores". Depois mostra o `placeholder="Pesquise por cidade"`. Ver [[wiki/concepts/acessibilidade]] e as tensões.
- **Dúvida da turma:** o `responsive.css` vem por último, senão as regras seguintes "sobrescrevem". Ver [[wiki/concepts/cascata-css]].
- **`modal.css`:**
  - `height: 100vh; width: 100vw`.
  - Fundo `#0e0a14` com dois dígitos a mais de alfa ("vai de zero até F"; `ff` é cor cheia, `00` some). Ver [[wiki/concepts/sistema-hexadecimal]].
  - `position: fixed; top: 0` cria "um novo contexto" por cima e trava o scroll da página. Ver [[wiki/concepts/css-position]].
  - `display: flex`, centralizado nos dois eixos, e `transition: 400ms`.
- **O conteúdo:**
  - `.content` com `color: white` e `width: 420px` ("você já sabe adicionar um media query").
  - Header em flex com `space-between`, e o `h1` com 36/42 px e `margin-bottom: 48px` no header.
  - O `a` mostra o `x.svg` como `background-image` em 20×20 com `display: flex`.
  - O texto "Fechar" fica com `font-size: 0.01px`: invisível, mas presente "por acessibilidade", já que o leitor "não vai conseguir ler o x".
- **Formulário do modal:**
  - O `label` em `display: block` para aceitar `margin-bottom`: "o display do label é inline ele não pega". Ver [[wiki/concepts/display-css]].
  - O `.field` em flex.
  - O input com `flex: 1`, fundo `#f0f0f5` ("um forte candidato a ser uma variável"), `border: 0`, `padding: 16px 24px` e `border-radius: 8px 0 0 8px`.
  - O botão com 72×72 px, `var(--primary-color)`, `border-radius: 0 8px 8px 0` (sentido horário, para o botão ter "uma cara como se ele tivesse grudado" no input) e `:hover` mais escuro.
- **Abrir e fechar:**
  - `#modal.hide { display: none }`, de novo sem espaço entre id e classe.
  - No `index.js`, o botão `#page-home main a` faz `modal.classList.remove("hide")`, e o `#modal .header a` faz `add("hide")`.
  - Dois bugs ao vivo. Primeiro, `querySelectorAll` devolve uma lista, e "não consigo colocar numa lista o add event listener". Segundo, o `href` vazio recarregava a página, corrigido com `href="#"`. Ver [[wiki/concepts/dom]] e [[wiki/concepts/debugging]].

### A página de resultados

- **HTML:**
  - Cópia de `create-point.html` com `id="page-search-results"` e `main` no lugar do form. Não tem JavaScript.
  - Um `h4` com `<strong>2 pontos</strong> encontrados`.
  - `div.cards` > `div.card` com `img` (imagens de reciclagem do [[wiki/entities/unsplash]], coladas por URL), `h1` "Colectoria", `h3` com os tipos de resíduo e um `p` de endereço quebrado com `<br>`.
- **CSS:**
  - Cópia do CSS do create-point, renomeada com o localizar e substituir (Ctrl+F) do [[wiki/entities/vs-code]].
  - `.cards` em grid `1fr 1fr 1fr` com `gap: 24px`.
  - A imagem com `height: 150px` e `border-radius: 8px 8px 0 0`.
  - O `font-weight: normal` do `h4` não pega na Ubuntu, que só tem o peso 700 carregado, e ele troca para Roboto.
  - Cores e tamanhos copiados do painel de inspeção do [[wiki/entities/figma]], exceto o posicionamento absoluto, "uma parada muito absoluta".
- **A faixa de fundo:**
  - `body::after { content: ""; position: fixed; ... }` cria um elemento que "o CSS está criando não existe na página". Ver [[wiki/concepts/pseudo-elemento-css]].
  - Esticado com top, right, left e bottom, ele fica por cima de tudo. Com `z-index: -1` vai para trás: "uma terceira dimensão que é a profundidade que é o eixo z", e a imagem é a das folhas de papel do dia 1. Ver [[wiki/concepts/css-position]].
  - A altura sai no chute até 260 px.
- **Responsivo:**
  - Dentro do `max-width: 900px`, os cards passam a `grid-template-columns: 1fr` e a imagem a 200 px de altura.
  - `object-fit: cover` faz a imagem "preencher todo o espaço" em vez de esticar.
  - O `main` ganha margem de 48 px também embaixo.
- **Links e action:**
  - Os `href` que ainda apontavam para o Google viram `/`, que funciona "como eu estou rodando pelo servidor" (Live Server). Sem ele, o caminho tem que ser `index.html`.
  - O form do modal ganha `action="/search-results"`.
  - "Não precisou nem de back end até agora": o protótipo navegável serve para apresentar "para um cliente".

### Atitude

- **"Bugs são erros na aplicação [...] a gente sempre tem bugs em nossas aplicações é normal."**
- **Revisão guiada:** Mayk passa por cada arquivo alterado, desliga o minimapa do VS Code e pede: "seja criativo [...] faça algo que chame a nossa atenção".

## Tensões e precisões

- **`li` fora de lista.** Os seis `li` ficam direto numa `div.items-grid`. O `li` só é válido dentro de `ul`, `ol` ou `menu` `[external]` (https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li). A semântica de lista que ele cita ("tags li para semântica de lista") só existe com o `ul` em volta. Melhor ainda seriam checkboxes, que dão foco, teclado e envio pelo próprio form sem JavaScript.
- **Itens só respondem ao mouse.** Um `li` com evento de clique não recebe foco nem responde a Enter ou Espaço. Quem usa teclado ou leitor de tela não consegue selecionar os itens. `[skill: tech-mentor-frontend]` Use `<input type="checkbox">` estilizado com `:checked`, ou `button` com `aria-pressed`. Ver [[wiki/concepts/acessibilidade]].
- **`pointer-events: none` resolve no CSS um problema de JavaScript.** `event.currentTarget` (o elemento onde o ouvidor foi registrado) ou `event.target.closest("li")` dão o `li` sem mudar o CSS `[external]` (https://developer.mozilla.org/en-US/docs/Web/API/Event/currentTarget). Ver [[wiki/concepts/event-listener-javascript]].
- **`==` e `===` não são "tanto faz".** Mayk diz que "há uma diferença [...] que não nos cabe entender agora" e usa `==`. O `==` converte tipos antes de comparar (`"1" == 1` é `true`), e o `===` não `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness). Aqui funciona porque `dataset.id` e os itens do array são strings. É o mesmo padrão do "tanto faz" de var/let/const no dia 2. Ver [[wiki/concepts/igualdade-javascript]].
- **`id` numérico é válido.** Em HTML5, `id="1"` é permitido. O problema fica no seletor CSS, que precisa de escape (`#\31`) `[external]` (https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id). Ainda assim, `data-id` é a escolha certa para um dado que o JavaScript lê. Ver [[wiki/concepts/atributos-data-html]].
- **O modal não é acessível.**
  - É uma `div` sem `role="dialog"`, sem mover o foco para dentro, sem fechar com Esc e sem bloquear o resto da página.
  - O "Fechar" é um `<a href="#">` fazendo papel de botão.
  - `[skill: tech-mentor-frontend]` O `<dialog>` com `showModal()` já dá a camada superior, o `inert` no resto da página, o foco preso e o Esc; o `::backdrop` substitui o fundo semitransparente. Ver [[wiki/concepts/modal]].
- **`font-size: 0.01px` para esconder texto** é frágil: o navegador pode arredondar o tamanho ou aplicar um tamanho mínimo de fonte. O padrão para texto só de leitor de tela é a classe "visually hidden" (`clip`/`clip-path`, 1 px, `overflow: hidden`). Num `<button>`, um `aria-label="Fechar"` também resolve `[external]` (https://www.a11yproject.com/posts/how-to-hide-content/).
- **`transition: 400ms` no modal não anima nada.** O modal aparece e some trocando `display`, que é uma propriedade discreta. `[skill: tech-mentor-frontend]` Para animar a entrada é preciso `@starting-style` com `transition-behavior: allow-discrete`, ou animar `opacity`.
- **O placeholder e os leitores de tela.** "Não consegue ser lido pelos leitores" é impreciso: a maioria dos leitores anuncia o placeholder. Mesmo assim ele não substitui o label, porque some ao digitar e costuma ter pouco contraste `[external]` (https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#placeholder). A decisão de pôr o label está certa.
- **O `label for` continua sem `id`.** `<label for="search">` aponta para um input que só tem `name="search"`, o mesmo problema do dia 2. Ver [[wiki/concepts/formulario-html]].
- **Os títulos dos cards.** Cada card tem um `h1`, e o `h4` da contagem vem antes deles. Isso quebra a hierarquia de títulos usada por quem navega com leitor de tela. O `h1` deveria ser o título da página e os cards ficariam com `h2`. Ver [[wiki/concepts/html-semantico]].
- **Detalhes menores:**
  - **Duplo clique** seleciona a palavra, não "a linha inteira".
  - **`cursor: pointer`** só vem de fábrica no `a` que tem `href`.
  - **As cores ditadas:**
    - O fundo do `selected`, ditado "e1fac", tem cinco dígitos. Pelo layout do Ecoleta, deve ser `#E1FAEC` (inferência).
    - O hover do botão foi ditado aos pedaços, "2f, b8, b9 não b8 6 e", e deve ser o `#2FB86E` do dia 1.
- **Conversão implícita.** `collectedItems.value = selectedItems` converte o array em texto com `toString()` (`"4,6,2"`). `selectedItems.join(",")` deixaria isso explícito.

## Entidades

- [[wiki/entities/mayk-brito]]: instrutor; a autoria agora está confirmada ("Mayk Brito na área")
- [[wiki/entities/rocketseat]] e [[wiki/entities/next-level-week]]: o evento e o projeto Ecoleta
- [[wiki/entities/vs-code]]: Ctrl+D, localizar e substituir, minimapa
- [[wiki/entities/figma]]: layout e painel de inspeção de estilos
- [[wiki/entities/unsplash]]: imagens provisórias dos cards
- [[wiki/entities/nodejs]] e [[wiki/entities/react]]: citados na abertura

Citados sem página: React Native, Google (links provisórios), Instagram e YouTube (CTA final).

## Conceitos

[[wiki/concepts/css-grid]] · [[wiki/concepts/flexbox]] · [[wiki/concepts/display-css]] · [[wiki/concepts/atributos-data-html]] · [[wiki/concepts/classlist-javascript]] · [[wiki/concepts/event-listener-javascript]] · [[wiki/concepts/dom]] · [[wiki/concepts/array]] · [[wiki/concepts/funcoes-javascript]] · [[wiki/concepts/igualdade-javascript]] · [[wiki/concepts/var-let-const]] · [[wiki/concepts/algoritmo]] · [[wiki/concepts/formulario-html]] · [[wiki/concepts/modal]] · [[wiki/concepts/css-position]] · [[wiki/concepts/pseudo-elemento-css]] · [[wiki/concepts/sistema-hexadecimal]] · [[wiki/concepts/cascata-css]] · [[wiki/concepts/acessibilidade]] · [[wiki/concepts/html-semantico]] · [[wiki/concepts/debugging]]

## Open Questions

- A página "cadastro concluído" e o envio de verdade dos formulários ficaram para "depois que a gente entrar no back-end".
- A busca por estado ficou "se der tempo"; por enquanto a busca é só por cidade.
- O back-end começa em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]] (Node.js, Express, Nunjucks); o `action` do modal passa a ser `/search`.
- Data provável: 3 de junho de 2020, o terceiro dia da NLW #1 `[external, não verificado]`.

## Raw quotes

- "Bugs são erros na aplicação, algum erro de lógica, algum erro de escrita, a gente sempre tem bugs em nossas aplicações é normal."
- "Isso aqui chama-se algoritmo de programação."
- "O grid é multidimensional, consigo criar linhas e colunas."
- "Console log tira todas as dúvidas da gente."
- "Não precisou nem de back end até agora."
