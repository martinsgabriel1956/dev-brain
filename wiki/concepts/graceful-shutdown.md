---
type: concept
title: "Graceful Shutdown"
aliases: ["desligamento gracioso", "encerramento controlado", "shutdown sequence"]
date_created: 2026-06-01
date_updated: 2026-06-01
source_count: 1
tags: [resiliencia, backend, nodejs, processo, orquestrador, infraestrutura]
skill: tech-mentor-backend
status: draft
---

# Graceful Shutdown

Sequência controlada de encerramento de uma aplicação que garante: (1) nenhuma requisição em andamento é abortada abruptamente, (2) o cliente que gerou o erro recebe feedback, e (3) todos os recursos externos são liberados antes do processo morrer.

## Por que importa

Um `process.exit()` imediato após um erro é destrutivo:

- Requisições em andamento são interrompidas — os clientes ficam sem resposta
- Conexões com banco de dados ficam em estado indefinido (transações abertas, locks não liberados)
- O orquestrador pode recriar a instância, mas os danos do encerramento abrupto persistem

## Sequência padrão

```
1. Receber o sinal de encerramento (SIGTERM, uncaughtException, unhandledRejection)
      │
2. Responder o cliente que causou o erro (se aplicável)
      │
3. server.close()
   → Para de aceitar novas conexões
   → Aguarda conexões ativas terminarem (callback executado quando todas fecharem)
      │
4. Encerrar conexões externas
   → Banco de dados (pool de conexões)
   → Filas de mensagens
   → Cache externo
      │
5. process.exit(código)
   → 0: encerramento normal
   → 1: encerramento por erro
```

## Implementação em Node.js

```javascript
// Captura exceção não tratada
process.on('uncaughtException', async (error) => {
  // 1. Responde o cliente (usando AsyncLocalStorage para identificar qual)
  const { response } = storage.getStore() ?? {};
  response?.status(500).json({ message: 'Algo deu errado.' });

  // 2. Para novas conexões, aguarda pendentes
  server.close(async () => {
    // 3. Encerra recursos externos
    await sequelize.close();
    // 4. Encerra o processo
    process.exit(1);
  });
});

// Mesma lógica para Promises rejeitadas
process.on('unhandledRejection', (reason) => { /* ... */ });
```

## Sinais POSIX relevantes

| Sinal | Quando é enviado | Ação padrão |
|---|---|---|
| `SIGTERM` | Kubernetes envia antes de matar o pod | Iniciar graceful shutdown |
| `SIGINT` | Ctrl+C no terminal | Iniciar graceful shutdown |
| `SIGKILL` | Kubernetes força após timeout | Não pode ser capturado |

O Kubernetes envia `SIGTERM` e aguarda um `terminationGracePeriodSeconds` (padrão 30s) antes de enviar `SIGKILL`. A aplicação deve completar o graceful shutdown dentro desse janela.

## Relação com outros conceitos

- [[let-it-crash]] — graceful shutdown é a implementação do ciclo Let it Crash
- [[asynclocalstorage]] — permite identificar o cliente específico a ser respondido durante o shutdown
- [[excecao-vs-erro]] — graceful shutdown só é acionado por exceções, não por erros de domínio
- [[robustez-de-sistemas]] — graceful shutdown é um dos atributos de um sistema robusto

## Key sources

- [[wiki/sources/let-it-crash-nodejs-asynclocalstorage]] — implementação completa em Node.js com Sequelize e AsyncLocalStorage
