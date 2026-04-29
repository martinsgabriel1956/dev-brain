---
type: concept
title: "Lentes de Código"
aliases: ["vocabulário técnico como ferramenta", "lentes de design", "mental models para código"]
date_created: 2026-04-25
date_updated: 2026-04-25
source_count: 1
tags: [software-design, vocabulario, mental-models, clean-code, fundamentos]
skill: tech-mentor-backend
status: stable
---

# Lentes de Código

Termos técnicos como acoplamento, abstração e estado não são para decorar — são **lentes**: formas diferentes de olhar para o mesmo código que revelam problemas invisíveis a quem não as conhece.

> "Talvez você esteja programando de forma vendado" — sem as lentes, você não consegue avaliar se o código é bom ou apenas funcionante.

## Por que "lentes" e não "regras"

Regras são aplicadas mecanicamente. Lentes mudam a percepção. Quem entende acoplamento *vê* o problema ao ler uma função god. Quem não entende, vê apenas "código que funciona".

## A família de lentes

| Lente | O que revela |
|---|---|
| [[acoplamento]] | Quanto uma mudança em A força mudança em B |
| [[abstracao]] | O que está oculto atrás de um contrato |
| [[estado-compartilhado]] | Quem muta o quê e em que ordem |
| [[coesao]] | Se as responsabilidades dentro de uma unidade fazem sentido juntas |
| [[efeito-colateral]] | O que uma função muda além do que retorna |
| [[imutabilidade]] | Se dados podem ser modificados inesperadamente |
| [[idempotencia]] | Se chamar N vezes tem o mesmo resultado que chamar 1 vez |

## Na era da IA

Modelos de linguagem geram código que funciona na maioria dos casos. O código gerado pode ser altamente acoplado, ter estado compartilhado e zero abstração. Sem essas lentes, você não distingue código bom de código funcionante. Você só descobre o problema quando a próxima mudança quebra tudo.

## Relações

- [[acoplamento]]
- [[abstracao]]
- [[estado-compartilhado]]
- [[coesao]]
- [[efeito-colateral]]
- [[imutabilidade]]
- [[idempotencia]]

## Key sources

- [[wiki/sources/acoplamento-abstracao-estado]]
