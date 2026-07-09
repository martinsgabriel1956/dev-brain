---
type: entity
title: "John Ousterhout"
aliases: ["ousterhout", "philosophy of software design"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [autor, complexidade, arquitetura, deep-modules, professor]
skill: tech-mentor-backend
status: stub
---

## Quem É

Professor de ciência da computação em Stanford, criador da linguagem Tcl, e autor de *A Philosophy of Software Design* (2018) — livro que define complexidade de software e propõe módulos profundos como estratégia central de design.

## Contribuições relevantes para o wiki

**Definição de complexidade:** "qualquer coisa relacionada à estrutura de um sistema de software que dificulta entender e modificar o sistema". Uma base de código ruim, por essa definição, é simplesmente uma base de código difícil de mudar sem causar bugs.

**Módulos profundos (deep modules) vs. módulos rasos (shallow modules):** módulos profundos escondem muita funcionalidade atrás de uma interface simples — a complexidade fica encapsulada, o consumidor não precisa (mas pode) olhar por dentro. Módulos rasos expõem pouca funcionalidade atrás de uma interface relativamente complexa — multiplicam o número de peças que quem lê o código precisa rastrear. Ver [[wiki/concepts/modulo-profundo]].

## Relevância na era da IA

Citado em [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] como base teórica para dois problemas de agentes de IA: (1) LLMs tendem a produzir código com módulos rasos por padrão, o que dificulta a própria IA explorar e entender a base de código depois; (2) módulos profundos permitem tratar a implementação como "caixa cinza" — o humano projeta e revisa a interface, delega a implementação à IA, sem precisar acompanhar cada linha.

## Key Sources

- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
