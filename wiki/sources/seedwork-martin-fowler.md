---
type: source
title: "Seedwork (Martin Fowler)"
aliases: ["seedwork bliki", "seed work"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_file: /home/nemomartins/Documentos/new/dev-study/raw/seedwork-martin-fowler.md
source_url: "https://martinfowler.com/bliki/Seedwork.html"
author: "Martin Fowler"
date_published: 2003-09-11
date_ingested: 2026-08-21
source_count: 0
tags: [arquitetura, reuso, frameworks, martin-fowler, copy-paste, dll-hell, application-boundary]
skill: tech-mentor-backend
status: stable
---

# Seedwork (Martin Fowler)

## TL;DR

Bliki entry curto de 2003 em que Fowler nomeia o **seedwork**: uma alternativa pragmática (e imperfeita) a frameworks reutilizáveis tradicionais, surgida de uma discussão originada num post de Michael Feathers. Enquanto um framework é uma aplicação parcialmente pronta que se estende de forma controlada, um seedwork é uma funcionalidade mínima que cada time modifica livremente — na prática, reuso por copiar-e-colar, que o próprio Fowler reconhece normalmente desprezar, mas defende como opção válida quando um bom framework está fora de alcance. O texto termina generalizando o argumento: reuso *dentro* de uma aplicação é essencial e alcançável; reuso *entre* aplicações é muito mais difícil, em parte porque uma [[wiki/concepts/application-boundary|fronteira de aplicação]] é, antes de tudo, uma construção social — o mesmo argumento que Fowler desenvolveria de forma independente no mesmo dia em [[wiki/sources/application-boundary-martin-fowler]].

## Key Claims

- **Definição central**: um framework é uma aplicação parcialmente construída que você estende de formas controladas; um **seedwork** é uma funcionalidade mínima que você modifica como quiser. A consequência inevitável: quem expande um seedwork passa a ser dono dele — não há atualizações compartilhadas depois disso. → [[wiki/concepts/seedwork]]
- **Origem do termo**: não é invenção original de Fowler — nasceu de um weblog de Michael Feathers e da discussão que se seguiu a ele; Fowler apenas relata e endossa a ideia.
- **Reabilitação parcial de reuso por copiar-e-colar**: Fowler reconhece que normalmente despreza esse tipo de reuso, mas argumenta que frameworks bons são raros e difíceis de alcançar — então a pergunta certa não é "isso é ideal?", é "isso é útil?". Isso tensiona diretamente com o sinal de [[wiki/concepts/under-engineering|under-engineering]] "copy-paste sem estrutura" já registrado na wiki — ver nota de contraste na página.
- **Mesmo o reuso maduro é difícil**: bibliotecas compartilhadas que evoluem em cronogramas diferentes geram problemas de versionamento — cita explicitamente o "DLL-hell" da Microsoft e um incidente pessoal de dependências quebradas no RedHat. Antecipa, em 2003, a mesma dor que hoje justifica práticas como [[wiki/concepts/schema-evolution|schema evolution]] e versionamento semântico de contratos.
- **Reuso intra-aplicação vital, reuso inter-aplicação muito mais difícil**: a causa principal, segundo Fowler, é que uma [[wiki/concepts/application-boundary|ApplicationBoundary]] é primariamente uma construção social — link explícito, feito pelo próprio Fowler no texto original, para o seu outro bliki entry do mesmo dia.
- **Conclusão pragmática**: seedworks não são a alternativa ideal, mas são uma alternativa "menos perfeita" que vale considerar justamente porque frameworks reutilizáveis são mais difíceis de acertar do que a indústria gostaria de admitir.

## Entities

[[wiki/entities/martin-fowler]] · [[wiki/entities/kent-beck]] (via [[wiki/concepts/seedwork]]) · [[wiki/entities/microsoft]] (DLL-hell)

## Concepts

[[wiki/concepts/seedwork]] · [[wiki/concepts/application-boundary]] · [[wiki/concepts/under-engineering]] · [[wiki/concepts/yagni]] · [[wiki/concepts/monolith-first]] · [[wiki/concepts/arquitetura-de-software]]

## Conexão com Application Boundary — mesmo dia, mesmo argumento em duas escalas

Este bliki e [[wiki/sources/application-boundary-martin-fowler]] foram publicados na mesma data (11 de setembro de 2003) e compartilham a mesma tese de fundo: fronteiras de software — seja a fronteira de uma aplicação, seja a fronteira de um pacote/framework compartilhado — não são resolvidas puramente por engenharia, porque a coordenação entre pessoas e times (quem mantém o quê, quem aceita atualizações de quem) é, no fim, um problema social. Aqui Fowler aplica esse argumento a *por que reuso entre aplicações falha*; lá, a *por que aplicações não desaparecem com SOA*. Ver a seção "Application Boundary" para o desenvolvimento completo dessa tese.

## Tensão com Under-Engineering: copy-paste é sinal ou é solução?

[[wiki/concepts/under-engineering]] lista "copy-paste sem estrutura" como sintoma de engenharia insuficiente — duplicação sem extrair um ponto único de mudança. Este artigo defende exatamente esse padrão em um contexto específico: quando a alternativa realista não é "um bom framework compartilhado" mas "nenhum framework nenhum", copiar e adaptar uma base mínima é mais honesto do que fingir que existe uma abstração compartilhável madura. As duas posições não se contradizem — convergem no mesmo critério contextual que a wiki já usa em outros lugares (ver [[wiki/concepts/yagni]] e [[wiki/concepts/monolith-first]]): a escolha certa depende de quão madura é a alternativa "certa" disponível *agora*, não de um ideal abstrato.

## Open Questions

- O artigo não detalha *como* decidir quando vale a pena migrar de seedwork para investir num framework compartilhado de fato — fica implícito que isso depende de quando a organização finalmente consegue "amadurecer" um framework, sem critério objetivo proposto.
- Não há, nesta wiki, uma fonte primária ingerida do weblog original de Michael Feathers que Fowler cita como origem do termo — apenas a menção de segunda mão feita aqui.

## Raw Quotes

> "A framework is supposed to be a part-baked application that you extend in controlled ways to provide what you need. A seedwork is some minimal functionality that you modify however you like to get what you need."

> "Frameworks and libraries work very well when they are well-seasoned. But getting a good framework is very hard. Seedworks are not as useful as a good framework, but are easier to create and use. The point is not whether they are ideal, but just whether they are useful."

> "I've found that reuse (or avoiding duplication) within an application is vital. But reuse across applications is much tougher, primarily because an ApplicationBoundary is primarily a social construction."

*(Tradução completa em `raw/seedwork-martin-fowler.md`; para o texto exato em inglês, ver `source_url`.)*
