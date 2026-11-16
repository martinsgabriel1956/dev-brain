---
type: concept
title: "Paleta de cores"
aliases: ["paleta", "color palette", "esquema de cores", "paleta da marca"]
date_created: 2026-11-14
date_updated: 2026-11-14
source_count: 1
tags: [ui, ui-design, cor, paleta-de-cores, harmonia-de-cores, design-tokens, branding]
skill: ux-ui-mentor
status: stub
---

# Paleta de cores

O conjunto de cores escolhido para uma interface ou marca. Na aula de [[wiki/concepts/harmonia-de-cores]], a harmonia é apresentada como o que "vai meio que introduzir a parte de como fazer uma paleta de cores"; a aula seguinte, ainda não ingerida, trata das paletas e "as principais variações delas" ([[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]]).

## O que a aula adianta

- Paletas têm "quatro cores, com cinco cores, ou apenas com três cores".
- Complementares são "muito utilizadas em paleta de cores" pelo contraste; triádicas são "muito boas para poder criar paleta de cores".
- Referência de paletas prontas: [[wiki/entities/color-hunt]]. Ferramenta para gerar a partir de uma regra: [[wiki/entities/adobe-color]].

## Da paleta ao sistema

`[skill: ux-ui-mentor]` A paleta de 3–5 cores de uma ferramenta de harmonia é o ponto de partida, não o sistema. Em UI, cada cor vira uma escala de primitivos (50–950), mapeada para tokens semânticos (`color-brand-default`, `color-text-secondary`, `color-feedback-error`); componentes usam só os semânticos. As cores de estado vêm de convenção, não da harmonia: ver [[wiki/concepts/cor-semantica]]. A [[wiki/concepts/consistencia-visual]] cita "uma paleta" como exemplo de padrão repetido.

## Key Sources

- [[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]] — harmonia como introdução à paleta; Color Hunt e Adobe Color
