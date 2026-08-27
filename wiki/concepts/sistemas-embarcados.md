---
type: concept
title: "Sistemas Embarcados"
aliases: ["embedded systems", "embarcados", "microcontroladores"]
date_created: 2026-08-27
date_updated: 2026-08-27
source_count: 1
tags: [cs-fundamentals, lang-systems, embarcados, hardware, baixo-nivel]
skill: lang-systems
status: stub
---

# Sistemas Embarcados

Programação de dispositivos com hardware e propósito dedicados (microcontroladores, Arduino, ESP), com forte interação a nível de protocolo e eletrônica: muito I/O, atuadores, interrupções customizadas disparadas por leitura de sensores, e necessidade de escrever drivers (ler/escrever em sensores e periféricos). Ver também [[wiki/concepts/rust-embedded|Rust Embedded]] na skill lang-systems para uma abordagem específica em Rust (no_std, HAL, RTIC, Embassy).

## Como porta de entrada para baixo nível

Apontado em [[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]] como uma das duas áreas mais recomendadas para aprender [[wiki/concepts/linguagem-c|programação de baixo nível]] na prática, ao lado de [[wiki/concepts/sistemas-operacionais]]. Diferença central apontada frente a SO: em sistemas operacionais muitas vezes é possível abstrair a arquitetura específica do processador; em embarcados isso não é possível — é preciso conhecer a arquitetura (ver [[wiki/concepts/arquitetura-de-computadores]]) em detalhe, incluindo tabelas de interrupção específicas (ex.: NVIC do ARM — ver [[wiki/concepts/interrupcao-de-hardware]]).

## Projetos práticos sugeridos

A fonte sugere projetos simples com Arduino ou ESP, e cita a intenção de conduzir um projeto combinando embarcados + sistemas operacionais: um SO minimalista escrito em Zig rodando em Arduino/ESP.

## Key sources

- [[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]]
