---
type: concept
title: "Affordance"
aliases: ["affordance em ux", "affordance visual", "signifiers"]
date_created: 2026-07-21
date_updated: 2026-11-13
source_count: 6
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

## Affordance por convenção

Parte das affordances de UI é aprendida, não física: três tracinhos são lidos como menu hambúrguer por hábito ([[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]]). Por isso dependem de [[wiki/concepts/padroes-de-interface|padrões]] estáveis ([[wiki/concepts/lei-de-jakob]]). `[external]` A NN/g registra que o ícone de hambúrguer não é reconhecido por todos ([NN/g, 2016](https://www.nngroup.com/articles/find-navigation-mobile-even-hamburger/)).

## Relação com outros conceitos

- [[wiki/concepts/hierarquia-visual]] — hierarquia atrai a atenção para o elemento certo; affordance confirma que aquele elemento pode (e deve) ser acionado.
- [[wiki/concepts/maquina-de-estados-ui]] — affordance também deveria refletir o estado atual do componente (ex.: botão desabilitado deve parecer visualmente diferente de um botão clicável).
- [[wiki/concepts/design-como-interacao]] — affordance é um dos elementos que compõem o design como experiência de uso, não só aparência.

## Botão não é link

[[wiki/sources/elementos-da-interface-introducao-ui-design]]: "o botão sempre está ligado à ação que o usuário tem que tomar, link é diferente de botão". `[skill: ux-ui-mentor]` Um botão deve parecer clicável e um link deve se distinguir do texto estático; no código, `<button>` para ação e `<a href>` para navegação. Ver [[wiki/concepts/elementos-da-interface]].

## Link se sinaliza

Na visão geral dos elementos: link azul se reconhece "de cara", texto branco "é literalmente texto"; "onde tem link eu tenho que saber sinalizar" ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]). `[external]` Pela WCAG 1.4.1, a cor sozinha não basta: precisa de 3:1 com o texto em volta e outro sinal no foco ou hover. Ver [[wiki/concepts/cor-semantica]].

## Hover como sinal de clicável

Em [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]: quando a área clicável "reage a eu passar o mouse", o usuário entende que é clicável e fica "mais instigado em clicar". Links do menu da [[wiki/entities/apple]] dão "a resposta à interação". `[skill: ux-ui-mentor]` Hover não existe no toque: o sinal de clicável precisa estar no repouso (forma, cor, label), e o hover só confirma. Ver [[wiki/concepts/botoes-em-interfaces]].

## Diagonal e seta como direção

O botão em diagonal "dá a sensação de direção, de vai", e costuma vir com "uma setinha [...] para poder melhorar a comunicação" ([[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]]). Ver [[wiki/concepts/formas-de-botoes]].

## Key Sources

- [[wiki/sources/5-boas-praticas-uiux-ux-pilot]]
- [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]] — ícone de hambúrguer como affordance por convenção
- [[wiki/sources/elementos-da-interface-introducao-ui-design]] — botão ligado à ação, link é outra coisa
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — link distinguível do texto pela cor
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — hover como resposta que indica clicável; link branco x texto cinza
- [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]] — botão diagonal + seta sinaliza direção
