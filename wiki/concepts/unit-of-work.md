---
type: concept
title: "Unit of Work"
aliases: ["unidade de trabalho", "unit of work pattern", "padrão unit of work"]
date_created: 2026-08-19
date_updated: 2026-08-19
source_count: 1
tags: [design-patterns, unit-of-work, transacoes, repository-pattern, sqlalchemy, rollback]
skill: tech-mentor-backend
status: draft
---

# Unit of Work

Padrão de *Patterns of Enterprise Application Architecture* ([[wiki/entities/martin-fowler]], PoEAA) que **reúne múltiplas operações (criações, atualizações, remoções) num ponto de coleta e as aplica todas de uma vez** através de um `commit`, em vez de disparar cada mudança individualmente contra o armazenamento.

## Mecanismo

Uma classe/objeto Unit of Work mantém internamente listas do que precisa acontecer — ex: `new`, `dirty` (sujo, precisa atualizar), `removed` — registradas conforme o código de negócio vai chamando métodos de rastreamento (`register_new`, `register_dirty`, `register_removed`). Nada acontece de fato no armazenamento até o método `commit()` ser chamado, que então executa inserções, atualizações e remoções em sequência. Como confirmar é um passo separado e explícito, é natural estender esse ponto único com um mecanismo de **rollback**: se qualquer operação falhar, as demais já aplicadas na mesma unidade podem ser desfeitas.

## Por que agrupar operações

- **Tráfego de rede** — várias mudanças viram uma única viagem de ida e volta ao banco, em vez de uma por operação.
- **Consistência sob falha** — se uma operação no meio do lote falhar, as anteriores podem ser revertidas, evitando estado parcialmente aplicado. Especialmente relevante em domínios sensíveis (finanças) onde dados fortemente relacionados não podem ficar inconsistentes entre si.
- **Legibilidade/depuração** — agrupar operações torna explícito o que uma transação inclui, facilitando raciocinar sobre o que uma unidade de trabalho faz como um todo.

## Unit of Work vs. Repository

Os dois padrões são frequentemente usados juntos, mas resolvem problemas diferentes:

- **[[wiki/concepts/repository-pattern]]** — camada de abstração sobre o armazenamento; o código interage com objetos/entidades em vez de queries cruas.
- **Unit of Work** — coordena *quando* e *como* as operações acumuladas via repositórios são efetivamente aplicadas e confirmadas (ou revertidas) como um lote atômico.

[[wiki/sources/unit-of-work-padrao-de-design]] usa SQLAlchemy como exemplo de biblioteca que fornece os dois ao mesmo tempo: as classes ORM (mapeadas via `declarative_base`) implementam o Repository, e o objeto `Session` implementa o Unit of Work — acumula `add`/updates in-place, e só escreve no banco em `session.commit()` (ou parcialmente, em `session.flush()`). Um `except` dentro do gerenciador de contexto da sessão chama `session.rollback()`, desfazendo tudo que havia sido acumulado desde o commit anterior. [[wiki/concepts/repository-pattern]] já registrava esse par (Fowler, PoEAA) como resposta a uma limitação de repositórios simples: sem transação, conflitos de concorrência (duas edições simultâneas do mesmo registro) não são tratados — Unit of Work resolve coordenando as escritas até o fim da requisição.

## `flush` vs. `commit`: estado intermediário

SQLAlchemy expõe um estado entre "nada aconteceu" e "tudo confirmado": `session.flush()` aplica as operações pendentes no banco (por exemplo, atribui o ID gerado a um registro recém-criado, tornando-o referenciável para um update seguinte) sem finalizar a transação — o `commit()` continua sendo o ponto que de fato encerra a unidade de trabalho e a torna permanente e visível para outras sessões.

## Semelhança com Command Pattern

[[wiki/concepts/command-pattern]] também encapsula uma operação como objeto antes de executá-la. A diferença de propósito: Command foca em parametrizar/enfileirar/desfazer *uma* ação individual; Unit of Work foca em agrupar *várias* operações heterogêneas (inserções, updates, deleções) num commit atômico único.

## Além de bancos de dados

O mecanismo generaliza para qualquer domínio onde uma operação complexa, multi-etapas, precisa permanecer consistente mesmo se falhar no meio:

- **Sincronização de arquivos** (ex: Dropbox) — reverter um upload parcial se a rede cair, para não deixar um arquivo corrompido no armazenamento em nuvem.
- **Jogos** — reverter um save de estado complexo se uma parte da gravação falhar.
- **Infraestrutura como código** — reverter/desprovisionar recursos de nuvem já criados (banco, servidores, storage) se um passo do provisionamento falhar, para não pagar por recursos órfãos.

Nenhum desses três exemplos tem demonstração de código na fonte — são citados como analogia conceitual da mesma ideia central (acumular, depois confirmar ou reverter tudo como uma unidade).

## Key Sources

- [[wiki/sources/unit-of-work-padrao-de-design]] — implementação artesanal em Python + exemplo real com SQLAlchemy (Session como Unit of Work), incluindo demonstração de rollback ao vivo e distinção flush vs. commit
