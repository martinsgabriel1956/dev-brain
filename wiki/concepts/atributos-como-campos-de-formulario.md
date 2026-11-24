---
type: concept
title: "Atributos como campos de formulário"
aliases: ["atributo vira campo", "do banco ao formulário", "campos a partir da modelagem"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 1
tags: [modelagem-de-dados, formularios, levantamento-de-requisitos, dashboard, ui-design]
skill: ux-ui-mentor
status: stub
---

# Atributos como campos de formulário

Ideia de [[wiki/entities/nasser|Násser]] para ligar modelagem e interface: "os atributos, quando a gente traduz para a nossa interface, são os campos. São campos que a gente vai colocar lá nos inputs, nos nossos formulários" ([[wiki/sources/frontpush-dashboards-principios-parte-2]]).

- **Exemplo:** venda = id, id do usuário, id do funcionário, valor, parcelada ou não. Usuário = perfil (para o acesso hierárquico), e-mail (para o código de recuperação de senha), CPF (para a nota fiscal).
- **Os fluxos definem os atributos:** recuperar senha pede e-mail; emitir nota pede CPF. "Você já tem que pensar nos fluxos, nessa etapa inicial, em uma modelagem. Porque senão você vai ter que voltar no processo todas as vezes": esquecer o CPF obriga a mexer no banco e nos campos.
- **Relacionamentos definem o formulário:** uma venda liga um comprador e um funcionário, e isso decide a ordem de cadastro e os filtros ([[wiki/concepts/chave-estrangeira]]).

## Ressalvas

Não é 1:1. Muitos atributos nunca viram campo (ids, datas de auditoria, o funcionário que vem da sessão), e alguns campos não viram atributo (confirmar senha). E nem todo campo vai na mesma tela: pedir o CPF no checkout, quando faz sentido, e não no cadastro, reduz atrito (inferência, alta). Ver [[wiki/concepts/formulario-html]], [[wiki/concepts/modelagem-de-dados]].

## Key Sources

- [[wiki/sources/frontpush-dashboards-principios-parte-2]]: atributos de venda e de usuário; o exemplo do CPF
