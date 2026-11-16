---
type: source
title: "Style Guide (edição \"W7\"): documentação, padronização dos elementos e a visão do desenvolvedor"
aliases: ["aula de style guide", "guia de estilo W7", "style guide FrontPUSH", "o que colocar no style guide"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, style-guide, guia-de-estilo, design-system, design-tokens, documentacao, handoff, dark-mode, estados, figma, css]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-15
---

# Style Guide (edição "W7"): documentação, padronização dos elementos e a visão do desenvolvedor

## TL;DR

Aula teórica (cerca de 23 min) do módulo de interface web, a "culminação" depois de pesquisa, [[wiki/concepts/wireframe]] e [[wiki/concepts/grid-de-colunas|grids]]. O [[wiki/concepts/style-guide]] é o passo em que o designer "passa o bastão para o time de desenvolvimento". Documenta o **design** (cor, card, border-radius, marca) e o **comportamento** (telas, especificações, guia de interação, flow, jornada). O que ele contém "depende": há **levels de complexidade**, de uma padaria a um Dropbox ou Google. Muito se descobre "na prática, fazendo perguntas", se colocando no papel do dev, que pode não saber abrir o [[wiki/entities/figma]] e às vezes recebe um PDF. A lista de padronização dos elementos: versão **light e dark**, **paleta** (hexadecimais no Sass ou em variáveis CSS), **[[wiki/concepts/tipografia]]** desktop x mobile (48, 36, 24 no style guide do [[wiki/entities/nubank]]), **[[wiki/concepts/familia-de-icones|ícones]]** ([[wiki/entities/feather-icons]]), **cards** e **botões** com estados (normal, hover com sombra, selecionado em roxo), **inputs** (hover, focus, erro, warning, sucesso), **[[wiki/concepts/elementos-de-composicao]]** e **animações com links de apoio**. Não esperar ficar perfeito: compartilhar o arquivo do Figma por link e evoluí-lo, com atualização "em tempo real". Na prática: grupos de estilo pré-definidos no Figma (texto, cor, sombra) e o CSS da aba **inspect** (background, box-shadow e border-radius servem; width, top e left dependem da arquitetura). Por fim, **labels** que design e dev entendem: `card-dark`, `card-hover`, `$orange`, orange dark e orange light ([[wiki/concepts/design-tokens]]). Soft skills centrais: comunicação e colaboração ([[wiki/concepts/colaboracao-times]]).

## Key Claims

### O que é

- **Onde fica no processo:** pesquisa, wireframe e grids levam ao "protótipo final, onde nós temos o style guide, aplicar as cores e definitivamente conseguir o layout final para a implementação". O exemplo é o projeto do Nubank, prometido para as aulas práticas.
- **Por que agora:** "a gente vai ter que começar a passar o bastão para o time de desenvolvimento, por isso que style guide tem muito dessa carga de documentação, de entrega [...], de colaboração, de comunicação".
- **Definição:** "ele é um guia, ele é um documento, ele padroniza o estilo, só que o estilo pode ser tanto focado só para design, tanto também como comportamento". Slide: "Guia de estilo da tipografia, paleta de cores, cards, elementos de composição, marca e etc." e "Doc onde você comunica ao time as telas, especificações, guia das interações, flow de telas e etc.". Ver [[wiki/concepts/style-guide]].

### O que colocar: depende

- **"Existem levels de complexidade."** Time maior e gerência de projeto mais complexa pedem um style guide "mais rebuscado, com mais detalhes, com mais padrões". O site de uma padaria que só expõe o cardápio não é um projeto para Dropbox ou Google.
- **"O style guide não é muito bem definido do que ter e do que não ter, muito do que deve ter você descobre na prática, fazendo perguntas."** Slide: "Se faça perguntas, se coloque no papel do desenvolvedor. Se você perceber que ele precisa, documente!".
- **O dev pode não saber usar o Figma:** "às vezes você vai ter que passar o PDF disso aqui e vai ter que estar tudo escrito lá". A sombra, o border-radius e o peso tipográfico que o designer definiu precisam estar escritos ([[wiki/concepts/sombra-em-interfaces]]).
- **Sempre em evolução:** o style guide filmado "pode estar atualizado" quando o aluno voltar. Ele pede feedback de quem não conhece o processo, porque coisas "passam batido".
- **"Faça notas, descreva com mais detalhes"** (slide).

### Padronização dos elementos (slide)

| Item do slide | O que a aula diz |
|---|---|
| Versão Light & Dark | A marca pode ser preferencialmente light, preferencialmente dark, ou ter só uma; "eu sempre gosto de deixar as duas" e deixar o usuário escolher |
| Cores: paleta no SASS | Seção própria; o dev põe os hexadecimais "lá no Sass ou então em variáveis no CSS" para dar consistência ao código |
| Tipografia: h1, h2, h3, h4, p, span | Títulos e corpo, desktop x mobile e responsivo; no do Nubank, 48, 36, 24; no que ele mostra, os tamanhos ainda são iguais ("ainda está para atualizar") |
| Ícones: family | Ícones próprios para download ou uma família ([[wiki/entities/feather-icons]]); no Nubank, "uma família exemplificando a família de ícones" |
| Cards: hover, comportamento | Normal, hover com sombra, clicado ou selecionado em roxo; "esses três estados [...] têm que estar muito bem claros e documentados com relação ao CSS" |
| Botões: hover, click | Normal e hover (sombra ou crescer) e "como é que vai ser a transição entre esses dois estados" |
| Inputs: hover, focus, error, warning | Placeholder "acende" no hover; borda cinza no focus; verde quando correto; borda vermelha, ícone e mensagem de erro no lugar certo |
| Elementos de composição | "Estabelecer o branding de elementos de composição": backgrounds, animations |
| Animações / Comportamento: links de apoio | "Eu quero que o meu card vire para cima, para baixo, que ele apareça em fade in, em fade out": nota, descrição e link de apoio |

- **"Só falar de cores, por exemplo, ou só de CSS fica muito raso."** O comportamento pede links de apoio, conversa com o time e exemplos práticos, "porque só o design em si muitas vezes não te dá essa informação". Ver [[wiki/concepts/feedback-do-sistema]].
- **Inputs como "respostas ao usuário":** padronizar "o que vai acontecer, aonde e por quê". Ver [[wiki/concepts/maquina-de-estados-ui]].
- **Formatos:** além do Figma, uma versão em slide com "teoricamente as mesmas informações", e outros modos "mais enxutos" em projeto, atualizados no Notion.

### Evolução da documentação

- **"Crie o arquivo, disponibilize pelo link e vá evoluindo com o tempo..."** (slide). Ele fez isso com os wireframes: share, copiar o link, os alunos copiaram para o próprio Figma.
- **"Eu vou continuar modificando e vocês vão receber essas atualizações em tempo real."** Por isso "não esperar [...] um documento ficar totalmente perfeito para você disponibilizar ele". Ver [[wiki/concepts/living-documentation]].

### Grupos de estilo e a aba inspect

- **Grupos de estilo pré-definidos no Figma** (texto, cores, sombras) "elevam a consistência no design em outro level" ([[wiki/concepts/consistencia-visual]]). Ficam para a aula prática.
- **Aba inspect:** selecionar o card "sem ser um grupo"; ali estão width, height, top, left e radius. Parte desse CSS "não cabe na realidade", porque depende de flexbox ou position. "Mas pelo menos as de background, de box-shadow, de border-radius, essa aqui sempre agregam muito." Slide: "Até onde vai a precisão do CSS no Figma??". Ver [[wiki/concepts/css]].

### Visão do desenvolvedor e labels

- **"Projetar labels para que o time de design e devs possam entender"** (slide): `card-dark`, `card-hover`. Hover porque é o nome do CSS: "se eu colocar o mesmo nome facilita para eu, o desenvolvedor, entender".
- **Cifrão para variável:** "orange, e aí eu sempre coloco um cifrão do lado para poder indicar que é algum tipo de variável para poder ser utilizado lá no código", junto com orange dark e orange light. A mesma label no Figma e no código. Ver [[wiki/concepts/design-tokens]].
- **Soft skills:** "comunicação e a colaboração" (slide: "Softskills: Comunicação & Colaboração"). Slide de abertura: "É criando o styleguide que percebemos o quanto o UX/UI agrega na carreira de devs front-end".

## Entities

- [[wiki/entities/nasser]]: autor. O nome é dito na pergunta dos alunos (legenda "Nácio", como "Inácio" na aula de vetorização); slides com o logo "W7".
- [[wiki/entities/figma]]: share por link, grupos de estilo, aba inspect.
- [[wiki/entities/nubank]]: projeto prático do curso; style guide com tipografia 48, 36, 24 e família de ícones.
- [[wiki/entities/feather-icons]]: família de ícones do style guide.
- Sem página nova: Dropbox e Google (exemplos de projeto complexo), Notion (onde os style guides são atualizados), Sass.

## Concepts

- [[wiki/concepts/style-guide]] (novo)
- [[wiki/concepts/design-tokens]] (novo)
- [[wiki/concepts/wireframe]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/tipografia]]
- [[wiki/concepts/familia-de-icones]]
- [[wiki/concepts/sombra-em-interfaces]]
- [[wiki/concepts/botoes-em-interfaces]]
- [[wiki/concepts/feedback-do-sistema]]
- [[wiki/concepts/maquina-de-estados-ui]]
- [[wiki/concepts/elementos-de-composicao]]
- [[wiki/concepts/css]]
- [[wiki/concepts/living-documentation]]
- [[wiki/concepts/colaboracao-times]]

## Tensões com a wiki

- **Hover não é pseudo-element.** Ele chama hover de "pseudo-element". `:hover` é uma **pseudo-classe** (estado); pseudo-elementos são `::before`, `::after` `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/:hover). O argumento do nome igual continua válido.
- **Faltam focus, active e disabled em cards e botões.** Os inputs têm focus e erro, mas cards e botões só têm normal, hover e selecionado. `[skill: ux-ui-mentor]` Um componente documentado lista default, hover, focus (visível no teclado), active, disabled e loading; o hover não existe no toque.
- **Dark mode como "versão".** `[skill: ux-ui-mentor]` Dark mode não é inverter cores: é um tema com tokens semânticos próprios (sem preto puro, texto não branco puro, sombras trocadas por bordas). As labels `card-dark` e `orange dark` misturam o tema no nome; a prática comum é um nome semântico (`card-background`) com valor por modo.
- **Style guide x design system.** A aula não usa o termo design system. `[skill: ux-ui-mentor]` A skill descreve o design system em camadas (tokens, componentes, patterns, guidelines); o style guide da aula cobre tokens e estados e aponta para guidelines de comportamento. Ver [[wiki/concepts/style-guide]].
- **Erro do input com ícone e cor.** Borda vermelha mais ícone e mensagem cumpre "nunca só a cor" ([[wiki/concepts/cor-semantica]]). `[skill: ux-ui-mentor]` A mensagem precisa estar ligada ao campo (`aria-describedby`, `aria-invalid`) e aparecer só depois da interação.
- **O CSS do inspect.** Bate com a skill: valores absolutos (top, left, width) raramente sobrevivem a um layout com flexbox ou grid; cor, sombra e radius viram tokens.

## Open Questions

- **"Acessões"** ("um pouco mais corrido, acessões e eu consigo detalhar"): mantido literal; talvez "as seções". Ambíguo.
- **"Que o design desenhou"**: talvez "o designer". Mantido.
- **Aula prática de style guide** (grupos de estilo, compartilhamento, versões para download) e o style guide do Nubank: prometidos, ainda não ingeridos.
- **Ordem do curso:** "esses três últimos" (pesquisa, wireframe, grids) sugere aulas de pesquisa e grids que a wiki ainda não tem nesta edição.
- `date_published` vazio.

## Raw Quotes

> "Ele é um guia, ele é um documento, ele padroniza o estilo, só que o estilo pode ser tanto focado só para design, tanto também como comportamento."

> "Muito do que deve ter você descobre na prática, fazendo perguntas."

> "Se eu colocar o mesmo nome facilita para eu, o desenvolvedor, entender."

## Ver também

- [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]]: o hover de sombra que "vai ficar muito bem claro no meu style guide"
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]: estados de botão e consistência
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]]: as duas famílias de ícones do autor
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]: o grid que vem antes do style guide
