---
type: concept
title: "Decidir O Que Importa"
aliases: ["decide what matters", "separar o que importa do que não importa"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [design, ousterhout, abstracao, performance, taste-dev]
skill: tech-mentor-backend
status: draft
---

# Decidir O Que Importa

## TL;DR

Capítulo de fechamento de [[wiki/entities/john-ousterhout]] (*A Philosophy of Software Design*, Cap. 21): boa parte do design de software se resume a separar o que importa do que não importa, e então estruturar o sistema em torno do que importa — emprestando prominência, repetição e centralidade às coisas importantes, e escondendo ao máximo as que não são.

## Duas formas de errar

1. **Tratar coisas demais como importantes** — cada detalhe irrelevante exposto aumenta a carga cognitiva de quem usa o módulo. Exemplo reciclado do Cap. 4: a interface de I/O do Java forçando todo desenvolvedor a saber a diferença entre stream bufferizada e não bufferizada, quando a esmagadora maioria sempre quer buffering.
2. **Não perceber que algo é importante** — leva a informação escondida demais, ou funcionalidade ausente que desenvolvedores precisam recriar toda vez. Esse é o tipo de erro que gera "unknown unknowns" (Cap. 2) — o pior dos três sintomas de complexidade do livro.

## Como encontrar o que importa: alavancagem (leverage)

A heurística central do capítulo: procure pontos de alavancagem, onde resolver um problema resolve vários outros de tabela, ou onde saber uma única informação permite prever o comportamento em muitas situações diferentes. Exemplo reciclado do Cap. 6: uma interface de texto genérica (`insert`/`delete` por intervalo) tem mais alavancagem que métodos especializados (`backspace`, `deleteSelection`) porque resolve mais problemas com a mesma API. Um invariante (algo sempre verdadeiro sobre uma variável ou estrutura) é outro exemplo de ponto de alavancagem: uma vez conhecido, permite prever comportamento em qualquer situação sem checar caso a caso.

## Como emphasizar o que importa

Três mecanismos citados: **prominência** (colocar em lugares onde será visto — documentação de interface, nomes, parâmetros de métodos muito usados), **repetição** (a mesma ideia aparecendo várias vezes reforça sua importância), e **centralidade** (a coisa mais importante deve estar no centro do sistema, determinando a estrutura ao redor dela — ex.: a interface de device drivers de um sistema operacional, da qual centenas de drivers dependem).

## Quando não é óbvio o que importa

O autor recomenda formular uma hipótese explícita ("acho que isso é o que mais importa aqui"), comprometer-se com ela, construir sob essa suposição, e depois avaliar se estava certo — aprendendo com o resultado de qualquer forma. Essa é uma aplicação prática de [[wiki/concepts/projetar-duas-vezes]]: ter múltiplas opções entre as quais escolher torna mais fácil enxergar o que de fato importa mais.

## "Bom gosto" como capacidade central

O capítulo fecha definindo **bom gosto** (good taste) como a capacidade de distinguir o que é importante do que não é — e trata isso como habilidade central de um bom designer de software, não talento inato. O mesmo raciocínio, segundo o autor, se aplica fora de software: em escrita técnica (organizar um documento em torno de poucos conceitos-chave) e mesmo como filosofia de vida (gastar energia no que de fato importa).

## Relação com outros conceitos

- [[wiki/concepts/definir-erros-para-fora-da-existencia]] — o limite do princípio (quando não mascarar/esconder um erro) é uma aplicação direta de "decidir o que importa": só esconda informação que realmente não importa para quem está de fora.
- [[wiki/concepts/ocultamento-de-informacao]] — ocultar informação é, no fundo, decidir que aquela informação não importa para fora do módulo.
- [[wiki/concepts/projetar-duas-vezes]] — comparar alternativas explicitamente ajuda a revelar o que realmente importa em uma decisão de design.
- [[wiki/concepts/naming]] — escolher nome de variável é descrito no livro como o mesmo exercício em miniatura: listar palavras candidatas e escolher as que carregam mais informação relevante.

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — Cap. 21 (fechamento) e Cap. 20 (performance como caso concreto de "decidir o que importa" no caminho crítico)
