---
type: concept
title: "Idempotência"
aliases: ["idempotência", "idempotency", "idempotency key"]
date_created: 2026-04-22
date_updated: 2026-09-02
source_count: 8
tags: [distribuidos, resiliencia, api, retry, mensageria, double-spend, double-submit, webhook, fintech]
skill: tech-mentor-system-design
status: stable
---

# Idempotência

Propriedade de uma operação que produz o mesmo resultado independente do número de vezes que é executada. Pré-requisito para [[concepts/retry-backoff]] seguro.

## O Problema sem Idempotência

```typescript
// ❌ Retry cria cobrança duplicada
async function chargeCard(orderId: string, amountCents: number) {
  return stripe.charges.create({ amount: amountCents, currency: "brl" });
}
// 3 retries = 3 cobranças
```

## A Solução: Idempotency Key

```typescript
// ✅ Stripe processa exatamente uma vez — retries são seguros
async function chargeCard(orderId: string, amountCents: number) {
  return stripe.charges.create(
    { amount: amountCents, currency: "brl" },
    { idempotencyKey: `order-${orderId}` }
  );
}
```

## Como Implementar em APIs Próprias

```typescript
// Cliente envia Idempotency-Key no header
// Servidor armazena resultado por key (ex: Redis com TTL de 24h)
// Segunda request com mesma key retorna resultado cacheado sem re-executar

async function processPayment(idempotencyKey: string, data: PaymentData) {
  const cached = await redis.get(`idem:${idempotencyKey}`);
  if (cached) return JSON.parse(cached);

  const result = await executePayment(data);
  await redis.set(`idem:${idempotencyKey}`, JSON.stringify(result), "EX", 86400);
  return result;
}
```

## Operações Naturalmente Idempotentes

- GET, HEAD, OPTIONS (HTTP)
- DELETE (o recurso ou já não existe)
- UPDATE com valor absoluto (`SET balance = 100` vs `SET balance = balance - 10`)

## Operações que Precisam de Idempotency Key

- POST que cria recursos ou processa pagamentos
- Qualquer operação com efeito colateral financeiro

## Double Spend / Double Submit — a Chave Gerada pelo Servidor

Double spend (transações) e double submit (formulários) são o mesmo problema por ângulos diferentes: um request se duplica por bug, duplo clique acidental ou abuso deliberado.

Variante importante do padrão: em vez do **cliente** gerar e enviar a Idempotency Key (vulnerável — um atacante reenvia o request com uma chave diferente e burla a dedução), o **servidor** pode gerar a chave como um **hash dos campos submetidos** (ex.: origem, destino, data do voo). Isso torna a dedução robusta contra reenvio malicioso, não só contra duplo clique acidental.

A definição de quais campos entram no hash — e qual a janela de tempo que caracteriza duplicidade (a mesma compra hoje vs. amanhã pode ser legítima) — é uma **decisão de negócio**, não só técnica.

Camadas complementares, cada uma cobrindo um ângulo diferente do problema:

| Camada | Cobre duplo clique acidental? | Cobre abuso deliberado? |
|---|---|---|
| Desabilitar botão de submit no frontend | Sim | Não — atacante ignora o frontend |
| Redirect após POST (padrão [[wiki/concepts/post-redirect-get]]) | Sim | Não |
| Idempotency Key (hash gerado no servidor + storage compartilhado) | Sim | Sim |
| Unique Constraint no banco (quando existe campo genuinamente único) | Sim | Sim — mas só se há campo único aplicável |

## Por que o Timeout Sozinho Não Basta

Um timeout só diz que o cliente não recebeu resposta a tempo — não diz se a operação falhou antes de chegar ao servidor, está em andamento, ou foi concluída e apenas a resposta se perdeu. O cliente não consegue diferenciar esses três casos olhando só para o relógio, e é exatamente por isso que ele retenta. A idempotência não existe para evitar o retry — existe para tornar o retry seguro diante dessa ambiguidade.

## Resolvendo a Corrida: `INSERT` Atômico, Não `SELECT` + `INSERT`

Comparar e depois inserir em duas etapas soltas deixa uma brecha: duas tentativas concorrentes podem consultar ao mesmo tempo, descobrir que a chave ainda não existe, e as duas começarem a processar. A chave primária (ou uma unique constraint) resolve isso deixando o **banco** decidir a vencedora de forma atômica:

```sql
-- Corrida resolvida pelo banco, não pela aplicação
INSERT INTO idempotency_keys (key, request_hash, status)
VALUES ($1, $2, 'processing')
ON CONFLICT (key) DO NOTHING
RETURNING key;
-- linha retornada → esta requisição ganhou o direito de processar
-- nenhuma linha retornada → outra tentativa já registrou a intenção; consultar o estado existente
```

Isso responde a pergunta que ficava em aberto em [[wiki/sources/double-spend-double-submit]] sobre qual mecanismo evita que dois requests concorrentes com a mesma chave processem simultaneamente antes do primeiro terminar.

## Idempotência ≠ Transação — Dois Problemas Complementares

[[wiki/concepts/distributed-transactions]] e idempotência resolvem problemas diferentes e não são substituíveis uma pela outra:

| Proteção | O que evita |
|---|---|
| Transação | A operação ficar **pela metade** (débito sem crédito, status inconsistente) |
| Idempotência | A operação **inteira** acontecer duas vezes |

Quando o efeito financeiro mora no mesmo banco, o lançamento contábil (ver [[wiki/concepts/ledger-dupla-entrada]]) e a mudança do status da chave para `completed` devem confirmar na **mesma transação** — o banco nunca deve permitir uma chave concluída sem lançamento correspondente, nem um lançamento confirmado com a chave ainda aberta.

## Cruzando Fronteiras de Serviço

A janela mais difícil de proteger é quando a operação atravessa mais de um sistema e o processo cai no meio: o processador de pagamento externo pode ter aprovado a cobrança, mas o backend caiu antes de salvar a resposta local. Um registro `processing` isolado não prova, por si só, se o efeito externo já aconteceu.

A solução é fazer a mesma identidade atravessar a fronteira: repassar a chave idempotente ao serviço seguinte (se ele aceitar esse contrato), ou manter uma referência estável para consultar e reconciliar o resultado antes de tentar criar outro efeito. Isso é o mesmo par de padrões usado para publicar e consumir eventos com segurança:

- [[wiki/concepts/outbox-pattern]] no lado de quem publica o trabalho nascido numa transação local.
- [[wiki/concepts/inbox-pattern]] no lado de quem consome — inclusive **webhooks**, onde o provedor pode reentregar o mesmo evento porque a confirmação de recebimento se perdeu, mesmo que o evento já tenha sido processado.

Cada fronteira de serviço precisa manter a identidade da operação mesmo com entrega **at-least-once** (pelo menos uma vez) — o objetivo é produzir um efeito financeiro único, não impedir a reentrega em si.

## Identidades de Negócio por Produto

A mesma arquitetura de chave de idempotência se repete em diferentes produtos financeiros, cada um escolhendo sua própria identidade de negócio em vez de um UUID genérico:

| Produto | Identidade | Papel |
|---|---|---|
| Carteira digital | Saque ID | Impede que o mesmo pedido de saque debite o saldo duas vezes |
| Emissão de boleto | Emissão ID | Devolve o título já criado em vez de gerar outro documento para o mesmo faturamento |
| Empréstimo | Crédito ID | Liga o contrato ao único crédito que deve entrar na conta |
| Corretora | Client order ID | Recupera a ordem que já chegou à mesa de execução |

Cancelar ou substituir uma ordem numa corretora cria uma **nova** intenção com outra identidade — não reaproveita a chave da ordem original.

## Retenção da Chave (TTL)

O tempo de retenção depende do produto: apagar cedo demais deixa um retry tardio repetir o efeito; guardar para sempre aumenta custo e complica a operação. A janela precisa cobrir o tempo real de retry e processamento, além de incluir webhooks e a conciliação daquele fluxo — não só a chamada síncrona original.

## Testando a Garantia

Desabilitar o botão após o clique melhora a UX, mas não protege o backend — duas abas abertas, retry automático da biblioteca HTTP, e um worker que reinicia depois de já ter concluído o efeito continuam possíveis. A garantia precisa morar perto da regra de negócio e do armazenamento que registra o efeito, não na UI.

O teste mais revelador corta a resposta **depois** que o efeito acontece e **antes** que o cliente receba a confirmação — reproduzindo a mesma janela de incerteza que motiva o retry. Complementares: disparar duas requisições simultâneas com a mesma chave, duplicar a entrega de um webhook, e reiniciar um worker no ponto mais crítico. Em produção, a taxa de chaves repetidas e de conflitos de payload mostra se o cliente usa o contrato corretamente; operações presas em `processing` mostram onde o fluxo não fechou o resultado.

## `SET ... EX ... GET` do Redis: Check-and-Set Atômico numa Única Chamada

Variante prática do padrão de chave em Redis, além do já registrado `SET NX EX` (usado para [[wiki/concepts/distributed-locking|locks]]): o comando `SET` aceita a flag `GET`, que faz o Redis retornar o valor **anterior** da chave no mesmo momento em que grava o novo valor e o TTL — dispensando uma chamada de leitura separada antes do `SET` e a janela de corrida que duas operações distintas (`GET` depois `SET`) abririam.

```javascript
// sent recebe o valor ANTERIOR da chave (ou null se não existia) — e já regrava, atomicamente
const sent = await redis.set(idempotencyKey, "1", "EX", 60, "GET");
if (!sent) {
  // chave não existia: primeira vez dentro da janela — processar
} else {
  // chave já existia: repetição dentro do TTL — ignorar
}
```

Diferença de propósito frente ao `SET NX EX`: `NX` recusa a escrita se a chave já existe (útil para lock, onde só um vencedor deve prosseguir); `GET` sempre escreve, mas devolve o estado anterior para a aplicação decidir — adequado a deduplicação onde não há necessidade de impedir a escrita, só de saber se já tinha acontecido antes.

## Caso Real: Notificações WhatsApp/SMS — Chave Composta + Janela de Minutos, Não Segundos

Fonte concreta de aplicação do padrão fora do domínio financeiro: um SaaS que envia mensagens via bot de WhatsApp não-oficial (instável, sem confirmação de entrega confiável) usa idempotência para não duplicar notificações quando um timeout no envio motiva um retry. A chave combina três características do próprio negócio, não um ID técnico: telefone do destinatário + tipo da mensagem + hash do conteúdo. A janela de deduplicação usada em produção é de **5 minutos** — mais longa que o típico timeout de rede, o suficiente para cobrir o "não sei se o WhatsApp recebeu" sem impedir o reenvio legítimo de uma mensagem realmente diferente pouco tempo depois.

O mesmo mecanismo (chave + TTL) também controla **volume de notificações por usuário** (ex.: limitar quantos SMS um mesmo destinatário recebe) — uso adjacente a idempotência estrita, mais próximo de rate limiting por destinatário do que de deduplicação de uma operação idêntica, mas implementado com a mesma primitiva.

## Riff de folclore: os "dois problemas difíceis" de sistemas distribuídos

Um riff citado em [[wiki/sources/two-hard-things-martin-fowler]] (autoria de Mathias Verraes) substitui os dois problemas clássicos de Phil Karlton — [[wiki/concepts/naming|naming]] e [[wiki/concepts/tradeoff-de-cache|cache invalidation]] — por "guaranteed order of messages" e "exactly-once delivery" em sistemas distribuídos. É piada, não claim técnico, mas a substituição funciona porque aponta certo: entrega exactly-once é precisamente o problema que idempotência resolve (via [[concepts/retry-backoff|retry]] seguro). Ver [[wiki/concepts/two-hard-things]].

## Key Sources

- [[wiki/sources/two-hard-things-martin-fowler]] — riff de folclore que cita "exactly-once delivery" como um dos dois problemas difíceis de sistemas distribuídos
- [[sources/retry-backoff]]
- [[wiki/sources/acoplamento-abstracao-estado]]
- [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] — idempotência como resposta ao webhook duplicado; errar at-least-once vs. exactly-once cobra o cliente em dobro ou perde o pedido
- [[wiki/sources/double-spend-double-submit]] — double spend/double submit como o mesmo problema; chave de idempotência gerada no servidor via hash dos campos (mais robusta que chave enviada pelo cliente); janela de tempo de duplicidade como decisão de negócio
- [[wiki/sources/kiss-yagni-entrega-rapida-qualidade]] — exemplo de [[wiki/concepts/kiss]] aplicado a uma checagem de status habilitados para reprocessamento (adjacente ao padrão de Idempotency Key, não idêntico)
- [[wiki/sources/idempotencia-pagamentos-retry-sistemas-distribuidos]] — por que o timeout sozinho não decide a causa; corrida resolvida por `INSERT` atômico em vez de `SELECT`+`INSERT`; idempotência vs. transação como proteções complementares; identidade cruzando fronteira de serviço via Outbox/Inbox; identidades de negócio por produto; TTL e testes de garantia
- [[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]] — teaser no fechamento do vídeo (ainda não desenvolvido como fonte própria): quando uma etapa posterior de um fluxo multi-step falha depois que o cartão já foi cobrado, como desfazer o efeito colateral já aplicado — aponta para o par idempotência/[[wiki/concepts/saga-pattern]]
- [[wiki/sources/idempotencia-redis-controle-mensagens-whatsapp-tulio-faria]] — caso real de notificações (WhatsApp/SMS): chave composta por telefone + tipo + hash da mensagem; janela de 5 minutos como decisão de produto; `redis.set(key, val, "EX", ttl, "GET")` como check-and-set atômico; mesmo mecanismo usado para limitar volume de SMS por usuário
