---
type: concept
title: "Herança vs. Composição"
aliases: ["composição sobre herança", "acoplamento por herança"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [heranca, composicao, oop, acoplamento, testes]
skill: tech-mentor-testing
status: draft
---

# Herança vs. Composição

Segundo [[wiki/sources/tres-tipos-de-acoplamento-que-impedem-teste-unitario-andre-casciotti]], herdar de uma `BaseService` só para reaproveitar `ChamarApi` (HTTP) é um **acoplamento por herança**: todo filho depende do que o pai faz e o teste não consegue trocar o método herdado, então o `HttpClient` real é chamado. Parece elegante (sem duplicação), mas mistura contexto de negócio com tecnologia.

**Alternativa:** uma classe de infraestrutura (outra camada) com interface, **injetada** na service — composição + [[wiki/concepts/dependency-injection]]; no teste usa-se mock.

Não é proibir herança: usar **dentro do mesmo contexto** (negócio com negócio). O autor atribui o excesso ao legado cultural do .NET (herança "superestimada" após ASP/VB6) e diz que atinge também devs novos. O mesmo risco existe para qualquer herança que carregue I/O.

Ver [[wiki/concepts/acoplamento-que-impede-teste-unitario]], [[wiki/concepts/go-oop-composicao]] (composição em Go) e [[wiki/concepts/acoplamento]].

## Key sources

- [[wiki/sources/tres-tipos-de-acoplamento-que-impedem-teste-unitario-andre-casciotti]]
