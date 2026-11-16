---
type: source
title: "Style Guide na prática (parte 2): o que documentar para o desenvolvedor"
aliases: ["StyleGuide Prática 2", "style guide prática 2", "documentação para o dev", "handoff no Figma", "mapa de design"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, figma, style-guide, handoff, documentacao, box-shadow, gradiente, border-radius, estados, hover, css, interfaces-web]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-15
---

# Style Guide na prática (parte 2): o que documentar para o desenvolvedor

## TL;DR

Aula curta (cerca de 4 min) do módulo de Interfaces Web do [[wiki/entities/frontpush]], aula 16, logo depois da parte 1, em que se criaram estilos de texto, cor e efeito no [[wiki/entities/figma]]. O [[wiki/concepts/style-guide]] existe para dar consistência "tanto no Figma, tanto na documentação". Esta parte trata do que passar ao desenvolvedor ([[wiki/concepts/handoff-design-dev]]), usando um card como exemplo. **Documente sempre** o que é refino de design: gradiente (orientação, inclinação, onde cada cor começa), camadas de `box-shadow`, cor em RGBA e hexadecimal, [[wiki/concepts/border-radius]] **proporcional ao tamanho do card** (38 px no exemplo). **Não leve em conta** o posicionamento que o Figma gera, porque no código o layout é flexbox e grid, não `position`. Dimensões entram quando importam. No botão, prefira documentar o **padding** (48 px de cada lado no exemplo) a uma largura fixa. A sombra de quatro camadas se copia do Inspect ([[wiki/concepts/sombra-em-interfaces]]). Cada módulo (card, ícone, input) ganha **três estados**: normal, hover e clicável ([[wiki/concepts/feedback-do-sistema]], [[wiki/concepts/maquina-de-estados-ui]]). A frase-síntese: o style guide é "o mapa que traduz o design para o CSS". O projeto Nubank ([[wiki/entities/nubank]]) vai servir de case.

## Key Claims

### O objetivo do style guide

- **Consistência nos dois lados:** "configurar alguns padrões para poder a gente ter consistência tanto no Figma, tanto na documentação, que esse é o objetivo do style guide". Ver [[wiki/concepts/style-guide]] e [[wiki/concepts/consistencia-visual]].
- **Três estilos principais** criados na aula anterior: "estilos de texto, de cor e de efeito". Eles se aplicam "de N formas" e o tema volta "com o decorrer dos projetos".
- **Mapa de design:** "é o mapa que traduz o design para o CSS da melhor forma possível".

### O que sempre documentar

- **O ponto de vista do dev:** "eu preciso passar quais são essas informações desse card para o desenvolvedor, quais são as informações que realmente são importantes". Ver [[wiki/concepts/handoff-design-dev]].
- **Refino de cor e sombra:** "o linear-gradient, qual é a orientação, qual é a inclinação, quantas camadas de box-shadow têm". "Aqueles que são mais relacionados a design mesmo [...] são sempre muito importantes de você colocar na descrição. Sempre, sempre, sempre."
- **Box-shadow do Inspect:** "para o desenvolvedor é muito complicado dizer quais são as sombras do CSS", então "não deixe de vir aqui e copiar sempre esse box-shadow". O Figma já entrega o RGBA, as opacidades e as camadas: "quatro camadas de drop-shadow para poder dar esse efeito". O caminho é "inspect, copia e cola, Ctrl-C, Ctrl-V". Ver [[wiki/concepts/sombra-em-interfaces]].
- **Documentação mais branda:** depois de colar, "sempre deixa ele um pouco mais brando assim, para poder dar essa hierarquia", "para poder ficar bem leve". Ver [[wiki/concepts/hierarquia-visual]]. (Leitura provável: o bloco de código na prancha do style guide fica visualmente discreto.)
- **"Com relação ao estilo em si, o Figma acerta muito."**
- **Gradiente:** aplicável "de forma nativa no CSS3" com "o background-linear-gradient". Ele lê a inclinação de "220 deg" e as paradas: "14,43% é onde começa essa cor e 85% é onde começa essa cor". "É muito importante você copiar esse background-linear, ou então mostrar como ele busca esse tipo de informação no arquivo."
- **Cor em dois formatos:** "tanto em CSS, que é o RGBA, muito comum de utilizar, tanto como hexadecimal, esses dois são os mais utilizados."

### Border-radius proporcional

- **"Super importante, porque o border-radius varia de acordo com o tamanho do card."** Com o mesmo radius num card pequeno, "olha só o que ele vira". Num card muito grande, "perde a identidade dele ter esse arredondadinho".
- **Regra:** "o border-radius precisa ser relativo, conforme o tamanho do card". Documente "quais os tamanhos do card que você está colocando e, juntamente, com o tamanho do border-radius". No card da aula, 38 px. Ver [[wiki/concepts/border-radius]].

### Dimensões e padding

- **Posicionamento automático do Figma, "nem tanto"**: "eu acho que não condiz muito com a realidade, não é assim que a gente aplica quando a gente está codando". O Inspect dá width e height, "beleza".
- **No botão, a dimensão importa:** "faço questão de deixar claro qual o tamanho que eu quero e muitas vezes eu posso até estabelecer o padding". A largura fixa não é obrigatória, "porque depende do conteúdo do texto". Ver [[wiki/concepts/botoes-em-interfaces]].
- **Exemplo ao vivo:** ele testa 16, 32, 36, 40 e fica em 48 px de cada lado, "indicando para ele que você quer um text-button, um padding aqui de um lado e de outro de 48 pixels". Depois volta ao estado anterior, porque ainda está editando o arquivo.
- **Cards:** o tamanho se especifica "traçando uma setinha de um lado e uma setinha do outro, uma linha guia".

### Position contra flexbox e grid

- **"O que não dá para levar muito em consideração é o position"**: "é muito difícil a gente utilizar o position para poder layoutar, não estou falando que é impossível, mas tendo o flexbox e o grid". Essas informações "quase sempre são totalmente descartadas quando a gente fala de layout".
- **O contraponto:** "quando a gente fala de design, de sombra, de cores, de linear, esses são sempre aspectos muito importantes da gente deixar documentado".

### Três estados por módulo

- **Normal, hover e clicável:** "cria o modo normal, cria o modo hover, quando você passa o mouse e cria o modo clicável, que quando você clica é o que ele fica". "Eu sempre costumo criar esses três módulos no card", e o mesmo vale para ícones. Ver [[wiki/concepts/feedback-do-sistema]] e [[wiki/concepts/maquina-de-estados-ui]].
- **Inputs:** "o modo quando ele está inativo, quando eu passo o mouse em cima, quando eu deixo e clico".
- **O que muda entre estados:** "quais são as características de design que mudam de um para o outro, qual é esse verde, esse verde eu já deixei especificado aqui".
- **Próximos passos:** "eu vou enfatizar isso nos projetos [...] principalmente do Nubank que vai servir de case". Ver [[wiki/entities/nubank]].

## Entities

- [[wiki/entities/nasser]]: autor (inferido). O nome não é dito. A aula está na pasta do FrontPUSH, módulo de Interfaces Web, e fala com a mesma voz e os mesmos hábitos das aulas de UI Design: style guide prometido na aula prática de botões, sombra de várias camadas, padding em vez de largura fixa.
- [[wiki/entities/figma]]: Inspect (width, height, CSS do box-shadow e do gradiente), aba Design para mudar o padding.
- [[wiki/entities/frontpush]]: curso de onde vem o módulo de Interfaces Web.
- [[wiki/entities/nubank]]: projeto-case anunciado.

## Concepts

- [[wiki/concepts/style-guide]] (novo)
- [[wiki/concepts/handoff-design-dev]] (novo)
- [[wiki/concepts/sombra-em-interfaces]]
- [[wiki/concepts/border-radius]]
- [[wiki/concepts/botoes-em-interfaces]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/feedback-do-sistema]]
- [[wiki/concepts/maquina-de-estados-ui]]
- [[wiki/concepts/hierarquia-visual]]

## Tensões com a wiki

- **Três estados contra sete.** `[skill: ux-ui-mentor]` A referência de handoff lista default, hover, focus, active, disabled, loading e error. A aula cobre três: normal, hover e clicável (o active). Faltam **focus**, que é obrigatório para navegação por teclado, e **disabled**. O "inativo" do input pode ser o default ou o disabled; a fala não deixa claro.
- **"background-linear-gradient" não é uma propriedade.** `[external]` Em CSS, `linear-gradient()` é um valor da propriedade `background` (ou `background-image`): `background: linear-gradient(220deg, cor1 14.43%, cor2 85%)`. Os percentuais são as posições das paradas de cor (https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/linear-gradient). "85% é onde começa essa cor" está certo para a segunda parada; antes dos 14,43%, a primeira cor fica sólida, e depois dos 85%, a segunda.
- **Hover em card.** `[skill: ux-ui-mentor]` Hover não existe no toque, como já registrado em [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]]. O estado clicável precisa de par visual fora do mouse.
- **Radius "relativo".** `[external]` Em CSS, `border-radius` em porcentagem é relativo à largura e à altura do elemento e vira elipse em retângulos; não é o "relativo" da aula. O que a aula pede é um radius por tamanho de card. `[skill: ux-ui-mentor]` Na prática, tokens como `radius-sm`, `radius-md`, `radius-lg`, um por tamanho de componente.
- **Position descartado.** `[external]` O Auto Layout do Figma corresponde ao flexbox (direção, gap, padding, alinhamento), e o CSS que o Figma gera para frames com Auto Layout usa `display: flex` (https://help.figma.com/hc/en-us/articles/360040451373). O "position" que a aula descarta vem de frames sem Auto Layout, que saem com coordenadas absolutas. A aula da parte prática de botões media o padding à mão pelo mesmo motivo.
- **Cor só em hex e RGBA.** `[skill: ux-ui-mentor]` A skill pede nome de token ao lado do valor (`color-interactive-default`, não só `#hex`). A aula documenta o valor sem nome.

## Open Questions

- **Partes anteriores não ingeridas:** "14 - StyleGuide" (teoria) e "15 - StyleGuide Prática 1" (estilos de texto, cor e efeito no Figma). Também as aulas 01 a 13 do mesmo módulo (usabilidade, acessibilidade, wireframes, grids). Esta é a primeira aula do módulo de Interfaces Web na wiki.
- **"O picola até o final"**: mantido literal. Talvez "copia e cola", "aplica" ou "e coloca"; ambíguo.
- **"Se eu der algum tipo de arquivo para ele"**: provavelmente "se eu der algum tipo de [conteúdo/texto]"; mantido literal.
- **"A proposta está muito errada"**: ele parece falar do arquivo de proposta ainda em edição; o style guide para download ainda não foi entregue.
- **Lacuna na legenda** de cerca de 11 s (01:20 → 01:31), provavelmente o Figma carregando ("desculpa ele ter travado").
- **Autoria inferida** (Násser), como explicado em Entities.
- `date_published` vazio.

## Raw Quotes

> "É o mapa que traduz o design para o CSS da melhor forma possível."

> "O border-radius precisa ser relativo, conforme o tamanho do card."

> "Tendo o flexbox e o grid, é muito difícil de utilizar essas informações aqui."

## Ver também

- [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]]: a sombra de várias camadas e o hover "muito bem claro no meu style guide"
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]]: ícones em cards, "um spoiler [...] da aula de style guide"
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]: botões consistentes em altura, padding e radius
