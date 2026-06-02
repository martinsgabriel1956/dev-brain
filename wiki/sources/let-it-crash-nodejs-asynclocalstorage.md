---
type: source
title: "Let It Crash — Graceful Shutdown com AsyncLocalStorage no Node.js"
aliases: []
date_created: 2026-06-01
date_updated: 2026-06-01
source_count: 0
tags: [let-it-crash, nodejs, graceful-shutdown, asynclocalstorage, resiliencia, excecao, backend, javascript]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/let-it-crash-nodejs-asynclocalstorage.md
source_url: ""
author: "Eric Lenda"
date_published: ""
date_ingested: 2026-06-01
---

# Let It Crash — Graceful Shutdown com AsyncLocalStorage no Node.js

## TL;DR

Filosofia de design onde o sistema é projetado para **quebrar de forma controlada** e uma nova cópia ser recriada por um orquestrador, em vez de tentar se recuperar de exceções imprevisíveis. Implementado em Node.js sem `try/catch` usando `AsyncLocalStorage` para rastrear o contexto assíncrono de cada cliente individualmente.

---

## Argumento Central

### O problema com recuperação de erros

Tentar se reconectar com banco de dados ou fazer retries após exceções parece sensato, mas pode mascarar problemas mais sérios:

- Vazamento de memória
- Estouro de limite de conexões

Nesses casos, a recuperação nunca termina de fato — o sistema fica num estado corrompido respondendo de forma imprevisível.

### A solução: deixar quebrar com controle

Em vez de tentar recuperar, executar uma sequência determinística de encerramento e deixar o orquestrador recriar a aplicação em estado limpo.

---

## Claims Principais

### Claim 1 — Erro ≠ Exceção

**Evidência:** A distinção é a base de toda a estratégia.

| Tipo | O que é | Exemplos | Como tratar |
|---|---|---|---|
| **Erro de domínio** | Previsível, dentro do controle | Campo inválido, usuário não encontrado | Retornar resposta de erro — sem exceção |
| **Exceção** | Imprevisível, fora do controle | Banco de dados fora, sem memória, sem rede | *Let it Crash* |

**Confiança:** Alta — distinção conceitual clássica, bem fundamentada.

### Claim 2 — Sequência de graceful shutdown

**Evidência:** Demonstrado ao vivo: banco de dados é derrubado e a aplicação executa o fluxo completo.

```
1. Responder o cliente que gerou o erro (feedback imediato)
2. server.close() → para novas conexões, aguarda pendentes terminarem
3. Encerrar conexões externas (sequelize.close())
4. process.exit(1)
5. Orquestrador detecta → cria novas réplicas
```

**Confiança:** Alta — fluxo concreto com código demonstrado.

### Claim 3 — AsyncLocalStorage rastreia contexto por cliente sem try/catch

**Evidência:** Usando `storage.run({ response, clientId }, () => handleRequest(...))`, cada requisição vive num contexto assíncrono isolado. Os handlers globais `uncaughtException` e `unhandledRejection` chamam `storage.getStore()` para recuperar o `response` do cliente específico que gerou o erro.

**Confiança:** Alta — demonstrado com código e com prova de funcionamento.

### Claim 4 — Armadilha: `async` na função de contexto quebra o rastreamento

**Evidência:** Quando se adiciona `async` na função passada ao `.run()`, o Node.js perde o rastreamento e `getStore()` retorna `undefined`.

```javascript
// ❌ Quebra o contexto
storage.run(store, async () => { await handleRequest(req, res); });

// ✅ Correto
storage.run(store, () => { handleRequest(req, res); }); // async fica dentro do handleRequest
```

**Confiança:** Alta — descoberta empírica demonstrada com dois cenários no vídeo.

---

## Entidades

- [[wiki/entities/eric-lenda]] — autor do vídeo; canal de JavaScript/Node.js

---

## Conceitos Tocados

- [[wiki/concepts/let-it-crash]] — conceito central desta fonte
- [[wiki/concepts/graceful-shutdown]] — implementação prática do Let it Crash
- [[wiki/concepts/asynclocalstorage]] — API do Node.js usada para rastrear contexto por cliente
- [[wiki/concepts/excecao-vs-erro]] — distinção fundamental para aplicar a estratégia corretamente
- [[wiki/concepts/robustez-de-sistemas]] — Let it Crash como estratégia de robustez sistêmica

---

## Questões em Aberto

1. Como aplicar Let it Crash em arquiteturas serverless (Lambda, Cloud Functions) onde não há processo persistente nem orquestrador tradicional?
2. Qual o impacto de `server.close()` em aplicações com WebSockets de longa duração — conexões persistentes são encerradas imediatamente?
3. AsyncLocalStorage tem custo de performance mensurável em alta concorrência? O autor menciona que não compromete performance, mas não apresenta benchmarks.
4. Como combinar Let it Crash com Circuit Breaker? São complementares ou há sobreposição?
