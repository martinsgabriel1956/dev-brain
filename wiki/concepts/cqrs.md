---
type: concept
title: "CQRS — Command Query Responsibility Segregation"
aliases: ["command query responsibility segregation", "cqrs pattern"]
date_created: 2026-05-31
date_updated: 2026-08-18
source_count: 7
tags: [cqrs, arquitetura, event-sourcing, ddd, sistemas-distribuidos]
skill: tech-mentor-backend
status: draft
---

# CQRS

## TL;DR

Separar o modelo de **escrita** (Commands) do modelo de **leitura** (Queries). O lado de escrita processa comandos e emite eventos; o lado de leitura mantém projeções otimizadas para consulta.

## Modelo Mental

```
Command side (write):
  [SacarDinheiro command] → [BankHandler] → persiste evento no event log

Query side (read):
  [event log] → reaplica eventos → [Saldo projeção em memória ou read DB]
  → consulta rápida sem tocar o event log
```

O estado em memória (ex: saldo calculado) **nunca vai direto ao banco** — o banco só armazena eventos. O estado é derivado sob demanda.

## Por que Separar

- Modelos de leitura e escrita têm formatos diferentes — forçar um único modelo gera complexidade
- Reads são geralmente muito mais frequentes que writes → otimizar separadamente
- Allows múltiplas projeções do mesmo dado (ex: saldo por conta, saldo por produto, relatório mensal)

## Relação com Event Sourcing

[[event-sourcing]] e CQRS andam juntos mas são independentes:
- Event Sourcing: *como persistir* (eventos imutáveis)
- CQRS: *como separar leitura de escrita*

Em prática: events persistidos, projeções (read models) construídas por CQRS para queries rápidas.

## Uso no Nubank

O [[nubank]] utiliza CQRS em conjunto com [[event-sourcing]] e [[datomic]]. A separação permite que o estado atual (saldo, status) seja reconstruído a partir do event log sem poluir o modelo de domínio.

## Redis como Read Layer

[[redis]] é uma escolha comum como camada de leitura em CQRS: gravações vão ao SQL (fonte de verdade), leituras vão ao Redis (projeção otimizada). Um batch ou trigger sincroniza SQL → Redis.

```
[Domínio]
  ├── Write → [SQL]       ← fonte de verdade
  └── Read  → [Redis]     ← projeção rápida
                  ↑
          [Batch / Trigger de sync]
```

Esse padrão resolve o trade-off leitura/escrita sem abrir mão de consistência nas escritas.

## Versão Didática: Duplicar o Banco em Write/Read

Uma explicação mais simples de CQRS parte de duplicar o banco de um microsserviço em uma instância de escrita (write) e uma (ou mais) de leitura (read/[[wiki/concepts/read-replicas]]), escalando cada lado independentemente — o serviço permanece conectado a ambos. O trade-off central é o **replication lag**: toda escrita no banco de escrita leva um tempo (a fonte estima 1-3 segundos) até ser refletida no banco de leitura, tipicamente via [[wiki/concepts/event-driven-architecture|trigger/evento]]. Sistemas que exigem resposta imediata de baixíssima latência não toleram esse delay — por isso nem toda arquitetura adota CQRS dessa forma. Ver [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]].

## Quando CQRS Passa a Fazer Sentido: Progressão de Cenários

[[wiki/sources/cqrs-dicionario-programador-codigo-fonte-tv]] ilustra a decisão de adotar CQRS com uma progressão de três cenários de concorrência crescente:

1. **Single-user** (app desktop de consultório médico, banco local): sem concorrência de acesso — CQRS não se justifica.
2. **LAN multi-atendente** (clínica com 10 atendentes, servidor local): concorrência moderada — CQRS começa a ser cogitado.
3. **SaaS multi-tenant** (100 mil+ pacientes usando o mesmo sistema simultaneamente): a carga de leitura e escrita diverge o suficiente para que separar os dois modelos valha a complexidade operacional.

A regra prática: CQRS não é uma decisão binária de "usar ou não" — é proporcional ao nível de concorrência e ao tamanho da divergência entre carga de leitura e de escrita.

## UI Baseada em Tarefas (Task-Based UI)

Um Command bem desenhado não deveria mapear 1:1 para um CRUD ("criar", "editar", "excluir"). A UI deveria expor a **intenção do usuário** — ex.: `CancelarPedido`, `AprovarReembolso` — em vez de uma tela genérica de update que edita qualquer campo. Isso mantém o Command semanticamente rico e alinhado ao domínio, em vez de virar uma camada fina sobre o banco. Ver [[wiki/concepts/task-based-ui]].

## Command Bus e a Regra de Void

Reforçando a regra "Commands retornam void ou ID" (já registrada acima): a fonte didática do Código Fonte TV é mais estrita — um Command bem-comportado **não deveria retornar nem o ID**. Se a aplicação depende do retorno de dados a partir de um Command, isso é sinal de que CQRS não deveria ser aplicado àquela parte específica do sistema (ou não deveria ser aplicado ao sistema inteiro). O mecanismo que roteia Commands até seus handlers é chamado de [[wiki/concepts/command-bus]].

## CQS: a Raiz Conceitual em Nível de Função

[[wiki/sources/cqrs-e-event-sourcing-explicado-na-pratica]] deriva CQRS a partir de um conceito anterior e mais primitivo, o **CQS (Command Query Separation)**, aplicado a nível de função em vez de sistema: um `get` nunca muta estado e sempre retorna um valor; um `set` recebe parâmetros e não retorna nada (analogia: getters/setters em Java). CQRS é a mesma ideia elevada ao nível de sistema inteiro — write model e read model como duas aplicações praticamente separadas.

## O Verdadeiro Ganho: Fragmentar Fisicamente o Banco por Natureza de Carga

Além de separar write/read logicamente, o ganho real de CQRS aparece ao fragmentar o banco em instâncias **fisicamente diferentes**, escolhidas pela natureza da carga: um banco colunar para agregação (ex.: contagem de views), um relacional (Postgres) para queries estruturadas complexas, e um NoSQL (DynamoDB, MongoDB) para escritas rápidas — cada um podendo inclusive servir um cliente/sistema diferente (analytics, read model "normal", logs). Ver [[wiki/sources/cqrs-e-event-sourcing-explicado-na-pratica]].

## Estratégias de Sincronização Write → Read

Além da dicotomia síncrona/assíncrona já registrada acima (ver "Redis como Read Layer"), existem variações mais finas de como sincronizar o read model:

- **Automática**: cada mudança de estado dispara imediatamente um processo síncrono no lado de leitura.
- **Eventual**: sincronização assíncrona, com um delay tolerado — ex. contagem de views de vídeo no YouTube, que não atualiza em tempo real.
- **Controlada**: disparo periódico agendado (batch).
- **Sob demanda**: a consistência entre as bases é verificada a cada consulta.

Mensageria ([[fila]], [[filas-e-workers]]) não é obrigatória para implementar sincronização eventual, mas é uma escolha comum.

## Origem: Greg Young e Agregados DDD

[[wiki/sources/cqrs-event-sourcing-full-cycle-wesley-williams]] atribui a criação do CQRS a [[wiki/entities/greg-young|Greg Young]] (baseado em CQS) e ancora a motivação prática num exemplo concreto de agregado em [[wiki/concepts/ddd|DDD]]: um agregado de ordem de serviço (ordem → pedido → cliente → indicação) sempre carrega tudo junto ao ser buscado via repositório, garantindo invariantes de domínio, mas tornando consultas de exibição desnecessariamente pesadas quando só uma parte dos dados é necessária. Separar o sistema em um lado de comandos (que segue os agregados) e um lado de leitura (livre da estrutura do agregado, podendo usar bancos orientados a documento ou a grafo) resolve essa rigidez.

## Origem Textual: o Post de Martin Fowler (2011)

[[wiki/sources/cqrs-martin-fowler]] é a fonte primária mais antiga já ingerida sobre CQRS — o post do bliki de [[wiki/entities/martin-fowler|Martin Fowler]] (14/07/2011) que popularizou a definição hoje mais citada: separar o modelo conceitual de comando (escrita) do de consulta (leitura), porque usar o mesmo modelo para as duas responsabilidades, em domínios complexos, produz um modelo mais complexo que não atende bem nenhuma delas. Fowler restringe o escopo de aplicação a dois cenários — domínios complexos onde a separação simplifica genuinamente a modelagem (minoria dos casos), e aplicações de alta performance com cargas de leitura/escrita muito diferentes exigindo escalabilidade independente — e amarra a decisão de escopo ao conceito de [[wiki/concepts/bounded-context]]: CQRS nunca deve ser aplicado ao sistema inteiro, só a bounded contexts específicos.

**Tom de cautela mais forte que as fontes derivadas:** Fowler afirma diretamente que a maioria das implementações de CQRS que observou se provou problemática, e sugere que um reporting database tradicional muitas vezes obtém benefícios semelhantes sem a sobrecarga de complexidade do CQRS — uma reserva mais explícita do que a lista de trade-offs já registrada acima.

## Key Sources

- [[wiki/sources/cqrs-martin-fowler]] — post original do bliki de Martin Fowler (2011); origem textual da definição mais citada; tom de cautela mais forte ("a maioria das implementações que vi foi problemática"); amarra o escopo de aplicação a bounded context
- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[wiki/sources/como-arquitetar-com-cache-e-redis]]
- [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]] — versão didática write/read split com read replicas e trade-off de replication lag
- [[wiki/sources/cqrs-dicionario-programador-codigo-fonte-tv]] — progressão de cenários de motivação (single-user → LAN → SaaS multi-tenant), task-based UI, command bus, e as quatro estratégias de sincronização (automática, eventual, controlada, sob demanda)
- [[wiki/sources/cqrs-e-event-sourcing-explicado-na-pratica]] — deriva CQRS de CQS (get/set em nível de função); fragmentação física do banco por natureza de carga como o "verdadeiro ganho"; tese de que CQRS quase sempre existe a serviço de Event Sourcing
- [[wiki/sources/cqrs-event-sourcing-full-cycle-wesley-williams]] — atribui a criação do CQRS a Greg Young; motivação via exemplo de agregado DDD; erro comum de reaproveitar models entre comando e leitura (viola SRP)
