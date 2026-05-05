# Sete Padrões de Design de Software

**Fonte:** Vídeo do canal Forest (YouTube)
**Tema:** Design Patterns — Criacionais, Estruturais e Comportamentais
**Data de adição:** 2026-05-05

---

## Contexto

Em 1994, quatro desenvolvedores conhecidos como **Gang of Four** escreveram um livro que documentou, catalogou e formalizou 23 padrões de design amplamente utilizados. Todos os 23 se encaixam em três categorias:

- **Criacionais** — como objetos são criados
- **Estruturais** — como objetos se relacionam entre si
- **Comportamentais** — como objetos se comunicam e distribuem responsabilidades

---

## Padrões Criacionais

### 1. Singleton

**Problema:** você precisa de uma única instância acessível globalmente — como um sistema de logging centralizado.

**Sem Singleton:**
```typescript
const logger1 = new Logger(); // escreve no mesmo arquivo
const logger2 = new Logger(); // conflito, caos
```

**Com Singleton:**
```typescript
const logger1 = Logger.getInstance();
const logger2 = Logger.getInstance(); // mesma instância
```

**Quando usar:** quando você precisa garantir uma única instância — pool de conexões com banco de dados, logger centralizado.

**Trade-offs:**
- ✅ Instância única garantida, acesso global
- ❌ Difícil de testar (mock não é trivial)
- ❌ Em ambientes multi-thread, precisa de tratamento especial
- ⚠️ Na prática, é uma variável global glorificada — use com cuidado

---

### 2. Builder

**Problema:** criar objetos complexos com muitos parâmetros opcionais.

**Sem Builder:**
```typescript
new HttpRequest("https://api.exemplo.com", "POST", headers, body, timeout, retryLogic);
```

**Com Builder:**
```typescript
class RequestBuilder {
  url: string;
  method: string;
  headers: Record<string, string>;

  setUrl(url: string) { this.url = url; return this; }
  setMethod(method: string) { this.method = method; return this; }
  setHeaders(headers: Record<string, string>) { this.headers = headers; return this; }
  build() { return new HttpRequest(this.url, this.method, this.headers); }
}

const request = new RequestBuilder()
  .setUrl("https://api.exemplo.com")
  .setMethod("POST")
  .setHeaders({ "Content-Type": "application/json" })
  .build();
```

**Quando usar:** construtores com mais parâmetros do que dedos na mão, ou quando a criação acontece passo a passo.

**Trade-offs:**
- ✅ Código legível, extensível sem alterar todos os pontos de criação
- ❌ Mais código up front

---

### 3. Factory

**Problema:** criação de objetos espalhada pelo código com lógica condicional repetida.

**Sem Factory:**
```typescript
if (type === "admin") return new AdminUser();
else if (type === "moderator") return new ModeratorUser();
else return new RegularUser();
// repetido em todo lugar que precisa criar um usuário
```

**Com Factory:**
```typescript
class UserFactory {
  static create(type: string, id: string, name: string) {
    switch (type) {
      case "admin": return new AdminUser(id, name);
      case "moderator": return new ModeratorUser(id, name);
      default: return new RegularUser(id, name);
    }
  }
}

const user = UserFactory.create("admin", "1", "John");
```

**Quando usar:** sempre que o operador `new` aparece espalhado pelo código base.

**Trade-offs:**
- ✅ Toda lógica de criação centralizada, fácil de manter
- ❌ Adiciona uma camada de abstração
- ❌ Classes ficam acopladas à factory

---

## Padrões Estruturais

### 4. Facade

**Problema:** subsistemas complexos que precisam ser orquestrados juntos repetidamente.

**Sem Facade:**
```typescript
const paymentProcessor = new PaymentProcessor();
const inventorySystem = new InventorySystem();
const fraudChecker = new FraudChecker();
const shippingCalculator = new ShippingCalculator();

if (fraudChecker.check(order)) {
  if (inventorySystem.hasStock(order)) {
    if (paymentProcessor.charge(order)) {
      shippingCalculator.calculate(order);
    }
  }
}
// repetido toda vez que um pedido é feito
```

**Com Facade:**
```typescript
class OrderFacade {
  private paymentProcessor = new PaymentProcessor();
  private inventorySystem = new InventorySystem();
  private fraudChecker = new FraudChecker();
  private shippingCalculator = new ShippingCalculator();

  placeOrder(order: Order) {
    if (!this.fraudChecker.check(order)) return;
    if (!this.inventorySystem.hasStock(order)) return;
    if (!this.paymentProcessor.charge(order)) return;
    this.shippingCalculator.calculate(order);
  }
}

const facade = new OrderFacade();
facade.placeOrder(order);
```

**Quando usar:** quando há um conjunto de subsistemas complexos que você precisa simplificar para os consumidores.

**Trade-offs:**
- ✅ Simplicidade para o consumidor, encapsulamento real
- ❌ Pode virar um "God Object" se não houver disciplina

> **Nota:** você provavelmente já usa facades sem perceber — `fetch()`, `ArrayList` do Java, qualquer cliente HTTP de alto nível.

---

### 5. Adapter

**Problema:** integrar uma biblioteca ou API externa que não bate com a interface que seu código espera.

**Sem Adapter:**
```typescript
const weatherApi = new ThirdPartyWeatherApi(); // retorna Celsius e km/h
// toda vez que usar, converter manualmente:
const tempF = (weatherApi.getTempC() * 9/5) + 32;
const speedMph = weatherApi.getSpeedKmh() * 0.621371;
```

**Com Adapter:**
```typescript
interface WeatherApp {
  getTempF(): number;
  getSpeedMph(): number;
}

class WeatherAdapter implements WeatherApp {
  constructor(private weatherApi: ThirdPartyWeatherApi) {}

  getTempF() {
    return (this.weatherApi.getTempC() * 9/5) + 32;
  }

  getSpeedMph() {
    return this.weatherApi.getSpeedKmh() * 0.621371;
  }
}

const weather = new WeatherAdapter(new ThirdPartyWeatherApi());
console.log(weather.getTempF()); // lógica de conversão isolada
```

**Quando usar:** integração com APIs ou libs de terceiros que não seguem a interface esperada pelo seu app.

**Trade-offs:**
- ✅ Conversão isolada, sem repetição, sem modificar a lib externa
- ❌ Pode ficar tedioso para APIs muito grandes

---

## Padrões Comportamentais

### 6. Strategy

**O melhor padrão de todos. Sempre use o Strategy Pattern.**

**Problema:** múltiplas formas de fazer a mesma coisa com `if/else` crescendo indefinidamente.

**Sem Strategy:**
```typescript
class Commuter {
  goToWork(transport: string) {
    if (transport === "car") {
      // lógica de carro
    } else if (transport === "bus") {
      // lógica de ônibus
    } else if (transport === "bike") {
      // lógica de bicicleta
    }
    // continua crescendo...
  }
}
```

**Com Strategy:**
```typescript
interface TransportStrategy {
  execute(): void;
}

class CarStrategy implements TransportStrategy {
  execute() { /* lógica de carro */ }
}

class BusStrategy implements TransportStrategy {
  execute() { /* lógica de ônibus */ }
}

class BikeStrategy implements TransportStrategy {
  execute() { /* lógica de bicicleta */ }
}

class Commuter {
  private strategy: TransportStrategy;

  setStrategy(strategy: TransportStrategy) {
    this.strategy = strategy;
  }

  goToWork() {
    this.strategy.execute();
  }
}

const commuter = new Commuter();
commuter.setStrategy(new CarStrategy());
commuter.goToWork();

commuter.setStrategy(new BikeStrategy());
commuter.goToWork();
```

**Quando usar:** sempre que houver diferentes formas de realizar a mesma operação. Segue o **Open/Closed Principle** — novas estratégias são adicionadas sem tocar no código existente.

**Trade-offs:**
- ✅ Código limpo, extensível, intercambiável
- ❌ Mais classes — mas infinitamente melhor que `if/else` aninhado

---

### 7. Observer

**Problema:** notificar múltiplos objetos quando algo acontece em outro objeto.

**Sem Observer:**
```typescript
class VideoChannel {
  private users: UserAccount[] = [];

  uploadVideo(title: string) {
    for (const user of this.users) {
      // notificar cada usuário manualmente
      // inviável com 600.000 inscritos
    }
  }
}
```

**Com Observer:**
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

**Quando usar:** quando objetos precisam ser notificados automaticamente sobre eventos em outros objetos — monitoramento de erros de servidor, mudanças de estado em componentes, sistemas de eventos.

**Trade-offs:**
- ✅ Desacoplamento, notificação automática
- ❌ Se abusado, pode causar "event callback hell" — um evento dispara outro que dispara outro

---

## Resumo

| Padrão | Categoria | Problema que resolve |
|---|---|---|
| Singleton | Criacional | Garantir uma única instância global |
| Builder | Criacional | Construção de objetos complexos passo a passo |
| Factory | Criacional | Centralizar lógica de criação de objetos |
| Facade | Estrutural | Simplificar acesso a subsistemas complexos |
| Adapter | Estrutural | Compatibilizar interfaces incompatíveis |
| Strategy | Comportamental | Trocar algoritmos/comportamentos em tempo de execução |
| Observer | Comportamental | Notificar múltiplos objetos sobre eventos |

---

## Referência

- **Livro:** *Design Patterns: Elements of Reusable Object-Oriented Software* — Gang of Four (1994)
- **Vídeo original:** Forest (YouTube) — "7 Software Design Patterns"
