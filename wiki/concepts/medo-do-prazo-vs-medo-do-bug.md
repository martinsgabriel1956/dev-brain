---
type: concept
title: "Medo do Prazo vs. Medo do Bug"
aliases: ["subir assim mesmo", "correr para entregar", "loop prazo-bug"]
date_created: 2026-09-23
date_updated: 2026-09-23
source_count: 2
tags: [qualidade, carreira, entrega, testes, divida-tecnica, dev-junior]
skill: tech-mentor-leadership
status: draft
---

## TL;DR

Erro descrito por [[wiki/entities/andre-casciotti]]: priorizar velocidade de entrega sobre corretude. O tempo ganho é gasto em bugs; o dev acumula [[wiki/concepts/tech-debt]] e a sensação de "só faço entrega ruim" erode a confiança ([[wiki/concepts/confianca-profissional-dev]]). [[wiki/sources/3-erros-que-minam-confianca-como-dev-andre-casciotti]]

## O loop

Correr para mostrar serviço → bug em produção → reclamação → tentar melhorar sem método, perdendo tempo → atraso → bronca → correr de novo.

## Frases-sintoma

- "Vou subir assim mesmo, depois que o teste testar, se vier bug eu corrijo" (empurrar para o QA).
- "Não me dão tempo de fazer direito; a empresa não liga para qualidade."

## Saída proposta

1. **Validar antes de passar adiante** (teste unitário e manual; saber *o que* testa).
2. **Análise de requisitos antes do teste**, senão o teste sai viciado ([[wiki/concepts/requisitos-funcionais-e-nao-funcionais]]).
3. **Identificar código ruim** por conceitos de arquitetura, não por "elegância".
4. **Decidir conscientemente e alinhar** (entregar com dívida ou sem teste completo pode ser válido se comunicado ao time).

[[wiki/sources/3-erros-que-minam-confianca-como-dev-andre-casciotti]]

## Key Sources

- [[wiki/sources/3-erros-que-minam-confianca-como-dev-andre-casciotti]]
- [[wiki/sources/como-ser-dev-essencial-e-ganhar-mais-andre-casciotti]] — visão complementar: entregar no prazo apesar de problemas é valorizado, desde que com consciência e velocidade *com qualidade* ([[wiki/concepts/entregar-apesar-dos-problemas]])
