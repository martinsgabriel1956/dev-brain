---
type: concept
title: "CQRS — Command Query Responsibility Segregation"
aliases: ["command query responsibility segregation", "cqrs pattern"]
date_created: 2026-05-31
date_updated: 2026-08-27
source_count: 8
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

## Dois Motivadores Independentes: Volume e Modelo

[[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] enquadra a decisão de adotar CQRS como resposta a dois problemas distintos, que podem aparecer separados ou combinados:

- **Volume** — proporção leitura/escrita muito diferente (ex.: logs e sistemas IoT são write-heavy; busca de e-commerce é read-heavy). Justifica escalar cada lado de forma independente.
- **Modelo/assinatura** — payloads de escrita e leitura muito diferentes (ex.: escrita via evento + leitura via HTTP, ou escrita via HTTP + leitura via GraphQL).

Segundo essa fonte, se só o modelo diverge e o volume é parecido, o CQRS tende a ser complexidade desproporcional ao ganho — o verdadeiro trunfo do padrão aparece quando **as duas divergências se combinam**.

## Forma Mais Simples: Mesmo Código-Fonte, Deployments com Escala Diferente

Antes de separar em serviços/código-fonte distintos, a forma mais simples de CQRS é manter **o mesmo código-fonte** com dois conjuntos de deployments escalados de forma independente (ex.: 30 réplicas de escrita vs. 3 de leitura), com o [[wiki/concepts/api-gateway]] roteando por método HTTP (POST/PUT → escrita, GET → leitura). Isso já basta para ter divisão de responsabilidade entre comando e consulta — código-fonte de fato separado costuma vir depois, quando o serviço "ganha corpo" ou quando escrita e leitura passam a usar bases/protocolos diferentes. Ver [[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]].

## Seis Técnicas de Sincronização: Consistência Forte vs. Eventual

[[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] organiza as estratégias de sincronização write→read em duas categorias. O argumento central: cada técnica de consistência forte resolve bem **ou** volume **ou** modelo, nunca os dois — só a consistência eventual entrega o trunfo completo do CQRS (escalar volume e ter modelo dedicado ao mesmo tempo).

**Consistência forte** (pouco comum em CQRS pleno, mas útil como primeiro passo de migração):

1. **Mesma base de dados com views/[[wiki/concepts/materialized-view|materialized views]]** — comando dá `UPDATE` na tabela, leitura faz `SELECT` numa view. Resolve modelo (API de consulta dedicada), não resolve volume (gargalo de banco compartilhado permanece — escalar a escrita ainda impacta a leitura).
2. **Escrita em transação cruzando write e query service** — o serviço de escrita grava na própria base e, na mesma operação, escreve também na base do serviço de leitura. Quebra a separação de responsabilidade (o query service vira também um serviço de escrita) e não resolve volume, mas preserva um modelo de leitura dedicado.
3. **[[wiki/concepts/api-composition|API Composition]]** — o query service perde base própria e passa a ter só cache; ao receber uma consulta, verifica o cache e, se ausente, propaga chamadas em fan-out para os serviços downstream que têm a informação, compõe e armazena o resultado. Funcionalmente equivalente a um BFF de leitura.

**Consistência eventual** (onde o autor situa a maioria das implementações reais de CQRS):

1. **[[wiki/concepts/read-replicas|Read replicas]]** — cluster com main node de escrita e réplicas de leitura (Aurora gerencia isso automaticamente; Postgres pode ser configurado manualmente). O read model preserva exatamente o schema da base de escrita.
2. **Eventos via broker ([[wiki/concepts/event-driven-architecture|EDA]])** — Kafka, RabbitMQ, SNS/SQS. Diferente das réplicas, o query service pode transformar a informação no formato final que quiser ao consumir o evento (ex.: escrita relacional → leitura em Elasticsearch/Solr para busca textual/facetada). Risco explícito: o **[[wiki/concepts/dual-write-problem|bug da escrita dupla]]** — escrever na base e publicar o evento não são atômicos por padrão; ver [[wiki/concepts/outbox-pattern]] para a solução (transactional outbox), que essa fonte cita apenas de passagem.
3. **Polling/job periódico** — o query service busca mudanças acumuladas de tempos em tempos (ex.: logs em S3, tabela temporária exposta via API), em vez de reagir em tempo real a cada mudança.

## Key Sources

- [[wiki/sources/cqrs-martin-fowler]] — post original do bliki de Martin Fowler (2011); origem textual da definição mais citada; tom de cautela mais forte ("a maioria das implementações que vi foi problemática"); amarra o escopo de aplicação a bounded context
- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[wiki/sources/como-arquitetar-com-cache-e-redis]]
- [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]] — versão didática write/read split com read replicas e trade-off de replication lag
- [[wiki/sources/cqrs-dicionario-programador-codigo-fonte-tv]] — progressão de cenários de motivação (single-user → LAN → SaaS multi-tenant), task-based UI, command bus, e as quatro estratégias de sincronização (automática, eventual, controlada, sob demanda)
- [[wiki/sources/cqrs-e-event-sourcing-explicado-na-pratica]] — deriva CQRS de CQS (get/set em nível de função); fragmentação física do banco por natureza de carga como o "verdadeiro ganho"; tese de que CQRS quase sempre existe a serviço de Event Sourcing
- [[wiki/sources/cqrs-event-sourcing-full-cycle-wesley-williams]] — atribui a criação do CQRS a Greg Young; motivação via exemplo de agregado DDD; erro comum de reaproveitar models entre comando e leitura (viola SRP)
- [[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] — dois motivadores independentes (volume e modelo/assinatura); CQRS sem código-fonte separado (mesmo código, deployments com escala diferente); seis técnicas de sincronização organizadas em consistência forte (mesma base+views, transação cruzada, API Composition) vs. eventual (read replicas, eventos com bug da escrita dupla, polling)
