---
date: 2026-04-23
tags: [tech-mentor, security, ofensivo, fraud, abuse, bot-detection]
skill: tech-mentor-security/references/fraud-abuse
level: avançado
---

# Fraud & Abuse Detection

## Contexto

Fraude e abuso são ataques de camada de aplicação que passam pela segurança técnica — o atacante está autenticado, usa HTTPS e não dispara WAF. O que distingue o comportamento fraudulento é contexto: velocidade, padrão de acesso, device, localização, sequência de ações.

Sistemas de detecção de fraude são mais próximos de ML do que de firewalls. A pergunta não é "esse request é válido?" mas "esse comportamento faz sentido para este usuário neste contexto?"

## Como Funciona

### Tipos de Abuso

| Tipo | Descrição | Exemplo |
|---|---|---|
| Account Takeover (ATO) | Comprometer conta de usuário legítimo | Credential stuffing, session hijacking |
| Account Fraud | Criar contas falsas em massa | Fake reviews, bonus abuse, spam |
| Payment Fraud | Transações com cartões roubados | Card testing, chargebacks |
| Bot Traffic | Automatização não autorizada | Scraping, scalping, inventory hoarding |
| Promo Abuse | Explorar promoções além do permitido | Múltiplas contas por promoção |
| Content Abuse | Spam, conteúdo malicioso | Review spam, phishing hospedado |

### Device Fingerprinting

Identifica dispositivos sem cookies — persiste mesmo após clear cookies ou private browsing.

```typescript
// Sinais coletados para fingerprint
type DeviceSignals = {
  // Browser
  userAgent: string;
  language: string;
  timezone: string;
  screenResolution: string;
  colorDepth: number;
  cookiesEnabled: boolean;
  doNotTrack: string | null;

  // Canvas fingerprint (rendering differences por GPU/driver)
  canvasFingerprint: string;

  // WebGL
  webglVendor: string;
  webglRenderer: string;

  // Audio context (processing differences por hardware)
  audioFingerprint: string;

  // Fonts instaladas
  fonts: string[];

  // Comportamento
  touchPoints: number;
  hardwareConcurrency: number;
  deviceMemory: number;
};

// Bibliotecas: FingerprintJS Pro (servidor-side enrichment)
// Alternativa: botd para detecção de bots específica
import FingerprintJS from "@fingerprintjs/fingerprintjs-pro";

const fp = await FingerprintJS.load({ apiKey: FPJS_KEY });
const { visitorId, confidence } = await fp.get();
// visitorId: hash estável por device, 99.5% accuracy
```

### Velocity Checks — Detecção por Padrão

```typescript
// Redis — velocity checks por janelas de tempo
const VELOCITY_RULES = [
  { key: "login_failures:ip", window: 300, limit: 10 },   // 10 falhas/5min por IP
  { key: "login_failures:email", window: 3600, limit: 20 }, // 20 falhas/h por email
  { key: "new_accounts:ip", window: 86400, limit: 3 },     // 3 contas/dia por IP
  { key: "payment_attempts:user", window: 3600, limit: 5 } // 5 tentativas/h por usuário
];

async function checkVelocity(key: string, identifier: string): Promise<boolean> {
  const redisKey = `velocity:${key}:${identifier}`;
  const rule = VELOCITY_RULES.find(r => r.key === key)!;

  const current = await redis.incr(redisKey);
  if (current === 1) {
    await redis.expire(redisKey, rule.window);
  }

  return current > rule.limit;  // true = bloqueado
}
```

### Fraud Scoring — Risk-Based Decision

```typescript
type FraudSignals = {
  deviceId: string;
  ipAddress: string;
  userId: string;
  action: string;
  amount?: number;
  timestamp: Date;
};

type RiskScore = {
  score: number;      // 0-100
  decision: "allow" | "challenge" | "block";
  reasons: string[];
};

async function calculateRiskScore(signals: FraudSignals): Promise<RiskScore> {
  const reasons: string[] = [];
  let score = 0;

  // IP reputation
  const ipRep = await checkIPReputation(signals.ipAddress);
  if (ipRep.isVPN) { score += 20; reasons.push("vpn_detected"); }
  if (ipRep.isTor) { score += 40; reasons.push("tor_detected"); }
  if (ipRep.isDatacenter) { score += 25; reasons.push("datacenter_ip"); }

  // Geolocation anomaly
  const lastLocation = await getLastUserLocation(signals.userId);
  if (lastLocation) {
    const distance = calculateDistance(lastLocation, signals.ipAddress);
    const timeDiff = Date.now() - lastLocation.timestamp;
    const impossibleTravel = distance > 1000 && timeDiff < 3600000; // 1000km em 1h
    if (impossibleTravel) { score += 50; reasons.push("impossible_travel"); }
  }

  // Device anomaly
  const knownDevices = await getUserDevices(signals.userId);
  const isNewDevice = !knownDevices.includes(signals.deviceId);
  if (isNewDevice) { score += 15; reasons.push("new_device"); }

  // Velocity
  const highVelocity = await checkVelocity("login_failures:ip", signals.ipAddress);
  if (highVelocity) { score += 30; reasons.push("high_velocity"); }

  const decision = score < 30 ? "allow" : score < 60 ? "challenge" : "block";
  return { score, decision, reasons };
}
```

### Account Takeover — Detecção

```typescript
// Sinais de ATO
const ATO_SIGNALS = {
  newDevice: true,           // device não visto antes
  newLocation: true,         // país/cidade diferente
  passwordChanged: true,     // senha mudada recentemente
  emailChanged: true,        // email de notificação alterado
  mfaDisabled: true,        // MFA desabilitado
  highValueAction: true,     // saque, transferência, mudança de conta bancária
  unusualHour: true,        // 3am no fuso do usuário
  multipleFailedLogins: true // tentativas falhas recentes
};

// Ação por combinação de sinais:
// 1 sinal: log + monitorar
// 2-3 sinais: exigir MFA / re-autenticação
// 4+ sinais: bloquear + notificar usuário + revisão manual
```

### Bot Detection

```typescript
// Sinais de comportamento humano vs bot
type BehaviorSignals = {
  mouseMovements: { x: number; y: number; t: number }[];
  keystrokes: { key: string; t: number; duration: number }[];
  scrollEvents: number;
  timeOnPage: number;
  formFillDuration: number;
};

// Heurísticas básicas:
// - Mouse movement com padrão linear/grid = bot
// - Velocidade de digitação > 150wpm = suspeito
// - Zero mouse movement antes de submit = headless browser
// - Tempo em página < 2s = automatizado

// Serviços especializados: Cloudflare Turnstile, reCAPTCHA Enterprise, Arkose Labs
// Preferir challenge invisível — CAPTCHA visível é ruim para UX e resolvido por farms
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Regras baseadas em velocidade | Simples, explicável, baixa latência | Atacantes adaptativos contornam |
| ML/fraud scoring | Detecta padrões complexos | Caixa-preta, difícil de debugar |
| Device fingerprinting | Alta precisão sem cookies | Privacidade, falso positivo em VPNs legítimas |
| Friction (MFA, captcha) | Bloqueia bots | Aumenta abandono de usuários legítimos |
| Block vs challenge | Block é simples | Challenge (MFA) é melhor UX, mas mais complexo |

## Quando Usar / Quando Evitar

**Velocity checks:** sempre. São o mínimo de qualquer sistema com login ou transação.

**Fraud scoring:** quando há transações financeiras, bonus/promoções, ou mercado com histórico de abuso. Vale o investimento cedo — fraude cresce com o sucesso do produto.

**Device fingerprinting:** apps financeiros, marketplaces, qualquer produto com fraude recorrente. Verificar compliance com LGPD/GDPR — fingerprinting pode ser considerado dado pessoal.

**Regra geral:** começar simples (velocity + IP reputation), medir taxa de fraude, evoluir para ML quando os dados justificarem.

## Conceitos Relacionados

[[rate-limiting]] · [[autenticacao-segura]] · [[api-security]] · [[owasp-top10]] · [[pentest-redteam]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-23*
