---
type: source
title: "Grids, parte 1 (edição \"W7\"): estrutura em colunas, Bootstrap, regra de oito pontos e responsividade"
aliases: ["grids pt. 1", "aula de grids W7", "fixo fluido adaptativo responsivo", "introdução a grids"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, grid, grid-de-colunas, grid-de-8-pontos, bootstrap, responsividade, breakpoint, media-query, layout, alinhamento, consistencia, css]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-15
---

# Grids, parte 1 (edição "W7"): estrutura em colunas, Bootstrap, regra de oito pontos e responsividade

## TL;DR

Aula introdutória (cerca de 17 min) do módulo de interface web. Grid é "a estrutura básica, o esqueleto para o seu design": colunas onde os elementos são colocados e alinhados ([[wiki/concepts/grid-de-colunas]]). Serve aos dois lados. Para o designer, dá alinhamento, distâncias consistentes e organização ([[wiki/concepts/consistencia-visual]]). Para o dev, é o caminho para resoluções, breakpoints e "a tão famigerada responsividade" ([[wiki/concepts/design-responsivo]]). Exemplo: a landing page do [[wiki/entities/frontpush]], com 12 colunas imaginárias divididas em 7–8 + 4–5, e 4 + 8 no design. Os dois padrões mais usados são o grid do [[wiki/entities/twitter-bootstrap|Bootstrap]] (colunas por tipo de dispositivo, larguras padrão) e a regra de oito pontos, querida por Android e iOS ([[wiki/concepts/grid-de-8-pontos]]). Os dois "se complementam". A maior parte da aula compara quatro tipos de layout ([[wiki/concepts/layout-fixo-fluido-adaptativo-responsivo]]). **Fixo** serve para uma tela só, como o iPad da pizzaria. **Fluido** usa largura em porcentagem e encolhe junto com a tela, mas não quebra para a vertical. **Adaptativo** usa media query e troca de estilo num [[wiki/concepts/breakpoint]], como 960 px. O **responsivo** mistura os dois e é "o queridinho", porque há aparelhos demais para fazer adaptativo. Ele fecha com o wireframe alinhado às colunas: "quanto que tem de distância de um elemento para o outro? Ah, é uma coluna."

## Key Claims

### O que é e para quem serve

- **Definição (fala e slide):** "os grids criam a estrutura básica, o esqueleto para o seu design"; no slide, "são colunas onde os elementos são colocados e alinhados". Ver [[wiki/concepts/grid-de-colunas]].
- **Grid é um padrão**, "criado para poder a gente conseguir os elementos fundamentais do design e [...] da responsividade".
- **Do lado da responsividade:** resoluções, breakpoints e "distâncias padronizadas de forma que, se eu tenho um padrão, eu consigo adaptar ele em vários tamanhos de tela". Ver [[wiki/concepts/breakpoint]].
- **Do lado do design:** elementos alinhados, "consistência de distância", aparência organizada, "uma sensação mais clean". Ver [[wiki/concepts/consistencia-visual]].
- **Liga os módulos:** "muito do que eu falei em wireframes também se encaixa" ([[wiki/concepts/wireframe]]). As próximas aulas trazem padrões, informações técnicas e a implementação "tanto no Figma, tanto no código".

### Exemplo: landing page do FrontPUSH

- **Desktop:** "12 colunas imaginárias, mais ou menos"; um bloco ocupa "de sete a oito colunas", o outro "de cinco a quatro". No arquivo de design: "quatro colunas de cá e aqui oito colunas restantes de cá". Ver [[wiki/entities/frontpush]].
- **No modo de responsividade**, a estrutura "quebrou justamente naquele breakpoint" ao passar para celular ou tablet.

### Padrões: Bootstrap e regra de oito pontos

- **"Os dois mais utilizados [...] é o Bootstrap, e a regra de oito pontos."** Ver [[wiki/entities/twitter-bootstrap]] e [[wiki/concepts/grid-de-8-pontos]].
- **Bootstrap Grid System:** "estabelece grids em colunas para diferentes tipos de dispositivos e estabelece padrões de width".
- **Regra dos oito pontos:** "utilizada demais em sistemas de apps, tanto o Android como o iOS".
- **"Os dois meio que se complementam"**: o Bootstrap decide colunas e larguras, os oito pontos decidem as medidas (leitura do agente). Outros grids existem, "mas que seguem essa mesma linha".

### Quatro tipos de layout

Ver [[wiki/concepts/layout-fixo-fluido-adaptativo-responsivo]].

- **Fixo:** "pouquíssimo comum hoje em dia"; serve a empresa que compra um aparelho para usar "por vários e vários anos". Exemplo: iPads de atendimento de uma pizzaria, "eu quero só um sistema para poder ficar mais barato". Aí "essa conversa [...] quanto à responsividade não faz tanto sentido".
- **Fluido:** "widths definidos em porcentagem". Num flexbox, a imagem com 100% da caixa encolhe junto com a caixa. O limite: "esse bloco não iria quebrar", os dois ficariam lado a lado "até eu esmagar os dois", com texto ilegível. "Não dá para aplicar o sistema fluido na tela inteira", só "em determinadas seções, em determinados breakpoints". Sozinho, é "um sistema responsivo porco".
- **Adaptativo:** media query, "uma cláusula para ele começar a ler determinada folha de estilo quando ele estiver abaixo de 960 pixels". Esse valor "é um breakpoint". A mudança é "de repente", não contínua. "Mais otimizado" e "mais rápido porque é um estilo só para cada tela"; "mais trabalhoso porque você tem que fazer vários estilos para várias telas". Numa resolução fora das previstas, "ele quebra". Ver [[wiki/concepts/breakpoint]].
- **Responsivo:** "engloba todos esses caras", "mistura o melhor de todos os mundos". Tem partes fluidas (seções que diminuem com a tela) e adaptativas (estilos a mais ou a menos em resoluções específicas). É "um pouco mais carregado". Ver [[wiki/concepts/design-responsivo]].
- **Teste sempre:** "isso nunca vai invalidar sempre você testar em vários tipos de dispositivos". Com tantos modelos de Galaxy e iPhone, "fazer o adaptativo é praticamente suicídio"; "o responsivo está sendo o queridinho".

### Alinhamento e consistência

- **Wireframe no grid:** "o meu conteúdo é alinhado aos grids"; o conteúdo pega seis colunas centrais, "sobra três para um lado, três para o outro". A ilustração fica de fora de propósito, "é o estilo dessa ilustração". Ver [[wiki/concepts/wireframe]].
- **A coluna como unidade de distância:** "quanto que tem de distância de um elemento para o outro? Ah, é uma coluna".
- **Websites e plugins para criar grids** ficam no "master file". Haverá parte prática.

## Entities

- [[wiki/entities/nasser]]: autor (inferido). Mostra "a landing page do FrontPush" entre "os sites que eu já desenvolvi" e diz "esse meu site aqui é responsivo". O slide traz o logo "W7" e a estrela "Post no insta" ao lado de "Ajudam em que?", e nasser.md já registra que ele tem posts sobre grids no Instagram.
- [[wiki/entities/frontpush]]: exemplo das 12 colunas e da quebra no breakpoint.
- [[wiki/entities/twitter-bootstrap]]: Bootstrap Grid System como um dos dois padrões.
- Sem página própria: Android, iOS, iPad, Galaxy, iPhone.

## Concepts

- [[wiki/concepts/layout-fixo-fluido-adaptativo-responsivo]] (novo)
- [[wiki/concepts/breakpoint]] (novo)
- [[wiki/concepts/grid-de-colunas]]
- [[wiki/concepts/grid-de-8-pontos]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/wireframe]]

## Tensões com a wiki

- **"Adaptativo é mais rápido" vale só no servidor.** `[external]` Com media queries no CSS, o navegador baixa a folha inteira, inclusive regras de outros breakpoints. Elas só deixam de ser aplicadas, então não há ganho de transferência. O ganho que a aula descreve ("eu fiz alguma requisição [...] eu vou mandar exatamente o estilo daquela tela") existe quando o servidor detecta o aparelho e manda HTML ou CSS diferente (dynamic serving, RESS) (https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing). Na aula, o adaptativo é mostrado justamente com media query. Confiança alta na distinção; a aula mistura os dois mecanismos.
- **Responsivo = fluido + media queries.** `[external]` Bate com a definição original de Ethan Marcotte (2010): grid fluido, imagens flexíveis e media queries (https://alistapart.com/article/responsive-web-design/). "Adaptive web design", no sentido de Aaron Gustafson (2011), quer dizer melhoria progressiva, não layouts fixos por breakpoint. O sentido da aula (layouts fixos trocados em breakpoints) é o mais comum hoje, mas não é o único.
- **Fixo e o container fixo.** `[skill: ux-ui-mentor]` A skill chama de "fixed" o container com max-width centralizado e de "hybrid" o container fixo com elementos fluidos, "mais comum em produtos". A aula usa "fixo" para um layout de uma tela só. São sentidos diferentes da mesma palavra.
- **Breakpoint de 960.** `[skill: ux-ui-mentor]` A skill não lista 960 entre os comuns (480, 768, 1024, 1280, 1536). `[external]` O Bootstrap 5 usa 576, 768, 992, 1200 e 1400 (https://getbootstrap.com/docs/5.3/layout/breakpoints/). O 960 lembra o antigo 960 Grid System. A regra da skill: "adicione um breakpoint quando o conteúdo pede, não para cobrir todos os devices", o mesmo argumento da aula contra o adaptativo.
- **Media query como "folha de estilo".** A aula diz que o CSS passa a "ler determinada folha de estilo". Media query pode estar num arquivo separado (`<link media="...">`) ou num bloco `@media` do mesmo arquivo. Os dois funcionam.
- **iOS e oito pontos.** `[external]` O Material Design define a grade de 8 dp com sub-grade de 4 dp (https://m2.material.io/design/layout/spacing-methods.html). As Human Interface Guidelines da Apple não fixam uma grade de 8 pt, embora muitos valores do sistema caiam nela. "Tanto o Android como o iOS" vale mais para o Android. Confiança média.
- **"Quatro colunas de cá e oito de cá" contra "sete a oito + cinco a quatro".** O site no navegador é lido "mais ou menos" (7–8 + 4–5). O design no Figma é 4 + 8, com o bloco menor à esquerda. As duas leituras usam 12 colunas.

## Open Questions

- **"Essa conversa de sub-grids na próxima aula"**: pode ser "sobre grids" (erro de legenda), o `subgrid` do CSS Grid (https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Subgrid) `[external]` ou a sub-grade de 4 px da skill. Mantido como "sub-grids"; confirmar na parte 2.
- **"Eu conheci das resoluções, dos breakpoints"**: provavelmente "o conhecimento das resoluções"; mantido literal.
- **"Aulas de desenvolvimento no script, a FIA"**: trecho ininteligível; mantido literal.
- **"Aqui no usuário frames"** corrigido para "wireframes" (ele fala de wireframes no começo e mostra um layout alinhado ao grid). Confiança média.
- **Lacunas na legenda:** cerca de 9 s entre 06:22 e 06:31 (o raw marca com `[...]`; deve ser a introdução dos quatro tipos de layout) e cerca de 10 s entre 10:50 e 11:00 (depois de "galgando degraus").
- **Websites e plugins para criar grids** do "master file": não listados na aula.
- `date_published` vazio.

## Raw Quotes

> "Os grids criam a estrutura básica, o esqueleto para o seu design."

> "Não dá para aplicar o sistema fluido na tela inteira."

> "Quanto que tem de distância de um elemento para o outro? Ah, é uma coluna."

## Ver também

- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]: o grid de 12 colunas montado no Figma (72 + gutter 32)
- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]: o grid de 8 pontos como escala de consistência
- [[wiki/sources/historia-do-front-end-akita-ep4]]: origem das media queries e do Bootstrap
