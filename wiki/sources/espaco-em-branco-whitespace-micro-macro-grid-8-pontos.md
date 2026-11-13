---
type: source
title: "Elementos da interface: espaço em branco (whitespace), parte 1"
aliases: ["aula whitespace", "aula espaço em branco", "micro e macro espaço", "grid de 8 pontos aula"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, elementos-da-interface, espaco-em-branco, whitespace, grid-de-8-pontos, espacamento, lei-da-proximidade, consistencia, wireframe, figma]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/espaco-em-branco-whitespace-micro-macro-grid-8-pontos.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Elementos da interface: espaço em branco (whitespace), parte 1

## TL;DR

Primeira aula de elemento do módulo "elementos da interface" do [[wiki/entities/frontpush|FrontPUSH]], de [[wiki/entities/nasser|Násser]]. Trata o [[wiki/concepts/espaco-em-branco]] (whitespace, espaço negativo), que o roteiro anterior chamava de "espaçamento e linhas". Define o conceito como o espaço vazio **entre** ou **ao redor** dos elementos e o divide em dois: **macro espaço**, ao redor, que dá foco e ênfase (home do [[wiki/entities/google]]); e **micro espaço**, entre elementos, que agrupa quando é pequeno e separa quando é grande ([[wiki/concepts/lei-da-proximidade-gestalt]]). Mostra isso num [[wiki/concepts/wireframe]] de menu no [[wiki/entities/figma]] e nos resultados de busca do Google, que agrupam sem bordas, só com espaço e recuo. Fecha com o [[wiki/concepts/grid-de-8-pontos]]: uma escala de "bons números" múltiplos de 8, usada com bom senso, para dar [[wiki/concepts/consistencia-visual]] aos espaçamentos. O slide lista mais quatro benefícios (respiro, personalidade, hierarquia, legibilidade) que ficam para a parte 2.

## Key Claims

### O que é

- **Whitespace, ou espaço negativo, é o espaço vazio entre ou ao redor dos elementos.** Slide e fala coincidem. Ver [[wiki/concepts/espaco-em-branco]].
- **Exemplo: landing page do [[wiki/entities/frontpush]]** com caixas vermelhas (espaço ao redor) e azuis (espaço entre): logo, título, subtítulo, ícone de apresentação, CTAs e margens.
- **Slide com os benefícios:** micro e macro espaço >> grid de 8 pontos; ajuda a dar ênfase; pausa no conteúdo, respiro; personalidade; hierarquia; legibilidade. Só os dois primeiros são explicados nesta parte.

### Macro espaço: foco

- **Macro espaço é o espaço ao redor de um elemento; ele dá foco ao que se quer destacar.** Os vermelhos do exemplo são macro.
- **Ligação com comportamento** (fator de [[wiki/concepts/contexto-do-usuario]] da aula de introdução): numa tela toda preta com uma bolinha de bom destaque no centro, o olhar vai para a bolinha "automaticamente".
- **Home do [[wiki/entities/google]]:** logo (às vezes doodle comemorativo), input com teclado virtual e voz, "Pesquisa Google" e "Estou com sorte", cercados de espaço em branco. A chance de errar como pesquisar é "muito pequena". O autor nota que a maioria das pessoas não sabe explicar o "Estou com sorte" e só usa a pesquisa. Também afirma que qualquer mudança mínima nessa página "deve ter um impacto gigantesco" pela escala de uso (sem dado).

### Micro espaço: juntar ou separar

- **Espaço grande entre dois elementos os separa; espaço pequeno indica que estão agrupados.** Ver [[wiki/concepts/lei-da-proximidade-gestalt]].
- **Exemplo de [[wiki/concepts/wireframe]] de menu:** logo circular de 72 × 72 na cor da marca (azul), links Home, Sobre e Contato em body B2 (16 px, "se não me engano") com a mesma distância entre si, e um CTA retangular ("Sign In" no print) do outro lado. Os vãos grandes (vermelhos) separam logo, links e CTA; os pequenos (azuis) unem os links numa mesma hierarquia. "São três elementos diferentes e eu consegui denotar isso somente com o espaçamento."
- **Wireframe é "um pequeno protótipo de uma tela"**, de alta ou média fidelidade.

### Resultados de busca do Google

- **O Google agrupa e separa resultados só com espaçamento, sem linhas de card.** Num print da busca por "Figma", a distância entre anúncio e título é menor que a distância até o bloco seguinte, então o anúncio e o título formam um grupo, "como se fosse um mesmo card".
- **Recuo (tabulação) indica pertencimento.** Um bloco abaixo, a uma distância maior, mas recuado à esquerda, é lido como parte do bloco de cima. O bloco seguinte, com a mesma tabulação do principal e distância maior, é outro grupo.
- O contraste é com o próprio [[wiki/entities/figma]], cuja interface delimita cards com linhas.

### Grid de 8 pontos

- **Pergunta-guia:** que espaço definir de um elemento para outro, e por que um vão é maior que o outro? Ver [[wiki/concepts/grid-de-8-pontos]].
- **O grid de 8 pontos serve ao princípio da [[wiki/concepts/consistencia-visual|consistência]]:** estabelecer uma escala e usá-la em toda a interface para ter consistência visual e uma interface "mais agradável".
- **É "um conjunto de bons números" múltiplos de 8**, usados para criar qualquer elemento, não só espaços (exemplo: altura de botão). Fala: 16, 32, 40, 48, 56, 64, 72, 80, 88, 96. Slide do Figma: 2, 4, 8, 16, 18, 24, 28, 32, 36, 40, 48, 56, 64, 72, 80, 88, 96.
- **Não é regra rígida:** 18 (par, meio-termo entre 16 e 24), 24, 28 e 36 também valem; "envolve muito do bom senso".
- **A distância medida no exemplo do Google é 28 pontos** (fala; não fica claro qual dos vãos).

### Aplicando: título, descrição e CTA

- **Título (h1) e descrição (corpo, 18) são conectados:** o título chama atenção por contraste e tamanho; a descrição detalha. O vão medido era 10 px; pode ir a 8 ou 4 px porque a altura de linha do título já dá espaço. Ver [[wiki/concepts/hierarquia-visual]].
- **Do bloco de texto ao call to action, espaço maior (40 ou 48):** "aqui eu estou comunicando e aqui eu estou chamando ele para a ação". É micro e macro aplicados com o grid de 8.
- A aula termina dividida em duas partes; a parte 2 ainda não foi ingerida.

## Entities

- [[wiki/entities/nasser]]: autor (voz e curso; o nome não é dito nesta aula).
- [[wiki/entities/frontpush]]: landing page com as caixas de espaço; arquivo "FrontPUSH 2.0" aberto no Figma.
- [[wiki/entities/google]]: home como macro espaço; busca como agrupamento por espaço e recuo.
- [[wiki/entities/figma]]: ferramenta do wireframe e da análise do print.

## Concepts

- [[wiki/concepts/espaco-em-branco]]
- [[wiki/concepts/grid-de-8-pontos]] (novo)
- [[wiki/concepts/wireframe]] (novo)
- [[wiki/concepts/lei-da-proximidade-gestalt]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/contraste]]
- [[wiki/concepts/simplicidade-visual]]
- [[wiki/concepts/contexto-do-usuario]]
- [[wiki/concepts/elementos-da-interface]]
- [[wiki/concepts/ui-design]]

## Tensões com a wiki

- **O que é macro.** A aula chama de macro o espaço **ao redor** de um elemento (foco) e de micro o espaço **entre** elementos (agrupar e separar). `[skill: ux-ui-mentor]` A skill usa outro corte: macro é o espaço entre seções e blocos grandes; micro é o espaço entre elementos, padding interno e line-height. Os dois concordam que o espaço pequeno agrupa; divergem em onde fica a fronteira. Na prática da própria aula, o vão entre logo, links e CTA (vermelho) é "entre" elementos e funciona como macro, o que fica mais perto do corte da skill. Registrado em [[wiki/concepts/espaco-em-branco]].
- **"Múltiplos de 8" com 18, 28 e 36.** O slide chama a lista de múltiplos de 8, mas 2, 4, 18, 28 e 36 não são. `[skill: ux-ui-mentor]` A skill resolve parte disso com o sub-grid de 4 px (4, 28 e 36 são múltiplos de 4); 18 não cabe em nenhum dos dois. O autor admite a exceção por bom senso. Ver [[wiki/concepts/grid-de-8-pontos]].
- **Sem conflito** com [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]], onde o espaço em branco aparece como ferramenta de simplicidade com a mesma home do Google. Esta aula acrescenta o micro espaço e a escala numérica.
- **Escala linear x geométrica.** Em [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]] (edição "W7"), o autor prefere a escala geométrica (2, 4, 8, 16, 32, 64) à linear; o grid de 8 desta aula é praticamente linear de passo 8. Ver [[wiki/concepts/escala-de-espacamento]].

## Open Questions

- "Vou dar um espaço maior, porque não são informações diferentes": pela lógica da frase seguinte ("aqui eu estou comunicando e aqui eu estou chamando para a ação"), provavelmente quis dizer "porque são informações diferentes". Mantido literal no raw.
- "28 pontos" responde a qual vão do print do Google? A fala não diz.
- "Desse anúncio HTTPS ao ar e tudo mais": trecho ambíguo da legenda, provavelmente o bloco anúncio, HTTPS e URL do resultado.
- Parte 2 (pausa e respiro, personalidade, hierarquia, legibilidade) ainda não ingerida.
- `date_published` vazio; o Figma mostra "FrontPUSH 2.0".

## Raw Quotes

> "Ele pode ser chamado de espaço negativo, é o espaço vazio entre ou ao redor dos elementos."

> "São três elementos diferentes e eu consegui denotar isso somente com o espaçamento."

> "Somente com o espaçamento ele consegue separar ou agrupar grupos de elementos."

> "Eu não posso generalizar que eu só vou utilizar múltiplos de oito."
