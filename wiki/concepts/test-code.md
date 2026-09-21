---
type: concept
title: "Test Code"
aliases: ["código de teste"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 1
tags: [testes, xunit, terminologia, test-code, production-code]
skill: tech-mentor-testing
status: stub
---

# Test Code

Termo do glossário de [[wiki/entities/gerard-meszaros]] ([[wiki/sources/test-code-xunitpatterns]]) para **todo código escrito especificamente para testar outro código** — o teste em si, em oposição ao código sendo testado. É o contraponto direto de [[wiki/concepts/production-code|production code]]: o par cobre a totalidade de qualquer base de código sob essa taxonomia.

## Definição e a cláusula não óbvia

Ao contrário de "production code" — que Meszaros precisou justificar tomando emprestado o nome do ambiente de produção — "test code" é tratado como autoexplicativo. A única cláusula não trivial da definição é que o código testado pelo test code **não precisa ser production code**: pode ser *outro test code*. Ou seja, um teste pode existir para verificar outro teste (ex.: um [[wiki/concepts/test-doubles|test double]] customizado, que é ele próprio test code, mas pode precisar de teste próprio).

## Onde o termo aparece implicitamente na wiki

O par test code / production code é o pressuposto silencioso por trás de todo o vocabulário SUT/DOC documentado em [[wiki/concepts/test-doubles]] e [[wiki/concepts/indirect-input-output]]: o **SUT** e o **DOC** são sempre production code; o que os exercita e verifica é test code.

## Ver também

- [[wiki/concepts/production-code]] — contraponto formal do termo
- [[wiki/concepts/test-doubles]] — SUT/DOC como production code; o double substitui um DOC durante a execução do test code

## Key Sources

- [[wiki/sources/test-code-xunitpatterns]] — fonte primária dedicada ao termo; origem e definição formal
