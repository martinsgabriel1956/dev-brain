---
type: source
title: "Micro-Kernel Architecture"
aliases: ["micro kernel", "microkernel", "plugin architecture", "extensible architecture", "core system plugins"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/micro-kernel.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [micro-kernel, plugin-architecture, extensibility, core-system, registry, architecture-styles]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Micro-Kernel Architecture: core system mínimo + plugins que estendem funcionalidade. Core define o contrato (interface/API) que plugins implementam. Registry gerencia plugins dinamicamente. Usado em: IDEs (VS Code), browsers (extensões), CMS, ferramentas de pipeline (Webpack). Trade-off: extensibilidade alta vs complexidade de versioning do contrato.

## Key Claims

**Claim:** Micro-kernel separa o core estável das extensões variáveis — core evolui lentamente, plugins evoluem rápido.
**Evidence:** Core: autenticação, roteamento básico, plugin registry. Plugin: lógica de negócio específica, integrações externas, features opcionais. Quando um plugin falha, o core continua funcionando. Novo plugin adicionado sem modificar o core. VS Code: editor é o core; Language Server Protocol + extensões são os plugins.
**Confidence:** alta

**Claim:** O contrato do plugin é o ponto mais crítico — difícil de evoluir sem quebrar plugins existentes.
**Evidence:** Plugin contract v1: `execute(context: Context): void`. Mudança para v2: `execute(context: Context, options: Options): Promise<void>`. Quebra todos os plugins v1. Solução: versioning explícito no contrato, backward compatibility por tempo limitado, semver no plugin registry. Investir em contrato estável no início é mais barato que migrar plugins depois.
**Confidence:** alta

**Claim:** Micro-kernel é adequado quando o sistema precisa ser extensível por terceiros ou times independentes.
**Evidence:** Time central define o core e o contrato. Times de produto constroem plugins independentemente. Deploy independente por plugin. Alternativa inadequada: monolito onde toda extensão requer modificação do core e redeploy completo. Casos: plataformas de e-commerce com plugins de pagamento, CMS com plugins de conteúdo.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/micro-kernel]]
- [[concepts/plugin-architecture]]
- [[concepts/extensibility]]
- [[concepts/registry-pattern]]
- [[concepts/hexagonal-architecture]]

## Open Questions

- Micro-kernel com plugins isolados em processos separados (IPC) vs in-process — quando o isolamento de processo vale o overhead?
- Versionamento de contrato de plugin em sistema com 100+ plugins externos — como deprecar versões antigas sem quebrar o ecossistema?
