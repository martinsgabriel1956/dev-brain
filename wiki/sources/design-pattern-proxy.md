---
type: source
title: "Padrão de Projeto: Proxy"
aliases: ["proxy pattern video", "renato augusto proxy", "design pattern proxy cache"]
date_created: 2026-05-01
date_updated: 2026-06-05
source_file: /home/nemomartins/Documentos/new/dev-study/raw/design-pattern-proxy.md
source_url: ""
author: "Renato Augusto"
date_published: ""
date_ingested: 2026-06-05
source_count: 0
tags: [proxy-pattern, design-patterns, structural, cache, solid, ocp, srp, decorator-pattern, open-closed, single-responsibility]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Proxy é um interceptador entre cliente e objeto real: implementa a mesma interface, recebe o objeto real no construtor e adiciona uma camada (cache, auth, log, validação) sem modificar nenhum dos dois lados. O cliente nunca sabe se está falando com o Proxy ou com o objeto real. Principal motivação de uso: evitar ferir OCP e SRP ao adicionar infraestrutura fora da classe de negócio e fora do Controller.

## Key Claims

**Claim:** Cache pertence ao Proxy, não ao Controller nem à classe de serviço.
**Evidence:** Controller não deve conter infraestrutura (viola SRP). Modificar a classe de serviço para adicionar cache viola OCP — mexer em código em produção é arriscado. O Proxy encapsula esse comportamento numa classe nova sem tocar em nenhuma das duas.
**Confidence:** alta — demonstrado com exemplo concreto (ReportGenerator + ReportGeneratorProxy).

**Claim:** O Proxy só funciona como substituto transparente se compartilhar a mesma interface do objeto real.
**Evidence:** O Controller depende da interface `IReportGenerator`. Tanto `ReportGenerator` quanto `ReportGeneratorProxy` a implementam — o Controller não muda, só troca qual instância recebe. Isso é LSP em ação.
**Confidence:** alta.

**Claim:** A diferença entre Proxy e Decorator está na motivação, não na estrutura.
**Evidence:** Ambos encapsulam um objeto e implementam a mesma interface. Proxy intercepta acesso e adiciona infraestrutura (cache, controle); Decorator adiciona comportamento funcional em cadeia. Cache não é regra de negócio — é infraestrutura, portanto vai no Proxy.
**Confidence:** alta.

## Fluxo de Execução (exemplo de cache)

```
Cliente → ReportGeneratorProxy.generate()
            ├── cache HIT  → retorna dado do cache (imediato)
            └── cache MISS → chama ReportGenerator.generate() (operação pesada)
                              → armazena no cache (TTL 1h)
                              → retorna resultado
```

## Entities & Concepts Touched

- [[concepts/proxy-pattern]]
- [[concepts/decorator-pattern]]
- [[concepts/cache-layer]]
- [[concepts/lazy-initialization]]
- [[concepts/open-closed-principle]]
- [[concepts/single-responsibility-principle]]
- [[concepts/design-patterns]]
- [[entities/gang-of-four]]
- [[entities/renato-augusto]]

## Open Questions

- Em que momento o Proxy vira over-engineering vs. quando é a solução certa?
- Como testar unitariamente um proxy com cache sem precisar de infra real?
- Em linguagens sem interfaces explícitas (Go, duck typing), como o Proxy se expressa idiomaticamente?
- Proxy vs. Middleware em frameworks web — quando usar um e quando usar o outro?
