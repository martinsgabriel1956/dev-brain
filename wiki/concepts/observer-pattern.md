---
type: concept
title: "Observer Pattern"
aliases: ["observer", "pub/sub pattern", "event listener pattern"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
tags: [design-patterns, behavioral, observer, gof, event-driven, pub-sub]
skill: tech-mentor-backend
status: stable
---

# Observer Pattern

Padrão [[behavioral-patterns|comportamental]] que define uma dependência **um-para-muitos** entre objetos: quando um objeto muda de estado, todos os seus dependentes são notificados automaticamente.

## Como funciona

```typescript
interface Subscriber {
  notify(videoTitle: string): void;
}

class VideoChannel {
  private subscribers: Subscriber[] = [];

  subscribe(subscriber: Subscriber) {
    this.subscribers.push(subscriber);
  }

  unsubscribe(subscriber: Subscriber) {
    this.subscribers = this.subscribers.filter(s => s !== subscriber);
  }

  uploadVideo(title: string) {
    this.notify(title);
  }

  private notify(title: string) {
    for (const subscriber of this.subscribers) {
      subscriber.notify(title);
    }
  }
}
```

## Terminologia

- **Subject/Observable**: objeto que emite eventos (`VideoChannel`)
- **Observer/Subscriber**: objeto que reage a eventos (`Subscriber`)
- **Event**: a mudança de estado que dispara notificações

## Quando usar

- Sistemas onde um evento deve disparar ações em múltiplos lugares
- Monitoramento de erros de servidor
- Mudanças de estado em componentes (React state, Redux)
- Domain Events em DDD

## Trade-offs

| ✅ | ❌ |
|---|---|
| Desacoplamento entre emissor e receptores | Event callback hell se abusado |
| Notificação automática sem polling | Ordem de notificação não garantida |
| Extensível — adicionar observers sem mudar o Subject | Debug difícil em cadeias longas de eventos |

## Relação com outros conceitos

- Base conceptual do [[mensageria]] e sistemas event-driven
- Domain Events em DDD usam o mesmo princípio
- Diferença de Pub/Sub: Observer tem referência direta ao Subject; Pub/Sub usa broker intermediário

## Key Sources

- [[sources/sete-padroes-de-design-de-software]]
- [[sources/design-pattern-observer]]
