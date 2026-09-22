---
type: concept
title: "Outbox Pattern"
aliases: ["transactional outbox", "outbox + cdc", "outbox"]
date_created: 2026-04-22
date_updated: 2026-09-14
source_count: 6
tags: [sistemas-distribuidos, mensageria, outbox, cdc, consistencia, idempotencia, inbox]
skill: tech-mentor-system-design
status: stub
---

# Outbox Pattern

Garante entrega de mensagens/eventos sem [[concepts/two-phase-commit]] — usando uma tabela `outbox` no mesmo banco da transação.

## Mecanismo

```
1. Transação local: escreve no banco + escreve evento na tabela outbox
2. CDC (Debezium) lê o outbox e publica no broker (Kafka, etc.)
3. Broker entrega ao consumidor
```

Atomicidade garantida pela transação local — não precisa de lock distribuído.

## Por que Funciona

Escrever no banco principal e na tabela outbox é uma única transação ACID. O CDC é assíncrono — se falhar, retenta. Garante **at-least-once delivery**.

## Trade-off

Latência adicional (CDC é assíncrono). Consumidor deve ser idempotente (mensagem pode ser entregue mais de uma vez).

## Alternativa ao 2PC

[[concepts/two-phase-commit]] garante entrega síncrona com risco de blocking. Outbox garante entrega assíncrona com risco de duplicação — trade-off de latência vs complexidade.

## Cruzando a Fronteira de Serviço com Identidade Idempotente

Outbox resolve a publicação confiável de um lado da fronteira. Do outro lado, quem consome precisa do complementar — [[wiki/concepts/inbox-pattern]] — para não duplicar o efeito quando o mesmo evento chega mais de uma vez (at-least-once delivery). Em pagamentos, isso é o que permite que a mesma chave de [[wiki/concepts/idempotencia]] atravesse o processo que caiu no meio do caminho: se o processador externo já aprovou a cobrança mas o backend caiu antes de salvar a resposta local, repassar a chave idempotente ao retry (ou reconciliar contra uma referência estável) evita criar uma segunda cobrança.

## Citado Como Solução do Bug da Escrita Dupla em CQRS

[[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] nomeia o problema resolvido por este padrão — "bug da escrita dupla", ver [[wiki/concepts/dual-write-problem]] — no contexto de sincronizar write e read model via eventos em [[wiki/concepts/cqrs]], mas apenas remete a outro vídeo do canal para a solução, sem detalhar o mecanismo (que já está registrado com profundidade acima e em `references/architecture-eda-patterns.md` da skill `tech-mentor-backend`).

## Por Que uma Transação Local Não Basta Sozinha

[[wiki/sources/transactional-outbox-pattern-entrevista-cadastro-usuario]] percorre o raciocínio passo a passo com um exemplo de entrevista (cadastro de usuário + e-mail de boas-vindas): a primeira correção intuitiva para o [[wiki/concepts/dual-write-problem]] é envolver o INSERT no banco e a publicação no broker numa mesma transação de banco de dados. Isso **não resolve** — a transação local não tem poder de atomicidade sobre a chamada externa (Kafka, HTTP). Se a aplicação ou o banco caírem exatamente entre a publicação da mensagem e o `COMMIT`, a mensagem já foi enviada mas o registro nunca foi persistido: o usuário recebe o e-mail de boas-vindas, mas não existe no banco para fazer login. Isso é o motivo estrutural pelo qual o outbox precisa estar **dentro** da mesma transação local do dado de negócio (não como uma segunda operação externa "protegida" por ela).

## Key Sources

- [[sources/3pc]]
- [[wiki/sources/transactional-outbox-pattern-entrevista-cadastro-usuario]] — desafio de entrevista de cadastro de usuário + e-mail de boas-vindas; demonstra por que envolver a chamada externa numa transação de banco não resolve o dual write, e detalha o Outbox Consumer via polling vs. CDC/Debezium como evolução
- [[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] — citação nominal do bug da escrita dupla como risco de sincronizar CQRS via eventos, sem detalhar a solução
- [[wiki/sources/outbox-pattern]]
- [[wiki/sources/idempotencia-pagamentos-retry-sistemas-distribuidos]] — Outbox/Inbox como o par que mantém a identidade da operação atravessando fronteiras de serviço sob entrega at-least-once
- [[wiki/sources/ciclo-de-mudanca-de-arquitetura]] — citado como exemplo de decisão de TO-BE (Transaction Outbox) que exige o ciclo AS-IS/POC/migração, ver [[wiki/concepts/ciclo-de-mudanca-de-arquitetura]]
