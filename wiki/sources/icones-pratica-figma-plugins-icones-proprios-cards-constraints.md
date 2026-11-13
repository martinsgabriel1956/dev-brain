---
type: source
title: "Ícones na prática no Figma (edição \"W7\"): plugins, ícones próprios, cards e constraints"
aliases: ["aula prática de ícones W7", "ícones na prática W7", "ícones dentro de cards", "plugins de ícones no Figma"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, figma, icones, iconografia, familia-de-icones, consistencia, constraints, svg, cards]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/icones-pratica-figma-plugins-icones-proprios-cards-constraints.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Ícones na prática no Figma (edição "W7"): plugins, ícones próprios, cards e constraints

## TL;DR

Aula prática (cerca de 12 min) que fecha o bloco de [[wiki/concepts/icones-em-interfaces|ícones]] da edição "W7", depois da [[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia|aula teórica]]. Quatro partes: (1) **plugins** da comunidade do [[wiki/entities/figma]]: [[wiki/entities/feather-icons]] ("o queridinho", exporta SVG), Bootstrap Icons, Material Design Icons, Iconify e "icons-code"; a instalação detalhada fica para uma aula bônus. (2) **Arquivo do Piqo** ([[wiki/entities/iconly]], inferido) duplicado da comunidade, com os estilos bold, bulk, light, light outline, broken e two-tone; ele usou esses ícones nos destaques do Instagram. (3) **Ícones próprios** nos módulos do site dele: computador + smartphone para "interface web responsiva", paleta para cores, átomo para React, colunas mescladas para grid x Flexbox, presente para bônus. Laranja = curso de UI Design. É a segunda [[wiki/concepts/familia-de-icones|família]], com o Feather para os ícones pequenos. (4) **Ícone dentro de estrutura regular** (círculo, card ou quadrado) para equilibrar ícones de proporções diferentes. Na demo, a medalha do Feather vai dentro de dois círculos (cor da marca a 50% e 90% com gradiente), com stroke branco. Para o ícone não deformar quando o frame estica, ele explica as [[wiki/concepts/constraints-no-figma|constraints]] (top/left, center).

## Key Claims

### Plugins e arquivos da comunidade

- **Caminho:** ícone do Figma → comunidade → buscar "icons". Aparece "uma porrada de arquivos de criadores", que servem "de inspiração para você criar os seus próprios ícones".
- **Plugins citados:** Feather Icons ("o que eu mais utilizo"), Bootstrap Icons ("muito legal, vou até instalar aqui"), Material Design Icons, Iconify ("muito utilizado") e "icons-code" (não identificado). Ver [[wiki/entities/feather-icons]] e [[wiki/entities/material-design]].
- **Uma regra no meio da demo:** "se for usar ícones de linhas, utilize só ícones de linhas; vai utilizar ícones com preenchimento, utilize só ícones com preenchimento". Ver [[wiki/concepts/familia-de-icones]].
- **Feather:** "tem a opção de exportar para SVG, então sempre isso é muito bom"; "o queridinho, queridinho, meu queridinho". Ver [[wiki/concepts/formato-svg]].
- **Piqo:** arquivo "muito bem acabado" para duplicar e consultar a "icon library". Estilos: bold; bulk ("preenchimento só com duas cores"); light ("ícone de linhas"); light outline ("a linha agora para fora"); broken ("ícones de linhas só que quebrados"); two-tone. Ver [[wiki/entities/iconly]].

### Duas famílias: uma trabalhada, uma simples

- **Ícones próprios** como "exercício de consistência visual" e "para criar algo literalmente que faça mais sentido". A seção de style guide terá uma parte só para isso. Ver [[wiki/concepts/consistencia-visual]].
- **Divisão:** "uma família um pouco mais trabalhada para poder indicar módulos ou partes mais importantes do nosso site" e "outros de forma mais simples", com o Feather Icons. "Eu utilizo apenas duas famílias." É a mesma regra da aula teórica.
- **Cada ícone diz o que o módulo trata:** interface web = computador + smartphone (responsivo, desktop e mobile); identidade visual, UX, cores = "uma paletinha aqui abrindo"; React = átomo; Flexbox e grid = colunas mescladas, porque mesclar colunas "é mais difícil com o Flexbox", que exige "um Flex dentro do outro"; propriedade do SVG = caixinha; animações = estrelinha com "efeito over" atrás ("indica que é movimento"); biblioteca, js, exemplos = quadradinhos; bônus = presente. "O ícone que eu desenhei já comunica o que vai ser tratado naquele módulo."
- **Cor como código entre cursos:** preenchimento laranja porque "tudo que é laranja está remetendo ao curso de UI Design"; "uma seleção que o seu cérebro faz até pela cor". Ver [[wiki/concepts/cor-semantica]].
- **Falha admitida:** o ícone do Sass no site "não é dessa forma aqui", e ele não sabe "por que deu errado".

### Ícone dentro de estrutura regular

- **Por quê:** "existem ícones que são mais retangulares, [...] mais deitados, são em pé"; dentro de cards ou "bolinhas" há "um equilíbrio maior". "Você dá um tchan na sua interface quando você engloba os ícones em estruturas regulares, seja um círculo, seja um card, seja um quadrado." Ver [[wiki/concepts/centralizacao-optica]].
- **Receita do círculo:** círculo maior; Ctrl D; cor de branding laranja, desconectada do estilo "para eu poder mexer na cor"; opacidade de 30%, depois 50%; círculo interno com Shift, a 90%, na cor de branding "normal com um gradiente". Medalha do Feather no centro, Ctrl G, stroke branco.
- **Mesma escala:** com o segundo ícone (Bluetooth), "certifique-se que você está aumentando ele na mesma proporção que você aumentou o ícone passado". Ver [[wiki/concepts/grid-de-icones]].
- **Casos reais:** "como eu fiz no curso do FrontPUSH", em cards; "um spoiler [...] da aula de style guide". Ver [[wiki/entities/frontpush]].

### Constraints

- **O ícone do plugin chega como frame** com os vetores separados. Dentro de outro frame (um "artboard"), "como as constraints dele não estão habilitadas, a escala fica presa ao tamanho do frame": esticar o frame deforma o ícone.
- **Correção:** "fique fixo na distância acima e na esquerda" (top e left); ou centralizado, e ele "vai ficar sempre centralizado". "Depende do que você quer fazer." Ver [[wiki/concepts/constraints-no-figma]].

## Entities

- [[wiki/entities/nasser]]: autor (confirmado pelo usuário).
- [[wiki/entities/feather-icons]]: plugin preferido; família simples ao lado dos ícones próprios.
- [[wiki/entities/iconly]]: arquivo do "Piqo" (inferido) com estilos bold, bulk, light, light outline, broken e two-tone.
- [[wiki/entities/material-design]]: plugin Material Design Icons.
- [[wiki/entities/twitter-bootstrap]]: plugin Bootstrap Icons.
- [[wiki/entities/figma]]: comunidade, plugins, Ctrl D, Ctrl G, constraints.
- [[wiki/entities/frontpush]]: ícones em cards como exemplo.
- Sem página própria: Iconify, "icons-code", Sass, React, Instagram.

## Concepts

- [[wiki/concepts/icones-em-interfaces]]
- [[wiki/concepts/familia-de-icones]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/constraints-no-figma]] (novo)
- [[wiki/concepts/centralizacao-optica]]
- [[wiki/concepts/grid-de-icones]]
- [[wiki/concepts/formato-svg]]
- [[wiki/concepts/cor-semantica]]

## Tensões com a wiki

- **Iconify como plugin "muito utilizado".** Em [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]], misturar Feather com Iconify é o exemplo de quebra de consistência. Não é contradição: o Iconify agrega muitos packs open source `[external]`, então o risco está em misturar, não no plugin (inferência).
- **"Constraints não habilitadas".** `[external]` A central do Figma diz que o padrão é Top e Left (https://help.figma.com/hc/en-us/articles/360039957734). O ícone esticou junto, então provavelmente o frame do plugin veio com Scale, ou o "artboard" foi criado em volta do ícone (inferência; a aula não mostra o painel).
- **"Fixo à esquerda e à direita".** Logo depois de pedir "acima e na esquerda", ele diz "esquerda e direita"; em seguida aplica "left e top". Lapso falado; no Figma, Left & Right estica o objeto junto com o frame `[external]`.
- **Cor desconectada do estilo.** Desconectar a cor de branding para mudar a opacidade cria um valor solto. `[skill: ux-ui-mentor]` Num design system, isso pede um token de opacidade ou de cor derivada, senão a marca diverge na manutenção. Ele mesmo promete tratar estilos na parte de interface web.
- **Ícone branco sobre laranja.** `[skill: ux-ui-mentor]` Ícone informativo pede contraste mínimo de 3:1 com o fundo. Branco sobre laranja de marca costuma ficar perto do limite; é preciso conferir no pior ponto do gradiente.
- **O círculo e o card padronizam a área**, mas não a massa visual. Ícones de proporções diferentes ainda pedem [[wiki/concepts/grid-de-icones|grid]] e [[wiki/concepts/centralizacao-optica|centralização óptica]] (mesma ressalva da aula teórica).

## Open Questions

- **"Piqo"** (legenda "pico", 2×): lido como Piqo Design, autor do Iconly, porque os estilos batem e a wiki já liga Násser ao Iconly. Confiança média; a busca não confirmou a autoria.
- **"Pattern icons"** (2×) foi lido como Feather Icons (confiança média): "que eu utilizo" e família simples, como o "vector icons" da aula teórica.
- **"icons-code"**: plugin não identificado; mantido literal.
- **"Frame do words"**, "efeito over" (hover? blur?), "você não entende nada que você disse" (provável "vocês não entenderam nada do que eu disse") e "biblioteca, js": mantidos literais.
- **Aula bônus de plugins** e **aula de style guide** prometidas; ainda não ingeridas.
- `date_published` vazio.

## Raw Quotes

> "Se for usar ícones de linhas, utilize só ícones de linhas; vai utilizar ícones com preenchimento, utilize só ícones com preenchimento."

> "Então meio que o ícone que eu desenhei já comunica o que vai ser tratado naquele módulo."

> "Então você dá um tchan na sua interface quando você engloba os ícones em estruturas regulares, seja um círculo, seja um card, seja um quadrado."

## Ver também

- [[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]] — a aula teórica desta edição: senso comum, dicas, no máximo duas famílias
- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — constraints e componente na outra edição; grid 20×20
- [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]] — os ícones próprios do FrontPUSH em cards
