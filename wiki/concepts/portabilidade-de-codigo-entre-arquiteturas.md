---
type: concept
title: "Portabilidade de Código entre Arquiteturas"
aliases: ["interoperabilidade de arquitetura", "compile once, target many", "portabilidade de C"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [lang-systems, portabilidade, compiladores, historia, c]
skill: lang-systems
status: draft
---

# Portabilidade de Código entre Arquiteturas

Poder pegar o **mesmo programa** e compilá-lo para máquinas/[[wiki/concepts/isa-instruction-set-architecture|ISAs]] diferentes. Para o apresentador de [[wiki/sources/por-que-c-e-alto-nivel-abstracao-portabilidade-hardware]] é *o* ganho central do [[wiki/concepts/alto-nivel-vs-baixo-nivel|alto nível]] e foi **revolucionário**: antes, mudar de fabricante significava reescrever o programa (ou ter um tradutor) e o fabricante distribuía dialetos e compiladores próprios (BCPL, PL/M). Com [[wiki/concepts/linguagem-c]] como "dialeto universal", cada arquitetura tem um [[wiki/concepts/compilador]] e o ideal é **corrigir uma vez, corrigir para todos** — o peso sai do fabricante e vai para o compilador.

Preço: ao se afastar do hardware, a linguagem precisa de conceitos abstratos (funções, ponteiros, unions) e herda [[wiki/concepts/comportamento-indefinido]]. Para o que não é portável, mistura-se [[wiki/concepts/assembly]]. Interface binária comum: [[wiki/concepts/abi]] (a de C é a "universal"). Origem histórica: [[wiki/concepts/dependencia-de-caminho-em-tecnologia]].

## Key sources

- [[wiki/sources/por-que-c-e-alto-nivel-abstracao-portabilidade-hardware]]
