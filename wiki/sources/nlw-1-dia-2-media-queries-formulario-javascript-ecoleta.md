---
type: source
title: "NLW #1, dia 2: media queries, formulário de cadastro e introdução ao JavaScript no Ecoleta"
aliases: ["NLW 1 dia 2", "Next Level Week 1 dia 2", "Ecoleta formulário", "Ecoleta JavaScript IBGE"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [frontend, html, css, javascript, formulario-html, box-sizing, media-query, fetch-api, promise, json, dom, event-listener, ibge, codepen, refatoracao, lang-dynamic, rocketseat, ecoleta, iniciante]
skill: tech-mentor-frontend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta.md"
source_url: ""
author: "Mayk Brito (inferido)"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #1, dia 2: media queries, formulário de cadastro e introdução ao JavaScript no Ecoleta

## TL;DR

Segunda aula (cerca de 2h12) da [[wiki/entities/next-level-week|Next Level Week #1]] da [[wiki/entities/rocketseat]], com [[wiki/entities/mayk-brito|Mayk Brito]] (autoria inferida, como no [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta|dia 1]]). Ela tem três blocos. Primeiro, uma [[wiki/concepts/refatoracao|refatoração]] que divide o `main.css` em `main`, `home` e `responsive`, seguida de media queries por largura e por altura testadas no modo de dispositivo do DevTools. Segundo, a página `create-point.html` com um [[wiki/concepts/formulario-html|formulário]] de cadastro (fieldset, legend, label, input, select desabilitado, botão submit), estilizado com `box-sizing: border-box`, [[wiki/concepts/flexbox]] em coluna e o seletor de irmão adjacente `.field + .field`. Terceiro, um "beabá" de JavaScript no [[wiki/entities/codepen]]: `document.write`, [[wiki/concepts/var-let-const|var, let e const]], string, number, boolean, objeto, [[wiki/concepts/array]], [[wiki/concepts/funcoes-javascript|funções]], if/else e for. Para fechar, ele liga o JavaScript à página: [[wiki/concepts/fetch-api|fetch]] na API de localidades do [[wiki/entities/ibge]], [[wiki/concepts/promise-javascript|promises]] com `then`, [[wiki/concepts/json]], `querySelector`, um [[wiki/concepts/event-listener-javascript|ouvidor de eventos]] `change` que carrega as cidades do estado escolhido e um `input type="hidden"` que guarda o nome do estado.

## Key Claims

### Refatorar e separar o CSS

- **Refatorar** é "refazer algumas coisas do nosso código para torná-lo um pouquinho mais fácil de dar manutenção depois"; "faz parte da vida do dev". Ver [[wiki/concepts/refatoracao]].
- **Três arquivos:** `main.css` fica com o que é geral (`:root`, `*`, `html`, `body`, `a`, títulos), `home.css` com tudo do `#page-home` e `responsive.css` com as media queries. No HTML, "o responsivo fica por último", depois de `main` e `home`, porque a ordem dos `<link>` decide quem sobrescreve. Ver [[wiki/concepts/cascata-css]].
- **Variáveis vêm do primeiro arquivo:** a `--title-color` funciona no `create-point.css` porque o `main.css` é carregado antes: "ele está seguindo esse fluxo".

### Media queries e o modo de dispositivo

- **Toggle Device Toolbar** (F12) simula 4K, laptop 1440 px, tablet e rotação. Ver [[wiki/concepts/breakpoint]].
- **Largura:** `@media (min-width: 1700px)` põe o fundo em `background-position-x: 40vw` (era 35 no original). O 1700 veio de olhar a tela até a imagem "encostar".
- **Altura:** `@media (max-height: 760px)` fixa `background-position-y: 200px`, para a imagem não subir sobre o "cadastre um ponto de coleta". "Fizemos uma regra para altura e regras para largura."
- **Definição:** responsividade é fazer "com que a sua aplicação se adapte em diversos tipos de tela"; media query são "regras para responsividade".

### A página de cadastro

- **Reaproveita a home:** copia o `index.html`, troca o id para `page-create-point`, remove a `div.content` e o `main`, e o link vira "voltar para home". Cuidado ao apagar uma tag: a linha guia do VS Code mostra onde ela fecha; esquecer o fechamento "meu layout pode quebrar".
- **Nome de arquivo** com traço, sem espaço e sem acento: `create-point.html`, `create-point.css`.
- **Ícone colorido editando o SVG:** a seta de voltar era preta porque o `stroke` é `currentColor`; ele copia o `stroke` verde do `log-in.svg`. Ver [[wiki/concepts/formato-svg]].

### Formulário

- **Estrutura:** `form` > `h1` + dois `fieldset` (dados da entidade; itens de coleta), cada um com `legend` > `h2`, e um `button type="submit"` que "vai querer fazer o submit do form". `fieldset` em vez de `div` "para uma ideia mais semântica". Ver [[wiki/concepts/formulario-html]] e [[wiki/concepts/html-semantico]].
- **Campo:** `div.field` com `label` + `input`; `.field-group` agrupa dois campos lado a lado. O `name` é o que leva o valor no envio; o `for` "pra referenciar que esse label pertence a esse input" (ver Tensões).
- **Tipos:** `type="number"` só aceita dígitos, mas ele usa `text` em "Número/Complemento" para aceitar "bloco, apartamento". `select` com `option value=""` "Selecione o estado"; a cidade começa `disabled` até o JavaScript habilitá-la.
- **Emmet:** `.field` cria `<div class="field">`; `.field*2` repete; `label+input` cria irmãos; `mr` vira `margin-right`. Ver [[wiki/entities/vs-code]].

### box-sizing

- **O padrão estica a caixa:** com `content-box`, o padding soma à largura definida, "ele tende a aumentar o tamanho da sua caixa". Ele mostra comentando e descomentando o `padding: 64px` do form.
- **`border-box`:** a largura vai até a borda e o padding fica "dentro dele mesmo". "Uma caixa ela é medida nas suas bordas", como uma caixa de papelão com uma garrafinha dentro. Por isso ele aplica `box-sizing: border-box` a todos os elementos no `main.css`, "como se eu estivesse resetando o comportamento padrão do CSS". Ver [[wiki/concepts/box-model]].
- **Centralizar "pelo lado de fora"** é `margin: 80px auto`; "pelo lado de dentro" é flex.

### Estilo do formulário

- **Campos:** `.field` em `flex-direction: column`; dentro do `.field-group`, `.field { flex: 1 }` divide a largura. Ver [[wiki/concepts/flexbox]].
- **Irmão adjacente:** `.field-group .field + .field { margin-left: 24px }` pega só o campo "que vier seguido de um field". Ver [[wiki/concepts/seletores-css]].
- **Input e select** compartilham regras com vírgula (`form input, form select`): fundo `#F0F0F5`, `border: 0`, `padding: 16px 24px`, `border-radius: 8px`.
- **`outline: none`** é "opcional"; "o importante é você colocar algum efeito visual para o cara saber que ele está no campo". Ver [[wiki/concepts/acessibilidade]].
- **`appearance: none`** com os prefixos `-webkit-` e `-moz-` tira o estilo nativo do select, que o Chrome e o Firefox não deixam estilizar.
- **Botão:** 260x56, `var(--primary-color)`, `:hover` mais escuro. `transition` só com a duração anima "tudo que aceita a transição", e isso fez o botão piscar no reload; por isso ele escreve `transition: background-color 400ms`. Ver [[wiki/concepts/pseudo-classe-css]].
- **Anote em comentários:** "Na programação a gente não é focado em decorar nada"; faça do cérebro "um arquivo de indexação", um sumário para saber onde achar.

### O beabá do JavaScript

- **`document.write("hello")`:** `document` "sempre vai estar se referindo ao documento", é um objeto, e `write` é "uma funcionalidade do objeto". Comentário é `//` (Ctrl+/). Ver [[wiki/concepts/dom]].
- **Variável** serve para "guardar em memória alguma coisa para usar mais tarde"; declarada sem valor é `undefined`. `var`, `let` e `const`: "tanto faz", mas ele prefere `const` "porque eu quero fazer algumas coisas que não mudam o seu valor" (ver Tensões e [[wiki/concepts/var-let-const]]).
- **String** com aspas duplas, simples ou crase; solta no código "não serve pra nada" sem ir para uma variável ou função. Ver [[wiki/concepts/string]].
- **Number e coerção:** `1 + 12` dá 13, mas `"1" + 12` dá `"112"`: "já que eu não consigo fazer soma de string com número [...] eu vou concatenar". Ver [[wiki/concepts/tipos-primitivos-javascript]].
- **Boolean** é "sempre true ou false", sem aspas.
- **Objeto** tem propriedades e funcionalidades, como um teclado ou uma câmera: `pessoa.altura`, `pessoa.idade`, `pessoa.solteiro`; propriedade inexistente dá `undefined`. Um método sem `return` também "é undefined".
- **Array** (vetor) é "uma coleção de dados", de qualquer tipo, acessada por posição a partir de 0. Ver [[wiki/concepts/array]].
- **Função** é "atalho", "reuso de código": registrar (`function sayMyName(name) {...}`) e executar (`sayMyName("Douglas")`). O argumento entra como por "a boca de um funil". Ver [[wiki/concepts/funcoes-javascript]].
- **Condicional:** `if (notaFinal < 5)` reprovado, `else` aprovado; o operador transforma a comparação em boolean. **Loop:** `for (let i = 0; i < 10; i++)`, com `i++` igual a `i = i + 1`, e template string `` `<p>${i}</p>` ``. Ver [[wiki/concepts/logica-de-programacao]].

### JavaScript na página

- **`<script src="/scripts/create-point.js">`** antes de fechar o `body`. No console do DevTools dá para rodar código; `console.log` mostra qualquer valor. `document.write` no console "acabou com a minha página inteira".
- **Selecionar:** `document.querySelector("form")`, `querySelectorAll("input")` (uma NodeList) e `querySelector("select[name=uf]")`, com a mesma sintaxe de seletor do CSS. Ver [[wiki/concepts/dom]].
- **API do IBGE:** `servicodados.ibge.gov.br/api/v1/localidades/estados` devolve um array de 27 objetos (id, sigla, nome, região); `.../estados/{UF}/municipios` devolve as cidades. Ver [[wiki/entities/ibge]].
- **JSON** é "JavaScript Object Notation", "um textão que ele parece muito com JavaScript". Ver [[wiki/concepts/json]].
- **fetch e promise:** `fetch(url)` devolve uma promessa: "eu prometo pra você que eu vou nesse site [...] Pode ser que dê certo, pode ser que não". `then` trata o caminho bom, `catch` o caminho de erro, que ele deixa de lado. `res.json()` "também é uma promessa", por isso há dois `then` encadeados. Ver [[wiki/concepts/fetch-api]] e [[wiki/concepts/promise-javascript]].
- **Arrow function** é "um outro jeito de criar a função anônima": com um parâmetro dispensa os parênteses; com uma linha só dispensa `return` e chaves: `res => res.json()`.
- **Populando o select:** `` for (const state of states) { ufSelect.innerHTML += `<option value="${state.id}">${state.nome}</option>` } ``, com `+=` em vez de `=` para não sobrescrever.
- **Evento:** `addEventListener("change", getCities)`, passando a função "por referência" (sem parênteses, para não executar na hora). `event.target` é o select; `event.target.value` é o id do estado, usado para montar a URL das cidades. Depois de preencher, `citySelect.disabled = false`. Ver [[wiki/concepts/event-listener-javascript]].
- **Nome em vez de id:** o envio mandaria `uf=12`; ele guarda o nome num `input type="hidden" name="state"`, preenchido com `event.target.options[event.target.selectedIndex].text`. Alternativa: salvar o id no banco e consultar o IBGE de novo depois, uma chamada a mais: "tudo tem prós e contras".
- **Copiar e colar** o bloco do fetch "é grotesco"; com o tempo "você vai fazer uma funcionalidade que vai reaproveitar esse código". Ver [[wiki/concepts/dry]].

### Atitude

- **Bugs são normais:** com o Edge travando, "quanto mais maduro você tiver a respeito desse assunto, mais rápido você vai resolver".
- **Descanso consolida:** "o cérebro ele vai assimilando as coisas"; "o descanso é importante para você recuperar suas energias e para fazer com que o cérebro consolide alguns conhecimentos". Ver [[wiki/concepts/pratica-deliberada]].

## Tensões e precisões

- **`for` do label aponta para `id`, não para `name`.** A aula escreve `<label for="name">` e `<input name="name">`, sem `id`; assim o label não fica associado ao campo (clicar no texto não foca o input, e o leitor de tela não anuncia o rótulo) `[external]` (https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label). Confiança alta. Ver [[wiki/concepts/acessibilidade]].
- **var, let e const não são "tanto faz".** `var` tem escopo de função e é içada; `let` e `const` têm escopo de bloco; `const` impede reatribuição, mas não mutação (`const pessoa = {}` aceita `pessoa.idade = 25`) `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const). Ver [[wiki/concepts/var-let-const]].
- **`innerHTML` com dado de fora.** Montar options com `innerHTML +=` e texto vindo de uma API abre espaço para XSS se a fonte não for confiável, e reconstrói o conteúdo do select a cada iteração. `[skill: tech-mentor-frontend]` Prefira `new Option(nome, id)` + `append`, ou `textContent`. Para o IBGE o risco é baixo, mas o hábito pesa.
- **Sem tratamento de erro.** A aula segue "o fluxo do caminho que dá certo": sem `catch` e sem checar `res.ok` (o `fetch` só rejeita em falha de rede; um 404 ou 500 cai no `then`) `[external]` (https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch). `[skill: tech-mentor-frontend]` Timeout com `AbortSignal.timeout()` e retry com backoff são o padrão de resiliência.
- **Cidades acumulam.** Como o `getCities` só faz `+=`, trocar de estado soma as cidades do novo estado às do anterior; a aula não limpa o select (talvez o dia 3 corrija). Inferência a partir do código descrito.
- **`selectedIndex` inclui o "Selecione o estado"**, que é o índice 0; os 27 estados ficam de 1 a 27, e não "de 0 a 26" como ele diz. O código funciona igual, porque o índice vem do próprio select.
- **Largura de "90 pixels"** no `#page-create-point` (dito três vezes) deve ser 90%, como na home; com 90 px o conteúdo não caberia. Erro de fala ou de ASR.
- **`appearance` sem prefixo** já funciona nos navegadores atuais; os prefixos são legado de 2020 `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/appearance).
- **"Maior que 5" e o 5 exato.** O `else` aprova também quem tirou 5; a fala diz "se esse aluno tirou mais que 5". Detalhe de borda, comum em exemplos didáticos.
- **"Colchetes" para chaves:** ao enxugar a arrow function ele diz que pode tirar "os colchetes"; são as chaves do bloco. Ele mesmo avisa: "eu erro o nome de tudo dessas coisas".

## Entidades

- [[wiki/entities/mayk-brito]]: instrutor (inferido)
- [[wiki/entities/rocketseat]] e [[wiki/entities/next-level-week]]: o evento e o projeto Ecoleta
- [[wiki/entities/ibge]]: API de localidades (estados e municípios)
- [[wiki/entities/codepen]]: editor online usado para o beabá de JavaScript
- [[wiki/entities/vs-code]]: Emmet, linha guia de tags, Ctrl+/

Citados sem página: Edge, Chrome, Firefox, Figma (layout), extensão JSON Formatter.

## Conceitos

[[wiki/concepts/refatoracao]] · [[wiki/concepts/cascata-css]] · [[wiki/concepts/breakpoint]] · [[wiki/concepts/formulario-html]] · [[wiki/concepts/html-semantico]] · [[wiki/concepts/acessibilidade]] · [[wiki/concepts/box-model]] · [[wiki/concepts/flexbox]] · [[wiki/concepts/seletores-css]] · [[wiki/concepts/pseudo-classe-css]] · [[wiki/concepts/formato-svg]] · [[wiki/concepts/dom]] · [[wiki/concepts/var-let-const]] · [[wiki/concepts/string]] · [[wiki/concepts/tipos-primitivos-javascript]] · [[wiki/concepts/array]] · [[wiki/concepts/funcoes-javascript]] · [[wiki/concepts/logica-de-programacao]] · [[wiki/concepts/fetch-api]] · [[wiki/concepts/promise-javascript]] · [[wiki/concepts/json]] · [[wiki/concepts/event-listener-javascript]] · [[wiki/concepts/dry]] · [[wiki/concepts/pratica-deliberada]]

## Open Questions

- O dia 3 limpa o select de cidades ao trocar de estado e corrige o `for` dos labels? Respondido em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: limpa o select (e o desabilita) antes do `fetch`; o `for` sem `id` se repete no modal de busca.
- A segunda fieldset (itens de coleta, feita no dia 3) e o envio do formulário ficaram para o dia seguinte: "A parte obviamente de enviar esses dados vai ser também pra depois".
- Data provável 2 de junho de 2020 (segundo dia da NLW #1) `[external, não verificado]`.

## Raw quotes

- "Refatorar faz parte da vida do dev."
- "Uma caixa ela é medida nas suas bordas."
- "Na programação a gente não é focado em decorar nada."
- "Eu prometo pra você que eu vou nesse site, mas eu vou voltar."
- "Bugs, erros, são comuns e isso acontece direto."
