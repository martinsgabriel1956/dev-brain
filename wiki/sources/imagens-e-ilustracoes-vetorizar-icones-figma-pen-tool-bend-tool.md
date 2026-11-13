---
type: source
title: "Imagens e ilustrações (edição \"W7\"): vetorizando ícones no Figma com a Pen Tool e a Bend Tool"
aliases: ["vetorizar ícone no Figma", "Pen Tool e Bend Tool", "ícone de telefone vetorizado", "aula de vetorização W7"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, figma, svg, ilustracoes, icones, vetorizacao, pen-tool, bezier, sombra, gradiente, motion]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Imagens e ilustrações (edição "W7"): vetorizando ícones no Figma com a Pen Tool e a Bend Tool

## TL;DR

Aula curta (cerca de 7 min), acrescentada ao módulo para responder "a pergunta que eu sempre recebo": como os ícones animados do autor foram feitos no [[wiki/entities/figma]] e por que são vetores. (1) Desagrupando o "app telefone", **tudo são vetores**: o fundo é um retângulo de bordas arredondadas (uma união de vetores) com gradiente linear verde e sombras, e o telefone tem preenchimento, sombra interna e externa. (2) O telefone foi **contornado à mão com a Pen Tool** sobre uma imagem do ícone tirada da internet: zoom, clicar onde a parte reta termina e onde a curva começa, com **o mínimo de pontos possível** e de forma simétrica. (3) Fechado o caminho, a **Bend Tool** arredonda os pontos; opacidade baixa ajuda a ver a imagem por baixo. (4) **Refino**: duplo clique no elemento, clique no ponto, mexer as duas alças até a curva ficar contínua e colada no contorno. "É paciência, é a grande realidade." (5) Por ser vetor, exporta tudo para [[wiki/concepts/formato-svg|SVG]]: "muito da mágica que eu faço está aqui no Figma". Ver [[wiki/concepts/vetorizacao-com-pen-tool]].

## Key Claims

### Tudo são vetores

- **Pergunta dos alunos:** "Násser, como é que você conseguiu fazer essas ilustrações bonitas [...] no Figma [...] e são vetores?". A ponte é com os ícones animados: "mais uma vez, partiu do Figma".
- **Desagrupar mostra a construção:** o telefone é um vetor; o de trás é "uma união de outros vetores"; no painel de camadas, "tudo, tudo, tudo são vetores". Ver [[wiki/concepts/operacoes-booleanas-em-formas]].
- **O fundo é fácil:** retângulo, bordas arredondadas, gradientes lineares verdes e sombras ("o único efeito que eu estou aplicando são sombras").
- **O telefone leva efeitos de preenchimento, sombra interna e sombra externa.** A dúvida é como desenhar a forma dele.

### Contornar a imagem com a Pen Tool

- **Processo:** pegar "uma imagem do ícone lá na internet", colar no Figma e seguir o contorno com a Pen Tool. Zoom com Ctrl mais; barra de espaço para navegar.
- **Reto e curvo:** clicar até onde a linha "está reto" e alinhado; quando "vai começar a dobrar", outro clique, e mais um se preciso.
- **Menos pontos possível:** "administrar os pontos nesse vetor de forma que seja a menor quantidade de pontos possível e que eu consiga aplicar as curvas da melhor forma possível". Um ponto marca onde a curvatura muda de leve para forte; trechos de curvatura uniforme não precisam de ponto no meio.
- **Simetria:** o que se faz de um lado do telefone se repete do outro ([[wiki/concepts/simetria-visual]]).
- **Não precisa ser perfeito nessa etapa:** "é literalmente identificar onde é parte reta, onde é parte curvada e ir administrando os pontos para depois vocês só irem entortando e refinando".

### Arredondar com a Bend Tool

- **Fechado o caminho**, a ferramenta "do lado", a Bend Tool, arredonda os pontos. Eles "não vão ficar perfeitos de primeira".
- **Opacidade** no vetor para "enxergar através" e contornar melhor o objeto (o mesmo truque dos 20% do mockup de iPhone na [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo|aula anterior]]).
- **Continuidade:** "o ideal é que fique reto para poder deixar uma curva suave e você não perceber que ali tem um ponto de descontinuidade". `[external]` Isto é, as duas alças do ponto alinhadas numa reta (tangente contínua).
- **"Quanto menos pontos melhor [...] quando você tem muito ponto, dá muito trabalho."**

### Refinar as alças e exportar

- **Duplo clique no elemento → clique no ponto → duas alças**; mexer "de um lado e de outro" até continuar contornando o telefone.
- **"É lógico que dá trabalho? Dá trabalho"**: tirar e pôr zoom até as partes ficarem uniformes.
- **Resultado:** uma versão vetorial do telefone para montar os ícones, exportável "tudo, tudo, tudo para SVG". Quem domina o Figma nesse sentido leva as criações "para outro nível".

## Entities

- [[wiki/entities/nasser]]: autor; o nome aparece na pergunta dos alunos que ele lê em voz alta (legenda: "Inácio").
- [[wiki/entities/figma]]: Pen Tool, Bend Tool, edição de pontos e alças, efeitos de sombra.
- Sem página própria: os ícones animados do autor (o "app telefone"), sem projeto nomeado.

## Concepts

- [[wiki/concepts/vetorizacao-com-pen-tool]] (novo)
- [[wiki/concepts/formato-svg]]
- [[wiki/concepts/icones-em-interfaces]]
- [[wiki/concepts/ilustracoes-em-interfaces]]
- [[wiki/concepts/operacoes-booleanas-em-formas]]
- [[wiki/concepts/simetria-visual]]

## Tensões com a wiki

- **Ícone de app ≠ ícone de interface.** O "app telefone" é um ícone ilustrado (gradiente, sombra interna e externa), mais próximo de ilustração que dos ícones de linha da [[wiki/concepts/familia-de-icones]] e do [[wiki/concepts/grid-de-icones|grid]] das aulas de ícones. A aula não fala de grid nem de família.
- **Copiar o contorno de um ícone da internet.** `[external]` O telefone é forma genérica, mas o desenho traçado de um ícone protegido continua sendo dele; a mesma ressalva dos logos redesenhados em [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]].
- **Sombras viram filtros no SVG.** Sombra interna e externa exportadas do Figma saem como filtros, que custam renderização ao animar `[external]` (ver [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] e [[wiki/concepts/mobile-animacoes-performaticas]]).
- **Atalho que o Figma já tem.** `[external]` O Figma tem "Simplify a vector path" para reduzir pontos depois (https://help.figma.com/hc/en-us/articles/33792593975575-Simplify-a-vector-path); a aula ensina a acertar o número de pontos na hora de traçar, o que costuma dar curvas mais limpas.

## Open Questions

- **Quais ícones animados?** "Esses ícones aqui e como eu animei eles" não identifica o projeto (FrontPUSH? site pessoal?).
- **"Ajeitar nas pinças"**: mantido literal; provável referência às alças.
- **"Como se de simétrica"**: mantido literal.
- `date_published` vazio.

## Raw Quotes

> "Então aqui é paciência, é a grande realidade."

> "Quanto menos pontos melhor para você aplicar, você vai aprender isso com o tempo."

> "Muito da mágica que eu faço está aqui no Figma e quando você sabe dominar o Figma nesse sentido, as suas criações vão para outro nível."

## Ver também

- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — aula anterior: ilustração é um conjunto de formas; mockup de iPhone com retângulos e subtração
- [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]] — onde a Pen Tool aparece pela primeira vez, para vetorizar logo de cliente
