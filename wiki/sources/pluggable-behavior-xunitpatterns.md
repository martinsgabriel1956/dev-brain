---
type: source
title: "Pluggable Behavior (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["pluggable behavior xunitpatterns", "external patterns pluggable behavior", "SBPP citation xunitpatterns"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: /home/nemomartins/Documentos/new/dev-study/raw/pluggable-behavior-xunitpatterns.md
source_url: "http://xunitpatterns.com/Pluggable%20Behavior.html"
author: "Gerard Meszaros (verbete de citação); Kent Beck — *Smalltalk Best Practice Patterns* [SBPP] (definição original parafraseada)"
date_published: 2011-02-09
date_ingested: 2026-09-21
source_count: 0
tags: [design-patterns, pluggable-behavior, smalltalk, kent-beck, xunit, external-patterns, fonte-primaria, reflection]
skill: tech-mentor-testing
status: stable
---

# Pluggable Behavior (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Terceira entrada da categoria **External Patterns** do catálogo xUnitPatterns.com ingerida na wiki, depois de [[wiki/sources/decorator-xunitpatterns]] e [[wiki/sources/command-xunitpatterns]] — mesmo formato de citação minimalista, mas com uma diferença importante: em vez de citar o GOF, parafraseia **Kent Beck** (*Smalltalk Best Practice Patterns* [SBPP]). Fecha uma lacuna sinalizada explicitamente como open question em [[wiki/sources/testcase-object-xunitpatterns]] (nota 2 das "Open Questions"): aquela fonte citava "Pluggable Behavior [SBPP]" de passagem, como o mecanismo pelo qual um [[wiki/concepts/testcase-object|Testcase Object]] recebe o nome do [[wiki/concepts/test-method|Test Method]] a invocar, sem nunca definir formalmente o padrão em si. Esta fonte fornece exatamente essa definição, incluindo uma distinção que a fonte do Testcase Object não fazia: **Pluggable (Method) Selector** (escolher entre métodos existentes) vs. **Pluggable Block** (injetar um bloco de código arbitrário).

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Pluggable Behavior é uma variável adicionada a um objeto para disparar comportamento diferente em runtime | "Add a variable that will be used to trigger different behavior." | fonte primária (Meszaros/Beck) | alta |
| É preferível a criar dezenas de subclasses que diferem em um ou dois métodos | "Using Pluggable Behavior is a much better solution than creating a hundred different subclasses, each differing from each other in only one or two methods." | fonte primária | alta |
| Existem duas formas comuns de implementar o padrão: Pluggable (Method) Selector e Pluggable Block | "There are two common ways to implement Pluggable Behavior. Pluggable (Method) Selector lets us choose which existing method of the class to run while Pluggable Block lets the creator of the object specify an arbitrary block of code to run." | fonte primária | alta |
| A definição é parafraseada do livro de Kent Beck, não formulação original de Meszaros | "Paraphrased from Kent Beck's book 'Smalltalk Best Practice Patterns' [SBPP]." | fonte primária (citação) | alta |

---

## Key Claims

### 1. Fecha a lacuna de definição deixada por Testcase Object
[[wiki/sources/testcase-object-xunitpatterns]] descrevia o mecanismo de despacho do Testcase Object (construtor recebe o nome do Test Method, `run` usa reflection para invocá-lo) e citava "Pluggable Behavior [SBPP]" como o nome do padrão por trás — sem definir o padrão nem identificar qual das duas variações estava em jogo. Esta fonte permite classificar precisamente: o Testcase Object usa **Pluggable (Method) Selector** (escolhe entre métodos já existentes da classe pelo nome), não Pluggable Block (nenhum bloco de código é passado ao construtor, apenas uma string com o nome do método).

### 2. Duas variações distintas, uma só citada de passagem em outras fontes
A wiki já tinha registrado o mecanismo de reflection + nome de método (Pluggable Method Selector, na prática), mas nunca havia mencionado **Pluggable Block** — a variação onde o criador do objeto injeta um bloco de código arbitrário em vez de escolher entre métodos nomeados. Essa segunda variação é conceitualmente mais próxima do [[wiki/concepts/command-pattern|Command Pattern]] (objetificar uma ação para executá-la depois) do que do despacho por nome usado no Testcase Object.

### 3. Origem em Kent Beck, não no GOF — terceira fonte diferente na categoria External Patterns
Ao contrário de [[wiki/sources/command-xunitpatterns]] e [[wiki/sources/decorator-xunitpatterns]] (ambas citações diretas do GOF), esta entrada parafraseia [[wiki/entities/kent-beck|Kent Beck]] e seu livro *Smalltalk Best Practice Patterns* [SBPP] — reforça a origem Smalltalk já registrada na wiki para o vocabulário de testes xUnit (SUnit, framework caseiro de Beck) e mostra que a categoria External Patterns do site não se limita a citar o GOF.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete de citação
- [[wiki/entities/kent-beck]] — autor da definição original parafraseada, em *Smalltalk Best Practice Patterns* [SBPP]

## Conceitos Tocados

- [[wiki/concepts/pluggable-behavior]] — página nova, criada a partir desta fonte
- [[wiki/concepts/testcase-object]] — recebe a definição formal do padrão que já usava sem citar; resolve a open question 2 registrada na fonte
- [[wiki/concepts/test-method]] — beneficiário indireto: o despacho do Test Method certo agora tem definição formal do mecanismo por trás
- [[wiki/concepts/command-pattern]] — comparado explicitamente: Pluggable Block é a variação conceitualmente mais próxima
- [[wiki/concepts/strategy-pattern]] — comparado explicitamente: mesma motivação (evitar subclasses/if-else para variar comportamento), mecanismo mais leve

## Questões Abertas

- O livro *Smalltalk Best Practice Patterns* [SBPP] em si não tem página própria na wiki — candidato a stub numa ingestão futura que leia mais do catálogo de padrões de Beck.
- Assim como em [[wiki/sources/command-xunitpatterns]] e [[wiki/sources/decorator-xunitpatterns]], as demais ~40 entradas da categoria "External Patterns" seguem majoritariamente não ingeridas.

---

## Citações Relevantes

> "Add a variable that will be used to trigger different behavior."

> "Using Pluggable Behavior is a much better solution than creating a hundred different subclasses, each differing from each other in only one or two methods."

> "Pluggable Behavior lets us specify the behavior of an object at runtime. There are two common ways to implement Pluggable Behavior. Pluggable (Method) Selector lets us choose which existing method of the class to run while Pluggable Block lets the creator of the object specify an arbitrary block of code to run."

> "Paraphrased from Kent Beck's book 'Smalltalk Best Practice Patterns' [SBPP]."

*(Tradução completa em `raw/pluggable-behavior-xunitpatterns.md`.)*
