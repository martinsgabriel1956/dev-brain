---
type: concept
title: "Drift Detection"
aliases: []
date_created: 2026-09-22
date_updated: 2026-10-06
source_count: 4
tags: [drift-detection, behavior-drift, llm, infraestrutura]
skill: tech-mentor-infra
status: stub
---

# Drift Detection

Stub criado durante sweep de lint (links quebrados) a partir de referências em 1 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/sources/terraform]]: [[wiki/concepts/drift-detection]]

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

## Dois sentidos do termo

- **Infrastructure drift** (Terraform/IaC): divergência entre o estado real da infraestrutura e o declarado no código — origem das citações acima.
- **Behavior drift de LLM:** mudança no comportamento de um sistema com LLM ao longo do tempo (troca/atualização de modelo, mudança de prompt). Segundo [[wiki/sources/dev-na-era-da-ia-qualidade-esteira-e-novas-preocupacoes]], é verificado com perguntas de teste à LLM (comportamento, vazamento de informação, segurança), **de tempos em tempos** (exemplo: a cada 2 semanas) ou **quando o prompt muda**, e não a cada commit. Ver [[wiki/concepts/ia-na-esteira-ci-cd]] e [[wiki/concepts/llm-evals-testing]].

## Versão Ativa Rastreável

Saber qual versão de prompt está ativa e o que mudou ([[wiki/concepts/metadados-de-prompt]]) é pré-condição para diagnosticar mudança de comportamento ([[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]]).

## Key sources

- [[wiki/sources/terraform]]
- [[wiki/sources/dev-na-era-da-ia-qualidade-esteira-e-novas-preocupacoes]] — sentido de behavior drift de LLM e cadência de verificação
- [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]] — rastreabilidade de versão como base para investigar mudança de comportamento
- [[wiki/sources/migrations-flyway-spring-boot-versionamento-de-banco]] — [[wiki/concepts/drift-de-schema-entre-ambientes]]: o equivalente em banco de dados (alteração manual fora do código)
