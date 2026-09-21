---
type: source
title: "There's Always an Exception (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["sempre existe uma exceção", "junit new instance", "nunit shared fixture bug", "testcase object exception"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 1
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/there-is-always-an-exception-xunitpatterns.md"
source_url: "http://xunitpatterns.com/There%20is%20Always%20an%20Exception.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
tags: [testes, xunit, junit, nunit, testng, shared-fixture, erratic-test, terminologia, tech-mentor-testing]
skill: tech-mentor-testing
status: stable
---

# There's Always an Exception (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Sidebar do catálogo xUnitPatterns.com que documenta a única exceção conhecida (na época) à regra de design mais fundamental do xUnit: um [[wiki/concepts/testcase-object|Testcase Object]] separado por [[wiki/concepts/test-method|Test Method]], mecanismo pelo qual o framework alcança "Independent Test". **NUnit** (versão 2.x) e **TestNG** rompem essa regra, instanciando a Testcase Class **uma única vez** e reutilizando-a para todos os métodos de teste. A fonte cita diretamente [[wiki/entities/james-newkirk|James Newkirk]], coautor do NUnit 2.0, admitindo publicamente que essa foi uma decisão de design que ele considera um erro ("uma das maiores burradas"): reutilizar a instância cria um [[wiki/concepts/shared-fixture|Shared Fixture]] implícito via variáveis de instância, o que introduz dependência de ordem de execução entre testes — um dos gatilhos clássicos de [[wiki/concepts/erratic-test|Erratic Test]]. A correção paliativa adotada pelo NUnit (tornar as variáveis de fixture `static`) é descrita pelo próprio Newkirk como algo que não resolve o problema de raiz, apenas o torna mais visível/honesto. [[wiki/entities/martin-fowler]] considerou o caso relevante o bastante para escrever um artigo dedicado defendendo a abordagem do JUnit (nova instância por método) — [JunitNewInstance](http://martinfowler.com/bliki/JunitNewInstance.html), referenciado mas não citado in extenso nesta fonte.

## Afirmações-chave

| Afirmação | Evidência | Confiança |
|---|---|---|
| A regra de design fundamental do xUnit é: um Testcase Object por Test Method, para garantir Independent Test | Afirmação central da fonte primária (Meszaros) | Alta |
| NUnit (2.x) e TestNG são, até onde o autor sabe, os únicos membros da família xUnit que não seguem essa regra | "The only members of the family (that I am aware of) that don't do this are TestNG and NUnit (version 2.x)" | Alta como declaração do autor — mas com ressalva explícita dele mesmo ("that I am aware of") |
| NUnit 2.0 cria uma única instância da Testcase Class e a reutiliza para todos os Test Methods | Citação direta de James Newkirk, coautor do NUnit 2.0 | Alta — fonte primária, admissão do próprio autor |
| Reutilizar a instância cria um Shared Fixture implícito via variáveis de instância, habilitando dependência de ordem de execução entre testes (anti-padrão) | Citação direta de Newkirk | Alta |
| A correção aplicada pelo NUnit (tornar variáveis de fixture `static`) não resolve o problema, apenas torna explícito que há uma única instância compartilhada | Citação direta de Newkirk ("It's almost like truth in advertising") | Alta |
| Martin Fowler escreveu um artigo dedicado ("JunitNewInstance") defendendo a abordagem do JUnit como a correta | Referência direta com URL, sem citação de trecho do artigo | Alta quanto à existência do artigo; conteúdo do artigo em si não verificado nesta ingestão (fora do escopo desta fonte) |

## Entidades Mencionadas

- [[wiki/entities/james-newkirk]] — coautor do NUnit 2.0, citado diretamente admitindo o erro de design
- [[wiki/entities/nunit]] — framework de teste para .NET, porta da família xUnit; foco central desta fonte
- [[wiki/entities/testng]] — framework de teste para Java, citado como o outro membro da família que rompe a regra de uma instância por método
- [[wiki/entities/martin-fowler]] — escreveu o artigo "JunitNewInstance" defendendo a abordagem do JUnit
- [[wiki/entities/junit]] — citado implicitamente como o padrão-ouro ("JUnit New Instance Behavior") contra o qual a exceção do NUnit é comparada
- [[wiki/entities/gerard-meszaros]] — autor da fonte

## Conceitos Tocados

- [[wiki/concepts/testcase-object]] — a regra de "um por Test Method" e sua exceção
- [[wiki/concepts/test-method]] — unidade associada a cada Testcase Object
- [[wiki/concepts/shared-fixture]] — conceito novo criado nesta ingestão: fixture reutilizado entre testes, aqui de forma implícita e não intencional
- [[wiki/concepts/erratic-test]] — conceito novo criado nesta ingestão: família de test smells causados por dependência de ordem de execução

## Open Questions

1. **Conteúdo do artigo "JunitNewInstance" de Fowler não verificado nesta ingestão.** A fonte apenas referencia a URL (http://martinfowler.com/bliki/JunitNewInstance.html); o argumento completo de Fowler sobre por que a abordagem do JUnit está correta fica como lacuna para uma ingestão futura dedicada.
2. **Estado atual do NUnit e do TestNG não verificado.** A fonte é de 2003-2008 (o rodapé da página cita geração em 2011, mas o copyright é 2003-2008); não há confirmação nesta ingestão sobre se versões mais recentes do NUnit (3.x+) ou do TestNG mudaram esse comportamento de instanciação.
3. **Ressalva do próprio autor** ("the only members of the family that I am aware of") deixa em aberto se existem outras portas do xUnit com o mesmo comportamento, não mencionadas por não serem de conhecimento de Meszaros na época.

## Raw Quotes

> "Whether we are learning to conjugate verbs in a new language or looking for patterns in how software is built, There's Always an Exception!"

> "I think one of the biggest screw-ups that was made when we wrote NUnit V2.0 was to not create a new instance of the test fixture class for each contained test method. [...] This can introduce execution order dependencies which for this type of testing is an anti-pattern."

> "Since it would be difficult to change the way that NUnit works now, too many people would complain, I now make all of the member variables in test fixture classes static. It's almost like truth in advertising."

*(Tradução completa em `raw/there-is-always-an-exception-xunitpatterns.md`.)*

## Key Sources (fontes citadas nesta ingestão)

Nenhuma — fonte primária desta ingestão.

**Atualização (2026-09-21):** [[wiki/sources/testcase-object-xunitpatterns]], fonte primária dedicada ao termo **Testcase Object**, foi ingerida e detalha a mecânica normal de instanciação (Command Pattern, Pluggable Behavior + reflection) que esta fonte trata como a regra rompida pela exceção do NUnit 2.x/TestNG.
