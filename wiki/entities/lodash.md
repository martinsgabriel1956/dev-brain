---
type: entity
title: "Lodash"
aliases: ["lodash", "_", "low dash"]
date_created: 2026-11-11
date_updated: 2026-11-11
source_count: 1
tags: [javascript, biblioteca, nodejs, performance]
skill: lang-dynamic
status: stub
---

# Lodash

Biblioteca utilitária de JavaScript, com funções para coleções, objetos e cópia profunda (`_.cloneDeep`, `_.filter`, `_.map`, entre outras).

Em [[wiki/sources/cpu-profiling-nodejs-inspector-autocannon-erick-wendel]], funções do Lodash ocupam o topo do [[wiki/concepts/cpu-profiling|CPU profile]] da rota lenta. O `cloneDeep` respondia por pouco mais de 10% do tempo gravado, e removê-lo levou a rota de 2000 para 11.000 requisições. Trocar `_.filter` pelo `filter` nativo subiu para 13.000; a troca do `map` não mostrou ganho claro. O caso não prova que o Lodash é lento em geral: o custo maior vinha de fazer cópia profunda dos dados a cada requisição. Ver [[wiki/concepts/standard-library-e-ecossistema]].

Outra página que cita o Lodash: [[wiki/concepts/tree-shaking]].

## Key sources

- [[wiki/sources/cpu-profiling-nodejs-inspector-autocannon-erick-wendel]]
