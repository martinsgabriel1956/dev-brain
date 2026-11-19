---
type: concept
title: "Elementos de composição"
aliases: ["elemento de composição", "ambiência", "elementos de ambiência", "elementos decorativos de fundo", "background decorativo"]
date_created: 2026-11-13
date_updated: 2026-11-19
source_count: 8
tags: [ui, ui-design, elementos-da-interface, elementos-de-composicao, ambiencia, background, branding, identidade-visual]
skill: ux-ui-mentor
status: stub
---

# Elementos de composição

Elementos de fundo que "servem para dar ambiência": deixam o usuário mais imerso no tema da interface, em vez de um fundo "chapado". Estrelas, poeira cósmica, ondas, órbitas, linhas, círculos tracejados, bubbles, texturas, gradientes ([[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]]). Item do roteiro de [[wiki/concepts/elementos-da-interface]].

## Quatro regras da aula

1. **Observar os elementos da natureza** (céu, ondas, espaço).
2. **Compõem o background, sem muito [[wiki/concepts/contraste]]**: o contraste fica com o ponto focal (logo, título, CTA). Ver [[wiki/concepts/hierarquia-visual]].
3. **Acompanham a branding, a ideia, o tema**: foguete e espaço na [[wiki/entities/rocketseat]], quadrado/X/triângulo/círculo na [[wiki/entities/playstation|PSN]], eclipse no [[wiki/entities/frontpush]], Matrix no [[wiki/entities/codesec]]. Ver [[wiki/concepts/harmonia-visual]].
4. **Ajudam a compor [[wiki/concepts/empty-state|empty screens]].**

## Como se fazem (no Figma)

- Luz difusa: uma elipse na cor da marca com layer blur alto (400 no FrontPUSH).
- Iluminação: camada extra de preenchimento radial.
- Pontinhos = estrelas; riscos = estrelas cadentes; círculos = órbitas.
- Integração de fotos: [[wiki/concepts/blend-modes]].

## Não é regra

"Depende do projeto": o [[wiki/entities/spider-man-projeto-nasser|Spider-Man]] usa textura e foto, quase sem elemento de composição.

## Olhar de dev

`[skill: ux-ui-mentor]` Decorativo não é conteúdo: vai em `background-image` no CSS ou em SVG/imagem com `aria-hidden="true"` / `alt=""` (ver [[wiki/concepts/texto-alternativo]]). Se animado, respeitar `prefers-reduced-motion`. WCAG não exige contraste de elemento decorativo, mas o texto por cima precisa passar no pior ponto do fundo `[external]` (https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).

## Na visão geral

Descritos em uma frase: trazem "pontos de atenção" e deixam a interface "um pouco mais elegante" ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]).

## No style guide

"Estabelecer o branding de elementos de composição" (backgrounds, animations) também entra no [[wiki/concepts/style-guide]], com links de apoio para o comportamento ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]).

## Na prática (edição "W7")

Em [[wiki/sources/elementos-de-composicao-pratica-figma-orbitas-pontilhado-cometas-playstation]], a versão prática: "um perfume na sua interface", "a cerejinha do bolo". O slide dá cinco funções (apoio na composição de telas, refino no design, background, branding, consistência). Receita no [[wiki/entities/figma]]: formas só com stroke 3 e sem preenchimento; elipses concêntricas (Shift) com cap round e pontilhado 2, 10 (traço, espaço) para órbitas; planetinha na cor de contraste com sombra da própria cor (30%, blur "o dobro", spread −4); cometa = linha com gradiente a 45°, cap round e elipse de 6 px na ponta. Regra: "tem que ser simples", "não pode tirar a atenção do usuário". `[external]` No SVG o pontilhado vira `stroke-dasharray="2 10"` + `stroke-linecap="round"`.

## Gradientes análogos

Cores análogas, "pela transição entre elas ser suave", são "muitíssimo aplicadas para gradientes", um dos recursos de fundo desta página ([[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]]). A "variação monocromática" de azul do FrontPUSH ganha definição na mesma aula. Ver [[wiki/concepts/harmonia-de-cores]].

## Gradiente atrás do texto

Em [[wiki/sources/aplicando-paleta-de-cores-base-destaque-hierarquia-gradiente-icones]]: um elemento de composição amarelo atrás de texto branco tira o contraste ("você está dificultando a vida do usuário"). A correção é um gradiente linear: o amarelo vira "um detalhezinho, um entalhe" que some antes do texto. Ver [[wiki/concepts/contraste]] e [[wiki/concepts/paleta-de-cores]].

## Elementos 3D como ambiência

Em [[wiki/sources/axlepush-por-que-usar-o-spline-webgl-threejs]], os objetos 3D da landing page do [[wiki/entities/axlepush]] fazem o papel de elementos de composição: recoloridos em roxo e rosa para "encaixar, dar maior ambiência". O [[wiki/entities/spline]] também exporta foto e vídeo, o que permite usar o 3D como imagem sem custo de runtime.

## Key Sources

- [[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]]
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — definição em uma frase na visão geral
- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]] — branding de elementos de composição no style guide
- [[wiki/sources/elementos-de-composicao-pratica-figma-orbitas-pontilhado-cometas-playstation]] — versão prática "W7": stroke, pontilhado 2, 10, planetas com sombra, cometas
- [[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]] — análogas para gradiente; definição de monocromática
- [[wiki/sources/aplicando-paleta-de-cores-base-destaque-hierarquia-gradiente-icones]] — elemento amarelo atrás do texto corrigido com gradiente linear
- [[wiki/sources/frontpush-position-css-relative-absolute-coordenadas]]: as bolinhas do site do FrontPUSH em `position: absolute`, animadas de `top`/`left` 50/50 → 80/80 → 30/30
- [[wiki/sources/axlepush-por-que-usar-o-spline-webgl-threejs]]: AxlePUSH: elementos 3D recoloridos como ambiência
