---
type: concept
title: "Objetivo da Interface"
aliases: ["qual o objetivo da UI", "o que faz uma boa UI", "boa UI depende do objetivo"]
date_created: 2026-11-13
date_updated: 2026-11-23
source_count: 12
tags: [ui, ui-design, ux, design, conversao, cta]
skill: ux-ui-mentor
status: stub
---

# Objetivo da Interface

Critério para julgar se uma UI é boa: ela serve ao objetivo para o qual existe? Não há definição universal de "boa UI"; há interfaces que cumprem ou traem o próprio objetivo ([[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]]).

## Definir pelo negativo

A aula admite que definir boa UI pelo positivo é arriscado ("posso esquecer de algum detalhe") e prefere listar o que é UI ruim: [[wiki/concepts/contraste]] mal aplicado, typeface pequena usada pequena, dashboard com tanta informação que o usuário se perde.

## Exemplos de objetivo

| Interface | Objetivo |
|---|---|
| Padaria (vitrine) | Você olhar, desejar e comprar |
| Portfólio de fotógrafo | Mostrar o trabalho e conseguir novos clientes |
| Obras de um mestre de obras | Dar confiabilidade antes da contratação |
| Landing page do [[wiki/entities/frontpush]] | Você deixar nome e e-mail (lista de espera) |
| E-commerce | Você chegar ao fim da jornada de compra |

Com o objetivo definido, as decisões viram consequência: na landing page, o azul é usado pouco para que o CTA se destaque ([[wiki/concepts/hierarquia-visual]]); no e-commerce, carrinho, endereço, confirmação e pagamento precisam estar claros.

`[skill: ux-ui-mentor]` Na pirâmide de Aarron Walter, o objetivo é a camada "funcional": acabamento visual não compensa uma interface que não leva o usuário aonde ela promete.

## Relação com outros conceitos

- [[wiki/concepts/ux-design]] — UI e UX "precisam estar alinhados" no mesmo objetivo.
- [[wiki/concepts/porque-das-decisoes-de-design]] — o objetivo é o primeiro porquê.
- [[wiki/concepts/design-como-interacao]] — o visual entra a serviço do objetivo, não como fim.
- [[wiki/concepts/definicao-de-objetivo-antes-de-decisao]] — a mesma ideia aplicada a decisões de carreira.

## Objetivo como primeiro fator

Em [[wiki/sources/elementos-da-interface-introducao-ui-design]] o objetivo abre a lista de fatores que o design de interface precisa responder (objetivos, preferências, comportamento, usuário, cultura, posicionamento; ver [[wiki/concepts/contexto-do-usuario]]). "Sem um objetivo, eu não consigo nortear, eu não consigo traçar uma jornada." O exemplo volta a ser a landing page do [[wiki/entities/frontpush]]: página de aterrissagem que apresenta o produto e responde às dúvidas do possível cliente até ele deixar nome, e-mail ou telefone.

## O que se quer comunicar

Na aula de formas, a pergunta-guia é "o que você está querendo passar?": precisão para um site de transferências, segurança e delicadeza para uma loja de bebês, realidade para uma hamburgueria. A forma, a tipografia e a cor seguem essa resposta ([[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]]).

## A forma do botão segue o objetivo

"Qual a ideia que a interface está querendo passar" decide a forma do botão: o segredo está na predominância "daquilo que é o seu produto ou serviço" ([[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]]).

## Objetivos principais no wireframe

Em [[wiki/sources/wireframes-parte-1-o-que-e-uso-foco-page-map-papel-e-caneta]], o wireframe em preto e branco existe para discutir "o conteúdo, é o grosso, são o levantamento de requisitos, são os objetivos principais". O exemplo é uma página de vendas de curso cujo objetivo é a chamada para cadastro. O [[wiki/concepts/page-map]] monta a jornada "em acordo com os objetivos" (slide).

## A pergunta central do briefing

Em [[wiki/sources/wireframes-parte-2-briefing-objetivo-page-map-leitura-f-z]], "qual é o principal objetivo da sua interface?" é a pergunta que o [[wiki/concepts/briefing]] não pode pular: "o que você quer que o usuário faça". Portfólio quer que o visitante mande "uma mensagem, uma proposta"; página de venda quer "a inscrição" (e-mail, telefone); a [[wiki/entities/apple]] quer a compra ("tem aqui a sacolinha, então é um e-commerce"). O objetivo vem antes de tudo: "para que você construa o flow, o site map, o page map, a interface, os wireframes com base nisso" ([[wiki/concepts/page-map]]).

## O hero diz o que o site faz

Cada modelo de seção tem sua situação: app, desktop, depoimentos, lista de espera. O [[wiki/concepts/secao-hero|hero]] serve para "dar a primeira informação do que o seu site faz" ([[wiki/sources/wireframes-pratica-1-hero-page-map-frankenstein-referencias]]).

## O objetivo de um portfólio freelancer

Em [[wiki/sources/wireframes-pratica-2-page-map-por-referencias-hero-processo-cta]], o objetivo do portfólio de [[wiki/entities/jonas-miller]] "é que você entre no site dele, conheça o trabalho dele e solicite alguma proposta". Por isso o CTA aparece no hero e de novo no fim, onde é "o objetivo principal do seu site". O menu fixo de quatro itens serve para "deixar os objetivos muito bem claros".

## Objetivo da interface vs. necessidade do usuário

A aula [[wiki/sources/o-que-e-um-bom-design-atributos-util-aprendizado-memoravel-eficaz-desejavel-prazeroso]] põe "útil" como primeiro [[wiki/concepts/atributos-de-bom-design|atributo de um bom design]]: o produto faz algo que o usuário realmente precisa. São perguntas complementares: o objetivo é o que a interface quer que o usuário faça (comprar, cadastrar); a utilidade é se aquilo resolve uma necessidade dele.

## Jornadas sem bifurcação

Na aula de usabilidade, a definição já é sobre objetivo: usabilidade "permite que as pessoas alcancem facilmente os seus objetivos". A boa prática é usar "jornadas com objetivos claros, sem muita bifurcação". Num e-commerce, "muitos links, muitas coisas na jornada" fazem o usuário "se perder" ([[wiki/sources/usabilidade-facilmente-tres-esferas-boas-praticas-auxilio-emergencial]]). Ver [[wiki/concepts/usabilidade]].

## Botão, não link (FrontPUSH, mentoria de UI Design)

Na [[wiki/sources/frontpush-mentoria-ui-design-referencias-patterns-leitura-z-f-contraste|mentoria de UI Design]]: "você sempre vai ter um objetivo [...] Qual é o objetivo da sua página?" Na landing page do [[wiki/entities/frontpush|FrontPUSH]], é "que você conheça o meu trabalho e que você deixe o seu nome e o seu e-mail". A ação principal vai em botão: "Link, ele tem que parecer link. Botão, ele tem que parecer botão. O botão é para a tomada de ação, link é para o usuário explorar". Depois, contraste e posição no caminho do Z ([[wiki/concepts/hierarquia-visual]]). `[skill: ux-ui-mentor]` No código, o par é `<button>` para ação e `<a href>` para navegação.

## Key Sources

- [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]]
- [[wiki/sources/elementos-da-interface-introducao-ui-design]] — objetivo como primeiro fator; landing page como página de aterrissagem
- [[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]] — o que se quer comunicar define forma, tipo e cor
- [[wiki/sources/formas-geometricas-organicas-exemplos-dropbox-madero-coco-bambu-nubank]] — "o que você está querendo comunicar?" como pergunta de partida para escolher formas
- [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]] — forma do botão escolhida pelo que se quer comunicar
- [[wiki/sources/wireframes-parte-1-o-que-e-uso-foco-page-map-papel-e-caneta]] — levantamento de requisitos e objetivos principais no wireframe
- [[wiki/sources/wireframes-parte-2-briefing-objetivo-page-map-leitura-f-z]] — o objetivo como pergunta do briefing e base do page map
- [[wiki/sources/wireframes-pratica-1-hero-page-map-frankenstein-referencias]] — cada modelo de wireframe tem a sua situação de uso
- [[wiki/sources/wireframes-pratica-2-page-map-por-referencias-hero-processo-cta]] — portfólio freelancer: o objetivo é o pedido de proposta, no hero e no fim
- [[wiki/sources/o-que-e-um-bom-design-atributos-util-aprendizado-memoravel-eficaz-desejavel-prazeroso]] — "útil" como necessidade do usuário, complementar ao objetivo
- [[wiki/sources/usabilidade-facilmente-tres-esferas-boas-praticas-auxilio-emergencial]] — usabilidade como alcançar objetivos; jornada de compra sem bifurcação
- [[wiki/sources/frontpush-mentoria-ui-design-referencias-patterns-leitura-z-f-contraste]] — objetivo da LP; ação principal em botão, link é secundário
