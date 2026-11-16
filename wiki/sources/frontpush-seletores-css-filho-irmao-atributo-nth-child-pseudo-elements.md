---
type: source
title: "Seletores no CSS: filho direto, irmão adjacente, universal, atributo, vírgula, nth-child e pseudo-elements (FrontPUSH, módulo de front-end)"
aliases: ["FrontPUSH seletores aula 04", "aula 04 módulo front-end FrontPUSH", "Seletores FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, seletores, combinadores, seletor-universal, seletor-de-atributo, nth-child, pseudo-classe, pseudo-elemento, before-after, position, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Seletores no CSS: filho direto, irmão adjacente, universal, atributo, vírgula, nth-child e pseudo-elements (FrontPUSH, módulo de front-end)

## TL;DR

Aula 04 do módulo de front-end do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]], continuação de [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css|classes e IDs]]. Além de tag, classe e ID, ele mostra os [[wiki/concepts/seletores-css|seletores]] que "mais utiliza no dia a dia", e avisa que saber selecionar ajuda no JavaScript, onde "é muito similar ou deveras igual" ([[wiki/concepts/dom]]). Seletores mostrados:

- filho direto (`section > p`) x descendente (`section p`);
- irmão adjacente (`p + span`);
- universal (`*`), para "generalizar, aplicar tudo e depois só [...] fazer tratamentos pequenos" com classes;
- atributo (`input[type="text"]`);
- vírgula (`h1, h2, h3`);
- `::first-letter`;
- `:nth-child`, `:first-child`, `:last-child`, pares e ímpares.

Fecha com `::before`/`::after`: "como se fosse duas divs" que você não precisa criar no HTML, o que deixa o código "mais clean". A setinha dos botões do site do FrontPUSH é um pseudo-element. Demonstra com `article { position: relative }` e `::after { content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 50%; background: blue }` ([[wiki/concepts/css-position]]). Recado geral: "até hoje eu aprendo CSS", e o programador deve "sempre estar perto da documentação" ([[wiki/entities/mdn-web-docs]]).

## Key Claims

### Abertura

- **Seletores ajudam no JavaScript**: selecionar um elemento no CSS "é muito similar ou deveras igual do que a gente faz no JavaScript". `[external]` `document.querySelector` e `querySelectorAll` recebem os mesmos seletores CSS: https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector. Ver [[wiki/concepts/dom]].
- **"Até hoje eu aprendo CSS"**: estar perto da documentação "deve ser algo presente na vida do programador". Mostra os seletores que mais usa e pede curiosidade para o resto.

### Pais e filhos

- `section` com um `p` direto e outro `p` dentro de uma `div`. **Filho direto** "não é neto, ele não é tataraneto"; seleciona-se com "símbolo de maior": `section > p { color: white }` pinta só o primeiro. **Com espaço** (`section p`), "todo e qualquer parágrafo que estiver dentro da section", e os dois ficam brancos. Ver [[wiki/concepts/seletores-css]].

### Irmãos

- `p`, `span`, `span` como irmãos. `p + span` pega "o span que esteja adjacente a um parágrafo, ou seja, do lado de um parágrafo": só o primeiro `span` fica branco, porque o segundo está do lado de outro `span`.

### Seletor universal

- Pela lista de seletores do MDN ("MDN Firefox"): tag, classe, ID, universal. O `*` serve para "fazer um reset": `* { color: white }` deixa tudo branco "por padrão", e depois classes ou IDs fazem as "variações, com importâncias diferentes", porque a classe "se sobressaiu da tag, ela tem uma hierarquia um pouquinho maior". "Você vai generalizar, aplicar tudo e depois só vai fazer tratamentos pequenos." Ver [[wiki/concepts/estilos-padrao-do-navegador-e-reset]] e [[wiki/concepts/especificidade-css]].

### Seletor de atributo

- Formulário com `input:button` e `input:text` (abreviações do Emmet). `input[type="text"] { background-color: aqua }` muda só o de texto; o botão, que também é `input`, fica igual. Ver [[wiki/concepts/formulario-html]].

### Vírgula

- "Digitei na W3C mais alguns atributos para vocês darem uma olhada" ([[wiki/entities/w3c]]). `h1, h2, h3 { color: #ccc }` ("um cinza clarinho") é "a mesma coisa" que repetir a regra para cada título, "um jeito mais compresso e mais objetivo".

### first-letter

- `p::first-letter` para "a primeira letra de cada parágrafo [...] sempre seja maiúscula", com "text transform capitalized", ou negrito com `font-weight: bold`. Ver [[wiki/concepts/pseudo-elemento-css]] e Tensões.

### nth-child, first-child e last-child

- **`nth-child`**: "child vem de criança, ou seja, filho". Numa `ul` com três `li`, `li:nth-child(1)` pinta o primeiro de `blueviolet`, e trocar para 2 ou 3 move a cor. Ele hesita entre o filho "do li ou dele" (do `ul`). Também cita `last-child` ("sempre vai ser o último elemento"), `first-child` ("se não me engano") e a seleção de pares ou ímpares. Ver [[wiki/concepts/pseudo-classe-css]] e [[wiki/concepts/listas-html]].
- **Não precisa saber todos**, "mas tem alguns que [...] quando você utiliza o seu CSS, ele vai se tornando mais profissional".

### before e after

- "Esses eu utilizo demais." É "como se fosse duas divs, uma que fica na frente do elemento, outra que fica depois do elemento", "só que você não precisa criar outra div para poder manipular ele e ele é filho do article".
- **No FrontPUSH**: a setinha do botão "entrar para a turma" em frontpush.com.br é um pseudo-element. "O seu HTML não fica muito poluído e isso dá uma cara mais profissional." Dá para fazer com `div`s, "mas você vai profissionalizando cada vez mais".

### Criando um pseudo-element na prática

- `article` com `border: 1px solid green`, `width` e `height` de 500 px (depois 200 px). O pai recebe `position: relative`, adiantando a aula de position ([[wiki/concepts/css-position]]). O `::after` recebe "conteúdo vazio", `position: absolute`, `top: 0`, `left: 0`, `width: 100%`, `height: 50%` e `background-color: blue`.
- "É uma div que é filha dele", mas "ela não está aqui no HTML"; mesmo assim dá para "colocar um ícone, posicionar ele dentro do meu elemento pai".
- Fecho: "sempre que tiver um novo seletor [...] eu sempre vou explicar ela nos diferentes projetos".

## Entities

- [[wiki/entities/nasser]]: instrutor; diz o nome.
- [[wiki/entities/frontpush]]: curso; aula 04 do módulo de front-end; a setinha dos botões do site como exemplo de pseudo-element.
- [[wiki/entities/mdn-web-docs]]: lista de seletores mostrada na aula.
- [[wiki/entities/w3c]]: "digitei na W3C" (provável W3Schools, como nas aulas anteriores).

## Concepts

- [[wiki/concepts/seletores-css]]
- [[wiki/concepts/pseudo-classe-css]]
- [[wiki/concepts/pseudo-elemento-css]]
- [[wiki/concepts/css-position]]
- [[wiki/concepts/especificidade-css]]
- [[wiki/concepts/estilos-padrao-do-navegador-e-reset]]
- [[wiki/concepts/formulario-html]]
- [[wiki/concepts/listas-html]]
- [[wiki/concepts/dom]]

## Tensões com a wiki

- **`::before` e `::after` ficam dentro do elemento, não antes e depois dele.** A aula diz as duas coisas ("na frente do elemento, outra [...] depois" e "é filho do article"); a segunda está certa. `[external]` São o primeiro e o último filho do elemento, inline por padrão, e só aparecem com a propriedade `content` (por isso o `content: ""`). Não existem no DOM, então o JavaScript não os seleciona, e o texto em `content` pode ser lido por leitores de tela. Para ícone decorativo, tudo bem; para conteúdo, não: https://developer.mozilla.org/en-US/docs/Web/CSS/::after. Elementos vazios como `<img>` e `<input>` não têm `::before`/`::after`.
- **"text transform capitalized".** `[external]` O valor é `capitalize`, e ele põe em maiúscula a primeira letra de cada palavra. Para só a primeira letra do parágrafo, usa-se `p::first-letter { text-transform: uppercase }`: https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform.
- **Universal como reset de cor.** `[external]` `color` já é herdada; pô-la no `body` basta. `* { color: white }` aplica a cor em cada elemento e passa por cima da herança, inclusive em links, inputs e botões. O universal tem especificidade zero, por isso qualquer classe ou tag o vence ([[wiki/concepts/especificidade-css]]). O reset de `margin`/`padding`/`box-sizing` com `*` das aulas de CSS faz mais sentido, porque essas propriedades não são herdadas.
- **"Do li ou dele?"** `[external]` `li:nth-child(1)` pega o `li` que é o primeiro filho do seu pai, não o primeiro filho do `li`. Pares e ímpares: `:nth-child(even)` / `:nth-child(odd)`, ou fórmulas como `2n+1`. `nth-child`, `first-child` e `last-child` são [[wiki/concepts/pseudo-classe-css|pseudo-classes]] (um dois-pontos), diferentes dos pseudo-elements (`::`).
- **Irmão adjacente x geral.** `p + span` pega só o irmão imediatamente seguinte; `[external]` o irmão geral `p ~ span` pegaria os dois `span`. Mesma lacuna registrada em [[wiki/concepts/seletores-css]].
- **Relação com a aula irmã do módulo Básico CSS** ([[wiki/sources/seletores-e-pseudo-elements-css]]): lá, toda a lista se chama "pseudo-elements"; aqui ele separa `first-letter`, `before` e `after` como pseudo-elements e trata `nth-child` à parte, sem dar nome. Esta aula está mais próxima da terminologia certa.

## Open Questions

- O trecho do seletor de atributo começa com "eu não quero modificar, então você também consegue selecionar"; a legenda daquele bloco (06:15–06:28) parece ter perdido palavras.
- Aula de position citada ("é só você ir na aula de position e voltar para cá"): no módulo Básico CSS já há [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]; a deste módulo ainda não chegou.
- `date_published` vazio (~2022, inferido pelas aulas vizinhas).

## Raw quotes

- "até hoje eu aprendo CSS, até hoje eu pesquiso sobre CSS"
- "você vai generalizar, aplicar tudo e depois só vai fazer tratamentos pequenos"
- "o seu HTML não fica muito poluído e isso dá uma cara mais profissional"
