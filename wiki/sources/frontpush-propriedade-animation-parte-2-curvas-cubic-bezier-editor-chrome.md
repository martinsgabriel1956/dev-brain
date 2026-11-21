---
type: source
title: "Propriedade animation, parte 2: as curvas e o cubic-bezier (FrontPUSH)"
aliases: ["FrontPUSH motion, básico CSS aula 04", "Propriedade animation pt.2", "animation parte 2", "CSS Animations, básico CSS, aula 04"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 0
tags: [css, animation, easing, cubic-bezier, timing-function, devtools, chrome, motion-design, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-propriedade-animation-parte-2-curvas-cubic-bezier-editor-chrome.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-20
---

# Propriedade animation, parte 2: as curvas e o cubic-bezier (FrontPUSH)

## TL;DR

Quarta aula do módulo "Básico CSS" do mini curso de CSS Animations do [[wiki/entities/frontpush|FrontPUSH]], cerca de 7 minutos, com trechos sem fala. [[wiki/entities/nasser|Násser]] diz o nome ("Ah, Násser, mas eu quero um padrão que é só o meu"). Continua a [[wiki/sources/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode|parte 1]] pela `animation-timing-function` ([[wiki/concepts/easing]]).

- **Editor de curvas do [[wiki/entities/chrome-devtools|DevTools]]:** clicando no ícone da curva ao lado do valor, mostra `ease-in-out` ("curvinha no começo e [...] no final"), `ease-out` e presets como *out sine* e *out back*. "Se você colocar ease meio que já está ok."
- **Curva própria com `cubic-bezier`:** arrastando os pontos de controle, a animação vem "muito rápida", "quase parando" e sai "rápida de novo"; com a curva dobrada, "ela vai ir e voltar".
- **O site [[wiki/entities/cubic-bezier-com|cubic-bezier.com]]** ("digitar cubic-bezier [...] nessa primeira ferramenta", também no Notion do curso): presets, duração, comparação com `linear` e botão *copy* para colar no lugar de `ease`.
- **Leitura do gráfico:** horizontal é o tempo ("literalmente é a sua linha do tempo"), vertical é "a progressão".
- **De volta ao carro freando:** "primeiro vem rápido, depois que ele vai freando, vai indo devagar" é a noção que a curva tem de passar.

## Key Claims

### Abertura

- "Aqui vai a parte 2 [...] a gente vai executar aquela animação que a gente fez no primeiro momento, só que agora utilizando a propriedade animation." "Essas propriedades são uma avalanche [...] é com muita prática que você vai pegando, fazendo todo dia."
- A legenda tem um vazio de 15 s logo depois (0:37–0:52); a fala volta já no editor de curvas.

### O editor do Chrome

- "Ele tem essa ferramenta aqui para poder a gente conhecer um pouco mais de como funcionam as curvas": `ease-in-out` "vai mais devagar, depois mais rápido e depois mais devagar"; `ease-out` "é o contrário" da curva anterior.
- "Esses aqui são as formas de curva padrão do sistema, então se você colocar ease meio que já está ok essa forma, porque ela é muito utilizada." "Outras formas, que é a out-sine", "out-back".
- Acesso: "é só você vir no console, clicar na sua div [...] ele vai aparecer aqui, esse Open cubic bezier editor" ([[wiki/entities/chrome-devtools]]).

### Criando a própria curva

- "Eu quero um padrão que é só o meu, aí você pode vir aqui e estabelecer o cubic-bezier, e aí você cria o seu próprio padrão de movimento."
- "Mais longe está da minha reta aqui, dessa reta cinza aqui, mais rápido é." Esticando o ponto, "ela vai praticamente parar no meio, e como fez uma curva aqui, ela vai ir e voltar, e aí depois ela vai rápido de novo." Ver Precisões.
- "Esse editor do Google Chrome é muito legal para [...] construir a nossa transição entre os estados da melhor forma possível."

### O site cubic-bezier

- "Você pode vir aqui no Google, digitar cubic-bezier, vem aqui nessa primeira ferramenta, eu até deixei também no Notion": "aqui são os modos padrões, tem como mudar a duração, e ele faz a comparação de um modo normal, linear, com o que você acabou de criar" ([[wiki/entities/cubic-bezier-com]]).
- "Isso eu fui pegando com o tempo, depois de muito executar": "da esquerda para a direita [...] é o tempo, literalmente é a sua linha do tempo, e aqui no eixo vertical é a progressão". Para não "ir e voltar", "eu tenho que deixar isso reto, o mais reto possível".
- "É só vir aqui em copy [...] e ao invés de colocar ease, eu coloco o cubic-bezier", salva, e a animação "está aplicando justamente essa curva".

### A curva do carro

- "A gente vai ter que começar a estudar qual é o tipo de curva": o carro freando "tem que vir primeiro rápido [...] não pode ser abrupto e nem começar devagar", "então eu preciso passar essa noção na curva do motion, na curva que faz e caracteriza a transição entre os estados". Retoma a aula de princípios ([[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]]).
- Depois de 14 s sem legenda, a aula termina em "Tudo junto, beleza?".

## Entities

- [[wiki/entities/nasser]]: instrutor; diz o nome.
- [[wiki/entities/frontpush]]: curso; Notion com o link do cubic-bezier.
- [[wiki/entities/chrome-devtools]]: editor de curvas no painel de estilos (página criada nesta ingestão).
- [[wiki/entities/cubic-bezier-com]]: ferramenta de curvas (página criada nesta ingestão).
- [[wiki/entities/google]]: o Chrome.

## Concepts

- [[wiki/concepts/easing]]: curvas-padrão, `cubic-bezier`, leitura do gráfico, o carro freando.
- [[wiki/concepts/keyframes-css]]: `animation-timing-function` no shorthand.
- [[wiki/concepts/motion-design]].

## Precisões e tensões com a wiki

Todas `[skill: tech-mentor-frontend]` ou `[external]` sem fetch, por conhecimento prévio da especificação CSS Easing Functions (w3.org/TR/css-easing-1) e do MDN.

- **"O ease [...] vai devagar e depois vai mais rápido"** descreve o `ease-in`, não o `ease`; logo em seguida ele diz que a próxima ("ease-out") "é o contrário". Pode ser lapso ou a legenda ter comido o "in"; deixado literal. O `ease` acelera rápido e desacelera longamente ([[wiki/concepts/easing]]). Confiança média-alta.
- **Velocidade é a inclinação, não a distância da reta.** A diagonal cinza é o `linear`. Ficar acima dela significa estar *adiantado* em relação ao linear; o que dá a velocidade em cada instante é a inclinação da curva. Na prática as duas coisas andam juntas no começo da curva, por isso a regra dele funciona como intuição. Confiança alta.
- **Por que a curva "vai e volta".** Em `cubic-bezier(x1, y1, x2, y2)`, os x precisam ficar entre 0 e 1 (o tempo não volta), mas os y podem sair desse intervalo: a progressão passa de 100% ou fica abaixo de 0% e retorna. É o *overshoot* dos presets *back*. Propriedades que não aceitam valor fora da faixa (`opacity`, `width` negativa) são limitadas na ponta. Confiança alta.
- **Presets do DevTools.** As famílias *sine*, *quad*, *cubic*, *back* etc. vêm das equações de easing de Robert Penner, populares no Flash e listadas no easings.net; o DevTools as converte em `cubic-bezier`. Confiança média-alta.
- **O que `cubic-bezier` não faz:** mola com vários quiques ou *bounce* real, porque é uma única curva de quatro pontos. Para isso existe `linear()` com muitos pontos (suporte amplo desde 2023) ou uma biblioteca ([[wiki/concepts/css-puro-vs-biblioteca-de-animacao]]). `steps()` faz movimento em degraus. Confiança alta.
- **A demo prometida não aparece na legenda.** "Executar aquela animação [...] utilizando a propriedade animation" fica nos vazios de 0:37–0:52, 2:56–3:06 e 6:52–7:06; só o "Tudo junto, beleza?" final sugere que ela foi montada.
- Curvas com *overshoot* e quique são das que `prefers-reduced-motion` mais pede para suavizar; segue ausente.

## Open Questions

- Que animação foi montada nos trechos sem fala?
- "A progressão de 2,3 segundos [...] onde faz em dois segundos": quais eram as durações comparadas no site?
- "Out-sine" e "out-back" foram reconstruídos de "out -sign" e "Outback" pelos nomes dos presets do DevTools (confiança média).

## Continuação

Encerra a parte de `animation` do módulo "Básico CSS"; a grade da parte 1 ainda lista `opacity` e `position` entre as propriedades de motion.

## Raw quotes

- "essas propriedades são uma avalanche"
- "eu quero um padrão que é só o meu"
- "literalmente é a sua linha do tempo, e aqui no eixo vertical é a progressão"
- "o carro primeiro vem rápido, depois que ele vai freando, vai indo devagar"
