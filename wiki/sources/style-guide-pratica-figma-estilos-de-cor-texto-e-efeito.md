---
type: source
title: "Style guide na prática no Figma (parte 1): estilos de cor, texto e efeito"
aliases: ["style guide prática 1", "aula prática de style guide", "color styles", "text styles", "effect styles", "estilos do Figma"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, figma, style-guide, design-system, design-tokens, cor, tipografia, sombra, handoff, documentacao]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-15
---

# Style guide na prática no Figma (parte 1): estilos de cor, texto e efeito

## TL;DR

Primeira aula prática de [[wiki/concepts/style-guide]] do módulo de interface web do [[wiki/entities/frontpush]], cerca de 24 min no [[wiki/entities/figma]]. A aula teórica que a precede não foi ingerida. Começa pela **documentação viva**: não espere ficar perfeito para começar a escrever, e mande **o link do arquivo** em vez de "PDF cópia versão 1, versão 2". Quem abre o link vê a edição em tempo real. Ele mostra onde buscar referências: Community do Figma (design systems, wireframes, UI Kits), com o [[wiki/entities/pegasus-design-system]] como exemplo de style guide de branding, e as guidelines de [[wiki/entities/apple]], Google ([[wiki/entities/material-design]]), Microsoft, IBM e Airbnb. Depois cria o arquivo, define a capa (set as thumbnail) e compartilha pelo Notion. A maior parte da aula é sobre os **estilos do Figma** ([[wiki/concepts/estilos-no-figma]]). Trocar um hex "colando em tudo" é "canseira"; com um estilo, **editar uma vez muda todos os elementos**. Os nomes seguem o padrão **`Grupo / nome`**: `Primary / Orange-1`, `-light` e `-dark`; `Secondary / Orange-2`; `Black / ...`. Os textos ficam em `Heads / H1` e `H2`, com grupos desktop e mobile e fonte Sora (48/36/24, line-height 110). As sombras ficam em `Shadow / Shadow purple 2`, criada com o plugin Smooth Shadow. Os nomes devem fazer sentido "para ambos os lados", design e dev.

## Key Claims

### Documentação viva e compartilhada

- **"O tanto que é importante você não esperar ficar perfeito para poder começar a escrever."** A documentação evolui. Ver [[wiki/concepts/style-guide]].
- **Link em vez de cópias:** "não ficar assim, manda um PDF com cópia versão 1, eu modifiquei, manda um cópia versão 2". Ele guarda o link do arquivo do [[wiki/entities/nubank]] no "Master File, no Notion", e quem clica "vai conseguir ver o que eu estou modificando".
- **Share:** quem tem o link pode ver ou editar; para copiar, "save local copy". No Notion, "create bookmark".
- **Labels "agregadoras" para design e dev:** "pode acontecer do design projetar uma label que não tem nada a ver com o que o dev costuma utilizar, então é legal conversar e colaborar". Ver [[wiki/concepts/estilos-no-figma]].
- **Prometido para a aula:** "a visão do desenvolvedor", "o CSS pronto da aba Inspect" e "até onde vai essa precisão". Não aparece nesta parte 1.

### Referências

- **Community do Figma:** "sempre, sempre, sempre, baixem esses arquivos". Design systems, wireframes, UI Kits; "os que têm muitos downloads assim são bons", "qualquer coisa você exclui".
- **[[wiki/entities/pegasus-design-system]] como style guide de branding:** cores; tipografia desktop e mobile; controladores; cards (Small Radius); Blur Light e Blur Dark ("cards com efeito de desfoque"); família de ícones; fotografia; elementos de composição; sistema de grids; componentes.
- **Guidelines nos "links úteis":** Apple, Google, Microsoft, IBM, Airbnb, "para poder criar variações de tudo que eu estou fazendo aqui".

### Estilos de cor

- **O problema:** aplicar `#F7931E` em vários elementos e mudar de ideia obriga a "sair colando em tudo". "Imagina um documento gigantesco [...] canseira."
- **O objetivo dos padrões no Figma:** "ganhar tanto consistência, porque a gente está aplicando uma cor só", quanto facilidade de mudar, "tanto de cor, como de tipografia, como de sombra". Ver [[wiki/concepts/consistencia-visual]].
- **Como criar:** selecionar a cor, ícone de estilos, "color styles", "+", nome com grupo: "primária espaço barra" cria o grupo `primary`. Ele nomeia `orange-1`, `orange-1-light`, `orange-1-dark`; `secondary` com `orange-2` e `orange-2-light`. Três tons por grupo.
- **Aplicar sem conta-gotas:** "em qualquer página, eu posso vir aqui nesse aba de estilos e selecionar os estilos que eu já criei".
- **Edit style:** troca o tipo do preenchimento (sólido, linear, radial, angular, diamond, image), e os elementos com o estilo "vão modificar automaticamente". **Add description** documenta o estilo no próprio Figma.
- **Detach:** o ícone "de correntinha quebrando" desvincula o estilo, e o elemento "volta para cor, como se não tivesse aplicado nenhum estilo".

### Black colors e nomes dos grupos

- **Pretos dele:** `#1A1A1A` "como cor principal de background" ("o preto que eu mais utilizo"), black light `#303030`, black dark (lido "0100"). Como o preto some no fundo preto, ele põe um stroke para indicar a amostra.
- **Nome é escolha do time:** "você pode criar os seus nomes do jeito que você quiser, isso aqui é um padrão meu". Variantes que ele já viu: brand color no lugar de primary; secondary e auxiliary; white colors e black colors separados (três tons de cada "para poder definir hierarquias textuais"); neutral colors (branco e preto juntos); gray colors, "para poder aplicar [...] hierarquia tipográfica". Ver [[wiki/concepts/cor-semantica]] e [[wiki/concepts/hierarquia-visual]].

### Estilos de texto

- **No arquivo do Nubank:** fonte Sora; heading 1, 2 e 3 em 48, 36 e 24; pesos 600, 400, 400; line-height 110 em todos. "O line-height para textos são menores", retomando a aula de [[wiki/concepts/tipografia]].
- **Peso maior nas fontes maiores:** "um peso de tipográfico um pouco maior nas fontes maiores". Ele diz "uma versão medium, que equivale a 600".
- **Criar o estilo:** text styles, "+", grupo `heads` e nome `h1`. Qualquer texto novo recebe o estilo, e "edit style" para 64 "modificou os dois, ao mesmo tempo". "A consistência melhora mil vezes."
- **Grupos por plataforma:** "eu crio o grupo de desktop, e eu crio o grupo de mobile".

### Estilos de efeito

- **Estilo serve para fill, stroke e efeitos:** drop shadow, inner shadow, layer blur, background blur. Ver [[wiki/concepts/sombra-em-interfaces]].
- **Shadow purple e shadow black:** a mesma sombra em duas cores; ela "fica um pouco mais para baixo" e não "pega todos os cantos".
- **Smooth Shadow para uma terceira:** cor roxa de branding, quatro layers, "offset bem no meio mesmo", "o mais centralizado possível". "Esse plugin de vez em quando dá pau."
- **Nome e ordem:** grupo `shadow`, nome `shadow purple 2`; os estilos podem ser reordenados ("primeiro que venha 1 e 2"). "É o mesmo processo, create style, você vai criar um grupo e o nome do elemento."

## Entities

- [[wiki/entities/nasser]]: autor (inferido: módulo "de interface web" do FrontPUSH, laranja de branding `#F7931E`, clone do Nubank no Figma, e o style guide para download prometido na aula prática de botões).
- [[wiki/entities/figma]]: color, text e effect styles; edit style; detach; share; set as thumbnail; save local copy; Community.
- [[wiki/entities/pegasus-design-system]]: referência de style guide de branding.
- [[wiki/entities/nubank]]: arquivo de estudo do autor, link no Notion, estilos de texto já criados.
- [[wiki/entities/frontpush]]: o módulo de interface web.
- [[wiki/entities/apple]], [[wiki/entities/material-design]]: guidelines citadas como referência.
- Sem página própria: Notion, fonte Sora, plugin Smooth Shadow, Microsoft, IBM e Airbnb como guidelines.

## Concepts

- [[wiki/concepts/style-guide]] (novo)
- [[wiki/concepts/estilos-no-figma]] (novo)
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/tipografia]]
- [[wiki/concepts/sombra-em-interfaces]]
- [[wiki/concepts/cor-semantica]]
- [[wiki/concepts/hierarquia-visual]]

## Tensões com a wiki

- **"Medium, que equivale a 600".** `[skill: ux-ui-mentor]` Na convenção do CSS e da maioria das fontes, 500 é Medium e 600 é Semibold (https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight). Nomear o estilo "medium" com peso 600 cria exatamente a label que "não tem nada a ver com o que o dev costuma utilizar", o problema que a própria aula aponta.
- **"Line-height de 110".** O mais provável é 110% (1.1), adequado para títulos grandes. A fala diz "para textos", mas o contexto são headings; texto corrido pede mais (cerca de 1.4 a 1.6). Ver [[wiki/concepts/tipografia]].
- **Offset da sombra: centralizado ou para baixo?** Na [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow|aula prática de botões]] a regra era "sempre é legal deixar deslocada para baixo". Aqui, no Smooth Shadow, ele quer o offset "bem no meio", "o mais centralizado possível". Os estilos shadow purple e shadow black seguem a regra antiga ("mais para baixo"). A terceira parece ser uma variante deliberada, sem explicação.
- **Nomes primitivos, não semânticos.** `[skill: ux-ui-mentor]` `Primary / Orange-1` mistura papel (primary) e valor (orange). Os design systems separam primitivos (`color-orange-500`) de semânticos (`color-brand-primary`) para poder trocar a cor sem renomear. A aula chega perto quando cita "brand color", mas não faz a distinção.
- **Styles x Variables.** `[external]` Desde 2023 o Figma tem **Variables**, com modos (light/dark, marcas) e aliases. Para tokens de cor e número costumam substituir os color styles; text e effect styles continuam como estilos (https://help.figma.com/hc/en-us/articles/15339657135383, não reconsultado nesta ingestão). A aula usa só styles.
- **"Aba Inspect".** `[external]` Desde 2023 o Inspect com CSS fica no **Dev Mode** do Figma (https://help.figma.com/hc/en-us/articles/15023124644247, não reconsultado nesta ingestão). A promessa de mostrar "até onde vai essa precisão" fica para a parte 2.

## Open Questions

- **"Nos Finalmente"**: provavelmente a expressão "nos finalmentes" (na reta final do módulo). Mantido literal.
- **"Na Acer tem como a gente copiar os seus arquivos"**, **"a aba de Instagram"** (no Notion), **"quatro pontinhos que têm um âmbito de três"** (ícone de estilos), **"visual style"** (talvez detach style), **"scriptwd-style-guide"** (nome do arquivo): ambíguos, mantidos literais.
- **Black dark "0100"** e **"1a, 1 0, 1 0, 1 0"**: talvez `#010101` e `#101010`. Não dá para decidir pela fala.
- **Aba Inspect, visão do dev, componentes**: prometidos, não cobertos nesta parte.
- **Aula teórica de style guide** ("a primeira aula, um pouco mais teórica"): não ingerida.
- `date_published` vazio.

## Raw Quotes

> "Imagina um documento gigantesco, você tendo que modificar todas as cores do seu projeto, canseira."

> "Pode acontecer do design projetar uma label que não tem nada a ver com o que o dev costuma utilizar, então é legal conversar e colaborar."

> "Você pode criar os seus nomes do jeito que você quiser, isso aqui é um padrão meu."

## Ver também

- [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]]: onde o style guide para download foi prometido; Smooth Shadow e Pegasus
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]]: cor de branding desconectada do estilo para mudar a opacidade
- [[wiki/sources/mobile-design-system]]: camadas de tokens em um design system de código
