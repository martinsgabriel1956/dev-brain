---
type: source
title: "Clean Architecture: Arquitetura Centrada no Domínio"
aliases: ["clean architecture domain-centric", "3-tier vs clean architecture"]
date_created: 2026-07-30
date_updated: 2026-07-30
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/clean-architecture-arquitetura-centrada-no-dominio.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-30
source_count: 0
tags: [clean-architecture, dependency-rule, 3-tier, arquitetura-em-camadas, dominio, arquitetura]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Transcrição de vídeo (em inglês, traduzida) que explica por que Clean Architecture é chamada de arquitetura **domain-centric**, contrastando-a diretamente com a arquitetura tradicional em 3 camadas (3-tier). Usa uma aplicação de lembretes como exemplo (plano básico: 3 lembretes/dia; plano pago: ilimitado) para mostrar como a lógica de negócio se divide em Application (use cases) e Domain (entidades + regras), e por que nenhuma delas depende de banco de dados — via Dependency Rule (camadas internas definem interfaces, camadas externas implementam).

## Key Claims

**Claim:** Na arquitetura em 3 camadas, a business layer depende diretamente da data access layer, e essa dependência tende a vazar transitivamente para a presentation layer.
**Evidence:** Nas palavras da fonte: "with time the business logic often becomes convoluted with the data access layer logic... sometimes data access logic will also end up in the presentation layer", já que a presentation layer depende da business layer, que depende da data access layer.
**Confidence:** média — é uma observação qualitativa sobre uma tendência comum, não uma prova formal, mas consistente com a literatura de acoplamento em camadas.

**Claim:** Clean Architecture divide a lógica de negócio que na 3-tier ficava numa única business layer em duas camadas distintas: Application (use cases) e Domain (entidades + regras).
**Evidence:** Exemplo do vídeo: `SetReminder`, `DismissReminder`, `DeleteReminder` são use cases na application layer; o objeto `Reminder` e `User`, junto com a regra que checa o tipo de plano, ficam na domain layer.
**Confidence:** alta — consistente com [[wiki/concepts/clean-architecture]], já documentado com outra fonte.

**Claim:** É chamada de arquitetura "domain-centric" porque, ao contrário da 3-tier (onde tudo aponta para o banco de dados embaixo), na Clean Architecture todas as dependências apontam para dentro, em direção ao domínio — e o banco de dados fica na infrastructure layer, uma camada externa.
**Evidence:** Comparação visual direta entre os dois diagramas na transcrição — 3-tier com data access layer "embaixo" recebendo dependências; Clean Architecture com domain no centro recebendo dependências de todas as camadas.
**Confidence:** alta.

**Claim:** A Dependency Rule se sustenta porque as camadas internas (application) definem interfaces que as camadas externas (infrastructure) implementam — permitindo trocar a tecnologia de uma camada externa sem afetar a lógica de negócio interna.
**Evidence:** "the inner layers define interfaces and the outer layers define the implementation to these interfaces" — mesmo mecanismo de inversão de dependência já documentado via Ports & Adapters em [[wiki/concepts/hexagonal-architecture]].
**Confidence:** alta — reforça claim já registrada em [[wiki/sources/clean-architecture]].

## Entities & Concepts Touched

- [[wiki/concepts/clean-architecture]]
- [[wiki/concepts/arquitetura-em-3-camadas]]
- [[wiki/concepts/hexagonal-architecture]]

## Open Questions

- A fonte é material promocional de um curso pago — as claims técnicas foram extraídas e a parte comercial foi descartada na transformação para `raw/`; não há prejuízo ao conteúdo técnico, mas vale registrar a natureza da fonte.
- O exemplo de app de lembretes (reminders) é pedagógico/simplificado — não há discussão de como a Dependency Rule se sustenta sob concorrência real ou múltiplos agregados, ponto já coberto com mais profundidade em [[wiki/sources/clean-architecture]] (fluxo Controller → Use Case → Presenter).
