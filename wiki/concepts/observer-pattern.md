---
type: concept
title: "Observer Pattern"
aliases: ["observer", "pub/sub pattern", "event listener pattern"]
date_created: 2026-05-05
date_updated: 2026-08-06
source_count: 5
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

## Implementação minimalista com `Set` (JavaScript)

```javascript
function createSubscriber() {
  const listeners = new Set(); // Set em vez de Array: add/delete diretos, sem indexOf/filter

  function subscribe(listener) {
    listeners.add(listener);
    return () => listeners.delete(listener); // padrão de unsubscribe via cleanup
  }

  function emit(event) {
    listeners.forEach((listener) => listener(event));
  }

  return { subscribe, emit };
}
```

Essa é exatamente a peça central por trás de bibliotecas de estado global como [[wiki/concepts/zustand]]: uma store observável que componentes React se inscrevem via [[wiki/concepts/useEffect]], sincronizando o valor externo com [[wiki/concepts/useState]] local. Ver [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]] para a implementação completa (Observer + `Map` para o valor + Hook de sincronização).

## Como terceiro estágio de desacoplamento (não a única opção correta)

[[wiki/sources/tres-estagios-de-acoplamento-observer-pattern-na-pratica]] enquadra o Observer como o terceiro de três estágios de acoplamento — não superior por natureza, mas o único que elimina até a dependência estática/explícita entre componentes:

1. **Estágio 1** — tudo misturado num mesmo lugar (ótimo só para prototipagem rápida).
2. **Estágio 2** — componentes isolados, mas um chama o outro de forma estática/explícita (ex.: via [[wiki/concepts/factory-pattern]]). É como a maioria do software profissional é construído, inclusive com [[wiki/concepts/dependency-injection]] — a DI torna a dependência flexível, mas não a remove.
3. **Estágio 3** — nenhum componente conhece o outro nem estaticamente. É aqui que entra o Observer: o subject (`createGame`) expõe `subscribe(observerFunction)` e `notifySubscribers(command)`; observers entram e saem em runtime sem que o subject precise saber quem são.

Implementação minimalista feita do zero (sem função `update()` padronizada — o autor passa a função observadora diretamente, argumentando que isso é mais flexível que exigir uma interface comum):

```javascript
function createGame() {
  const state = { observers: [] };
  function subscribe(observerFunction) { state.observers.push(observerFunction); }
  function notifySubscribers(command) {
    state.observers.forEach((observerFunction) => observerFunction(command));
  }
  return { subscribe, notifySubscribers };
}
```

**Trade-off explícito da fonte**: o custo de complexidade do Observer só se paga quando há múltiplos observers anexados ao mesmo subject — com um único observer, "talvez não valha a pena". O ganho concreto: anexar um novo observer (ex.: uma camada de rede escutando os mesmos comandos de teclado para sincronizar cliente e servidor) tem impacto quase zero no código já existente, porque nem o subject nem os observers anteriores precisam mudar.

## Mais de um tipo de observer para o mesmo evento

[[wiki/sources/design-pattern-observer-codigo-fonte-tv]] implementa o padrão duas vezes: um exemplo genérico de aquecimento e um exemplo de notificação de vídeo novo do YouTube, onde **dois tipos diferentes de observer** implementam a mesma interface `IObserver` mas reagem de formas estruturalmente distintas ao mesmo evento — `Subscriber` (notificação pessoal ao inscrito) e `Feed` (atualização da URL do feed do canal). Reforça que "não existe só um tipo de observer" ao lidar com esse padrão: o mesmo `notifyAll` pode disparar reações completamente diferentes dependendo do tipo concreto do assinante.

## Relação com outros conceitos

- Base conceptual do [[mensageria]] e sistemas event-driven
- Domain Events em DDD usam o mesmo princípio
- Diferença de Pub/Sub: Observer tem referência direta ao Subject; Pub/Sub usa broker intermediário

## Key Sources

- [[sources/sete-padroes-de-design-de-software]]
- [[sources/design-pattern-observer]]
- [[wiki/sources/seis-design-patterns-mais-usados-na-pratica]] — analogia do sino de inscrição do YouTube; nota o `useEffect` do React e o `EventEmitter` do Node.js como Observer do dia a dia
- [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]] — implementação minimalista com `Set`, usada como base de uma store estilo Zustand
- [[wiki/sources/tres-estagios-de-acoplamento-observer-pattern-na-pratica]] — Observer como terceiro estágio de desacoplamento (vs. acoplamento estático via Factory); implementação `subscribe`/`notifySubscribers` sem `update()` padronizado; trade-off complexidade vs. número de observers
- [[wiki/sources/design-pattern-observer-codigo-fonte-tv]] — implementação em TypeScript/Deno com `Subject`/`Observer` genéricos e exemplo de notificação de vídeo do YouTube com dois tipos de observer (`Subscriber` e `Feed`)
