---
type: concept
title: "AsyncLocalStorage"
aliases: ["async local storage", "ALS", "contexto assíncrono Node.js"]
date_created: 2026-06-01
date_updated: 2026-06-01
source_count: 1
tags: [nodejs, javascript, async, contexto, rastreamento, performance]
skill: tech-mentor-backend
status: draft
---

# AsyncLocalStorage

API do módulo `async_hooks` do Node.js que permite armazenar e recuperar dados associados a um contexto assíncrono específico — sem passar o dado por parâmetros através de toda a call stack. Cada requisição HTTP, por exemplo, pode ter seu próprio "armazém" isolado.

## Analogia

É o equivalente a uma variável de thread-local storage em linguagens com threads reais (Java, Go) — mas para o modelo assíncrono de single-thread do Node.js.

## API básica

```javascript
import { AsyncLocalStorage } from 'async_hooks';

const storage = new AsyncLocalStorage();

// Inicia um novo contexto com um valor
storage.run({ userId: 123, response: res }, () => {
  // Tudo que acontecer aqui (e em funções chamadas por aqui)
  // tem acesso a esse contexto via getStore()
  processRequest();
});

// Em qualquer lugar da call stack assíncrona:
function processRequest() {
  const { userId } = storage.getStore(); // retorna { userId: 123, response: res }
}
```

## Caso de uso central: rastrear cliente em Let it Crash

No padrão [[let-it-crash]] sem `try/catch`, os handlers globais de erro (`uncaughtException`, `unhandledRejection`) precisam saber **qual cliente** causou o erro para responder apenas ele. AsyncLocalStorage resolve isso:

```javascript
// Por requisição: inicia contexto com response e clientId
app.use((req, res, next) => {
  storage.run({ response: res, clientId: req.id }, () => next());
});

// No handler de erro global: recupera o contexto do cliente
process.on('unhandledRejection', () => {
  const { response, clientId } = storage.getStore();
  response.status(500).json({ message: 'Pedido falhou.' });
  // ... graceful shutdown
});
```

## Outros casos de uso

- **Request ID / trace ID**: propagar um ID de rastreamento por toda a call stack sem passar como parâmetro
- **Tenant isolation**: multi-tenancy onde cada requisição carrega o tenant atual
- **Logging contextual**: adicionar contexto da requisição a todos os logs sem passar logger por parâmetro
- **Transações de banco de dados**: associar uma transação aberta à requisição que a iniciou

## Armadilha crítica: `async` na função de contexto

```javascript
// ❌ Quebra o rastreamento — getStore() retorna undefined no handler de erro
storage.run(store, async () => {
  await handleRequest(req, res);
});

// ✅ Correto — async/await deve ficar dentro do contexto, não na função de entrada
storage.run(store, () => {
  handleRequest(req, res); // handleRequest pode usar async/await internamente
});
```

Quando o `async` está na função passada para `.run()`, o Node.js cria uma nova microtask antes de entrar no contexto — e o `AsyncLocalStorage` não consegue propagá-lo corretamente para handlers de erro globais.

## Performance

AsyncLocalStorage é uma das APIs mais avançadas e complexas do Node.js. O overhead existe mas é considerado aceitável para rastreamento de contexto por requisição em cenários de produção. Medir em benchmarks próprios para workloads de alta concorrência.

## Relação com outros conceitos

- [[let-it-crash]] — caso de uso principal desta fonte
- [[graceful-shutdown]] — AsyncLocalStorage viabiliza o shutdown controlado por cliente
- [[excecao-vs-erro]] — contexto é necessário apenas quando exceções ocorrem

## Key sources

- [[wiki/sources/let-it-crash-nodejs-asynclocalstorage]] — uso prático para rastrear cliente que gerou exceção; armadilha do `async` na função de contexto
