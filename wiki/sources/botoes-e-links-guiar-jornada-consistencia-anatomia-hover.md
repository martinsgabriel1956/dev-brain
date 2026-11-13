---
type: source
title: "Botões e links (edição \"W7\"): guiar a jornada, consistência, anatomia e hover"
aliases: ["aula teórica de botões W7", "botões e links W7", "UX em botões", "anatomia dos botões"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, botoes, links, hierarquia-visual, consistencia, area-clicavel, acessibilidade, hover, motion, sombra]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/botoes-e-links-guiar-jornada-consistencia-anatomia-hover.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Botões e links (edição "W7"): guiar a jornada, consistência, anatomia e hover

## TL;DR

Aula teórica (cerca de 16 min) que abre o bloco de [[wiki/concepts/botoes-em-interfaces|botões e links]] da edição "W7"; a prática no [[wiki/entities/figma]] vem depois. A tese: **botões guiam o usuário na jornada**, de um ponto A a um ponto B. Mostram os principais caminhos, funcionalidades e ações, ou a finalidade de um formulário ("cadastre-se"). Exemplos: [[wiki/entities/frontpush]] ("grade do curso" + "inscreva-se"), [[wiki/entities/apple]] (links destacados, link branco e texto cinza como [[wiki/concepts/hierarquia-visual|hierarquia]]), [[wiki/entities/sketch]] ("See pricing", "tente de graça", "leia mais"), Framer (CTA fixo ao rolar) e Adobe XD. Regras: [[wiki/concepts/consistencia-visual|consistência]] (mesma altura, mesmo padding, mesmo [[wiki/concepts/border-radius]]; a largura varia com o texto); um botão **primário** (preenchido) e um **secundário** ("vazio", sem background), nunca cinco tipos; boa [[wiki/concepts/area-clicavel|área clicável]], porque o dedo é menos preciso que o mouse; label curto e objetivo; fundo na cor de [[wiki/concepts/contraste]] da paleta, o "ímã"; resposta no hover ([[wiki/concepts/feedback-do-sistema|feedback]]: cresce, ganha sombra da cor do botão, muda opacidade); **altura mínima de 44 px** (ele usa 56) e padding pela [[wiki/concepts/escala-de-espacamento|escala]] adotada.

## Key Claims

### Para que servem

- **"Eles meio que guiam o usuário na jornada"**: itens "importantíssimos para poder levar o usuário de um ponto A a um ponto B". Mostram "os principais caminhos, as principais funcionalidades, as principais ações", ou "a finalidade [...] de um formulário": clicar em "cadastre-se". Ver [[wiki/concepts/botoes-em-interfaces]].
- **Ajudam na compreensão do conteúdo** e a "mostrar os principais pontos da sua interface, do seu produto, do seu serviço". O slide "UX em botões" lista: compreensão do conteúdo, principais funcionalidades, principais caminhos, guiar o usuário na jornada, consistência e anatomia.

### Exemplos de referência

- **Por que copiar gigantes:** empresas "bilionárias como a Apple" têm "um time gigantesco de UX, [...] de marketing, [...] de pesquisa"; "tudo vai ter um motivo". Ver [[wiki/entities/apple]] e [[wiki/concepts/padroes-de-interface]].
- **FrontPUSH:** a interface demonstra o valor do curso, mas há "objetivos primordiais e específicos". Todo aluno quer a grade, então "de cara" há um botão "grade do curso". O objetivo do dono é a inscrição, então há "inscreva-se", que leva a um formulário (nome, e-mail, telefone) com um botão final para enviar. Ver [[wiki/entities/frontpush]].
- **Apple:** "trabalha com links", "sempre são dois links muito simples" por produto (iPhone 12). Links do menu dão "a resposta à interação" que diz que são links. Onde ela quer que se veja o preço ("qual é o preço disso?") há um botão. **"Ele deixa os links em branco e o texto em cinza"**: hierarquia visual para entender o que é link. Ver [[wiki/concepts/hierarquia-visual]] e [[wiki/concepts/affordance]].
- **Sketch** ("ferramenta de prototipagem, mas voltado para o Mac"): objetivos da empresa e do usuário viram botões: "See pricing", "tente de graça" (no corpo e no menu, com login), "leia mais" em cada funcionalidade nova. "O link [...] tem a hierarquia visual maior do corpo de texto." Ver [[wiki/entities/sketch]].
- **Framer:** o link que fica fixo ao rolar é "entre" e "teste de graça". "Mesma coisa o Adobe XD."

### Consistência

- **"Escolheu um botão para sua interface, utilize o mesmo botão do mesmo jeito durante toda a sua interface."** Ver [[wiki/concepts/consistencia-visual]].
- **O que se mantém:** mesma estrutura, mesma altura, mesmo padding "do conteúdo até o fim do botão", mesmo [[wiki/concepts/border-radius]]. **O que varia:** só a largura, "de acordo com a quantidade de texto". No FrontPUSH, "inscreva-se" é menor que "grade do curso", mas o padding é igual.
- **Primário e secundário** para "estabelecer algum tipo de hierarquia com relação a funcionalidades ou principais objetivos". "Não venha colocar mais de dois botões, eu quero colocar cinco tipos de botão na minha interface, nunca é uma decisão legal."

### Anatomia

- **Área clicável:** o site é responsivo, e "a precisão que eu tenho no mouse é muito maior do que a que eu tenho com o meu dedo". Botão pequeno dificulta o clique no mobile e "aqueles que têm algum problema de visão". Ver [[wiki/concepts/area-clicavel]] e [[wiki/concepts/design-responsivo]].
- **Demo:** no DevTools, modo celular, os botões da Apple "pelo menos mantiveram o mesmo tamanho para uma tela menor".
- **Text label:** "frases muito bem claras, muito bem objetivas". Não "clique aqui para ir para tal seção do site, isso tudo em um botão só"; "sempre frases curtas e objetivas".
- **Background na cor de contraste da paleta:** o botão "sempre chame a atenção do usuário". No FrontPUSH, o azul contra o preto se repete nas labels ("3 em 1"), nos ícones e nos botões: "um ímã na visão do usuário". Ver [[wiki/concepts/contraste]].
- **Primário x secundário:** "um botão [...] que é preenchido e outro que é vazio, entre aspas, sem background". Ver [[wiki/concepts/hierarquia-visual]].

### Hover e sombra

- **Resposta à interação** é motion: "o objetivo do movimento é melhorar a interatividade". Quando a área clicável reage ao mouse, "eu entendo de forma mais clara e talvez eu fique até mais instigado em clicar". Ver [[wiki/concepts/feedback-do-sistema]].
- **Receitas de hover:** "aumenta um pouquinho de tamanho", "alguma animação", "acrescenta uma sombra de hover da cor do botão", ou muda a opacidade. No Sketch, todo link "fica um pouquinho mais clarinho" no hover.
- **Sombra:** ele remete a um post no Instagram sobre "o melhor Drop Shadow": "colocar 80% do elemento" e regras de blur, aplicadas na próxima aula. O slide traz os valores: `box-shadow: 0px 4px 25px -10px rgba(0,0,0,0.5)` em repouso e `rgba(252,189,56,0.8)` no hover (a cor do botão a 80%).

### Acessibilidade e medidas

- **"Com base em vários guidelines [...] coloque a altura mínima de 44 pixels"**; ele usou 56. Ver [[wiki/concepts/area-clicavel]].
- **Padding pelo sistema adotado:** "não é qualquer valor aleatório"; "coloque como um padrão em todos os botões". Ver [[wiki/concepts/escala-de-espacamento]] e [[wiki/concepts/grid-de-8-pontos]].
- **Slide (especificação):** botão de 56 × 260 px; tokens "gradient-orange", "black" e "button-hover gradient-orange", todos com `border-radius: 16px` e `font-size: 16px`. Tamanho de fonte fica para a seção de tipografia.

## Entities

- [[wiki/entities/nasser]]: autor (confirmado pelo usuário; o texto já indicava: "meu próprio site do FrontPUSH", "um post no meu Instagram").
- [[wiki/entities/frontpush]]: "grade do curso" + "inscreva-se"; azul como cor de contraste.
- [[wiki/entities/apple]]: links destacados; link branco x texto cinza; botões mantidos no mobile.
- [[wiki/entities/sketch]]: "See pricing", "tente de graça", "leia mais"; dois botões consistentes; hover nos links.
- [[wiki/entities/figma]]: aula prática anunciada.
- Sem página própria: Framer, Adobe XD, Instagram.

## Concepts

- [[wiki/concepts/botoes-em-interfaces]] (novo)
- [[wiki/concepts/area-clicavel]] (novo)
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/affordance]]
- [[wiki/concepts/contraste]]
- [[wiki/concepts/feedback-do-sistema]]
- [[wiki/concepts/border-radius]]
- [[wiki/concepts/escala-de-espacamento]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/elementos-da-interface]]

## Tensões com a wiki

- **"2, 4, 6, 8, 32, 64" na fala, "2, 4, 8, 16, 32, 64" no slide.** O slide é a escala geométrica que ele prefere em [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]]. A fala troca o 16 pelo 6, provável lapso. O raw mantém a fala.
- **44 px "com base em vários guidelines".** `[external]` A Apple HIG pede 44 × 44 pt; o Material, 48 × 48 dp; a WCAG 2.5.5 (nível AAA) pede 44 × 44 px CSS, e a 2.5.8 (AA, WCAG 2.2) aceita 24 × 24 com espaçamento (https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html). A aula fala só de altura; a área vale para as duas dimensões, e links dentro de texto são isentos. `[skill: ux-ui-mentor]` A skill usa 44 × 44 e atribui à 2.5.5.
- **"Nunca mais de dois tipos".** `[skill: ux-ui-mentor]` Design systems costumam ter primary, secondary, ghost e destructive, com "no máximo um primary por seção". A regra útil é **um primário por contexto**, não dois tipos no sistema todo. O próprio slide mostra um terceiro, "text button", com o mesmo visual do primário: o nome não bate com o desenho (ou o slide não foi atualizado).
- **Hover não existe no toque.** `[skill: ux-ui-mentor]` O estado que a aula ensina precisa de par: focus visível para teclado (nunca `outline: none` sem substituto) e active/pressed para toque. Micro-hover dura 100–150 ms. "Aumentar de tamanho" deve usar `transform: scale`, que não empurra o layout `[external]`.
- **"Copiar o que a Apple faz".** Funciona como ponto de partida ([[wiki/concepts/lei-de-jakob]]), mas o porquê da Apple vale para os objetivos dela. Ele mesmo começa pelo objetivo do FrontPUSH antes de mostrar os botões ([[wiki/concepts/objetivo-da-interface]]).
- **Link branco e texto cinza.** Distinguir link só por tom de cor esbarra na WCAG 1.4.1 (ver [[wiki/concepts/affordance]]). No menu da Apple, a posição já sinaliza; no corpo de texto, não basta `[external]`.
- **"Clique aqui"** como anti-exemplo bate com a orientação de usar verbo + objeto no label `[external]` (NN/g, "Click Here" e links descritivos); leitor de tela lista links fora de contexto.

## Open Questions

- **"80% do elemento"**: lido como a opacidade da sombra de hover (0.8 no slide, na cor do botão). Confiança média; o post do Instagram não foi consultado.
- **"Melhora a opacidade, o botão fica um pouco mais opaco"**: não diz se a opacidade sobe ou desce. Mantido literal.
- **"See pricing"** (legenda "Se pricing"): leitura do botão do Sketch, confiança média.
- **"Há de ter de uma boa área clicável"**, "um botão é tamanho diferente": mantidos literais.
- **Aula prática no Figma** e **próxima aula de sombras** prometidas; ainda não ingeridas.
- `date_published` vazio.

## Raw Quotes

> "Então, vamos lá, primeira coisa, que os botões, se eu fosse resumir para vocês, eles meio que guiam o usuário na jornada."

> "Escolheu um botão para sua interface, utilize o mesmo botão do mesmo jeito durante toda a sua interface."

> "A precisão que eu tenho no mouse é muito maior do que a que eu tenho com o meu dedo, no meu smartphone."

## Ver também

- [[wiki/sources/elementos-da-interface-introducao-ui-design]] — "link é diferente de botão"; botões e links anunciados na ordem do módulo
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — link azul se reconhece; botão preenchido acima do vazio
- [[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]] — o mesmo radius em botões, cards e ícones
- [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]] — a escala geométrica de espaçamento
- [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]] — a aula seguinte: as seis formas de botão
