---
type: concept
title: "Causa Raiz (Root Cause)"
aliases: ["root cause", "root cause analysis", "RCA", "causa raiz"]
date_created: 2026-05-01
date_updated: 2026-07-30
source_count: 2
tags: [debugging, resolucao-de-problemas, sre, pensamento-estruturado]
skill: tech-mentor-leadership
status: stable
---

## Definição

A causa raiz é o ponto de origem real de um problema — não o sintoma visível. Atuar no sintoma sem encontrar a causa raiz resolve temporariamente, mas o problema retorna.

## Por que a maioria erra

As pessoas atacam o problema visível ("relatório lento") em vez de decompor até encontrar onde está o gargalo real ("busca ao banco demora 8s por ausência de índice").

## Técnica dos 5 Porquês

Perguntar "por quê?" repetidamente até chegar à causa raiz:

```
Por que o relatório está lento?
→ Porque a query demora muito.
Por que a query demora?
→ Porque faz full table scan.
Por que faz full table scan?
→ Porque não existe índice na coluna filtrada.
Por que não existe o índice?
→ Porque nunca foi criado.
→ Causa raiz: índice ausente.
```

## Regra de Ouro

> Atue **somente** onde está a causa raiz. Não tente corrigir tudo. Uma causa raiz bem identificada resolve o problema com o mínimo de mudança.

## Relação com outros conceitos

- [[arvore-de-decomposicao]] é a ferramenta para chegar à causa raiz
- [[hipotese-e-validacao]] confirma que a causa raiz identificada é a real
- [[blameless-post-mortem]] usa RCA formalmente em incidentes de produção
- [[pensamento-estruturado]] — passo 2 (decompor) aponta para a causa raiz
- [[wiki/concepts/over-engineering]] — a versão arquitetural de "atacar o sintoma": escolher a solução mais complexa em vez de identificar e resolver a causa raiz com o menor atrito

## Aplicação em Nível Arquitetural

[[wiki/sources/arquitetura-frontend-dash-fornecedores-vs-microfrontends-super-roupas]] aplica a mesma regra de ouro num caso de arquitetura frontend: o sintoma visível era "a experiência está fragmentada entre 4 sistemas de fornecedor", mas a causa raiz do problema reportado pela operação era falta de visibilidade de status/atraso entre esses sistemas. Atacar o sintoma (unificar tudo via [[wiki/concepts/microfrontends-parciais|microfrontends]]) custaria 3+ meses sem resolver o problema real; atacar a causa raiz (dashboard read-only + [[wiki/concepts/bff-pattern|BFF]] agregador) resolveu em menos de 2 meses.

## Key Sources

- [[wiki/sources/pensamento-estruturado-resolucao-de-problemas]]
- [[wiki/sources/arquitetura-frontend-dash-fornecedores-vs-microfrontends-super-roupas]] — aplicação em nível de decisão arquitetural (frontend/BFF vs. microfrontends)
