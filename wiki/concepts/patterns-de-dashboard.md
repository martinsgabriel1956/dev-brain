---
type: concept
title: "Patterns de dashboard"
aliases: ["padrões de dashboard", "patterns de web app", "estruturas de dashboard"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 3
tags: [dashboard, padroes-de-interface, login, sidebar, topbar, cards, tabelas, formularios, modal]
skill: ux-ui-mentor
status: stub
---

# Patterns de dashboard

"Telas ou elementos [...] que vai estar presente em todo e qualquer Dashboard": "é muito difícil você achar um Dashboard que não tenha essas estruturas". São os [[wiki/concepts/padroes-de-interface|padrões de interface]] próprios de [[wiki/concepts/dashboard|dashboards]] e web apps, o ponto de partida dos wireframes, junto com o [[wiki/concepts/grid-de-dashboard|grid]] ([[wiki/sources/frontpush-dashboards-grids-e-patterns]]).

| Pattern | Para quê, segundo a aula |
|---|---|
| Login | "Uma primeira barreira": o acesso "é restrito aos funcionários, aos gerentes" ([[wiki/concepts/autenticacao-e-autorizacao]]) |
| [[wiki/concepts/sidebar\|Sidebar]] | "Como se fosse o menu das nossas Landing Pages": os principais fluxos de navegação |
| Top bar | Busca, notificações, usuário; opcionalmente o launcher de apps ("nove pontinhos", como o [[wiki/entities/google\|Google]]) |
| Cards e gráficos | Comparar com filtros "para poder melhor realizar [...] decisões" |
| Listas e tabelas | "Muitos filtros [...] e as principais ações" |
| Formulários | Dados do usuário, com uma "sub-sidebar" de seções |
| [[wiki/concepts/modal\|Modais]] | Confirmar, questionar, avisar, informar, com [[wiki/concepts/cor-semantica\|cor semântica]] |

A justificativa é a mesma da [[wiki/concepts/lei-de-jakob]]: "se eu ficar mudando demais esse Pattern, ele pode ser que piore a experiência do usuário". E os patterns de navegação (sidebar, menu que expande, launcher) servem para "classificar e hierarquizar" o que os dashboards antigos jogavam "em uma tela só" ([[wiki/concepts/hierarquia-visual]]).

`[skill: ux-ui-mentor]` Para as tabelas, a referência `ux-enterprise-b2b.md` acrescenta chips de filtros ativos, visões salvas, ações em lote com "desfazer", exportação que respeita filtros e estados de vazio e erro.

## Login como ponto de partida de fluxos

Na [[wiki/sources/frontpush-dashboards-principios-parte-1|aula 04 do módulo de dashboards]], o pattern de login vira exemplo de fluxo: a tela inicial abre sucesso, senha errada, recuperar senha, criar conta e login social, cada um com subfluxos. Ver [[wiki/concepts/fluxos-bem-definidos]].

## Entidades à esquerda, conta à direita

Na [[wiki/sources/frontpush-dashboards-wireframes-e-fluxos|aula 07 do módulo de dashboards]]: "as principais entidades" e ações vão na sidebar (home, cursos, administração, suporte, logout); conta, busca, apps e notificações na top bar, com o perfil "no canto superior direito", como no Google. "Como é que você sabe disso? Patterns."

## Key Sources

- [[wiki/sources/frontpush-dashboards-grids-e-patterns]]: os sete patterns do DashClass
- [[wiki/sources/frontpush-dashboards-principios-parte-1]]: FrontPUSH, dashboards aula 04: fluxos que saem do login
- [[wiki/sources/frontpush-dashboards-wireframes-e-fluxos]]: FrontPUSH, dashboards aula 07: o que vai na sidebar e na top bar
