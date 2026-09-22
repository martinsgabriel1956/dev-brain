---
type: concept
title: "Developers Not Writing Tests"
aliases: ["desenvolvedores não escrevem testes", "test debt", "dívida de teste"]
date_created: 2026-09-22
date_updated: 2026-09-22
source_count: 4
tags: [testes, test-smell, project-smell, xunit, terminologia, test-debt]
skill: tech-mentor-testing
status: stub
---

# Developers Not Writing Tests

Test smell de categoria "Project Smell" do catálogo xUnitPatterns.com de [[wiki/entities/gerard-meszaros]], irmão de [[wiki/concepts/production-bugs|Production Bugs]] — os dois se citam mutuamente na fonte original. Diferente de smells de código, este é detectado tipicamente por gestão (PM, Scrum master, tech lead), não pelo desenvolvedor lendo o próprio código: o sintoma é "ouvimos dizer que os devs não estão escrevendo testes".

## Test Debt

A fonte cunha o termo **test debt**: não escrever testes para todo código "que poderia quebrar" hipoteca o futuro do time — cada nova feature fica mais lenta de entregar, e refatorar para melhorar o design fica cada vez mais arriscado (por isso, cada vez mais raro). É o mesmo mecanismo de juros compostos já documentado para dívida técnica genérica em [[wiki/concepts/tech-debt-como-ferramenta]], mas nomeado e ancorado especificamente em ausência de cobertura de teste. O termo tem verbete próprio no glossário do catálogo — ver [[wiki/sources/test-debt-xunitpatterns]] para a fonte primária isolada, incluindo a origem do vocabulário de "dívida" (lista Industrial XP) e uma nota sobre colisão terminológica com o uso de "Test Debt" na skill `tech-mentor-testing` (testes de ROI negativo, um mecanismo diferente que compartilha o nome).

## Três causas raiz

- **Falta de tempo** — prazo agressivo, ordem explícita de gestão para "não perder tempo com testes", ou falta de skill/curva de aprendizado ainda não vencida. Solução apontada: ajuste temporário de cronograma até o time internalizar o processo — a partir daí, escrever teste + código leva o mesmo tempo que só código, porque o tempo antes gasto no debugger é reaproveitado.
- **Código difícil de testar** — típico de legado sem suíte completa; remete a [[wiki/concepts/hard-to-test-code|Hard-to-Test Code]], agora com fonte primária dedicada e árvore completa de três sub-causas (Highly Coupled Code, Asynchronous Code, Untestable Test Code).
- **Estratégia errada de automação de testes** — ambiente ou abordagem que produz **Fragile Test** ou **Obscure Test** (ambos ainda sem página própria), demorados demais de escrever. Técnica de investigação recomendada: os "cinco porquês" (Toyota Production System).

## Metas de melhoria gameáveis — aplicação de Goodhart's Law

A fonte alerta explicitamente contra metas de processo mal desenhadas: "escrever 205 testes a mais" pode ser satisfeito sem qualquer ganho real de cobertura, simplesmente dividindo testes existentes em pedaços menores ou clonando-os. A recomendação é mirar metas de nível mais alto (ex.: "redução de X% em código não testado") — aplicação direta de [[wiki/concepts/goodharts-law|Goodhart's Law]] ao contexto de métricas de teste.

## Sintoma observável relacionado: Frequent Debugging

[[wiki/sources/frequent-debugging-xunitpatterns]] descreve o sintoma que a ausência de unit/component tests granulares causa na prática: depuração manual frequente, porque a suíte não tem **Defect Localization** suficiente para apontar sozinha onde um erro está. Ver [[wiki/concepts/frequent-debugging]] — mesma raiz estrutural (testes insuficientes), consequência diferente (custo de localizar bugs em vez de bugs escaparem para produção).

## Status: stub

Criado a partir de uma fonte primária dedicada. **Hard-to-Test Code** já fechou a lacuna (ver [[wiki/concepts/hard-to-test-code]]); **Fragile Test** e **Obscure Test** ainda não têm páginas próprias — candidatas a ingestão futura, já citadas de passagem tanto aqui quanto em [[wiki/sources/production-bugs-xunitpatterns]].

## Relacionado

[[wiki/concepts/production-bugs]] · [[wiki/concepts/tech-debt-como-ferramenta]] · [[wiki/concepts/code-smells]] · [[wiki/concepts/hard-to-test-code]]

## Key Sources

- [[wiki/sources/developers-not-writing-tests-xunitpatterns]] — **fonte primária dedicada**: sintomas/causas/conselhos de troubleshooting completos
- [[wiki/sources/test-debt-xunitpatterns]] — verbete de glossário isolando a definição formal do termo **test debt**, com a origem do vocabulário de "dívida"
- [[wiki/sources/hard-to-test-code-xunitpatterns]] — fonte primária dedicada da causa "código difícil de testar", com árvore completa de três sub-causas
- [[wiki/sources/frequent-debugging-xunitpatterns]] — sintoma observável de testes insuficientes: depuração manual frequente por falta de Defect Localization
