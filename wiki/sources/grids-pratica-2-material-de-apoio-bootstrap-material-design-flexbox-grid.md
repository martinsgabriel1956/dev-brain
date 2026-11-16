---
type: source
title: "Grids na prática, parte 2: material de apoio (Grid System Library, Bootstrap, Material Design, Flexbox Grid, responsivo x adaptativo)"
aliases: ["Grids Prática 2", "aula 13 do FrontPUSH", "material de apoio de grids", "links do Notion sobre grids"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, grid, grid-de-colunas, grid-de-8-pontos, breakpoint, design-responsivo, design-adaptativo, bootstrap, material-design, flexbox, media-query]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-15
---

# Grids na prática, parte 2: material de apoio

## TL;DR

Aula curta (8 min) em que o autor percorre os links do Notion do curso sobre grids, sem demo no [[wiki/entities/figma]]. Sete materiais: (1) **Grid System Library**, kit gratuito (doação opcional de US$ 4) com grids de iOS, Android e Bootstrap e uma calculadora de colunas, gutter e margem; (2) o **grid do [[wiki/entities/twitter-bootstrap|Bootstrap]]**, de onde vêm "alguns valores" que ele usou nas aulas (large, extra large), e o Bootstrap 5, que deixa mudar gutter e coluna; (3) um artigo sobre [[wiki/concepts/grid-de-8-pontos]]; (4) o [[wiki/entities/material-design]], com breakpoints, 4/8/12 colunas, margens, gutters, grid fluido e regiões de UI; (5) a biblioteca **Flexbox Grid** (classes de tamanho, offset, alinhamento, distribuição); (6) um artigo sobre [[wiki/concepts/design-responsivo|responsivo]] x [[wiki/concepts/design-adaptativo|adaptativo]]; (7) exemplos de layouts flexíveis com media query, como [[wiki/entities/dropbox]] e [[wiki/entities/dribbble]]: o que fica lado a lado no desktop empilha no tablet, e o formulário da home vira um botão no mobile. A ideia que fica: 4, 8 e 12 colunas são "esses números que a gente está sempre circundando".

## Key Claims

### Grid System Library

- **Biblioteca gratuita de grids para iOS, Android e Bootstrap**: de 6 a 12 colunas, 15 dispositivos, 26 grids e 5 "ferramentas de gráfico". Download com doação opcional de US$ 4; tem versão para Figma.
- **Os padrões da biblioteca não são os da aula**: tem até mobile com duas colunas. "Você desenha e vê qual o melhor padrão para você." Ver [[wiki/concepts/grid-de-colunas]].
- **Os valores do iOS variam bastante** entre dispositivos.
- **Calculadora:** você informa a largura (1.440), as colunas (12), o gutter (32) e a margem, e ela devolve a largura das colunas, "não chutando valores". 12 colunas com gutter de 32 é a mesma configuração da [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt|aula de espaçamento]]; ali a coluna era 72, o que dá 1216 de conteúdo num frame de 1440 (conta do agente).

### Bootstrap

- **Alguns valores das aulas vêm do Bootstrap**, "por ser muito utilizado na web": o large e o extra large.
- **O Bootstrap 5 melhorou o grid em relação ao 4.5**: adicionou "mais uma seção" e deixa mudar o gutter e o tamanho da coluna. `[external]` A documentação confirma que o Bootstrap 5 acrescentou o breakpoint `xxl` (≥ 1400 px) aos `sm`/`md`/`lg`/`xl` (576/768/992/1200) e criou as classes de gutter `.g-*`, `.gx-*`, `.gy-*`: https://getbootstrap.com/docs/5.0/layout/grid/ e https://getbootstrap.com/docs/5.0/layout/gutters/. A "seção" a mais é provavelmente o `xxl` (inferência do agente).

### Grid de 8 pontos e Material Design

- **Artigo sobre [[wiki/concepts/grid-de-8-pontos]]** para entender "como é que se dá este processo".
- **O [[wiki/entities/material-design]] complementa as aulas**: breakpoints, 4, 8 e 12 colunas, margens, gutters, resoluções e "os ranges que a gente consegue nesses valores".
- **"Sempre são esses números que a gente está sempre circundando"**: 4, 8 e 12 colunas. `[skill: ux-ui-mentor]` A tabela da skill dá 4 colunas no mobile, 8 no tablet e 12 no desktop. Ver [[wiki/concepts/breakpoint]].
- **Grid fluido:** "conforme aumenta a tela também, aumenta o sistema de grids", o conceito que ele diz ter explicado na teoria.
- **Regiões de UI** servem para dashboards.

### Flexbox Grid

- **Biblioteca que implementa muitos conceitos do Bootstrap** com classes prontas: tamanho de coluna, offset, size, alinhamento, distribuição. Para "construir, por exemplo, interfaces mais rápidas". `[external]` flexboxgrid.com, com classes como `col-xs-6`, `col-md-offset-2`, `center-xs` e `between-xs`; não conferido nesta ingestão.
- **Um módulo do curso vai tratar grid e flexbox no código**; o autor fala em "lá no Script FE" (nome literal, ver Open Questions). Os conceitos de Flexbox "a gente já viu".

### Responsivo x adaptativo

- **São "dois conceitos diferentes"**, já vistos na teoria. O autor recomenda um artigo "ou até me corrigirem se eu estiver errado". Ver [[wiki/concepts/design-adaptativo]].

### Exemplos: o horizontal que quebra na vertical

- **Layout horizontal se projeta para empilhar**: "esse elemento fica em cima desse, depois fica em cima desse". Ver [[wiki/concepts/design-responsivo]].
- **Olhar empresas grandes**: [[wiki/entities/dropbox]] e [[wiki/entities/dribbble]] em telas maiores e menores, para enxergar padrões.
- **Do desktop ao tablet, duas caixas lado a lado viram coluna**: "modo linha, modo coluna".
- **No mobile, elementos são suprimidos**: o formulário da home vira "um botãozinho", porque um formulário grande na página inicial "pode atrapalhar o fluir" numa tela pequena. `[skill: ux-ui-mentor]` É a pergunta do mobile-first: o que é essencial numa tela pequena? O resto entra em telas maiores.
- **Ver o comportamento do grid ajuda o design e a implementação.**

### Fechamento

- **O Notion é o material de apoio do curso** e reúne todos os links.
- **Praticar e perguntar**: "venham aqui nos meus wireframes, vejam se tem alguma coisa errada, pergunta para mim." Ver [[wiki/concepts/wireframe]].

## Entities

- [[wiki/entities/nasser]]: autor (inferido: série de aulas do [[wiki/entities/frontpush]], "meus wireframes", mesmo estilo das aulas práticas anteriores). O nome não é dito.
- [[wiki/entities/twitter-bootstrap]]: grid de referência; Bootstrap 4.5 x 5.
- [[wiki/entities/material-design]]: breakpoints, colunas, margens, grid fluido, regiões de UI.
- [[wiki/entities/dropbox]], [[wiki/entities/dribbble]]: exemplos de layout responsivo.
- [[wiki/entities/figma]]: formato da Grid System Library.
- [[wiki/entities/frontpush]]: curso; Notion como material de apoio.
- Sem página própria: Grid System Library, Flexbox Grid, Notion, iOS, Android.

## Concepts

- [[wiki/concepts/grid-de-colunas]]
- [[wiki/concepts/breakpoint]] (novo)
- [[wiki/concepts/design-adaptativo]] (novo)
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/grid-de-8-pontos]]
- [[wiki/concepts/wireframe]]
- [[wiki/concepts/mobile-layouts-responsivos]]

## Tensões com a wiki

- **Aulas teóricas de grid fora da wiki.** O autor cita o grid fluido e a diferença entre responsivo e adaptativo "que eu expliquei para vocês", mas a parte teórica de grids e a parte 1 desta prática não foram ingeridas. As definições em [[wiki/concepts/design-adaptativo]] vêm da skill, não do autor.
- **"Alguns valores eu me baseei" no Bootstrap x 72 + 32.** O Bootstrap usa gutter padrão de 1.5rem (24 px) `[external]` (https://getbootstrap.com/docs/5.0/layout/gutters/), e a aula de espaçamento usou 32. A frase deve valer para os breakpoints (large, extra large), não para o gutter. Inferência do agente.
- **Mobile com duas colunas** na Grid System Library x 4 colunas na tabela da skill: o autor deixa a escolha ao designer.

## Open Questions

- "Lá no Script FE": nome de módulo ou curso que a ASR pode ter errado. Mantido literal no raw.
- "Essa caixa simplesmente clica em cima dessa": provavelmente "fica em cima" (como na frase anterior) ou "encaixa"; mantido literal.
- "Grid points, padrões de breakpoints": provavelmente "breakpoints" duas vezes; mantido literal.
- Quais artigos são (8 pontos, responsivo x adaptativo, exemplos de media query)? Os links estão no Notion, não na fala.
- `date_published` vazio.

## Raw Quotes

> "Sempre são esses números que a gente está sempre circundando."

> "Esse formulário aqui vira um botãozinho, então ele é meio que suprimido."

> "Venham aqui nos meus wireframes, vejam se tem alguma coisa errada."
