---
type: source
title: "Patterns: o que faz uma boa UI e o que são padrões"
aliases: ["aula patterns ui design", "o que faz uma boa ui", "o que são padrões em ui"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, ux, design, padroes-de-interface, contraste, lei-de-jakob, e-commerce, landing-page, cta]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/patterns-o-que-faz-uma-boa-ui-padroes.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-13
---

# Patterns: o que faz uma boa UI e o que são padrões

## TL;DR

Aula do módulo de UI Design do [[wiki/entities/frontpush|FrontPUSH]], provavelmente do instrutor [[wiki/entities/nasser|Násser]] (mesmo módulo de [[wiki/sources/o-que-e-ux-ui-design]] e [[wiki/sources/como-aprender-ui]]). Duas perguntas. **O que faz uma boa UI?** É difícil definir pelo positivo, mas fácil pelo negativo: contraste mal aplicado, tipografia pequena, dashboard lotado. O critério de fundo é [[wiki/concepts/objetivo-da-interface|o objetivo da interface]]: padaria quer que você compre, portfólio quer clientes, landing page quer o e-mail, e-commerce quer que você conclua a jornada. **O que são padrões?** O cérebro trabalha com padrões (busca no topo, três tracinhos = menu), e a UI deve jogar a favor deles ([[wiki/concepts/padroes-de-interface]], [[wiki/concepts/lei-de-jakob]]). Fecha lembrando que o usuário talvez não seja você.

## Key Claims

- **Boa UI se define melhor pelo negativo.** O autor não arrisca uma definição afirmativa porque "posso esquecer de algum detalhe", mas lista o que é UI ruim:
  - [[wiki/concepts/contraste|contraste]] mal aplicado, que você lê mas idosos ou pessoas com baixa visão não;
  - typeface que já é pequena, usada pequena;
  - dashboard com tanta informação que o usuário demora a achar a ação e se perde.
  - `[skill: ux-ui-mentor]` Os três casos batem com WCAG AA (texto normal pede 4.5:1) e com a heurística 8 de Nielsen ("dashboard com 12 métricas de igual peso visual" é a violação clássica).
- **A pergunta certa é "qual o objetivo desta interface?"** Exemplos: padaria (desejar e comprar), portfólio de fotógrafo (novos clientes), obras do mestre de obras (confiabilidade antes de contratar), landing page do FrontPUSH (nome e e-mail), e-commerce (chegar ao fim da jornada). Ver [[wiki/concepts/objetivo-da-interface]].
- **E-commerce falha por detalhes de jornada:** CTA mal estabelecido, sem controle do carrinho e do endereço, sem confirmação, sem informação do método de pagamento. UI e UX "precisam estar alinhados" ([[wiki/concepts/ux-design]]).
- **Contraste a serviço do objetivo.** A landing page do autor é toda preta e neutra, com branco no texto e azul só em pontos específicos. Quanto menos azul, mais o botão "entrar na lista de espera" se destaca de longe. Botão de cadastro sem contraste trai o objetivo da página. Ver [[wiki/concepts/hierarquia-visual]].
  - Isso tem nome no catálogo de [[wiki/sources/ui-patterns-com-biblioteca-de-padroes]]: Isolation Effect (o efeito Von Restorff), na seção de atenção dos padrões persuasivos.
- **O visual importa.** O autor escolhe produtos e carros também pelo design, mesmo quando outro tem motor melhor. (Parte do exemplo do carro caiu da legenda.)
- **O cérebro trabalha com padrões.** Se o produto não está nos destaques, o usuário procura a busca no menu, e o menu fica no topo. Três tracinhos são lidos como menu hambúrguer. "Não é tão interessante você fugir desses padrões." Ver [[wiki/concepts/padroes-de-interface]] e [[wiki/concepts/lei-de-jakob]].
- **Padrão se valida com pesquisa.** Teste de usabilidade e heatmap mostram o lado intuitivo do usuário; a aula só passa a ideia.
- **Lupinha sozinha é um equívoco em e-commerce.** Com muita informação na tela, o usuário leigo não vai notar um ícone no canto; uma barra de busca grande ("digite o seu produto") antecipa o erro ([[wiki/concepts/usuarios-como-agentes-do-caos]]).
  - `[external]` Nielsen recomendava o mesmo em 2001: na home, busca como caixa de texto no topo, não como link; ele relata 91% a mais de uso da busca ao trocar o link pela caixa no próprio site ([NN/g, "Search: Visible and Simple"](https://www.nngroup.com/articles/search-visible-and-simple/)). Confiança média-alta: a orientação é antiga, mas segue no catálogo da NN/g.
- **O usuário talvez não seja você.** É preciso entender quem ele é.

## Entities

- [[wiki/entities/nasser]] — instrutor provável (inferido pelo módulo e pelo curso).
- [[wiki/entities/frontpush]] — curso do autor; a landing page é o exemplo central.

## Concepts

- [[wiki/concepts/objetivo-da-interface]] (novo)
- [[wiki/concepts/padroes-de-interface]] (novo)
- [[wiki/concepts/lei-de-jakob]] (novo)
- [[wiki/concepts/contraste]] (novo)
- [[wiki/concepts/ui-design]]
- [[wiki/concepts/ux-design]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/affordance]] — o ícone de três tracinhos só funciona por convenção aprendida
- [[wiki/concepts/usuarios-como-agentes-do-caos]]
- [[wiki/concepts/pattern-recognition]]
- [[wiki/concepts/design-como-interacao]]

## Tensões com a wiki

- **"O visual importa" vs. "a ilusão do bonito".** [[wiki/concepts/design-como-interacao]] alerta que estudar só a parte visual gera layouts bonitos e inúteis. A aula não contradiz: o visual entra subordinado ao objetivo (o azul existe para o CTA), não como fim.
- **Menu hambúrguer como padrão reconhecível.** A aula o trata como intuitivo, com a ressalva "pode não ser o senso comum". `[external]` A NN/g diz que o ícone não é reconhecido por todos e que navegação escondida é menos usada que a visível ou combinada: num teste no mobile, 89% das tarefas usaram a navegação num site com menu visível + escondido, contra 44% num site só com menu escondido ([NN/g, Pernice e Budiu, 2016](https://www.nngroup.com/articles/find-navigation-mobile-even-hamburger/)). É o mesmo argumento da aula contra a lupinha sozinha, aplicado ao próprio hambúrguer.

## Open Questions

- ~~O instrutor é mesmo Násser e o curso é o FrontPUSH?~~ Resolvido em [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]]: Násser diz o próprio nome e mostra frontpush.com.br como "a minha interface".
- O que dizia o trecho perdido entre "carcaça bem estabelecida" e "Requisitos para poder eu decidir naquele carro"?
- A aula promete "muitos exemplos" de padrões; o slide lista "Exemplos", mas a fala só dá três (busca no topo, hambúrguer, lupinha). Vêm em aula futura?

## Raw Quotes

> "Talvez eu não consiga te definir, mas eu consigo te definir o que é uma má UI."

> "Qual é o objetivo da UI? Qual é o objetivo da minha interface?"

> "Vocês têm que entender, pessoal, que o cérebro humano trabalha com padrões."

> "Quando a gente está projetando a UI não é tão interessante você fugir desses padrões."

> "O usuário daquela interface talvez não seja eu, e eu preciso entender quem é aquele usuário."
