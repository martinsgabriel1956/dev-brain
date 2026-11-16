---
type: source
title: "Botões na prática no Figma (edição \"W7\"): padding, gradiente, contraste e sombras suaves"
aliases: ["aula prática de botões W7", "botões no Figma", "smooth shadow", "sombra de botão", "receita de drop shadow"]
date_created: 2026-11-14
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, figma, botoes, padding, gradiente, contraste, sombra, drop-shadow, hover, design-system]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-14
---

# Botões na prática no Figma (edição "W7"): padding, gradiente, contraste e sombras suaves

## TL;DR

A aula prática (cerca de 10 min) que [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] prometeu, feita no [[wiki/entities/figma]]. O botão tem **56 px de altura** (mínimo de 44, ver [[wiki/concepts/area-clicavel]]) e o padding lateral é medido à mão: 64 de cada lado, depois 96. Ele lembra que "no CSS é muito fácil", porque o padding acompanha o conteúdo. O fundo leva o **gradiente da marca**, que "enche mais os olhos do que uma cor sólida". O texto, branco ou preto, se escolhe pela [[wiki/concepts/contraste|legibilidade]]: no amarelo, só o preto funciona. Radius de 16, texto de 16 ([[wiki/concepts/border-radius]], [[wiki/concepts/tipografia]]). A maior parte da aula é **sombra** ([[wiki/concepts/sombra-em-interfaces]]). Primeiro o plugin **Smooth Shadow**, com quatro a seis layers de drop shadow, alpha baixo, offset para baixo e blur. Depois o [[wiki/entities/pegasus-design-system]] como referência (y 32, blur 64, 8% de #111). Por fim o "curinga" sem plugin: y 16, **blur igual ou o dobro do offset** (32), **cor da marca a no máximo 40%** (ele usa 25%) e **spread negativo** (−10 a −16). Assim a sombra cobre cerca de **80% do elemento**, só embaixo, e vira o hover a ser documentado no style guide.

## Key Claims

### Altura e padding

- **"Coloque um mínimo de 44 pixels"**; ele usa 56. Ver [[wiki/concepts/area-clicavel]].
- **Atalhos:** Ctrl D ou Ctrl C, Ctrl V para duplicar o texto; botão direito, "bring to front", para trazê-lo à frente. Ver [[wiki/entities/figma]].
- **Padding medido à mão:** o texto tem 108 de largura, e ele deixa 64 de cada lado. "O próprio Figma faz essas medições para a gente de forma automática", "vai traçando as linhas".
- **"No Figma é um pouco difícil de controlar isso, mas no CSS é muito fácil, porque ele vai ajustar o padding de acordo com o conteúdo."** É a regra da aula teórica, padding igual e largura pelo texto ([[wiki/concepts/botoes-em-interfaces]]).
- **O valor é flexível:** "Tem como colocar um pouco mais? Tem", "não é uma regra que a gente leva muito ao pé da letra". Ele passa para 96. Ver [[wiki/concepts/escala-de-espacamento]].

### Branding, gradiente e contraste

- **"Sempre coloque o branding da sua marca"**; no caso dele, um gradiente laranja. "O gradiente é mais bonito, enche mais os olhos do que uma cor sólida." A cor sólida "é legal, sim, dependendo da interface do branding que você tem", mas "sempre que possível tente aplicar um gradiente".
- **"Garantir a melhor legibilidade possível"**: no laranja, branco ou preto servem. "Lógico que o preto vai ter um contraste melhor, mas o branco não fica tão estourado." No amarelo, "com certeza [...] eu teria que colocar preto". Ver [[wiki/concepts/contraste]].
- **Radius 16 e texto 16**, "meio que esquematizado". Os padrões de tamanho de texto ficam para tipografia e para o style guide da parte de interfaces web, que "vai ficar para download". Ver [[wiki/concepts/border-radius]] e [[wiki/concepts/tipografia]].
- **"A grande questão do momento é saber aplicar o efeito hover e como a gente exporta depois isso para o CSS."** Ver [[wiki/concepts/feedback-do-sistema]].

### Plugin Smooth Shadow

- **Objetivo:** "deixar as sombras as mais realistas possíveis". Ver [[wiki/concepts/sombra-em-interfaces]].
- **Layers:** "quanto mais camadas de drop shadow você aplica, teoricamente mais realista fica a sua sombra"; "eu sempre aplico quatro ou seis layers".
- **Gradação:** "a sombra que é mais perto tem uma opacidade maior". As mais afastadas ficam "mais transparentes", "dando aquela sensação de penumbra".
- **Controles:** alpha "bem pouquinho mesmo"; offset "é literalmente o deslocamento da sombra", e "sempre é legal deixar deslocada para baixo"; blur "é justamente o quão desfocado está a sombra"; color recebe o hexadecimal da cor da marca.
- **O offset do plugin precisa de ajuste:** "o offset deles não fica muito bom". Ele remete às "regrinhas lá no meu post".
- **Sombra embaixo, não em volta:** "não é para ficar ao redor de tudo, é para ficar na parte de baixo, compreendendo aqui mais ou menos 80%". "São sombras bem suaves mesmo."

### Referência: Pegasus Design System

- **Onde achar:** "community do Figma, Pegasus design system". Ver [[wiki/entities/pegasus-design-system]].
- **Sombra dos cards:** duplo clique no elemento, depois "edit style" na propriedade. Valores lidos: "32 para baixo, um blur de 64, 100 spread e 8% na cor 111, que é um cinza escuro".
- **"Vocês vão conhecendo os padrões de design system famosos e bonitos visualmente e literalmente copia para suas interfaces."** Uma aula só de sombras é anunciada.

### O "curinga" sem plugin

- **Offset para baixo e blur "o dobro ou igual"**: y 16, blur 32, "o dobro ou até um pouquinho mais". "Não é uma regra, mas é meio que um caminho."
- **Cor da marca, "no máximo 40%"**; ele baixa para 25%.
- **Spread negativo** para a sombra "encurtar e ficar a 80% do elemento": −10, depois −12, −16. "Percebe que já ficou bem mais suave."
- **Vira o hover:** "eu vou controlando o efeito hover para quando eu passar o mouse e deixar isso muito bem claro no meu style guide". Ver [[wiki/concepts/feedback-do-sistema]].

## Entities

- [[wiki/entities/nasser]]: autor (inferido: "aquelas regrinhas lá no meu post" retoma "um post no meu Instagram" da aula teórica; mesmo botão de 56 px, gradiente laranja, radius 16 e texto 16 do slide daquela aula).
- [[wiki/entities/figma]]: ferramenta da aula; medições automáticas, bring to front, edit style, Community.
- [[wiki/entities/pegasus-design-system]] (novo): referência de sombra em cards.
- Sem página própria: plugin Smooth Shadow.

## Concepts

- [[wiki/concepts/sombra-em-interfaces]] (novo)
- [[wiki/concepts/botoes-em-interfaces]]
- [[wiki/concepts/area-clicavel]]
- [[wiki/concepts/contraste]]
- [[wiki/concepts/border-radius]]
- [[wiki/concepts/escala-de-espacamento]]
- [[wiki/concepts/tipografia]]
- [[wiki/concepts/feedback-do-sistema]]

## Tensões com a wiki

- **"80% do elemento" resolvido.** Em [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]], a expressão foi lida como a opacidade 0.8 da sombra de hover do slide, com confiança média. Esta aula mostra outro sentido: **a sombra cobre cerca de 80% do elemento**, só embaixo, encurtada pelo spread negativo. O slide daquela aula (`0px 4px 25px -10px`) já tinha spread negativo. O 0.8 do slide continua sendo opacidade, mas não é o que "80%" quer dizer.
- **"Mais opacas, mais transparentes".** A fala diz que as sombras afastadas ficam "mais opacas" e corrige para "mais transparentes" logo em seguida. Pelo contexto ("a mais perto tem uma opacidade maior"), vale a segunda. O raw mantém a fala.
- **Padding de 64 e 96 contra a escala.** A aula teórica manda tirar o padding da escala adotada ([[wiki/concepts/escala-de-espacamento]]). Os dois valores são múltiplos de 8 ([[wiki/concepts/grid-de-8-pontos]]), mas 96 não está na escala geométrica 2, 4, 8, 16, 32, 64 que ele prefere. Ele mesmo diz que "não é uma regra".
- **"No Figma é difícil de controlar".** `[external]` O Auto Layout do Figma faz o mesmo que o CSS: padding fixo e largura que cresce com o texto (https://help.figma.com/hc/en-us/articles/360040451373). A aula mede à mão.
- **Texto branco sobre gradiente.** `[external]` Com texto de 16 px (não é "texto grande"), a WCAG 1.4.3 pede 4,5:1. No gradiente, a conta vale no ponto mais claro, não na média (https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). "Não fica tão estourado" é julgamento visual, sem medição. Laranja claro com branco costuma ficar abaixo de 4,5:1.
- **Sombra só em hover.** `[skill: ux-ui-mentor]` Hover não existe no toque; a sombra de hover precisa de par em focus e active. No dark mode, sombra some e a elevação passa para superfícies mais claras ou bordas sutis.
- **Pegasus "100 spread".** Spread positivo de 100 alargaria muito a sombra, o oposto do que a aula ensina. Pode ser leitura errada do painel (outro campo, ou −100 com y 32 e blur 64). Não verificado.

## Open Questions

- **Smooth Shadow:** `[external]` provavelmente o plugin de Philipp Brumm, que empilha camadas de `box-shadow` com opacidade decrescente (https://shadows.brumm.af/). Não confirmado na aula; confiança média.
- **"Em soma eu deixo assim"**, **"as sombras atacando"**, **"um belo grau do que você aplica"**: mantidos literais. Talvez "em suma", "destacando", "graph"; ambíguos.
- **"Na cor 111"**: lido como `#111111` (cinza escuro, como ele diz). Confiança média.
- **"Vai ter uma sessão só para a gente trabalhar com sombras"**: prometida, ainda não ingerida. O style guide foi entregue em [[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]].
- **Post das "regrinhas" de drop shadow** (Instagram): não consultado.
- `date_published` vazio.

## Raw Quotes

> "No Figma é um pouco difícil de controlar isso, mas no CSS é muito fácil, porque ele vai ajustar o padding de acordo com o conteúdo."

> "Não é para ficar ao redor de tudo, é para ficar na parte de baixo, compreendendo aqui mais ou menos 80%."

> "Geralmente eu aplico um blur que seja o dobro ou igual."

## Ver também

- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]: a aula teórica; anatomia, 44 px, hover com sombra da cor do botão
- [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]]: as seis formas de botão
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]: medir distâncias no Figma (Alt, nudge de 8)
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]]: cor de branding desconectada do estilo para mudar a opacidade
- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]: a aula teórica de style guide, onde o hover de sombra é documentado
- [[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]: a aula prática de style guide (parte 1): estilos de cor, texto e efeito
- [[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]]: o style guide prometido: copiar o box-shadow do Inspect e documentar os estados
