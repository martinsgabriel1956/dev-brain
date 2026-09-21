---
type: concept
title: "Production Bugs"
aliases: ["bugs em produção", "project smell: production bugs", "lost test", "teste perdido", "missing unit test", "untested requirement", "neverfail test"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 2
tags: [testes, test-smell, project-smell, xunit, terminologia]
skill: tech-mentor-testing
status: stub
---

# Production Bugs

Test smell de categoria "Project Smell" do catálogo xUnitPatterns.com de [[wiki/entities/gerard-meszaros]]: bugs demais aparecem em teste formal ou em produção, apesar do esforço em testes automatizados. É uma árvore de causas, não uma causa única — **Infrequently Run Tests** (testes lentos ou instáveis fazem devs pararem de rodá-los localmente) e **Untested Code** são as duas raízes; a segunda se ramifica em **Missing Unit Test** (falta TDD real, só há [[wiki/sources/customer-test-xunitpatterns|customer tests]]) e **Lost Test**.

## Sub-causas

- **Lost Test** — um [[wiki/concepts/test-method|Test Method]] ou uma Testcase Class foi desabilitado ou nunca chegou a ser registrado na suíte. Ver [[wiki/concepts/test-discovery]] para os mecanismos que, quando falham silenciosamente, produzem esse sintoma.
- **Untested Code** — o SUT tem caminhos de código que nenhum teste exercita, tipicamente por incapacidade de controlar **indirect inputs** de um depended-on component (ver [[wiki/concepts/indirect-input-output]]).
- **Untested Requirement** — o SUT tem comportamento (correto ou não) que se manifesta como **indirect output** (efeito colateral) e que nenhum teste observa diretamente; solução apontada é Behavior Verification via [[wiki/concepts/test-doubles|Mock Objects]].
- **Neverfail Test** — um teste que não falha mesmo quando deveria; causas vão de asserção mal codificada a falhas em thread assíncrona que o [[wiki/concepts/test-runner|Test Runner]] não captura.

## Gate de CI depende de uma definição binária de "build falho"

[[wiki/sources/continuous-integration-xunitpatterns]] fecha a peça que faltava para o gate de CI recomendado contra Lost Test: a própria definição de **continuous integration** de Meszaros já estabelece que o build é considerado "falho" se **qualquer** teste falhar, e que consertar o build vira prioridade máxima do time (stop-the-line) até haver um build bem-sucedido de novo. Ver [[wiki/concepts/ci-cd]].

## Status: stub

Criado a partir de uma fonte primária dedicada. As variações individuais (Lost Test, Missing Unit Test, Untested Code, Untested Requirement, Neverfail Test) ainda não têm páginas próprias — ficam documentadas dentro desta página e da fonte até que alguma delas justifique um desdobramento.

## Key Sources

- [[wiki/sources/production-bugs-xunitpatterns]] — **fonte primária dedicada**: sintomas/causa-raiz/solução completos para as cinco sub-causas
- [[wiki/sources/continuous-integration-xunitpatterns]] — define o critério binário de "build falho" e a regra stop-the-line que sustentam o gate de CI contra Lost Test
