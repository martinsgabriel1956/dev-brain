---
type: source
title: "CQRS e Event Sourcing Explicado na Prática"
aliases: ["CQRS e Event Sourcing"]
date_created: 2026-08-17
date_updated: 2026-08-17
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/cqrs-e-event-sourcing-explicado-na-pratica.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-08-17
source_count: 0
tags: [cqrs, event-sourcing, arquitetura, cqs, write-ahead-log, impedance-mismatch, ddd, ledger, patrocinio-abacus]
skill: tech-mentor-backend
status: stable
---

# CQRS e Event Sourcing Explicado na Prática

## TL;DR

Vídeo pt-BR (autor não identificado) que ensina CQRS e Event Sourcing juntos, argumentando que embora sejam conceitos teoricamente independentes, quase todo sistema real que implementa CQRS o faz com o objetivo de viabilizar Event Sourcing. Constrói a explicação de baixo para cima: parte de **CQS** (Command Query Separation) em nível de função (`get`/`set`), sobe para **write model/read model** em nível de sistema, mostra o ganho real ao fragmentar o banco em bancos fisicamente diferentes por natureza de carga (colunar para analytics, relacional para queries estruturadas, NoSQL para escrita rápida), introduz o **impedance mismatch** (um JSON de "criar ordem" que vira 4 linhas em 4 tabelas relacionais) como motivação central para persistir eventos em vez de estado, conecta isso ao **write-ahead log** do próprio Postgres, usa a analogia do **ledger bancário** para explicar auditabilidade e imutabilidade de eventos (correção via transação inversa, nunca via UPDATE), e fecha com a tese central: adotar CQRS/Event Sourcing é geralmente uma **decisão de domínio** (necessidade de auditabilidade), não uma decisão técnica — não recomendado para CRUD simples. Inclui bloco patrocinado pela Abacus AI comparando geração de MVP (DeepAgent vs. ChatGPT).

## Claims Principais

| Claim | Confiança |
|---|---|
| CQRS e Event Sourcing são teoricamente conceitos separados, mas na prática de sistemas reais quase todo CQRS existe a serviço de viabilizar Event Sourcing (segundo "dois dos maiores experts no tema" — não nomeados na fala, mas as referências citadas na descrição original são Martin Fowler e Greg Young) | Média — atribuição de autoridade não verificável na transcrição, mas consistente com a literatura padrão do assunto |
| CQS (Command Query Separation) é o conceito-raiz de CQRS em nível de função: `get` nunca muta estado e sempre retorna valor; `set` recebe parâmetros e não retorna nada | Alta |
| O ganho real de CQRS não está só em separar write/read model logicamente, mas em fragmentar fisicamente o banco por natureza de carga — ex.: banco colunar para agregação de views, relacional para queries estruturadas, NoSQL para escrita rápida | Alta |
| Impedance mismatch: um evento de domínio (ex.: "criar ordem") cabe naturalmente em um único objeto/JSON, mas ao persistir em modelo relacional normalizado se fragmenta em múltiplas linhas de múltiplas tabelas — motivação central para preferir persistir o evento em vez do estado derivado | Alta |
| O write-ahead log (WAL) de bancos relacionais tradicionais (ex.: Postgres) já é, internamente, uma forma de Event Sourcing — grava a sequência de ações antes de refletir no estado presente | Alta |
| Auditabilidade é o objetivo central de Event Sourcing: o estado final por si só não revela o histórico de ações que levou até ele (exemplo: não dá pra saber quantas pessoas removeram itens do carrinho olhando só o carrinho atual) | Alta |
| Imutabilidade de eventos é inegociável — correções não apagam/alteram o evento anterior, são feitas por uma transação inversa seguida da transação correta (mesmo padrão contábil) | Alta |
| Adotar CQRS/Event Sourcing deveria ser motivado pelo **domínio** (necessidade de auditabilidade/negócio), não por uma decisão puramente técnica de escalabilidade — mesmo havendo ganhos técnicos legítimos (escalar read/write separadamente, times diferentes por lado) | Alta — reforçada explicitamente como a "tese" de fechamento do vídeo |
| Não recomendado para CRUD simples: aumenta complexidade sem contrapartida quando não há necessidade real de auditoria/replay | Alta |

## Entidades

- [[wiki/entities/abacus-ai]] — bloco patrocinado citando o produto "DeepAgent", comparando geração de MVP com ChatGPT

## Conceitos

- [[wiki/concepts/cqrs]]
- [[wiki/concepts/event-sourcing]]
- [[wiki/concepts/command-bus]]
- [[wiki/concepts/ddd]]

## Open Questions

- Autor/canal do vídeo não identificado na transcrição (sem autorreferência de nome de canal, diferente de outras fontes já ingeridas como [[wiki/sources/cqrs-dicionario-programador-codigo-fonte-tv]]). Não foi criada nem vinculada nenhuma entidade de canal.
- A fonte atribui a tese "CQRS quase sempre existe a serviço de Event Sourcing" a "dois dos maiores experts no tema", citando na descrição original um artigo de Martin Fowler e uma talk de Greg Young — mas não nomeia isso na fala nem dá URL. Tratado como claim de confiança média.

## Contradições com a Wiki Existente

Nenhuma. Esta fonte é consistente com [[wiki/concepts/cqrs]] e [[wiki/concepts/event-sourcing]] (ambos já cobrem a separação write/read, a relação de independência teórica entre CQRS e Event Sourcing, e a analogia bancária de ledger). Contribui incrementalmente com: (1) a derivação de CQRS a partir de **CQS** em nível de função (`get`/`set`), ausente nas fontes já ingeridas; (2) o conceito de **impedance mismatch** como motivação concreta e nomeada para Event Sourcing, com exemplo passo a passo (JSON → 4 tabelas); (3) a conexão explícita entre **write-ahead log** de bancos relacionais tradicionais e Event Sourcing; (4) o argumento de que a fragmentação **física** de bancos por natureza de carga (colunar/relacional/NoSQL) é o "verdadeiro ganho" de CQRS, além da separação lógica write/read.

## Citações Brutas Preservadas

> "Segundo dois dos maiores experts nesse tema, CQRS é apenas uma noção muito simples: existe um modelo diferente para atualizar as informações do que para ler essas informações."

> "O verdadeiro ganho aqui começa a ser quando a gente começa a fragmentar um pouco o nosso banco de dados."

> "Isso daqui é uma decisão de domínio — é uma decisão de eu preciso dar auditabilidade dos meus eventos — e claramente não é uma decisão puramente técnica."

> "Nem o maior defensor do mundo de CQRS/Event Sourcing vai te falar que isso daqui é menos complexo do que um CRUD simples — é mais complexo."

## Key Sources (páginas que citam esta fonte)

- [[wiki/concepts/cqrs]]
- [[wiki/concepts/event-sourcing]]
- [[wiki/entities/abacus-ai]]
