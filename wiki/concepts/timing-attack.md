---
type: concept
title: "Timing Attack"
aliases: ["timing attack", "ataque de temporização", "side-channel timing", "crypto.timingSafeEqual"]
date_created: 2026-06-10
date_updated: 2026-07-04
source_count: 3
tags: [security, timing-attack, side-channel, criptografia, appsec, senhas]
skill: tech-mentor-security
status: stable
---

# Timing Attack

Ataque de side-channel que extrai informação a partir do **tempo de resposta** de operações criptográficas ou de autenticação. Se o tempo varia com base nos dados processados, esse delta de tempo vaza informação ao atacante.

## O Exemplo Clássico: Verificação de Senha Letra a Letra

Um algoritmo ingênuo de comparação de senha verifica caractere por caractere e retorna imediatamente ao encontrar a primeira divergência:

```
Senha real: gato12345

Tentativa: aaaa → falha no 1º char → resposta em 0.01ms
Tentativa: baaa → falha no 1º char → resposta em 0.01ms
...
Tentativa: gaaa → passa o 1º char, falha no 2º → resposta em 0.03ms
```

O delta de 0.02ms revela que o primeiro caractere é `g`. Repetindo o processo para cada posição, o atacante descobre a senha testando apenas **26 × N** combinações em vez de **26^N** — redução exponencial no esforço de brute force.

## Por Que Isso É Relevante

Mesmo tempos de resposta da ordem de microssegundos podem ser mensuráveis com estatística suficiente e condições de rede controladas. Ataques de timing remotos são difíceis mas não impossíveis — ataques locais são triviais.

O ponto prático: **qualquer comparação de segredos deve ser de tempo constante**.

## A Solução: Comparação de Tempo Constante

```typescript
// ❌ Vulnerável a timing attack — short-circuit em divergência
if (userToken === storedToken) { ... }

// ✅ Tempo constante — sempre compara todos os bytes
import { timingSafeEqual } from 'crypto'
const a = Buffer.from(userToken)
const b = Buffer.from(storedToken)
if (a.length === b.length && timingSafeEqual(a, b)) { ... }
```

Bibliotecas de criptografia estabelecidas (bcrypt, Argon2, libsodium) já usam comparação de tempo constante internamente.

## Implicações Mais Amplas

O timing attack é um exemplo de que **qualquer output do sistema pode ser vetor de informação**, não só os dados retornados. O tempo de resposta, o tamanho da resposta, o padrão de erros — tudo pode vazar estado interno.

Ver [[attack-surface]]: superfície de ataque inclui os outputs do sistema, não só os inputs.

## Relação com Outros Conceitos

- [[attack-surface]] — outputs (incluindo latência) são parte da superfície de ataque
- [[defense-in-depth]] — comparação de tempo constante é uma camada de controle na validação de credenciais
- [[concepts/bcrypt]] — já usa comparação de tempo constante internamente
- [[concepts/argon2]] — idem; bibliotecas maduras de password hashing abstraem isso
- [[concepts/password-hashing]] — contexto onde timing attacks em verificação de senha são relevantes

## Timing Attack em Assinatura de Webhook

O mesmo princípio se aplica à validação de webhooks: comparar a assinatura HMAC recebida com `===` vaza, por diferença de tempo, em qual byte a assinatura correta diverge — permitindo reconstruí-la. Ver [[wiki/concepts/webhook-signature-validation]].

## Key Sources

- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — exemplo didático: descobrir senha de 9 chars com 26×9 tentativas em vez de 26^9
- [[sources/seguranca-armazenamento-senhas-banco-de-dados]] — bcrypt e Argon2 como implementações que já resolvem o problema
- [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]] — timing attack aplicado à validação de assinatura de webhook
