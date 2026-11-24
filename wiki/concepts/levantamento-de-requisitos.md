---
type: concept
title: "Levantamento de requisitos"
aliases: ["levantar requisitos", "elicitação de requisitos", "requirements elicitation", "reunião de requisitos"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 3
tags: [levantamento-de-requisitos, reuniao-com-cliente, atores-do-sistema, modelagem-de-dados, dashboard, ux-design]
skill: ux-ui-mentor
status: stub
---

# Levantamento de requisitos

Descobrir, com o cliente e os usuários, o que o sistema precisa fazer e com que qualidades, antes de desenhar telas. No módulo de dashboards do [[wiki/entities/frontpush|FrontPUSH]], [[wiki/entities/nasser|Násser]] o trata como assunto que "tanto designer como desenvolvedores precisam saber" ([[wiki/sources/frontpush-dashboards-principios-parte-2]]) e o aplica ao [[wiki/entities/dash-class|DashClass]] ([[wiki/sources/frontpush-dashboards-levantamento-de-requisitos-dashclass]]).

## O roteiro dele

1. **Entender o negócio:** "uma conversa franca com o dono do negócio". Perguntas: "como é que vocês pensam de fazer isso? Qual a estrutura que vocês já têm? Qual é a experiência de vocês com relação a isso?"
2. **Avaliar viabilidade na hora:** "é possível, não é possível? Dou conta, não dou conta?"
3. **Abstrair e anotar:** [[wiki/concepts/requisitos-funcionais-e-nao-funcionais|requisitos funcionais e não funcionais]], [[wiki/concepts/atores-do-sistema|atores]] em hierarquia, entidades com [[wiki/concepts/crud|CRUD]], [[wiki/concepts/atributos-como-campos-de-formulario|atributos]] e relacionamentos ([[wiki/concepts/modelagem-de-dados]]).
4. **Voltar com as dúvidas:** desenhando, "vai aparecer algumas dúvidas", e "em uma segunda oportunidade" se tira com o cliente ([[wiki/concepts/workflow-de-reunioes-do-freela]]).
5. **Só então** [[wiki/concepts/patterns-de-dashboard|patterns]] e [[wiki/concepts/wireframe|wireframes]].

Regra prática dele: "cada ator que tem no sistema aumenta drasticamente a quantidade de telas, a quantidade de relacionamentos".

## Ressalvas

- `[skill: ux-ui-mentor]` A referência `pesquisa.md` prefere perguntas abertas sobre comportamento real ("me conta como você acompanha o progresso dos seus alunos hoje") a perguntas sobre solução ("você gostaria de uma feature de..."). O dono do negócio fala de objetivos; os usuários, do uso real ([[wiki/concepts/pesquisa-com-usuario]]).
- O cliente pede o quê ("quero gamificação"); o como é trabalho do designer, como o próprio Násser diz.
- Ver também [[wiki/concepts/briefing]], a versão freela da mesma conversa.

## Depois do levantamento (aula 07)

Na [[wiki/sources/frontpush-dashboards-wireframes-e-fluxos|aula 07 do módulo de dashboards]]: completar as anotações "com o máximo possível de informações", tirar dúvidas "até chegar em um consenso", e então abstrair em telas, conteúdo e fluxos, ticando cada requisito ([[wiki/concepts/rastreabilidade-de-requisitos]]).

## Key Sources

- [[wiki/sources/frontpush-dashboards-principios-parte-2]]: método (requisitos, atores, entidades, CRUD)
- [[wiki/sources/frontpush-dashboards-levantamento-de-requisitos-dashclass]]: aplicação ao DashClass e roteiro da reunião
- [[wiki/sources/frontpush-dashboards-wireframes-e-fluxos]]: FrontPUSH, dashboards aula 07: completar, consensuar, ticar
