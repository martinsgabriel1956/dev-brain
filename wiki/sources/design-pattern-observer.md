---
type: source
title: "Observer — Padrão de Projeto Comportamental (Refactoring Guru)"
aliases: ["refactoring guru observer", "observer pattern guru"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 0
tags: [design-patterns, behavioral, observer, gof, pub-sub, event-driven, assinatura]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/design-pattern-observer.md
source_url: https://refactoring.guru/pt-br/design-patterns/observer
author: "Refactoring Guru"
date_published: ""
date_ingested: 2026-05-05
---

# Observer — Padrão de Projeto Comportamental (Refactoring Guru)

Artigo canônico do Refactoring Guru sobre o padrão Observer. Fonte primária com estrutura, pseudocódigo completo, aplicabilidade e relações com Chain of Responsibility, Command e Mediator.

## TL;DR

[[observer-pattern]] define um mecanismo de assinatura: a publicadora mantém uma lista de assinantes e os notifica automaticamente quando algo acontece. Publicadora e assinantes comunicam através de interface comum — desacoplados. Lista dinâmica: assinantes entram e saem em runtime. Diferença importante com [[pub-sub]]: Observer tem comunicação direta publicadora→assinante; Pub/Sub usa broker intermediário.

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| Publicadora não conhece classes concretas dos assinantes | "todas essas classes devem implementar a mesma interface para que a publicadora não fique acoplada à classes concretas" | Alto |
| Lista de assinantes é dinâmica | "assinantes podem entrar e sair da lista sempre que quiserem" | Alto |
| OCP aplicado ao Observer | "Você pode introduzir novas classes assinantes sem ter que mudar o código da publicadora" | Alto |
| Assinantes notificados em ordem aleatória | Listado como desvantagem explícita | Alto |
| Observer ≠ Pub/Sub | Observer: comunicação direta; Pub/Sub: via broker intermediário | Alto |
| Mediator pode ser implementado com Observer | "às vezes você pode aplicar ambos simultaneamente" | Médio |

## Estrutura

```
Cliente → cria e registra → Publicadora (EventManager)
                                  │ notify(eventType, data)
                                  ▼
                          <<interface>> Assinante
                              + atualizar(dados)
                                  ▲
                    LoggingListener  EmailAlertsListener  (...)
```

## Pseudocódigo Central

```
class EventManager is
    private listeners: hash map of event types and listeners
    method subscribe(eventType, listener) is listeners.add(eventType, listener)
    method unsubscribe(eventType, listener) is listeners.remove(eventType, listener)
    method notify(eventType, data) is
        foreach listener in listeners.of(eventType) do listener.update(data)

class Editor is
    public events: EventManager
    constructor() is this.events = new EventManager()
    method openFile(path) is
        this.file = new File(path)
        events.notify("open", file.name)
    method saveFile() is
        file.write()
        events.notify("save", file.name)

// Assinantes concretos — desacoplados entre si e do Editor
class LoggingListener implements EventListener is
    method update(filename) is log.write(message.replace('%s', filename))

class EmailAlertsListener implements EventListener is
    method update(filename) is system.email(email, message.replace('%s', filename))
```

## Aplicabilidade

1. Conjunto de objetos a notificar é desconhecido de antemão ou muda dinamicamente
2. Objetos devem observar outros apenas por tempo limitado ou em casos específicos

## Relações com Outros Padrões

- [[chain-of-responsibility-pattern]] — passa pedido sequencialmente pela corrente
- [[command-pattern]] — conexão unidirecional remetente→destinatário
- [[mediator-pattern]] — elimina conexões diretas; todos comunicam via mediador. Observer pode ser usado para implementar Mediator dinamicamente
- [[pub-sub]] — Observer direto vs Pub/Sub via broker intermediário

## Questões em Aberto

- Como garantir ordem de notificação quando ela importa (ex: logging antes de email)?
- Memory leaks por assinantes não removidos — como gerenciar ciclo de vida em linguagens sem GC?
- Quando usar Observer in-process vs mensageria externa (Kafka, SNS)?
