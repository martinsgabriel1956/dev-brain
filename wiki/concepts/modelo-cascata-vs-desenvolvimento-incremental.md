---
type: concept
title: "Modelo Cascata vs. Desenvolvimento Incremental"
aliases: ["waterfall", "waterfall model", "agile design", "design incremental"]
date_created: 2026-07-10
date_updated: 2026-07-29
source_count: 2
tags: [waterfall, agile, design, processo, ousterhout, complexidade]
skill: tech-mentor-backend
status: draft
---

# Modelo Cascata vs. Desenvolvimento Incremental

## TL;DR

Modelo cascata (waterfall): projeto dividido em fases discretas e sequenciais (requisitos → design → codificação → testes → manutenção), com o design congelado ao final da fase de design. Desenvolvimento incremental (ágil): o design foca em um pequeno subconjunto da funcionalidade por vez, é implementado, avaliado, e o próximo subconjunto se beneficia dos problemas descobertos no anterior.

## Por que o cascata falha estruturalmente para software

Segundo [[wiki/entities/john-ousterhout]], o cascata funciona em engenharia física (prédios, navios, pontes) porque é possível visualizar o design inteiro antecipadamente. Software é intrinsecamente mais complexo — não dá para visualizar todas as implicações de um design grande antes de construir algo. O resultado: os problemas do design inicial só aparecem quando a implementação já está avançada, mas o modelo cascata não tem mecanismo para revisar o design nesse ponto (os designers já passaram para outros projetos). Desenvolvedores então remendam os problemas sem mudar o design geral — o que causa explosão de complexidade.

## Por que o incremental funciona especificamente para software

Software é maleável o suficiente para permitir mudanças de design significativas no meio da implementação — uma propriedade que sistemas físicos não têm (não é prático mudar o número de torres de uma ponte no meio da construção). Cada iteração expõe problemas do design existente antes do próximo conjunto de features ser projetado; problemas do design inicial são corrigidos enquanto o sistema ainda é pequeno.

Consequência: **design de software nunca termina**. É um processo contínuo ao longo de toda a vida do sistema, o que implica redesign contínuo — o design inicial de um componente quase nunca é o melhor possível, e desenvolvedores devem planejar gastar uma fração do tempo em melhorias de design, não tratar design como fase concluída.

## Relação com outros conceitos

- [[wiki/concepts/modulo-profundo]] — a estratégia de encapsulamento (design modular) que este texto introduz como uma das duas formas gerais de combater complexidade; módulos profundos são o desenvolvimento detalhado dessa estratégia.
- [[wiki/concepts/accidental-complexity]] — a "explosão de complexidade" do cascata remendado é um exemplo direto de complexidade acidental se acumulando por falta de revisão de design.
- [[wiki/concepts/arquitetura-de-software]] — decisão arquitetural via cascata (congelada cedo) vs. via incremental (revisada continuamente) é uma tensão central de como estruturar processos de arquitetura.

## Agile como incremental "por feature", não por abstração — risco de virar tático

[[wiki/sources/filosofia-do-design-de-software-livro-completo]] (Cap. 19) qualifica a defesa do incremental feita no capítulo 1: concorda que agile (incremental e iterativo) é compatível com o argumento contra o cascata, mas aponta um risco — agile foca desenvolvedores em features, não em abstrações, e encoraja adiar decisões de design para entregar software funcionando o quanto antes. Isso pode deslizar para [[wiki/concepts/tech-debt-como-ferramenta|programação tática]] se levado ao extremo. A régua do autor: os incrementos de desenvolvimento deveriam ser **abstrações**, não features — é aceitável adiar todo pensamento sobre uma abstração até que uma feature precise dela, mas quando a abstração é necessária, vale investir tempo para desenhá-la de forma limpa de uma vez (ver [[wiki/concepts/projetar-duas-vezes]]), não construí-la aos pedaços ao longo de várias features. TDD é citado como o exemplo mais extremo desse risco: "test-driven development is tactical programming pure and simple" — foca em fazer o próximo teste passar, não em achar o melhor design.

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-introducao]]
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — qualificação do agile/TDD como risco de deslizar para o tático (Cap. 19)
