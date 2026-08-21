---
type: source
title: "CQRS (Martin Fowler bliki)"
aliases: ["CQRS Martin Fowler", "Martin Fowler bliki CQRS"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/cqrs-martin-fowler.md
source_url: "https://martinfowler.com/bliki/CQRS.html"
author: "Martin Fowler"
date_published: 2011-07-14
date_ingested: 2026-08-18
source_count: 0
tags: [cqrs, arquitetura, ddd, bounded-context, event-sourcing]
skill: tech-mentor-backend
status: stable
---

# CQRS (Martin Fowler bliki)

## TL;DR

Post original do bliki de [[wiki/entities/martin-fowler|Martin Fowler]] (14/07/2011) que cunhou/popularizou a definição mais citada de CQRS: separar o modelo conceitual de comando (escrita) do de consulta (leitura), em vez de usar um único modelo CRUD para ambos. É a fonte primária mais antiga já ingerida na wiki sobre o tema — as demais fontes de [[wiki/concepts/cqrs]] são cursos, vídeos e transcrições que derivam ou reformulam esta ideia original. O tom do post é de **cautela**: Fowler defende CQRS apenas para bounded contexts específicos, nunca para o sistema inteiro, e afirma que a maioria das implementações que observou foi problemática.

## Claims Principais

| Claim | Evidência | Confiança |
|---|---|---|
| A justificativa central do CQRS é que usar o mesmo modelo conceitual para comandos e consultas, em domínios complexos, produz um modelo mais complexo que não atende bem nenhuma das duas responsabilidades | Citação direta de Fowler no post original | Alta — fonte primária |
| Os modelos de comando e consulta podem rodar em processos/hardware lógicos diferentes, comunicando-se via banco compartilhado ou stores separados (o segundo caso cria, na prática, um banco de relatórios em tempo real) | Descrição direta do post | Alta |
| CQRS combina naturalmente com task-based UI, Event Sourcing, consistência eventual e DDD | Descrição direta do post | Alta — consistente com [[wiki/concepts/task-based-ui]] e [[wiki/concepts/event-sourcing]] já documentados na wiki |
| CQRS só compensa em dois cenários: (1) domínios complexos onde a separação realmente simplifica a modelagem — caso minoritário — e (2) aplicações de alto desempenho com cargas de leitura/escrita muito diferentes que exigem escalabilidade independente | Citação direta de Fowler | Alta |
| CQRS deve se aplicar apenas a bounded contexts específicos, nunca ao sistema inteiro; aplicações incorretas aumentam complexidade e risco sem benefício correspondente | Citação direta de Fowler | Alta |
| Fowler afirma que a maioria das implementações de CQRS que ele encontrou foi problemática, e sugere que reporting databases podem obter benefícios similares sem a sobrecarga de complexidade do CQRS | Citação direta de Fowler | Alta — é a opinião pessoal do autor, não um dado estatístico |

## Conceitos Abordados

- [[wiki/concepts/cqrs]]
- [[wiki/concepts/ddd]]
- [[wiki/concepts/event-sourcing]]
- [[wiki/concepts/task-based-ui]]
- [[wiki/concepts/bounded-context]] (novo — stub)

## Entidades Abordadas

- [[wiki/entities/martin-fowler]] (novo — stub)

## Observações / Contradições

Sem contradições factuais com [[wiki/concepts/cqrs]] — esta fonte é consistente com o que já estava documentado (via [[wiki/sources/cqrs-event-sourcing-full-cycle-wesley-williams]]) sobre a origem em [[wiki/entities/greg-young|Greg Young]] e CQS. O valor desta fonte é ser a **origem textual mais citada** do termo, permitindo checar se as fontes derivadas (cursos, vídeos) mantiveram fidelidade à ideia original de Fowler.

Um ponto que nenhuma fonte anterior enfatizava com este peso: o **tom de cautela explícito** de Fowler — "a maioria das implementações que encontrei se provou problemática" — é mais forte que o tom das fontes técnicas já na wiki (que listam trade-offs mas não citam uma taxa de insucesso observada pelo autor). Vale adicionar essa nuance ao corpo de [[wiki/concepts/cqrs]].

## Perguntas Abertas

Nenhuma pergunta aberta relevante — post curto e direto, sem ambiguidades no conteúdo capturado.

## Raw Quotes

> "The rationale is that for many problems, particularly in more complicated domains, having the same conceptual model for commands and queries leads to a more complex model that does neither well."

> "CQRS should be used only on specific portions of a system and not the whole thing — most systems where I've seen it applied badly is where people have used it as a blanket architectural style for a whole system, which usually leads to too much complexity and too much risk for most enterprise systems."

> "My primary worry is that people will use CQRS because it's the cool thing to do, [...] most of the systems I've seen using it have been legitimately more complex, and quite often that complexity wasn't worth it."
