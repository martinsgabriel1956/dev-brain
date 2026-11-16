---
type: source
title: "Align-content: alinhar as linhas de flex-itens quando há quebra (FrontPUSH, módulo de Flexbox)"
aliases: ["FrontPUSH flexbox aula 05", "Align-content FrontPUSH", "aula 05 módulo Flexbox FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, flexbox, align-content, flex-wrap, alinhamento, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-align-content-linhas-flex-wrap.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Align-content: alinhar as linhas de flex-itens quando há quebra (FrontPUSH, módulo de Flexbox)

## TL;DR

Aula 05 do módulo de [[wiki/concepts/flexbox]] do [[wiki/entities/frontpush|FrontPUSH]], de [[wiki/entities/nasser|Násser]]. Última propriedade do flex-container ([[wiki/concepts/flex-container-e-flex-item]]): `align-content`.

- **Quando funciona**: só com "um grupo maior" de itens e `flex-wrap` ligado, "porque ela ajusta quando tem muitos itens quebrados". Com um grupo pequeno, "literalmente não vai fazer diferença nenhuma".
- **Valores**: `flex-start` (linhas coladas no topo), `flex-end` (embaixo), `stretch`, `center`, `space-between`, `space-around`. "É o mesmo conceito, só que aplicado de maneiras diferentes" do `justify-content` e do `align-items`.
- **Pouco uso**: "na maioria das vezes eu coloco três, nunca chega a ter muitas linhas [...] e eu faço mais uso do flex-direction".
- **Método**: trocar para `column` e ir vendo, "para você entender o máximo da propriedade" ([[wiki/concepts/pratica-deliberada]]).

## Key Claims

### Quando o align-content faz diferença

- "Ele se dá justamente pelos vários elementos." Com quatro itens e `align-items: center`, o grupo inteiro se move; `align-content` "literalmente não vai fazer diferença nenhuma [...] eu só tenho um grupo pequeno". Ele sobe para 12 itens.
- "A propriedade do flex-wrap tem que estar ativada para poder essa propriedade fazer sentido", porque ela "vai gerenciar como eles vão se posicionar" quando há "muitos itens quebrados". Ver [[wiki/sources/frontpush-flex-direction-flex-wrap-flex-flow]].
- Slide (print enviado com a transcrição): "Alinha as linhas do container em relação ao eixo vertical. A propriedade só funciona se existir mais de uma linha de flex-itens. Para isso o flex-wrap precisa ser wrap." E: "se você não definir height para o container, a propriedade não influencia no layout."

### Os valores

- `flex-start`: no `justify-content` "alinhava à esquerda"; no `align-items`, "colado no topo". No `align-content`, os itens que estavam "espaçados um do outro [...] vão colar na parte de cima". `flex-end`: "vão colar todos na parte de baixo".
- "É a maneira de como os itens se espaçam entre si quando eu tenho vários itens e eles estão com a propriedade de flex-wrap, e aí sim cabe o align-content. Por isso que a gente utiliza menos."
- `stretch` "vai pegar o tamanho que tem disponível dentro do container e vai completar", como "o align-items stretch da última vez, ele meio que dá um width ou um height de 100%". Na demo, "como eu defini alguma margem aqui, ele não completou". Ver Precisões.
- `center`: "todos ficam alinhados ao centro". `space-around` deixa "o espacinho em cima e o espacinho embaixo"; `space-between` "vai completar", colando nas pontas. Ver [[wiki/concepts/espaco-em-branco]].
- "São posições relativas com relação ao container ou com relação aos próprios conteúdos, que são os flex-itens."

### Testar e combinar

- "É sempre bom a gente trocar para column para ver como é que funciona."
- "O tanto de posicionamento diferente que você pode só apenas com flexbox dentro de um mesmo container": `flex-start` de um lado e `space-around` do outro para distribuir; `flex-start` nos dois para "colar na parte esquerda e na parte do topo".
- Abertura: "Eu podia ter explicado o align-content depois que eu fui perceber, mas vamos gravá-lo aqui agora". Próxima aula: `flex-grow`, primeira propriedade dos itens.

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/frontpush]]: curso; módulo de Flexbox.

## Concepts

- [[wiki/concepts/flexbox]]
- [[wiki/concepts/flex-container-e-flex-item]]
- [[wiki/concepts/espaco-em-branco]]
- [[wiki/concepts/pratica-deliberada]]

## Precisões e tensões com a wiki

- **Linhas, não itens.** `[external]` `align-content` distribui as *linhas* de um contêiner flex com várias linhas no eixo cruzado; `align-items` alinha os *itens* dentro de cada linha: https://developer.mozilla.org/en-US/docs/Web/CSS/align-content. O slide diz isso; a fala ("como os itens se espaçam entre si") mistura os dois.
- **Contêiner de uma linha.** `[external]` A MDN diz que a propriedade não tem efeito em contêiner de uma linha só, ou seja, com `flex-wrap: nowrap`. Com `wrap`, o contêiner é multilinha mesmo que caiba tudo numa linha.
- **Padrão.** `[external]` O valor inicial é `normal`, que no flexbox se comporta como `stretch` (o slide diz `stretch`). `space-evenly` também existe.
- **`stretch` não é "100%".** `[external]` Ele divide o espaço livre do contêiner entre as linhas; itens com altura `auto` esticam até a altura da linha. Na demo, o que segura os itens é o `max-height: 100px` da aula 04 ([[wiki/sources/frontpush-justify-content-align-items-box-sizing]]), não só a margem.
- **"Eixo vertical".** Vale para `row`. Em `column`, o eixo cruzado é horizontal e `align-content` distribui colunas, que é o que ele mostra ao "trocar para column".
- **"flex-stretch".** Não existe esse valor; é `stretch`. Ficou literal no raw.

## Open Questions

- `date_published` vazio (~2022, inferido pelo resto do curso).

## Raw quotes

- "eu só tenho um grupo pequeno"
- "é o mesmo conceito, só que aplicado de maneiras diferentes"
- "sempre troca para coluna e vai vendo o que vai acontecendo"
