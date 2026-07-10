---
type: concept
title: "HMAC (Hash-based Message Authentication Code)"
aliases: ["hmac", "hash-based message authentication code", "rfc 2104", "ipad", "opad"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_count: 1
tags: [hmac, criptografia, hashing, appsec, integridade, rfc-2104]
skill: tech-mentor-security
status: draft
---

# HMAC (Hash-based Message Authentication Code)

**Mecanismo que garante integridade e autenticidade de uma mensagem usando uma chave simétrica compartilhada**, sem os custos computacionais de uma assinatura assimétrica. Padronizado na RFC 2104.

## Por que não basta `Hash(secret + mensagem)`

A ideia ingênua de concatenar um segredo com a mensagem e aplicar uma função de hash (`Hash(secret || mensagem)`) parece resolver o problema, mas é vulnerável a **ataque de extensão de mensagem**: como o segredo fica no início da concatenação e a maioria das funções de hash processa a entrada por blocos, é possível — com tempo e poder computacional suficientes — explorar o estado interno do algoritmo para anexar dados à mensagem original e produzir um novo hash válido, sem nunca conhecer o segredo. Concatenar o segredo na frente da mensagem não gera entropia suficiente para tornar isso inviável.

## A construção HMAC

Em vez de concatenar a chave direto com a mensagem, o HMAC **deriva duas chaves diferentes** a partir da mesma chave secreta, usando XOR com dois padrões de byte fixos:

- **ipad** (inner pad): byte `0x36`, repetido até o tamanho de bloco do algoritmo de hash.
- **opad** (outer pad): byte `0x5C`, repetido até o mesmo tamanho de bloco.

Esses dois valores foram escolhidos pelos autores da RFC por serem os mais distantes entre si em bits — minimizam correlação entre a chave interna e a chave externa resultantes.

### Normalização da chave

Antes do XOR, a chave é ajustada para o tamanho de bloco do algoritmo (64 bytes para MD5/SHA-1/SHA-256):

- Chave **menor** que o bloco → completada com padding de zeros.
- Chave **maior** que o bloco → reduzida aplicando o próprio hash sobre ela.

### As duas etapas de hash

```
chave_interna = chave_normalizada XOR ipad (0x36...)
chave_externa = chave_normalizada XOR opad (0x5C...)

hash_1     = Hash(chave_interna || mensagem)
HMAC       = Hash(chave_externa || hash_1)
```

A etapa 1 é equivalente à abordagem ingênua (`Hash(secret + msg)`), mas usando a chave já derivada/com padding. A etapa 2 é o que muda tudo: em vez de concatenar a chave diretamente com a *mensagem original*, ela concatena a chave externa com o **hash resultante da etapa 1**. Isso quebra o ataque de extensão de mensagem — o atacante não manipula mais texto em claro, mas um digest intermediário já protegido por uma segunda chave derivada.

```typescript
import { createHmac, timingSafeEqual } from 'crypto'

const tag = createHmac('sha256', secret).update(message).digest('hex')
// Verificação sempre em tempo constante — nunca usar === (ver timing-attack)
timingSafeEqual(Buffer.from(tag), Buffer.from(received))
```

Bibliotecas modernas (Node `crypto`, Python `hmac`) já implementam essa construção internamente — o desenvolvedor não precisa calcular `ipad`/`opad` manualmente, só entender por que o algoritmo é seguro.

## HMAC vs. hash simples vs. assinatura assimétrica

| | Hash(secret+msg) ingênuo | HMAC | Assinatura assimétrica (RSA/ECDSA) |
|---|---|---|---|
| Resistente a extensão de mensagem | ❌ | ✅ | ✅ |
| Chave | Simétrica | Simétrica | Par público/privado |
| Custo computacional | Baixo | Baixo | Alto |
| Quem verifica | Quem tem o secret | Quem tem o secret | Qualquer um com a chave pública |
| Não-repúdio | ❌ | ❌ (ambos os lados podem gerar) | ✅ |

## Aplicação prática: local-first sem storage

Um caso de uso concreto: um servidor gera um payload (ex.: carrinho de compras calculado) e o HMAC desse payload, envia os dois para o cliente sem persistir nada. Quando o cliente reenvia o payload, o servidor recalcula o HMAC com seu segredo e compara com o header recebido — se baterem, o payload não foi alterado desde que o próprio servidor o gerou. Ver [[wiki/concepts/local-first]] para o padrão completo e a motivação de custo de storage que leva a essa escolha.

## Relação com outros conceitos

- [[wiki/concepts/local-first]] — HMAC é o mecanismo que viabiliza confiar em dado do cliente sem persistir no servidor
- [[wiki/concepts/webhook-signature-validation]] — aplicação mais comum de HMAC em produção (Stripe, GitHub, Mercado Pago), mas sem a garantia de janela de tempo/replay que o cenário local-first também precisaria
- [[wiki/concepts/timing-attack]] — comparar o HMAC recebido com `===` vaza informação; sempre usar comparação em tempo constante
- [[wiki/concepts/criptografia]] — HMAC ocupa o meio-termo entre hash puro (sem chave) e assinatura assimétrica (par de chaves)
- [[wiki/concepts/encryption]] — HMAC garante integridade, não confidencialidade; não substitui encryption quando o dado precisa ficar ilegível

## Key sources

- [[wiki/sources/hmac-integridade-mensagem-local-first-entrevista]]
