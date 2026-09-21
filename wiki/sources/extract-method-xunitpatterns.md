---
type: source
title: "Extract Method (xUnitPatterns.com — catálogo de Gerard Meszaros, conteúdo atribuído a Martin Fowler)"
aliases: ["extract method", "extrair método", "xunit patterns code refactoring extract method"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/extract-method-xunitpatterns.md
source_url: "http://xunitpatterns.com/Extract%20Method.html"
author: "Gerard Meszaros (catálogo); conteúdo atribuído a Martin Fowler"
date_published: 2007-01-01
date_ingested: 2026-09-21
source_count: 0
tags: [testes, refactoring, test-code-duplication, xunit, fonte-primaria]
skill: tech-mentor-testing
status: stable
---

# Extract Method (xUnitPatterns.com — catálogo de Gerard Meszaros, conteúdo atribuído a Martin Fowler)

## TL;DR

Verbete curtíssimo da categoria **Code Refactorings** do catálogo xUnitPatterns.com, dedicado à refatoração **Extract Method** — irmã de nome parecido com [[wiki/sources/extract-interface-xunitpatterns|Extract Interface]], já ingerida, e com a mesma proveniência: Meszaros hospeda o verbete no seu site, mas credita o conteúdo a **[[wiki/entities/martin-fowler|Fowler]]** (*Refactoring: Improving the Design of Existing Software*), não a si mesmo. Fecha uma lacuna citada de passagem em [[wiki/sources/testcase-class-xunitpatterns]] e em [[wiki/concepts/refatoracao]], onde Extract Method já era mencionada como a refatoração recomendada para evitar **Test Code Duplication**, mas sem fonte primária dedicada. Assim como Extract Interface, o verbete é minimalista: problema, resumo de uma frase, remissão bibliográfica — sem mecânica passo a passo nem exemplo de código — e carrega a mesma nota do site alertando que o capítulo correspondente do livro publicado "provavelmente mudou substancialmente" em relação a esta versão preliminar.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| O problema motivador é: um fragmento de código (sequência de instruções) pode ser agrupado | "You have a code fragment (sequence of statements) that can be grouped together" | fonte primária (catálogo, atribuída a Fowler) | alta |
| A solução é transformar o fragmento num método cujo nome explique seu propósito | "Turn the fragment into a method whose name explains the purpose of the method" | fonte primária | alta |
| O conteúdo desta página é atribuído a Fowler, não a Meszaros — remissão bibliográfica explícita | "From [Ref] Refactoring: Improving the Design of Existing Software" | fonte primária | alta |
| A própria página se declara desatualizada em relação ao livro publicado | "The book has now been published and the content of this chapter has likely changed substanstially" | nota do site | alta (é o próprio site que avisa) |

---

## Key Claims

### 1. Extract Method resolve duplicação de *comportamento*, não de *tipos*
Ao contrário de [[wiki/concepts/extract-interface|Extract Interface]] — que extrai um subconjunto compartilhado de contrato para uma interface, sem alterar comportamento algum — Extract Method ataca a duplicação de **lógica**: uma sequência de instruções repetida (ou repetível) é isolada num método próprio, nomeado para comunicar sua intenção. É a refatoração clássica de "nomear a intenção" citada de forma dispersa em toda a literatura de Clean Code, mas aqui na sua formulação mais reduzida e original (Fowler, via o catálogo de Meszaros).

### 2. É a refatoração-alvo por trás de "Test Utility Method" em [[wiki/sources/testcase-class-xunitpatterns]]
Essa fonte já citava Extract Method de passagem, como a técnica recomendada para evitar **Test Code Duplication**: o código comum extraído de Test Methods repetidos vira um Test Utility Method, que pode viver na própria Testcase Class ou ser movido para uma Testcase Superclass ou Test Helper. Esta ingestão fecha a lacuna da fonte primária da refatoração em si — mas não elabora, além da frase de problema/solução, nenhuma mecânica específica de como decidir os limites do método extraído (parâmetros, nomes, visibilidade). Essa mecânica mais fina segue sendo território do livro de Fowler, não desta versão preliminar do site.

### 3. Mesmo padrão de atribuição cruzada já visto em Extract Interface
Confirma, com um segundo exemplo, o padrão "host ≠ autor" dentro da categoria **Code Refactorings** do catálogo de Meszaros: diferente de verbetes como "control point", "Testcase Class" ou "substitutable dependency" (autoria própria de Meszaros), esta categoria inteira funciona como índice/pointer para a literatura clássica de refatoração de Fowler — consistente com a lista de refatorações irmãs no rodapé da página (Extract Class, Extract Superclass, Inline Method, Inline Temp, Introduce Explaining Variable, Move Method, Pull Up Method, Rename Method, Replace Conditional With Guard Clause, etc.), nenhuma delas específica de teste.

---

## Entidades Mencionadas

- [[wiki/entities/martin-fowler]] — creditado como autor original da refatoração Extract Method, via seu livro *Refactoring: Improving the Design of Existing Software*
- [[wiki/entities/gerard-meszaros]] — autor do catálogo/site que hospeda este verbete, mas não do conteúdo em si; mesmo padrão "host ≠ autor" já registrado para Extract Interface e outras páginas de Fowler

## Conceitos Tocados

- [[wiki/concepts/extract-method]] — página nova; conceito central desta fonte
- [[wiki/concepts/extract-interface]] — refatoração-irmã de Fowler, citada aqui por contraste: Extract Interface muda vocabulário de tipos, Extract Method extrai comportamento duplicado
- [[wiki/concepts/refatoracao]] — Extract Method como instância concreta do princípio geral de refatoração, já documentado na página-guarda-chuva
- **Test Code Duplication** — motivação prática citada em [[wiki/sources/testcase-class-xunitpatterns]] para aplicar esta refatoração a Test Methods; ainda sem página própria

## Questões Abertas

- **Resolve uma lacuna citada em pelo menos duas fontes**: [[wiki/sources/testcase-class-xunitpatterns]] e [[wiki/concepts/refatoracao]] citavam "Extract Method [Fowler]" sem página própria dedicada — esta ingestão fecha essa lacuna, mas só até o nível de detalhe que o próprio verbete oferece (uma frase de problema, uma de solução), igual ao caso de Extract Interface.
- **A própria fonte se declara desatualizada** ("o conteúdo deste capítulo provavelmente mudou substancialmente" na edição publicada do livro) — tratado aqui como a versão disponível mais primária que se pôde ingerir, não como o texto definitivo de Fowler.
- **Test Utility Method, Testcase Superclass e Test Helper** — os três destinos possíveis para o código extraído por esta refatoração, citados em [[wiki/sources/testcase-class-xunitpatterns]] — seguem sem página própria; candidatos naturais à próxima ingestão do cluster.

---

## Citações Relevantes

> "You have a code fragment (sequence of statements) that can be grouped together."

> "Turn the fragment into a method whose name explains the purpose of the method."

> "From [Ref] Refactoring: Improving the Design of Existing Software."

*(Tradução completa em `raw/extract-method-xunitpatterns.md`.)*
