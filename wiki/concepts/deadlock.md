---
type: concept
title: "Deadlock"
aliases: ["deadlock", "impasse", "bloqueio mútuo", "abraço mortal"]
date_created: 2026-04-22
date_updated: 2026-07-30
source_count: 5
tags: [sistema-operacional, concorrência, sincronização, cs-fundamentals, mysql, gap-locking]
skill: cs-fundamentals
status: stable
---

# Deadlock

Situação onde duas ou mais threads ficam bloqueadas para sempre, cada uma esperando um recurso que a outra segura.

## Como acontece

```
Thread A: segura recurso 1, espera recurso 2
Thread B: segura recurso 2, espera recurso 1

→ Nenhuma das duas avança. Para sempre.
```

Analogia: cruzamento onde 4 carros chegam ao mesmo tempo e nenhum dá passagem — todo mundo fica parado.

## As 4 Condições de Coffman

Para um deadlock ocorrer, as 4 condições devem ser verdadeiras simultaneamente:

1. **Mutual exclusion**: recurso pode ser usado por apenas uma thread por vez
2. **Hold and wait**: thread segura recurso enquanto espera outro
3. **No preemption**: recurso só é liberado voluntariamente
4. **Circular wait**: cadeia circular de espera (A→B→C→A)

Quebrar qualquer uma das 4 previne deadlock.

## Estratégias de prevenção

- **Ordenação de locks**: sempre adquirir locks na mesma ordem global (quebra circular wait)
- **Lock timeout**: tentar adquirir com timeout — se não conseguir, libera o que tem e tenta de novo
- **Lock hierarchy**: numerar recursos, sempre pegar em ordem crescente
- **Detecção + recovery**: sistema detecta ciclo no grafo de espera e mata um dos processos

## Deadlock vs Starvation

- **Deadlock**: threads bloqueadas para sempre (nenhuma avança)
- **Starvation**: thread nunca é agendada, mas o sistema avança. Solução: aging de prioridade no [[concepts/escalonador]]

## Deadlock por Banco de Dados Compartilhado entre Microsserviços

Além de gap locking, existe uma causa mais estrutural de deadlock em sistemas distribuídos: dois microsserviços (ex.: payments e shipping) compartilhando o mesmo banco de dados (**shared database**). Enquanto um serviço está escrevendo, o outro fica bloqueado, porque o banco precisa manter consistência de dados — o serviço que espera fica em deadlock até a atualização do primeiro terminar. A solução apontada é [[wiki/concepts/database-per-service]] — isolar um banco por serviço —, que elimina esse deadlock específico mas introduz um problema novo de atomicidade entre serviços, resolvido por [[wiki/concepts/two-phase-commit]] ou [[wiki/concepts/saga-pattern]]. Ver [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]].

## Deadlock em Banco de Dados: Gap Locking do MySQL

Deadlock não é só de threads em memória — bancos relacionais também sofrem. O InnoDB (MySQL) trava, por padrão, não só a linha lida mas também os espaços vazios ("gaps") ao redor dela, para prevenir phantom reads em `REPEATABLE READ`. Isso amplia o escopo de bloqueio muito além do necessário e pode gerar deadlock sob alta concorrência de inserts/deletes na mesma faixa de índice — mesmo quando as transações, à primeira vista, não deveriam competir pelo mesmo recurso. Ver [[wiki/concepts/mysql]] e o caso da [[wiki/entities/shopify]] em [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]], que precisou corrigir gap locking (além de PK mal desenhada e ordem de execução divergente) antes de escalar reserva de estoque via [[wiki/concepts/skip-locked]].

## Ver também

- [[concepts/mutex]] — mecanismo que, se mal usado, causa deadlock
- [[concepts/thread]] — unidade de execução que pode entrar em deadlock
- [[concepts/escalonador]] — aging evita starvation mas não resolve deadlock

## Key Sources

- [[sources/sistema-operacional-por-baixo-dos-panos]]
- [[sources/como-sistemas-operacionais-funcionam]]
- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]] — gap locking do MySQL como causa de deadlock em reserva de estoque de alta concorrência
- [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]] — deadlock por banco de dados compartilhado entre microsserviços, resolvido isolando um banco por serviço
