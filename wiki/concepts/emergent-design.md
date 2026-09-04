---
type: concept
title: "Emergent Design"
aliases: ["design emergente", "emergent design"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_count: 4
tags: [testes, tdd, design, xunit, bduf]
skill: tech-mentor-testing
status: stable
---

# Emergent Design

Termo do glossário do xUnitPatterns.com ([[wiki/entities/gerard-meszaros]]), com verbete próprio dedicado em [[wiki/sources/emergent-design-xunitpatterns]]: o **oposto formal de [[wiki/concepts/bduf|BDUF]]** (Big Design, Up Front). Consiste em deixar o design certo ser **descoberto** à medida que o software evolui lentamente para passar em **um teste de cada vez** durante o [[wiki/concepts/tdd|test-driven development]] — em vez de o design ser definido antecipadamente.

É essa característica que distingue [[wiki/concepts/tdd|test-driven development]] de [[wiki/concepts/test-first-development|test-first development]], termo mais genérico que só implica "escrever o teste antes", sem exigir incrementalidade teste-a-teste.

Ver a discussão informal já existente em [[wiki/concepts/tdd]] ("As duas escolas") — a escola London/Mockist é descrita como tendo "o design emerge das interfaces que o teste exige", mesma ideia, agora com termo e fonte primária formais.

## Key Sources

- [[wiki/sources/emergent-design-xunitpatterns]] — **fonte primária dedicada**: define o termo diretamente e nomeia o oposto formal, [[wiki/concepts/bduf|BDUF]]
- [[wiki/sources/bduf-xunitpatterns]] — fonte primária do termo-oposto: confirma BDUF diretamente, fechando o par de contraste com fonte dedicada dos dois lados
- [[wiki/sources/test-driven-development-xunitpatterns]] — cita o termo, cunhado por contraste com test-first development
- [[wiki/sources/test-first-development-xunitpatterns]] — confirma, pelo lado do termo-irmão test-first, que essa é a característica que TDD acrescenta e test-first não exige
