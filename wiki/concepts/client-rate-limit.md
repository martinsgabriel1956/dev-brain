---
type: concept
title: "Client Rate Limit"
aliases: ["rate limit no cliente", "rate limit de saída"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [rate-limiting, apis-terceiros, integracao]
skill: tech-mentor-backend
status: draft
---

# Client Rate Limit

Rate limit aplicado **do nosso lado, nas chamadas de saída** a APIs de terceiros, para não ultrapassar uma taxa na API do parceiro nem inundar os próprios logs de erros ([[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]]). Motivo: não conhecemos a capacidade real do parceiro nem podemos validar que ele limita (embora devesse). Exemplos do vídeo: app tipo iFood chamando APIs de restaurantes; venda de ingressos chamando APIs de redes de cinema (ilustrativos).

Encaixa no [[wiki/concepts/leaky-bucket]]: o usuário final gera centenas de solicitações rápido, mas o processamento real sai a taxa menor, via fila. O autor ressalva que é só a ideia de fila, não processamento assíncrono. Combina com [[wiki/concepts/retry-backoff]] ao receber 429 do parceiro e é afim a [[wiki/concepts/back-pressure]]. Ver [[wiki/concepts/rate-limiting]].

## Key Sources

- [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]]
