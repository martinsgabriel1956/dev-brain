---
type: source
title: "Padrão de Projeto: Adapter"
aliases: ["adapter pattern video", "renato augusto adapter", "design pattern adapter dompdf tcpdf"]
date_created: 2026-07-15
date_updated: 2026-07-15
source_file: "raw/design-pattern-adapter.md"
source_url: ""
author: "Renato Augusto"
date_published: ""
date_ingested: 2026-07-15
source_count: 0
tags: [adapter-pattern, design-patterns, structural, solid, srp, acoplamento, abstracao, oop, testabilidade]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Uma classe de negócio (`SalesReportGenerator`) instancia diretamente uma lib externa de PDF (DomPDF) via `new`, chamando seus métodos específicos (`loadHtml`, `setPaper`, `render`). Isso acopla uma classe de alto nível a um detalhe de baixo nível, fere SRP (duas razões para mudar: regra de negócio e API da lib) e torna o código impossível de testar unitariamente sem gerar o PDF de verdade. A correção: extrair uma interface (`PdfAdapter`), criar um adaptador concreto que envelopa a lib (`DomPdfAdapter`), e injetar essa interface no construtor da classe de negócio. Trocar de biblioteca (demonstrado com TCPDF no lugar do DomPDF) passa a exigir só um novo adaptador — zero alteração na classe de regra de negócio.

## Key Claims

**Claim:** Toda vez que uma classe de alto nível dá `new` numa classe concreta de baixo nível dentro do próprio corpo, isso gera acoplamento e é sinal para aplicar o Adapter.
**Evidence:** `SalesReportGenerator::generate()` fazia `new DomPdf()` e chamava `loadHtml`/`setPaper`/`render` diretamente. Se a lib mudar a API (ex. `render` virar `generate`), a classe de negócio precisa mudar — mais de um motivo para mudar viola SRP.
**Confidence:** alta — demonstrado com exemplo de código completo, refatorado ao vivo.

**Claim:** Interface própria do domínio (`PdfAdapter`) é a "tomada" — quem se adapta a ela são as implementações concretas, nunca a classe de negócio.
**Evidence:** Ao trocar DomPDF por TCPDF (duas libs com APIs completamente diferentes: `loadHtml/setPaper/render` vs. `writeHTML/setFont`), só foi necessário criar um novo `TcpdfAdapter implements PdfAdapter` e trocar a instância injetada no `Command`. `SalesReportGenerator` não mudou uma linha.
**Confidence:** alta — troca de biblioteca demonstrada ao vivo com execução do script antes/depois.

**Claim:** Sem o Adapter, a classe de negócio é impossível de testar unitariamente de forma isolada.
**Evidence:** Com `new DomPdf()` cravado dentro do método, não há como mockar ou substituir por um dublê de teste. Com a interface `PdfAdapter` injetada via construtor, um fake que implementa a interface pode ser passado no lugar, sem gerar PDF real.
**Confidence:** alta, mas apenas argumentada — o vídeo não chega a escrever o teste unitário de fato.

## Fluxo de Execução (antes → depois)

```
Antes:
Command → new SalesReportGenerator()
             └── generate() → new DomPdf() → loadHtml/setPaper/render (acoplado, não testável)

Depois:
Command → new DomPdfAdapter() (ou TcpdfAdapter)
        → new SalesReportGenerator(pdfAdapter)   // injeção via interface PdfAdapter
             └── generate() → this.pdfAdapter.generate(fileName, content)
                                 └── DomPdfAdapter/TcpdfAdapter encapsula a API específica da lib
```

## Entities & Concepts Touched

- [[wiki/concepts/adapter-pattern]]
- [[wiki/concepts/acoplamento]]
- [[wiki/concepts/abstracao]]
- [[wiki/concepts/single-responsibility]]
- [[wiki/concepts/design-patterns]]
- [[wiki/entities/renato-augusto]]

## Open Questions

- O vídeo argumenta a testabilidade do resultado mas não escreve o teste unitário de fato — como ficaria o fake/mock de `PdfAdapter` na prática?
- Em que ponto múltiplos adapters para a mesma interface (DomPDF, TCPDF, mPDF) viram um caso de uso para injeção de dependência configurável (factory/container) em vez de troca manual no `Command`?
- Como esse mesmo problema se resolveria numa linguagem sem interfaces explícitas (Go via duck typing, Python via protocolos)?
