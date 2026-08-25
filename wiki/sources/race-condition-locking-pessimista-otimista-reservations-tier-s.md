---
type: source
title: "Race Condition: Locking Pessimista, Controle de Concorrência Otimista e Reservations (System Design para Entrevistas Tier S)"
aliases: ["race condition entrevista tier s", "locking pessimista vs otimista", "reservations redis set nx ex", "cadeira A3 vingadores ultimato"]
date_created: 2026-08-25
date_updated: 2026-08-25
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/race-condition-locking-pessimista-otimista-reservations-tier-s.md
source_url: ""
author: "Pedro Camaforte"
date_published: ""
date_ingested: 2026-08-25
source_count: 0
tags: [system-design, entrevistas, race-condition, toctou, locking, optimistic-concurrency-control, redis, distributed-lock, reservations, backend]
skill: tech-mentor-system-design
status: stable
---

# Race Condition: Locking Pessimista, Controle de Concorrência Otimista e Reservations (System Design para Entrevistas Tier S)

## TL;DR

Sexto vídeo da série de System Design de [[wiki/entities/pedro-camaforte]] para entrevistas Tier S (o primeiro, sobre escalar leituras, já está em [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]]). Usa dois exemplos didáticos — dupla venda da mesma cadeira de cinema e sobrescrita de estoque de e-commerce — para introduzir **race condition** como o padrão check-then-act já documentado em [[wiki/concepts/toctou]], e então percorre três estratégias de resolução em ordem crescente de sofisticação de UX: (1) **locking pessimista** via `SELECT ... FOR UPDATE` — trava a linha, serializa acesso, ideal sob alta contenção quando o custo de um conflito é alto; (2) **controle de concorrência otimista (OCC)** — não trava nada, detecta conflito no `UPDATE` via condição no `WHERE` (contador simples ou coluna `version`), ideal quando conflitos são raros, mas degrada sob alta contenção (retries em cascata); (3) **reservations** — separa o momento do conflito (clique no assento, reserva por TTL) do momento do pagamento, evitando que o usuário só descubra a perda do lugar depois de preencher o cartão. A fonte demonstra as três estratégias com código real rodando 5 conexões simultâneas contra PostgreSQL, resolve o problema de expiração de reserva com `SET NX EX` no Redis em vez de cron job, e cobre o edge case "e se o Redis cair" com fallback de segunda camada via lock pessimista no banco. Fecha com três erros clássicos de entrevista: não perceber o risco de race condition, usar Redis onde um `FOR UPDATE` bastaria, e travar uma linha do banco durante chamadas a APIs externas.

## Key Claims

- **Race condition = TOCTOU**: os dois exemplos da fonte (cadeira dupla-vendida, estoque sobrescrito) são instâncias do mesmo padrão check-then-act já formalizado em [[wiki/concepts/toctou]] — verificar disponibilidade (`check`) e agir sobre ela (`use`) em passos separados, com uma janela de milissegundos onde duas requisições concorrentes veem o mesmo estado "válido" e ambas prosseguem. A fonte não usa o termo TOCTOU, mas descreve o mecanismo idêntico ao exemplo de saque bancário duplicado já presente na wiki. → [[wiki/concepts/toctou]], [[wiki/concepts/race-condition]]
- **Dois padrões de dano cobrem ~90% dos casos**: (a) *falso positivo de disponibilidade* — dois leitores veem "disponível" antes de qualquer um escrever "indisponível" (cadeira de cinema); (b) *escrita perdida por leitura-em-memória desatualizada* — segunda escrita usa um valor lido antes da primeira escrita e sobrescreve o resultado dela (estoque de e-commerce, `20-17` sobrescrito por `20-2`), sem levar em conta o resultado da primeira operação.
- **Locking pessimista (`SELECT ... FOR UPDATE`) serializa acesso à linha**: dentro de uma transação, trava a linha lida até o `COMMIT`/`ROLLBACK`; qualquer outra transação que tente tocar a mesma linha espera em fila. Usar sob alta contenção e quando o custo de um conflito é alto (dano financeiro); tradeoff é o gargalo de fila sob muita concorrência simultânea. *Confiança: alta* — bate exatamente com [skill: tech-mentor-system-design] `performance-profiling-core.md`, que documenta a mesma sintaxe e o mesmo critério de uso ("conflitos frequentes, operação rápida, não pode ter dados stale"). → [[wiki/concepts/distributed-lock]]
- **Controle de concorrência otimista (OCC) detecta conflito no `WHERE` do `UPDATE`**, sem travar nada previamente — condição sobre o valor lido no `SELECT` anterior (contador simples) ou sobre uma coluna `version` incrementada a cada escrita. Se `rowCount = 0`, a escrita foi disputada e perdeu; a aplicação trata isso como falha e pede retry. Usar quando conflitos são raros — sob alta contenção, a maioria das tentativas falha e precisa retry, o que pode ser ineficiente. *Confiança: alta* — mesmo padrão (`version` column, `rowCount = 0` → conflito) documentado em [skill: tech-mentor-system-design] `performance-profiling-core.md` e em [[wiki/concepts/event-sourcing]] (`expectedRevision`).
- **A variante `estoque > 0` no lugar de `version = valor_lido` é uma flexibilização deliberada da regra de negócio**: permite que múltiplos compradores concorrentes com estoque restante > 0 todos consigam comprar, em vez de falhar todo mundo exceto o primeiro que tocou a linha — só falha quando o contador realmente chega a zero.
- **Demonstração empírica com 5 conexões simultâneas contra PostgreSQL**: sem tratamento, as 5 "pessoas" conseguem reservar a mesma cadeira (overbooking reproduzido na prática, não só teorizado); com `FOR UPDATE`, só a primeira consegue e as demais falham na checagem inicial; com OCC + coluna `version`, o Postgres serializa as escritas concorrentes na mesma linha (nunca duas ao mesmo tempo) e só a primeira a rodar o `UPDATE` bate a condição — as demais descobrem que a `version` mudou. Prova que ambas as estratégias funcionam de fato, não só na teoria.
- **Reservations move o momento do conflito de "depois do pagamento preenchido" para "no clique do assento"** — melhor experiência de usuário porque o conflito é resolvido com feedback instantâneo (escolher outro assento) em vez de erro após o usuário já ter preenchido dados de cartão. Preferir essa estratégia quase sempre que o fluxo envolve interação direta do usuário (compra de ingresso, e-commerce com estoque limitado, passagem aérea) — locking pessimista/OCC seguem valendo para conflitos puramente de back-end/automação.
- **Cron job de expiração de reserva tem um bug estrutural de atraso**: se o job roda de N em N minutos e a reserva expira logo depois de uma execução, a reserva efetivamente dura quase 2×N minutos em vez de N — o autor propõe isso explicitamente como algo que passa em entrevista júnior/pleno mas que um entrevistador sênior vai questionar.
- **`SET show:seat NX EX 600` no Redis substitui o cron job**: `NX` garante atomicidade check-and-set (só seta se a chave não existir — sem race condition entre checar e setar), `EX` expira nativamente sem job externo. O banco passa a controlar só "disponível"/"ocupado"; o Redis controla "reservado" via TTL. Mesmo primitivo `SET NX EX` já documentado em [[wiki/concepts/distributed-lock]] (caso Uber: `driver:{id}` como chave), mas aplicado aqui a um caso de uso diferente — reserva temporizada de UX, não exclusão mútua entre workers concorrentes. → [[wiki/concepts/distributed-lock]]
- **Fallback de duas camadas para quando o Redis cai**: lock distribuído via Redis no caminho feliz + locking pessimista (`FOR UPDATE`) no banco como segunda camada de garantia durante a janela em que o Redis está fora do ar (ex.: ~60s para subir uma nova instância). Garante que, mesmo nesse intervalo excepcional, só uma pessoa complete a compra — ao custo de pior UX só nesse período raro. *Nota de calibração:* [skill: tech-mentor-system-design] `performance-profiling-core.md` levanta um risco relacionado mas distinto que a fonte não menciona — clock skew/pausa de processo (GC, swap) pode expirar um lock do Redis antes do processo terminar de usá-lo, mitigado com **fencing tokens**; a fonte só cobre o caso "Redis totalmente indisponível", não o caso "Redis disponível mas o lock expira cedo demais".
- **Três erros que eliminam candidatos em entrevista**: (1) não identificar sozinho que um cenário tem risco de race condition — o entrevistador não vai apontar; (2) usar Redis/lock distribuído para tudo quando um `FOR UPDATE` simples resolveria — complexidade desnecessária também é red flag; (3) abrir transação, travar uma linha, e dentro dela fazer chamadas a APIs externas (ex.: gateway de pagamento) — trava a linha por segundos e forma fila; a ordem correta é fechar a transação com o banco primeiro, conversar com APIs externas depois. → [[wiki/concepts/entrevista-system-design]]

## Entities

[[wiki/entities/pedro-camaforte]]

## Concepts

[[wiki/concepts/race-condition]] · [[wiki/concepts/toctou]] · [[wiki/concepts/distributed-lock]] · [[wiki/concepts/pessimistic-locking]] · [[wiki/concepts/optimistic-concurrency-control]] · [[wiki/concepts/reservation-pattern]] · [[wiki/concepts/mutex]] · [[wiki/concepts/entrevista-system-design]] · [[wiki/concepts/idempotencia]] · [[wiki/concepts/saga-pattern]]

## Conexão com outras fontes

Sexta entrada da série Tier S de [[wiki/entities/pedro-camaforte]], que começou com [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]] (escalar leituras). Diferente daquela fonte (framework diagnóstico sobre banco de dados), esta é focada em concorrência/escrita segura — par natural, não repetição. O mecanismo TOCTOU já documentado a partir de [[wiki/concepts/toctou]] (saque bancário duplicado) ganha aqui dois novos exemplos de domínio (venda de ingresso, estoque de e-commerce) que reforçam a mesma mecânica sem contradizê-la. O primitivo `SET NX EX` do Redis já estava documentado em [[wiki/concepts/distributed-lock]] a partir do caso Uber (matching de motorista) — esta fonte mostra o **mesmo comando** resolvendo um problema estruturalmente diferente (reserva de UX com TTL, não exclusão mútua entre workers), o que é um bom caso para a página de conceito distinguir "mesma ferramenta, usos diferentes". O teaser do próximo vídeo (pagamento já cobrado, uma etapa posterior falha, como desfazer) aponta diretamente para [[wiki/concepts/idempotencia]] e [[wiki/concepts/saga-pattern]] — já presentes na wiki — como o assunto provável da próxima ingestão da série.

## Open Questions

- **Terminologia TOCTOU não usada pela fonte**: o autor nunca usa o termo "TOCTOU", nem cita [[wiki/concepts/toctou]] diretamente — a equivalência foi inferida durante a ingestão por comparação estrutural com o exemplo de saque bancário já documentado. Vale checar em fontes futuras da série se o termo aparece explicitamente.
- **Fencing token não é mencionado pela fonte** apesar de ser o complemento natural da estratégia de reservations com Redis sob falha (clock skew, GC pause) — cross-referenciado aqui via skill como gap explícito, não como erro da fonte (o autor está resolvendo um problema diferente: Redis totalmente fora do ar, não lock expirado cedo demais).
- **Próximo vídeo da série (7º, teaser no final)**: rollback de efeitos colaterais já aplicados (cartão já cobrado) quando uma etapa posterior de um fluxo multi-step falha — candidato natural a fechar o arco com [[wiki/concepts/saga-pattern]] e [[wiki/concepts/idempotencia]] já presentes na wiki.

## Raw Quotes

> "Isso tem o nome, isso se chama race condition: quando muitas pessoas estão tentando fazer a mesma ação ao mesmo tempo e o nosso servidor, o nosso banco de dados, não está preparado para lidar com isso."

> "Nesse meio tempo, nesses milissegundos de diferença, o nosso sistema deu um falso positivo — falou que a cadeira tava livre porque realmente ela tava, só que o nosso usuário um já tinha pagado por ela."

> "O for update vai controlar o nosso lock pessimista: banco, não deixe ninguém modificar essa linha dessa tabela que eu estou mexendo — somente quando eu finalizar tudo que eu preciso fazer e liberar essa linha é que a próxima pessoa vai poder mexer."

> "É muito melhor a gente ter um conflito de reserva de assento do que um conflito no pagamento, concorda?"

> "Nunca jamais abra uma transação com o banco de dados, loque uma linha da tabela, e vá fazer outras operações como chamadas para APIs de pagamento, para APIs externas. [...] Se você pisar nisso, você vai ser eliminado da entrevista na hora."
