---
type: concept
title: "Lei da Proximidade (Gestalt)"
aliases: ["law of proximity", "gestalt proximity", "princípios de gestalt", "gestalt design"]
date_created: 2026-07-21
date_updated: 2026-11-13
source_count: 6
tags: [ui, ux, design, gestalt, frontend]
skill: tech-mentor-frontend
status: draft
---

# Lei da Proximidade (Gestalt)

Um dos princípios de Gestalt (área de pesquisa em percepção visual): elementos próximos entre si — em distância, cor ou forma — são percebidos pelo cérebro como pertencentes a um único grupo, independentemente de serem, individualmente, itens distintos. Afastar um elemento dos demais (ou dar-lhe uma cor/forma diferente) quebra essa percepção de grupo, mesmo sem mudar nada no conteúdo.

## Exemplo clássico

Três fileiras de bolinhas equidistantes são lidas como um único grupo. Ao afastar a terceira fileira das outras duas, o cérebro passa a interpretar duas fileiras como um grupo e a terceira como outro grupo, separado — só pela distância, sem qualquer outra mudança.

O logo da Unilever ilustra o mesmo princípio aplicado a ícones: cada desenho (cenoura, flor, peixe etc.) é, isoladamente, um item independente; vistos em conjunto e próximos, formam a letra U — um grupo percebido como unidade.

## Por que importa em UI

Se um dado (por exemplo, prova social — número de usuários, cursos disponíveis) deve reforçar um argumento (por exemplo, uma promessa de valor no título), os dois precisam estar **próximos na tela**, não apenas relacionados no conteúdo. Sem proximidade visual, o cérebro processa os dois blocos como coisas separadas, e o argumento perde força — mesmo que a lógica textual conecte os dois.

O inverso também vale: para separar duas ideias que não devem ser lidas como a mesma coisa (por exemplo, a "promessa" de um produto e a "ação" que o usuário precisa tomar, como preencher um formulário), é preciso aumentar deliberadamente o espaço/margem entre os blocos.

## Aplicação em prompts de geração de UI

Pode ser declarada explicitamente num prompt de refatoração de layout: agrupar visualmente elementos que reforçam o mesmo argumento (reduzindo o gap entre eles) e aumentar a margem entre blocos que representam etapas ou ideias diferentes do fluxo do usuário.

## Relação com outros conceitos

- [[wiki/concepts/hierarquia-visual]] — proximidade agrupa elementos; hierarquia define a ordem em que os grupos são vistos.
- [[wiki/concepts/design-como-interacao]] — Gestalt é um princípio de percepção que informa decisões de design que vão além do visual isolado.

## Eixo de reforço

Em [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]], deslocar um item para fora do [[wiki/concepts/eixo-visual|eixo]] principal faz o usuário lê-lo como parte do item de cima (retweet e resposta no feed do Twitter). É agrupamento por posição, o mesmo mecanismo desta lei. `[skill: ux-ui-mentor]` O sistema de espaçamento relacional (8 a 16px entre relacionados, 48 a 64px entre grupos) é esta lei implementada; ver [[wiki/concepts/espaco-em-branco]].

## Micro espaço e resultados do Google

Em [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]], a lei aparece como **micro espaço**: espaço pequeno entre elementos indica grupo, espaço grande indica coisas diferentes. No [[wiki/concepts/wireframe]] de menu, links próximos e equidistantes formam um grupo, separados da logo e do CTA por vãos maiores. Nos resultados de busca do [[wiki/entities/google]], anúncio e título formam um "card" sem borda nenhuma, só por estarem mais perto, e um bloco recuado à esquerda é lido como parte do bloco de cima mesmo estando mais longe: o recuo (alinhamento) reforça a proximidade. Para fixar os valores dos vãos, a aula usa o [[wiki/concepts/grid-de-8-pontos]].

## Google na visão geral

A visão geral dos elementos repete o exemplo: o texto pertence ao título "por ele estar mais próximo", o recuo maior marca sublinks e cada resultado é "uma caixinha" sem borda ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]).

## Espaço curto agrupa, longo separa

O slide da aula de espaçamento e linhas resume a lei em duas linhas: "Agrupa elementos: espaço curto / Separa os elementos: espaço longo". Em interfaces densas (Facebook, G1), o espaço encolhe e linhas e cards reforçam a separação ([[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]]; ver [[wiki/concepts/densidade-de-informacao]]).

## Key Sources

- [[wiki/sources/5-boas-praticas-uiux-ux-pilot]]
- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] — eixo de reforço como agrupamento por posição
- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]] — micro espaço; agrupamento sem bordas na busca do Google
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — mesmo exemplo do Google, na visão geral do módulo
- [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]] — slide: espaço curto agrupa, longo separa
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — agrupar (Ctrl + G) e dar 16 dentro do grupo e 32 entre grupos
