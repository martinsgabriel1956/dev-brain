---
type: concept
title: "Power Wall"
aliases: ["thermal wall", "barreira de potência", "muro de potência", "fim do escalonamento de Dennard", "Dennard scaling"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 1
tags: [cs-fundamentals, hardware, cpu, frequencia, potencia, dennard-scaling]
skill: cs-fundamentals
status: draft
---

# Power Wall

Limite prático em que subir a frequência de um processador passa a gerar mais calor do que é viável dissipar. Foi o que encerrou a era em que a CPU ficava mais rápida quase de graça, somando [[wiki/concepts/transistor|transistores]] e frequência ([[wiki/sources/por-que-cpus-nao-evoluem-como-antes-power-wall-gpus]]).

## Mecanismo

A potência ativa é proporcional a `C · V² · f` (capacitância, tensão ao quadrado, frequência). [external] Pelo [escalonamento de Dennard](https://en.wikipedia.org/wiki/Dennard_scaling), transistores menores usavam tensão menor, o que mantinha a densidade de potência sob controle. Isso se rompeu por volta de 2005 a 2007, porque corrente de fuga e tensão de limiar não escalam com o tamanho.

A fonte explica só a relação entre frequência e calor. Sem a parte da tensão, não fica claro por que o limite apareceu naquele momento e não antes.

## Data e frequência

| | Fonte | Conferência externa |
|---|---|---|
| **Quando** | "Por 2002, mais ou menos" | [Maio de 2004](https://www.theregister.com/2004/05/07/intel_kills_tejas/): Intel cancela o Tejas; a Wikipedia cita 2005 a 2007 |
| **Frequência atual** | 2 a 3 GHz | [Base de 3,2 a 4,3 GHz, pico de 5,7 a 6,2 GHz](https://hmc-tech.com/cpus/amd-ryzen-9-9950x-vs-intel-core-i9-14900ks) em chips de desktop (agregador de especificações) |

A frequência continuou subindo devagar. O que acabou foi o crescimento acelerado.

## Saídas

- [[wiki/concepts/multicore]]: manter a frequência e multiplicar os núcleos.
- [[wiki/concepts/microarquitetura]]: fazer mais por ciclo.
- [[wiki/concepts/gpu]]: paralelismo massivo em cargas adequadas. A fonte diz que o power wall motivou esse caminho, mas a GPU é anterior ao marco de 2004.

## Relação com outros conceitos

- [[wiki/concepts/lei-de-moore]]: fala de contagem de transistores, não de frequência; a contagem seguiu crescendo depois do power wall.
- [[wiki/concepts/arquitetura-de-computadores]]: área em que esse limite se traduz em decisões de projeto.

## Key sources

- [[wiki/sources/por-que-cpus-nao-evoluem-como-antes-power-wall-gpus]]
