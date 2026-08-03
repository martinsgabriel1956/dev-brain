---
type: concept
title: "Template Method Pattern"
aliases: ["template method", "método template"]
date_created: 2026-05-05
date_updated: 2026-08-03
source_count: 2
tags: [design-patterns, behavioral, template-method, gof, heranca]
skill: tech-mentor-backend
status: stub
---

# Template Method Pattern

Padrão [[behavioral-patterns|comportamental]] que define o **esqueleto de um algoritmo** na classe base e deixa as subclasses sobrescreverem etapas específicas sem mudar a estrutura geral.

## Mecanismo

Usa **herança** — a estrutura do algoritmo fica na classe pai (método template), as etapas variantes são métodos abstratos implementados pelas subclasses.

## Distinção do Strategy

| | Template Method | [[strategy-pattern]] |
|---|---|---|
| Mecanismo | Herança (estático) | Composição (dinâmico) |
| Troca em runtime? | Não | Sim |
| Granularidade | Etapas do algoritmo | Algoritmo inteiro |
| Acoplamento | Subclasse acoplada à base | Contexto desacoplado da estratégia |

## Quando usar

- Quando várias classes compartilham a mesma estrutura de algoritmo, mas diferem em etapas específicas
- Quando quer evitar duplicação do esqueleto do algoritmo em subclasses

## Exemplos reais

- Parsers que compartilham lógica de leitura mas diferem no processamento
- Frameworks de teste (`setUp`, `test`, `tearDown`)
- Geradores de relatório com formato fixo mas dados variáveis

## Variação via composição em vez de herança

[[wiki/sources/arquitetura-limpa-na-pratica]] implementa uma variação deliberada do padrão para os controladores web de uma API REST: em vez de subclasses sobrescrevendo métodos abstratos, uma classe `WebController` recebe por **injeção de dependência** um objeto `ControllerOperation` (interface com uma operação específica e a lista de parâmetros requeridos). O `WebController.handle` implementa a lógica genérica (checar parâmetros faltando → 400, executar operação específica envolta em `try-catch` → 500 em caso de exceção), delegando a variação para composição. Justificativa citada pelo autor: o próprio livro do GoF recomenda favorecer composição sobre herança.

## Key Sources

- [[sources/design-pattern-strategy]] — mencionado nas relações como contraponto ao Strategy
- [[wiki/sources/arquitetura-limpa-na-pratica]] — variação via composição (não herança) na classe `WebController` de uma API REST em Clean Architecture
