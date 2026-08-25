---
type: concept
title: "Célula Padrão (Standard Cell)"
aliases: ["standard cell", "célula macro", "macro cell", "porta lógica física", "hierarquia de chip"]
date_created: 2026-08-25
date_updated: 2026-08-25
source_count: 1
tags: [cs-fundamentals, hardware, celula-padrao, celula-macro, arquitetura-de-processador, cmos]
skill: cs-fundamentals
status: stub
---

# Célula Padrão (Standard Cell)

A unidade física fundamental de todo processador e GPU: um pequeno grupo de [[wiki/concepts/transistor|transistores]] conectados por uma camada de fios chamada **interconexões locais**, implementando uma única [[wiki/concepts/logica-booleana|porta lógica]]. É a estrutura real que existiria fisicamente se fosse possível dar zoom nanoscópico num chip.

Analogia didática (Branch Education): se um transistor é um pino de Lego, uma célula padrão é uma peça de Lego montada a partir de vários pinos.

## Exemplos por número de transistores

| Porta | Transistores | Topologia |
|---|---|---|
| Inversor (NOT) | 2 (1 tipo N + 1 tipo P) | Gates compartilhados |
| NAND | 4 | 2 tipo P em paralelo (acima) + 2 tipo N em série (abaixo) |
| AND | NAND + inversor na saída | mais cara que NAND — por isso processadores preferem NAND |
| NOR | 4 | topologia invertida da NAND (P em série, N em paralelo) |
| OR | NOR + inversor na saída | |
| XOR / XNOR | 10 cada | lógica "exatamente uma entrada ativa" exige mais transistores |

Todo o circuito segue a topologia [[wiki/concepts/cmos|CMOS]]: para a saída de uma NAND ser 0, ambas as entradas devem ser 1 (liga os dois tipo N em série); para ser 1, basta uma entrada ser 0 (liga um dos tipo P em paralelo).

## Hierarquia: de célula padrão a chip completo

A analogia de Lego se estende para toda a escala de um processador:

```
transistor (pino de Lego)
  → célula padrão (peça de Lego)     — 2 a 10 transistores, ligados por interconexões locais
    → célula macro (conjunto de Lego) — centenas a milhares de células padrão, ligadas pela camada M1
      → núcleo IP
        → núcleo / acelerador de hardware
          → chip completo (processador)
```

Exemplos concretos de célula macro:

- **Somador de 32 bits**: ~160 células padrão.
- **Multiplicador de 32 bits**: ~6.100 células padrão — complexidade comparável ao conjunto LEGO Millennium Falcon (~7.500 peças).

Processadores reais usam cerca de **17 camadas metálicas** de fios (muito além da única camada M1 do exemplo didático) para conectar toda essa hierarquia, chegando a dezenas de bilhões de transistores no chip completo.

## Velocidade

Cada célula padrão comuta em poucos [[wiki/concepts/transistor|picossegundos]]; uma célula macro inteira (ex.: o multiplicador de 6.100 células) completa toda sua lógica em ~150–200 picossegundos entre a chegada da entrada e a estabilização da saída.

## Relação com outros conceitos

- [[wiki/concepts/transistor]] — o componente que a célula padrão organiza em pequenos grupos
- [[wiki/concepts/cmos]] — a topologia elétrica (N+P complementar) usada em toda célula padrão
- [[wiki/concepts/logica-booleana]] — cada célula padrão implementa fisicamente uma porta lógica (AND/OR/NOT/XOR/NAND/NOR)
- [[wiki/concepts/sistema-binario-bit-byte]] — a saída de uma célula padrão é sempre 0V ou 1V, o bit físico

## Key sources

- [[wiki/sources/como-transistores-formam-portas-logicas-celulas-padrao-cmos]] — anatomia de inversor/NAND/AND/NOR/OR/XOR/XNOR em transistores, e a hierarquia célula padrão → célula macro → núcleo IP → chip
