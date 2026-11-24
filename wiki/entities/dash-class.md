---
type: entity
title: "Dash Class"
aliases: ["DashClass", "Dash Class", "Desk Class", "módulo de dashboards do FrontPUSH"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 6
tags: [projeto, curso, dashboard, plataforma-de-ensino, ui-design]
skill: ux-ui-mentor
status: stub
---

# Dash Class

Módulo de dashboards do [[wiki/entities/frontpush|FrontPUSH]], lançado na "atualização 3.0", e o projeto que dá nome a ele: uma plataforma de ensino com painel administrativo, que [[wiki/entities/nasser|Násser]] "desenvolveu para algumas pessoas" e adaptou para o curso ([[wiki/sources/frontpush-dashboards-introducao-para-que-serve-utilidades-tipos]]).

- O arquivo no [[wiki/entities/figma|Figma]] "é bem completo com relação a fluxos" e traz modelos de wireframe, com uma página só de aulas. O link fica no Notion do curso, com senha.
- Foco: dashboards financeiro, estratégico e de plataforma ([[wiki/concepts/tipos-de-dashboard]]); no estratégico, o engajamento dos alunos.
- Origem: a experiência no player de vídeo da [[wiki/entities/finclass|Finclass]] e plataformas de ensino feitas para clientes ([[wiki/entities/gustavo-web|Gustavo Web]], professor de PHP, e o [[wiki/entities/como-se-virar|Como se virar]], de uma dupla de médicos). Provável parentesco com o orçamento "UI Design Dashboard" de [[wiki/sources/frontpush-monetizacao-freelancer-modelos-de-orcamento-e-invoice]] (inferência, média).
- Grafia: o slide da aula 02 escreve "DashClass", junto; as legendas separam ("Dash Class", "Desk Class").

Ver [[wiki/concepts/dashboard]].

## Escopo e fluxos (aula 02)

Na [[wiki/sources/frontpush-dashboards-overview-do-projeto-dashclass|aula 02 do módulo de dashboards]]: "uma plataforma de ensino para disponibilizar aulas gravadas", "como se fosse a [[wiki/entities/hotmart|Hotmart]]", mix enxuto de três projetos ([[wiki/entities/finclass|Finclass]], [[wiki/entities/como-se-virar|Como se virar]] e a plataforma de [[wiki/entities/gustavo-web|Gustavo Web]]). Escopo do slide: fluxo de pagamentos, login, [[wiki/concepts/gamificacao|gamificação]], fluxo de usuário, painel administrativo, fluxo de aulas; mobile e template HTML/CSS/JS "em breve". O arquivo tem abas de inspirações, style guide e grids, telas e aulas. O slide escreve "DashClass", junto.

## Grids e patterns (aula 03)

Na [[wiki/sources/frontpush-dashboards-grids-e-patterns|aula 03 do módulo de dashboards]]: três grids de 12 colunas com offset para a sidebar (o projeto usa o grid 1: coluna 70, gutter 30, offset 240) e sete patterns, todos mostrados em telas de alta fidelidade (login, sidebar, top bar, painel administrativo, vendas, perfil, modais). As telas trazem marcas do [[wiki/entities/como-se-virar|Como se virar]].

## Fluxo de recuperar senha (aula 04)

Na [[wiki/sources/frontpush-dashboards-principios-parte-1|aula 04 do módulo de dashboards]], o login do DashClass ilustra fluxos bem definidos: "passo 1 de 3, recuperar senha", por e-mail ou telefone, código de verificação, nova senha e redirecionamento, com cancelar e voltar.

## Requisitos prometidos (aula 05)

Na [[wiki/sources/frontpush-dashboards-principios-parte-2|aula 05 do módulo de dashboards]], [[wiki/entities/nasser|Násser]] explica o método (requisitos, atores, entidades, CRUD, atributos) e anuncia "um breve levantamento de requisitos" do DashClass nas próximas aulas.

## Requisitos e modelo (aula 06)

Na [[wiki/sources/frontpush-dashboards-levantamento-de-requisitos-dashclass|aula 06 do módulo de dashboards]]: três atores (aluno, funcionário, administrador), dois fluxos (aluno e administrativo) e três entidades: user (id, perfil, e-mail, data de aniversário, nome, CPF), venda (forma de pagamento, id do funcionário, id do comprador, parcelamento, NF-e, data, itens) e produtos = cursos (nome, capa, instrutores, módulos, aulas). A gamificação exige notificações e uma hierarquia de cursos, módulos e aulas. O modelo é simplificado de propósito e deixa de fora entidades que as telas pressupõem (módulo, aula, progresso, conquista, matrícula).

## Key Sources

- [[wiki/sources/frontpush-dashboards-introducao-para-que-serve-utilidades-tipos]]: aula 01, introdução
- [[wiki/sources/frontpush-dashboards-overview-do-projeto-dashclass]]: FrontPUSH, dashboards aula 02: origem, escopo, fluxos e painel admin
- [[wiki/sources/frontpush-dashboards-grids-e-patterns]]: FrontPUSH, dashboards aula 03: grids e patterns
- [[wiki/sources/frontpush-dashboards-principios-parte-1]]: FrontPUSH, dashboards aula 04: recuperar senha em três passos
- [[wiki/sources/frontpush-dashboards-principios-parte-2]]: FrontPUSH, dashboards aula 05: método de requisitos antes do DashClass
- [[wiki/sources/frontpush-dashboards-levantamento-de-requisitos-dashclass]]: FrontPUSH, dashboards aula 06: atores, entidades e gamificação
