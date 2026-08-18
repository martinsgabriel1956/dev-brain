---
type: concept
title: "Refresh Token Rotation"
aliases: ["rotation de refresh token", "anti-replay refresh token", "refresh token reuse detection", "janela de exposição", "device fingerprinting de token"]
date_created: 2026-08-14
date_updated: 2026-08-14
source_count: 1
tags: [jwt, refresh-token, seguranca, autenticacao, stateful, device-fingerprinting]
skill: tech-mentor-security
status: draft
---

# Refresh Token Rotation

Camada de segurança sobre o [[wiki/concepts/jwt|refresh token]]: em vez de um refresh token viver estático por dias/semanas e ser reutilizado em toda renovação, cada uso o torna **descartável**. A cada renovação de access token, o servidor invalida o refresh token que acabou de ser apresentado e emite um novo no lugar, junto com o novo access token.

## Por que rotacionar

Sem rotation, um refresh token roubado continua válido pelo prazo inteiro concedido a ele — dias ou semanas — mesmo que o dono legítimo continue usando o sistema normalmente sem perceber o roubo. Com rotation, o token vira de uso único: a primeira parte a apresentá-lo (dono ou atacante) o invalida para qualquer uso seguinte.

## Detecção de replay (reuse detection)

Se um refresh token **já rotacionado** (portanto inválido) for reapresentado ao servidor, isso é um sinal forte de que ele foi roubado — o atacante capturou o token antes do dono usá-lo, ou o dono usou antes do atacante, e a segunda tentativa cai num token morto. Nesse momento, a prática recomendada é revogar **toda a família de tokens** daquela sessão — não apenas negar a renovação — forçando reautenticação em todos os dispositivos, como um alarme automático que reage à fraude detectada.

```typescript
// Refresh token rotation — invalida o anterior ao emitir novo
async function refreshTokens(refreshToken: string) {
  const stored = await redis.get(`rt:${refreshToken}`);
  if (!stored) throw new Error('Token revogado ou inválido');

  await redis.del(`rt:${refreshToken}`);  // invalida imediatamente (rotation)

  const newAccessToken = generateAccessToken(stored.userId);
  const newRefreshToken = generateRefreshToken();
  await redis.set(`rt:${newRefreshToken}`, stored, { EX: 30 * 24 * 3600 });

  return { accessToken: newAccessToken, refreshToken: newRefreshToken };
}
```

## Fingerprinting / vinculação de dispositivo

Camada complementar: além de o token ser válido, ele precisa estar nas mãos de quem o solicitou originalmente. No login, o servidor captura um elemento identificador — user agent da requisição, ou um hash de dispositivo em caso de mobile — e o guarda atrelado ao refresh token. Se a renovação chegar de um navegador ou dispositivo diferente do capturado, o servidor recusa, mesmo que o token em si ainda seja válido e não tenha sido rotacionado.

É uma proteção mais fraca que amarração criptográfica de posse de chave (ex.: DPoP, RFC 9449 `[external]`) — um user agent pode ser forjado por um atacante — mas eleva o custo do ataque sem exigir troca de protocolo.

## Janela de exposição

A rotation e o fingerprinting reduzem, mas não eliminam, o risco residual do [[wiki/concepts/jwt|access token]] continuar válido até expirar mesmo após uma revogação — a chamada "janela de exposição" (tipicamente 5-15min, tempo de vida do access token). Nada verifica revogação a cada requisição enquanto o access token não expirar; só a tentativa de renovação via refresh token é bloqueada. Para a maioria das aplicações esse risco residual é aceitável; para sistemas de alta criticidade (pagamentos instantâneos, operações financeiras de alto valor, tempo real) pode não ser.

## Relação com outros conceitos

- [[wiki/concepts/jwt]] — refresh token rotation é a camada de segurança que compensa o refresh token ser [[wiki/concepts/stateless|stateful]] (revogável) enquanto o access token permanece stateless
- [[wiki/concepts/oauth2]] — o authorization server é tipicamente quem implementa e armazena o estado de rotation
- [[wiki/concepts/stateless]] — trade-off entre revogação (stateful) e performance (stateless) que motiva a divisão em dois tokens

## Key Sources

- [[wiki/sources/refresh-token-pattern-access-token-de-curta-duracao]] — rotation, reuse detection, fingerprinting e janela de exposição, no contexto de por que access token deve ser curto
