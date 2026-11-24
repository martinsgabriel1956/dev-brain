---
type: concept
title: "Modo escuro (dark mode)"
aliases: ["dark mode", "modo dark", "tema escuro", "dark theme"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 1
tags: [ui-design, tema, cores, contraste, acessibilidade, design-system, dashboard]
skill: ux-ui-mentor
status: stub
---

# Modo escuro (dark mode)

Tema de interface com fundos escuros e texto claro. O [[wiki/entities/dash-class|DashClass]] é todo em modo escuro: [[wiki/entities/nasser|Násser]] levou a questão ao cliente e decidiu implementar "por ser uma plataforma de vídeos em que a pessoa está sempre olhando [...] horas e horas", porque "pode ficar mais confortável os olhos" ([[wiki/sources/frontpush-dashboards-wireframes-e-fluxos]]).

## O que sustenta (e o que não)

- `[external]` Os estudos de polaridade resumidos pela Nielsen Norman Group (2020) indicam que texto escuro sobre claro é lido com mais precisão por quem tem visão normal; o escuro ajuda em pouca luz e para parte das pessoas com baixa visão (média-alta, sem fetch). "Cansa menos a vista" não é regra geral.
- Para vídeo, o argumento mais forte é a convenção de cinema: o fundo escuro some ao redor do player e não compete com a imagem, como em [[wiki/entities/netflix|Netflix]] e YouTube (inferência, alta).

## Como fazer

`[skill: ux-ui-mentor]` Referência `design-system.md`: dark mode "não é inverter as cores", é um tema com decisões próprias, de preferência por tokens semânticos.

- Evitar preto puro no fundo e branco puro no texto (contraste excessivo, ofuscamento).
- Superfícies em camadas: fundo < superfície < card, cada uma um pouco mais clara.
- Sombras somem no escuro: usar bordas sutis.
- Respeitar a preferência do sistema (`prefers-color-scheme`) e oferecer a troca.

Relacionado: [[wiki/concepts/contraste]], [[wiki/concepts/luminosidade-das-cores]] (fundos escuros "nunca é um preto puro", na mentoria de UI Design), [[wiki/concepts/cor-semantica]].

## Key Sources

- [[wiki/sources/frontpush-dashboards-wireframes-e-fluxos]]: o DashClass em modo escuro e o motivo dado
