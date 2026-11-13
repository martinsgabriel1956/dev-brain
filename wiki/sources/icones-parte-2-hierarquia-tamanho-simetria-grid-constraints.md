---
type: source
title: "Elementos da interface: ícones, parte 2 (hierarquia visual, tamanho, simetria, grid e constraints)"
aliases: ["ícones parte 2", "iconografia parte 2", "como construir um ícone", "grid de ícone no Figma"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, elementos-da-interface, icones, iconografia, hierarquia-visual, simetria, grid, figma, constraints, componentes, svg, material-design]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Elementos da interface: ícones (parte 2)

## TL;DR

Segunda aula de iconografia de [[wiki/entities/nasser|Násser]] ([[wiki/entities/frontpush|FrontPUSH]]), continuação de [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]]; anuncia uma parte 3 sobre os ícones do FrontPUSH. Seis ideias: (1) **preenchido ou linha é decisão de [[wiki/concepts/hierarquia-visual]]**: preenchido chama mais atenção (o botão "Get More with Pro" do [[wiki/entities/font-awesome]]), linha é mais neutra, e dá para subir a hierarquia de um ícone de linha pela cor de destaque e pela posição; (2) **tamanho importa pouco**: o [[wiki/entities/material-design]] diz 24×24, ele usa 56×56 para ícones de ênfase e 32×32 para os menores, mas como o ícone é [[wiki/concepts/formato-svg|SVG]] ele escala; (3) **margem e ponto focal**: não encostar o desenho na borda do frame; (4) **[[wiki/concepts/simetria-visual|simetria]] e tamanhos pares**: círculo de 7×7 num frame de 24 "fica torto", e o triângulo do play centralizado pela matemática parece descentralizado ([[wiki/concepts/centralizacao-optica]]); (5) **[[wiki/concepts/grid-de-icones|grid de construção]]**: área útil de 20×20 num frame de 24, quadrado, círculo, X e um círculo central, agrupados, com opacidade de 20–30% e travados; (6) **constraints em scale + componente no [[wiki/entities/figma]]**: o ícone vira componente e as instâncias escalam com as proporções certas (16 → 36).

## Key Claims

### Recapitulação da parte 1

- **Ícone como pista visual e "senso comum"**, ligado aos [[wiki/concepts/padroes-de-interface|patterns]]; escolher ou construir uma [[wiki/concepts/familia-de-icones|família]] alinhada à identidade visual.
- **[[wiki/concepts/consistencia-visual]]:** escolhida a forma de construir (linha, linha mais fina, preenchimento, duas cores), "construa o resto de todos os seus ícones seguindo essas mesmas linhas".
- **Reduz a [[wiki/concepts/carga-cognitiva]]** por ser representação visual simples.
- **"Não levar ao pé da letra"**, adaptar ao cliente e à realidade (dito duas vezes).

### Preenchido x linha é hierarquia

- **Pergunta do aluno:** "quando é que é melhor eu fazer ele preenchido, quando é que é melhor eu fazer ele por stroke?" Resposta: "a ideia de hierarquia visual". Ver [[wiki/concepts/hierarquia-visual]].
- **Exemplo do [[wiki/entities/font-awesome]]:** "Start for Free" x "Get More with Pro". O botão de assinatura é o que o negócio quer destacar, "por isso que ele é preenchido, [...] tem uma maior área preenchida".
- **Ícone só de linha é "mais neutro, um pouco mais apagado", "mas às vezes é justamente essa a intenção"**: ícones pretos de linha ficam "assentados no seu lugar, comunicando nas abas, nos menus".
- **Preto e branco "não são cores, são extremos de luz"**, por isso deixam os ícones mais neutros.
- **Subir a hierarquia sem trocar o estilo:** nas seções de ícones do FrontPUSH ele manteve a linha (identidade e consistência) mas pintou de azul, "a cor de destaque da minha paleta de cores", e os pôs "em primeiro, à esquerda". Ver [[wiki/concepts/contraste]].
- **"Um jogo complexo de várias variáveis"**: posicionamento, tamanho, formas, preenchimento. "Não existe fórmula pronta."
- **Variações de um mesmo ícone no Font Awesome:** preenchido, regular, light, thin e duotone ("preenchimento, mas utilizando duas cores"). Cada variação "pode transmitir ideias diferentes".

### Tamanho

- **"System icons are displayed 24 por 24"** ([[wiki/entities/material-design]]). "Regra a ser seguida de forma literal? Não."
- **Ele divide os ícones em dois grupos:** os de hierarquia maior e os mais neutros. A setinha no botão do FrontPUSH é neutra porque é azul em botão azul (pouco [[wiki/concepts/contraste]]) e menor que os outros, que têm "contraste maior, um tamanho maior e um posicionamento onde eu enxergo eles primeiro".
- **Tamanhos que ele usa:** 56×56 para ênfase, 32×32 para os menores; 24×24 também serve.
- **"O tamanho não é a coisa que mais importa"** porque o ícone "deve ser exportado como SVG", que é vetor e escala. Ver [[wiki/concepts/formato-svg]].
- **Desenhar pequeno ajuda:** com zoom num frame pequeno, o Figma mostra o pixel grid sozinho ("se eu vir aqui tem grid, se eu vir aqui não tem").

### Margem e ponto focal

- **Material pede margem, "espaço em branco"**: não "colar todos os pontos" do círculo na borda do frame; "é interessante que você tenha um pontinho focal também no ícone". Ver [[wiki/concepts/espaco-em-branco]].

### Simetria e tamanhos pares

- **"O olho humano consegue perceber que alguma coisa está torta."** Um círculo de 7×7 (ímpar) dentro de um de 18×18 num frame de 24×24 não centraliza: "faltando um pixel ali, você vai perceber". Ver [[wiki/concepts/simetria-visual]].
- **Triângulo do play:** centralizado pelas guias do Figma, "mas para o olho humano ele está centralizado? Logicamente que não", porque "a base do triângulo [ocupa] mais espaço do que a ponta". Ver [[wiki/concepts/centralizacao-optica]].
- **Segundo ele, o Figma "automaticamente coloca dois espaços aqui em branco"** no shape de triângulo para o play ficar no centro. Não verificado (ver open questions).
- **Regra prática:** simetria, tamanhos pares e margem.

### Grid de construção

- **Área útil do Material:** frame de 24×24, área de 20×20, "dois pontos" de cada lado. Ele desenha um retângulo de 20×20 e as linhas guia. Ver [[wiki/concepts/grid-de-icones]].
- **O grid dele:** quadrado com stroke em cinza, elipse (o tamanho do Material "muito apertado ainda", ele deixa "um pouco mais espaçado", "eu gosto de ser clean"), círculo, "gray 6", um X e um quadrado ou círculo a mais no meio, "formas de a gente concentrar o ponto focal".
- **Construir dentro do círculo:** mesmo ícone mais retangular ou "em pé" (microfone) pode sobrar "um pouquinho para cima, um pouquinho para baixo", mas fica centrado no círculo.
- **Fluxo no Figma:** Ctrl G no grid, opacidade de 20–30% no grupo (pass-through), travar o grupo para não mover. "Eu sempre aplico grids para a gente conseguir a maior exatidão possível e consistência possível."

### Constraints e componentes

- **Constraints dizem "como o objeto vai se comportar quando eu modificar as dimensões do frame".** Fixado em top e left, o ícone fica parado ao puxar o frame para a direita e se move ao puxar pela esquerda ou por cima; right-bottom faz o contrário.
- **Para ícone, constraints em scale.** Ver [[wiki/entities/figma]].
- **Transformar em componente "é altamente recomendável"**, porque o ícone se reusa em outras seções. Fluxo: esconder o grupo do grid ("grid-icon"), tirar o fundo, criar o componente, copiar e colar a instância e redimensionar; ela "mantém as mesmas proporções de distância" (de 16×16 a 36×36). "Vai aumentar demais a sua consistência quando você estiver construindo os seus assets."
- **Anuncia mais uma aula** sobre os ícones feitos para o FrontPUSH.

## Entities

- [[wiki/entities/nasser]]: autor (legenda: "Nasser", "Nárcia", "eu nasci").
- [[wiki/entities/font-awesome]] (novo): site de ícones que ele usa e indica no Notion; exemplo dos dois botões e das variações.
- [[wiki/entities/material-design]]: 24×24, área útil 20×20, margem.
- [[wiki/entities/figma]]: pixel grid no zoom, triângulo, Ctrl G, travar, constraints, componentes.
- [[wiki/entities/frontpush]]: ícones de linha em azul; setinha neutra no botão; ícone de 16×16 "iconCircle".
- Sem página própria: Notion (links do curso).

## Concepts

- [[wiki/concepts/grid-de-icones]] (novo)
- [[wiki/concepts/centralizacao-optica]] (novo)
- [[wiki/concepts/icones-em-interfaces]]
- [[wiki/concepts/familia-de-icones]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/simetria-visual]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/contraste]]
- [[wiki/concepts/espaco-em-branco]]
- [[wiki/concepts/formato-svg]]
- [[wiki/concepts/carga-cognitiva]]
- [[wiki/concepts/padroes-de-interface]]

## Tensões com a wiki

- **Material Design conferido (M3).** `[external]` A página "Designing icons" do Material 3 confirma: ícones padrão em 24dp×24dp; conteúdo limitado a uma live area de 20dp×20dp, com 2dp de padding; tamanhos ópticos adicionais de 20, 40 e 48dp; keyline shapes de quadrado 18dp, círculo 20dp, retângulo vertical 16×20 e horizontal 20×16; ícones "on pixel"; stroke recomendado de 2dp; "simple, modern, friendly, and sometimes quirky" (https://m3.material.io/styles/icons/designing-icons, lido em 2026-11-13). O conteúdo pode se estender ao padding "if additional visual weight is needed", o que bate com "pode sobrar um pouquinho para cima". A página do M2 segue sem renderizar o texto.
- **O círculo de 18 dele x keyline de 20 do Material.** Ele desenha o círculo em 18×18 e diz que o Material é "muito apertado"; no M3 o círculo-keyline tem 20dp e o quadrado 18dp. Não é contradição: ele escolhe deliberadamente mais respiro que a diretriz.
- **56 e 32 x 20/24/40/48.** Os tamanhos que ele usa não estão entre os do Material 3; como ele mesmo diz, o SVG escala. `[skill: ux-ui-mentor]` Ícone clicável precisa de alvo de toque de pelo menos 44×44 px, mesmo que o desenho seja menor ("nunca ícones de 16px clicáveis sozinhos"); e ícone informativo pede contraste de 3:1, o que a setinha azul em botão azul talvez não tenha. Como ela acompanha o texto do botão, é decorativa (`aria-hidden="true"`).
- **"O tamanho não é a coisa que mais importa" x pixel grid.** O SVG escala sem perder nitidez, mas o próprio Material pede desenhar "for viewing at 100% scale" e oferece tamanhos ópticos: um ícone de 24 ampliado para 56 mantém o stroke proporcional (fica mais grosso), e um reduzido pode cair fora do pixel. Escalar é possível; ser ótimo em todo tamanho, não necessariamente (inferência do agente, apoiada na página do M3).
- **Triângulo do Figma "com dois pixels vazios".** Não verificado. `[external]` O fenômeno em si é conhecido: o centro geométrico do bounding box de um triângulo não coincide com o centroide (a 1/3 da altura a partir da base), e ícones de play costumam ser deslocados para o lado da ponta. Se é o Figma que compensa ou se é o shape usado na aula, a aula não deixa claro.
- **Preenchido = destaque, e a parte 1.** Na parte 1, preenchido e arredondado = amigável (Iconly no Creator Push). Aqui, preenchido = hierarquia. As duas leituras convivem: o estilo da família vem da identidade visual, e dentro da interface o preenchimento é um dos meios de destacar (o Font Awesome mostra o mesmo ícone em vários estilos).
- **Consistência x cor de destaque.** Pintar alguns ícones de azul não quebra a [[wiki/concepts/consistencia-visual]]: ele manteve a família (linha) e mudou só a cor, dentro da paleta.

## Open Questions

- **"Pontos hipo importantíssimos"**: provável "super"; mantido literal.
- **"Balanceio"** de formas geométricas: provável "balanceamento"; mantido literal.
- **"Font -s1" → Font Awesome** (2×): inferido pelos estilos citados (preenchido/solid, regular, light, thin, duotone), que são os do Font Awesome; o site hoje mostra "Solid · Regular · Light · Thin" (https://fontawesome.com/, 2026-11-13), mas os botões "Start for Free" e "Get More with Pro" não estão mais na home. Confiança média-alta.
- **"Right -button" → right-bottom** e **"move to" → move tool**: correções de confiança média.
- **"Ícones do front"** marcado como `Front[PUSH]` no raw.
- **Qual o tamanho do círculo central e do X no grid dele?** Não ditos; só a área útil (20) e o círculo (18).
- **Parte 3** (os ícones do FrontPUSH): ingerida em [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]].
- `date_published` vazio.

## Raw Quotes

> "Quando você coloca ícone só de linha, você percebe que eles são um pouco mais neutros, um pouco mais apagados, mas às vezes é justamente essa a intenção."

> "Por isso que não existe fórmula pronta."

> "O olho humano consegue perceber que alguma coisa está torta, principalmente quando a gente fala de ícones."

> "Eu sempre aplico grids para a gente conseguir a maior exatidão possível e consistência possível."

## Ver também

- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — constraints na edição "W7": ícone do plugin deformando com o frame
- [[wiki/concepts/constraints-no-figma]]
