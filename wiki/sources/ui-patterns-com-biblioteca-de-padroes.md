---
type: source
title: "UI-Patterns.com — biblioteca de padrões de UI e persuasivos"
aliases: ["ui-patterns.com", "ui patterns library", "biblioteca de padrões de ui"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ux, design, padroes-de-interface, design-persuasivo, onboarding, navegacao, gamificacao, vieses-cognitivos, referencia]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/ui-patterns-com-biblioteca-de-padroes.md"
source_url: "https://ui-patterns.com/patterns"
author: "Learning Loop ApS (UI-Patterns.com)"
date_published: ""
date_ingested: 2026-11-13
---

# UI-Patterns.com — biblioteca de padrões de UI e persuasivos

## TL;DR

Página-índice do [[wiki/entities/ui-patterns-com|UI-Patterns.com]], catálogo mantido desde 2007 pela Learning Loop ApS. Divide-se em duas metades: **padrões de UI** (soluções recorrentes para problemas comuns: entrada de dados, onboarding, navegação, dados, social, compras) e **padrões persuasivos** (estratégias baseadas em psicologia para conduzir o usuário: cognição, mecânicas de jogo, percepção e memória, feedback, vieses sociais). A tese da introdução é a mesma de [[wiki/concepts/design-patterns]] em software: padrões dão uma **linguagem comum**, e nomear um padrão carrega o problema, o contexto e as alternativas. Indicada na aula [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]] como referência de [[wiki/concepts/padroes-de-interface]].

## Key Claims

- **Definição.** Padrões de UI são "soluções recorrentes que resolvem problemas comuns de design" e pontos de referência para o designer experiente. Ver [[wiki/concepts/padroes-de-interface]].
- **Linguagem comum.** Nomear um padrão diz mais que o nome e permite debater alternativas. É a ideia de [[wiki/entities/christopher-alexander]] que também originou [[wiki/concepts/design-patterns]] em software.
- **Persuasão como categoria própria.** Os padrões persuasivos guiam o usuário a resultados pretendidos, "alinhados" ao objetivo da organização e ao valor para o usuário. Ver [[wiki/concepts/design-persuasivo]].
- **Organização do catálogo** (só nomes e links na página; descrições ficam em cada padrão):

| Metade | Categoria | Exemplos |
|---|---|---|
| UI | Obter entrada de dados | Forgiving Format, Good Defaults, Undo, Wizard, Steps Left |
| UI | Onboarding | Lazy Registration, Guest Access, Blank Slate, Coachmarks, Paywall, Cancellation Flow |
| UI | Navegação | Breadcrumbs, Fat Footer, Modal, Progressive Disclosure, Continuous Scrolling |
| UI | Lidar com dados | Table Filter, Dashboard, Autocomplete, Search Filters |
| UI | Social / Diversos | Testimonials, Activity Stream, Shopping Cart, Pricing table |
| Persuasivo | Cognição | Loss Aversion, Decoy Effect, Sunk Cost, Peak-end rule, Scarcity |
| Persuasivo | Mecânicas de jogo | Variable Rewards, Goal-Gradient Effect, Achievements, Levels |
| Persuasivo | Percepção e memória | Isolation Effect, Zeigarnik Effect, Chunking, Recognition over Recall, Pattern Recognition |
| Persuasivo | Feedback | Kairos, Feedback Loops, Trigger |
| Persuasivo | Social | Social Proof, Authority Bias, Reciprocation, Commitment & Consistency |

- **Padrões que a aula já usa sem nomear:** Isolation Effect (o azul isolado no CTA da landing page, ver [[wiki/concepts/contraste]]); Pattern Recognition e Recognition over Recall (busca no topo, ícone de hambúrguer, ver [[wiki/concepts/lei-de-jakob]]); Shopping Cart e Steps Left (jornada de e-commerce); Dashboard (tela lotada como exemplo de UI ruim).
- **Inclui padrões recentes de IA:** Suggested Prompts, Refinement Controls, Source Citations, na seção de onboarding.

## Entities

- [[wiki/entities/ui-patterns-com]] — o site e a Learning Loop ApS.
- [[wiki/entities/christopher-alexander]] — origem da ideia de linguagem de padrões (ligação feita pela wiki, não pela página).

## Concepts

- [[wiki/concepts/padroes-de-interface]] (novo)
- [[wiki/concepts/design-persuasivo]] (novo)
- [[wiki/concepts/design-patterns]]
- [[wiki/concepts/pattern-recognition]]
- [[wiki/concepts/hierarquia-visual]]

## Observações da leitura

- O título diz "170 padrões", mas a contagem da listagem dá cerca de 199 entradas (120 de UI, 79 persuasivos). "Social" aparece nas duas metades. A página não explica a diferença.
- A página não traz data de atualização; o copyright vai de 2007 a 2026.
- `[skill: ux-ui-mentor]` Persuasão sem limite vira dark pattern. Escassez e Loss Aversion são as categorias mais usadas de forma manipuladora (contador falso, "só restam 2"). A página afirma o alinhamento com o valor do usuário, mas não define a fronteira.

## Open Questions

- Onde fica a linha entre padrão persuasivo e dark pattern? Vale ingerir a seção de ética da skill ou um texto dedicado (Harry Brignull, deceptive.design).
- Quais páginas individuais valem ingestão própria? Candidatas: Isolation Effect, Recognition over Recall, Forgiving Format, Lazy Registration.
