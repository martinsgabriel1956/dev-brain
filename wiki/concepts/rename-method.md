---
type: concept
title: "Rename Method"
aliases: ["renomear método"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 2
tags: [testes, refatoracao, martin-fowler, xunit, terminologia]
skill: tech-mentor-testing
status: stable
---

# Rename Method

Refatoração de [[wiki/entities/martin-fowler|Martin Fowler]] (*Refactoring*): alterar o nome de um método para melhor comunicar seu propósito. Segundo [[wiki/sources/rename-method-xunitpatterns]], fonte primária dedicada ao próprio termo, o problema motivador é genérico — "o nome de um método não revela seu propósito" — e a solução é de uma frase: "mude o nome do método". A fonte não menciona teste em nenhum momento; é [[wiki/sources/test-discovery-xunitpatterns]] quem aplica a técnica a um contexto específico de migração: ao adotar um framework [[wiki/concepts/tdd|xUnit]] existente que descobre [[wiki/concepts/test-method|Test Methods]] por convenção de nomenclatura (ver [[wiki/concepts/test-discovery]]), pode ser necessário renomear métodos de teste já existentes para que passem a ser reconhecidos pelo mecanismo de **[[wiki/concepts/test-discovery|Test Method Discovery]]** do framework — em vez de reescrever a lógica do teste, basta um Rename Method.

## Alternativa quando o framework usa metadado

A própria fonte contrasta esse caso com frameworks que descobrem Test Methods via **method attribute** ou **annotation**: nesse caso, não é preciso renomear nada — basta adicionar o atributo apropriado ao método já existente.

## Citação preservada de Fowler sobre o risco de métodos pequenos demais

[[wiki/sources/rename-method-xunitpatterns]] preserva uma citação direta de Fowler ausente nas duas refatorações-irmãs já ingeridas (Extract Method, Extract Interface): "uma parte importante do estilo de código que eu defendo é usar métodos pequenos para fatorar processos complexos. Feito de forma ruim, isso pode te levar numa dança sem fim para descobrir o que todos aqueles métodos pequenos fazem" — um alerta sobre o risco da técnica-irmã Extract Method, não sobre Rename Method em si.

## Status: stable

Segue o mesmo padrão host≠autor já registrado para [[wiki/concepts/extract-method]] e [[wiki/concepts/extract-interface]] (ambas do livro *Refactoring* de Fowler, catalogadas mas não escritas no site de Meszaros). Agora com fonte primária própria dedicada ("Rename Method" no catálogo de Meszaros), além da citação indireta em test-discovery.

## Key Sources

- [[wiki/sources/rename-method-xunitpatterns]] — **fonte primária dedicada**: problema/solução em uma frase cada, mais citação direta de Fowler sobre métodos pequenos demais
- [[wiki/sources/test-discovery-xunitpatterns]] — aplica a técnica ao contexto de migração para descoberta de testes por convenção de nomenclatura
