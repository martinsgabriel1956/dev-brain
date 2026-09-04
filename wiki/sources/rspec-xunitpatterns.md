---
type: source
title: "RSpec (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["rspec xunitpatterns", "rspec glossary xunitpatterns"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/rspec-xunitpatterns.md
source_url: "http://xunitpatterns.com/RSpec.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-04
source_count: 0
tags: [testes, rspec, jbehave, bdd, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# RSpec (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curto da categoria **xUnit Members** do catálogo xUnitPatterns.com dedicado ao próprio framework [[wiki/entities/rspec|RSpec]] — até agora citado na wiki apenas de passagem em [[wiki/sources/test-context-xunitpatterns]] (que registrava só a renomeação "fixture" → "context"). Esta fonte fecha essa lacuna com página primária dedicada e amplia o quadro: RSpec é um dos **primeiros de uma nova geração de membros da família xUnit**, criado para tornar os testes de [[wiki/concepts/tdd|TDD]] mais úteis como **Tests as Specification**, e faz isso trocando **todo** o vocabulário de teste por vocabulário de especificação — não só "fixture"/"context", mas também Test Method → "specify" e "assert" → "should". Cita [[wiki/entities/jbehave|JBehave]] como o equivalente em Java, entidade sem qualquer menção prévia na wiki.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| RSpec é um dos primeiros membros de nova geração da família xUnit, feito para tornar testes de TDD úteis como especificação | "RSpec is one of the first of a new generation of xUnit members designed to make tests written as part of TDD more useful — Tests as Specification" | fonte primária (Meszaros) | alta |
| A diferença central é terminológica: abandona vocabulário de "teste" por vocabulário de especificação | "The main difference from more traditional members of the xUnit family is that it eschews the 'test' terminology and replaces it with terms more appropriate for specification" | fonte primária | alta |
| Mapeamento de termos: fixture→context, Test Method→specify, assert→should | "'Fixture' becomes 'context', Test Methods becomes 'specify', 'assert' becomes 'should' and so on" | fonte primária | alta |
| JBehave é o equivalente em Java do RSpec | "JBehave is the Java equivalent" | fonte primária | alta |

---

## Key Claims

### 1. RSpec ganha página própria e fecha a lacuna deixada por Test Context
[[wiki/sources/test-context-xunitpatterns]] já registrava, como open question, que "RSpec não tem página própria na wiki — candidato natural caso uma fonte futura aprofunde BDD/RSpec especificamente". Esta é exatamente essa fonte: verbete dedicado ao framework, com detalhe suficiente para justificar a página [[wiki/entities/rspec]].

### 2. O mapeamento terminológico é mais amplo do que a wiki já sabia
Antes desta ingestão, a wiki só tinha um ponto do mapeamento (fixture → context, via [[wiki/sources/test-context-xunitpatterns]]). Esta fonte acrescenta dois pares novos: **Test Method → "specify"** e **assert → "should"** — o vocabulário de asserção do RSpec (`x.should eq(y)`) citado por nome pela primeira vez na wiki.

### 3. JBehave surge como entidade nova, sem profundidade própria
A fonte cita JBehave apenas como "o equivalente em Java" do RSpec, sem elaborar. Não há fonte anterior ou posterior na wiki que aprofunde o framework — criado stub mínimo, candidato a expansão futura.

### 4. Conexão inferida, não confirmada pela fonte: origem do vocabulário de "specification" que o BDD formaliza depois
A fonte não menciona BDD nem Gherkin. Mas a motivação declarada do RSpec — "Tests as Specification" e a troca de "assert" por "should" — é reconhecível como precursora direta do vocabulário que [[wiki/concepts/bdd]] formaliza depois com Given/When/Then. Fica marcado como **[external]/inferência**, não como fato desta fonte.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada em toda a série xUnitPatterns.com
- [[wiki/entities/rspec]] — sujeito do verbete; primeira fonte dedicada ao framework na wiki
- [[wiki/entities/jbehave]] — citado como equivalente Java do RSpec; primeira menção na wiki, sem profundidade própria

## Conceitos Tocados

- [[wiki/concepts/tdd]] — RSpec é enquadrado explicitamente como ferramenta para tornar os testes de TDD "mais úteis como especificação"
- [[wiki/concepts/bdd]] — conexão inferida (não confirmada pela fonte) entre o vocabulário "specification" do RSpec e o vocabulário formal de BDD
- [[wiki/concepts/indirect-input-output]] — via [[wiki/sources/test-context-xunitpatterns]], o "context" do RSpec é o mesmo test fixture que organiza entradas/saídas indiretas

## Questões Abertas

- **Conexão RSpec → origem do vocabulário BDD não confirmada por esta fonte.** É uma inferência razoável (mesma motivação declarada: "specification" em vez de "test"), mas o verbete não cita BDD, Gherkin, nem Dan North. Fica marcada como [external] na página da entidade.
- **JBehave sem fonte própria.** Citado apenas por contraste; se aparecer fonte dedicada, expandir o stub em [[wiki/entities/jbehave]].
- Sem contradição com o resto da wiki — esta fonte apenas amplia, com fonte primária dedicada, o que já era conhecido de passagem sobre o RSpec.

---

## Citações Relevantes

> "RSpec is one of the first of a new generation of xUnit members designed to make tests written as part of TDD more useful — Tests as Specification. The main difference from more traditional members of the xUnit family is that it eschews the 'test' terminology and replaces it with terms more appropriate for specification. 'Fixture' becomes 'context', Test Methods becomes 'specify', 'assert' becomes 'should' and so on."

> "RSpec is available at http://rspec.rubyforge.org. JBehave is the Java equivalent."

*(Tradução completa em `raw/rspec-xunitpatterns.md`.)*
