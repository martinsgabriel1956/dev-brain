---
type: source
title: "Unit of Work — Padrão de Design"
aliases: ["unit of work pattern", "unidade de trabalho", "arjancodes unit of work"]
date_created: 2026-08-19
date_updated: 2026-08-19
source_file: "raw/unit-of-work-padrao-de-design.md"
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-08-19
source_count: 0
tags: [unit-of-work, design-patterns, sqlalchemy, repository-pattern, transacoes, rollback, python]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Unit of Work é um padrão que funciona como ponto de coleta de múltiplas operações (criar, atualizar, remover) para aplicá-las todas de uma vez num `commit`, em vez de disparar cada mudança individualmente contra o banco. Isso economiza tráfego de rede e, principalmente, permite reverter (`rollback`) todas as operações acumuladas se qualquer uma delas falhar — crítico em domínios sensíveis como finanças, onde dados fortemente conectados precisam permanecer consistentes. A fonte demonstra primeiro uma implementação artesanal em Python (classe `UnitOfWork` com listas de novos/sujos/removidos e um método `commit`), depois um exemplo real com SQLAlchemy, onde a `Session` acumula operações (`add`, updates in-place) sem tocar o banco até `session.commit()`, e `session.rollback()` desfaz tudo se uma exceção ocorrer dentro do gerenciador de contexto. O padrão normalmente não é implementado do zero — vem embutido em ORMs como SQLAlchemy, combinado com o [[wiki/concepts/repository-pattern]] (SQLAlchemy fornece os dois ao mesmo tempo: a camada ORM age como Repository, a `Session` age como Unit of Work).

## Key Claims

**Claim:** Unit of Work é um ponto de coleta para múltiplas operações que são aplicadas todas de uma vez, e não uma abstração de acesso a dados em si.
**Evidence:** A classe `UnitOfWork` do exemplo básico mantém listas internas (`new_users`, `dirty_users`, `removed_users`) e só executa qualquer ação real dentro do método `commit()` — antes disso, nenhuma mudança acontece de fato. Comparado explicitamente ao [[wiki/concepts/command-pattern]]: ambos encapsulam operações como objetos/entradas antes da execução.
**Confidence:** alta — demonstrado com implementação de código completa e execução ao vivo.

**Claim:** O principal ganho de agrupar operações num commit único (além de tráfego de rede) é viabilizar um mecanismo de rollback coerente quando uma das operações falha.
**Evidence:** No exemplo SQLAlchemy, dentro do gerenciador de contexto da sessão, uma exceção levantada no meio das operações (`ValueError` explícito, ou um `id` de usuário inexistente) reverte todas as criações/atualizações feitas até aquele ponto — a lista final de usuários volta a ficar vazia. Quando a mesma sequência de operações é dividida em sessões separadas, apenas a unidade de trabalho que efetivamente falhou é revertida — as sessões anteriores, já commitadas, permanecem.
**Confidence:** alta — demonstrado com dois cenários (mesma sessão vs. sessões separadas) e outputs antes/depois.

**Claim:** `session.flush()` aplica operações pendentes no banco (torna o ID gerado disponível, por exemplo) sem finalizar a transação — a diferença entre "aplicado" e "commitado" é explícita no SQLAlchemy.
**Evidence:** Um usuário recém-criado tem `id=None` até `session.flush()` ser chamado; depois do flush, o ID é atribuído, permitindo referenciar o registro (ex: para um update) mesmo antes do `commit()` final. Isso ilustra que Unit of Work não é binário (nada aconteceu / tudo commitado) — há um estado intermediário de "escrito mas não confirmado".
**Confidence:** alta — demonstrado com print do objeto antes e depois do flush.

**Claim:** SQLAlchemy é um exemplo de biblioteca que combina Repository Pattern com Unit of Work na mesma ferramenta.
**Evidence:** As classes ORM (`User`, `UserDetail`, `UserPreference`) fornecem a abstração de acesso a dados (Repository) — o código interage com objetos, não com SQL bruto. A `Session` fornece o agrupamento/commit/rollback de operações (Unit of Work). A fonte generaliza: normalmente você não implementa nenhum dos dois do zero, mas é útil entender o mecanismo por trás.
**Confidence:** alta, mas apresentada como afirmação do autor sem contraponto — vale checar contra documentação oficial do SQLAlchemy se for citar formalmente.

**Claim:** Unit of Work é útil fora de bancos de dados, em qualquer domínio onde uma operação complexa e multi-etapas precisa permanecer consistente mesmo se falhar no meio.
**Evidence:** Três exemplos dados: (1) sincronização de arquivos (ex: Dropbox) — reverter upload parcial de um arquivo grande se a rede cair, evitando armazenar um arquivo corrompido; (2) jogos — reverter um save complexo de estado de jogo se uma parte falhar ao salvar; (3) infraestrutura como código — reverter o provisionamento de recursos de nuvem já criados (banco, servidores, storage) se um passo do provisionamento falhar, evitando pagar por recursos órfãos.
**Confidence:** média — exemplos dados como analogia conceitual, sem demonstração de código para nenhum dos três.

## Entities & Concepts Touched

- [[wiki/concepts/unit-of-work]]
- [[wiki/concepts/repository-pattern]]
- [[wiki/concepts/command-pattern]]
- [[wiki/concepts/database-transactions]]
- [[wiki/concepts/design-patterns]]
- [[wiki/entities/martin-fowler]] — origem do padrão em *PoEAA*, citada indiretamente via [[wiki/concepts/repository-pattern]]

## Open Questions

- **Autor/canal não identificado por nome na transcrição** — única pista é a menção a "arjancodes.com" e a um "workshop gratuito de diagnóstico de código", ambos característicos do canal técnico de Python ArjanCodes, mas não confirmado por citação explícita de nome; nenhuma entidade de autoria foi criada para não forçar uma atribuição não verificada.
- **Mecanismo de rollback do exemplo básico (sem SQLAlchemy) fica apenas esboçado** — a fonte menciona que o método `commit` poderia ser estendido com lógica de reversão em caso de exceção, mas não implementa isso no exemplo artesanal (só no exemplo real com SQLAlchemy, via `session.rollback()`).
- **Nenhum dos três exemplos de domínio fora de banco de dados (sync de arquivos, jogos, IaC) tem implementação de código** — candidatos a fonte dedicada futura se algum aparecer com exemplo prático (ex: Terraform apply/rollback, ou state machine de save de jogo).
