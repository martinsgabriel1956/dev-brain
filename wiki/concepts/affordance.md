---
type: concept
title: "Affordance"
aliases: ["affordance em ux", "affordance visual", "signifiers"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [ui, ux, design, frontend, affordance]
skill: tech-mentor-frontend
status: draft
---

# Affordance

Propriedade visual ou interativa de um elemento que sugere, por si só, como ele deve ser usado — guiando o usuário através das ações de forma intuitiva, sem exigir uma curva de aprendizado. O conceito se aplica tanto a elementos de tela quanto a objetos físicos (um botão de controle remoto sugere clique; um knob sugere giro; um switch sugere puxar).

## Exemplos em UI

| Elemento | Affordance sugerida |
|---|---|
| Botão com sombra/relevo | Clicável, muda de estilo ao pressionar |
| Switch (toggle) | Arrastar/clicar para ligar-desligar |
| Bolinha sobre uma linha (slider) | Arrastar |
| Campo com cursor piscando | Clicar e digitar |
| Ícone de microfone | Falar em vez de digitar |
| Link sublinhado | Clicável, leva a outro lugar |

## Falhas comuns em UI gerada por IA

Interfaces geradas rapidamente por IA frequentemente omitem sinais de affordance básicos:

- Ausência de `cursor: pointer` em botões e elementos clicáveis.
- Ausência de `:hover` (mudança de cor, glow) em botões.
- Ausência de sublinhado (ou outro sinal visual) em links.

Esses detalhes são baratos de implementar e têm efeito direto na capacidade do usuário de entender o que é interativo na tela sem precisar testar cada elemento por tentativa e erro.

## Affordance vs. reforço de continuidade

Nem todo elemento visual adicional é, estritamente, uma affordance. Um exemplo citado: adicionar uma seta num CTA não é necessário para indicar que o botão é clicável (o próprio estilo do botão já faz isso) — mas reforça a sensação de que a ação leva a uma próxima etapa (continuidade do fluxo), o que é um reforço complementar à affordance, não a affordance em si.

## Relação com outros conceitos

- [[wiki/concepts/hierarquia-visual]] — hierarquia atrai a atenção para o elemento certo; affordance confirma que aquele elemento pode (e deve) ser acionado.
- [[wiki/concepts/maquina-de-estados-ui]] — affordance também deveria refletir o estado atual do componente (ex.: botão desabilitado deve parecer visualmente diferente de um botão clicável).
- [[wiki/concepts/design-como-interacao]] — affordance é um dos elementos que compõem o design como experiência de uso, não só aparência.

## Key Sources

- [[wiki/sources/5-boas-praticas-uiux-ux-pilot]]
