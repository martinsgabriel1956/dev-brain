---
type: concept
title: "Instance Variable"
aliases: ["variável de instância", "attribute (NUnit)"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 3
tags: [oo, testes, xunit, terminologia]
skill: tech-mentor-testing
status: draft
---

# Instance Variable

Também conhecida como **member variable**: uma variável associada a um objeto, e não à classe do objeto — só acessível de dentro da instância ou através dela, tipicamente usada para guardar estado que se espera diferente de uma instância para outra ([[wiki/sources/instance-variable-xunitpatterns]]). No vocabulário do xUnitPatterns.com, também aparece como um dos dois sentidos possíveis do termo [[wiki/sources/attribute-xunitpatterns|attribute]] (o outro é sinônimo de [[wiki/sources/annotation-xunitpatterns|annotation]]). Fora do glossário de teste, é o termo genérico de OO para propriedade/campo de um objeto — não específico de xUnit.

A sintaxe de acesso varia por linguagem: o padrão mais comum é `objectReference.variableName` quando a instance variable não é `private`; de dentro dos próprios métodos, algumas linguagens exigem referência explícita ao objeto (`self.x`, `this.x`), enquanto outras assumem implicitamente que qualquer variável não qualificada é instance variable — a menos que uma [[wiki/concepts/local-variable|local variable]] a sobreponha (shadowing) dentro do método. Essa segunda ponta do par agora também tem fonte primária isolada: local variable é definida como variável associada a um bloco de código (não a um objeto ou classe), acessível só de dentro dele e fora de escopo assim que o bloco retorna ao chamador ([[wiki/sources/local-variable-xunitpatterns]]).

## Por que importa em xUnit: o vetor do Shared Fixture implícito

O papel da instance variable em xUnit não é neutro: é exatamente o mecanismo pelo qual um [[wiki/concepts/shared-fixture|Shared Fixture]] implícito se forma. Quando uma Testcase Class é instanciada uma única vez para todos os [[wiki/concepts/test-method|Test Methods]] (comportamento do [[wiki/entities/nunit|NUnit]] 2.x e do [[wiki/entities/testng|TestNG]], documentado em [[wiki/sources/there-is-always-an-exception-xunitpatterns]]), qualquer objeto referenciado por uma instance variable fica visível para todos os métodos subsequentes — habilitando dependência de ordem de execução, uma causa clássica de [[wiki/concepts/erratic-test|Erratic Test]]. Já quando a Testcase Class é instanciada uma vez por Test Method (comportamento padrão do JUnit), esse vazamento não ocorre.

## Status: draft

Conceito criado a partir de [[wiki/sources/attribute-xunitpatterns]], que isolava o termo pela primeira vez como sentido próprio (antes só aparecia embutido na explicação do mecanismo de instanciação do NUnit/TestNG, sem página dedicada). Agora com fonte primária própria — [[wiki/sources/instance-variable-xunitpatterns]] — que define o termo isoladamente, fora do contexto específico de xUnit.

## Key Sources

- [[wiki/sources/attribute-xunitpatterns]] — isola o termo como um dos dois sentidos possíveis de "attribute" no xUnit
- [[wiki/sources/instance-variable-xunitpatterns]] — fonte primária isolada: definição genérica de OO, sintaxe de acesso por linguagem, e local variable como único mecanismo de shadow citado
- [[wiki/sources/local-variable-xunitpatterns]] — fonte primária isolada do termo que faz shadow: local variable, escopo de bloco de código
