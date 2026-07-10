---
type: concept
title: "Validação de Assinatura de Webhook"
aliases: ["webhook signature", "stripe-signature", "x-signature", "hmac webhook", "webhook validation"]
date_created: 2026-07-04
date_updated: 2026-07-10
source_count: 2
tags: [webhook, hmac, timing-attack, appsec, api-security]
skill: tech-mentor-security
status: stable
---

# Validação de Assinatura de Webhook

Webhooks costumam viver em rotas previsíveis (`/api/webhook`, `/api/hook`), o que permite que um atacante enumere a rota e mande requisições forjadas fingindo ser o serviço de origem (ex: confirmando um pagamento que nunca aconteceu). A defesa é validar uma assinatura secreta enviada em header a cada chamada.

## Assinatura por provedor

- Stripe: header `Stripe-Signature`
- Mercado Pago: header `X-Signature`
- GitHub: header `X-Hub-Signature-256`

O backend deve calcular o HMAC do payload recebido com o segredo compartilhado e comparar com a assinatura do header. Se a assinatura estiver ausente ou não bater, a requisição deve ser rejeitada.

## Implementação completa (com defesas adicionais)

```typescript
async function validateWebhook(req: Request, secret: string): Promise<boolean> {
  const signature = req.headers['x-hub-signature-256'] as string
  if (!signature) return false

  const body = await getRawBody(req)
  const expected = 'sha256=' + createHmac('sha256', secret).update(body).digest('hex')
  // comparação em tempo constante — evita timing attack revelando a assinatura byte a byte
  if (!timingSafeEqual(Buffer.from(expected), Buffer.from(signature))) return false

  // replay attack prevention — rejeita eventos antigos reenviados
  const age = Date.now() - parseInt(req.headers['x-timestamp'] as string) * 1000
  if (age > 5 * 60 * 1000) return false

  // idempotência — processa cada evento uma única vez
  const eventId = req.headers['x-delivery-id'] as string
  const alreadyProcessed = await redis.set(`webhook:${eventId}`, '1', 'EX', 86400, 'NX')
  if (!alreadyProcessed) return false

  return true
}
```

## Ponto crítico: nunca usar `===` para comparar a assinatura

Comparação de string comum (`===`) retorna assim que encontra o primeiro byte diferente — isso vaza, por diferença de tempo de resposta, onde a assinatura correta diverge, permitindo reconstruí-la byte a byte. Usar sempre `crypto.timingSafeEqual`.

## Como o HMAC é construído por baixo

Esta página trata `createHmac` como caixa-preta — o suficiente para validar webhooks. Para entender por que a construção com chave interna/externa (`ipad`/`opad`) é resistente a ataque de extensão de mensagem, ao contrário de um simples `Hash(secret + payload)`, ver [[wiki/concepts/hmac]].

## Ver também

- [[wiki/concepts/timing-attack]] — por que `===` em segredos é uma vulnerabilidade, não só um detalhe de implementação
- [[wiki/concepts/idempotencia]] — o mesmo endpoint de webhook deve tratar reentrega do provedor sem duplicar efeito
- [[wiki/concepts/hmac]] — mecânica interna do HMAC (ipad/opad, duas etapas de hash) e outro caso de uso: validar payload do próprio servidor em padrão [[wiki/concepts/local-first]]

## Key Sources

- [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]]
- [[wiki/sources/hmac-integridade-mensagem-local-first-entrevista]]
