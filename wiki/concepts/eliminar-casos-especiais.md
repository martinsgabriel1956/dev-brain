---
type: concept
title: "Eliminar Casos Especiais"
aliases: ["eliminate special cases", "elimine casos especiais", "casos especiais", "special cases", "caso normal trata o contorno"]
date_created: 2026-11-26
date_updated: 2026-11-26
source_count: 2
tags: [design, ousterhout, casos-especiais, simplicidade, especializacao]
skill: tech-mentor-backend
status: draft
---

# Eliminar Casos Especiais

## TL;DR

Técnica de [[wiki/entities/john-ousterhout]] (*A Philosophy of Software Design*, 6.8): casos especiais são especialização dentro do corpo dos métodos. Eles enchem o código de `if`, deixam o código difícil de entender e criam bugs. A melhor saída é desenhar o caso normal para que ele trate as condições de contorno sem código extra ([[wiki/sources/filosofia-do-design-de-software-cap-06-modulos-de-proposito-geral-sao-mais-profundos]]).

## O exemplo da seleção vazia

No editor dos alunos, a maioria guardava uma variável dizendo se havia seleção, porque às vezes nada está selecionado na tela. O código ganhou verificações de "nenhuma seleção" em vários lugares.

A correção: a seleção sempre existe. Quando nada está selecionado, ela é vazia (início igual ao fim). Copiar uma seleção vazia insere 0 bytes, sem verificação. Para apagar uma seleção dentro de uma linha, junte o trecho antes dela com o trecho depois; se ela for vazia, a operação devolve a linha original.

## Onde a ideia aparece no livro

- **Cap. 1:** remover casos especiais é um dos exemplos da primeira abordagem contra a complexidade, eliminar em vez de encapsular ([[wiki/concepts/reducao-de-complexidade]]).
- **Cap. 6:** a seleção vazia, acima. A introdução do capítulo diz que eliminar casos especiais também pode deixar o código mais eficiente, tema do cap. 20.
- **Cap. 10:** exceções criam ainda mais casos especiais; a resposta é [[wiki/concepts/definir-erros-para-fora-da-existencia]], que também redefine a semântica para o caso de erro virar caso normal.
- **Cap. 20:** o caminho crítico de desempenho deixa os casos especiais fora dele ([[wiki/sources/filosofia-do-design-de-software-livro-completo]]).

## Relação com outros conceitos

- [[wiki/concepts/modulo-de-proposito-geral]]: a mesma ideia no nível da interface; aqui ela vale dentro do método.
- [[wiki/concepts/definir-erros-para-fora-da-existencia]]: a versão da técnica para erros e exceções.
- O padrão Null Object, que troca a verificação de `null` por um objeto que não faz nada, segue a mesma lógica. Fowler o generaliza como *Special Case* ([external] https://martinfowler.com/eaaCatalog/specialCase.html). O nome é o oposto, mas a ideia é igual: o caso especial vira um objeto que o código normal trata sem `if`. O livro não cita nenhum dos dois (leitura da wiki).

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-cap-06-modulos-de-proposito-geral-sao-mais-profundos]]: 6.8, a seleção vazia, em primeira mão
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]: casos especiais no cap. 10 e fora do caminho crítico no cap. 20
