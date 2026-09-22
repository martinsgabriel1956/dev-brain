---
type: concept
title: "Hard-to-Test Code"
aliases: ["código difícil de testar", "highly coupled code", "hard-coded dependency", "código altamente acoplado"]
date_created: 2026-09-22
date_updated: 2026-09-22
source_count: 1
tags: [testes, test-smell, xunit, terminologia, acoplamento, testabilidade]
skill: tech-mentor-testing
status: stub
---

# Hard-to-Test Code

Test smell de categoria "Test Smells" do catálogo xUnitPatterns.com de [[wiki/entities/gerard-meszaros]], irmão de Obscure Test, Conditional Test Logic, Test Code Duplication e Test Logic in Production. É a segunda das três causas raiz de [[wiki/concepts/developers-not-writing-tests|test debt]] já citada de passagem antes de ganhar fonte primária: código que dificulta escrever **Fully Automated Test** de forma economicamente eficiente. GUI, código multi-thread e o próprio código de teste são exemplos citados de cara pela fonte.

## Três causas raiz

- **Highly Coupled Code** (a.k.a. Hard-Coded Dependency) — uma classe não pode ser testada sem arrastar várias outras junto, porque não executa isoladamente. Causa raiz: design ruim, falta de experiência em OO, ou falta de incentivo ao desacoplamento. Solução: quebrar o acoplamento — surge naturalmente ao fazer test-driven development, ou explicitamente via [[wiki/concepts/test-doubles|Test Double]]/Test Stub/Mock Object. Retrofit em legado é mais desafiador — a fonte cita o livro "Working Effectively with Legacy Code" de Michael Feathers como referência dedicada ao tema.
- **Asynchronous Code** — o teste não pode chamar o método diretamente; precisa iniciar um executável (thread/processo/aplicação) e esperar sua inicialização antes de interagir. Isso adiciona complexidade e lentidão — crítico para testes unitários, que precisam rodar rápido. Solução: separar a lógica do mecanismo de acesso assíncrono via padrão **Humble Object** (incluindo Humble Dialog e Humble Executable) — mesmo padrão já citado em [[wiki/concepts/production-bugs]] para Neverfail Test, ainda sem página própria.
- **Untestable Test Code** — o corpo do próprio Test Method é obscuro (Obscure Test) ou tem Conditional Test Logic suficiente para o teste em si precisar ser questionado. Causa raiz: testar o corpo do teste exigiria substituir o SUT por um Test Double e rodar dentro de outro Expected Exception Test — trabalho demais para valer a pena. Solução: manter o Test Method extremamente simples, extraindo qualquer lógica condicional para Test Utility Methods.

## Relacionado

[[wiki/concepts/developers-not-writing-tests]] · [[wiki/concepts/test-doubles]] · [[wiki/concepts/production-bugs]] · [[wiki/concepts/code-smells]]

## Status: stub

Criado a partir de uma fonte primária dedicada. **Humble Object**, **Obscure Test** e **Conditional Test Logic** seguem sem página própria — candidatos a ingestão futura, agora citados em múltiplas fontes convergentes.

## Key Sources

- [[wiki/sources/hard-to-test-code-xunitpatterns]] — **fonte primária dedicada**: três causas raiz completas, cada uma com sintoma/impacto/causa-raiz/solução
