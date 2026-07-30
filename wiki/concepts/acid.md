---
type: concept
title: "ACID"
aliases: ["atomicity", "consistency isolation durability", "acid properties"]
date_created: 2026-04-22
date_updated: 2026-07-30
source_count: 7
tags: [banco-de-dados, acid, transactions, postgresql, system-design]
skill: tech-mentor-system-design
status: stable
---

# ACID

Propriedades que garantem confiabilidade em transações de bancos de dados relacionais.

- **Atomicity** — transação toda ocorre ou nada ocorre. Não existe "cobrou mas não criou o pedido".
- **Consistency** — banco nunca fica em estado inválido. Constraints, foreign keys e checks sempre respeitados.
- **Isolation** — transações concorrentes não interferem entre si. Dois usuários comprando o último item — só um vence.
- **Durability** — dado commitado sobrevive a falha de hardware. Gravado no WAL antes de confirmar.

## Atomicidade entre Microsserviços: Por Que o "A" Quebra Primeiro

Numa arquitetura de microsserviços com [[wiki/concepts/database-per-service|banco por serviço]], não existe mais uma transação de banco única cobrindo múltiplos serviços — então a Atomicity do ACID (toda operação deve poder ser revertida) passa a ser responsabilidade explícita da aplicação, não do banco. Se o serviço de pagamento falha depois que o serviço de envio já foi autorizado, o sistema fica num estado logicamente inconsistente (pedido despachado sem pagamento confirmado), mesmo com cada banco individualmente ACID. É esse gap que motiva [[wiki/concepts/two-phase-commit]] (coordenação síncrona) e, para mais serviços, [[wiki/concepts/saga-pattern]] (compensação assíncrona via fila). Ver [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]].

## Relação com Transações

ACID é o **contrato** que o banco oferece. `$transaction` é como o código o invoca. Sem transação explícita, operações dependentes violam Atomicity. → [[concepts/database-transactions]]

## NoSQL e ACID

A maioria dos bancos NoSQL oferece consistência eventual, não ACID completo. Para operações financeiras e inventário crítico, use banco relacional. → [[concepts/relational-vs-nosql]]

O contraponto formal de ACID é [[wiki/concepts/base-basically-available-soft-state-eventual|BASE]] (Basically Available, Soft State, Eventual Consistency) — garantias mais fracas, mas com maior disponibilidade e escalabilidade.

## O Custo de Consistência: Exemplo do E-mail Único

Garantir uma constraint como "e-mail único" (Consistency) não é gratuito: o banco precisa, a cada escrita, ou varrer todos os registros existentes ou consultar um [[wiki/concepts/database-index|índice]] (tipicamente hash) antes de confirmar. Essa é a contrapartida de performance que a consistência forte impõe — e por isso escalar um sistema fortemente consistente para milhões de usuários é mais difícil do que escalar um sistema BASE. Ver [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]].

## Origem Histórica: Por Que o Relacional Existe

ACID não nasceu como especificação abstrata — nasceu como resposta a um problema concreto dos anos 70/80: sistemas em COBOL/Clipper/Assembly manipulavam arquivos ISAM/CSV diretamente, sem SGBD, com o programa acoplado à estrutura física do arquivo e sem qualquer garantia transacional. Edgar F. Codd (IBM, 1970) propôs o modelo relacional com **independência de dados** — o programa declara o que quer, o sistema decide como buscar e garante consistência. ACID é a formalização das garantias que esse modelo passou a oferecer. Ver [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]].

## Termo de Concurso: SGBDR

Provas de concurso brasileiras chamam o banco relacional de **SGBDR** (Sistema Gerenciador de Banco de Dados Relacional) — o "R" distingue de SGBD NoSQL. ACID é citado nesse contexto como propriedade típica do SGBDR, com "atomicidade" formalmente definida como: se ocorrer erro em uma transação, todo o conjunto de ações relacionado é desfeito até o retorno ao estado inicial. Ver [[wiki/sources/sgbd-conceitos-fundamentais-questoes-concurso]].

## Durability na Prática: WAL, Buffer Pool e Recovery

Durability não significa "gravado imediatamente no arquivo final" — significa que o banco tem informação suficiente para reconstruir o estado confirmado depois de uma queda. Na prática: a mudança é gravada primeiro no [[wiki/concepts/write-ahead-log]] (mais barato, sequencial), o banco já responde "commit OK", e só depois a página suja no [[wiki/concepts/buffer-pool]] é persistida no arquivo de dados definitivo, de forma assíncrona. Se o processo cai no meio, o [[wiki/concepts/database-recovery|recovery]] relê o WAL e reaplica o que estava confirmado. Isolation, por sua vez, é ajustável via [[wiki/concepts/isolation-levels]] e sustentado por [[wiki/concepts/mvcc]] — ver [[wiki/sources/como-um-banco-de-dados-funciona-por-dentro]].

## Key Sources

- [[sources/banco-de-dados]]
- [[wiki/sources/como-um-banco-de-dados-funciona-por-dentro]] — mecanismo concreto de Durability (WAL → commit → dirty page → recovery) e de Isolation (MVCC + isolation levels)
- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]] — contraponto com BASE e custo de performance da consistência forte
- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]] — origem histórica do modelo relacional (Codd, 1970) e por que sistemas financeiros/saúde dependem de ACID
- [[wiki/sources/sgbd-conceitos-fundamentais-questoes-concurso]] — definição formal cobrada em prova de concurso, termo SGBDR
- [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]] — por que atomicidade quebra entre microsserviços com banco por serviço, motivando 2PC e Saga Pattern
