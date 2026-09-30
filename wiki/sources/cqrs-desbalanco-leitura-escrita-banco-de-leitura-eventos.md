---
type: source
title: "CQRS — Desbalanço Leitura/Escrita, Banco de Leitura e Sincronização por Eventos"
aliases: ["cqrs desbalanco leitura escrita", "cqrs banco de leitura nosql rabbitmq", "cqrs com rabbitmq e nosql"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 0
tags: [cqrs, read-model, consistencia-eventual, mensageria, rabbitmq, nosql, lock-contention, escalabilidade]
skill: tech-mentor-backend
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/cqrs-desbalanco-leitura-escrita-banco-de-leitura-eventos.md"
source_url: ""
author: ""
date_published: ""
date_ingested: "2026-09-30"
---

## TL;DR

Vídeo didático (autor/canal não identificados) que parte de um problema concreto: sistema com volume muito divergente entre **consulta** e **alteração**, em que as consultas ficam presas por **locks**/transações abertas no mesmo banco ([[wiki/concepts/contencao-de-lock-leitura-escrita]]). A solução proposta é [[wiki/concepts/cqrs]] levado até a **separação física**: o lado de escrita recebe comandos por um [[wiki/concepts/command-bus]], executa-os num command handler com regras de domínio e persiste num **banco relacional** (ex.: SQL Server, Postgres); o lado de leitura consulta direto um **banco desnormalizado** (tipicamente NoSQL/JSON) montado para ficar "o mais próximo possível do que a tela consome" ([[wiki/concepts/read-model]]). A ponte entre os dois é um **evento** publicado após a escrita, transportado como mensagem numa fila de um broker ([[wiki/entities/rabbitmq]]) e processado por um consumer assíncrono ([[wiki/concepts/event-handler]]) que transforma e grava no banco de leitura. A escrita não é onerada, o consumer escala de forma independente, e o preço é um pequeno delay — [[wiki/concepts/eventual-consistency]].

---

## Reivindicações Principais

**Claim:** Com carga de leitura e escrita muito desbalanceada num único banco, as consultas ficam presas por locks de tabela/transações abertas e a contenção degrada o banco e a aplicação; além disso, sem separar as responsabilidades não se escala leitura e escrita individualmente — só o conjunto.
**Evidência:** Descrição do autor, sem medições; o vídeo não cita números nem um sistema real.
**Confiança:** Média — o diagnóstico é plausível, mas a causa depende do SGBD: em bancos com MVCC (ex.: [[wiki/concepts/postgresql]]) leitores não bloqueiam escritores por padrão; o problema de "leitura presa por lock" é mais típico de SGBDs que leem com locks (ex.: [[wiki/concepts/sql-server]] em `READ COMMITTED` sem snapshot) [skill: tech-mentor-backend; ver [[wiki/concepts/isolation-levels]]]. Essa distinção não é feita no vídeo.

**Claim:** CQRS segrega a responsabilidade de alteração e de consulta; o lado de escrita recebe **comandos** roteados por um bus até um command handler, que usa repositório/domínio/entidades e persiste no banco relacional.
**Evidência:** Diagrama e descrição do autor.
**Confiança:** Alta — coincide com [[wiki/sources/cqrs-dicionario-programador-codigo-fonte-tv]] e [[wiki/sources/cqrs-event-sourcing-full-cycle-wesley-williams]]. Ver [[wiki/concepts/command-bus]].

**Claim:** O lado de leitura pode ir direto a um banco próprio, sem passar pelo domínio, por uma camada de dados dedicada; o banco de leitura costuma ser **desnormalizado** (NoSQL, documentos JSON) com o formato próximo do que a UI consome, evitando vários joins.
**Evidência:** Exemplo do autor: tela com cinco informações → um documento com as cinco; em SQL seriam inner joins com duas/três tabelas para trazer descrições de códigos.
**Confiança:** Alta para a ideia; média para a generalização — "costuma ser NoSQL" é uma tendência, não regra: [[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] cita read replicas com o mesmo schema e Elasticsearch como opções de read model. Ver [[wiki/concepts/read-model]] e [[wiki/concepts/nosql]].

**Claim:** A sincronização write → read é feita por **eventos**: após gravar, a aplicação publica um evento (ex.: "formulário cadastrado"); um event handler o recebe, transforma o dado e o persiste no banco de leitura no formato final.
**Evidência:** Descrição do autor; o vídeo diz que não especifica se a comunicação é interna à aplicação ou externa.
**Confiança:** Alta — equivale ao item "Eventos via broker" de [[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]]. Ver [[wiki/concepts/event-handler]] e [[wiki/concepts/event-driven-architecture]].

**Claim:** Os eventos viajam como mensagens numa fila gerenciada por um message broker (ex.: RabbitMQ); um consumer assíncrono, apartado da aplicação de escrita, lê as filas e insere no banco de leitura. A aplicação de escrita só grava e emite o evento — não trabalha ativamente para atualizar o read model — e o consumer pode ser escalado de forma independente.
**Evidência:** Descrição do autor.
**Confiança:** Alta para o desacoplamento escrita/leitura ([[wiki/concepts/mensageria]], [[wiki/concepts/filas-e-workers]], [[wiki/entities/rabbitmq]]). Lacuna (ver Perguntas Abertas): o vídeo não fala de [[wiki/concepts/dual-write-problem]], idempotência do consumer, ordenação nem DLQ.

**Claim:** O resultado é separação lógica (aplicação) e física (bancos) entre alteração e consulta; a estratégia de atualização do read model pode ser imediata ou assíncrona, e na assíncrona há um pequeno delay em relação ao banco de escrita — consistência eventual.
**Evidência:** Fecho do vídeo.
**Confiança:** Alta — ver [[wiki/concepts/eventual-consistency]]; o vídeo não quantifica o delay nem discute impacto em UX (o usuário que acabou de cadastrar não ver o registro na listagem).

---

## Entidades

- [[wiki/entities/rabbitmq]] — broker citado como exemplo de transporte dos eventos.
- SQL Server e Postgres — exemplos de banco relacional de escrita: [[wiki/concepts/sql-server]], [[wiki/concepts/postgresql]].

## Conceitos

- [[wiki/concepts/cqrs]] — padrão central.
- [[wiki/concepts/contencao-de-lock-leitura-escrita]] — o problema motivador (novo).
- [[wiki/concepts/read-model]] — banco de leitura desnormalizado (novo).
- [[wiki/concepts/event-handler]] — consumer que projeta eventos no read model (novo).
- [[wiki/concepts/command-bus]] — roteia comandos ao handler.
- [[wiki/concepts/eventual-consistency]] — custo da sincronização assíncrona.
- [[wiki/concepts/mensageria]], [[wiki/concepts/filas-e-workers]], [[wiki/concepts/event-driven-architecture]] — transporte e processamento assíncrono.
- [[wiki/concepts/nosql]], [[wiki/concepts/mongodb]] — bancos típicos de leitura (MongoDB é exemplo de documento JSON [skill]; o vídeo não cita produto).
- [[wiki/concepts/read-replicas]], [[wiki/concepts/materialized-view]] — alternativas mais simples a um banco de leitura separado [skill].
- [[wiki/concepts/dual-write-problem]] — risco não discutido no vídeo.

---

## Perguntas Abertas

- O vídeo não trata do **dual write**: gravar no banco e publicar o evento não é atômico; se o processo cair entre os dois, o read model nunca recebe o dado. Solução usual: [[wiki/concepts/outbox-pattern]].
- Consumer **idempotente** e ordenação: mensagens podem ser entregues mais de uma vez (ver [[wiki/concepts/idempotencia]], [[wiki/concepts/garantia-de-entrega]]).
- Como lidar com *read-your-writes* no delay de consistência eventual (ex.: UI otimista, ler do write side logo após o comando) — não abordado.
- Antes de separar bancos, o diagnóstico de contenção de lock poderia ser tratado com níveis de isolamento por snapshot, read replicas ou índices — o vídeo vai direto a CQRS. [[wiki/sources/cqrs-martin-fowler]] alerta que a maioria das implementações observadas foi problemática e que um reporting database costuma bastar.

## Citações Brutas

> "você tem um desbalanço muito grande entre a parte de consulta e alteração [...] você tem consulta que fica presa por causa de transação aberta do banco"

> "você não onera a aplicação que está rodando na parte de alteração porque simplesmente ela vai inserir, vai gerar um evento que vai cair numa fila e acabou a relação"

> "dessa forma você tem uma separação tanto lógica da aplicação quanto separação física dos bancos de dados"

## Notas de Ingestão

- Transcrição limpa em [[raw/cqrs-desbalanco-leitura-escrita-banco-de-leitura-eventos]] (já em PT-BR; sem tradução). Erros de reconhecimento de fala corrigidos por contexto e listados no cabeçalho do raw; dois trechos ambíguos marcados com [?].
- Autor e canal não identificados; `author` e `source_url` vazios.
- Extensões vindas da skill estão marcadas `[skill]`.
