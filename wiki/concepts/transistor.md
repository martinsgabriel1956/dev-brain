---
type: concept
title: "Transistor"
aliases: ["FinFET", "transistor tipo N", "transistor tipo P", "gate/canal/dielétrico"]
date_created: 2026-08-25
date_updated: 2026-08-26
source_count: 2
tags: [cs-fundamentals, hardware, transistor, finfet, cmos]
skill: cs-fundamentals
status: stub
---

# Transistor

Componente eletrônico fundamental de todo circuito digital — a unidade física que liga e desliga a passagem de eletricidade, servindo como o "interruptor" que representa um bit (0 ou 1). Processadores modernos contêm dezenas de bilhões de transistores, fabricados com apenas alguns nanômetros de tamanho.

## Anatomia (formato FinFET)

Um transistor FinFET (nome vindo do formato físico semelhante a uma barbatana/"fin") tem três partes principais:

- **Porta (gate)** — recebe a tensão de controle (0V ou 1V).
- **Canal** — o caminho por onde a eletricidade pode ou não fluir.
- **Dielétrico** — barreira isolante entre porta e canal, que impede a eletricidade de vazar diretamente pela porta.

Contatos metálicos em cada lado do canal e acima da porta se conectam a vias verticais, usadas para entrada e saída de eletricidade.

## Tipo N vs. Tipo P

Os dois tipos de transistor usados em circuitos [[wiki/concepts/cmos|CMOS]] têm comportamento **oposto**:

| Transistor | Gate = 1V | Gate = 0V |
|---|---|---|
| **Tipo N** | Canal conduz (ligado) | Canal isolado (desligado) |
| **Tipo P** | Canal isolado (desligado) | Canal conduz (ligado) |

Analogia da torneira: o tipo N é uma torneira normal (alavanca aberta = água passa); o tipo P é uma torneira "defeituosa" onde a alavanca precisa ser levantada para *fechar* a água.

Ao conectar o gate de um tipo N e de um tipo P na mesma entrada, uma única tensão controla ambos simultaneamente — e como eles são opostos, exatamente um dos dois conduz a cada momento. Essa propriedade é a base de toda [[wiki/concepts/celula-padrao|célula padrão]] CMOS, incluindo o inversor mais simples (2 transistores).

## Velocidade de comutação

A transição de estado de um transistor individual — e a lógica completa de uma [[wiki/concepts/celula-padrao|célula padrão]] simples como o inversor — leva apenas alguns **picossegundos** (10⁻¹² segundos).

## Relação com outros conceitos

- [[wiki/concepts/cmos]] — a topologia complementar (N+P) que usa este componente
- [[wiki/concepts/celula-padrao]] — a menor combinação útil de transistores (inversor = 2, NAND = 4, XOR = 10)
- [[wiki/concepts/sistema-binario-bit-byte]] — o bit físico (0V/1V) que o transistor implementa é a base de toda representação binária
- [[wiki/concepts/logica-booleana]] — as portas AND/OR/NOT que redes de transistores implementam fisicamente
- [[wiki/concepts/ddr-sdram]] — cada célula de DRAM (a base física da RAM) é um único transistor + capacitor por bit; a evolução geracional DDR muda interface/voltagem/frequência, não essa célula elementar

## Key sources

- [[wiki/sources/como-transistores-formam-portas-logicas-celulas-padrao-cmos]] — anatomia do FinFET, comportamento tipo N vs. tipo P, e a analogia "transistor = pino de Lego"
- [[wiki/sources/evolucao-memorias-ram-ddr1-a-ddr5]] — aplicação do transistor como célula de armazenamento em DRAM, contexto da evolução DDR1–DDR5
