---
type: concept
title: "Fluxos bem definidos (uma ação por fluxo)"
aliases: ["fluxo bem definido", "uma tela para cada fluxo", "step by step", "passo a passo", "fluxo com objetivo único"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 2
tags: [ux-design, fluxos, foco, wizard, stepper, dashboard, login]
skill: ux-ui-mentor
status: stub
---

# Fluxos bem definidos (uma ação por fluxo)

Dividir o que o usuário pode fazer em fluxos separados, cada um com um único objetivo, "uma ação no centro da tela" e passos numerados. Para [[wiki/entities/nasser|Násser]], é o segundo princípio de [[wiki/concepts/dashboard|dashboards]]: "não colocar tudo para resolver em uma tela só", porque mesmo com boa [[wiki/concepts/hierarquia-visual]] muitas ações juntas "vão confundir o usuário" ([[wiki/sources/frontpush-dashboards-principios-parte-1]]).

## Como ele aplica

1. **Mapear os fluxos a partir da tela inicial.** No login: sucesso ("o usuário não fez nada de errado", o [[wiki/concepts/caminho-feliz]]), senha errada, esqueci a senha, criar conta, entrar com Google, GitHub ou Facebook. Cada um pode ter subfluxos.
2. **Uma ação por tela, centralizada.** Isolar o fluxo dá à tela "o famigerado foco". Uma tela com várias ações de pesos diferentes é "template de resumo, não é um fluxo": serve para iniciar fluxos, como a home.
3. **Dizer onde o usuário está.** "Step 1", "são quantos passos ao total? São 5." Ver [[wiki/concepts/poder-da-barra-de-progresso-e-do-check]].
4. **Fechar com sucesso ou erro com saída.** "Você concluiu. [...] Cadastrado." Ou "qual que é o erro? Procure o administrador [...] verifique o SMS" ([[wiki/concepts/feedback-do-sistema]]).

No [[wiki/entities/dash-class|DashClass]]: recuperar senha em "passo 1 de 3", por e-mail ou telefone, código de verificação, nova senha e volta à página inicial, com cancelar e voltar em cada passo.

## Ressalvas

`[skill: ux-ui-mentor]` A referência `formularios.md` usa wizard para formulário longo (10+ campos) ou com etapas naturais, e não para o que cabe numa tela. Boas práticas: indicar "Etapa 2 de 4", permitir voltar sem perder dados, salvar ao avançar. Fluxo bem definido não é dividir em muitas telas, e sim não misturar objetivos na mesma.

Relacionado: [[wiki/concepts/carga-cognitiva]], [[wiki/concepts/patterns-de-dashboard]].

## Nomear o fluxo (aula 05)

Na [[wiki/sources/frontpush-dashboards-principios-parte-2|aula 05 do módulo de dashboards]]: "coloque uma ação em cada tela" e saiba nomear o fluxo de forma específica ("recuperar senha por SMS", "por e-mail", "uma venda"). "Quanto mais específico você for, [...] mais direcionado." O custo: "vai ter muita tela", fantástico para a experiência, "mas vai dar muito trabalho".

## Key Sources

- [[wiki/sources/frontpush-dashboards-principios-parte-1]]: definição, o desenho das bolinhas, o fluxo de recuperar senha
- [[wiki/sources/frontpush-dashboards-principios-parte-2]]: FrontPUSH, dashboards aula 05: nomear fluxos; o custo de muitas telas
