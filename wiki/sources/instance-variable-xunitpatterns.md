---
type: source
title: "Instance Variable (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["instance variable", "variável de instância", "member variable", "xunit patterns glossary instance variable"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: /home/nemomartins/Documentos/new/dev-study/raw/instance-variable-xunitpatterns.md
source_url: "http://xunitpatterns.com/instance%20variable.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
source_count: 0
tags: [testes, oo, xunit, fonte-primaria, terminologia, glossario]
skill: tech-mentor-testing
status: stable
---

# Instance Variable (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete do Glossário do xUnitPatterns.com que finalmente dá fonte primária isolada ao termo **instance variable** (também conhecida como **member variable**): "uma variável associada a um objeto, e não à classe do objeto". Só é acessível de dentro da instância ou através dela, e serve tipicamente para guardar estado que se espera diferente de uma instância para outra. O verbete cobre também a sintaxe de acesso (`objectReference.variableName`, ou `self`/`this` explícito dentro de métodos, dependendo da linguagem) e o único mecanismo de sombreamento citado: **local variables** podem sobrepor uma instance variable dentro de um método. Este verbete resolve o stub que já existia em [[wiki/concepts/instance-variable]], criado antes a partir de uma menção lateral em [[wiki/sources/attribute-xunitpatterns]].

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Instance variable é uma variável associada a um objeto, não à classe | "A variable that is associated with an object rather than the class of object." | fonte primária (Meszaros) | alta |
| Só é acessível de dentro ou através da instância | "is only accessible from within or via an instance of the class" | fonte primária | alta |
| "member variable" é sinônimo direto | "Also known as: member variable" | fonte primária | alta |
| Local variables podem sobrepor (shadow) instance variables dentro de um método | "unless overridden by local variables" | fonte primária | alta |

---

## Key Claims

### 1. Fonte primária isolada que resolve o stub aberto por "attribute"
[[wiki/concepts/instance-variable]] existia como stub desde a ingestão de [[wiki/sources/attribute-xunitpatterns]], que citava o termo apenas como um dos dois sentidos possíveis de "attribute" no xUnit, sem verbete próprio no catálogo até agora. Este verbete fecha essa lacuna: define o termo por si mesmo, fora do contexto específico de xUnit — é vocabulário genérico de orientação a objetos, não uma invenção do glossário de testes.

### 2. Sintaxe de acesso varia por linguagem, mas o padrão dominante é `objectReference.variableName`
O verbete nota que, quando a instance variable não é `private`, o acesso mais comum é via `objectReference.variableName`. De dentro dos próprios métodos do objeto, algumas linguagens exigem referência explícita (`self.myVariableName` em Python/Ruby, `this.myVariableName` em Java/C#/JavaScript), enquanto outras assumem implicitamente que qualquer variável não qualificada é uma instance variable a menos que uma **local variable** a sobreponha.

### 3. O único mecanismo de shadow citado é local variable — não há menção a class variable
Diferente do que se poderia esperar de um contraste mais completo (instance vs. class vs. local), o verbete menciona apenas **local variable** como o mecanismo que pode sobrepor uma instance variable. Não há menção a class variable (variável compartilhada entre todas as instâncias) neste verbete específico — a wiki ainda não tem fonte primária isolada para esse terceiro termo do trio.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para dezenas de outros termos de glossário já ingeridos

## Conceitos Tocados

- [[wiki/concepts/instance-variable]] — página que este verbete resolve de stub para fonte primária própria
- [[wiki/concepts/shared-fixture]] — já discutia o mecanismo pelo qual instance variables viram vetor de Shared Fixture implícito quando a Testcase Class é reutilizada entre Test Methods (NUnit 2.x/TestNG)

## Questões Abertas

- O verbete não define **class variable** separadamente, e a wiki ainda não tem página nem fonte primária isolada para o termo — candidato natural para ingestão futura, fechando o trio local/instance/class variable.
- Não há menção, neste verbete, ao comportamento específico de xUnit (Shared Fixture implícito via reuso de instância entre Test Methods) já documentado em [[wiki/concepts/instance-variable]] a partir de [[wiki/sources/there-is-always-an-exception-xunitpatterns]] — a definição aqui é puramente genérica de OO, e a conexão com xUnit continua vindo de outras fontes.

---

## Citações Relevantes

> "A variable that is associated with an object rather than the class of object. An instance variable is only accessible from within or via an instance of the class and is typically used to access information that is expected to be different from one instance to another."

> "The exact syntax used to access an instance variable varies from language to language. [...] some languages require an explicit reference to the object (e.g. self myVariableName or this.myVariableName) while others just assume that any variables are instance variable unless overridden by local variables."

*(Tradução completa em `raw/instance-variable-xunitpatterns.md`.)*
