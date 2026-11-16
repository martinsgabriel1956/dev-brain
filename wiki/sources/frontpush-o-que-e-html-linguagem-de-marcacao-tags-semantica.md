---
type: source
title: "O que é HTML: linguagem de marcação, tags, HTML semântico e estrutura básica (FrontPUSH)"
aliases: ["FrontPUSH o que é HTML", "aula 02 módulo front-end FrontPUSH", "HTML básico FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [html, html5, html-semantico, linguagem-de-marcacao, tags, head, meta, utf-8, viewport, emmet, live-server, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# O que é HTML: linguagem de marcação, tags, HTML semântico e estrutura básica (FrontPUSH)

## TL;DR

Aula 02 do módulo de front-end do [[wiki/entities/frontpush|FrontPUSH]], de nivelamento, com [[wiki/entities/nasser|Násser]] ("Násser aqui"). [[wiki/concepts/html-hipertexto|HTML]] é *Hypertext Markup Language*, "uma linguagem, só que [...] de marcação": tags funcionam como etiquetas que marcam o conteúdo, e o HTML "é responsável pelo conteúdo das páginas web"; o estilo fica para o [[wiki/concepts/css]]. No [[wiki/entities/vs-code]], uma pasta "HTML básico", um `index.html` e o Emmet (`html` + a opção 5) geram a estrutura. Depois vem um tour pelas tags: título (`h1` a `h6`, "uma escala tipográfica"), seções (`section`, `header`, `footer`, `nav`, `div`), texto (`p`, `span`, `strong`), `img`, `form` e `input`. Defende sempre o [[wiki/concepts/html-semantico]]: dá para montar tudo com `div` dentro de `div`, mas isso dificulta entender a estrutura, refatorar e "a vida do Google de indexar o seu site". Fecha com tags aninhadas e a estrutura `html` / `head` / `body`: o `head` traz os [[wiki/concepts/head-html-metadados|metadados]] (`meta charset` UTF-8, `viewport`, `title` na aba) e o `body` o conteúdo. Para estudar: "W3C" e [[wiki/entities/mdn-web-docs|MDN]].

## Key Claims

### Linguagem de marcação

- **HTML = Hypertext Markup Language**: "se está falando aqui language, é uma linguagem, só que é uma linguagem de marcação". Marcação = "labels, ou seja, etiquetas", "uma linguagem para você marcar o conteúdo". Ver [[wiki/concepts/html-hipertexto]].
- **HTML é conteúdo**: "quando eu quero inserir o conteúdo, marcar o conteúdo, criar o conteúdo, eu faço tudo na página HTML". No fim: "a gente vai começar a construir o nosso conteúdo com HTML, nós vamos estilizar com CSS".
- **Não precisa saber tudo de início**: "utilizar o HTML puro, sozinho, não faz muito sentido, principalmente nos dias de hoje"; as tags se aprendem ao longo dos módulos.

### Primeira página e Emmet

- Pasta "HTML básico" na área de trabalho, Open Folder no [[wiki/entities/vs-code]], New File `index.html`.
- **Emmet**: digitar `html` e dar enter "nesse 5" gera "a estrutura básica de uma página HTML"; é "um recurso do próprio VSCode, que é a linguagem Emmet". `[external]` A opção é a abreviação `html:5` (ou `!`); o Emmet é um conjunto de abreviações embutido no editor, não uma linguagem: https://code.visualstudio.com/docs/editor/emmet.

### Tags

- **Uma tag** é "abrir o sinal de maior, digitar alguma label", e ela "abre e fecha". O nome pode ser qualquer coisa: ele cria `<tiririca>` "por meio de didática" e avisa que não é recomendável, "ele não conhece o que é isso". Cada tag pode ter "uma pré-definição ou então um significado semântico". `[external]` Uma tag abre com o sinal de **menor** (`<`). Uma tag desconhecida não quebra a página: o navegador a trata como `HTMLUnknownElement`, inline e sem significado. Tags próprias válidas são os custom elements, com hífen no nome (`<minha-tag>`): https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_custom_elements.
- **Títulos**: `h1` "é o maior título que tem", `h2` menor, até `h6`; "é meio que [...] uma escala tipográfica". Ver [[wiki/concepts/escala-tipografica]] e Tensões.
- **Seções**: `section` (seção simples), `header` (cabeçalho), `footer` (rodapé), `nav` (barra de navegação), `div` (caixinha genérica, personalizada por classe ou ID). "Todas essas tags aqui são caixas, são elementos de bloco, são box." Ver [[wiki/concepts/box-model]] e [[wiki/concepts/display-css]].
- **Texto**: `p` (corpo de texto), `span` (outro trecho), `strong`.
- **Imagem e formulário**: `img`; `form`, com `input` de tipo texto ou botão, entre "vários tipos". Ver [[wiki/concepts/formulario-html]].

### Por que usar o HTML semântico

- **"O Google gosta disso, do HTML semântico"**: a tag já carrega o significado "por pré-definição".
- **Dá para fazer sem semântica**, "porque tudo no final são caixinhas": `div` dentro de `div` dentro de `div`. O custo: é difícil "compreender de como é a estrutura, porque está tudo genérico"; dificulta "a vida do Google de indexar o seu site lá nos motores de busca"; e atrapalha quem pegar o código depois "para poder refatorar". Regra: "Qual é a seção que eu quero construir? [...] Qual é a tag semântica para poder representar isso? É essa, vai lá e utiliza". Ver [[wiki/concepts/html-semantico]].

### Inserindo conteúdo e abrindo no Live Server

- `h1` "esse aqui é o blog do Nasa" (provável "do Násser", ver log) e `h2` com o título de uma notícia, "em uma tipografia menor". Open With Live Server cria "um servidorzinho com essa página". Ver [[wiki/concepts/setup-live-reload-debug-testes]].
- **Para estudar**: "muito conteúdo na internet, principalmente no W3C, ou então no próprio MDN da Firefox". Ver [[wiki/entities/w3c]] e [[wiki/entities/mdn-web-docs]].

### Tags dentro de tags: html, head e body

- **Aninhamento**: "as tags podem estar uma dentro das outras, muito importante isso"; usar sempre a tabulação para ver quem está dentro de quem.
- **`<html>` engloba tudo** e diz ao computador "isso aqui é um documento HTML, interprete como um HTML", porque "todos os arquivos são exatamente iguais para o computador, as extensões servem justamente para poder falar, interpreta desse jeito". Ver Tensões.
- **`head`** é "o cabeçalho do site" com "os dados inerentes ao site [...] os metadados, por isso que existem as tags meta". Ver [[wiki/concepts/head-html-metadados]].
- **UTF-8**: a codificação serve para "a padronização dos inputs do teclado" e "a respectiva interpretação deles"; o Brasil tem "o padrão ABNT-2", com caracteres especiais que outros países não têm, e o UTF-8 faz "aquilo que é digitado no teclado aparecer certinho na sua tela". Ver [[wiki/concepts/utf-8]] e Tensões.
- **viewport**: "a padronização de como aparece na tela o seu HTML, se tem a versão responsiva, qual é a escala". Ver [[wiki/concepts/design-responsivo]].
- **title**: trocar "Document" por "primeira aula de HTML" muda o texto da aba.
- **`body`** "é o corpo da página, é onde eu vou inserir o conteúdo".

## Entities

- [[wiki/entities/nasser]]: instrutor; diz o nome na abertura.
- [[wiki/entities/frontpush]]: curso; aula 02 do módulo de front-end.
- [[wiki/entities/vs-code]]: editor, com Emmet e Live Server.
- [[wiki/entities/google]]: motivo dado para o HTML semântico (indexação).
- [[wiki/entities/w3c]]: indicado como referência (provavelmente o [[wiki/entities/w3schools]], ver Tensões).
- [[wiki/entities/mdn-web-docs]] (novo): "MDN da Firefox", indicado como referência.

## Concepts

- [[wiki/concepts/head-html-metadados]] (novo)
- [[wiki/concepts/html-hipertexto]]
- [[wiki/concepts/html-semantico]]
- [[wiki/concepts/escala-tipografica]]
- [[wiki/concepts/box-model]]
- [[wiki/concepts/display-css]]
- [[wiki/concepts/formulario-html]]
- [[wiki/concepts/utf-8]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/setup-live-reload-debug-testes]]
- [[wiki/concepts/css]]

## Tensões com a wiki

- **`h1`–`h6` não são escala de tamanho.** `[external]` Os níveis de título marcam a hierarquia do documento; o tamanho vem da folha de estilo padrão do navegador e se muda no CSS. O MDN pede para não escolher título pelo tamanho e não pular níveis: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements#usage_notes. A [[wiki/concepts/escala-tipografica]] é uma decisão de design aplicada pelo `font-size`, não pela tag.
- **"Todas essas tags aqui são caixas, são elementos de bloco."** Vale para `section`, `header`, `footer`, `nav` e `div`. `[external]` `span`, `strong` e `img`, citados logo depois, são inline por padrão ([[wiki/concepts/display-css]]); a aula de propriedades do mesmo curso já esbarrou nisso com `<img>` ([[wiki/sources/principais-propriedades-css-color-background-font]]).
- **UTF-8 não tem a ver com teclado.** `[external]` O layout ABNT2 decide qual tecla produz qual caractere; o UTF-8 decide como cada caractere Unicode vira bytes no arquivo e na rede. O `<meta charset="UTF-8">` diz ao navegador como decodificar esses bytes; sem ele, um "ç" pode virar "Ã§" (mojibake): https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta#charset. Ver [[wiki/concepts/utf-8]] e [[wiki/concepts/encoding]].
- **Quem diz "isso é HTML" ao navegador.** `[external]` Não é a tag `<html>`: o servidor manda o tipo no cabeçalho `Content-Type: text/html` (o Live Server o deduz pela extensão `.html`), e o `<!DOCTYPE html>` liga o modo padrão de renderização. O `<html>` é o elemento raiz: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types e https://developer.mozilla.org/en-US/docs/Glossary/Doctype.
- **`title` não é meta.** A lista "outros arquivos meta [...] viewport [...] qual é o título que vai aparecer na aba" junta os dois; `<title>` é um elemento próprio do `head`.
- **"W3C" de novo.** Mesma troca registrada em [[wiki/entities/w3c]]: para tutoriais, o site mais provável é o W3Schools; o W3C publica as especificações (a do HTML hoje é o WHATWG Living Standard: https://html.spec.whatwg.org/). O MDN é da Mozilla, hoje mantido com o Open Web Docs e outros parceiros.
- **"O Google gosta" do HTML semântico.** Como em [[wiki/concepts/html-semantico]], o ganho mais concreto é [[wiki/concepts/acessibilidade]] (landmarks, títulos navegáveis); o efeito em SEO é real mas modesto (confiança média). A aula não fala de acessibilidade.

## Open Questions

- Corte de cerca de 16 s na legenda (05:01–05:18), bem na resposta a "o que é um significado semântico?". O que foi dito ali não está na transcrição.
- `date_published` vazio; provavelmente gravada junto da aula 01 (cerca de 2022, inferido).

## Raw quotes

- "uma linguagem para você marcar o conteúdo"
- "tudo no final são caixinhas"
- "Qual é a tag semântica para poder representar isso? É essa, vai lá e utiliza"
