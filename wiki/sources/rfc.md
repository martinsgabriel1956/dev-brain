---
type: source
title: "RFC — Request for Comments"
aliases: ["rfc", "request for comments", "rfc template", "technical decision", "rfc process"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/rfc.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [rfc, technical-decision, documentation, architecture, process, team-communication]
skill: tech-mentor-backend
status: stable
---

## TL;DR

RFC (Request for Comments): documento para propor e debater decisões técnicas significativas antes de implementar. Diferente do ADR (que registra a decisão tomada), o RFC é o processo de chegar nessa decisão. Formato: contexto, problema, alternativas consideradas, proposta, trade-offs, critérios de sucesso. Armazenado como PR em `docs/rfcs/`. RFC vs ADR: RFC é processo de decisão; ADR é registro histórico do resultado.

## Key Claims

**Claim:** RFC resolve o problema de decisões técnicas tomadas de forma não-consensual ou não-documentada.
**Evidence:** Sem RFC: arquiteto decide unilateralmente, engenheiros descobrem no PR. Com RFC: proposta publicada como PR, todos comentam assincronamente, time alinha antes de implementar. Evita: reescrita após implementação, resistência de engenheiros excluídos do processo, decisões sem registro de alternativas consideradas.
**Confidence:** alta

**Claim:** RFC é adequado para decisões significativas e irreversíveis — não para implementações cotidianas.
**Evidence:** Merece RFC: mudança de banco de dados, adoção de nova tecnologia, mudança de paradigma de autenticação, mudança de protocolo de comunicação entre serviços. Não merece RFC: refactoring de função, adição de endpoint, escolha de biblioteca para feature específica. Heurística: se desfazer custaria > 1 sprint, escreve um RFC.
**Confidence:** alta

**Claim:** RFC como PR em `docs/rfcs/` integra com git flow existente — review, comentários e aprovação pelo mesmo mecanismo.
**Evidence:** PR: revisores fazem comentários linha a linha no documento. Thread de discussão fica vinculada ao arquivo. Aprovação via CODEOWNERS ou review mínimo configurável. Merge = decisão tomada. Git history: quem aprovou, quando, quais alternativas foram discutidas. Sem ferramenta adicional.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/rfc]]
- [[concepts/adr]]
- [[concepts/architecture-documentation]]
- [[concepts/technical-decision]]

## Open Questions

- Como escalar RFC em times grandes (50+ engenheiros) sem cada RFC virar um processo lento de semanas?
- RFC vs Spike: quando o time não tem informação suficiente para propor — como estruturar investigação prévia?
