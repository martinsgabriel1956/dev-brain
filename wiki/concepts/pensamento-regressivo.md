---
type: concept
title: "Pensamento Regressivo"
aliases: ["backward thinking", "pensar de trás pra frente", "raciocínio reverso"]
date_created: 2026-05-01
date_updated: 2026-05-01
source_count: 1
tags: [resolucao-de-problemas, pensamento-estruturado, debugging]
skill: tech-mentor-leadership
status: stable
---

## Definição

Técnica de resolução de problemas que começa pelo **estado final desejado** e trabalha de forma regressiva até o ponto inicial, em vez de avançar por suposições.

## Por que funciona melhor que pensar "para frente"

Pensar para frente → "se eu fizer X, será que melhora?" → suposição → gasto de tempo sem garantia.

Pensar para trás → define o destino primeiro → mapeia cada passo necessário → revela pontos de falha e dados necessários automaticamente.

## Exemplo — Fluxo de Login

```
Estado final: usuário autenticado no sistema
← Senha validada
← Credenciais inseridas
← Página de login aberta
← Usuário acessou a URL
```

Esse mapeamento revela de forma natural:
- todos os pontos onde o sistema pode quebrar
- todas as validações necessárias
- todos os dados que precisam ser armazenados

## Relação com outros conceitos

- É o passo 3 do [[pensamento-estruturado]]
- Complementa a [[arvore-de-decomposicao]] (que trabalha por dimensões)
- Aplicado em [[causa-raiz]] para rastrear a origem de um bug
- Similar ao princípio da inversão de [[principio-da-inversao]]

## Key Sources

- [[wiki/sources/pensamento-estruturado-resolucao-de-problemas]]
