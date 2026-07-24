---
type: concept
title: "RFC — Request for Comments"
aliases: ["RFC", "Request for Comments"]
date_created: 2026-05-17
date_updated: 2026-07-22
source_count: 3
tags: [rfc, documentação, processo, arquitetura, ia, source-of-truth]
skill: tech-mentor-system-design
status: draft
---

# RFC — Request for Comments

Documento de proposta aberta que busca feedback antes de uma decisão ser tomada. Diferente do [[trd-technical-requirements-document]] (especificação para implementar) e do [[adr-architecture-decision-record]] (registro de decisão já tomada).

Uso: quando a decisão ainda está em aberto e múltiplos stakeholders devem opinar.

## RFC como Source of Truth para Agentes de IA

[[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] argumenta que, na era do [[wiki/concepts/vibe-coding|vibe coding]], a RFC ganhou um papel adicional: é a fonte da verdade que um agente de IA segue para não alucinar arquitetura ou violar padrões da empresa. A tese central é uma **inversão de tempo** — historicamente gastava-se pouco tempo em planejamento e muito em codificação; com a IA acelerando a execução, devs que rodam agentes autônomos relatam gastar ~80% do tempo em RFC e apenas 20% em execução. Uma RFC sozinha não garante evals nem quality gate (ver [[wiki/concepts/quality-gate]]), mas garante um norte sobre o que deve ser feito e a oportunidade de o próprio dev conhecer o sistema que está sendo criado — algo que se perde quando o dev vai direto da ideia à execução sem essa etapa intermediária.

Uma variante discutida na mesma fonte é a **especificação agnóstica à linguagem de programação** (tese atribuída a [[wiki/entities/fabricio-arcanjo]]): documentar entradas/saídas rigorosamente em Markdown, focado em [[wiki/concepts/ddd|DDD]] e padrões, permite pedir a um agente para implementar a mesma arquitetura em linguagens diferentes (Rust, .NET, Java, Go, TypeScript) a partir de um único documento, reduzindo ambiguidade.

## Homônimo: RFC como Especificação Técnica (IETF)

Fora do contexto de processo organizacional documentado acima, "RFC" também é o nome dado aos documentos de especificação técnica publicados pela IETF — ex.: RFC 3629, que define o padrão [[utf-8]]. É o mesmo termo, sentido completamente diferente: aqui não há coleta de objeções nem decisão em aberto, é uma especificação normativa e estável que implementações devem seguir. [[wiki/sources/algoritmo-decode-utf8-com-tdd]] usa "RFC" exclusivamente nesse segundo sentido, ao implementar um decoder UTF-8 diretamente a partir da tabela de codificação definida na RFC 3629. Sinalizado aqui para não confundir os dois usos ao pesquisar "RFC" na wiki.

## Key Sources

- [[wiki/sources/trd-technical-requirements-document]]
- [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] — RFC como source of truth anti-alucinação para IA; inversão de tempo 80/20 planejamento/execução; especificações agnósticas à linguagem
- [[wiki/sources/algoritmo-decode-utf8-com-tdd]] — uso homônimo do termo: RFC como especificação técnica IETF (RFC 3629 / UTF-8), não processo de proposta
