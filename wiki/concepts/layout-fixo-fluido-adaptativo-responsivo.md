---
type: concept
title: "Layout fixo, fluido, adaptativo e responsivo"
aliases: ["layout fixo", "layout fluido", "layout adaptativo", "fixed vs fluid vs adaptive vs responsive", "adaptive design", "fluid layout"]
date_created: 2026-11-15
date_updated: 2026-11-16
source_count: 5
tags: [ui, ui-design, layout, responsividade, breakpoint, media-query, css]
skill: ux-ui-mentor
status: stub
---

# Layout fixo, fluido, adaptativo e responsivo

Quatro formas de uma interface lidar com tamanhos de tela diferentes, apresentadas como degraus em [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]]:

| Tipo | Como funciona (na aula) | Quando serve | Limite |
|---|---|---|---|
| **Fixo** | Projetado para uma tela só | Aparelho único e duradouro, como iPads de atendimento de uma pizzaria | "Pouquíssimo comum hoje em dia" |
| **Fluido** | Larguras em porcentagem; a imagem com 100% da caixa encolhe com ela | Seções e trechos entre breakpoints | Não quebra para a vertical: os blocos ficam lado a lado "até eu esmagar os dois" |
| **Adaptativo** | Media query troca o estilo num [[wiki/concepts/breakpoint]] (ex.: abaixo de 960 px), "de repente" | Conjunto conhecido de telas | Quebra em resoluções não previstas; um estilo por tela dá trabalho |
| **Responsivo** | Fluido + adaptativo: seções que encolhem e estilos extras em resoluções específicas | O padrão atual, "o queridinho" | "Um pouco mais carregado"; precisa de teste em vários aparelhos |

O argumento contra o adaptativo puro é a variedade de aparelhos: "você tem quantos modelos de Galaxy [...] até de iPhone". Fazer um estilo para cada um "é praticamente suicídio". Ver [[wiki/concepts/design-responsivo]].

## Nomes que mudam de sentido

`[external]` Ethan Marcotte definiu o design responsivo (2010) como grid fluido, imagens flexíveis e media queries (https://alistapart.com/article/responsive-web-design/), a mesma soma da aula. "Adaptive web design" (Aaron Gustafson, 2011) originalmente quer dizer melhoria progressiva. O sentido da aula (layouts fixos trocados em breakpoints) é o uso mais comum hoje.

`[skill: ux-ui-mentor]` Na skill, "fixed" é o container com max-width centralizado e "fluid" é o que acompanha a viewport (dashboards, tabelas). O "hybrid", container fixo com elementos fluidos, é "o mais comum em produtos". É o responsivo da aula visto pelo container.

## "Adaptativo é mais rápido"

A aula diz que o adaptativo é "mais otimizado" porque manda "exatamente o estilo daquela tela". `[external]` Isso vale quando o servidor detecta o aparelho e serve HTML ou CSS diferente (dynamic serving). Com media queries, o navegador baixa todas as regras e só aplica as que casam; o ganho de transferência some (https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing).

## Relação com outros conceitos

- [[wiki/concepts/grid-de-colunas]]: o número de colunas muda em cada breakpoint.
- [[wiki/concepts/breakpoint]]: o ponto onde o adaptativo troca de estilo.
- [[wiki/concepts/design-responsivo]]: o histórico e as práticas do responsivo.

## "Uma sanfona" (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-funcoes-sass]]: "o caráter ser responsivo precisa ser adaptável e ele precisa ser fluido"; o layout foi desenhado para 1920 × 1080, mas há telas de 1366, então o grid usa % para "ir cabendo antes de quebrar para a versão mobile".

## Máximo fixo, depois fluido (FrontPUSH, Sass aula 10)

Em [[wiki/sources/frontpush-grid-system-sass-parte-1]]: "eu utilizo os containers com tamanho máximo fixo e depois ele se torna fluido", porque em monitores 21:9 um layout totalmente fluido "iria esticar em toda a tela". As colunas em % fazem o conjunto "apertar" até o breakpoint, onde empilham.

## Key Sources

- [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]]: os quatro tipos, com o iPad da pizzaria, a logo que encolhe e o breakpoint de 960
- [[wiki/sources/frontpush-intro-flexbox-flex-container-flex-item]]: Flexbox como o esqueleto que "se adapte ao tamanho da tela"
- [[wiki/sources/frontpush-flex-direction-flex-wrap-flex-flow]]: container com `max-width: 700px` "ajusta"; com `width: 700px`, não
- [[wiki/sources/frontpush-funcoes-sass]]: grid fluido em % antes do breakpoint mobile
- [[wiki/sources/frontpush-grid-system-sass-parte-1]]: container de máximo fixo + colunas fluidas
