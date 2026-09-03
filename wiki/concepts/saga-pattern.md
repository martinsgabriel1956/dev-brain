---
type: concept
title: "Saga Pattern"
aliases: ["saga", "saga distribuída", "compensating transactions"]
date_created: 2026-04-22
date_updated: 2026-09-01
source_count: 7
tags: [sistemas-distribuidos, consistencia, saga, microsservicos, compensação]
skill: tech-mentor-system-design
status: stub
---

# Saga Pattern

Padrão para transações distribuídas sem locks distribuídos — usa consistência eventual com transações de compensação.

## Problema que Resolve

[[concepts/two-phase-commit]] requer locks distribuídos. Em microsserviços, isso é impraticável — serviços são independentes, não compartilham banco.

## Mecanismo

Sequência de transações locais. Se uma falha, as anteriores são **compensadas** (revertidas via operação inversa).

```
T1 (Pagamento) → T2 (Reserva) → T3 (Envio)
         ↓ falha em T3
C2 (Cancela Reserva) → C1 (Estorna Pagamento)
```

## Dois Estilos

- **Coreografado** — cada serviço publica evento e reage a eventos de outros. Sem orquestrador central.
- **Orquestrado** — orquestrador central comanda cada passo. Mais visível, mais acoplado.

Essa escolha (coreografia vs. orquestração) é citada em [[wiki/sources/ciclo-de-mudanca-de-arquitetura]] como um exemplo de decisão de TO-BE que precisa ser validada por POC antes da migração — ver [[wiki/concepts/ciclo-de-mudanca-de-arquitetura]].

## Implementação com Fila (RabbitMQ) — Versão Didática

Uma explicação simplificada apresenta o Saga coreografado como: cada serviço (order, payments, shipping, inventory...) publica na fila (ex.: [[wiki/entities/rabbitmq]]), que garante ordem e evita gargalo de coordenação síncrona — em contraste direto com o [[wiki/concepts/two-phase-commit|two-phase commit]], que trava esperando aprovação sequencial. O trade-off citado: a fila resolve o problema de gargalo, mas cada serviço precisa implementar manualmente sua própria compensação/rollback caso uma etapa falhe — isso é descrito como a parte "muito difícil" de implementar Saga na prática. Essa arquitetura de fila é chamada de [[wiki/concepts/event-driven-architecture]]. Ver [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]].

## Aplicação a Transações Cross-Shard

O mesmo problema resolvido para microsserviços com bancos separados se repete em [[wiki/concepts/sharding|sharding]] de banco de dados: uma transferência que debita um shard e credita outro não pode ser atômica como uma transação local. Exemplo: transferir R$ 50 do usuário 1 (shard A) para o usuário 2 (shard B) — se o débito é concluído e o sistema falha antes do crédito, o dinheiro simplesmente desaparece (usuário 1 fica negativo, usuário 2 nunca recebe). O Saga pattern é citado como a solução recomendada também nesse contexto: débito e crédito como transações locais sequenciais, com compensação (estorno) se a segunda etapa falhar. Ver [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]].

## Trade-off

Consistência eventual — não ACID. Compensações podem falhar também (saga idempotente é obrigatória). Mais complexo que uma transação local, mas escala horizontalmente.

## Relação com Event Sourcing

[[wiki/sources/event-sourcing-conceito-pros-contras-cases-mercado]] cita a aplicação do Saga em microsserviços como um dos casos de mercado mais comuns onde o apresentador precisou aplicar [[wiki/concepts/event-sourcing]]: sem uma transação de banco garantida entre serviços, é necessário registrar o histórico das transações (total ou parcialmente, no espírito do padrão) para poder desfazer uma etapa caso alguma falhe no meio do fluxo — o mecanismo de compensação depende de saber exatamente o que já foi feito.

## Key Sources

- [[sources/3pc]]
- [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]] — saga pattern/consistência eventual citado como conceito que ajuda a lidar com cenários de concorrência e integração mesmo num único banco de dados, fora de arquitetura distribuída
- [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]] — versão didática coreografada via RabbitMQ, contrastada com o gargalo de coordenação do 2PC
- [[wiki/sources/ciclo-de-mudanca-de-arquitetura]] — coreografia vs. orquestração como exemplo de decisão de TO-BE a validar via POC
- [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] — Saga aplicado a transações que cruzam shards de banco de dados (exemplo de transferência financeira entre usuários em shards diferentes)
- [[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]] — teaser no fechamento do vídeo (ainda não desenvolvido como fonte própria): cartão já cobrado quando uma etapa posterior de um fluxo multi-step falha, cenário canônico de compensação que aponta para saga
- [[wiki/sources/event-sourcing-conceito-pros-contras-cases-mercado]] — Saga citado como um dos principais motivadores práticos para aplicar Event Sourcing em microsserviços sem transação de banco garantida
