---
type: concept
title: "Causas de Complexidade (Ousterhout): Dependências e Obscuridade"
aliases: ["dependências e obscuridade", "dependencies and obscurity", "obscuridade", "obscurity", "causas da complexidade"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 4
tags: [complexidade, design, ousterhout, dependencias, obscuridade, acoplamento]
skill: tech-mentor-backend
status: draft
---

# Causas de Complexidade (Ousterhout): Dependências e Obscuridade

## TL;DR

Para [[wiki/entities/john-ousterhout]], a complexidade tem duas causas: **dependências** e **obscuridade** (cap. 2.3). Dependências geram amplificação de mudanças e carga cognitiva; a obscuridade gera incógnitas desconhecidas e também carga cognitiva ([[wiki/concepts/sintomas-de-complexidade-ousterhout]]). Dependências não podem ser eliminadas, só reduzidas e tornadas óbvias. A obscuridade se combate primeiro com design e depois com documentação.

## Dependências

Há dependência quando um trecho de código não pode ser compreendido e modificado isoladamente: mudar um exige considerar ou mudar outro. Exemplos do livro: a cor do banner repetida em cada página; remetente e destinatário de um protocolo de rede; a assinatura de um método e seus chamadores ([[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]]).

Dependências são parte do software e às vezes intencionais: cada classe nova cria dependências em torno da sua API. O objetivo é **ter menos e deixar as que restam simples e óbvias**. No exemplo do site, a variável central `bannerBg` não zerou as dependências. Ela trocou uma dependência entre todas as páginas, difícil de gerenciar, por uma dependência de cada página com um nome que se acha com busca e que o compilador verifica.

O resto da wiki trata o mesmo fenômeno como [[wiki/concepts/acoplamento]]. O [[wiki/concepts/ocultamento-de-informacao]] é a técnica central do livro para reduzir dependências entre módulos.

## Obscuridade

Obscuridade é quando informação importante não é óbvia. Exemplos do livro: um nome genérico (`time`); a unidade de uma variável que não está documentada; um novo status de erro que exige mexer numa tabela de mensagens de cuja existência ninguém sabe; o mesmo nome usado para dois propósitos (ver o bug da variável `block` em [[wiki/concepts/naming]]).

A obscuridade costuma vir de uma dependência que não é óbvia. Por isso as duas causas aparecem juntas. Ela também vem de **inconsistência** e de documentação ruim. Ousterhout insiste que é sobretudo questão de design: "a necessidade de documentação extensa costuma ser um alerta vermelho" ([[wiki/concepts/red-flags-de-design]]), e a melhor forma de reduzi-la é simplificar o design. A documentação cobre o que sobra ([[wiki/concepts/comentarios-como-ferramenta-de-design]]).

Não confundir com [[wiki/concepts/seguranca-por-obscuridade]]: lá a obscuridade é uma escolha (esconder para proteger), aqui é um defeito (informação que deveria estar visível e não está).

## Relação com outros conceitos

- [[wiki/concepts/complexidade-incremental]]: nenhuma dependência ou obscuridade isolada pesa muito; o problema é o acúmulo.
- [[wiki/concepts/dependencia-externa-oculta]] e a seção "Dependência Escondida" de [[wiki/concepts/acoplamento]]: casos em que dependência e obscuridade coincidem.
- [[wiki/concepts/complexidade-acidental]]: as duas causas são estruturais, ou seja, acidentais no vocabulário de Brooks, e não inerentes ao domínio (inferência desta wiki).

## Dependência e obscuridade no nível do módulo (cap. 4)

[[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]] leva as duas causas para o design modular. Sobre **dependências**, o objetivo passa a ser minimizá-las, porque eliminá-las é impossível: módulos chamam uns aos outros (4.1). Os exemplos são os argumentos de um método e uma dependência de ordem, em que um método só funciona se outro foi chamado antes. Sobre **obscuridade**, a 4.3 dá o mecanismo no nível da interface: uma abstração que omite um detalhe importante é uma falsa abstração, e quem olha só para ela não tem a informação para usá-la ([[wiki/concepts/abstracao]]).

## O vazamento pela porta dos fundos junta as duas causas (cap. 5)

No cap. 5, duas classes que conhecem o mesmo formato de arquivo dependem uma da outra sem que isso apareça em nenhuma interface. É dependência somada a obscuridade, e o livro diz que esse vazamento "é mais pernicioso" que o da interface "porque não é óbvio" ([[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]], 5.2). O [[wiki/concepts/ocultamento-de-informacao]] ataca a dependência; a interface simples ataca a obscuridade.

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]]: definição das duas causas, exemplos e o mapeamento causa → sintoma (2.3)
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]: "Complexity is caused by two things: dependencies and obscurity", retomado ao longo do livro
- [[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]] — dependências minimizadas, não eliminadas (4.1); falsa abstração como forma de obscuridade (4.3)
- [[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]]: vazamento pela porta dos fundos como dependência não óbvia (5.2)
