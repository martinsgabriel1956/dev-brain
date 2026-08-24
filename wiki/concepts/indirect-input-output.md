---
type: concept
title: "Entrada e Saída Indireta (Indirect Input / Indirect Output)"
aliases: ["indirect input", "indirect output", "entrada indireta", "saída indireta", "control point", "observation point", "ponto de controle", "ponto de observação", "direct input", "entrada direta"]
date_created: 2026-08-21
date_updated: 2026-08-23
source_count: 4
tags: [testes, test-doubles, sut, doc, terminologia, xunit]
skill: tech-mentor-testing
status: stub
---

# Entrada e Saída Indireta (Indirect Input / Indirect Output)

Par de termos do vocabulário formal de [[wiki/entities/gerard-meszaros]] ([[wiki/sources/test-double-xunitpatterns-meszaros]]) que explica **por que** existem os cinco tipos de [[wiki/concepts/test-doubles|Test Double]] — o eixo é a direção do dado entre o **SUT** (*system under test*) e o **DOC** (*depended-on component*, a dependência real que o double substitui).

## As duas direções

- **Entrada indireta** (*indirect input*) — valor que o SUT **recebe** de um DOC e que afeta seu comportamento. Fonte primária: [[wiki/sources/indirect-input-xunitpatterns]]. Formas concretas: retorno de função, parâmetro de saída (out) atualizado, ou erro/exceção levantado pelo DOC.
- **Saída indireta** (*indirect output*) — chamada ou efeito que o SUT **dispara** sobre um DOC, observável de fora.

A contraparte de entrada indireta é a **entrada direta** (*direct input*): um valor passado explicitamente ao SUT pelo próprio teste (ex.: argumento de método), sem passar por nenhum DOC.

## Pontos de controle e de observação

Testar cada direção exige um ponto de acesso diferente "na parte de trás" do SUT:

| Direção | Ponto de acesso | Double típico |
|---|---|---|
| Entrada indireta | **control point** (ponto de controle) | [[wiki/concepts/test-doubles\|Stub]] — injeta o valor controlado |
| Saída indireta | **observation point** (ponto de observação) | [[wiki/concepts/test-doubles\|Spy ou Mock]] — registra ou verifica a chamada |

Esse eixo controle × observação é o mesmo já sintetizado em [[wiki/concepts/test-doubles]] a partir da fonte primária de Test Double — este conceito isola especificamente o vocabulário de entrada/saída, já que agora há uma fonte primária dedicada só a "indirect input" ([[wiki/sources/indirect-input-xunitpatterns]]).

## Control point é mais amplo do que a injeção de indirect input

A fonte primária isolada do próprio termo ([[wiki/sources/control-point-xunitpatterns]]) corrige uma leitura estreita demais: "control point" não é exclusivo da injeção de entrada indireta pelo Stub. A definição formal é "como o teste pede ao SUT para fazer algo por ele" — cobre **qualquer** interação de comando, incluindo o próprio ato de exercitar o SUT (fase **exercise SUT**, o "front door" normal do teste) e a configuração/desmontagem da fixture. O "control point on the back side of the SUT" citado em [[wiki/sources/indirect-input-xunitpatterns]] é um **caso específico** — o usado para configurar um DOC antes do teste — não a definição inteira do termo. A fonte também isola uma regra de design: control points criados **estritamente para viabilizar teste** (ex.: um setter de estado interno, um hook de reset) **não devem ser usados pelo production code**, porque contornam validação de entrada ou encurtam o ciclo de vida normal do SUT/DOC.

## Fixture setup: a fase onde control points entram em cena

A fonte primária isolada do termo fixture setup ([[wiki/sources/fixture-setup-xunitpatterns]]) fecha o outro lado da relação já registrada acima: control points (usados "for the purpose of setting up or tearing down the fixture") são acionados justamente durante a fase de **fixture setup**, a primeira do teste. É nessa fase que o teste configura as precondições — o **test fixture** (ou **test context**), termo que a fonte define como o conjunto coletivo de todos os objetos e seu estado necessários antes do SUT poder ser exercitado. Nomear a fase (fixture setup) separadamente do seu produto (test fixture) é uma distinção fina que faltava na wiki antes desta fonte.

## Por que "examinar e controlar" é a motivação formal

A fonte primária isolada do próprio termo DOC ([[wiki/sources/depended-on-component-doc-xunitpatterns]]) confirma que esse eixo controle/observação não é um detalhe do padrão Test Double — é a razão formal de existir um DOC como conceito: "we need to be able to examine and control its interactions with the SUT to get complete test coverage". Examinar = ponto de observação (saída indireta); controlar = ponto de controle (entrada indireta).

## Por que a distinção importa

Sem esse vocabulário, é fácil descrever "mock" como "stub com asserção" — uma simplificação que a própria fonte primária rejeita (ver [[wiki/sources/test-double-xunitpatterns-meszaros]]). A distinção correta é: Stub controla **entrada** indireta; Mock/Spy observam **saída** indireta. É esse eixo que também organiza a distinção entre [[wiki/concepts/unit-test-solitario-vs-sociavel|estilo de teste London (mocka saída) e Detroit (usa objetos reais, stuba só entrada de I/O externo)]].

## Ver também

- [[wiki/concepts/test-doubles]] — taxonomia completa dos cinco tipos organizados por esse eixo
- [[wiki/concepts/unit-test-solitario-vs-sociavel]] — escolas de TDD mapeadas no mesmo eixo controle/observação
- [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]] — narrow integration test depende de um double fiel o suficiente para as entradas indiretas que fornece

## Questões Abertas

- Os verbetes irmãos "indirect output", "observation point", "direct input" e "fixture teardown" do mesmo glossário xUnitPatterns.com ainda não têm fonte primária própria ingerida — só são conhecidos aqui por inferência a partir de [[wiki/sources/indirect-input-xunitpatterns]] e [[wiki/sources/test-double-xunitpatterns-meszaros]]. "control point" e "fixture setup" já foram ingeridos isoladamente em [[wiki/sources/control-point-xunitpatterns]] e [[wiki/sources/fixture-setup-xunitpatterns]]. Candidatos a ingestão futura para fechar o vocabulário.

## Key Sources

- [[wiki/sources/control-point-xunitpatterns]] — fonte primária isolada do termo control point: definição mais ampla que "back side do SUT", e regra de design sobre control points exclusivos de teste
- [[wiki/sources/fixture-setup-xunitpatterns]] — fonte primária isolada do termo fixture setup: a fase onde control points são acionados; define test fixture/test context como o produto dessa fase
- [[wiki/sources/depended-on-component-doc-xunitpatterns]] — fonte primária do termo DOC; "examinar e controlar" como motivação formal do eixo observação/controle
- [[wiki/sources/indirect-input-xunitpatterns]] — fonte primária de "indirect input"
- [[wiki/sources/test-double-xunitpatterns-meszaros]] — vocabulário completo SUT/DOC/entrada-saída indireta/pontos de controle-observação
