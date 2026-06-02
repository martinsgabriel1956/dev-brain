---
type: source
title: "5 Princípios Que Vão Mudar Você Como Programador"
aliases: ["5 Principles Programmer", "5 princípios programador"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/5-principles-that-changed-me-as-a-programmer.md"
source_url: ""
author: ""
date_published: 2026
date_ingested: 2026-06-02
source_count: 0
tags: [logging, tech-debt, testes, naming, paridade-dev-prod, carreira, boas-praticas]
skill: tech-mentor-leadership
status: stable
---

# 5 Princípios Que Vão Mudar Você Como Programador

## TL;DR

Artigo sobre cinco lições práticas aprendidas na dor que a academia não ensina. A tese central: bons engenheiros operam pela realidade de produção, não pela teoria. Os cinco princípios são: logs estruturados, testar inputs impossíveis, tech debt deliberado, naming cuidadoso, e paridade dev-prod.

## Key Claims

- Logs com contexto (user_id, amount, error) são a diferença entre "vejo o problema" e "3 horas chutando" às 3h da manhã
- Todo código quebra em produção — o problema é não ter observabilidade quando isso acontece
- Usuários quebram tudo: strings vazias, emojis, null, SQL injection, 50 cliques seguidos, IE em 2026
- Tech debt deliberado e prudente (Quadrante de Fowler) é válido na fase de validação; refatore só se a feature sobreviver
- **A maioria das features falha** — não construa um palácio para algo que pode ser descartado no próximo mês
- Naming ruim aumenta o custo cognitivo de toda a equipe ao longo do tempo; é onde a maioria do tempo de leitura de código vai
- Ambiente local mente: variáveis de ambiente, permissões, dados e rede são diferentes em produção

## Conceitos Relacionados

- [[wiki/concepts/logging-estruturado]]
- [[wiki/concepts/observabilidade]]
- [[wiki/concepts/tech-debt-como-ferramenta]]
- [[wiki/concepts/quadrante-de-fowler]]
- [[wiki/concepts/naming]]
- [[wiki/concepts/paridade-local-producao]]
- [[wiki/concepts/usuarios-como-agentes-do-caos]]

## Quotes

> "Seu código vai quebrar em produção. Sempre. E quando acontecer — às 3h da manhã — você precisa saber o que de fato aconteceu. Não o que você acha que aconteceu."

> "Faça o deploy com debt. Pague depois. Se sobreviver. Palavra-chave: se."

## Open Questions

- Como equilibrar velocidade de validação com o risco de tech debt estrutural acumulado em times pequenos?
- Qual é o texto original do Quadrante de Fowler? (referência indireta no artigo)
