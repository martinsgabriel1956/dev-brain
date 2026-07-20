---
title: "Test Double"
author: "Martin Fowler"
source_url: "https://martinfowler.com/bliki/TestDouble.html"
date_published: 2006-01-17
date_ingested: 2026-07-19
note: "Tradução para PT-BR do artigo original (bliki entry, texto curto). Para o texto exato em inglês, consultar a source_url."
---

# Test Double

Gerard Meszaros está [escrevendo um livro](https://martinfowler.com/books/meszaros.html) para capturar padrões de uso dos vários frameworks [Xunit](https://martinfowler.com/bliki/Xunit.html). Uma das dificuldades que ele encontrou foi a quantidade de nomes diferentes para stubs, mocks, fakes, dummies e outras coisas que as pessoas usam para substituir partes de um sistema durante o teste. Para lidar com isso, ele criou seu próprio vocabulário, que vale a pena divulgar.

O termo genérico que ele usa é [Test Double](http://xunitpatterns.com/Test%20Double.html) (pense em dublê de cinema). Test Double é o termo genérico para qualquer caso em que você substitui um objeto de produção por outro com propósito de teste. Existem vários tipos de double que Gerard lista:

- **Dummy**: objetos que são passados adiante mas nunca de fato usados. Geralmente servem só para preencher listas de parâmetros.
- **Fake**: objetos que têm implementações funcionais de verdade, mas normalmente tomam algum atalho que os torna inadequados para produção (um `InMemoryTestDatabase` é um bom exemplo).
- **Stub**: fornecem respostas prontas para as chamadas feitas durante o teste, normalmente sem responder a nada além do que foi programado para o teste.
- **Spy**: são stubs que também registram alguma informação sobre como foram chamados. Um exemplo seria um serviço de e-mail que registra quantas mensagens foram enviadas.
- **Mock**: são pré-programados com expectativas que formam uma especificação das chamadas que esperam receber. Podem lançar uma exceção se receberem uma chamada que não esperavam, e são verificados durante a validação para garantir que receberam todas as chamadas esperadas.

## Leitura complementar

Fowler expande o uso de Mocks, Doubles e afins em [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html).

## Metadados do artigo

- Publicado em 17 de janeiro de 2006. Um dos bliki entries mais antigos e mais citados de Fowler — é a fonte primária do termo "Test Double" que se tornou vocabulário padrão da indústria.
- Autor da taxonomia (Dummy/Fake/Stub/Spy/Mock) é **Gerard Meszaros**, não Fowler — Fowler está apenas relatando e divulgando um vocabulário que Meszaros desenvolveu para o livro *xUnit Test Patterns* (2007). Fowler cunha/divulga o termo guarda-chuva "Test Double" no bliki, mas atribui explicitamente a taxonomia interna a Meszaros.
- Termos/artigos relacionados citados: `Xunit` (bliki), `InMemoryTestDatabase` (bliki), *xUnit Test Patterns* (livro de Meszaros), "Mocks Aren't Stubs" (artigo mais longo do próprio Fowler sobre o mesmo tema).
