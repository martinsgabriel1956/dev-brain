---
type: concept
title: "Extract Method"
aliases: ["extrair método"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 2
tags: [refactoring, testes, test-code-duplication]
skill: tech-mentor-testing
status: stub
---

# Extract Method

Refatoração catalogada por [[wiki/entities/martin-fowler|Fowler]] (*Refactoring: Improving the Design of Existing Software*): você tem um fragmento de código (sequência de instruções) que pode ser agrupado — a solução é transformá-lo num método cujo nome explique seu propósito. Diferente de [[wiki/concepts/extract-interface|Extract Interface]], que é uma refatoração estrutural de **tipos**, Extract Method ataca duplicação de **comportamento**: nomeia e isola uma sequência de instruções repetida ou repetível.

## Papel em testes: eliminar Test Code Duplication

Fonte primária: [[wiki/sources/extract-method-xunitpatterns]]. Citada em [[wiki/sources/testcase-class-xunitpatterns]] como a técnica recomendada para evitar **Test Code Duplication** entre [[wiki/concepts/test-method|Test Methods]]: o código comum extraído vira um **Test Utility Method**, que pode ficar na própria [[wiki/concepts/testcase-object|Testcase Class]] ou ser movido para uma **Testcase Superclass** ou um **Test Helper** — nenhum dos dois com página própria ainda.

## Status: stub

Fonte disponível é minimalista (problema + solução em uma frase cada, sem mecânica passo a passo) — a própria página original se declara desatualizada em relação ao capítulo publicado do livro de Fowler, mesma ressalva já registrada para [[wiki/concepts/extract-interface]]. Candidata a expansão se uma fonte mais detalhada (o capítulo do livro, ou um exemplo de código) for ingerida.

## Key Sources

- [[wiki/sources/extract-method-xunitpatterns]] — verbete de "Code Refactorings" do xUnitPatterns.com, conteúdo atribuído a Fowler: definição formal do problema e da solução
- [[wiki/sources/testcase-class-xunitpatterns]] — cita a refatoração de passagem, como técnica para evitar Test Code Duplication entre Test Methods
