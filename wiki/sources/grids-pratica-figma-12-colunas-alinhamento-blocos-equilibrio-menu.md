---
type: source
title: "Grids na prática no Figma: 12 colunas, alinhamento em blocos e equilíbrio do menu"
aliases: ["grids prática 1", "aula prática de grids", "layout grid no Figma", "grid 72 + 36", "equilíbrio do menu"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, figma, grid, grid-de-colunas, layout, alinhamento, max-width, responsividade, flexbox, equilibrio, menu, wireframe]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-15
---

# Grids na prática no Figma: 12 colunas, alinhamento em blocos e equilíbrio do menu

## TL;DR

Primeira aula prática de grids (cerca de 19 min) do [[wiki/entities/frontpush|FrontPUSH]], depois das partes 1 e 2 teóricas (ainda não ingeridas). No [[wiki/entities/figma]], num frame Full HD (1920×1080), ele troca o grid padrão de 8 pontos pelo "do Bootstrap": **12 colunas, tipo Center**, e não Stretch, porque a tela cheia pede mais breakpoints. A largura da coluna mais o gutter dá o **max-width** do conteúdo. **72 + 36 = 1260** é o que ele mais usa, "no meio termo"; 72 + 32 = 1216; 96 + 24 = 1416 (para chegar perto dos 1440); 96 + 32 = 1504 e 96 + 36 = 1548 (para TV, perto de 1600). Ver [[wiki/concepts/grid-de-colunas]]. Na segunda parte, **"sempre pense em blocos [...] tudo é div"**: o bloco de seis colunas vira uma classe, o par de blocos menores vira flexbox dentro de flexbox, e o desenho já antecipa a responsividade ([[wiki/concepts/design-responsivo]]). O grid **"é um guia"**: ilustração de 88 ou que passa da coluna é normal se o alinhamento continua no grid. Para três elementos que não cabem em colunas exatas, agrupar e usar distribuir horizontal spacing. Por fim, o grid ajuda a **balancear o menu** ([[wiki/concepts/equilibrio-visual]]): sem o nome da empresa ao lado da logo, um lado pesa mais (1, 4, 4); com ele, 3, 4, 4. No menu de três ênfases, ele cola dois grupos para ficar 5 e quase 5.

## Key Claims

### Configurar o layout grid

- **Onde fica:** seleciona o frame, "opção Layout Grid", clica e ele adiciona. Ver [[wiki/entities/figma]].
- **O padrão do Figma é o de 8 pontos:** "ele já criou quadradinhos de 8 pontos". "Mas como eu disse para vocês, eu prefiro o do Bootstrap." Ver [[wiki/concepts/grid-de-8-pontos]] e [[wiki/entities/twitter-bootstrap]].
- **12 colunas "porque eu estou projetando para interface web, para desktop aliás".**
- **Center em vez de Stretch:** Stretch "vai ajustar ao tamanho da tela" e "sempre vai preencher a tela inteira", mas "em questão de responsividade [...] é um pouco mais trabalhoso, porque você vai ter uma série de breakpoints maior". Com Center, "a gente [define] um limite e otimiza essa parte".
- **Width e gutter:** width é "literalmente o tamanho horizontal, a largura da nossa coluna" (72); gutter "é o espaço entre as colunas" (32, 36 ou 24, "a regra dos oito pontos").

### Tabela de max-widths

As contas (12 × coluna + 11 × gutter) são do agente e batem com os valores que ele lê no Figma:

| Coluna | Gutter | Max-width | Para quê, segundo ele |
|---|---|---|---|
| 72 | 32 | 1216 | "um pouquinho menor" |
| 72 | 36 | 1260 | o principal, "meio termo" |
| 96 | 24 | 1416 | "buscar os 1440", monitores maiores |
| 96 | 32 | 1504 | "o mais exagerado", rumo aos 1600 |
| 96 | 36 | 1548 | TV, "se aproximando cada vez mais dos 1600" |

- **"Esses dois aqui são os principais para mim"**, "principalmente esse 1260". Os "dois" parecem ser 1216 e 1260; ele diz que 1260 está "no meio termo do 1440 e desse aqui". Ver [[wiki/concepts/grid-de-colunas]].
- **Olhinho e style guide:** o grid pode ficar oculto, "porque às vezes com ele o tempo todo fica muito poluído"; adicioná-lo ao guia de estilo fica para a aula de style guide.

### Pensar em blocos

- **"Sempre pense em blocos, tem que pensar do jeito que o desenvolvedor vai pegar, tudo é div, tudo é bloco."**
- **O bloco de features ocupa seis colunas** e reúne título, parágrafo e lista, "alinhado todo mundo aqui à esquerda". A distância é a mesma na horizontal e na vertical. Ver [[wiki/concepts/wireframe]].
- **Padrão vira classe:** blocos do mesmo tamanho permitem "aplicar a mesma classe nesse bloco e nesse bloco, e pedir para eles quebrarem com determinado flex-basis".
- **Flexbox dentro de flexbox:** dois blocos menores são "duas divs"; "então eu já estou projetando a minha interface com base em grids, de forma que eu tenha alinhamento, consistência". Ver [[wiki/concepts/consistencia-visual]].
- **Desenho que já pensa no dev:** "eu já vou desenhando a minha interface interpretando como é que vai ser a caixinha, como é que vai ser a responsividade, como é que eu vou deixar ele fluido ou então responsivo depois". Ver [[wiki/concepts/design-responsivo]].
- **"Eu sempre procuro deixar os textos alinhados em alguma dessas coluninhas"**, e admite "alguns wireframes que eu pequei em determinado alinhamento".

### O grid é um guia

- **"Não precisa dessa precisão exagerada, mas é um guia."** A figura pode ir para 88 ("seguindo a regra dos 8pt"). "Não necessariamente está do tamanho do grid, mas ele está alinhado."
- **Ilustrações saem do grid, e "isso é normal, perfeitamente normal"**: "minhas ilustrações doidas [...] sempre sai um pouquinho". O grid dá "um norte de como você vai projetar depois no desenvolvimento". Deslocar a ilustração para preencher mais tela "é algo que você tem que se atentar depois que você voltar para o mobile".
- **"Ele é um guia? Ele é. É bom você ter essa precisão de alinhamento? É bom"**, mas "tem determinados layouts que você não vai conseguir alinhar perfeitamente".
- **Centralizado = margens iguais:** título com "dois grids para cá, dois grids para cá"; a ilustração também com dois e dois. Uma que estava torta, ele corrige: "nem para lá e nem para cá, para poder ficar equilibrado". Um elemento grande e centralizado torto mostra "o desequilíbrio da interface". Ver [[wiki/concepts/equilibrio-visual]].
- **Exercício:** "não deixem de pegar os wireframes que eu disponibilizei para vocês no arquivo e irem verificando".

### Distribuir o que não cabe em colunas

- **Três elementos equidistantes:** agrupa, deixa "sempre sobrando um grid de um lado e um grid do outro" e usa "distribuir horizontal spacing" do Figma, que deixa o espaço "no meio das duas colunas".
- **"Um grid de 12, ele agrega muitos tamanhos, mas não todos"**: onde a divisão não fecha, os recursos de alinhamento do Figma completam.

### O grid e o equilíbrio do menu

- **Menu com CTA, busca, links e logo:** apagar o nome da empresa ao lado da logo deixa "esse lado aqui [...] mais pesado e isso visualmente incomoda". Com o nome, "balanceou mais o meu design". Ver [[wiki/concepts/equilibrio-visual]].
- **Contagem de colunas:** "se ficar 1, 4, 4 fica muito desbalanceado"; aumentar a logo ou pôr o nome deixa 3, 4, 4. Noutro exemplo, 3, 3, 3 vira 1, 3, 3 sem o nome. A leitura de que os números são colunas ocupadas por logo, links e ações é do agente.
- **Desequilíbrio proposital:** um menu com "só [...] duas pontas, uma é a minha logo, outra são as informações" já tem "a intenção de ser desequilibrado", e "se encaixa muito bem".
- **Três ênfases (links, logo, botões de ação):** espaçar tudo por igual "não ficou bem equilibrado"; "você tem que tentar deixar um pouco simétrico". A solução foi colar dois grupos "para ele virar um elemento só" e balancear "com cinco grids e aqui com quase cinco". Ver [[wiki/concepts/simetria-visual]].
- **Próximo passo prometido:** "mais modelos de responsividade no código".

## Entities

- [[wiki/entities/nasser]]: autor (inferido: a legenda está na pasta `FrontPush` do curso; mesmo grid de 12 colunas de 72 da [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt|prática de espaçamento]]; "minhas ilustrações doidas", wireframes do próprio curso).
- [[wiki/entities/frontpush]]: curso da aula (pasta da legenda); wireframes de features e de menu disponibilizados no arquivo.
- [[wiki/entities/figma]]: Layout Grid, tipos Center e Stretch, olhinho do grid, distribuir horizontal spacing.
- [[wiki/entities/twitter-bootstrap]]: o grid de 12 colunas que ele "prefere".

## Concepts

- [[wiki/concepts/grid-de-colunas]]
- [[wiki/concepts/equilibrio-visual]] (novo)
- [[wiki/concepts/grid-de-8-pontos]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/wireframe]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/simetria-visual]]
- [[wiki/concepts/harmonia-visual]]

## Tensões com a wiki

- **Gutter 32 ou 36.** Na [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt|prática de espaçamento]], o grid era 72 + 32 (1216). Aqui o principal é 72 + 36 (1260), e 1216 fica como opção "um pouquinho menor". Não é contradição: os dois aparecem como "os principais".
- **36 e "a regra dos oito pontos".** 36 não é múltiplo de 8 (é de 4). [[wiki/concepts/grid-de-8-pontos]] já registra 18, 28 e 36 como valores "por bom senso"; esta aula repete o 36 sem ressalva.
- **"O do Bootstrap" com colunas fixas.** `[external]` O grid do Bootstrap 5 tem colunas fluidas (porcentagem), gutter de 1,5rem (24 px) e containers com max-width por breakpoint (540, 720, 960, 1140, 1320) (https://getbootstrap.com/docs/5.3/layout/containers/, https://getbootstrap.com/docs/5.3/layout/gutters/). O que ele "prefere do Bootstrap" é o número 12, não as medidas: o 1260 dele fica perto do 1320 do container `xxl`.
- **Center x Stretch no Figma.** `[external]` O Figma tem quatro tipos de column grid: Stretch, Left, Center e Right. Com Center, a largura da coluna é fixa e o grid fica centralizado; com Stretch, a coluna estica e o que se fixa são as margens (https://help.figma.com/hc/en-us/articles/360040450513). A fala "do tipo Center, Stretch" junta os dois nomes, mas a escolha é Center.
- **No código.** `[skill: ux-ui-mentor]` O Center do Figma é o layout fixed da skill: `.container { max-width: 1260px; margin-inline: auto; }`, com `grid-template-columns: repeat(12, 1fr); column-gap: 36px;` dentro (com 1260 de largura, cada `1fr` dá 72). O Stretch é o fluid. A skill dá gutter de 24 no desktop e de 32 no wide (> 1440); o 36 dele fica acima dos dois.

## Open Questions

- **Partes 1 e 2 teóricas de grids**: citadas ("se você viu a parte 1 e a parte 2"), ainda não ingeridas. Os "modelos que eu falei para vocês" (32, 36 ou 24) vêm delas.
- **"O conteúdo do script-fe"**: mantido literal. Pode ser o módulo de flexbox do curso, ou "o conteúdo de CSS"; ambíguo.
- **"Agropal"**: mantido literal; pelo contexto ("então eu agrupo o elemento"), provavelmente "agrupo" ou "agrupa". Confiança média.
- **"O Figma também traz esses skills"**: mantido literal; provavelmente "recursos" de alinhamento.
- **"Esses dois aqui são os principais"**: não fica claro se o par é 1216 e 1260 ou 1260 e 1416. A leitura 1216 e 1260 é do agente, pela ordem da fala.
- **Contagens 3, 4, 3, 4 / 3, 4, 4 / 3, 3, 3**: lidas como colunas por grupo do menu; a aula não diz o que cada número mede.
- **Lacuna de cerca de 9 s** na legenda (05:19 → 05:28), entre o anúncio da aula de style guide e "Está tudo certo".
- **Exercícios** prometidos na abertura ("vou deixar alguns exercícios") não aparecem na aula, além do pedido de conferir os wireframes do arquivo.
- `date_published` vazio.

## Raw Quotes

> "Sempre pense em blocos, tem que pensar do jeito que o desenvolvedor vai pegar, tudo é div, tudo é bloco."

> "Não precisa dessa precisão exagerada, mas é um guia."

> "Os grids eles também ajudam a você saber balancear isso."

## Ver também

- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]: o mesmo grid de 12 colunas de 72, com gutter de 32, aplicado a um wireframe desalinhado
- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]: o grid de 8 pontos como escala
- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]]: simetria e eixo
- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]]: "o olho humano consegue perceber que alguma coisa está torta"
