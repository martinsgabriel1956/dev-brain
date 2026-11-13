---
type: source
title: "Elementos da interface: imagens e ilustrações, parte 3 (bom senso, ferramenta de contraste, padronização e blend modes)"
aliases: ["aula de imagens parte 3", "imagens e ilustrações parte 3", "blend modes no Figma", "padronização de imagens"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, elementos-da-interface, imagens, ilustracoes, contraste, acessibilidade, wcag, padronizacao, aspect-ratio, handoff, blend-modes, figma, composicao-de-imagens, gradiente]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Elementos da interface: imagens e ilustrações (parte 3)

## TL;DR

Terceira aula de [[wiki/entities/nasser|Násser]] sobre [[wiki/concepts/imagens-em-interfaces|imagens]] no curso do [[wiki/entities/frontpush|FrontPUSH]], depois de [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao|parte 1]] e [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto|parte 2]]. Quatro blocos: (1) **bom senso**: a imagem precisa acompanhar o que está ao lado dela, seja para ambientar ou para complementar uma ação (biometria, app em língua desconhecida); (2) **ferramenta de [[wiki/concepts/contraste]]**: o [[wiki/entities/who-can-use]] simula problemas de visão e dá nota ao par cor do texto / cor do fundo, complementando o gradiente de [[wiki/concepts/texto-sobre-imagem]]; (3) **padronização**: imagem de ponta a ponta exige banco em alta resolução (até 4K) e todas as imagens no mesmo [[wiki/concepts/aspect-ratio]], para o desenvolvedor copiar e colar sem ajuste; (4) **[[wiki/concepts/blend-modes]] no [[wiki/entities/figma]]**: máscara com gradiente radial e modos como color dodge, lighten e difference "tiram" o fundo preto de fotos de alto contraste do [[wiki/entities/unsplash]]. Foi assim que ele fez os wallpapers do FrontPUSH, "não precisei utilizar Photoshop".

## Key Claims

### Bom senso na escolha da imagem

- **A imagem "precisa acompanhar o entendimento e aquilo que é passado ao lado dela."** Ela passa uma essência ou ideia, ou complementa uma ação que o usuário precisa tomar. Ver [[wiki/concepts/imagens-em-interfaces]].
- **Dois papéis:** ambientar e dar sensações ao usuário, ou complementar o que está sendo pedido.
- **Exemplo da biometria:** apps que pedem foto do rosto mostram antes uma pequena animação ou fotografia descrevendo a etapa.
- **Exemplo do idioma:** num app em japonês ou chinês, "uma boa ilustração ou uma boa imagem" dá a ideia mínima do que fazer naquele ponto da interface. Ver [[wiki/concepts/contexto-do-usuario]].

### Ferramenta de contraste: Who Can Use

- **Retoma o linear-gradiente** de [[wiki/concepts/texto-sobre-imagem]] num card do blog que abre o post, para garantir o contraste do texto.
- **[[wiki/entities/who-can-use]]**, link no Notion do curso (seção de tipografia), "aplica diversos testes de problemas visuais que o ser humano pode ter" e diz se o contraste passa na maioria deles.
- **Notas "A, 2A, 3A":** pelo menos um A para tipografia em geral, "mais As" para corpo de texto. Ver tensão abaixo.
- **Título tem outros mecanismos de contraste**: peso tipográfico e tamanho maiores, "que não seja só a cor". Bate com a lista de quatro meios em [[wiki/concepts/contraste]].
- **"Nesse caso aqui, ele só avalia a cor"**, por isso serve mais para corpo de texto. Ver tensão abaixo.
- **Uso:** duas cores (fundo e texto); ele pega a cor de fundo com o conta-gotas, cola o hexadecimal e obtém "nota 3A", passando em todas as simulações.

### Padronização

- **Decisão de design:** a imagem "pega de ponta a ponta, independente da resolução da máquina do usuário", dentro de uma div. Ver [[wiki/concepts/design-responsivo]].
- **Consequência para o designer:** separar um [[wiki/concepts/banco-de-imagens]] em alta resolução que aguente "resoluções pelo menos de 4K para baixo"; do contrário, explicar ao desenvolvedor como a imagem vai se comportar.
- **"Pensar sempre não só na tela que você está projetando, mas também quais são as outras telas."**
- **Todas as imagens no mesmo [[wiki/concepts/aspect-ratio]] e resolução**, padronizadas no Figma, para o desenvolvedor "copiar e colar com as outras imagens e vai funcionar".
- **Sem padronização**, tamanhos diferentes podem não ser problema num caso, mas "em determinadas seções [...] pode ser que prejudique": a thumb do post fica "mais para cima" ou "mais para baixo". Ver [[wiki/concepts/consistencia-visual]].

### Blend modes no Figma

- **Blend modes "pode salvar muito a sua vida"** para não precisar do Photoshop. Ver [[wiki/concepts/blend-modes]].
- **Exercício do banner:** a foto do autor (fundo escuro) sobre um fundo claro tem contraste "muito alto"; para "embutir" a imagem no fundo, aplica blend modes.
- **Primeiro passo: máscara com gradiente radial.** Shape em cima da foto, radial-gradiente, manda para trás, seleciona os dois e aplica máscara; "já conectou bem mais com o fundo".
- **Depois, experimentação:** "isso aqui é literalmente experimentação", muda de aplicação para aplicação.
- **Color dodge** "vai pegar mais ou menos a mesma cor que está ali no fundo e transmitir para a imagem".
- **Overlay, soft light, hard light, difference** também levam em conta o fundo.
- **Gradientes ao redor** (um "linear radial" invertido por cima) terminam a integração.

### Fotos de alto contraste com fundo preto

- **Com color dodge, foto de fundo preto (comum no Unsplash) perde o preto "automaticamente"**, e o resto ganha a cor do fundo.
- **Fundo granulado não fica bom;** prefira fundos mais escuros.
- **"Quanto maior é o contraste da foto, melhor é para você aplicar esses blend modes."**
- **Temperatura de cor importa:** o fogo (laranja, quente) "destoa" no azul com color dodge; com difference "ficou legal".
- **Regra de escolha:** imagens avermelhadas para composição vermelha, mais azuis para temperaturas frias, com bom contraste e "preferencialmente um fundo totalmente preto".

### Os wallpapers do FrontPUSH

- **Receita:** foto de fundo preto do [[wiki/entities/unsplash]] → modo **lighten** → baixar a temperatura para puxar ao azul. O fundo preto some, "como se fosse um PNG".
- **Às vezes mexe em saturação, contraste e exposição**; nessa imagem, só temperatura.
- **Ambientação depois:** outros gradientes, efeito de estrelas. Ver [[wiki/entities/frontpush]].
- **Os que mais usa:** lighten, screen, color dodge, overlay ("muito importante"), difference, darken e multiply.
- **Promete "um estudo um pouco mais aprimorado"** dos modos.

## Entities

- [[wiki/entities/nasser]]: autor ("Násser aqui"); usa a própria foto na demonstração do banner.
- [[wiki/entities/frontpush]]: wallpapers feitos com blend modes; blog com cards e thumbs padronizadas.
- [[wiki/entities/figma]]: máscara, gradientes e blend modes; padronização das imagens.
- [[wiki/entities/who-can-use]] (novo): ferramenta de contraste com simulação de visão.
- [[wiki/entities/unsplash]]: fonte das fotos de fundo preto.
- Sem página própria: Photoshop, Notion.

## Concepts

- [[wiki/concepts/blend-modes]] (novo)
- [[wiki/concepts/imagens-em-interfaces]]
- [[wiki/concepts/contraste]]
- [[wiki/concepts/texto-sobre-imagem]]
- [[wiki/concepts/tipografia]]
- [[wiki/concepts/aspect-ratio]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/banco-de-imagens]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/contexto-do-usuario]]

## Tensões com a wiki

- **"Ele só avalia a cor."** A página do Who Can Use diz o contrário: "The grading uses a combination of color contrast, text size and text weight", e o formulário tem campos de tamanho em px e negrito `[external]` (https://www.whocanuse.com/). O ponto do autor, de que título grande e pesado tem outros meios de contraste, continua de pé; a própria ferramenta já os considera.
- **"Nota A, 2A, 3A."** Em WCAG, contraste de texto só tem critério nos níveis AA (1.4.3, 4.5:1) e AAA (1.4.6, 7:1); não há critério de contraste no nível A `[external]` (https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). A página do Who Can Use mostra notas AA e AAA. "Pelo menos um A" fica impreciso; o piso prático é AA. `[skill: ux-ui-mentor]` AA: 4.5:1 texto normal, 3:1 texto grande; AAA: 7:1 e 4.5:1.
- **Who Can Use x [[wiki/concepts/texto-sobre-imagem|gradiente sobre foto]].** O checker compara duas cores sólidas; sobre foto o fundo varia. Ele mede um ponto com o conta-gotas. `[skill: ux-ui-mentor]` "Sempre teste com texto real, não só com hexadecimais no checker"; meça no pior ponto atrás do texto.
- **Padronização x [[wiki/concepts/aspect-ratio]] (parte 2).** A parte 2 diz não distorcer; esta diz entregar todas as imagens na mesma proporção. São duas faces: preservar a proporção de cada imagem e uniformizar a proporção do conjunto. No código, `[external]` `object-fit: cover` dentro de um container com `aspect-ratio` fixo resolve as duas (https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit).
- **"Tira o fundo preto automaticamente."** Não é remoção de fundo: `[external]` em lighten, screen, color dodge e difference, o preto da camada é neutro (o resultado é a camada de baixo), por isso some (W3C Compositing and Blending, https://www.w3.org/TR/compositing-1/). Só funciona com preto puro; preto "lavado" ou granulado deixa marca, como o próprio autor viu no fundo granulado.
- **Ilustrações ainda não.** A parte 2 dizia que ilustrações viriam a seguir; esta parte é "mais focado em imagens". **Fechado:** a parte 4 ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]]) trata de ilustrações.

## Open Questions

- **Quais as diferenças práticas entre os modos?** O autor promete um estudo "mais aprimorado"; a wiki registra a matemática básica em [[wiki/concepts/blend-modes]] `[external]`.
- **"Linear radial"** (gradiente por cima, "invertendo dessa forma"): não dá para saber pela fala se é linear, radial ou os dois.
- **"Essa cor que está sendo espremida"**: provável "expressa" ou "exprimida"; mantido literal.
- **"Contraste ratio"**: mistura de "contrast ratio" (o rótulo da ferramenta); mantido literal.
- **A partir de quando "talvez não" é problema** padronizar? O autor não dá critério ("em determinadas seções").
- `date_published` vazio.

## Raw Quotes

> "Ela precisa acompanhar o entendimento e aquilo que é passado ao lado dela."

> "Você já tem que pensar sempre não só na tela que você está projetando, mas também quais são as outras telas."

> "Quanto maior é o contraste da foto, melhor é para você aplicar esses blend modes."

> "Só utilizando blend modes dentro do Figma eu utilizei, não precisei utilizar Photoshop."
