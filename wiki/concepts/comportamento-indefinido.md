---
type: concept
title: "Comportamento Indefinido (Undefined Behavior)"
aliases: ["undefined behavior", "UB", "comportamento indefinido em C"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [lang-systems, c, undefined-behavior, portabilidade]
skill: lang-systems
status: draft
---

# Comportamento Indefinido (Undefined Behavior)

Casos em que a especificação de [[wiki/concepts/linguagem-c]] não define o resultado. Na leitura do Recursive em [[wiki/sources/por-que-c-e-alto-nivel-abstracao-portabilidade-hardware]], existe **porque C abstrai arquiteturas que se comportam de forma diferente**: ao não fixar o comportamento, deixa cada [[wiki/concepts/compilador]]/hardware agir como for natural — resolveria-se só com uma "arquitetura indiscutivelmente perfeita". É o custo residual da [[wiki/concepts/portabilidade-de-codigo-entre-arquiteturas]]; BCPL → B → C resolveu os problemas "em parte".

[external, não verificado aqui] UB também decorre de licença para otimização do compilador, não só de diferenças de hardware; a explicação da fonte é parcial. É um dos "vários problemas" de C que o apresentador reconhece ao defender melhorias de ecossistema ([[wiki/entities/zig]]).

## Key sources

- [[wiki/sources/por-que-c-e-alto-nivel-abstracao-portabilidade-hardware]]
