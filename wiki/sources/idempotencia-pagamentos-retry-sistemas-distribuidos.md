---
type: source
title: "Idempotência em Pagamentos: Retry, Sistemas Distribuídos e Chaves de Idempotência"
aliases: ["idempotency key pagamentos", "chave de idempotência", "inbox pattern webhook", "client order id"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 0
tags: [idempotencia, pagamentos, retry, sistemas-distribuidos, webhook, outbox, inbox, fintech]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/idempotencia-pagamentos-retry-sistemas-distribuidos.md
source_url:
author:
date_published:
date_ingested: 2026-07-27
---

# Idempotência em Pagamentos: Retry, Sistemas Distribuídos e Chaves de Idempotência

## TL;DR

Um timeout não diz se a cobrança falhou, está em andamento, ou foi aprovada e só a resposta se perdeu — por isso o cliente tem que reter e reenviar retries com a mesma identidade de intenção. A chave de idempotência nasce no cliente antes da primeira tentativa, cobre uma intenção (não um conteúdo — duas transferências iguais e intencionais precisam de duas chaves), e o servidor decide o vencedor da corrida entre tentativas concorrentes via `INSERT` atômico (chave primária/unique constraint), não via `SELECT` seguido de `INSERT`. Idempotência e transação resolvem problemas diferentes e complementares: transação evita efeito pela metade, idempotência evita o efeito inteiro duplicado. A mesma identidade precisa atravessar fronteiras de serviço (Outbox no lado de quem publica, Inbox no lado de quem consome) porque webhooks e filas entregam pelo menos uma vez (at-least-once). Produtos financeiros reaproveitam a arquitetura com identidades de negócio próprias — saque ID, emissão ID, crédito ID, client order ID.

## Key Claims

| Claim | Evidência |
|---|---|
| Um timeout de cliente não distingue falha antes do servidor, processamento em andamento, ou sucesso com resposta perdida | O app não consegue diferenciar os três casos olhando só para o relógio — por isso ele tenta de novo, o que motiva a necessidade de idempotência, não a evita |
| A chave de idempotência deve ser criada pelo cliente antes da primeira tentativa e reenviada idêntica em todo o bloco de retry | Se o código gerasse uma chave nova em cada tentativa, o servidor veria três operações diferentes em vez de uma |
| A chave identifica a intenção, não o conteúdo — duas transferências iguais e intencionais (mesmo valor, mesmo destinatário) precisam de chaves diferentes | Deduplicar só pelo conteúdo apagaria uma operação legítima; uma pessoa pode querer transferir R$ 100 duas vezes para a mesma conta |
| Comparar e depois inserir em duas etapas soltas (`SELECT` então `INSERT`) não fecha a corrida entre tentativas concorrentes | Duas requisições podem consultar ao mesmo tempo, achar que a chave não existe, e as duas começarem a processar — só um `INSERT` atômico contra chave primária/unique constraint decide um vencedor |
| Idempotência e transação são proteções complementares, não substituíveis uma pela outra | Transação impede que a transferência fique pela metade; idempotência impede que a transferência inteira aconteça duas vezes — produtos financeiros geralmente precisam das duas no mesmo fluxo |
| Quando o efeito financeiro mora no mesmo banco, o lançamento e a mudança de status da chave para concluído devem confirmar na mesma transação | Evita banco deixar uma chave concluída sem lançamento correspondente, ou um lançamento confirmado com a chave ainda aberta |
| Webhooks exigem idempotência do lado do consumidor via inbox persistente, porque a confirmação de recebimento pode se perder mesmo após o evento já ter sido processado | Provedor vê a chamada como pendente e reentrega; inbox guarda `provedor + event ID`, aplica o efeito só na primeira entrega e responde sucesso nas seguintes sem duplicar |
| Quando a operação cruza mais de um sistema e o processo cai no meio, o registro local sozinho (ex.: status `processing`) não prova se o efeito externo já aconteceu | Backend precisa repassar a mesma chave idempotente ao serviço seguinte, ou manter uma referência estável para consultar/reconciliar o resultado antes de tentar de novo |
| Cada produto financeiro reaproveita a mesma arquitetura com uma identidade de negócio própria | Saque ID (carteira digital), emissão ID (boleto), crédito ID (empréstimo), client order ID (corretora) — cancelar/substituir uma ordem cria uma nova intenção com outra identidade |
| Desabilitar o botão após o clique melhora a UX mas não protege o backend | Duas abas abertas, retry automático da biblioteca HTTP, e worker que reinicia após já ter concluído o efeito continuam possíveis — a garantia precisa morar perto da regra de negócio e do armazenamento, não na UI |
| O teste mais revelador corta a resposta depois que o efeito acontece e antes que o cliente receba a confirmação | Reproduz exatamente a janela de incerteza que motiva o retry em primeiro lugar; complementar: duas requisições simultâneas, webhook duplicado, worker reiniciando no ponto crítico |

## Conceitos

- [[wiki/concepts/idempotencia]] — página já existente, atualizada com: resolução do request race (INSERT atômico vence sobre SELECT+INSERT), distinção idempotência vs. transação, identidade cruzando fronteira de serviço, identidades de negócio por produto, TTL e observabilidade
- [[wiki/concepts/retry-backoff]] — o timeout como motivador do retry, e por que o app não pode diferenciar as três causas do timeout só pelo relógio
- [[wiki/concepts/inbox-pattern]] — novo stub criado a partir desta fonte, complementar ao Outbox no lado do consumidor de webhook/evento
- [[wiki/concepts/outbox-pattern]] — cruzamento de fronteira de serviço com identidade idempotente propagada
- [[wiki/concepts/distributed-transactions]] — a distinção explícita entre o que a transação resolve e o que a idempotência resolve
- [[wiki/concepts/ledger-dupla-entrada]] — lançamento e mudança de status da chave confirmando na mesma transação local

## Entidades Mencionadas

Nenhuma entidade nomeada relevante — a fonte menciona uma aula gratuita associada ao vídeo, mas sem nome de empresa ou produto que justifique página de entidade.

## Open Questions

- A fonte não detalha o schema exato da tabela de chave de idempotência (nomes de coluna, índices) além de citar chave, request hash, status e resposta salva — comparar com o schema mais explícito já registrado em [[wiki/sources/idempotencia]] (Redis com TTL, `payment-${orderId}`) e com o middleware completo da referência da skill (`tech-mentor-backend/references/idempotency-patterns.md`), que já cobre lock via `SET NX` separado do cache key.
- Não fica claro qual mecanismo garante que o serviço seguinte (ex.: processador de pagamento externo) de fato aceite e honre a chave idempotente repassada pelo backend — a fonte assume que "sempre que o serviço aceita uma chave idempotente" o problema está resolvido, mas não cobre o caso (mencionado só como alternativa) de reconciliar contra uma referência estável quando o serviço externo não suporta idempotência nativa.

## Key Sources

_Este é o documento primário._
