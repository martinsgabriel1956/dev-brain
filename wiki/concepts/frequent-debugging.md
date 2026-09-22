---
type: concept
title: "Frequent Debugging"
aliases: ["manual debugging", "depuração manual", "depuração frequente"]
date_created: 2026-09-22
date_updated: 2026-09-22
source_count: 3
tags: [testes, test-smell, behavior-smell, xunit, terminologia, defect-localization]
skill: tech-mentor-testing
status: stub
---

# Frequent Debugging

Test smell de categoria "Behavior Smell" do catálogo xUnitPatterns.com de [[wiki/entities/gerard-meszaros]] — irmão de Assertion Roulette, Erratic Test, Fragile Test, Manual Intervention e Slow Tests, e a primeira fonte dessa subcategoria a entrar na wiki (as outras duas já documentadas são Code Smells, com [[wiki/concepts/hard-to-test-code]], e Project Smells, com [[wiki/concepts/production-bugs]] e [[wiki/concepts/developers-not-writing-tests]]). Também conhecido como **Manual Debugging**: precisar de um debugger interativo ou de prints espalhados pelo código para entender a maioria das falhas de teste, em vez de a própria falha (mensagem ou padrão) já indicar a causa.

## Test error como caso de alta Defect Localization por natureza

[[wiki/sources/test-error-xunitpatterns]], verbete de glossário do mesmo catálogo, afirma que um **test error** (erro que impede o teste de rodar até a conclusão, ex.: exceção não tratada) é "muito mais fácil de depurar" que uma [[wiki/sources/test-failure-xunitpatterns|test failure]] justamente porque a causa "tende a ser muito mais local ao ponto onde o test error ocorre" — o oposto exato do smell descrito nesta página. Um stack trace de exceção já entrega boa parte da Defect Localization de graça; é a ausência dessa localidade (asserção divergente sem indício de onde/por quê) que empurra em direção à depuração manual documentada abaixo.

## Causa raiz: falta de Defect Localization

O smell é sintoma de que a suíte carece de **Defect Localization** — a propriedade de um teste que falha já indicar, sozinho, o que quebrou. Duas causas nomeadas levam a essa lacuna:

- **Unit tests ou component tests insuficientes** — falta granularidade para isolar um erro de lógica numa classe individual, ou um erro de integração num cluster de classes ([[wiki/concepts/production-bugs|component]]). Agravado quando [[wiki/concepts/test-doubles|Mock Objects]] substituem depended-on objects extensivamente, mas os unit tests desses objetos não batem com o comportamento programado nos mocks — o mock "passa" localmente sem refletir o comportamento real do DOC.
- **[[wiki/concepts/production-bugs|Infrequently Run Tests]]** — mesma sub-causa já documentada para Production Bugs, aqui usada por outro ângulo: não é que o bug escape para produção, é que ele fica mais caro de *localizar* quando finalmente aparece, porque a memória de qual mudança o introduziu já se perdeu. Rodar os testes a cada pequena alteração preserva essa memória.

## Impacto

Depuração manual é lenta e imprevisível — uma única sessão pode estender o prazo de entrega em meio dia ou mais, além do risco de deixar passar despercebido um indício sutil do problema.

## Solução: test-driven development verdadeiro

A fonte aponta [[wiki/concepts/tdd|test-driven development]] verdadeiro (não apenas test-first) como a solução central, combinado com [[wiki/concepts/storytest-driven-development|storytest-driven development]] para cobrir também a camada de component test — unit tests para classes individuais mais component tests para os clusters relacionados. Quando o gatilho foi um teste manual de usuário revelando um problema, o cenário é provavelmente **Untested Requirement** (sub-causa de [[wiki/concepts/production-bugs|Production Bugs]]); a resposta recomendada é escrever o teste automatizado que exporia o problema e então aplicar [[wiki/sources/test-driven-bug-fixing-xunitpatterns|test-driven bug fixing]] — agora com fonte primária própria: escrever o unit test que reproduz o bug antes de depurar e corrigir, formalizado como a extensão do TDD para correção de defeitos.

## Relacionado

[[wiki/concepts/production-bugs]] · [[wiki/concepts/developers-not-writing-tests]] · [[wiki/concepts/test-doubles]] · [[wiki/concepts/tdd]] · [[wiki/concepts/test-runner]] · [[wiki/concepts/code-smells]]

## Status: stub

Criado a partir de uma fonte primária dedicada. **Defect Localization** e **Assertion Message** são citados como conceitos centrais mas ainda sem página própria — candidatos a ingestão futura. **Component test** como categoria (entre unit test e customer test) segue sem página conceitual própria apesar de citada em múltiplas fontes.

## Key Sources

- [[wiki/sources/frequent-debugging-xunitpatterns]] — **fonte primária dedicada**: sintomas, duas causas raiz e solução completos
- [[wiki/sources/test-driven-bug-fixing-xunitpatterns]] — fecha a referência ao termo "test-driven bug fixing" citado sem fonte própria na solução acima
- [[wiki/sources/test-error-xunitpatterns]] — verbete de glossário que afirma explicitamente a relação inversa: test error tem causa mais local (alta Defect Localization por natureza), test failure não
