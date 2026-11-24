---
type: concept
title: "Rbac"
aliases: []
date_created: 2026-09-22
date_updated: 2026-11-24
source_count: 5
tags: [rbac]
skill: tech-mentor-security
status: stub
---

# Rbac

Stub criado durante sweep de lint (links quebrados) a partir de referências em 2 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/sources/kubernetes-security]]: [[wiki/concepts/rbac]]
- Em [[wiki/sources/rbac-abac-rebac]]: [[wiki/concepts/rbac]]

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

## Atores em hierarquia (FrontPUSH)

Na [[wiki/sources/frontpush-dashboards-principios-parte-2|aula 05 do módulo de dashboards]], a hierarquia funcionário → gerente → administrador ou CEO é levantada como [[wiki/concepts/atores-do-sistema|atores do sistema]], e o atributo "perfil" do usuário define o "acesso hierárquico": RBAC em forma de requisito.

## Perfil com valores de menos

Na [[wiki/sources/frontpush-dashboards-levantamento-de-requisitos-dashclass|aula 06 do módulo de dashboards]], o perfil do user é "administrador ou um usuário normal", mas há três atores (aluno, funcionário, administrador) e o administrativo tem "acesso restrito a determinadas telas": o perfil precisa de pelo menos três papéis.

## Esconder o ícone por perfil

Na [[wiki/sources/frontpush-dashboards-wireframes-e-fluxos|aula 07 do módulo de dashboards]]: o ícone de administração da sidebar "só vai aparecer para funcionários [...] o sistema verifica o perfil". Padrão certo na interface; a verificação de autorização tem de existir também no servidor.

## Key sources

- [[wiki/sources/kubernetes-security]]
- [[wiki/sources/rbac-abac-rebac]]
- [[wiki/sources/frontpush-dashboards-principios-parte-2]]: FrontPUSH, dashboards aula 05: perfil de usuário e acesso hierárquico
- [[wiki/sources/frontpush-dashboards-levantamento-de-requisitos-dashclass]]: FrontPUSH, dashboards aula 06: perfil × três atores
- [[wiki/sources/frontpush-dashboards-wireframes-e-fluxos]]: FrontPUSH, dashboards aula 07: ícone de ADM só para quem tem perfil
