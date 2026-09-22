---
type: concept
title: "Production Bugs"
aliases: ["bugs em produção", "project smell: production bugs", "lost test", "teste perdido", "missing unit test", "untested requirement", "neverfail test"]
date_created: 2026-09-21
date_updated: 2026-09-22
source_count: 6
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
- **Neverfail Test** — um teste que não falha mesmo quando deveria; causas vão de asserção mal codificada a falhas em thread assíncrona que o [[wiki/concepts/test-runner|Test Runner]] não captura. A solução apontada — refatorar para **Humble Executable** — é a mesma família **Humble Object** citada em [[wiki/sources/hard-to-test-code-xunitpatterns]] como solução geral para código assíncrono difícil de testar (ver [[wiki/concepts/hard-to-test-code]]): duas fontes independentes agora convergem no mesmo padrão sem que ele tenha página própria.

## Infrequently Run Tests também alimenta um Behavior Smell irmão

[[wiki/sources/frequent-debugging-xunitpatterns]] cita a mesma sub-causa **Infrequently Run Tests** por um ângulo diferente: em vez de deixar bugs escaparem para produção, rodar os testes raramente faz um bug, quando finalmente detectado, ficar mais caro de *localizar* — perde-se a memória de qual mudança recente o introduziu. Ver [[wiki/concepts/frequent-debugging]], primeira fonte da wiki para a subcategoria "Behavior Smells" do catálogo (irmã de Code Smells e Project Smells). A mesma fonte também cita **Untested Requirement** num cenário adjacente: teste manual do usuário revela um problema que nenhum customer test expõe.

## Smell-irmão: Developers Not Writing Tests

[[wiki/sources/developers-not-writing-tests-xunitpatterns]] é o outro Project Smell do catálogo, citado de passagem nesta própria página original ("Ambos os casos estão relacionados a *Developers Not Writing Tests*"). Enquanto Production Bugs é o sintoma observável (bugs demais aparecendo), [[wiki/concepts/developers-not-writing-tests]] é a causa de nível de projeto — a ausência de testes que gera esses bugs, cunhada pela fonte como **test debt**. Ver também [[wiki/concepts/tech-debt-como-ferramenta]] para o mecanismo genérico de dívida técnica do qual test debt é um caso específico.

## Gate de CI depende de uma definição binária de "build falho"

[[wiki/sources/continuous-integration-xunitpatterns]] fecha a peça que faltava para o gate de CI recomendado contra Lost Test: a própria definição de **continuous integration** de Meszaros já estabelece que o build é considerado "falho" se **qualquer** teste falhar, e que consertar o build vira prioridade máxima do time (stop-the-line) até haver um build bem-sucedido de novo. Ver [[wiki/concepts/ci-cd]].

## Status: stub

Criado a partir de uma fonte primária dedicada. As variações individuais (Lost Test, Missing Unit Test, Untested Code, Untested Requirement, Neverfail Test) ainda não têm páginas próprias — ficam documentadas dentro desta página e da fonte até que alguma delas justifique um desdobramento.

## Key Sources

- [[wiki/sources/production-bugs-xunitpatterns]] — **fonte primária dedicada**: sintomas/causa-raiz/solução completos para as cinco sub-causas
- [[wiki/sources/continuous-integration-xunitpatterns]] — define o critério binário de "build falho" e a regra stop-the-line que sustentam o gate de CI contra Lost Test
- [[wiki/sources/developers-not-writing-tests-xunitpatterns]] — smell-irmão citado de passagem na fonte original; cunha o termo "test debt" como causa de nível de projeto por trás dos bugs em produção
- [[wiki/sources/hard-to-test-code-xunitpatterns]] — segunda fonte a citar o padrão Humble Object, agora para código assíncrono em geral (não só Neverfail Test)
- [[wiki/sources/frequent-debugging-xunitpatterns]] — segunda ocorrência independente de Infrequently Run Tests, agora como causa de depuração manual cara em vez de bug escapando para produção; cenário adjacente de Untested Requirement
- [[wiki/sources/test-driven-bug-fixing-xunitpatterns]] — a resposta formalizada para o cenário de Untested Requirement: escrever o unit test que reproduz o bug antes de depurar e corrigir
