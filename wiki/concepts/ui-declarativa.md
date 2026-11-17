---
type: concept
title: "UI declarativa vs. imperativa"
aliases: ["abordagem declarativa", "interface declarativa", "UI = f(state)", "programação declarativa de interfaces"]
date_created: 2026-11-17
date_updated: 2026-11-17
source_count: 1
tags: [frontend, react, declarativo, imperativo, virtual-dom, dom]
skill: tech-mentor-frontend
status: stub
---

# UI declarativa vs. imperativa

- **Imperativa:** o código diz *como* mudar a tela, passo a passo: selecionar o elemento, criar o nó, trocar a classe ([[wiki/concepts/dom]], [[wiki/concepts/criacao-de-elementos-dom]]).
- **Declarativa:** o código diz *o que* a tela deve ser para um estado, e o framework calcula as mudanças. No [[wiki/entities/react]], `UI = f(state)`: o componente devolve JSX a partir de props e estado ([[wiki/concepts/jsx]]).

Atualizar só o que mudou é **consequência** do mecanismo que torna o declarativo viável, não a definição dele: no React, [[wiki/concepts/virtual-dom]] mais [[wiki/concepts/reconciliacao]]; no Svelte, compilação; no Solid, sinais ([[wiki/concepts/signals]]). `[skill: tech-mentor-frontend]`

O mesmo par existe fora do front: [[wiki/concepts/infraestrutura-declarativa]] (Terraform descreve o estado final).

## Nas fontes

- [[wiki/sources/frontpush-conceitos-gerais-react-interface-dinamica-spa-virtual-dom-jsx]]: [[wiki/entities/nasser]] define a abordagem declarativa como "atualiza apenas os componentes necessários" (chat do Facebook). É o efeito, não a definição.
- A NLW #2 descreve o lado imperativo pelo contraste: "a gente não vai no HTML [...] e adiciona uma nova div", como no jQuery (ver [[wiki/entities/react]]).

## Related

- [[wiki/concepts/virtual-dom]]
- [[wiki/concepts/reconciliacao]]
- [[wiki/concepts/componentizacao]]
- [[wiki/concepts/infraestrutura-declarativa]]

## Key Sources

- [[wiki/sources/frontpush-conceitos-gerais-react-interface-dinamica-spa-virtual-dom-jsx]]: FrontPUSH, React aula 03: "abordagem declarativa" no slide de SPA
