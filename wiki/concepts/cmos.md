---
type: concept
title: "CMOS (Complementary Metal-Oxide-Semiconductor)"
aliases: ["CMOS", "circuito complementar", "semicondutor de óxido metálico complementar"]
date_created: 2026-08-25
date_updated: 2026-08-25
source_count: 1
tags: [cs-fundamentals, hardware, cmos, transistor, baixo-consumo]
skill: cs-fundamentals
status: stub
---

# CMOS

Tecnologia de circuito integrado dominante em processadores e memórias modernas, baseada em pares de [[wiki/concepts/transistor|transistores]] tipo N e tipo P com comportamento **complementar** (opostos entre si) — daí o nome "Complementary" MOS.

## Por que a combinação N+P importa

Em cada [[wiki/concepts/celula-padrao|célula padrão]] CMOS, a mesma tensão de entrada controla um transistor tipo N e um tipo P conectados ao gate compartilhado. Como os dois têm resposta oposta à mesma tensão, **exatamente um dos dois conduz a cada momento** — nunca os dois ao mesmo tempo, e nunca nenhum dos dois.

Essa propriedade dá dois benefícios práticos:

1. **Baixo consumo de energia** — se o circuito for projetado corretamente, nunca existe um caminho direto entre o trilho de 1V e o trilho de 0V (terra); só há fluxo de corrente durante a própria comutação de estado, não enquanto o valor permanece estável.
2. **Alta tolerância a ruído** — a lógica de ligado/desligado é mais robusta a pequenas variações de tensão do que topologias que dependem de um único tipo de transistor.

## Exemplo físico: o inversor

O inversor CMOS mais simples usa apenas 2 transistores (1 tipo N + 1 tipo P):

- Entrada 1V → tipo N liga, tipo P desliga → saída puxada para 0V (via trilho de terra)
- Entrada 0V → tipo P liga, tipo N desliga → saída puxada para 1V (via trilho de energia)

Portas mais complexas (NAND, NOR, AND, OR, XOR, XNOR) seguem o mesmo princípio, variando o número de transistores e a topologia série/paralelo de cada grupo N e P. Ver detalhamento em [[wiki/concepts/celula-padrao]].

## Relação com outros conceitos

- [[wiki/concepts/transistor]] — os componentes tipo N e tipo P que este circuito combina
- [[wiki/concepts/celula-padrao]] — a unidade física real construída em topologia CMOS
- [[wiki/concepts/logica-booleana]] — as funções lógicas (AND/OR/NOT/XOR) que circuitos CMOS implementam fisicamente

## Key sources

- [[wiki/sources/como-transistores-formam-portas-logicas-celulas-padrao-cmos]] — definição de CMOS, motivo do nome, e por que a oposição N/P resulta em baixo consumo e alta tolerância a ruído
