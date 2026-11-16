---
type: source
title: "NLW #2, dia 3: página de dar aulas do Proffy, formulário e primeiro JavaScript"
aliases: ["NLW 2 dia 3", "Next Level Week 2 dia 3", "Proffy dia 3", "Proffy give-classes"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [frontend, html, css, javascript, formulario-html, fieldset, required, input-type, textarea, seletores-css, seletor-irmao-adjacente, important, css-grid, transition, transform, refatoracao, favicon, theme-color, dom, querySelector, addEventListener, cloneNode, foreach, const, null, defer, rocketseat, proffy, iniciante]
skill: tech-mentor-frontend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy.md"
source_url: ""
author: "Mayk Brito"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #2, dia 3: página de dar aulas do Proffy, formulário e primeiro JavaScript

## TL;DR

Terceira aula (cerca de 1h35) da [[wiki/entities/next-level-week|NLW #2]] com [[wiki/entities/mayk-brito|Mayk Brito]]. Fecha o front-end do **Proffy**. A primeira hora monta `give-classes.html`, a página onde o professor se cadastra. Ela tem três `fieldset`: seus dados, sobre a aula e horários disponíveis. Os campos usam `required`, `type="url"`, `number`, `time`, `textarea` e `name` com colchetes, e o botão de cadastro, que está fora do form, usa o atributo `form`. O CSS ganha `header.css` e `forms.css` compartilhados, o seletor de irmão adjacente `+`, `transition` + `transform`, um grid no desktop e uma demonstração de `!important`, que Mayk desaconselha.

A segunda parte é o primeiro [[wiki/concepts/dom|JavaScript]] da semana. Mostra objetos, `document.location.href`, `querySelector` e `style` no console, depois a tag `<script>` no fim do body, o erro "não pude ler a propriedade style de null" e o `defer`. Por fim, o botão "Novo horário" ganha um [[wiki/concepts/event-listener-javascript|listener]] de clique. Ele chama `cloneField()`, que copia o `.schedule-item` com `cloneNode(true)`, limpa os inputs com `querySelectorAll` + `forEach` e insere a cópia com `appendChild`, tudo em `scripts/addField.js`. O back-end fica para o dia seguinte.

## Key Claims

### Cabeçalho, ícone e refatoração

- **Favicon:** `<link rel="shortcut icon" href="images/favicon.png" type="image/png">` no head, mais `<meta name="theme-color" content="#8257E5">` como "uma informação a mais da nossa página". Ver [[wiki/concepts/head-html-metadados]] (e Tensões).
- **Refatorar** "é melhorar o seu código, é você reescrever parte do seu código a fim de melhorá-lo". Como o cabeçalho da página study se repete na de dar aulas, o CSS do `.page-header` sai para `styles/partials/header.css`. Para selecionar o bloco, ele usa clique + Shift + clique. Ver [[wiki/concepts/refatoracao]].
- **give-classes.html** nasce copiando `study.html` e trocando `study` por `give-classes` com Ctrl+D. O título vira "Que incrível que você quer dar aulas." e entra um `p` com "O primeiro passo é preencher esse formulário de inscrição". Theme-color e favicon repetidos em todas as páginas ficam para o back-end, "de uma maneira muito mais dinâmica".
- **Ctrl+P** abre qualquer arquivo do projeto pelo nome. Ver [[wiki/entities/vs-code]].
- **Filho direto, de novo:** `.top-bar-container > img` para não pegar também a imagem dentro do `a`. Ver [[wiki/concepts/seletores-css]].

### Formulário: estrutura

- **Agrupamentos** de dados viram `fieldset` com `legend` ("toda fieldset precisa vir com uma legend"); o navegador desenha uma borda em volta. O `form` ganha `id="create-class"`, que vai servir depois. Ver [[wiki/concepts/formulario-html]].
- **Seus dados:** nome, avatar (`type="url"`, que "exige que você coloque links [...] HTTP ou HTTPS, dois pontos, barra, barra"), WhatsApp (`type="number"`) e biografia (`textarea`, "multilinhas").
- **`required`:** "o formulário ele não envia [...] se esse campo não estiver preenchido".
- **`small`** para o texto auxiliar pequeno do label.
- **textarea com quebra de linha** entre as tags faz o cursor começar no lugar errado; deixar `<textarea></textarea>` colado.
- **name e id:** cada campo leva `name` para o back-end (`name`, `avatar`, `whatsapp`, `bio`); "cada label também, eu tenho que deixar com for o name e eu já deixo o id também" (ver Tensões).
- **Sobre a aula:** `select` de matéria (as `option` copiadas da página study, a primeira com `value=""`) e "Custo da sua hora/aula" em `input type="number" name="cost"`.
- **Horários disponíveis:** `legend` com o botão "Novo horário" (id dito "addTime"), e um `.schedule-item` com dia da semana, "das" e "até" (`type="time"`).
- **Colchetes no name:** `name="weekday[]"`, `time_from[]`, `time_to[]`, porque "lá no back-end [...] ele pode vir com mais de um valor". E sem id nos campos repetidos: "o ID na página ele tem que ser único. Toda vez que o JavaScript adicionar, ele vai acabar tendo um id duplicado".
- **Footer:** `p` com `warning.svg`, "Importante! Preencha todos os dados", e `br` para quebrar a linha; um `button` "Salvar cadastro".
- **Botão fora do form:** um submit só envia o form em que está; como o footer ficou de fora "por causa do layout", o botão recebe `form="create-class"`. Testado: o `required` bloqueia o envio, a URL inválida também, e Enter num campo também envia.

### Formulário: CSS

- **`forms.css`:** os estilos de `.input-block` e `.select-block` saem da página study para um arquivo comum, que as duas páginas importam. A `.textarea-block` entra nos mesmos seletores, inclusive no `:focus-within::after`, com `position: relative` no bloco.
- **main do formulário:** `max-width: 74rem`, `width: 100%`, `border-radius` e uma margem superior negativa para "subir um pouco" sobre o header, como no layout.
- **fieldset:** `border: none` e `padding: 0 2.4rem`. **textarea:** `padding: 1.2rem 1.6rem`, `height` maior e `resize: vertical` (só puxa na vertical).
- **legend:** `font: 700 2.4rem Archivo`, `color: var(--color-text-title)`, `display: flex; justify-content: space-between` (para o botão "Novo horário" ir para a direita), `width: 100%`, `padding-bottom: 1.6rem` e `border-bottom: 1px solid var(--color-line-in-white)`. O padding separa a borda do texto: "o preenchimento vem e depois vem a borda". Ver [[wiki/concepts/box-model]].
- **Irmão adjacente `+`:** `.input-block + .input-block`, `.input-block + .textarea-block`, `.select-block + .input-block`, `.schedule-item + .schedule-item` e `fieldset + fieldset` pegam só o elemento "que tenha anterior a ele" outro; o primeiro fica sem margem. "A primeira vez que eu aprendi isso aqui eu achei bem confuso." Ver [[wiki/concepts/seletores-css]].
- **CSS organizado na ordem dos elementos:** "eu gosto de organizá-lo conforme os elementos estão próximos". Ele pede que os alunos avisem se algo estiver fora de ordem.
- **Botão "Novo horário":** `background: none` ("não é o background color"), `border: 0`, `color: var(--color-primary)`, `font: 700 1.6rem Archivo`, `cursor: pointer` e `transition: 0.2s`. Sem nome de propriedade, "ele transicione todas as propriedades". De brincadeira, `:hover { transform: translateY(-5px) }` com 1 s, para ver o botão subir; fica só a troca de cor. Ver [[wiki/concepts/transition-e-transform-css]].
- **Footer do formulário:** `padding: 4rem 2.4rem`, `background: var(--color-box-footer)`, `border-top`, `margin-top: 6.4rem`; o `p` com flex centralizado e a imagem com margem; o botão com `width: 100%`, `height: 5.6rem` e cor `secondary`.
- **Schedule item repetido** à mão para ver o espaçamento entre cópias: `margin-top`, `padding-top` e `border-top`.

### Desktop

- **Fieldsets** com `padding: 0 64px`; `.schedule-item` em grid `2fr 1fr 1fr` com `column-gap: 1.6rem`. Ver [[wiki/concepts/css-grid]].
- **`!important`:** o `margin-top: 0` no `.input-block` do grid aparece riscado no DevTools, porque "eu tenho uma profundidade de cascata muito mais forte". Com `!important` funciona, "mas eu não vou usar o important, e você deve usar o important com muito cuidado [...] você fica por tempos procurando por que não está aplicando algum CSS". Em vez dele, copia o seletor mais específico e o limita a `#schedule-items`, um id novo no fieldset, para não "machucar" os espaçamentos dos outros campos. Ver [[wiki/concepts/especificidade-css]].
- **Footer:** `padding: 40px 64px`, `display: flex; justify-content: space-between`, botão com `width: 200px` e `margin-top: 0`. "O display flex [...] não modifica o display de cada um dos itens" (ver Tensões).
- **Navegação completa:** os botões da página inicial levam a study e give-classes, e o formulário só envia com todos os obrigatórios preenchidos.

### JavaScript: objetos e o DOM

- **Paralelo HTML → CSS → JS:** no HTML é `<div id="container">`, no CSS é `#container`; no JS é preciso "entrar no documento" e pesquisar.
- **O JavaScript já está no navegador:** o console do F12 roda código.
- **Objetos:** "todo objeto tem propriedades e funcionalidades", como uma folha de papel (cor, peso, tamanho; embrulhar, receber texto). A página é o objeto `document`; o ponto dá acesso a propriedades e funcionalidades, que "são tantas que [...] até hoje não tem como" memorizar.
- **`document.location.href = "https://google.com"`:** o `=` atribui; sem aspas, o JavaScript "ia entender que eu tenho um objeto Google que tem uma propriedade com". "A gente consegue absolutamente tudo, fazer o controle geral do navegador pelo JavaScript."
- **Funções como caixinha mágica:** `querySelector('#container')` recebe algo e devolve algo; "como ele vai fazer isso eu não sei", como o pedal do acelerador. Essas funcionalidades "não [são] específica[s] do JavaScript, é do JavaScript no browser", que "criou toda uma estrutura pra gente poder fazer a conexão". Ver [[wiki/concepts/funcoes-javascript]] e [[wiki/concepts/dom]].
- **Elemento como objeto:** `querySelector` devolve um HTML element, com `.style.width = "500px"`. "Esse entendimento de objetos é a base para a gente poder entender JavaScript."
- **camelCase:** `background-color` vira `backgroundColor`, "troca os tracinhos pela próxima letra maiúscula".
- **Tipos:** string (aspas duplas ou simples), objeto e, mais adiante, boolean, null e NodeList. Ver [[wiki/concepts/tipos-primitivos-javascript]].

### Onde pôr o script

- **No fim do body:** colado no começo, a página não fica vermelha, porque o HTML é lido "linha a linha" e o container "não foi renderizado ainda".
- **O erro do null:** "eu não pude ler a propriedade style de null". `querySelector` sem resultado devolve `null`, "que é vazio", como a casa da música que "não tinha teto, não tinha nada". "Sempre que você vir esse erro [...] significa que você não pegou o objeto do jeito que deveria ter pego." Ver [[wiki/concepts/null-e-undefined]].
- **`defer`:** no head com `defer`, um script externo (`<script src="scripts/main.js" defer></script>`) roda "depois de passar por toda a renderização da página"; não funciona em script inline. O arquivo vira `scripts/addField.js`. Ver [[wiki/concepts/carregamento-de-scripts]].

### Pensar como programador

- **HTML e CSS "não é programar de fato"**: é a interface. Programar exige caminhos: "se estiver chovendo, você vai pegar um guarda-chuva [...] se estiver frio, você vai pegar uma jaqueta". As variáveis "afeta[m] o jeito, o passo a passo, o algoritmo". Ver [[wiki/concepts/algoritmo]] e [[wiki/concepts/logica-de-programacao]].
- **Escrever os passos em português primeiro:** procurar o botão; quando clicar, executar uma ação; duplicar os campos; colocar na página. "Primeiro você verbaliza [...] conforme você for construindo, você vai percebendo outras coisas que talvez estavam faltando." Ver [[wiki/concepts/traducao-logica-para-codigo]].
- **A sensação de copiar é normal:** "a gente tem a sensação de estar copiando o que os outros estão fazendo [...] É essa sensação mesmo"; "isso não é de uma hora pra outra e não vai ser só nessa semana".
- **O computador pergunta "que campos?" e "onde?"** a cada passo vago, e é assim que o algoritmo fica completo.

### O botão "Novo horário"

- **type="button":** sem tipo, o botão dentro do form "estava querendo submeter o formulário".
- **Eventos:** "o JavaScript aqui na página [...] é muito voltado à ideia de eventos"; `addEventListener('click', cloneField)` é "um ouvidor de eventos". Aspas simples ou duplas servem. Ver [[wiki/concepts/event-listener-javascript]].
- **`function cloneField() {}`:** a palavra `function`, o nome, parênteses "porque eu posso ou não receber argumentos" e chaves, que são "um novo contexto". `console.log('cheguei aqui')` confirma o clique.
- **DOM e nós:** `cloneNode` porque "a gente vai usar sempre node para se referir a elementos HTML"; o DOM (Document Object Model) é uma árvore de nós, com parent e child.
- **`cloneNode(true)`:** com `true` (o *deep*), copia também os filhos; sem ele, "vai pegar a div vazia". Boolean é "o famoso 8 ou 80".
- **`appendChild`:** "onde, querido?", diz o computador; a cópia vai para `#schedule-items`.
- **Variáveis e const:** a expressão longa vira `const newFieldContainer`, porque "eu não gostaria que [...] fosse trocado"; "É até esquisito, né? Como uma variável pode ser constante?". Ver [[wiki/concepts/var-let-const]].
- **Nomes em inglês:** "começa a codar tudo em inglês"; os comentários ficam em português "pra você ter uma clareza". Ver [[wiki/concepts/ingles-para-desenvolvedores]].
- **Limpar os campos:** a cópia trazia "9 e meio-dia". `querySelectorAll('input')` devolve uma NodeList; as posições começam em 0 ("eu não sei porquê"); `fields[0].value = ''` limpa um campo. Ver [[wiki/concepts/array]].
- **Repetição em vez de cópia:** "vamos supor que você tenha 20 campos aqui [...] você vai fazer 20 vezes isso daqui? Não". `fields.forEach(function(field) { field.value = '' })`: a função anônima recebe "o field do momento" e roda uma vez por campo, "se tiverem mil fields, mil vezes".
- **"Com pouquíssimas linhas de código [...] um controle incrível."**

### Fechamento

- Estrutura final: `images/`, `scripts/addField.js`, `styles/main.css`, `styles/partials/` (forms, header, page-give-classes, page-landing, page-study), `index.html`, `study.html`, `give-classes.html`.
- Próximos dias: back-end e banco de dados, porque "não adianta nada a gente ter uma aplicação que tá com dados falsos, que não dá pra filtrar".

## Tensões e precisões

- **`for` do label aponta para o `id`, e os campos repetidos perderam o id.** Mesmo erro do [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy|dia 2]] ("for o name"). Aqui pesa mais: ao tirar o `id` dos campos de horário, os labels "Das" e "Até" deixam de estar ligados aos campos, e cada clone repete labels que não apontam para nada. Leitores de tela não anunciam o rótulo e clicar no texto não foca o campo `[external]` (https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label). Pôr o input dentro do label, ou gerar ids únicos no clone, resolve. Ver [[wiki/concepts/formulario-html]]. Confiança alta.
- **Colchetes no `name` são convenção do servidor, não do HTML.** O navegador só envia o mesmo nome várias vezes (`weekday=1&weekday=3`). Quem transforma `weekday[]` em lista é o parser do back-end (PHP, ou o `qs` do Express com `extended`) `[external]` (https://expressjs.com/en/api.html#express.urlencoded). Confiança alta.
- **WhatsApp como `type="number"`.** Number tira zeros à esquerda, aceita `e` e decimais, mostra setinhas e não aceita `+` ou espaços; para telefone o tipo é `tel` `[external]` (https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/tel). Confiança alta.
- **`required` não protege nada.** A validação do navegador é conveniência; qualquer cliente pode enviar sem ela, então o back-end precisa validar de novo. `[skill: tech-mentor-frontend]`
- **`rel="shortcut icon"` é legado.** O valor padrão é `rel="icon"`; "shortcut" é uma palavra a mais aceita por compatibilidade com versões antigas do Internet Explorer `[external]` (https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel). Confiança alta.
- **"Profundidade de cascata" é especificidade.** O `margin-top` riscado perdeu para um seletor mais específico, a mesma confusão dos dias 1 e 2 (ver [[wiki/concepts/cascata-css]]). `!important` não é "a força maior" da especificidade: ele muda a etapa de importância da cascata, acima da especificidade. O conselho de evitá-lo está certo. Confiança alta.
- **flex muda, sim, o display dos filhos.** Os filhos de um flex container viram itens flex e são "blockificados": um `span` inline passa a se comportar como bloco no cálculo de layout (`display` computado vira `block`) `[external]` (https://www.w3.org/TR/css-flexbox-1/#flex-items). O que não muda é o display do lado de dentro de cada item. Confiança alta.
- **`defer` não é "depois de um certo tempo".** O script com `defer` baixa em paralelo enquanto o HTML é lido e executa na ordem, quando a análise do documento termina, antes do `DOMContentLoaded`. Não é preciso esperar a página ser desenhada. `async` executa assim que baixa, fora de ordem `[external]` (https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script#defer). Ver [[wiki/concepts/carregamento-de-scripts]]. Confiança alta.
- **`const` não congela o valor.** `const` impede reatribuir o nome, não alterar o objeto: `newFieldContainer.querySelector(...)` e mudanças nos filhos continuam possíveis. E, por estar dentro da função, um novo `const` é criado a cada clique `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const). Ver [[wiki/concepts/var-let-const]].
- **`querySelector('#addTime')`**, não "asterisco": na fala, o seletor de id é chamado de "asterisco, addTime". O `#` é o que funciona; `*` é o seletor universal. Lapso de fala, como na NLW #1.
- **O clone copia o valor digitado** porque o `cloneNode` de um `input` copia também o valor atual, não só o atributo `value` `[external]` (https://html.spec.whatwg.org/multipage/input.html#the-input-element). Daí a necessidade de limpar. Os `select` voltaram ao padrão no teste, o que bate com a especificação, que não copia a seleção feita pelo usuário.
- **Índice começando em 0** vem do deslocamento a partir do início da lista (o primeiro item está a zero posições do começo), herança de C e da aritmética de ponteiros `[external, não verificado]`.
- **`document.location`** funciona, mas o objeto canônico é `window.location` (e `location`), e `document.location` é um atalho para ele `[external]` (https://developer.mozilla.org/en-US/docs/Web/API/Document/location).
- **"HTML e CSS não é programar"** é a posição da NLW #1 e #2. Mantida aqui como opinião do instrutor.

## Entidades

- [[wiki/entities/mayk-brito]]: instrutor
- [[wiki/entities/next-level-week]]: NLW #2, projeto Proffy
- [[wiki/entities/rocketseat]]: organizadora
- [[wiki/entities/vs-code]]: Ctrl+P, Shift + clique, Ctrl+D, Emmet
- [[wiki/entities/google-fonts]]: Archivo nos legends e botões

Citados sem página: Thiago (layout), Google (exemplo no `location.href`), a música "A Casa" (sem autor citado), Google Tradutor.

## Conceitos

[[wiki/concepts/head-html-metadados]] · [[wiki/concepts/refatoracao]] · [[wiki/concepts/formulario-html]] · [[wiki/concepts/seletores-css]] · [[wiki/concepts/especificidade-css]] · [[wiki/concepts/cascata-css]] · [[wiki/concepts/box-model]] · [[wiki/concepts/transition-e-transform-css]] · [[wiki/concepts/css-grid]] · [[wiki/concepts/flexbox]] · [[wiki/concepts/pseudo-elemento-css]] · [[wiki/concepts/dom]] · [[wiki/concepts/funcoes-javascript]] · [[wiki/concepts/event-listener-javascript]] · [[wiki/concepts/var-let-const]] · [[wiki/concepts/tipos-primitivos-javascript]] · [[wiki/concepts/null-e-undefined]] · [[wiki/concepts/array]] · [[wiki/concepts/carregamento-de-scripts]] · [[wiki/concepts/algoritmo]] · [[wiki/concepts/logica-de-programacao]] · [[wiki/concepts/traducao-logica-para-codigo]] · [[wiki/concepts/ingles-para-desenvolvedores]] · [[wiki/concepts/acessibilidade]]

## Open Questions

- Os dias 4 e 5 (back-end e banco de dados) dirão como `weekday[]`, `time_from[]` e `time_to[]` chegam ao servidor e se o favicon e o theme-color viram um template compartilhado, como prometido.
- O nome do arquivo é "addField" na fala; não dá para saber se ficou `add-field.js` ou `addField.js` no código publicado.
- O dia 2 deixou a pergunta sobre o `:root` em 40% da landing; este dia não volta a ela.

## Raw quotes

- "Refatorar é melhorar o seu código, é você reescrever parte do seu código a fim de melhorá-lo."
- "Você deve usar o important com muito cuidado."
- "Todo objeto tem propriedades e funcionalidades."
- "Primeiro você verbaliza, pode escrever assim mesmo."
- "A gente tem a sensação de estar copiando o que os outros estão fazendo, né? É essa sensação mesmo."
