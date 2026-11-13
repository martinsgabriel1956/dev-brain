---
type: source
title: "Ícones (edição \"W7\"): comunicação, senso comum, dicas e consistência"
aliases: ["aula teórica de ícones W7", "ícones W7", "ícones universais", "senso comum de ícones"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, elementos-da-interface, icones, iconografia, padroes-de-interface, consistencia, svg, alinhamento, acessibilidade]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/icones-comunicacao-senso-comum-dicas-consistencia.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Ícones (edição "W7"): comunicação, senso comum, dicas e consistência

## TL;DR

Aula teórica (cerca de 7 min) que abre o bloco de [[wiki/concepts/icones-em-interfaces|ícones]] na edição "W7" do curso; a prática fica para a aula seguinte. O ícone ganha bloco próprio, separado de imagens e ilustrações, por ser "um elemento da interface tão importante". Slide em três colunas: **Comunicação** (comunicam algo; pistas visuais; ícones universais; senso comum), **Dicas** (clareza; legibilidade = simples + SVG; alinhamento; personalidade linha x preenchimento) e **Consistência** (famílias: Font Awesome, IcoMoon, Feather, Eva, Basicons; os três últimos gratuitos). (1) A principal característica do ícone é **comunicar um conceito rápido**: são "pistas visuais", e na viagem a Viena o autor se guiou por **ícones universais** em interfaces sem opção de inglês. (2) **Não fugir do senso comum**: engrenagem = configuração (mais forte que chave de boca ou de fenda), carta = e-mail, balão = chat, escudo = segurança, carrinho ou sacola = compras. (3) **Label** quando preciso, inclusive em botões. (4) **Legível** em vários tamanhos: simples e em [[wiki/concepts/formato-svg|SVG]]. (5) **Alinhamento**: ícones de proporções diferentes ficam homogêneos dentro de cards, mas o play desalinhado no card ainda falha ([[wiki/concepts/centralizacao-optica]]). (6) **Personalidade**: preenchido parece mais realista, linha mais simplificada. (7) **[[wiki/concepts/familia-de-icones|Uma família]]**, no máximo duas e "com muita consciência" (uma para funções, outra mais trabalhada para destacar módulos).

## Key Claims

### Por que ícone tem aula própria

- **"Pode até ser"** um tipo de imagem ou ilustração, mas por ser tão importante fica separado, "para poder a gente tratar ele com mais ênfase". Mesmo formato do módulo: aula teórica, depois aula prática.

### Comunicação: pistas visuais e senso comum

- **Todo elemento tem um porquê**: "o UI Design está aí justamente para poder a gente descobrir os porquês". A característica principal do ícone é "comunicar um conceito de forma rápida, é ele ter clareza".
- **"Como se fossem não. De fato, são pistas visuais."**
- **Viena:** manuais e estabelecimentos menores sem inglês; interfaces "que não tinham a opção para mudar a inglês", e ele se guiou "pelos ícones universais". Ver [[wiki/concepts/padroes-de-interface]].
- **Engrenagem = configurações**, "de forma literal, sempre". Duas chaves de boca ou chave de fenda também indicam configuração, mas "a engrenagem é até mais forte".
- **Regra:** "entender o senso comum de ícones e não mudar drasticamente", para atingir a maior quantidade de usuários, "justamente por ter criado um padrão na cabeça do ser humano". Ver [[wiki/concepts/lei-de-jakob]].
- **Tour no [[wiki/entities/feather-icons]]** (plugin, instalação prometida para a aula prática): cartinha = e-mail; pino = localização; balão = chat ou conversa; settings = configuração; escudo = proteção e segurança; carrinho ou sacolinha = carrinho de compras no e-commerce; share = compartilhamento. O smartphone "não sei se é tão universal assim".

### Dicas

- **Clareza:** o ícone precisa transmitir "exatamente a mensagem"; "pode ser necessário ou não" adicionar um label, "uma pequena descrição". Em botões, o ícone ao lado enfatiza a ação (tema da aula de botões e links).
- **Legibilidade:** "toda e qualquer pessoa veja ele de longe, entenda e seja reconhecido em diferentes tamanhos e ambientes". Para isso, simples e em SVG, que não perde resolução. Ver [[wiki/concepts/simplicidade-visual]] e [[wiki/concepts/formato-svg]].
- **Alinhamento:** ícones têm proporções diferentes (uns retangulares, outros cabem num quadrado). "Para poder forçar o alinhamento e a homogeneidade dos ícones, a gente costuma colocá-los dentro de cards". Mas não adianta se o play do card está fora do centro: "sempre se preocupe em ele estar alinhado, centralizado e equilibrado uns com relação aos outros". Ver [[wiki/concepts/centralizacao-optica]] e [[wiki/concepts/grid-de-icones]].
- **Personalidade:** ícones de linha e de preenchimento "transmitem também personalidades diferentes". No Flaticon, os preenchidos "talvez trazem uma noção um pouco mais realista"; os de linha são "mais simplificados".

### Sites de ícones

- **Seção no Notion do curso** com sites para baixar ou se basear. Há pagos e gratuitos: "cabe a você sempre observar isso".
- **Flaticon** ("free vector icons"); **Feather Icons**, "o que eu mais utilizo", gratuito e com plugin no [[wiki/entities/figma]]; **Icons8**, ícones grátis; **Iconfinder**, "esse aqui já é pago".

### Consistência

- **Mesmo princípio de sempre:** como ilustrações "de um mesmo designer", os ícones "têm que parecer estar dentro de uma mesma família". Ver [[wiki/concepts/consistencia-visual]].
- **"Como é que você cura o problema da consistência?"** Uma família de ícones, "só ela na sua interface, no máximo utilize duas, mas com muita consciência": parecidas, ou em categorias diferentes (uma para funções; outra mais complexa, com cores ou mais preenchimento, para destacar módulos). "Mas não utilize mais que isso." Ver [[wiki/concepts/familia-de-icones]].
- **Três packs gratuitos:** [[wiki/entities/feather-icons]], [[wiki/entities/eva-icons]] e Basicons. O slide ainda lista [[wiki/entities/font-awesome]] e IcoMoon, sem comentário falado.

## Entities

- [[wiki/entities/nasser]]: autor (confirmado pelo usuário).
- [[wiki/entities/feather-icons]]: pack que ele mais usa; tour de ícones universais.
- [[wiki/entities/eva-icons]], [[wiki/entities/font-awesome]]: famílias no slide.
- [[wiki/entities/figma]]: plugin do Feather prometido para a aula prática.
- Sem página própria: Flaticon, Icons8, Iconfinder, Basicons, IcoMoon, Notion do curso.

## Concepts

- [[wiki/concepts/icones-em-interfaces]]
- [[wiki/concepts/familia-de-icones]]
- [[wiki/concepts/padroes-de-interface]]
- [[wiki/concepts/lei-de-jakob]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/centralizacao-optica]]
- [[wiki/concepts/grid-de-icones]]
- [[wiki/concepts/formato-svg]]
- [[wiki/concepts/simplicidade-visual]]

## Tensões com a wiki

- **Uma família ou duas?** A parte 1 da outra edição diz para escolher uma e não misturar ([[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]]); aqui o teto é dois, com papéis separados. Não é contradição: a segunda família tem função distinta (destacar módulos), como os ícones maiores e com gradiente dos cards do FrontPUSH em [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]] (inferência).
- **Label "necessário ou não".** `[external]` A NN/g pede rótulo de texto para quase todo ícone, porque universais são raros (https://www.nngroup.com/articles/icon-usability/). A própria lista da aula concorda em parte: o smartphone "não sei se é tão universal". `[skill: ux-ui-mentor]` Sem label visível, o ícone funcional leva `aria-label`; contraste mínimo de 3:1.
- **Card não conserta alinhamento.** O card padroniza a área, mas o conteúdo ainda precisa de [[wiki/concepts/grid-de-icones|grid]] e de [[wiki/concepts/centralizacao-optica|centralização óptica]] (o play da parte 2).
- **"Viena [...] é um país".** Viena é a capital da Áustria `[external]`; deslize falado, mantido literal no raw. Não muda o argumento.
- **"Ícones universais".** Mesmo exemplo de idioma da outra edição (retroprojetor em japonês; Facebook em japonês): funciona para quem já conhece o pattern.

## Open Questions

- **"Deixar com alguns skills"**: mantido literal; provável "estilos" (sombra, fundo do card). A legenda de outra aula "W7" trouxe "skill -that" e "skill-depth".
- **"Mudar a inglês"**: mantido literal; provável "para inglês".
- **"O vector icons"** foi lido como Feather Icons (confiança média): é "o que eu mais utilizo" e "tem um plugin no Figma", como o Feather no início da aula.
- `date_published` vazio.

## Raw Quotes

> "Então, ele funciona como se fossem pistas visuais, como se fossem não. De fato, são pistas visuais."

> "Então, é legal a gente sempre entender o senso comum de ícones e não mudar drasticamente."

> "Utilize uma família de ícones e utilize só ela na sua interface, no máximo utilize duas, mas com muita consciência."

## Ver também

- [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]] — a aula teórica de ícones da outra edição: objeto, ação, ideia; Material Design; Iconly x Feather
- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — o play e a centralização óptica; grid; SVG escala
- [[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]] — aula "W7" anterior: ícone de app vetorizado à mão
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — a aula prática desta edição: plugins, ícones próprios, ícone em círculo, constraints
