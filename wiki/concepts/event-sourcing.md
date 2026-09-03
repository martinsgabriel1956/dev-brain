---
type: concept
title: "Event Sourcing"
aliases: ["event store", "append-only log", "eventsourcing"]
date_created: 2026-05-31
date_updated: 2026-09-01
source_count: 8
tags: [event-sourcing, arquitetura, cqrs, ddd, imutabilidade, fintech]
skill: tech-mentor-backend
status: stable
---

# Event Sourcing

## TL;DR

Em vez de persistir o **estado atual**, você persiste a **sequência de eventos que levou a esse estado**. O estado é sempre derivado por replay do log. Eventos são fatos imutáveis sobre o passado.

## Modelo Mental

```
Tradicional (state-based):
  saldo = 1000
  UPDATE conta SET saldo = 950 WHERE id = 1  ← destrói histórico

Event Sourcing (event-based):
  [DepositoCreditado: +1500]
  [PIXDebitado: -50]
  [CassinoDebitado: -100]
  [TED: -400]
  → saldo atual = replay de todos os eventos = 950
```

A conta bancária é a analogia canônica: o extrato é o event log, o saldo é o estado derivado.

## Propriedades dos Eventos

- **Imutáveis** — fatos sobre o passado não mudam
- **Append-only** — nunca UPDATE/DELETE no event log
- **Sequenciados** — cada evento tem posição no stream
- **Nomeados no passado** — `OrderShipped`, `PaymentConfirmed`, não `ShipOrder`

## Quando Usar

✅ Auditoria completa obrigatória (financeiro, compliance, regulatório)
✅ Time-travel: "qual era o estado em T?"
✅ Múltiplas projeções do mesmo dado ([[cqrs]])
✅ Replay: reconstruir projeções corrompidas ou criar novas
✅ Bugs 100% reproduzíveis (salva eventos, dá replay)
❌ Queries ad-hoc complexas — event sourcing não é OLAP
❌ Times sem experiência em [[ddd]] — complexidade alta

## Snapshots

Para aggregates com muitos eventos, replay completo fica lento. Solução: snapshots periódicos.

```
Snapshot em t=1000: { saldo: 950, versão: 1000 }
Replay: snapshot + eventos de t=1001 em diante
```

## Vantagens

- **Auditoria nativa** — trilha completa sem esforço extra
- **Bugs reproduzíveis** — salva o event log, dá play, reproduz 100%
- **Testes determinísticos** — dado input de eventos, output é previsível
- **Sem [[complexidade-acidental]]** de estado mutável
- **Time-travel** — ver estado em qualquer ponto do histórico ([[datomic]])

## Desvantagens

- Curva de aprendizado alta
- Event log cresce indefinidamente → precisa de snapshot strategy
- Queries sobre estado atual exigem projeções ([[cqrs]])
- Complexidade arquitetural — raramente usado fora de bancos/apostas/compliance

## Relação com CQRS

Event Sourcing e [[cqrs]] andam juntos mas são independentes:
- Event Sourcing resolve *como persistir*
- CQRS resolve *como separar leitura de escrita*

Em prática financeira: events persistidos no store, projeções (read models) construídas por [[cqrs]] para queries rápidas.

## Uso no Nubank

O [[nubank]] usa Event Sourcing + [[datomic]] como fundação. O Datomic é essencialmente um banco de dados que implementa event sourcing nativamente — append-only, com time-travel e snapshots imutáveis.

Adotar Event Sourcing como TO-BE de uma migração de arquitetura segue o mesmo ciclo de qualquer outra mudança arquitetural significativa — AS-IS entendido, POC validada na escala real, coexistência com o modelo anterior. Ver [[wiki/concepts/ciclo-de-mudanca-de-arquitetura]].

## Impedance Mismatch: a Motivação Concreta

[[wiki/sources/cqrs-e-event-sourcing-explicado-na-pratica]] nomeia e detalha a motivação central para persistir eventos em vez de estado: o **impedance mismatch**. Um evento de domínio (ex.: "criar ordem", com lista de produtos, quantidades, preços e ID do consumidor) cabe naturalmente em um único objeto/JSON — mas ao ser persistido em modelo relacional normalizado, se fragmenta em múltiplas linhas de múltiplas tabelas (ex.: uma linha em `users`, duas em `product`, duas em `order_line_items`, uma em `order`). O evento, ao contrário, preserva a forma original da intenção do usuário e pode ser reconstruído em N estruturas relacionais diferentes a partir do mesmo payload.

## Write-Ahead Log: Bancos Relacionais Já Fazem Event Sourcing Internamente

A mesma fonte conecta Event Sourcing ao **write-ahead log (WAL)** de bancos relacionais tradicionais: ao submeter uma transação, o banco (ex.: Postgres) não persiste imediatamente no estado final — primeiro grava a sequência de ações num log (semelhante a um append-only log), e só depois reflete isso no estado presente. Ou seja, o mecanismo interno de um banco relacional convencional já é, estruturalmente, uma forma de Event Sourcing.

## Definição Curta (Macoratti, via Código Fonte TV)

[[wiki/sources/cqrs-dicionario-programador-codigo-fonte-tv]] cita José Carlos Macoratti para uma formulação enxuta da ideia central: garantir que toda alteração de estado de uma aplicação seja capturada em um objeto de evento, e que esses eventos sejam armazenados na sequência em que foram aplicados, pelo mesmo tempo de vida útil do estado da aplicação. Consistente com a definição já registrada acima — sem contradição, apenas outra formulação da mesma regra de append-only + replay.

## Command Sourcing: Armazenar os Comandos, Não Só os Eventos

[[wiki/sources/cqrs-event-sourcing-full-cycle-wesley-williams]] descreve uma ideia atribuída a [[wiki/entities/greg-young|Greg Young]], **Command Sourcing**, citada como raramente aplicada na prática: além de armazenar os eventos (o que aconteceu), armazenar também os comandos originais (a intenção que gerou o evento). Como o mesmo comando pode produzir resultados diferentes dependendo do contexto de negócio no momento da execução (ex.: taxa de juros alta vs. baixa), ter os comandos preservados permite reexecutá-los sob outro contexto e simular decisões de negócio alternativas — algo que eventos sozinhos (que já capturam o resultado, não a intenção) não permitem.

## Exemplo: Placar de Futebol como Estado Derivado

[[wiki/sources/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto]] usa um domínio diferente do bancário para o mesmo princípio: um placar de futebol ("2 a 1") **não é armazenado** como linha mutável numa tabela — é *derivado* processando, em ordem, eventos como `match_started`, `goal`, `goal`, `match_ended`, cada um com um campo de sequência para desempatar eventos que caem no mesmo minuto. O evento em si passa por um tópico [[wiki/concepts/kafka|Kafka]], que retém a timeline completa — diferente de uma fila tradicional, que remove a mensagem ao entregá-la — viabilizando tanto a reconstrução do estado quanto o event replay.

**Custo real de recalcular a timeline a cada leitura**: essa mesma fonte expõe o problema prático que motiva [[wiki/concepts/cqrs|projeções/read models]] — reconstruir o placar do zero a cada requisição (buscar todos os gols, ordenar, interpretar payload, somar por time, considerar VAR) não escala com um volume alto de leitores simultâneos. A solução aplicada foi um consumer dedicado, mantendo um estado pré-computado em [[wiki/concepts/redis|Redis]], em vez de recalcular a projeção a cada leitura — CQRS na prática, sem nomear o padrão explicitamente.

## Variante Leve: Histórico Sem Event Store Completo

[[wiki/sources/event-sourcing-conceito-pros-contras-cases-mercado]] descreve uma alternativa pragmática para quando só se precisa de rastro histórico, sem implementar Event Sourcing por completo (sem event store dedicado, sem streaming): uma tabela append-only onde cada mudança de estado é um novo insert, e o registro anterior é marcado com um campo `enabled = false` (mantendo só um `enabled = true` por entidade) em vez de sofrer update de valor. Exemplo de modelagem: uma tabela de **saldo** (um único registro `enabled = true`, todo o histórico preservado nos anteriores) ligada a uma tabela de **extrato** (todos os lançamentos válidos, quase sempre só inserts — um lançamento errado gera um novo registro de estorno, não uma edição do original) via uma tabela `account` que desacopla cliente de conta corrente. Essa mesma fonte nota que esse desacoplamento (extrato referenciando só o `account_id`, não o cliente diretamente) já ajuda com [[wiki/concepts/compliance|LGPD]]: apagar os dados do cliente não exige tocar no histórico financeiro.

## Arquitetura Completa: Streaming + Registro Dedicado + Replay

A mesma fonte descreve a arquitetura de referência para aplicar o padrão por completo: APIs orquestram microsserviços coreografados que publicam mudanças de estado numa ferramenta de streaming (Kafka ou equivalente — tratado como "black box", não precisa ser Kafka necessariamente). Um componente dedicado ("o Betty" — apelido informal do apresentador) registra cada mudança tanto no banco de eventos/streaming quanto num banco SQL transacional, tipicamente serializando o próprio objeto de domínio. Um segundo componente faz o caminho inverso — lê o evento do banco e o relança na fila no estado daquele momento passado — fazendo os microsserviços reexecutarem as ações e reproduzirem exatamente o que aconteceu, para fins de auditoria ou troubleshooting.

## Cases de Mercado

[[wiki/sources/event-sourcing-conceito-pros-contras-cases-mercado]] lista quatro cenários reais (relato de experiência do apresentador, sem nomes de empresa) onde aplicou Event Sourcing: (1) **[[wiki/concepts/saga-pattern|Saga]]** — necessário para garantir contexto transacional sem transação de banco real, permitindo desfazer etapas em caso de falha; (2) **opt-in/[[wiki/concepts/compliance|LGPD]]** — histórico de consentimento do cliente e broadcast confiável de mudanças para parceiros (cobrança, marketing); (3) **auditoria de segurança financeira** — adotado após uma empresa sofrer auditoria sem os dados necessários; (4) **faturamento de telecomunicações** — controle de consumo (dados, voz, pacotes) sujeito a fiscalização da Anatel; segundo o autor, raríssimas operadoras aplicam o padrão corretamente, mas as que aplicam conseguem justificar rapidamente cada lançamento ao regulador.

## Key Sources

- [[wiki/sources/cqrs-martin-fowler]] — post original do bliki (2011) já lista Event Sourcing como padrão que combina naturalmente com CQRS
- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[wiki/sources/ciclo-de-mudanca-de-arquitetura]] — citado como exemplo de decisão de TO-BE que exige o ciclo AS-IS/POC/migração
- [[wiki/sources/cqrs-dicionario-programador-codigo-fonte-tv]] — definição curta citando José Carlos Macoratti
- [[wiki/sources/cqrs-e-event-sourcing-explicado-na-pratica]] — impedance mismatch como motivação concreta; conexão com write-ahead log de bancos relacionais; tese de que adotar Event Sourcing é decisão de domínio, não técnica
- [[wiki/sources/cqrs-event-sourcing-full-cycle-wesley-williams]] — exemplo do Datomic/Nubank como banco imutável; conceito de Command Sourcing (Greg Young)
- [[wiki/sources/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto]] — placar de futebol como exemplo concreto de estado derivado de uma timeline via Kafka; custo de recalcular a timeline a cada leitura como motivação prática para cache de estado pré-computado
- [[wiki/sources/event-sourcing-conceito-pros-contras-cases-mercado]] — variante leve via insert + flag `enabled` sem event store completo; arquitetura de referência (streaming + componente de registro + componente de replay); cases de mercado (Saga, opt-in/LGPD, auditoria financeira, faturamento de telecom sob fiscalização Anatel); prós/contras consolidados (reprodutibilidade total vs. volume de dados/complexidade/tempo de desenvolvimento)
