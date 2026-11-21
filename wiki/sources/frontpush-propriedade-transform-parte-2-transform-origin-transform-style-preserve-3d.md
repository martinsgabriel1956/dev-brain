---
type: source
title: "Propriedade transform, parte 2: transform-origin e transform-style (FrontPUSH)"
aliases: ["FrontPUSH motion, básico CSS aula 02", "Propriedade transform pt.2", "transform parte 2", "CSS Animations, básico CSS, aula 02"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 0
tags: [css, transform, transform-origin, transform-style, preserve-3d, perspective, 3d, hover, transition, motion-design, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-20
---

# Propriedade transform, parte 2: transform-origin e transform-style (FrontPUSH)

## TL;DR

Segunda aula do módulo "Básico CSS" do mini curso de CSS Animations do [[wiki/entities/frontpush|FrontPUSH]], cerca de 15 minutos, com slide e código ao vivo. Continua a [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva|parte 1]]. [[wiki/entities/nasser|Násser]] não diz o nome; autoria pela sequência. Duas propriedades que "ajudam a configurar a propriedade transform": "dominem essa propriedade, eu posso dizer 70% dela a gente vai entender".

- **`transform-origin`** muda o "ponto de ancoragem", o eixo de rotação: X, Y e Z; X e Y aceitam `left`/`center`/`right`, comprimento ou porcentagem; Z só comprimento ([[wiki/concepts/transform-origin-css]]). Demo: `rotate(180deg)` no hover com `transition: all 1s ease`, girando em torno de `center`, `0% 0%`, `50% 0%`, `100%`. Prefere porcentagem, "mais intuitivo". Importante para SVG.
- **`transform-style`**: `flat` (padrão) achata os filhos; `preserve-3d` faz os filhos "preservar a visão 3D". Demo: `.parent` com `perspective: 200px` e `rotateY(30deg)`, `.box` filho com `rotateX(70deg)`; com `preserve-3d` os dois giros aparecem juntos ([[wiki/concepts/perspective-css]]).
- **"O CSS já faz isso"**: as bibliotecas JS "auxiliam justamente essa manipulação [...] que não é muito simples" ([[wiki/concepts/css-puro-vs-biblioteca-de-animacao]]).

## Key Claims

### O slide

"Domine a propriedade transform". "Propriedades transform":

- `transform-origin: x-axis y-axis z-axis;` → "Mudar o ponto de ancoragem". x-axis e y-axis: `left`, `center`, `right`, "lenght", `%`. z-axis: "lenght".
- `transform-style: flat | preserve-3d | initial | inherit;` → "flat: valor padrão do objeto. Specifies that child elements will NOT preserve its 3D position"; "preserve-3d: Specifies that child elements will preserve its 3D position".
- `transform:` → "Manipulação de objetos": `rotate(angle)`, `rotate3d(x,y,z,angle)`, `skew(x-angle,y-angle)`, [...].

O usuário enviou também um diagrama "Definindo ponto de ancoragem": um quadrado com os nove pontos nomeados por palavras-chave (`top left`, `top center`, `top right`, `center left`, `center center`, `center right`, `bottom left`, `bottom center`, `bottom right`). O estilo difere do slide do curso; a origem não está clara.

### Material de apoio

- "Vocês vêm aqui no W3C e colocam a propriedade transform. [...] tem vários exercícios [...] clicando nos exemplos que essa plataforma oferece." Ver [[wiki/entities/w3c]], [[wiki/entities/w3schools]] e Precisões.

### transform-origin

- "Lembra que eu disse na primeira aula sobre mudar o ponto de ancoragem, meio que é o eixo do elemento": "a primeira informação no X, depois no Y e no Z. No X e no Y tem como colocar o left, center, right, ou um determinado valor ou em porcentagem, enquanto no Z tem como colocar um valor fixo". Ver [[wiki/concepts/transform-origin-css]].
- `center` diz que "no eixo X ele está centralizando e no eixo Y ele está centralizando".
- Montagem da demo: `rotate(20deg)`, depois um hover que gira "de 0 para 180" e um `transition` "para não ficar bruto": "tem como eu especificar qual é a transição de qual propriedade [...] e tem como eu fazer de todas, eu coloco all", "um segundo e o modo da transição do modo ease" ([[wiki/concepts/transition-e-transform-css]], [[wiki/concepts/easing]]). O hover "é um pseudo-element que muda o estado atual do objeto" (é pseudo-classe; ver Precisões e [[wiki/concepts/pseudo-classe-css]]).
- No modo responsivo do DevTools, "eu tenho que simular isso com o clique, não passando o mouse".
- `0% 0%`: o eixo vai ao canto ("o 0 do Y é aqui [...] no X ele veio para cá"). `50% 0%`: meio da borda de cima. `50% 50%` "vai funcionar como se fosse o center-center". "0% em X é aqui, 50% em X é no meio, 100% em X é aqui"; "pode colocar valores quebrados também".
- "Eu utilizo muito da porcentagem porque eu acredito que é mais intuitivo." Nas palavras-chave: "quando é Y, é left ou right [...] quando é no X, ou é top ou é bottom" (eixos trocados; ver Precisões).
- "Ele é muito importante para quando a gente estiver falando de SVGs e quando você quer [...] mudar esse eixo de rotação" ([[wiki/concepts/formato-svg]]).

### transform-style

- Envolve `.box` numa `.parent` "porque eu vou ter que aplicar perspectiva". Na `.box`: `rotateX(70deg)`; com a perspectiva do body "está pegando certinho"; tirando-a, "como se tivesse só diminuído" (a observação da parte 1).
- `.parent` do mesmo tamanho, `background-color: #CCC`, mesmo `border-radius`, e "o pulo do gato": `perspective: 200px` no pai. Depois `rotateY(30deg)` na própria `.parent`: "não aconteceu nada, então ele simplesmente diminuiu, talvez porque eu teria que colocar a perspectiva no cara de cima também, que é o pai do pai".
- "O valor flat é o valor padrão [...] os elementos filhos não vão preservar o elemento 3D, já quando eu coloco preserve-3d [...] os elementos filhos irão preservar a visão 3D." Com `preserve-3d` "esse aqui também rotacionou no eixo Y"; "o flat ele leva em consideração só ele, não o filho". "Quando tem um elemento filho que também está rotacionado, ele vai começar a dar noção de perspectiva e realmente de elemento 3D no CSS." Ver [[wiki/concepts/perspective-css]].
- Testes ao vivo no DevTools: "clicar com o botão direito no Chrome, vir em inspecionar [...] você clica no objeto e ele vai aparecer aqui o CSS do objeto".

### CSS e bibliotecas

- "Ver que o CSS já faz isso e aquelas bibliotecas JS que eu comentei [...] auxiliam justamente essa manipulação que você está vendo que não é muito simples você entender, tem que colocar perspectiva, tem que colocar o preservar 3D." Ver [[wiki/concepts/css-puro-vs-biblioteca-de-animacao]].
- "Pense na possibilidade de coisas que dá para você agora colocar transitando esses estados utilizando a animação" ([[wiki/concepts/motion-design]]). "Me marque lá no Instagram que eu vou repostar."

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/frontpush]]: curso; módulo "Básico CSS" do mini curso.
- [[wiki/entities/w3c]] e [[wiki/entities/w3schools]]: o "W3C" recomendado; o texto do slide é do W3Schools.
- [[wiki/entities/chrome-devtools]]: inspecionar e editar o CSS ao vivo; modo responsivo.

## Concepts

- [[wiki/concepts/transform-origin-css]]: ponto de ancoragem (página criada nesta ingestão).
- [[wiki/concepts/perspective-css]]: `transform-style: preserve-3d` e a perspectiva no "pai do pai".
- [[wiki/concepts/transition-e-transform-css]]: `transition: all 1s ease` no hover.
- [[wiki/concepts/pseudo-classe-css]]: `:hover`, chamado de pseudo-element.
- [[wiki/concepts/easing]]: `ease`, prometido para depois.
- [[wiki/concepts/formato-svg]]: onde o `transform-origin` pesa.
- [[wiki/concepts/css-puro-vs-biblioteca-de-animacao]], [[wiki/concepts/motion-design]].

## Precisões e tensões com a wiki

Todas `[skill: tech-mentor-frontend]` ou `[external]` sem fetch, por conhecimento prévio da especificação CSS Transforms (w3.org/TR/css-transforms-1 e -2), do MDN e do W3Schools.

- **O "W3C" da aula é o W3Schools.** O texto em inglês do slide ("Specifies that child elements will NOT preserve its 3D position") e a sintaxe `flat|preserve-3d|initial|inherit` são os da página de `transform-style` do W3Schools, e os "exercícios" em que se clica são o "Try it Yourself". Reforça o padrão já anotado em [[wiki/entities/w3c]]. Confiança alta.
- **Os eixos das palavras-chave estão trocados na fala.** `left`/`right` são do X, `top`/`bottom` do Y. Funciona mesmo assim porque, com duas palavras-chave, o navegador as identifica pelo nome: `top center` = `center top`. Com números, a ordem é obrigatoriamente X Y. Confiança alta.
- **Detalhes da sintaxe.** Um valor só (`center`, `left`) vale para os dois eixos (o outro fica `center`); o padrão é `50% 50% 0`; porcentagens são do próprio elemento; valores fora de 0–100% e negativos levam o eixo para fora da caixa (órbitas). Z aceita só comprimento, como ele diz. Confiança alta.
- **`:hover` é pseudo-classe, não pseudo-elemento.** Pseudo-elementos (`::before`, `::after`) criam partes novas; pseudo-classes descrevem estados ([[wiki/concepts/pseudo-classe-css]]). Confiança alta.
- **`transition: all` é cômodo, não ideal.** Anima qualquer propriedade que mude, inclusive as caras; nomear `transform` é mais seguro. Para animar a ida e a volta, a `transition` vai na regra base, não só no `:hover` ([[wiki/concepts/transition-e-transform-css]]). A legenda não diz onde ele a pôs. Confiança alta.
- **Hover no modo responsivo:** a emulação de toque troca o mouse pelo toque e o hover fica "grudado" até tocar fora, como num celular real. Quem anima no hover deve prever `@media (hover: hover)` ou um equivalente em foco/clique ([[wiki/concepts/microinteracao]]). Confiança alta.
- **O palpite do "pai do pai" está certo.** A propriedade `perspective` afeta os filhos, não o próprio elemento. Sem perspectiva no body (ele a apagou), o `rotateY` da `.parent` só achata. A perspectiva de 200 px da `.parent` vale para a `.box`. Confiança alta.
- **O que `preserve-3d` faz de fato.** Com `flat`, os filhos são desenhados no plano do pai e giram junto como uma figura chapada. Com `preserve-3d`, filhos e pai dividem o mesmo espaço 3D: a rotação X da `.box` se compõe com a rotação Y da `.parent`. O valor não é herdado; cada nível de um cubo aninhado precisa dele. Confiança alta.
- **Pegadinha não mencionada.** `overflow` diferente de `visible`, `opacity` < 1, `filter`, `clip-path`, `mask` e `isolation: isolate` no pai forçam `flat` mesmo com `preserve-3d` (propriedades de agrupamento da especificação). É a causa comum de "o preserve-3d não funciona". Confiança alta.
- **Slide:** "lenght" é erro de digitação de *length*; `initial` e `inherit` são palavras-chave globais de qualquer propriedade (assim como `unset` e `revert`). Confiança alta.
- **`transform-origin` no SVG.** Em elementos SVG o padrão é `0 0` (canto do viewport do SVG), não o centro; para girar um ícone no lugar, use `transform-box: fill-box` com `transform-origin: center`. É o motivo de ele dizer que a propriedade é "muito importante" em SVG ([[wiki/concepts/formato-svg]]). Confiança alta.
- **"O CSS já faz isso"** confirma o que a parte 1 mostrou: 3D de cartões e caixas sai em CSS puro. Ele agora diz que as bibliotecas "auxiliam", em vez de "imprescindíveis" (aula 04).
- `prefers-reduced-motion` segue ausente.

## Open Questions

- A legenda termina no meio da frase ("é isso sobre a propriedade transform,"); o fechamento da aula não foi transcrito.
- "Mudar o..." na `.parent`: a fala se interrompe e retoma quatro segundos depois.
- A "terceira [posição] que é a Z, mas não precisa da gente entender agora": não foi retomada.
- De onde é o diagrama "Definindo ponto de ancoragem" enviado junto?

## Continuação

O `transition` usado no hover, "uma propriedade que a gente ainda vai estudar", é contrastado com `animation` em [[wiki/sources/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode]]: dois estados × N estados.

## Raw quotes

- "dominem essa propriedade, eu posso dizer 70% dela a gente vai entender"
- "meio que é o eixo do elemento"
- "talvez porque eu teria que colocar a perspectiva no cara de cima também, que é o pai do pai"
- "o flat ele leva em consideração só ele, não o filho"
- "ver que o CSS já faz isso"
