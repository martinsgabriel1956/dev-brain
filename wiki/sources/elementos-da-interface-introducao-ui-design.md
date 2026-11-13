---
type: source
title: "Elementos da interface: introdução (UI Design)"
aliases: ["aula elementos da interface", "introdução elementos da interface", "design de interface melhores práticas"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, elementos-da-interface, feedback, contraste, consistencia, hierarquia-visual, simplicidade, padroes-de-interface, acessibilidade, cultura]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/elementos-da-interface-introducao-ui-design.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Elementos da interface: introdução (UI Design)

## TL;DR

Abertura do módulo "elementos da interface" do curso de UI Design do [[wiki/entities/frontpush|FrontPUSH]], de [[wiki/entities/nasser|Násser]]. Define design de interface como **antecipar o que o usuário vai precisar fazer para facilitar a interação com o produto**. Essa antecipação depende de seis fatores (slide): [[wiki/concepts/objetivo-da-interface|objetivo]], preferências, comportamento, usuário, cultura e posicionamento, reunidos em [[wiki/concepts/contexto-do-usuario]]. Daí saem seis melhores práticas: [[wiki/concepts/simplicidade-visual|simplicidade]], [[wiki/concepts/consistencia-visual|consistência]], [[wiki/concepts/hierarquia-visual|hierarquia]], [[wiki/concepts/contraste|cor e contraste]], [[wiki/concepts/feedback-do-sistema|feedback do sistema]] e [[wiki/concepts/padroes-de-interface|patterns]]. A aula anuncia o roteiro do módulo ([[wiki/concepts/elementos-da-interface]]) e pede que o aluno saiba explicar o porquê de cada detalhe de uma tela ([[wiki/concepts/porque-das-decisoes-de-design]]).

## Key Claims

### O que é design de interface

- **Design de interface antecipa o que o usuário pode precisar fazer para facilitar a interação com o produto digital** (landing page, website, aplicativo). Slide e fala coincidem.
- **A melhor forma "depende".** Para definir a interação, o designer precisa responder a perguntas sobre vários fatores antes de decidir.
- **Os princípios do design norteiam as melhores práticas.** A aula liga o módulo anterior ([[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]]) a este.

### Objetivo

- **Todo produto digital precisa de um objetivo; sem ele não dá para traçar a jornada.** Ver [[wiki/concepts/objetivo-da-interface]].
- **Exemplo: landing page do [[wiki/entities/frontpush]].** Landing page é "página de aterrissagem": a pessoa conhece o produto ou serviço, e o objetivo é apresentá-lo bem para que o interessado deixe um ponto de contato (nome, e-mail, telefone). A página deve responder às dúvidas que o possível cliente tem ao comprar. Mesmo exemplo de [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]].

### Preferências, comportamento, usuário e cultura

- **Classificar o usuário já define comportamento e preferências.** Ver [[wiki/concepts/contexto-do-usuario]].
- **Exemplo: app para idosos.** 14 px e até 16 px seriam pequenos; ele começaria a escala tipográfica em 18 px para cima, a depender da fonte. Também mais [[wiki/concepts/contraste]] na tipografia (cuidado com cinzas próximos do fundo) e um botão de alto contraste para quem tem problema de vista.
  - `[skill: ux-ui-mentor]` A skill traz o mesmo para idosos: texto base de 16 a 18 px com zoom até 200%, contraste alto, alvos de 44 a 48 px, rótulos visíveis, confirmação clara de sucesso. A WCAG pede 4,5:1 para texto normal e 3:1 para texto grande (≥ 18 pt).
- **Menu embaixo num website "fere um pattern".** As pessoas aprenderam que o menu fica à esquerda ou no topo. A razão dada: leitores ocidentais leem da esquerda para a direita, então a esquerda é o primeiro ponto de atenção. Ver [[wiki/concepts/padroes-de-interface]] e [[wiki/concepts/lei-de-jakob]].
  - O exemplo vale para website. Em mobile, a navegação inferior (tab bar) é o padrão nativo de iOS e Android; ver Tensões.
- **Cultura muda o que funciona.** Algo desenhado para o Brasil não necessariamente funciona nos EUA ou no Japão, e a cor pode ter outra leitura em cada país ou na Europa. O autor diz que não chegou a explicar cultura e só cita isso no fim.
- **Posicionamento** aparece no slide, mas não é explicado na fala.

### Melhores práticas

- **Simplicidade: a boa interface passa despercebida "de tão fácil".** Contraexemplo: o app da Caixa, que "complica uma série de coisas" e deixa o autor "extremamente aborrecido". Quando o app é simples, o usuário "meio que não percebe". Ver [[wiki/concepts/simplicidade-visual]].
- **Consistência: escala tipográfica seguida, hierarquia definida, paleta estabelecida e botões que guiam a jornada.** "O botão sempre está ligado à ação que o usuário tem que tomar, link é diferente de botão." Ver [[wiki/concepts/consistencia-visual]] e [[wiki/concepts/affordance]].
  - `[skill: ux-ui-mentor]` Na implementação, botões usam `<button>` e links usam `<a href>`: o botão executa uma ação, o link leva a outro lugar.
- **Hierarquia visual por cor, contraste de cor, forma e tamanho**, retomando o módulo anterior. Ver [[wiki/concepts/hierarquia-visual]].
- **Cor e contraste complementam a hierarquia.** Ver [[wiki/concepts/contraste]].
- **Feedback do sistema: sempre responder ao usuário.** "Deu certo", "o e-mail foi enviado", "deu erro", "você está em tal passo", "só falta isso para concluir"; caixas de diálogo que digam onde ele está, se falta algo ou se há pendência. Ver [[wiki/concepts/feedback-do-sistema]].
- **Patterns: usar os padrões a que o ser humano se acostumou.** Ver [[wiki/concepts/padroes-de-interface]].

### Elementos da interface e roteiro do módulo

- **Os elementos são o meio de atender às melhores práticas:** formas, ilustrações, botões, links, tipografia e cores, ajustados para ficarem "harmônicos" e converterem em boa interação. Ver [[wiki/concepts/elementos-da-interface]].
- **Ordem anunciada:** espaçamentos, linhas e formas (uma aula e pouco, com prática); depois ilustrações, imagens, iconografia, botões e links e elementos de composição. Cores e tipografia são "tão densos" que ganham módulos próprios.
- **Objetivo pedagógico: saber explicar.** O autor usa o próprio slide como exercício: por que esse fundo, essas bolinhas, essa typeface, essa escala, títulos com mais contraste e itens em escala de cinza, e o ícone preenchido maior ao lado da descrição enquanto os outros são menores ("definindo hierarquia"). Ver [[wiki/concepts/porque-das-decisoes-de-design]].
- **Design tem caráter subjetivo** porque depende de muitas variáveis; por isso o módulo é mais teórico, e a prática virá depois.

## Entities

- [[wiki/entities/nasser]]: autor; diz o nome na abertura ("Násser aqui").
- [[wiki/entities/frontpush]]: landing page como exemplo de objetivo.
- Sem página própria: Caixa Econômica Federal (contraexemplo de simplicidade).

## Concepts

- [[wiki/concepts/elementos-da-interface]] (novo)
- [[wiki/concepts/feedback-do-sistema]] (novo)
- [[wiki/concepts/contexto-do-usuario]] (novo)
- [[wiki/concepts/objetivo-da-interface]]
- [[wiki/concepts/simplicidade-visual]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/contraste]]
- [[wiki/concepts/padroes-de-interface]]
- [[wiki/concepts/lei-de-jakob]]
- [[wiki/concepts/affordance]]
- [[wiki/concepts/porque-das-decisoes-de-design]]
- [[wiki/concepts/ui-design]]
- [[wiki/concepts/design-como-interacao]]

## Tensões com a wiki

- **Menu embaixo.** A aula diz que pôr o menu na parte de baixo de um website fere um padrão. O exemplo é de website. Em app mobile, a barra de navegação inferior é o padrão nativo, e a regra de escolha da skill põe o nativo da plataforma em primeiro lugar ([[wiki/concepts/padroes-de-interface]]). A aula não fala de mobile, então não é contradição, mas a regra não deve ser generalizada.
- **Leitura da esquerda para a direita.** A justificativa é cultural, coerente com o próprio fator "cultura" da aula: em idiomas lidos da direita para a esquerda (árabe, hebraico) a interface se espelha. `[skill: ux-ui-mentor]` A skill registra "topo e esquerda têm prioridade em culturas ocidentais".
- **Sem conflito** com [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]]: aquela aula listou simplicidade, consistência e contraste como princípios; esta os repete como melhores práticas e acrescenta feedback do sistema.

- **Outra abertura do mesmo módulo:** [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] também se apresenta como aula introdutória do "segundo módulo". Complementa esta: faz o tour dos elementos e define boa interface por propósito, simplicidade e consistência.

## Open Questions

- "Posicionamento" está no slide mas não foi explicado. Posicionamento de marca no mercado ou posição dos elementos na tela?
- O exemplo de 18 px para idosos não diz a fonte nem a unidade de referência (px de design no Figma ou CSS). A aula ressalva "a depender da fonte".
- Espaçamentos e linhas viraram a aula de espaço em branco, parte 1 ingerida em [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]. Ainda não ingeridas: parte 2 do whitespace, formas, ilustrações, imagens, iconografia, botões e links, elementos de composição; módulos de cores e de tipografia.
- Grid (prometido para outra aula): aparece de forma operacional em [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] (12 colunas de 72, gutter de 32); o tratamento completo foi adiado de novo para a parte de interface web.
- `date_published` vazio.

## Raw Quotes

> "Design de interface se preocupa em antecipar o que os usuários podem precisar fazer para facilitar a interação do produto."

> "Uma boa interface é aquela mais simples possível, é aquela que passa imperceptível para o usuário, de tão fácil que ela é."

> "O botão sempre está ligado à ação que o usuário tem que tomar, link é diferente de botão."

> "Você tem que saber bater o olho nas interfaces e me dizer, explicar o porquê daquilo ali."

## Ver também

- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — a aula de botões e links anunciada aqui (edição "W7")
