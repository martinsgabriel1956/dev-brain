---
type: concept
title: "Let It Crash"
aliases: ["deixa quebrar", "let it crash philosophy", "crash-first design"]
date_created: 2026-06-01
date_updated: 2026-06-01
source_count: 1
tags: [resiliencia, arquitetura, backend, erlang, nodejs, excecao, orquestrador]
skill: tech-mentor-backend
status: draft
---

# Let It Crash

Filosofia de design de sistemas onde a aplicação é projetada para **quebrar de forma controlada** quando encontra [[excecao-vs-erro|exceções]] imprevisíveis — em vez de tentar se recuperar delas. O sistema deposita a responsabilidade de retomada no orquestrador (Kubernetes, PM2, etc.), que recria réplicas em estado limpo.

## Origem

Princípio central da linguagem **Erlang** e da plataforma OTP, onde processos são baratos, supervisores monitoram e reiniciam workers com falha, e o isolamento entre processos impede que uma falha se propague. Popularizado fora do ecossistema Erlang pela observação de que estratégias de recuperação complexas frequentemente mascaram problemas em vez de resolvê-los.

## Por que não tentar recuperar?

Estratégias de retry e reconexão parecem prudentes, mas podem estabilizar o sistema num **estado corrompido**:

- **Vazamento de memória**: reconectar não libera a memória já corrompida
- **Estouro de conexões**: tentar abrir novas conexões quando o pool já está no limite piora o problema
- **Estado inconsistente**: objetos em memória que assumiram estado errado continuam sendo usados

A recuperação bem-sucedida de uma exceção é rara — geralmente o sistema precisaria reiniciar de qualquer forma.

## Pré-condição: distinguir erro de exceção

Let it Crash só faz sentido para **[[excecao-vs-erro|exceções]]** — eventos fora do controle da aplicação. Erros de domínio (campo inválido, usuário não encontrado) devem ser tratados normalmente com respostas de erro.

Aplicar Let it Crash a erros de domínio é destruir a aplicação por motivos evitáveis.

## O ciclo correto

```
Exceção acontece
      │
1. Responde o cliente que gerou o erro
2. Para aceitar novas conexões (server.close)
3. Aguarda requisições em andamento terminarem
4. Encerra conexões externas (banco, filas, etc.)
5. process.exit(1)
      │
Orquestrador detecta processo morto
      │
Cria N novas réplicas em estado limpo
      │
Novos pedidos respondidos normalmente
```

Ver [[graceful-shutdown]] para a implementação detalhada desta sequência.

## Contraste com Circuit Breaker

| | Let it Crash | Circuit Breaker |
|---|---|---|
| **Quando** | A própria instância falhou | Dependência externa está degradada |
| **Ação** | Mata o processo, orquestrador recria | Abre o circuito, para de chamar a dependência |
| **Estado** | Processo morre | Processo continua, circuito fecha depois de um tempo |
| **Combinável?** | Sim — complementares |

## Relação com outros conceitos

- [[excecao-vs-erro]] — pré-condição para aplicar corretamente
- [[graceful-shutdown]] — a implementação prática do ciclo
- [[asynclocalstorage]] — mecanismo para responder o cliente correto sem try/catch (Node.js)
- [[robustez-de-sistemas]] — Let it Crash como estratégia de robustez sistêmica
- [[era-agentica]] — relevância crescente: sistemas gerados por IA precisam de estratégias de recuperação robustas

## Key sources

- [[wiki/sources/let-it-crash-nodejs-asynclocalstorage]] — implementação em Node.js sem try/catch com AsyncLocalStorage
