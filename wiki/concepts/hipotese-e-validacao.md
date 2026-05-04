---
type: concept
title: "Hipótese e Validação"
aliases: ["hypothesis testing", "validar hipóteses", "testar suposições"]
date_created: 2026-05-01
date_updated: 2026-05-01
source_count: 1
tags: [debugging, resolucao-de-problemas, pensamento-estruturado, dados]
skill: tech-mentor-leadership
status: stable
---

## Definição

Antes de atuar num problema, formule uma hipótese específica e valide-a com dados. "Pode ser" não é suficiente — você precisa confirmar ou descartar antes de gastar tempo na solução.

## Por que é crítico

Sem validação, você pode passar dias resolvendo o ponto errado. Exemplo: achou que era banco de dados, mudou o banco, o problema continuou — porque era rede.

## Como validar (pergunte aos dados)

| Hipótese | Como validar |
|---|---|
| "É o banco de dados" | Rode a query isolada e meça o tempo |
| "É a rede" | Meça tempo de requisição vs tempo de processamento |
| "É escala" | Teste com 10 usuários e depois com 1000 |
| "É um usuário específico" | Reproduza com a conta desse usuário |

## Relação com outros conceitos

- É o passo 4 do [[pensamento-estruturado]]
- As hipóteses vêm da [[arvore-de-decomposicao]]
- Confirmar a hipótese isola a [[causa-raiz]]
- [[dados-vs-intuicao]] — dados superam intuição; hipótese sem validação é intuição

## Key Sources

- [[wiki/sources/pensamento-estruturado-resolucao-de-problemas]]
