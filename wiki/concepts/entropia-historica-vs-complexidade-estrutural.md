---
type: concept
title: "Entropia Histórica vs. Complexidade Estrutural"
aliases: ["entropia histórica", "complexidade estrutural vs entropia", "código feio não é legado", "historical entropy"]
date_created: 2026-10-30
date_updated: 2026-10-30
source_count: 1
tags: [legado, entropia-de-software, modernizacao, cobol, metricas]
skill: tech-mentor-backend
status: draft
---

# Entropia Histórica vs. Complexidade Estrutural

Distinção proposta em [[wiki/sources/spec2cobolrot-envelhecer-cobol-com-ia-complexidade-vs-entropia-historica]]:

- **Complexidade estrutural** é o que métricas capturam: tamanho, [[wiki/concepts/complexidade-ciclomatica]], GO TO, variáveis sobrando, parágrafos mortos. É fácil de fabricar: basta mais linhas, mais desvios incondicionais, mais variáveis.
- **Entropia histórica** é o acúmulo de décadas de regras de negócio (acordo sindical, mudança de lei, decisão judicial, patrocinadora nova, imposto novo) implementadas por pessoas, equipes e empresas diferentes. Cada intervenção foi "localmente justificável": regra nova sem desligar a antiga, variável nova por medo de mexer, `if` hardcoded de madrugada que fica para sempre.

As duas andam juntas no legado real, mas não são a mesma coisa. Um programa pode bater todas as métricas de um legado e ainda não ter a história que o torna difícil de modernizar.

## Evidência

`[external]` No paper Spec2COBOLRot ([[wiki/entities/spec2cobolrot]]), injetar padrões até as métricas estruturais baterem com programas reais produziu código que especialistas acharam "sintético demais". Em escala, o LLM bateu a meta de tamanho duplicando parágrafos parecidos. Os autores concluem que a complexidade estrutural é guiada pela lógica de negócio e por décadas de remendos, e propõem como trabalho futuro simular a história de desenvolvimento.

## Por que importa na modernização

O que trava um projeto de [[wiki/concepts/modernizacao-de-mainframe|modernização]] é a entropia histórica, não o código feio: traduzir a linguagem preserva a estrutura e perde a razão de cada regra. Daí a necessidade de [[wiki/concepts/descoberta-de-regras-de-negocio-legado]] antes de traduzir e o peso do [[wiki/concepts/conhecimento-perdido-em-legado]].

## Relação

- [[wiki/concepts/entropia-de-software]] — o processo; esta página separa o que ele deixa de rastro medível do que não deixa.
- [[wiki/concepts/code-smells]] — sintomas estruturais; não contam a história.
- [[wiki/concepts/teoria-do-programa-naur]] — a "teoria" que se perde é a parte histórica [inferência].

## Key Sources

- [[wiki/sources/spec2cobolrot-envelhecer-cobol-com-ia-complexidade-vs-entropia-historica]]
