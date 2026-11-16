---
type: source
title: "CSS, classes e IDs: ligando o style.css, seletores de tag, classe e ID (FrontPUSH, módulo de front-end)"
aliases: ["FrontPUSH CSS classes e IDs aula 03", "aula 03 módulo front-end FrontPUSH", "CSS, Classes & ID's"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, html, seletores, classe, id, especificidade, listas-html, link, caminho-relativo, reset, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-css-classes-e-ids-seletores-link-style-css.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# CSS, classes e IDs: ligando o style.css, seletores de tag, classe e ID (FrontPUSH, módulo de front-end)

## TL;DR

Aula 03 do módulo de front-end do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] ("Násser aqui"), logo depois de [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica|o que é HTML]]. Monta um menu em HTML (`header` > `nav` > `ul` > `li` > `a`, ver [[wiki/concepts/listas-html]]) e mostra que o HTML sozinho "é pobre visualmente": ele "só serve para criar estrutura", e o [[wiki/concepts/css]] é "um segundo agente". Cria `css/style.css` e o liga pelo `<link>` com [[wiki/concepts/caminho-relativo|caminho relativo]] (`css/style.css`, `./`, `../`). Primeiros estilos: fundo `#0f0f0f` no `body`, links sem sublinhado e brancos, `list-style: none`. É um começo de [[wiki/concepts/estilos-padrao-do-navegador-e-reset|reset]] dos padrões do navegador. Uma borda no `header` mostra que "tudo são caixinhas" ([[wiki/concepts/box-model]]). Depois vêm os [[wiki/concepts/seletores-css|seletores]]: o de tag para quando você troca `header`/`nav` por `div` ("vai contra o HTML semântico"). Por isso existem **classe** (`.`, vários elementos, também serve ao JavaScript) e **ID** (`#`, um único elemento, "da mesma forma que você não pode ter dois CPFs"). A classe `.nav-link` vence o estilo do seletor `a` porque "a classe está em uma hierarquia maior que o seletor", que é a [[wiki/concepts/especificidade-css]]. Mesmo tema da aula de classes e IDs do módulo Básico CSS ([[wiki/sources/classes-e-ids-no-css]]), com outra demonstração.

## Key Claims

### Estrutura do menu

- **HTML organiza o conteúdo "por meio de marcações"**: "a gente delimita caixinhas e a gente vai organizando".
- **Menu**: `header` (cabeçalho) > `nav` (barra de navegação, "onde tem os principais links") > `ul` > `li` > link. "Olha só a escadinha que a gente está fazendo." Ver [[wiki/concepts/html-semantico]].
- **`ul` x `ol`**: `ul` é lista não ordenada ("ou é um pontinho, ou é um quadradinho"); `ol` ordena por número, romanos ou letras. "É diferença semântica de tags", com "pré-definições do próprio HTML" que o CSS muda depois. Ver [[wiki/concepts/listas-html]].

### HTML é estrutura, CSS é estilo

- "O HTML sozinho [...] é pobre visualmente, porque o HTML só serve para criar estrutura no nosso site, colocar conteúdo." O CSS é "um segundo agente para poder deixar as coisas bonitas".
- "O HTML é uma linguagem de marcação, não de programação, o CSS é uma linguagem de estilização, não de programação." Estilizar "pelo HTML puro é possível, só que é muito complicado e muito limitado".

### Criando o style.css e ligando pelo link

- Pasta `CSS` com `style.css`; o [[wiki/entities/vs-code]] reconhece o tipo pelo arquivo.
- **`<link>`**: "eu tenho que dizer para o HTML onde está esse arquivo CSS para ele ler". O Emmet tem a opção `link:css`; a tag `link` "não serve para linkar só CSS", tem "vários atributos".
- **Caminho relativo**: `CSS/style.css` entra na pasta; `../` volta uma pasta (que, no exemplo, lista os arquivos da área de trabalho); `./` é "esse diretório de agora". Digitar `./` faz o VS Code listar o conteúdo da pasta. Ver [[wiki/concepts/caminho-relativo]].
- **Não aprender tudo de uma vez**: "esse momento é muito de descoberta"; seletores e propriedades vêm nas próximas aulas.

### Fundo, links e listas: os primeiros estilos

- **Fundo**: o `body` "engloba tudo"; `background-color` em [[wiki/concepts/sistema-hexadecimal|hexadecimal]] `0f0f0f` "ficou preto". "Eu gosto de fundo dark." Ver [[wiki/concepts/background-css]].
- **Links**: roxos e sublinhados por padrão; `text-decoration: none` e `color: #FFF`. "Isso aqui já participa de uns resets que eu gosto de deixar dentro da página, porque isso aqui é tudo configuração padrão do HTML." O azul para não visitado e o roxo para visitado, que até o [[wiki/entities/google]] usa, também é padrão e se muda no CSS. Ver [[wiki/concepts/estilos-padrao-do-navegador-e-reset]].
- **Listas**: `list-style: none` tira os pontinhos; `square` dá quadradinho; comentado, volta a bolinha; numa `ol`, "iria virar 123". Ver [[wiki/concepts/listas-html]].

### Tudo são caixinhas

- `border: 2px solid green` no `header` mostra a caixa; `dashed` deixa tracejada. "Tudo são caixinhas, tudo é div, então a sua capacidade está em você organizar essas caixinhas." Ver [[wiki/concepts/box-model]].
- "Até hoje tem personalizações do CSS que eu não conheço", mas as principais se repetem.

### Seletores de tag, classe e ID

- **Seletor de tag**: "o seletor é o próprio nome da tag" (`header`, `nav { background-color: pink }`). Ver [[wiki/concepts/seletores-css]].
- **Trocar as tags por `div`** ("isso aqui vai contra o HTML semântico, mas só para eu explicar") faz o CSS "perder a referência": não há mais `header` nem `nav`.
- **Classe** = "uma label, uma etiqueta" na tag, identificada no CSS "com um ponto" (`.header`, `.nav`) e também no JavaScript, "para poder eu elencar ali e puxar e manipular esses elementos" ([[wiki/concepts/dom]]). "Primordiais para você entender as aulas de programação."
- **ID**: `id="nav-menu"` e `#nav-menu` ("hashtag, que é a cerquilha"); fica "exatamente igual".
- **O `.header` verde que não aparecia**: só surgiu com uma borda de 1 px, "porque eu precisei definir o tamanho dele". Ver Tensões.

### Comentários

- Comentar é "apagar alguma coisa da interpretação" sem perdê-la, ou explicar "esse trecho no código faz isso e isso". "Recomendo demais, principalmente na parte de lógica." Comentado, o estilo some; descomentado, volta. Ver [[wiki/concepts/comentarios-o-que-nao-o-como]].

### Classe x ID: a diferença semântica

- **ID é identificador único**: "da mesma forma que você não pode ter dois CPFs", RG ou "número de banco". Repetir o ID "você pode, mas a interpretação vai estar errada", "pode quebrar o seu código", porque o JavaScript ou o CSS que pegou aquele ID esperava uma tag só. "Ele pode pegar pela ordem e ainda funcionar", mas a ordem pode mudar.
- **Classe vale para vários**: `class="nav-link"` nos três links e `.nav-link { color: #000 }` deixa todos pretos; tirar a classe do terceiro o devolve ao branco do seletor `a`. Promete uma aula sobre como nomear classes.
- **"A classe está em uma hierarquia maior que o seletor"**: com `a { background-color: red }` e `.nav-link { background-color: #FFF }`, o link com a classe fica branco. Ver [[wiki/concepts/especificidade-css]].
- **Fecho**: os "seletores padrões" são tags, classe e ID; "vai ter uma aula só sobre seletores".

## Entities

- [[wiki/entities/nasser]]: instrutor; diz o nome.
- [[wiki/entities/frontpush]]: curso; aula 03 do módulo de front-end.
- [[wiki/entities/vs-code]]: editor; Emmet `link:css` e autocompletar de caminho com `./`.
- [[wiki/entities/google]]: exemplo de link azul/roxo padrão.

## Concepts

- [[wiki/concepts/listas-html]] (novo)
- [[wiki/concepts/estilos-padrao-do-navegador-e-reset]] (novo)
- [[wiki/concepts/seletores-css]]
- [[wiki/concepts/especificidade-css]]
- [[wiki/concepts/css]]
- [[wiki/concepts/html-semantico]]
- [[wiki/concepts/box-model]]
- [[wiki/concepts/caminho-relativo]]
- [[wiki/concepts/background-css]]
- [[wiki/concepts/sistema-hexadecimal]]
- [[wiki/concepts/comentarios-o-que-nao-o-como]]
- [[wiki/concepts/dom]]

## Tensões com a wiki

- **"A classe está em uma hierarquia maior que o seletor."** A classe também é seletor. `[external]` O que pesa é a [[wiki/concepts/especificidade-css]]: classe (0,1,0) vence tag (0,0,1) seja qual for a ordem no arquivo; ID (1,0,0) vence os dois: https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity. A outra aula de classes e IDs também não usa a palavra ([[wiki/sources/classes-e-ids-no-css]]).
- **O verde do `.header` não precisava de "tamanho".** Inferência pelo código mostrado: a `div.header` tinha dentro a `div.nav` rosa, que ocupava a mesma área (sem padding), então o rosa do filho cobria o verde do pai; a borda só deixou à mostra a beirada do pai. Uma `div` com conteúdo já tem altura.
- **"Configuração padrão do HTML."** `[external]` O azul, o roxo, o sublinhado e os marcadores vêm da folha de estilo do navegador (user agent stylesheet), não do HTML: https://developer.mozilla.org/en-US/docs/Web/CSS/Cascade#user-agent_stylesheets. Ver [[wiki/concepts/estilos-padrao-do-navegador-e-reset]].
- **`list-style: none` e acessibilidade.** `[external]` O Safari com VoiceOver deixa de anunciar como lista uma `ul` com `list-style: none`; num menu, costuma-se repor com `role="list"` (ou aceitar, já que a `nav` já anuncia a região): https://developer.mozilla.org/en-US/docs/Web/CSS/list-style#accessibility. Ver [[wiki/concepts/acessibilidade]].
- **ID repetido "pode pegar pela ordem".** Consistente com [[wiki/sources/classes-e-ids-no-css]]: `[external]` o CSS estiliza todos os elementos com o ID repetido; `getElementById` devolve só o primeiro.
- **"Recomendo demais [comentar], principalmente na parte de lógica"** vs. [[wiki/concepts/comentarios-o-que-nao-o-como]]: a aula trata o comentário também como "desligar código", o que o controle de versão ([[wiki/concepts/git]]) faz melhor; o "esse trecho faz isso e isso" é o comentário de "como" que aquela página desaconselha.
- **`#FFF` e `#000`** são branco e preto; "0f, 0f, 0f" é `#0f0f0f`, quase preto (o mesmo "meu preto" das aulas de CSS).

## Open Questions

- Aulas prometidas: nomes de classe ("bons padrões", provavelmente BEM), seletores (já há [[wiki/sources/seletores-e-pseudo-elements-css]], do outro módulo).
- `date_published` vazio; provavelmente gravada junto das aulas 01 e 02 (~2022, inferido).

## Raw quotes

- "o HTML sozinho [...] é pobre visualmente"
- "tudo são caixinhas, tudo é div"
- "da mesma forma que você não pode ter dois CPFs"
