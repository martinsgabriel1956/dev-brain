---
type: concept
title: "Redução de Complexidade como Trabalho do Engenheiro"
aliases: ["reduzir complexidade", "simplificar", "complexidade é o inimigo"]
date_created: 2026-09-29
date_updated: 2026-11-25
source_count: 3
tags: [complexidade, engenharia-de-software, simplicidade, design]
skill: tech-mentor-testing
status: stub
---

# Redução de Complexidade como Trabalho do Engenheiro

Tese de [[wiki/sources/como-ser-otimo-programador-sem-usar-o-cerebro]]: engenharia de software é complicada, então a melhor descrição do trabalho é **tornar tudo o mais simples possível** — complexidade é "muito, muito ruim". É nessa parte que se deve realmente usar o cérebro.

Duas vias descritas pela fonte:

1. **Práticas de programação:** código elegante, padrões OOP certos no momento certo, programação funcional quando faz sentido, refatoração, evitar dívida técnica/código espaguete (o artigo só lista; não detalha).
2. **Metodologia de trabalho** (foco do artigo): decompor a tarefa em passos pequenos ([[wiki/concepts/atomic-commits]]), especificar antes de codar ([[wiki/concepts/bdd]]), e concentrar o pensamento no momento certo ([[wiki/concepts/pensar-na-hora-certa]]).

## Ligações

- A distinção clássica entre [[wiki/concepts/complexidade-acidental]] e [[wiki/concepts/essential-complexity]] dá o critério do que *pode* ser reduzido: a fonte não a menciona, então isso é **inferência** desta wiki.
- Dividir uma tarefa grande em etapas menores é chamado pela fonte de "a receita clássica para reduzir complexidade".
- Contraste: [[wiki/concepts/complexidade-como-estrategia]] (complexidade usada como proteção de emprego).

## As duas abordagens de Ousterhout

O cap. 1 de *A Philosophy of Software Design* ([[wiki/sources/filosofia-do-design-de-software-cap-01-traducao-revisada]]) divide o combate à complexidade em duas abordagens. A primeira é **eliminá-la**, deixando o código mais simples e óbvio, por exemplo removendo casos especiais ou usando identificadores de forma consistente. A segunda é **encapsulá-la** com design modular, para que ninguém precise ver toda a complexidade do sistema de uma vez (ver [[wiki/concepts/modulo-profundo]]). Ele também diz que a complexidade sempre cresce. Designs simples não a zeram: eles deixam o sistema crescer mais antes de ela ficar avassaladora. Isso dá mais base à tese desta página, que até aqui tinha uma fonte só.

## Por que encapsular funciona: $C = \sum_p c_p t_p$

O cap. 2 dá a base para a segunda abordagem: a complexidade total é a de cada parte pesada pelo tempo que os desenvolvedores passam nela. Uma parte complicada que quase nunca é tocada pesa pouco, e "isolar a complexidade em um lugar onde ela nunca será vista é quase tão bom quanto eliminá-la" ([[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]]). O mesmo capítulo explica por que a complexidade sempre cresce: ela é [[wiki/concepts/complexidade-incremental|incremental]] e só se segura com "tolerância zero".

## Key Sources

- [[wiki/sources/como-ser-otimo-programador-sem-usar-o-cerebro]]
- [[wiki/sources/filosofia-do-design-de-software-cap-01-traducao-revisada]] — as duas abordagens gerais de Ousterhout: eliminar e encapsular
- [[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]] — fórmula da complexidade ponderada pelo tempo; isolar ≈ eliminar
