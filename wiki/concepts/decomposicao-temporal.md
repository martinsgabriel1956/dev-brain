---
type: concept
title: "Decomposição Temporal"
aliases: ["temporal decomposition", "decomposição temporal", "decomposicao temporal"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 2
tags: [design, ousterhout, information-hiding, vazamento-de-informacao, modularizacao, red-flag]
skill: tech-mentor-backend
status: draft
---

# Decomposição Temporal

## TL;DR

Estilo de design, nomeado por [[wiki/entities/john-ousterhout]], em que a estrutura do sistema segue a ordem cronológica das operações: uma classe para ler, outra para modificar, outra para gravar. É uma causa comum de vazamento de informação ([[wiki/concepts/ocultamento-de-informacao]]), porque a mesma decisão de design costuma ser usada em vários momentos da execução e acaba codificada em vários módulos. É um dos red flags do livro ([[wiki/concepts/red-flags-de-design]]).

## Os dois exemplos do cap. 5

- **Arquivo.** Uma aplicação lê um arquivo, modifica o conteúdo e grava de volta. Em três classes, a de leitura e a de gravação conhecem o formato do arquivo. A correção é juntar leitura e gravação numa classe só, usada nas duas fases ([[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]], 5.3).
- **Requisição HTTP.** Uma equipe de alunos separou "ler a requisição da rede" e "analisar a string". Como o `Content-Length` diz onde a requisição termina, ler exige analisar os cabeçalhos. As duas classes entendiam o formato e o código de análise ficou duplicado. O livro diz que "teria sido melhor" fundi-las (5.5).

## Por que é fácil cair nela

A ordem das operações está na cabeça de quem programa. Mas a maioria das decisões de design aparece em vários momentos do ciclo de vida da aplicação. A ordem importa e vai aparecer em algum lugar do código; só não deve definir a estrutura dos módulos, a não ser que cada etapa use informações totalmente distintas. A regra do livro: pense no conhecimento de cada tarefa, não na ordem das tarefas.

## Não confundir com temporal coupling

[[wiki/concepts/temporal-coupling]] é uma ordem de chamada implícita, que nada no código impõe. A decomposição temporal é um critério de modularização. Uma pode causar a outra: no exemplo HTTP, quem chamava tinha de invocar dois métodos de classes diferentes numa ordem específica. A ordem vazou para a interface.

## Relação com outros conceitos

- [[wiki/concepts/modulo-profundo]]: a decomposição temporal gera muitas classes rasas; a fusão gera uma classe mais profunda.
- [[wiki/concepts/ocultamento-de-informacao]]: o vazamento que a decomposição temporal causa.
- [[wiki/concepts/causas-de-complexidade-ousterhout]]: o formato de arquivo dividido entre leitor e escritor é uma dependência sem estar na interface, ou seja, também obscuridade.

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]]: definição (5.3), exemplo HTTP (5.5) e conclusão (5.10), em primeira mão
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]: resumo do cap. 5 e o red flag no apêndice
