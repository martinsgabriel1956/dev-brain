---
type: concept
title: "Programação Tática vs. Estratégica"
aliases: ["programação tática", "programação estratégica", "tactical programming", "strategic programming", "tactical vs strategic programming", "mentalidade de investimento"]
date_created: 2026-11-25
date_updated: 2026-11-26
source_count: 3
tags: [design, ousterhout, tech-debt, programacao-tatica, programacao-estrategica, cultura-de-engenharia]
skill: tech-mentor-backend
status: draft
---

# Programação Tática vs. Estratégica

## TL;DR

São as duas mentalidades com que, segundo [[wiki/entities/john-ousterhout]], se aborda uma tarefa de programação ([[wiki/sources/filosofia-do-design-de-software-cap-03-codigo-funcional-nao-e-suficiente]]). A **tática** quer que a tarefa funcione o mais rápido possível e aceita, a cada vez, uma pequena complexidade ou gambiarra. A **estratégica** trata código que funciona como requisito mínimo: o objetivo é "um excelente design, que por acaso também funciona", porque a maior parte do código futuro vai estender o que existe. A estratégica custa de 10 a 20% a mais no começo e, pela opinião do autor, se paga em 6 a 18 meses.

## Tática

- Imediatista: planejar o futuro não é prioridade.
- Cada concessão parece razoável isoladamente, e é assim que a [[wiki/concepts/complexidade-incremental]] se acumula.
- Se reforça sozinha: quando os atalhos começam a doer, a próxima funcionalidade parece mais urgente que refatorar, e os remendos pedem mais remendos.
- O extremo é o [[wiki/concepts/tornado-tatico]].

## Estratégica

Exige **mentalidade de investimento**, em doses pequenas e contínuas (não um projeto inicial gigante, que seria cascata: [[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental]]).

| Tipo | Exemplos do livro | Na wiki |
|---|---|---|
| Proativo | tentar alternativas de design para cada classe nova; imaginar como o sistema vai mudar; escrever boa documentação | [[wiki/concepts/projetar-duas-vezes]], [[wiki/concepts/comentarios-como-ferramenta-de-design]] |
| Reativo | ao descobrir um erro de design, consertá-lo em vez de ignorar ou remendar | [[wiki/concepts/refatoracao]], [[wiki/concepts/boy-scout-rule]] |

## Quanto investir

- **10 a 20%** do tempo total de desenvolvimento. Em alguns meses o ganho de velocidade cobre os investimentos novos, e eles "se tornam gratuitos".
- **Cruzamento das curvas** (Figura 3.1): entre 6 e 18 meses, porque depois de alguns meses os desenvolvedores esquecem o que tinham em mente e o código complexo passa a custar caro.
- As duas cifras são opinião do autor, que diz não ter dados. A figura é qualitativa.

## Onde a ideia aparece de novo no livro

- **Cap. 16:** ao modificar código existente, ser estratégico é deixar o sistema com a estrutura que teria se tivesse sido projetado com aquela mudança em mente ([[wiki/concepts/refatoracao]]).
- **Cap. 19:** agile focado em funcionalidades, e TDD em especial, pode deslizar para a tática ([[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental]]).

## Relação com outros conceitos

- [[wiki/concepts/tech-debt-como-ferramenta]]: a programação tática é como Ousterhout explica a dívida técnica. Ele é mais restritivo que o quadrante de Fowler: diz que a maior parte da dívida nunca é quitada e não abre exceção para a dívida prudente e deliberada.
- [[wiki/concepts/folga-de-capacidade-slack]]: a folga de ~20% chega a uma proporção parecida por outro caminho (capacidade reservada no time, não investimento embutido em cada tarefa).
- [[wiki/concepts/mvp]] e [[wiki/concepts/lean-startup]]: tensão. O MVP corta escopo; a tática corta cuidado. Um MVP estratégico é possível (leitura da wiki).

## Uso geral como investimento (cap. 6)

[[wiki/sources/filosofia-do-design-de-software-cap-06-modulos-de-proposito-geral-sao-mais-profundos]] compara a abordagem de uso geral com a mentalidade de investimento do cap. 3: um pouco mais de tempo agora para economizar depois (6.1). O autor acrescenta que, no caso da classe de texto, a versão geral nem custa mais: dá menos trabalho e tem menos código. Ver [[wiki/concepts/modulo-de-proposito-geral]].

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-cap-03-codigo-funcional-nao-e-suficiente]]: texto do cap. 3, primeira mão
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]: resumo do cap. 3 e as retomadas nos caps. 16 e 19
- [[wiki/sources/filosofia-do-design-de-software-cap-06-modulos-de-proposito-geral-sao-mais-profundos]] — 6.1: uso geral comparado à mentalidade de investimento
