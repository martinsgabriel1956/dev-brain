---
type: concept
title: "Atores do sistema"
aliases: ["ator do sistema", "atores", "actors", "papéis de usuário"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 1
tags: [levantamento-de-requisitos, atores, rbac, modelagem, dashboard, casos-de-uso]
skill: ux-ui-mentor
status: stub
---

# Atores do sistema

Quem opera ou interage com o sistema. Levantar os atores é um dos três produtos do levantamento de requisitos, ao lado dos fluxos e do banco de dados, segundo [[wiki/entities/nasser|Násser]] ([[wiki/sources/frontpush-dashboards-principios-parte-2]]).

- **Pergunta-base:** "quem é que vai operar o sistema?" Funcionário, gerente; "acima do gerente tem alguém? Tem a parte do administrador? Ou então os CEOs, que eles têm outro acesso personalizado?"
- **Em hierarquia:** organizar os atores por nível de acesso já dá "os rabiscos iniciais do sistema para poder definir fluxos".
- **Todos são usuários:** "obrigatoriamente, em todo sistema eu tenho um usuário", e o usuário precisa de um atributo de perfil para o "acesso hierárquico". O comprador também é ator, mesmo "fora dos atores do sistema no quesito administrativo".

## Ressalvas

- Na modelagem de casos de uso (UML), ator é um **papel**, não uma pessoa, e pode ser um sistema externo (gateway de pagamento, emissor de nota fiscal) (alta).
- A hierarquia de atores vira [[wiki/concepts/rbac]]. `[skill: ux-ui-mentor]` A referência `ux-enterprise-b2b.md`: papel = conjunto de permissões, menor privilégio por padrão, permissões aditivas; na UI, esconder o que o usuário nunca poderá fazer ou desabilitar com explicação, e tela 403 com "solicitar acesso".

Relacionado: [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]], [[wiki/concepts/crud]], [[wiki/concepts/autenticacao-e-autorizacao]].

## Key Sources

- [[wiki/sources/frontpush-dashboards-principios-parte-2]]: atores em hierarquia; todos são usuários
