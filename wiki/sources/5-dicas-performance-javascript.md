---
type: source
title: "5 Dicas para Elevar a Performance de Aplicações JavaScript"
aliases: ["5 dicas js performance", "erick wendel performance javascript"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 0
tags: [javascript, nodejs, performance, event-loop, web-streams, opentelemetry, testes-de-carga]
skill: lang-dynamic
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/5-dicas-performance-javascript.md
source_url: ""
author: "Erick Wendel"
date_published: 2026-05-01
date_ingested: 2026-06-02
---

# 5 Dicas para Elevar a Performance de Aplicações JavaScript

## TL;DR

Cinco dicas práticas de Erick Wendel para performance JS no mundo real: processar listas sob demanda com Web Streams (não carregar tudo em memória), evitar código síncrono que trava o event loop, adotar arquitetura assíncrona por design (separar recebimento de processamento), monitorar com OpenTelemetry antes do problema aparecer, e combinar testes automatizados com testes de carga para descobrir gargalos antes do incidente.

## Afirmações-chave

| Afirmação | Evidência | Confiança |
|---|---|---|
| Manipular listas grandes em memória bloqueia o event loop — processar sob demanda com Web Streams | Erick Wendel, exemplos práticos | Alta |
| Funções com sufixo `Sync` bloqueiam o event loop; em 10 clientes, 1 `readFileSync` para todos os outros | Erick Wendel | Alta |
| `console.log` é síncrono — usar Pino para logs assíncronos em produção | Erick Wendel | Alta |
| Arquitetura assíncrona (recebe → salva → notifica depois) pode reduzir custo de VMs significativamente | Erick Wendel, caso real de CSV | Alta |
| OpenTelemetry open source roda em container Docker e monitora qualquer stack JS | Erick Wendel | Alta |
| Playwright + Artillery + OpenTelemetry permite simular Black Friday antes de acontecer | Erick Wendel | Alta |

## As 5 Dicas

### Dica 1 — Processar sob Demanda (Web Streams)

**Anti-padrão:** carregar lista inteira em memória → rodar `for/map/filter` → retornar

**Padrão correto:** receber item → transformar → retornar → próximo item (sem acumular)

Ferramentas: **Web Streams** (nativo JavaScript, any environment) ou **RxJS/Observables** (curva maior).

Exemplo: processar 10 GB de dados no browser sem backend e sem travar a tela.

Ver [[wiki/concepts/event-loop-performance-js]] — bloqueio de event loop e alternativas.

### Dica 2 — Evitar Código Síncrono

Identificar `*Sync` no codebase. Cada chamada síncrona bloqueia o event loop inteiro.

**Impacto:** 10 clientes → 1 `readFileSync` → 9 aguardam.

**Fix:** delegar para tarefa assíncrona → continuar atendendo → entregar quando pronto.

**Logs:** `console.log` síncrono → usar **Pino** (assíncrono, multithreads para logs).

### Dica 3 — Arquitetura Assíncrona

**Caso real:** cliente gastava muito com VMs de alto CPU/memória para processar CSVs.

**Antes:** cliente envia CSV → backend processa → responde "processado"

**Depois:** cliente envia CSV → backend salva → responde "em andamento" → outro processo processa → notifica por e-mail

Benefícios: custo menor, responsabilidades isoladas, falhas contidas.

### Dica 4 — Monitorar e Melhorar

Mínimo necessário: métricas (requests lentos, endpoints, erros/sucesso), tracing (gargalos em código e queries), alertas (antes do usuário perceber).

Ferramenta: **OpenTelemetry** open source — sobe em Docker, agnóstico de vendor.

### Dica 5 — Testes Automatizados + Carga

```
testes automatizados
→ validam comportamento esperado
→ permitem plugar ferramenta de carga (Artillery)
→ simulam N usuários simultâneos
→ monitoramento (OpenTelemetry) aponta gargalos
→ você sabe antes do incidente
```

Stack recomendada:
- **Playwright** — testes E2E (automatiza ações do usuário)
- **Artillery** — testes de carga (simula N usuários virtuais)
- **OpenTelemetry** — observabilidade durante os testes

## Resumo

| # | Dica | Ferramenta-chave |
|---|---|---|
| 1 | Processar sob demanda | Web Streams, RxJS |
| 2 | Evitar bloqueio síncrono | async/await, Pino |
| 3 | Arquitetura assíncrona | background jobs, notificação |
| 4 | Monitorar | OpenTelemetry |
| 5 | Testes de carga | Playwright + Artillery |

## Conceitos Introduzidos/Reforçados

- [[wiki/concepts/event-loop-performance-js]] — o event loop como gargalo central do JS
- [[wiki/concepts/observabilidade]] — OpenTelemetry como camada agnóstica
- [[wiki/concepts/background-jobs]] — separar recebimento de processamento

## Entidades Mencionadas

- Erick Wendel — JavaScript Expert, autor da série YouTube Performance JavaScript
