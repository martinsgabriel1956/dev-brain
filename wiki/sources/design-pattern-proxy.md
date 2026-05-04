---
type: source
title: "Padrão de Projeto: Proxy"
aliases: ["proxy pattern", "design pattern proxy"]
date_created: 2026-05-01
date_updated: 2026-05-01
source_file: /home/nemomartins/Documentos/new/dev-study/raw/design-pattern-proxy.md
source_url: https://refactoring.guru/pt-br/design-patterns/proxy
author: Renato Augusto
date_published: null
date_ingested: 2026-05-01
tags: [design-patterns, structural, proxy, cache, solid, oop]
skill: tech-mentor-backend
status: stable
---

## TL;DR

O padrão Proxy insere um objeto intermediário entre o cliente e o objeto real, permitindo controlar o acesso e adicionar comportamentos (cache, log, validação, controle de acesso) sem modificar a classe original e sem poluir o código cliente.

## Problema Central

Uma classe `ReportGenerator` com lógica pesada demorava 5 segundos por requisição. Onde adicionar cache sem violar SRP (não no Controller) e sem violar OCP (não na classe original)?

**Resposta:** criar `ReportGeneratorProxy` que encapsula o `ReportGenerator` real e adiciona a camada de cache.

## Afirmações-chave

| Afirmação | Evidência | Confiança |
|---|---|---|
| Proxy é um padrão estrutural | Catalogado pelo GoF | Alta |
| Proxy serve como substituto/espaço reservado | Definição do padrão | Alta |
| Ambos devem implementar a mesma interface | Necessário para LSP — cliente não distingue proxy do real | Alta |
| Diferente do Decorator, que decora em cadeia | Decorator tem motivação de extensão; Proxy tem motivação de controle de acesso | Alta |
| Aplicável a cache, log, validação, lazy init, controle de acesso | Listado no Refactoring Guru e demonstrado no exemplo | Alta |

## Fluxo de Execução (exemplo de cache)

```
Cliente → ReportGeneratorProxy.generate()
            ├── cache HIT  → retorna dado do cache (imediato)
            └── cache MISS → chama ReportGenerator.generate() (5s)
                              → armazena no cache (TTL 1h)
                              → retorna resultado
```

## Conceitos e Entidades Relacionados

- [[proxy-pattern]] — conceito principal
- [[structural-patterns]] — categoria do padrão
- [[cache-layer]] — uso mais comum demonstrado
- [[open-closed-principle]] — razão para não modificar a classe original
- [[single-responsibility-principle]] — razão para não colocar cache no Controller
- [[liskov-substitution-principle]] — interface compartilhada garante substituição
- [[decorator-pattern]] — padrão similar com motivação diferente
- [[facade-pattern]] — padrão similar mencionado
- [[adapter-pattern]] — padrão similar mencionado
- [[repository-pattern]] — padrão de infraestrutura usado no exemplo
- [[lazy-initialization]] — caso de uso do Proxy
- [[gang-of-four]] — autores do catálogo oficial
- [[refactoring-guru]] — referência de estudo

## Perguntas em Aberto

- Em que momento o Proxy vira over-engineering vs. quando é a solução certa?
- Como testar unitariamente um proxy com cache sem precisar de infra real?

## Citações Relevantes

> "Padrão de projeto proxy é como se fosse um interceptador — do código cliente eu não consigo conversar diretamente com a classe que eu queria, tenho que passar por um proxy primeiro."

> "A gente pode fazer diversas coisas como cache, log, validação... esse padrão de projeto aqui ele é muito versátil."
