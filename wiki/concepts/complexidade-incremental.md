---
type: concept
title: "Complexidade Incremental"
aliases: ["complexity is incremental", "a complexidade é incremental", "tolerância zero à complexidade", "zero tolerance"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 2
tags: [complexidade, design, ousterhout, tech-debt, entropia]
skill: tech-mentor-backend
status: draft
---

# Complexidade Incremental

## TL;DR

A complexidade não nasce de um erro catastrófico. Ela se acumula em centenas ou milhares de pequenas dependências e obscuridades ([[wiki/concepts/causas-de-complexidade-ousterhout]]), até que qualquer mudança esbarre em várias delas. Por isso a resposta de [[wiki/entities/john-ousterhout]] é "tolerância zero": não aceitar nem a pequena complexidade da mudança atual ([[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]], seção 2.4).

## Por que é difícil de controlar

1. **Na entrada:** é fácil se convencer de que um pouco de complexidade na mudança atual "não é nada demais". Se todos pensam assim a cada mudança, ela se acumula rápido.
2. **Na saída:** depois de acumulada, remover uma dependência ou obscuridade isolada não muda quase nada. Não existe a correção única que resolve.

A assimetria é o argumento: o custo de cada concessão é invisível na hora e o custo de desfazer o acúmulo é alto. Só a disciplina na entrada funciona.

## Relação com outros conceitos

- [[wiki/concepts/programacao-tatica-vs-estrategica]] e [[wiki/concepts/tech-debt-como-ferramenta]]: o cap. 3 transforma a "tolerância zero" em mentalidade (programação estratégica, 10–20% do tempo em design). A programação tática é exatamente o hábito de aceitar cada pequena concessão.
- [[wiki/concepts/entropia-de-software]]: mesmo fenômeno visto de outro jeito. A entropia é descrita como tendência natural, quase física, de degradação. Para Ousterhout o acúmulo é a soma de **escolhas** individuais, e por isso evitável. As duas leituras levam à manutenção contínua (refatorar sempre, corrigir o design assim que o problema aparece), mas a de Ousterhout põe a responsabilidade em quem faz cada mudança (contraste da wiki).
- [[wiki/concepts/reducao-de-complexidade]]: a 2.4 explica por que o cap. 1 diz que a complexidade sempre cresce. Design simples não zera o crescimento, só o desacelera.

## A mesma dinâmica no cap. 3

A 3.1 mostra o mecanismo em ação: cada tarefa tática acrescenta algumas complexidades, os remendos pedem mais remendos, e quando a bagunça fica grande corrigir um ou dois problemas "não parece fazer muita diferença". A 3.5 dá a versão de comportamento: adiar a limpeza "até o aperto acabar" vira adiamento permanente, porque depois de uma crise vem outra ([[wiki/sources/filosofia-do-design-de-software-cap-03-codigo-funcional-nao-e-suficiente]], [[wiki/concepts/programacao-tatica-vs-estrategica]]).

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]]: seções 2.4 e 2.5
- [[wiki/sources/filosofia-do-design-de-software-cap-03-codigo-funcional-nao-e-suficiente]]: seções 3.1 e 3.5, o acúmulo visto pela mentalidade tática
