---
type: source
title: "Elementos de composição (edição \"W7\"): na prática no Figma (órbitas, pontilhado, planetas, cometas e PlayStation)"
aliases: ["elementos de composição W7", "aula prática de elementos de composição", "órbitas no Figma", "pontilhado no Figma", "cometas no Figma"]
date_created: 2026-11-14
date_updated: 2026-11-14
source_count: 0
tags: [ui, ui-design, design, elementos-da-interface, elementos-de-composicao, background, branding, figma, stroke, pontilhado, sombra, gradiente, simplicidade, consistencia]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/elementos-de-composicao-pratica-figma-orbitas-pontilhado-cometas-playstation.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-14
---

# Elementos de composição (edição "W7"): na prática no Figma

## TL;DR

Aula curta (cerca de 8 min) da edição "W7" do curso de UI de [[wiki/entities/nasser|Násser]] (autoria inferida) sobre [[wiki/concepts/elementos-de-composicao]]. Enquanto a versão da edição FrontPUSH ([[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]]) é teórica e cheia de exemplos de projetos, esta é **"um pouquinho mais prática"**: ele monta no [[wiki/entities/figma]] o fundo que aparece no próprio slide da aula. O slide lista cinco funções: **apoio na composição de telas, refino no design, background, branding e consistência**. Elemento de composição é "um perfume na sua interface", "a cerejinha do bolo". A receita: formas só com stroke (3 px, sem preenchimento), elipses concêntricas com **pontilhado 2, 10** e cap round para fazer órbitas, um **planetinha** na cor de contraste com sombra da própria cor (blur "o dobro", 30%, spread negativo), e **cometas** feitos de uma linha com gradiente a 45° e uma elipse de 6 px na ponta. Exemplos: o branding de "boost" e foguete do [[wiki/entities/frontpush]], os botões do controle no projeto de [[wiki/entities/playstation|PlayStation]] e o "Confetti Kit" achado num design system. A regra que fecha: **tem que ser simples**, "não pode tirar a atenção do usuário"; e manter a [[wiki/concepts/consistencia-visual|consistência]].

## Key Claims

### Para que serve

- **"É como se fosse um perfume na sua interface"**, "talvez, de artifício", mas "dá uma cerejinha do bolo". As funções batem com o slide: apoiar a composição das telas, refinar o design, compor o background, reforçar o branding. Ver [[wiki/concepts/elementos-de-composicao]].
- **Branding = "a ideia que eu quero passar, a sensação que eu quero transmitir."** No [[wiki/entities/frontpush]] a ideia é "boost", "um empurrão na sua carreira", "impulsionar"; daí o foguete, e daí órbitas e planetas como elementos de composição. Ver [[wiki/concepts/harmonia-visual]].
- **Formas geométricas reforçam "a precisão, a exatidão que eu quero passar"**, mesma associação da aula de formas. Ver [[wiki/concepts/formas-geometricas-e-organicas]].

### Na prática: stroke e pontilhado

- **Frame preto** (a "cor preta normal" que ele sempre usa), um retângulo com borda arredondada **só com stroke 3** e sem preenchimento ("stroke é delinear"). Partes quadradas atrás do texto "já dá um outro quê".
- **Elipses com cap round e pontilhado "2, 10"**: "2 é o tamanho do pontilhado e 10 é o espaçamento". 5, 10 "também fica legal". Rotacionar dá variação.
- **Órbitas concêntricas:** várias elipses criadas segurando Shift, para "crescer de forma regular".

### Planetinha com sombra

- **Cor:** "a cor de contraste do branding" (no slide, o laranja do logo "W7"). Ver [[wiki/concepts/contraste]].
- **Sombra da mesma cor:** pega a cor com o conta-gotas, opacidade 30% (70% "está muito"), "blur sempre o dobro", spread negativo (testa −12 e −8, fica com −4). "Aplicando aquela mesma técnica": a sombra da cor do elemento já vista na aula de botões ([[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]). Copia e cola para espalhar os planetas.

### PlayStation e design systems

- **Projeto PlayStation:** podia ter só o controle do PS5 (desenhado no Figma), mas pôs atrás os botões do PlayStation e uma linha "onde eu posso animar ela depois", de tamanhos diferentes, rodeando, o que dá "sensação de maior movimento". Ver [[wiki/entities/playstation]].
- **Depende do branding:** se é colorido e vibrante, cabe esse tipo de elemento.
- **Ideias vêm de design systems** "desses caras grandes". Ele mostra o "Confetti Kit": colorido, transmite "algo mais vibrante, algo mais animado, algo mais alegre".

### Cometas e simplicidade

- **Cometa:** linha com gradiente na direção de 45°, stroke com cap round "para a bordinha ficar redondinha", e uma elipse bem pequena (6) na ponta. Vale "o gradiente, ou a bolinha mesmo".
- **"Tem que ser simples para poder formar o background, não pode tirar a atenção do usuário"**: "é simplesmente para compor um cenário". Ver [[wiki/concepts/simplicidade-visual]] e [[wiki/concepts/hierarquia-visual]].
- **Tipologia de universo ou de confete**: "depende de tudo que você quer transmitir".
- **Consistência:** "sempre a querida consistência no princípio de design ajudando a gente". Ver [[wiki/concepts/consistencia-visual]].

## Entities

- [[wiki/entities/nasser]]: autor (inferido; o nome não é dito).
- [[wiki/entities/frontpush]]: "meu site do FrontPUSH", branding de boost, foguete e órbitas.
- [[wiki/entities/playstation]]: projeto com o controle do PS5 e os botões como fundo.
- [[wiki/entities/figma]]: onde a prática acontece (stroke, dash, conta-gotas, drop shadow, gradiente).
- [[wiki/entities/rocketseat]]: não citada aqui; o foguete do FrontPUSH ecoa o exemplo da outra edição.
- Sem página própria: "Confetti Kit", "DUI".

## Concepts

- [[wiki/concepts/elementos-de-composicao]]
- [[wiki/concepts/elementos-da-interface]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/simplicidade-visual]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/contraste]]
- [[wiki/concepts/harmonia-visual]]
- [[wiki/concepts/formas-geometricas-e-organicas]]

## Tensões com a wiki

- **Duas edições, dois temas para o FrontPUSH.** Na edição FrontPUSH o fundo simula um **eclipse** (universo); aqui o branding é **boost** e o símbolo é o **foguete**, com órbitas e planetas. Não se contradizem (os dois são "universo"), mas a justificativa muda: lá é cenário de eclipse, aqui é metáfora de impulso. E o foguete era o exemplo de branding da [[wiki/entities/rocketseat]] na outra aula.
- **Pontilhado no código.** `[external]` O "2, 10" do Figma vira `stroke-dasharray="2 10"` com `stroke-linecap="round"` num SVG; com cap round, cada traço ganha meia espessura em cada ponta, então com stroke 3 e dash 2 os pontos ficam levemente alongados; dash 0 dá círculos perfeitos (https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke-dasharray).
- **Sombra colorida no escuro.** `[skill: ux-ui-mentor]` em dark mode sombras pretas somem e o design system troca por borda sutil; aqui a sombra é da cor do planeta, então funciona como brilho (glow), não como elevação. Faz sentido para elemento decorativo, não como token de elevação.
- **Linha animada.** A linha do PlayStation "posso animar depois". `[skill: ux-ui-mentor]` animação decorativa em loop pede `prefers-reduced-motion` e não deve competir com o conteúdo; a aula não fala disso.
- **Decorativo no HTML.** `[skill: ux-ui-mentor]` órbitas e cometas são decoração: `background-image` ou SVG com `aria-hidden="true"`. Ver [[wiki/concepts/elementos-de-composicao]].

## Open Questions

- **"Branding do DUI"**: não identificado. Pode ser erro de ASR (da UI? do W7?). No slide a cor de contraste é o laranja do logo "W7". Mantido literal.
- **"Confetti Kit"**: a legenda diz "confeti kit"; não identificado qual design system mostra esse kit ("ele tem essa ideia aqui na introdução").
- **"Blur sempre o dobro"**: o dobro de quê não é dito (provavelmente do deslocamento Y). O offset não aparece na fala.
- **"Vários shift"**: lido como "segurar Shift ao redimensionar"; mantido literal.
- **Autoria inferida** (Násser): logo "W7" no slide, "meu site do FrontPUSH", continuidade com as outras aulas "W7". O nome não é dito.
- `date_published` vazio.

## Raw Quotes

> "É como se fosse um perfume na sua interface, mas eu sempre gosto de usar e acredito que dá uma cerejinha do bolo."

> "2 é o tamanho do pontilhado e 10 é o espaçamento entre os pontilhados."

> "Esse tipo de coisa tem que ser simples para poder formar o background, não pode tirar a atenção do usuário."

> "Sempre a querida consistência no princípio de design ajudando a gente."
