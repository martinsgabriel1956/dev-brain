---
type: source
title: "Alinhamento e espaçamento de texto: esquerda como padrão, centralizado em cards, parágrafo de 4 a 8 linhas"
aliases: ["aula de alinhamento de texto", "alinhamento e espaçamento em textos", "texto justificado", "espaçamento entre parágrafos aula", "FrontPUSH tipografia aula 4"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, tipografia, alinhamento, alinhamento-de-texto, espacamento, espacamento-entre-paragrafos, line-height, legibilidade, consistencia, design-responsivo, css, figma]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/alinhamento-e-espacamento-de-texto.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-15
---

# Alinhamento e espaçamento de texto: esquerda como padrão, centralizado em cards, parágrafo de 4 a 8 linhas

## TL;DR

Aula 4 do módulo de [[wiki/concepts/tipografia]] do curso do [[wiki/entities/frontpush|FrontPUSH]] (slide com a marca "W7"; autoria de [[wiki/entities/nasser|Násser]] inferida). Duas "variáveis tipográficas" que deixam a leitura mais confortável, depois de altura de linha e largura de texto (aula 3, ainda não ingerida). **[[wiki/concepts/alinhamento-de-texto|Alinhamento]]:** à esquerda é o padrão e "o coringa" (leitura da esquerda para a direita, padrão do [[wiki/concepts/css]], borda esquerda fixa no [[wiki/concepts/design-responsivo|responsivo]]); centralizado só em títulos e trechos curtos de cards; à direita só em pequenas ações; justificado nunca, porque sem hifenização o espaço entre palavras fica irregular. **[[wiki/concepts/espacamento-entre-paragrafos|Espaçamento]]:** quebrar o texto em parágrafos de 4 a 8 linhas e separá-los por um vão do tamanho do line-height (o "enter clássico"), nunca grande a ponto de separar o conteúdo, e o mesmo vão em todo o site. Exemplos: [[wiki/entities/new-york-times]], G1 e o site do próprio autor.

## Key Claims

### Alinhamento

- **Alinhamento é "aquele eixo onde o texto está alinhado"**: esquerda, centro, direita ou justificado. Ver [[wiki/concepts/eixo-visual]].
- **À esquerda é o mais comum, "cerca de 90%" da web**, e o padrão do CSS: "todas as tags de texto, de título já vêm automaticamente alinhados à esquerda". Os 90% são estimativa da aula, não medição. `[external]` O valor inicial de `text-align` é `start`, que vira esquerda em idiomas LTR e direita em RTL: https://developer.mozilla.org/en-US/docs/Web/CSS/text-align.
- **Dois porquês para a esquerda:** (1) cultura, "a gente lê da esquerda para a direita"; (2) responsividade, porque em todos os dispositivos "a esquerda fica fixa" e "quem move é [...] a parte direita".
- **Prova pelas referências:** no New York Times títulos, títulos menores e corpo são todos alinhados à esquerda; "você não vai errar se você colocar alinhado à esquerda".
- **Centralizado: títulos e "pequenos trechos em cards".** O autor mostra o próprio site: tudo à esquerda, exceto uma seção de cards com título e texto curtos centralizados.
- **À direita: quase inexistente.** Aparece em pequenas ações, como um link "passe para o outro lado" no canto direito, ou ao lado de uma ilustração; mesmo assim o autor prefere a esquerda: "meio que é feio colocar alinhado à direita".
- **Justificado: "não utilize".** Pouco usado e "não tem hifenização automática"; os espaços entre palavras "não ficam consistentes" e, com palavras curtas que não cabem, o texto pode "quebrar, ficar mais difícil de ler". O autor tenta mostrar no [[wiki/entities/figma]] e admite que "não deu para perceber muito".
- **Regra final:** esquerda como padrão predominante; centralizado nos casos de cards.

### Espaçamento

- **Espaço entre parágrafos do mesmo tamanho do line-height**, o "clássico enter". Ver [[wiki/concepts/espacamento-entre-paragrafos]].
- **Texto corrido, sem quebra, "fica um texto muito pesado, fica cansado de ler"**: o slide resume "sem quebras, sem parágrafos: texto pesado, cansativo".
- **Quebre a cada 4 a 8 linhas**: numa matéria do NYT o autor conta um parágrafo de 4 linhas e outro de 6; "é literalmente parágrafos", um assunto por bloco.
- **O vão não pode ser grande**: espaço grande ou uma linha divisória "separa o conteúdo", e a intenção é manter o texto junto. É a regra das aulas de espaçamento e linhas aplicada ao texto ([[wiki/concepts/lei-da-proximidade-gestalt]], [[wiki/concepts/espaco-em-branco]]).
- **Pode ser "um pouquinho maior"**: no G1 o vão entre parágrafos é maior e "não tem problema nenhum", desde que não chegue a separar; o vão da imagem (trecho de vídeo) para o texto é maior ainda.
- **Consistência:** "uma vez que você colocou o espaçamento aqui, utilize ele em todo o seu site". Ver [[wiki/concepts/consistencia-visual]].

## Entities

- [[wiki/entities/nasser]]: autor inferido. "Meu próprio site" com cards centralizados; pasta "FrontPush" da transcrição; slide com a marca "W7", como nas aulas cuja autoria o usuário confirmou. O nome não é dito.
- [[wiki/entities/frontpush]]: curso de origem da transcrição.
- [[wiki/entities/new-york-times]]: referência de alinhamento à esquerda e de parágrafos de 4 a 6 linhas.
- [[wiki/entities/figma]]: onde o autor tenta mostrar o justificado.
- Sem página própria: G1 (vão entre parágrafos um pouco maior).

## Concepts

- [[wiki/concepts/alinhamento-de-texto]] (novo)
- [[wiki/concepts/espacamento-entre-paragrafos]] (novo)
- [[wiki/concepts/tipografia]]
- [[wiki/concepts/eixo-visual]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/css]]
- [[wiki/concepts/espaco-em-branco]]
- [[wiki/concepts/lei-da-proximidade-gestalt]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/densidade-de-informacao]]

## Tensões com a wiki

- **Vão de parágrafo = line-height x WCAG.** `[external]` O critério 1.4.8 da WCAG (AAA) pede espaço entre parágrafos de pelo menos 1,5 vez o espaço entre linhas, e texto não justificado: https://www.w3.org/WAI/WCAG21/Understanding/visual-presentation.html. A aula fica abaixo disso no vão e concorda no justificado. O G1 "um pouquinho maior" se aproxima da WCAG.
- **"Não tem hifenização automática".** Vale para o Figma da demonstração. `[external]` Na web existe `hyphens: auto`, que depende do atributo `lang` e do suporte do navegador ao idioma: https://developer.mozilla.org/en-US/docs/Web/CSS/hyphens. Mesmo com hifenização, o justificado em coluna estreita forma "rios" de espaço `[skill: ux-ui-mentor]` (a skill manda evitar justificado no mobile).
- **Esquerda é cultural, não universal.** A própria aula funda a regra na leitura da esquerda para a direita; em árabe ou hebraico o padrão se inverte, e `text-align: start` já acompanha isso `[external]`.
- **"90%" de novo.** Na visão geral do módulo, "tipografia compõe 90% da web" ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]); aqui, cerca de 90% dos textos são alinhados à esquerda. Claims diferentes, o mesmo número redondo sem medição.
- **Line-height engana a medição.** A aula prática de espaçamento já avisava que a caixa de texto inclui o line-height ([[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]). Com vão de parágrafo = line-height, a distância visual entre as letras de dois parágrafos fica perto de duas entrelinhas. Inferência do agente.

## Open Questions

- A aula 3 (altura de linha e largura de texto) está no mesmo diretório de transcrições e ainda não entrou na wiki; ela deve dar os valores de line-height que esta aula usa como unidade.
- "A gente vem aqui nas maiores informações": provavelmente um painel do Figma; mantido literal no raw.
- 4 a 8 linhas: regra de bolso do autor, sem fonte citada.
- `date_published` vazio.

## Raw Quotes

> "É meio que o coringa, você não vai errar se você colocar alinhado à esquerda."

> "Se eu fizer o texto totalmente corrido, ele fica um texto muito pesado, fica cansado de ler."

> "O clássico enter é o tamanho de um line-height que separa uma seção da outra."

## Ver também

- [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]] — "aquelas aulas de espaçamento e linhas" citadas na aula
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — line-height na medição de texto
