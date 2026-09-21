---
type: source
title: "Local Variable (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["local variable", "variável local", "xunit patterns glossary local variable"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: /home/nemomartins/Documentos/new/dev-study/raw/local-variable-xunitpatterns.md
source_url: "http://xunitpatterns.com/local%20variable.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
source_count: 0
tags: [testes, oo, xunit, fonte-primaria, terminologia, glossario]
skill: tech-mentor-testing
status: stable
---

# Local Variable (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete mínimo do Glossário do xUnitPatterns.com que dá fonte primária isolada ao termo **local variable**, até agora citado apenas de passagem em [[wiki/sources/instance-variable-xunitpatterns]] como o único mecanismo de shadow que sobrepõe uma [[wiki/concepts/instance-variable|instance variable]] dentro de um método. Definição: "uma variável associada a um bloco de código, e não a um objeto ou classe". Só é acessível de dentro do bloco de código e sai de escopo quando esse bloco retorna para quem o chamou. É o verbete mais curto da série até agora — uma única frase, sem exemplo de código, sem seção de termos relacionados no original.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Local variable é associada a um bloco de código, não a um objeto ou classe | "A variable that is associated with a block of code rather than an object or class." | fonte primária (Meszaros) | alta |
| Só é acessível de dentro do bloco de código | "is only accessible from within the code block" | fonte primária | alta |
| Sai de escopo quando o bloco retorna ao chamador | "it goes out of scope when the block of code returns to its caller" | fonte primária | alta |

---

## Key Claims

### 1. Fonte primária isolada que fecha a lacuna sinalizada em "instance variable"
[[wiki/sources/instance-variable-xunitpatterns]] já citava local variable como o único mecanismo de shadow explícito no glossário, mas sem fonte primária própria. Este verbete fecha essa lacuna: define o termo isoladamente, também fora do contexto específico de xUnit — assim como instance variable, é vocabulário genérico de escopo de variável em linguagens de programação, não uma invenção do glossário de testes.

### 2. Escopo é definido por bloco de código, não por objeto/classe
O contraste é direto com [[wiki/concepts/instance-variable]] (escopo = objeto) e, por extensão, com class variable (escopo = classe, ainda sem fonte primária isolada na wiki). O verbete não usa o termo "método" explicitamente — usa "code block", termo mais genérico que cobre métodos, mas também blocos de controle de fluxo (if, loop) em linguagens onde esses blocos criam escopo próprio.

### 3. Verbete mais curto da série: sem exemplo de código, sem sintaxe, sem termos relacionados no original
Diferente de [[wiki/sources/instance-variable-xunitpatterns]] (que trazia sintaxe de acesso por linguagem) e de [[wiki/sources/block-xunitpatterns]] (que trazia exemplos concretos), este verbete é uma única frase sem elaboração. A seção "Termos relacionados" na tradução em `raw/local-variable-xunitpatterns.md` foi construída pelo agente a partir de conexões já presentes na wiki, não do original.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para dezenas de outros termos de glossário já ingeridos

## Conceitos Tocados

- [[wiki/concepts/instance-variable]] — já citava local variable como mecanismo de shadow; agora ambos os lados do par têm fonte primária isolada
- [[wiki/concepts/local-variable]] — novo stub criado a partir desta fonte

## Questões Abertas

- **class variable** (terceiro termo do trio local/instance/class) continua sem fonte primária isolada no catálogo — candidato natural para ingestão futura, fechando o trio completo.
- O verbete não distingue explicitamente "local variable de método" de "local variable de bloco de controle" (if/loop) — nuance que varia por linguagem (Java declara escopo por bloco `{}`; Python não cria escopo próprio para if/for) e não é resolvida pela fonte primária.

---

## Citações Relevantes

> "A variable that is associated with a block of code rather than an object or class. An local variable is only accessible from within the code block and it goes out of scope when the block of code returns to its caller."

*(Tradução completa em `raw/local-variable-xunitpatterns.md`.)*
