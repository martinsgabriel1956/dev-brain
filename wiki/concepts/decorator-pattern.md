---
type: concept
title: "Decorator Pattern"
aliases: ["padrão decorator", "design pattern decorator"]
date_created: 2026-05-01
date_updated: 2026-08-06
source_count: 3
tags: [design-patterns, structural, decorator, oop]
skill: tech-mentor-backend
status: stub
---

## Definição

Padrão estrutural que adiciona comportamento a objetos em cadeia (wrapping recursivo), sem alterar a classe original. Foco em extensão funcional.

## Diferença do Proxy

| | Decorator | Proxy |
|---|---|---|
| Motivação | Extensão de comportamento em cadeia | Controle de acesso / interceptação |
| Instanciação | Recebe o objeto decorado externamente | Geralmente cria/recebe o objeto real internamente |
| Quantidade de wrappers | Múltiplos encadeados | Normalmente um único interceptador |

Ambos encapsulam um objeto e implementam a mesma interface — a diferença está na **intenção**.

## Exemplo: encadeamento de canais de notificação

[[wiki/sources/seis-design-patterns-mais-usados-na-pratica]] ilustra o Decorator com um sistema de notificações que começa só com e-mail e depois precisa mandar por Slack e SMS também. Em vez de uma classe "Deus" que faz tudo, cada canal vira um decorator — `SlackDecorator` recebe um `notifier` no constructor, chama o `send` do objeto original e adiciona a lógica do Slack por cima. Encadeando os decorators, cada camada adiciona comportamento sem alterar as anteriores, e a combinação é escolhida montando a cadeia (quer só e-mail e SMS, sem Slack? não adiciona o `SlackDecorator`).

**Nota de precisão:** a fonte equipara os *decorators de linguagem* do TypeScript (`@Injectable` do Angular, `@Component` do NestJS) ao Decorator Pattern estrutural do GoF. A analogia funcional procede — ambos adicionam comportamento sem alterar a classe original —, mas a mecânica é diferente: decorators de linguagem operam via metadata/reflection em tempo de definição da classe, enquanto o Decorator GoF é wrapping de objeto em runtime, implementando a mesma interface do objeto decorado.

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
- [[sources/design-pattern-strategy]] — distinção Decorator (pele) vs Strategy (miolo/algoritmo)
- [[wiki/sources/seis-design-patterns-mais-usados-na-pratica]] — analogia dos filtros de foto do Instagram; exemplo de encadeamento de canais de notificação (e-mail → Slack → SMS); nota sobre decorators do TypeScript/Angular/NestJS
