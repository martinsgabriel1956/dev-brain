---
type: source
title: "Princípios de motion: linha do tempo, keyframes e transição entre estados (FrontPUSH)"
aliases: ["FrontPUSH motion aula 03", "Princípios Motion", "CSS Animations, aula 03"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 0
tags: [motion-design, animacao, keyframes, linha-do-tempo, easing, timing-function, transicao, css, after-effects, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-20
---

# Princípios de motion: linha do tempo, keyframes e transição entre estados (FrontPUSH)

## TL;DR

Aula 03 do mini curso de CSS Animations do [[wiki/entities/frontpush|FrontPUSH]], cerca de 11 minutos, com slide e uma demonstração em código. Autoria pela sequência e pelo lançamento do curso. Não diz o nome. [[wiki/entities/nasser|Násser]] aprendeu esses princípios no [[wiki/entities/after-effects|After Effects]], "muito mais complexo que no CSS, mas os princípios meio que se estabelecem". Os "princípios de Motion" prometidos na aula 01 são três conceitos:

- **Linha do tempo:** "o tempo transcorrido de uma determinada animação" (2 s, milissegundos). Nela se marcam os pontos de mudança.
- **[[wiki/concepts/keyframes-css|Keyframes]]:** "os pontos que você estabelece na linha do tempo". Com `@keyframes` do CSS3, "quantos estados eu quiser", de 0% a 100% (até 0,5%), mexendo em escala, opacidade, translado e skew. A fluidez vem da mesma ideia do vídeo: mais quadros por segundo, mais fluido ([[wiki/concepts/taxa-de-quadros-60fps]]).
- **Transição entre N estados ([[wiki/concepts/easing|easing]]):** como a velocidade varia entre os pontos. Frear um carro com `linear` "seria totalmente irreal"; é rápido no começo e devagar no fim ("o ease invertido").
- **Demonstração:** animação de "faltando três dias para o lançamento do curso": bolinha com `bounce in` (escala 0,3 → 1 → um pouco menor → 1, opacidade 0 → 1) e duas órbitas, cada uma com duas animações: aparecer (com delay) e girar 0 → 360deg em 7 s. "Uma linha do tempo para cada elemento."

## Key Claims

### Origem: After Effects

- "Essas noções eu aprendi muito quando estava trabalhando com o programa do Adobe, do After Effects", "justamente feito para poder fazer as animações, só que é de um nível muito mais complexo que no CSS, mas os princípios meio que se estabelecem." Ver [[wiki/entities/after-effects]].

### Linha do tempo

- "A linha do tempo literalmente é o tempo transcorrido de uma determinada animação, onde você define um tempo. Ah, eu quero que essa animação dure dois segundos."
- Nela "você consegue colocar pontos" para dizer se o objeto cresce aos poucos ou aparece já no tamanho original, se vai de opacidade 0 a 1, de escala 0 a 1, ou as duas coisas juntas. Em CSS, a duração da linha do tempo é `animation-duration` ([[wiki/concepts/keyframes-css]]).

### Keyframes

- "Key vem de chave, frame vem de foto, é literalmente um breakpoint, um ponto, onde você adiciona uma determinada característica de forma que quando passa na fluidez do tempo, você pensa que é algo fluido." Ver Precisões sobre "foto" e "breakpoint".
- Analogia com vídeo: "o vídeo nada mais é do que uma sequência de fotos"; "quanto mais frames você tem em um segundo, mais fluido parece", por isso 60 fps em vídeo e jogos ([[wiki/concepts/taxa-de-quadros-60fps]]).
- "O motion que é a propriedade do keyframes que trouxe no CSS3, é justamente eu conseguir emendar vários estados em uma linha do tempo": 0%, 0,5%, 0,7%, 1%, 5%, 10%, 20%... "N estados", mudando escala, opacidade, translado e "skew, que aí eu consigo meio que inverter o objeto, deitar o objeto" ([[wiki/concepts/transition-e-transform-css]]).

### Transição entre estados

- "A transição entre eles é muito importante." Frear um carro: "no começo do percurso o carro está mais rápido, quando ele vai freando, a velocidade dele vai diminuir." Com `linear`, "a mesma velocidade [...] no começo do percurso e [...] no final", "seria totalmente irreal".
- "Eu teria que utilizar a transição do tipo ease [...] Aqui é o ease invertido, ele é mais rápido aqui no começo e depois ele vai freando um pouquinho." Promete "ver todas as transições e como construir a nossa própria transição". Ver [[wiki/concepts/easing]].

### A animação de lançamento

- Bolinha preta: "keyframe de escala", "começou pequena, ficou maior e depois diminuiu", "de uma escala de 0 até uma escala de 1,2" e de volta a 1; "keyframe de opacidade": transparente, opaca "no momento 20% do meu keyframe".
- Cada elemento tem sua linha do tempo: o "3", a bolinha girando, os dois arcos "em um time diferente". "Eu tenho uma linha do tempo para cada elemento."
- No código: "estou aplicando o bounce in, eu acho que na bolinha"; opacidade 0, escala inicial "não era de 0, era de 0,3"; "a 50% do tempo, de 2 segundos" opacidade 1 e escala 1, "depois ela diminui um pouquinho, depois ela volta".
- Órbita 1: duas animações no mesmo elemento. A primeira, "para aparecer" (opacidade 0, escala 0,3 → escala normal), com transição, delay e "como é para terminar essa animação". A segunda dura sete segundos: de 0deg a 360deg.
- "Tudo se baseia nisso, em vários elementos, aplicando vários keyframes, numa mesma linha do tempo, cada um de forma independente ou não."

### O slide

"Princípios Motion": "Linha do tempo no CSS", com régua 0% / 50% / 100% e uma curva que cai no fim ("Exemplo: freiar de um carro"); "Keyframes"; "Transição entre n estados", com quatro curvas: reta (linear), começo lento (ease-in), começo rápido (ease-out) e uma quarta parecida com a terceira (provável `ease` ou `ease-in-out`; leitura da imagem, confiança média).

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido pela sequência e pelo lançamento do curso).
- [[wiki/entities/frontpush]]: curso; animação de "três dias para o lançamento".
- [[wiki/entities/after-effects]]: onde ele aprendeu os princípios (página criada nesta ingestão).
- [[wiki/entities/gsap]]: contraste com a "linha do tempo para cada elemento" do CSS.

## Concepts

- [[wiki/concepts/motion-design]]: os três princípios.
- [[wiki/concepts/keyframes-css]]: pontos na linha do tempo; `@keyframes` (página criada nesta ingestão).
- [[wiki/concepts/easing]]: transição entre estados, linear × ease (página criada nesta ingestão).
- [[wiki/concepts/transition-e-transform-css]]: escala, translado, skew, rotate.
- [[wiki/concepts/taxa-de-quadros-60fps]]: fluidez por quadros por segundo.
- [[wiki/concepts/breakpoint]]: o termo que ele usa para keyframe, que no CSS é outra coisa.
- [[wiki/concepts/css]]: `@keyframes` "trouxe no CSS3".

## Precisões e tensões com a wiki

- **Os "princípios" não são os 12 da Disney.** A aula 01 prometia "princípios de Motion" e a wiki inferiu, com confiança média, os 12 princípios da animação. Na prática são linha do tempo, keyframes e easing, vindos do After Effects. A inferência foi corrigida em [[wiki/concepts/motion-design]]. Dos 12 da Disney, só um aparece de fato: *slow in and slow out*, que é o easing.
- **"Frame vem de foto".** *Frame* é quadro. *Keyframe* (quadro-chave) vem da animação tradicional: o animador principal desenhava as poses-chave e os assistentes faziam os quadros intermediários (*in-betweens*). No CSS, o navegador faz os intermediários: interpola as propriedades entre os keyframes a cada quadro da tela. `[external]` sem fetch; confiança alta.
- **Keyframes não são quadros por segundo.** A analogia com 60 fps explica a fluidez, mas um `@keyframes` com 3 pontos roda a 60 fps do mesmo jeito; a taxa vem da tela e de o navegador conseguir entregar cada quadro em ~16 ms ([[wiki/concepts/taxa-de-quadros-60fps]]). Mais keyframes dão mais controle da forma do movimento, não mais fluidez.
- **"Breakpoint" é outra coisa no CSS.** Na wiki, [[wiki/concepts/breakpoint]] é a largura onde o layout muda (media query). Keyframe é um ponto no tempo; a palavra foi usada no sentido comum de "ponto de parada".
- **`@keyframes` é at-rule, não propriedade.** As propriedades são `animation-*` (`animation-name`, `-duration`, `-timing-function`, `-delay`, `-iteration-count`, `-fill-mode`). É do módulo CSS Animations, não de uma "versão 3" ([[wiki/concepts/css]]). `[external]` https://www.w3.org/TR/css-animations-1/; confiança alta.
- **"Ease invertido" é `ease-out`.** Começa rápido e desacelera: é a curva do carro freando. `ease` (o padrão) acelera um pouco no início e desacelera bastante no fim; `ease-in` começa devagar. `[external]` `ease` = `cubic-bezier(0.25, 0.1, 0.25, 1)`, `ease-out` = `cubic-bezier(0, 0, 0.58, 1)`; confiança alta. Ver [[wiki/concepts/easing]].
- **O gráfico não é de velocidade.** As curvas de easing do CSS mostram progresso × tempo; a velocidade é a inclinação. No carro freando, a curva sobe íngreme e achata no fim. A curva do slide, que "cai" perto de 100%, lê melhor como velocidade caindo, como ele narra. Confiança média (leitura da imagem).
- **Números da bolinha.** Na fala, escala 0 → 1,2 → 1 e opacidade cheia a 20%; no código, escala inicial 0,3, opacidade 1 a 50%, escala 1, "diminui um pouquinho, depois volta". Ele mesmo corrige a escala ("não era de 0, era de 0,3"). O padrão 0,3 → maior → menor → 1 lembra o `bounceIn` do Animate.css (inferência pelo nome; confiança média). "Bounce in" na legenda veio como "balse in".
- **Duas animações de `transform` no mesmo elemento brigam.** Se "aparecer" anima `transform: scale()` e "girar" anima `transform: rotate()` no mesmo elemento, a última da lista `animation` vence a propriedade `transform` inteira enquanto roda. Saídas: animar o elemento-pai e o filho separadamente, ou usar as propriedades individuais `scale` e `rotate` (suporte amplo desde 2022). Não dá para ver o código da órbita; confiança média de que o problema se aplica. `[skill: tech-mentor-frontend]`
- **"Como é para terminar" é `animation-fill-mode`.** Com `forwards`, o elemento fica no último keyframe; sem ele, volta ao estilo de antes. `[external]` confiança alta.
- **Uma linha do tempo por elemento.** Em CSS cada animação tem duração e delay próprios; sincronizar muitas exige calcular delays à mão. É aí que entra a `timeline` do [[wiki/entities/gsap|GSAP]], que encadeia animações numa linha do tempo só, como no After Effects. Ligação com o debate "biblioteca ou CSS puro" da aula 01.

## Open Questions

- O "3" que "é uma outra linha do tempo": provavelmente o número 3 dos "três dias para o lançamento" (inferência).
- O slide escreve "freiar de um carro"; a fala diz "frear". O erro de grafia é do slide.
- A aula promete "todas as transições e como construir a nossa própria transição": `cubic-bezier()` personalizado, provavelmente.

## Continuação

Na aula 04 ([[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]), o mesmo código volta como exemplo de animação "puramente implementada em CSS", e a biblioteca CSS descrita lá (classes com keyframes prontos) reforça a ligação do `bounce in` com o Animate.css.

A linha do tempo, os keyframes e a curva viram código em [[wiki/sources/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode]]: `@keyframes` com `from`/`to` ou porcentagens e as subpropriedades de `animation`.

O carro freando volta em [[wiki/sources/frontpush-propriedade-animation-parte-2-curvas-cubic-bezier-editor-chrome]] como a noção que a curva tem de passar, agora desenhada num `cubic-bezier()`.

## Raw quotes

- "os princípios meio que se estabelecem"
- "key vem de chave, frame vem de foto"
- "eu consigo colocar N estados aqui dentro"
- "se eu fosse aplicar, por exemplo, o estilo linear ou frear um carro, seria totalmente irreal"
- "eu tenho uma linha do tempo para cada elemento"
