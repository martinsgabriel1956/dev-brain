---
type: source
title: "Formas na prática (parte 2): radius, consistência e as decisões nos projetos FrontPUSH, Spider-Man e Creator Push"
aliases: ["aula de formas parte 2", "formas na prática", "radius de 8 pixels", "decisões de formas nos projetos do Násser"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, elementos-da-interface, formas, border-radius, consistencia, harmonia, icones, fotografia, branding]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/formas-exemplos-praticos-radius-consistencia-projetos.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Formas na prática (parte 2): radius, consistência e as decisões nos projetos FrontPUSH, Spider-Man e Creator Push

## TL;DR

Parte 2 da aula de formas de [[wiki/entities/nasser|Násser]]; a parte 1 é [[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]]. Aqui ele mostra três projetos próprios e explica as decisões de forma de cada um. No [[wiki/entities/frontpush]], usa formas geométricas e formas da natureza (elipse, ondas senoidais, céu com estrelas, eclipses e planetas) e escolheu **8 px de [[wiki/concepts/border-radius|radius]]** no botão, depois de testar 4 px: o meio-termo entre racional e amigável, sem perder seriedade. A regra que fica é de [[wiki/concepts/consistencia-visual|consistência]]: escolhido o radius do botão, ele vale para cards, ícones e o resto da interface. O [[wiki/entities/spider-man-projeto-nasser|Spider-Man]] sai do padrão de propósito, com radius de 3–4 px, elementos "deitados" (itálicos), muita transparência e botões e grids chanfrados. O [[wiki/entities/creatorpush|Creator Push]], de proposta "mais baixo nível" que o FrontPUSH, é mais arredondado para ficar mais próximo do usuário. Fecha com dois limites: arquitetura pede formas retas, e fotografia já puxa a interface para o lado orgânico.

## Key Claims

### FrontPUSH: geometria e natureza

- **O FrontPUSH precisa de formas mais geométricas** (retomando a parte 1), e o autor soma a isso formas da natureza: "uma elipse", ondas senoidais, que remetem a matemática e racionalidade. Ver [[wiki/concepts/formas-geometricas-e-organicas]].
- **O céu do site simula estrelas, gradientes do universo, eclipses e planetas.** O autor diz que observa a natureza ao desenhar e tenta replicá-la, porque "sempre tem algo a gente aprender com aquilo que está na natureza". Isso amplia a parte 1: forma da natureza não é só orgânica; ondas senoidais e órbitas também comunicam exatidão.

### Radius de 8 px: o meio-termo

- **Objetivo duplo:** racionalidade e, ao mesmo tempo, algo amigável, próximo do público "nesse primeiro contato".
- **Processo empírico:** reto demais ficaria "mais distante do usuário"; 4 px foi o primeiro teste (o "FrontPUSH antigo era assim"); olhando "de longe", com o azul da marca aplicado, subiu para 8 px e achou "o ponto ideal".
- **Mais que 8 seria "amigável demais"**, e arredondar totalmente também não era a intenção. Proximidade demais "não transmite seriedade"; o lado totalmente racional "não combina muito bem com a interface". Ver [[wiki/concepts/border-radius]].
- **O botão de borda levemente arredondada é "um coringa"** na maioria das vezes, o que torna difícil dar exemplo contrário. A página institucional do [[wiki/entities/nubank]] é citada por ter, até onde ele viu, um botão "assim", aparentemente o totalmente arredondado que ele acabara de descartar (inferência: a fala depende do gesto na tela).

### Consistência: o radius do botão vale para tudo

- **"Se você escolheu 8 como radius do seu botão, você vai aplicar 8-radius no resto da sua interface."** Os cards seguem o mesmo valor, como o card do [[wiki/entities/spider-man-projeto-nasser|Spider-Man]] exibido no próprio FrontPUSH. Ver [[wiki/concepts/consistencia-visual]].
- **Ícones também:** de nada adianta botão arredondado com ícones "totalmente retos"; isso é "uma quebra". Nos ícones do FrontPUSH nenhum é totalmente reto, e até os quadrados têm "bordinhas arredondadas".
- **Cards de depoimentos "chanfradinhos, no mesmo padrão do botão".** O autor diz estar "amarrando a tipografia, o jeito dos cards, as cores, os botões" para conversarem entre si e criar a "ambiência" do que se quer transmitir. É a [[wiki/concepts/harmonia-visual]] da parte 1 aplicada a um valor concreto.

### Spider-Man: fora da caixa, de propósito

- **Projeto do autor com style guide "mais fora da caixa"**, porque é "mais entusiasta" e quer "chamar a atenção mesmo por sair do padrão". O FrontPUSH, ao contrário, "precisa ser um pouquinho mais dentro da caixa". Ver [[wiki/entities/spider-man-projeto-nasser]].
- **Recursos:** traços retos "ainda arredondados", mas menos (3–4 de radius); elementos e quadradinhos "deitados", como itálicos; muita transparência; botões e grids chanfrados.
- **Método:** "eu construo as formas já sabendo mais ou menos o que eu quero comunicar, escolho as características e aplico com consistência". Tudo deve "ser parte de uma mesma família". Ver [[wiki/concepts/porque-das-decisoes-de-design]].

### Creator Push: mais redondo, mais perto

- **O Creator é "mais baixo nível" que o Front** pela proposta de entrega: menos complexo e avançado, embora entregue "muita coisa boa". Por isso o autor arredondou mais para "se aproximar mais do usuário". Ver [[wiki/entities/creatorpush]].
- **Mesma fonte do FrontPUSH, que o autor admite ter mantido "mais por correria"**, mas com elementos, cards e ícones mais arredondados e mais circunferências: "outra bolinha, outra circunferência, poderia muito bem fazer um quadrado". O efeito, diz ele, é inconsciente: a interface fica "um pouco mais amigável". Ver [[wiki/concepts/tipografia]].
- **Reto não afasta sempre.** Num site de arquitetura (ao contratar "um designer de interiores"), tudo arredondado não passaria confiança; ali ele prefere "mais quadradinho". "Depende daquilo que a gente está tratando", que é o [[wiki/concepts/contexto-do-usuario]].

### Fotografia e ilustração

- **O autor prefere ilustração vetorial** ("eu gosto de otimização") a ilustrações mais orgânicas, que não combinariam com esses projetos.
- **Num site de fotógrafo, a fotografia é inevitável e "automaticamente vai elencar a realidade"**: sozinha, já puxa a interface para o lado orgânico. Liga a parte 1 (orgânico = impressão, emoção, realidade) a [[wiki/concepts/imagens-em-interfaces]].
- **Exercício final:** pegar interfaces e perguntar "essa aqui tem qual característica mais", ou pensar nisso antes de construir.

### Contexto: Hotmart

- **O autor evita mostrar interfaces de terceiros** porque foi notificado pela [[wiki/entities/hotmart]]: sem autorização, a aula poderia ser desabilitada. Por isso só mostra projetos próprios e pede que os alunos visitem os sites citados.

## Entities

- [[wiki/entities/nasser]]: autor; "Násser aqui".
- [[wiki/entities/frontpush]]: radius de 8 px, formas da natureza, ícones e cards consistentes.
- [[wiki/entities/spider-man-projeto-nasser]] (novo): projeto do autor fora do padrão.
- [[wiki/entities/creatorpush]] (novo): projeto do autor, mais arredondado; site creatorpush.com.br.
- [[wiki/entities/nubank]]: botão da página institucional citado de passagem.
- [[wiki/entities/hotmart]]: notificação que limita os exemplos da aula.

## Concepts

- [[wiki/concepts/border-radius]] (novo)
- [[wiki/concepts/formas-geometricas-e-organicas]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/harmonia-visual]]
- [[wiki/concepts/tipografia]]
- [[wiki/concepts/imagens-em-interfaces]]
- [[wiki/concepts/contexto-do-usuario]]
- [[wiki/concepts/porque-das-decisoes-de-design]]
- [[wiki/concepts/elementos-da-interface]]

## Tensões com a wiki

- **Formas da natureza como geométricas.** A parte 1 associa natureza a orgânico (feito à mão, fotografia). Aqui, a elipse e as ondas senoidais entram do lado racional, e o céu do site soma eclipses e planetas. Não é contradição: o critério é a regularidade da forma, não a origem. Registrado em [[wiki/concepts/formas-geometricas-e-organicas]].
- **Mesma fonte, mensagem diferente.** A parte 1 trata a tipografia como parte da harmonia; aqui o Creator Push mantém a fonte do FrontPUSH "por correria" e muda a mensagem só com o radius e as formas. Sugere que, na predominância, forma pode pesar mais que fonte, mas é um caso único e o próprio autor admite que não foi decisão de design.
- **"Chanfrado" para radius arredondado.** O autor chama de "chanfradinho" o card arredondado do FrontPUSH e de "chanfrados" os botões do Spider-Man. Em desenho técnico, chanfro é um corte reto no canto, não um arco. Pode ser uso solto da palavra ou corte de canto de fato no Spider-Man; sem a imagem, não dá para saber.
- `[skill: ux-ui-mentor]` O exemplo de multi-brand theming da skill (`--radius-card: 8px` numa marca, `0px` na outra, sobrescritos por `[data-theme]`) é exatamente o caso FrontPUSH × Creator Push: mesmo esqueleto de componentes e mesma fonte, radius diferente por marca. A regra "8 em tudo" vira um token semântico (`--radius-*`) que botões, cards e inputs consomem, em vez de valores fixos espalhados.
- **Ícones do FrontPUSH "mais retos"?** Na aula de ícones ([[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]]), o FrontPUSH tem a família de traço mais "abrupto" e o Creator Push a mais arredondada. Não contradiz "nenhum é totalmente reto": o Feather tem cantos arredondados em todos os ícones; "reto" é relativo à comparação.

## Open Questions

- ~~"Uma eclipse" / "os próprios eclipses"~~ **Resolvido pelo usuário (2026-11-13):** o primeiro é *elipse* (forma geométrica, ao lado das ondas senoidais), corrigido no raw; o segundo é *eclipse* (fenômeno celeste, ao lado de estrelas e planetas), mantido.
- ~~"Na Acer" (2×)~~ **Resolvido pelo usuário (2026-11-13):** é "Násser", o autor falando consigo mesmo como na parte 1 ("qual é a fonte que eu vou escolher, Násser?"). Corrigido no raw.
- ~~"Do próprio Aranha aqui"~~ **Resolvido pelo usuário (2026-11-13):** é o card do projeto Spider-Man dentro da interface do FrontPUSH. Corrigido no raw para "Spider-Man".
- **"Vou falar muito em coreografia nas próximas aulas"**: pode ser *coreografia* no sentido de motion ou erro de ASR para outra palavra (tipografia?). Mantido literal.
- **"Apengando muito para o lado orgânico"**: provável "apelando" ou "pendendo". Mantido literal.
- **O que é o Spider-Man?** Só se sabe que é "um outro projeto meu" com style guide. Não está claro se é estudo, fan site ou cliente.
- **Botão do Nubank:** a fala depende do gesto na tela; "assim" parece ser o totalmente arredondado.
- `date_published` vazio.

## Raw Quotes

> "Se você escolheu 8 como radius do seu botão, você vai aplicar 8-radius no resto da sua interface."

> "Às vezes, quando você está muito próximo, você não transmite seriedade."

> "Eu construo as formas já sabendo mais ou menos o que eu quero comunicar, escolho as características e aplico com consistência ao longo do meu design."

> "Fotografia automaticamente vai elencar a realidade."
