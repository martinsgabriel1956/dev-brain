---
type: source
title: "Architecture Fitness Functions"
aliases: ["fitness functions", "architecture fitness functions", "evolutionary architecture", "archunit", "deptrac"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/architecture-fitness-functions.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [fitness-functions, evolutionary-architecture, archunit, deptrac, ci, architecture-testing]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Fitness Functions são testes automatizados que validam restrições arquiteturais — conceito de *Building Evolutionary Architectures* (Ford, Parsons, Kua). Em vez de ADRs que ninguém lê, você escreve testes que quebram o build se a regra for violada. Ferramentas: ArchUnit (Java/Kotlin), Deptrac (TypeScript/PHP via YAML), k6 para performance em CI. Executadas em CI/CD, não em produção.

## Key Claims

**Claim:** Fitness Functions transformam decisões arquiteturais em testes executáveis — ADRs que se auto-validam.
**Evidence:** ADR "sem dependências circulares entre camadas" pode ser ignorado. Fitness function com ArchUnit: `noClasses().that().resideInPackage("..domain..").should().dependOnClassesThat().resideInPackage("..infrastructure..")` — quebra o build se violado. Regra sobrevive ao crescimento do codebase.
**Confidence:** alta

**Claim:** Fitness Functions cobrem diferentes dimensões: estruturais, de performance, de segurança e de cobertura.
**Evidence:** Estrutural: ArchUnit/Deptrac para dependências entre camadas. Performance: k6 em CI com threshold (p95 < 200ms). Segurança: check de dependências com known vulnerabilities. Cobertura: coverage mínimo de 70%. Cada uma automatiza uma preocupação arquitetural.
**Confidence:** alta

**Claim:** Deptrac é a melhor opção para TypeScript — define regras de dependência em YAML, sem código Java.
**Evidence:** ArchUnit requer JVM. Deptrac: YAML define layers (Domain, UseCase, Infrastructure) e allowed dependencies. Integra com GitHub Actions. Output: lista de violations com arquivo e linha. Mais acessível para times Node.js/TypeScript.
**Confidence:** média

## Entities & Concepts Touched

- [[concepts/fitness-functions]]
- [[concepts/evolutionary-architecture]]
- [[entities/archunit]]
- [[entities/deptrac]]
- [[concepts/clean-architecture]]
- [[concepts/adr]]

## Open Questions

- Fitness functions para microserviços distribuídos — como testar contratos entre serviços em CI sem subir todo o ambiente?
- Deptrac em monorepos grandes (100+ pacotes) — performance e configuração de múltiplas regras?
