---
type: concept
title: "Lei da Proximidade (Gestalt)"
aliases: ["law of proximity", "gestalt proximity", "princípios de gestalt", "gestalt design"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
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

## Key Sources

- [[wiki/sources/5-boas-praticas-uiux-ux-pilot]]
