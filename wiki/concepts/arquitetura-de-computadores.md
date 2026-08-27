---
type: concept
title: "Arquitetura e Organização de Computadores"
aliases: ["computer architecture", "arquitetura de von neumann", "organização de computadores", "pipeline de execução", "registradores"]
date_created: 2026-08-27
date_updated: 2026-08-27
source_count: 1
tags: [cs-fundamentals, lang-systems, arquitetura, hardware, baixo-nivel]
skill: cs-fundamentals
status: stub
---

# Arquitetura e Organização de Computadores

Área de estudo sobre como o computador funciona em nível conceitual: os componentes internos (CPU, memória, disco) e como se comunicam — não montagem física de hardware, mas o modelo teórico por trás dela. Apontada em [[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]] como a segunda base teórica indispensável para [[wiki/concepts/linguagem-c|programação de baixo nível]], depois de [[wiki/concepts/algoritmos-e-estruturas-de-dados|algoritmos e estruturas de dados]].

## Tópicos centrais

- **Arquitetura de Von Neumann** — modelo de comunicação entre memória de dados, memória de código e CPU.
- **Pipeline de execução** e **caches**.
- **Registradores** — unidades de armazenamento internas da CPU.
- **Interrupções** — ver [[wiki/concepts/interrupcao-de-hardware]], incluindo tabelas de interrupção específicas de arquitetura (ex.: NVIC do ARM).
- **Localidade de memória** — temporal e espacial, relevante para performance em [[wiki/concepts/gerenciamento-de-memoria|gerenciamento de memória]] manual.
- **Branch prediction**.

## Por que importa para quem programa em baixo nível

Segundo a fonte, ninguém programa em baixo nível sem um motivo concreto — sistemas paralelos, [[wiki/concepts/paralelismo|computação de alto desempenho]], [[wiki/concepts/sistemas-embarcados|sistemas embarcados]] ou sistemas críticos — e cada um desses motivos exige, em algum grau, entender arquitetura para de fato exercer controle de baixo nível sobre o hardware. A fonte também associa boa parte dos ataques de **side-channel** (ver [[wiki/concepts/timing-attack]]) a decisões tomadas nesse nível.

## Referências recomendadas

Dois livros de **John Hennessy** e **David Patterson** (Prêmio Turing 2017) são citados como referência canônica em [[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]]: um voltado a nível de mestrado/aprofundamento e outro de nível de graduação, cobrindo a interface hardware/software. Como projeto prático, a fonte sugere construir uma CPU do zero usando linguagens de descrição de hardware (VHDL ou Verilog).

## Key sources

- [[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]]
