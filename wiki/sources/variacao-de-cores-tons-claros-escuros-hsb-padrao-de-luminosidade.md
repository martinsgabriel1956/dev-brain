---
type: source
title: "Variação de cores: tons mais claros e mais escuros, HSB e padrão de luminosidade"
aliases: ["aula de variação de cores", "variação de cores W7", "tons mais claros e mais escuros", "padrão de luminosidade"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, cor, paleta, hsb, saturacao, brilho, matiz, luminosidade, contraste, acessibilidade, regra-60-30-10, sombra]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-15
---

# Variação de cores: tons mais claros e mais escuros, HSB e padrão de luminosidade

## TL;DR

Última aula teórica do bloco de cores (cerca de 19 min), antes da prática no [[wiki/entities/figma]]. A pergunta: como conseguir **tons mais claros e mais escuros** da paleta sem perder a harmonia. Para que serve: **mudança de estado** (hover mais escuro ou mais claro), hierarquia, paletas monocromáticas com contraste, e fundos, ilustrações e neutros "com um pingo" da cor de base, como o preto azulado do Facebook ([[wiki/entities/meta]]). A regra, tirada da natureza e conferida com o ColorZilla em fotos do [[wiki/entities/unsplash]]: em HSB, **tom mais claro = mais brilho e menos saturação; tom mais escuro = menos brilho e mais saturação**. Mexer só no brilho funciona, mas fica pior. O segundo eixo é o **[[wiki/concepts/padrao-de-luminosidade|padrão de luminosidade]]**: cada matiz tem um brilho próprio (amarelo 89%, ciano 70%, verde 60%, rosa 41%, vermelho cerca de 30%, azul 11% no slide). Isso explica por que branco sobre amarelo não se lê, por que o azul é o queridinho dos fundos, e como girar o Hue quando o brilho já está no máximo (ele mesmo "não indica" esse recurso). Fecha com a [[wiki/concepts/regra-60-30-10]], o conselho de evitar branco e preto puros e sombras pretas, uma ferramenta geradora de variações (nome não dito) e o [[wiki/entities/who-can-use]]: verde claro com texto branco reprova, com preto tira AAA (10.50:1). "Não basta que ela seja bonita, ela precisa ser acessível."

## Key Claims

### Não é regra

- Ele repete o aviso das aulas anteriores: "não leve ao pé da letra [...] que isso aqui que eu estou pregando é uma regra". Há sites "que saem dessa caixinha": base em duas cores (triádica) ou gradiente que não é nem primária nem secundária.
- **Stripe** como exceção: a base "talvez seja o azul, mas só que é um azul em gradiente". "Cabe a nós aceitar isso." Ver [[wiki/entities/stripe]].

### Para que variar

- **Onde aplicar cada cor** vem primeiro: a base em 60%, depois 30%, depois 10%, "aquela regrinha que a gente viu da arquitetura". Ver [[wiki/concepts/regra-60-30-10]].
- **Cor de enfoque (destaque)** em botões, títulos e banners, onde se quer a atenção, porque contrasta com a base. A interface dele "é toda preta" e o destaque é o laranja: "meio que o seu olho puxa". Junto com o princípio de deixar espaço em branco "para poder o seu olho ter foco". Ver [[wiki/concepts/hierarquia-visual]], [[wiki/concepts/contraste]] e [[wiki/concepts/espaco-em-branco]].
- **Mudança de estado:** "quando eu passo um efeito hover em um botão, eu quero que ele mude a cor dele, ele vai ficar ou mais escuro ou mais claro", mantendo "a harmonização do meu site". Ver [[wiki/concepts/feedback-do-sistema]].
- **Paleta monocromática:** a variação precisa ser "harmônica" e criar "um bom contraste do claro e do escuro".
- **Fundos, ilustrações e neutros:** variação "no mesmo matiz" harmoniza o ambiente. No Facebook, o preto "não é um preto totalmente sem saturação, ele tem um pingo de azul", e o branco também. Ver [[wiki/concepts/harmonia-visual]] e [[wiki/entities/meta]].

### A regra de variação no HSB

- **Inspiração na natureza**, tema da abertura do módulo. Com o plugin ColorZilla (pega o hexadecimal no meio de uma cruz), ele mede variações de uma mesma cor numa foto do Unsplash.
- **Tons mais claros:** "geralmente eles apresentam uma saturação menor e um brilho maior". **Tons mais escuros:** "você diminui o brilho e aumenta a saturação". O brilho é intuitivo; "o que você não pegou ainda é que é inverso da saturação". "É lógico que existem exceções talvez [...] mas pelo menos a grande maioria." Ver [[wiki/concepts/variacao-de-cores]].
- **O erro dele:** "eu simplesmente aumentava o brilho sem diminuir a saturação. A variação acontece? Acontece, só que vocês vão verificar a diferença" (demonstração prometida para a aula prática no Figma).
- **Slide:** "Tons mais claros: H: luminosidade das cores, S: diminuir saturação, B: aumentar o brilho, variação diagonal"; "Tons mais escuros: H: luminosidade das cores, S: aumentar saturação, B: diminuir o brilho, variação diagonal". As duas escalas de laranja (cinco passos cada) ilustram.

### Padrão de luminosidade

- **Demonstração:** uma barra com gradiente linear passando por vermelho, laranja, amarelo, verde, ciano, azul, roxo, rosa e de volta ao vermelho ("um ciclo cromático só que disposto em barra"). No tipo de layer, de pass-through para **luminosity**, a barra vira escala de cinza. Ver [[wiki/concepts/blend-modes]] e [[wiki/concepts/padrao-de-luminosidade]].
- **Valores "de maneira aproximada":** vermelho "aproximadamente 30%", amarelo 89% ("a parte mais clara de todo o espectro"), verde 60%, ciano 70%, rosa 41%. O azul (11%) está só no slide.
- **Amarelo:** explica "porque o contraste fica tão ruim, mas tão ruim do branco com o amarelo"; ele cita "bad UIs" de branco com amarelo.
- **Na própria marca:** branco sobre laranja ele "consegue até ler dependendo do tamanho da tipografia e do peso"; sobre amarelo não. Por isso o texto ao lado do logo ficou em preto ("ao invés de colocar script FE na frente do logo [...] como eu fiz aqui no script WD"). O ciano tem o mesmo problema.
- **Azul:** "um dos mais queridos do pessoal dos designs" porque "ele próprio já é escuro": ótimo para background com o maior contraste.
- **Girar o Hue:** se o brilho já está em 100 e se quer um tom mais claro, dá para mover a matiz na direção dos matizes mais luminosos (ou, para escurecer o amarelo, na direção dos mais escuros), "de forma sutil". "Só que eu não indico essa parte [...] se você aplicar simplesmente essa regrinha aqui sem mudar a matiz, já é sucesso."

### Materiais de apoio

- **Artigo "como usar as cores em um UI design":** regra 60-30-10 ("da arquitetura, design de interiores"): 60% dominante, 30% secundária, 10% destaque. Daí vem a relação primária/secundária; a cor de enfoque pode compor a primeira cor ou servir de complementar. "Evitar utilizar o branco puro ou preto puro, porque são cores que não existem na natureza, então passam um ar de artificialidade."
- **Outro artigo ("dark variation", análise em HSB):** "não é legal utilizar preto nas sombras", porque a sombra sobre um fundo colorido "vai ser essa mesma cor em uma versão mais dark".
- **[[wiki/entities/dribbble]]:** fica para a aula sobre onde buscar inspiração.

### Ferramentas

- **Gerador de variações ("o grande carro-chefe", nome não dito):** recebe a cor (o "verdinho do meu branding") e devolve a escala pronta. Ele deixa "4 e 4" (claros e escuros), ou "3, 2 ou menos possível", porque "quando a gente vai passar para o CSS dá muito trabalho se tiver muitas variações". A "angulação" gira a matiz pelo círculo cromático; ele mantém perto de 0, também na parte light. Link prometido na descrição do vídeo.
- **Ferramenta de contraste** (citada "bastante em tipografia"; pela descrição, o [[wiki/entities/who-can-use]]): simula problemas de visão e dá uma nota. Com o verde claro dele ("5F36A") e texto branco, "deu fail"; com preto, "uma nota AAA [...] contrast ratio de 10.50 para 1". "Não basta que ela seja bonita, ela precisa ser acessível." Ver [[wiki/concepts/contraste]].

## Entities

- [[wiki/entities/nasser]]: autor inferido. O nome aparece só nas perguntas retóricas ("Ah, Násser, para quê?"), padrão das outras aulas dele; slide com logo "W7" e "verdinho do meu branding".
- [[wiki/entities/meta]]: Facebook, preto com "um pingo de azul".
- [[wiki/entities/unsplash]]: fotos usadas para medir variações naturais.
- [[wiki/entities/stripe]]: base em gradiente azul, exceção às regras.
- [[wiki/entities/who-can-use]]: ferramenta de contraste (identificação inferida).
- [[wiki/entities/dribbble]]: anunciado para a aula de inspirações.
- [[wiki/entities/figma]]: prática prometida; modo luminosity no tipo de layer.
- Sem página própria: ColorZilla, "ScriptWD"/"script FE" (marcas dele?), "NY", o gerador de variações.

## Concepts

- [[wiki/concepts/variacao-de-cores]] (novo)
- [[wiki/concepts/padrao-de-luminosidade]] (novo)
- [[wiki/concepts/regra-60-30-10]] (novo)
- [[wiki/concepts/contraste]]
- [[wiki/concepts/harmonia-visual]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/feedback-do-sistema]]
- [[wiki/concepts/espaco-em-branco]]
- [[wiki/concepts/blend-modes]]

## Tensões com a wiki

- **Os números do slide são luma Rec. 601.** `[external]` 31/89/60/70/11/41 batem com Y' = 0,299 R + 0,587 G + 0,114 B para vermelho, amarelo, verde, ciano, azul e magenta puros (30%, 89%, 59%, 70%, 11%, 41%), a fórmula de luminosidade dos editores (https://www.w3.org/TR/AERT/#color-contrast). O "padrão" não foi descoberto estudando a natureza: é a sensibilidade do olho por canal, já codificada. Para contraste WCAG vale outra conta, a luminância relativa linear (0,2126 / 0,7152 / 0,0722), em que o amarelo puro dá 93% e o azul 7% (https://www.w3.org/TR/WCAG22/#dfn-relative-luminance). A ordem dos matizes é a mesma.
- **"Mais claro = menos saturação" é quase tautologia no HSB.** `[external]` Misturar uma cor com branco (tint) baixa S e sobe B por definição; misturar com preto (shade) baixa B e mantém S. Então "escurecer aumentando a saturação" é uma escolha estética, para o escuro não ficar "sujo". A mesma receita aparece em guias de cor para UI (Refactoring UI; Erik Kennedy, "Color in UI Design: A (Practical) Framework"), que também sugerem girar a matiz. É provável que o "artigo do HSB" citado seja o de Kennedy (inferência, não conferida).
- **"Eu não indico" girar o Hue** contra a skill. `[skill: ux-ui-mentor]` A skill recomenda HSL ou, melhor, **OKLCH**, que é perceptualmente uniforme: "em HSL, azul e amarelo com o mesmo L parecem ter brilhos diferentes. Em OKLCH, não." É o padrão de luminosidade resolvido no espaço de cor, sem girar matiz na mão.
- **"Regular vision"** descrita como quem "não consegue distinguir as três cores primárias". No Who Can Use, "Regular Vision (Trichromatic)" é a visão típica; quem distingue mal são as variações de daltonismo (ver [[wiki/entities/who-can-use]]).
- **"4 e 4" por "dar muito trabalho no CSS".** `[skill: ux-ui-mentor]` A skill separa primitivos (escala 50–950) de tokens semânticos; o componente só usa o semântico, então o tamanho da escala não pesa no CSS. Poucos passos também funcionam, desde que hover, borda e fundo sutil tenham onde cair.
- **Branco e preto puros "não existem na natureza".** `[skill: ux-ui-mentor]` Bate com "não usar preto puro em dark mode — #111 ou #0F172A". Combina com o próprio exemplo do Facebook (neutros tingidos) e com a lição de sombra colorida da aula de botões ([[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]).
- **"Preto e branco não são cores, são extremos de luz"** ([[wiki/concepts/contraste]], aula de ícones) e "evitar preto puro" aqui convivem: lá o assunto é neutralidade do ícone, aqui o acabamento da paleta.

## Open Questions

- **Qual é o gerador de variações?** Tem "angulação" (rotação de matiz), controle "light" e número de passos claros/escuros. Link só na descrição do vídeo.
- **"5F36A"** tem cinco dígitos; o hexadecimal real do verde dele não foi recuperado.
- **"ScriptWD", "script WD", "script FE"** e **"NY"**: mantidos literais. O logo "W7" do slide pode ser o "WD" estilizado (inferência). Os nomes não aparecem em outras páginas da wiki.
- **"Variações mais pendadas"**, **"a gente está indo a luminosidade"**, **"como a avaliação [...] nas interfaces"** (talvez "variação"), **"código hexagonal"**: mantidos literais.
- **Aula anterior** (teoria de cores, inspiração na natureza, 60-30-10 "da arquitetura") ainda não ingerida; esta aula se apoia nela.
- **Lacuna de ~6 s** na legenda (11:55 → 12:01), na passagem para o Stripe.
- Autoria inferida; `date_published` vazio.

## Raw Quotes

> "Quando você quer tons mais claros na natureza, você vai perceber que aumenta o brilho e diminui a saturação, enquanto quando você quer tons mais escuros, você diminui o brilho e aumenta a saturação."

> "Então o amarelo por si só já carrega mais brilho, 89%. Então isso explica porque o contraste fica tão ruim, mas tão ruim do branco com o amarelo."

> "Então não basta que ela seja bonita, ela precisa ser acessível, certo?"

## Ver também

- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — fundo do botão na cor de contraste; sombra de hover na cor do botão
- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — primeira aparição do Who Can Use; blend modes no Figma
- [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]] — cor de destaque escassa sobre fundo preto
