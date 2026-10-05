---
type: concept
title: "Acoplamento Desejável vs. Indesejável (new)"
aliases: ["quando usar new", "new de domínio vs infraestrutura"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [acoplamento, new, dominio, infraestrutura, injecao-de-dependencia]
skill: tech-mentor-testing
status: draft
---

# Acoplamento Desejável vs. Indesejável

Todo `new` acopla, mas [[wiki/sources/tres-tipos-de-acoplamento-que-impedem-teste-unitario-andre-casciotti]] distingue:

- **Desejável:** tipos do próprio runtime (`List`, strings...) — não precisa testar que funcionam nem trocar por abstração; e **classes de domínio** — o sistema é quem constrói seus objetos de negócio (mesmo com input de tela/sistema externo).
- **Indesejável:** **serviços, utilitários e infraestrutura** (banco, HTTP, disco), que não pertencem ao core nem às regras de negócio. Devem ficar fora do método, atrás de **interface**, e ser injetados ([[wiki/concepts/dependency-injection]], montados numa [[wiki/concepts/composition-root]]).

Critério prático: *se o teste não deveria precisar saber que isso existe, é indesejável.* Combina com [[wiki/concepts/ports-adapters]] e [[wiki/concepts/separation-of-concerns]]. Ver [[wiki/concepts/acoplamento-que-impede-teste-unitario]]; taxonomia mais ampla (apropriado/não apropriado) em [[wiki/concepts/acoplamento]].

## Key sources

- [[wiki/sources/tres-tipos-de-acoplamento-que-impedem-teste-unitario-andre-casciotti]]
