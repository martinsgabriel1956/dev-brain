---
type: source
title: "AI and Software Architecture: A Dangerous Convenience"
aliases: ["abstraction illusion", "super productivity ai architecture", "constraints first"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [ia, arquitetura, abstraction-illusion, constraints, decisao, yagni, reversibilidade]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartinis/Documentos/new/dev-study/raw/super-productivity-ai-architecture-guide.md
source_url: https://super-productivity.com/blog/ai-software-architecture-guide/
author: "Super Productivity Blog"
date_published: 2026
date_ingested: 2026-04-23
---

# AI and Software Architecture: A Dangerous Convenience

## TL;DR

A IA torna padrões sofisticados *acessíveis* sem torná-los *apropriados*. Arquitetura é escolha de constraints, não de padrões. A IA conhece os padrões mas não conhece suas constraints. A solução é constraints-first: escreva suas limitações reais antes de perguntar qualquer coisa à IA.

## Key Claims

**Claim:** A Abstraction Illusion: a IA remove a barreira de implementação de padrões complexos sem remover a questão de adequação.
**Evidence:** Antes: implementar Event Sourcing exigia livros, exemplos, construção incremental — filtro natural. Hoje: CQRS completo em uma tarde. O time paga o overhead por anos.
**Source:** super-productivity.com/blog/ai-software-architecture-guide
**Confidence:** Alta

**Claim:** Arquitetura é escolha de constraints, não de padrões.
**Evidence:** Microsserviços trocam independência de deploy por complexidade operacional. Event Sourcing troca simplicidade de query por completude de auditoria. Monolito troca flexibilidade de escala por velocidade de desenvolvimento.
**Source:** super-productivity.com/blog/ai-software-architecture-guide
**Confidence:** Alta

**Claim:** A IA responde a pergunta que *pode* responder (quais padrões existem), não a que você *precisa* (quais constraints devem guiar sua escolha).
**Evidence:** "AI knows the patterns but not your constraints."
**Source:** super-productivity.com/blog/ai-software-architecture-guide
**Confidence:** Alta

**Claim:** Prefira sempre a opção mais reversível quando empatado — reserve decisões irreversíveis para alta confiança.
**Evidence:** Código simples é mais fácil de refatorar. Com IA, refatorar código simples é rápido.
**Source:** super-productivity.com/blog/ai-software-architecture-guide
**Confidence:** Alta

## Workflow Prático (7 Passos)

1. Colete constraints antes de qualquer prompt (team size, tráfego, consistência, capacidade operacional, timeline)
2. Explore opções com a IA — survey, não recomendação
3. Forme sua própria opinião baseada em constraints + opções
4. Teste com a IA como devil's advocate
5. Aplique o teste das 10 perguntas de adequação
6. Escolha a opção mais reversível quando empatado
7. Documente constraints, opções e rationale — isso a IA não consegue gerar

## Entities

- [[entities/super-productivity]] — ferramenta e blog de produtividade para devs

## Concepts

- [[concepts/abstraction-illusion]] — IA torna padrões acessíveis sem torná-los apropriados
- [[concepts/yagni]] — princípio subjacente à abordagem constraints-first
- [[concepts/abstraction-bloat]] — efeito prático da abstraction illusion
- [[concepts/adr]] — Architecture Decision Record, onde documentar o rationale

## Open Questions

- As 10 perguntas de adequação são suficientes ou existe um conjunto melhor calibrado para domínios específicos (fintech, healthcare)?
- Como integrar constraints-first em fluxos onde a pressão de prazo é alta?

## Raw Quotes

> "This is the abstraction illusion: AI makes sophisticated patterns accessible without making them appropriate."

> "AI knows the patterns but not your constraints. When you ask 'how should I architect this?', AI answers the question it can answer rather than the question you need answered."

> "Choose the more reversible option when tied. Reserve irreversible decisions for situations where you have high confidence."
