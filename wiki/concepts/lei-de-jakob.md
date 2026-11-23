---
type: concept
title: "Lei de Jakob"
aliases: ["Jakob's Law", "jakobs law", "lei de jakob nielsen"]
date_created: 2026-11-13
date_updated: 2026-11-23
source_count: 7
tags: [ux, ui, design, leis-de-ux, padroes-de-interface, usabilidade]
skill: ux-ui-mentor
status: stub
---

# Lei de Jakob

`[skill: ux-ui-mentor]` Usuários passam a maior parte do tempo em outros sites e esperam que o seu funcione igual. Aplicação: não reinventar padrões sem motivo forte (logo no canto esquerdo, busca no header). Para dev: seguir os padrões de um design system (Radix, shadcn) já é a Lei de Jakob na prática. Leva o nome de Jakob Nielsen, da NN/g.

A aula [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]] defende a mesma ideia sem o nome: o usuário procura a busca no menu do topo porque é onde ela sempre esteve, e "não é tão interessante você fugir desses padrões". Ver [[wiki/concepts/padroes-de-interface]].

`[external]` A heurística 4 de Nielsen, "consistência e padrões", cobre a mesma ideia dentro de um produto: mesmas ações, mesmas palavras, mesmos resultados.

## Relação com outros conceitos

- [[wiki/concepts/padroes-de-interface]] — os padrões que a lei manda respeitar.
- [[wiki/concepts/pattern-recognition]] — o mecanismo cognitivo por trás da expectativa.
- [[wiki/concepts/affordance]] — convenções aprendidas viram affordances.

## Menu à esquerda ou no topo

[[wiki/sources/elementos-da-interface-introducao-ui-design]] dá outro exemplo: num website o menu fica à esquerda ou no topo, porque as pessoas aprenderam isso no dia a dia; pô-lo embaixo "fere um pattern".

## Ícones de senso comum

A aula de ícones da edição "W7" aplica a ideia a ícones: "sempre procurar colocar ícones de senso comum" e "não mudar drasticamente" ([[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]]).

## Aprender de novo custa

Em [[wiki/sources/acessibilidade-wcag-contraste-textos-invisiveis-kiss-patterns]]: "se você projetar algo totalmente novo, o usuário vai ter que gastar tempo para poder aprender como é que utiliza a sua interface". Patterns já testados poupam isso. Ver [[wiki/concepts/padroes-de-interface]].

## Padrões internos: os atalhos do Photoshop

[[wiki/sources/o-que-e-um-bom-design-atributos-util-aprendizado-memoravel-eficaz-desejavel-prazeroso]] aplica a ideia dentro de um produto: a Adobe mudou atalhos de teclado do Photoshop que já eram usados, e o usuário teve que reaprender. "Deve ter um bom motivo", mas no critério de aprendizado "pode ter sido um pecado". Aqui a expectativa não vem de outros sites, vem das versões anteriores do mesmo software, mais perto da heurística 4 (consistência e padrões) que da lei de Jakob em sentido estrito.

## Menu da Apple e "não reinventar a roda"

Na aula de usabilidade, o menu da [[wiki/entities/apple]] fica no topo, fixo, "que é justamente onde você procura. Isso aqui é um padrão". Padrões "testados" e "comprovados no mercado" melhoram a [[wiki/concepts/usabilidade]] porque "as empresas já trabalharam para poder instalar esses padrões na sua cabeça" ([[wiki/sources/usabilidade-facilmente-tres-esferas-boas-praticas-auxilio-emergencial]]). É a lei sem o nome, outra vez.

## Mudança pequena e gradual (FrontPUSH, mentoria de UI Design)

Na [[wiki/sources/frontpush-mentoria-ui-design-referencias-patterns-leitura-z-f-contraste|mentoria de UI Design]]: o usuário da Kabum "já sabe onde está o botão de adicionar novo endereço", "o código de rastreio", "a posição e a jornada que eu faço toda vez". Por isso grandes lojas trocam a UI em passos pequenos, e "toda e qualquer decisão que você saia do padrão nisso aqui, você pode acabar com a empresa". Ele restringe o peso ao e-commerce, "dados as devidas proporções em outras UIs".

## Key Sources

- [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]]
- [[wiki/sources/elementos-da-interface-introducao-ui-design]] — menu embaixo em website fere o padrão aprendido
- [[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]] — ícones de senso comum, "não mudar drasticamente"
- [[wiki/sources/acessibilidade-wcag-contraste-textos-invisiveis-kiss-patterns]] — interface totalmente nova obriga o usuário a reaprender
- [[wiki/sources/o-que-e-um-bom-design-atributos-util-aprendizado-memoravel-eficaz-desejavel-prazeroso]] — atalhos do Photoshop: expectativa formada pelo próprio produto
- [[wiki/sources/usabilidade-facilmente-tres-esferas-boas-praticas-auxilio-emergencial]] — menu fixo da Apple; padrões "instalados na sua cabeça"
- [[wiki/sources/frontpush-mentoria-ui-design-referencias-patterns-leitura-z-f-contraste]] — usuário da Kabum já sabe onde fica cada botão; redesign só em passos pequenos
