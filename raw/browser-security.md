---
date: 2026-04-23
tags: [tech-mentor, security, ofensivo, browser, csp, cors, spectre]
skill: tech-mentor-security/references/browser-security
level: avançado
---

# Browser Security

## Contexto

O browser é o runtime mais hostil que existe: executa código de múltiplas origens simultaneamente, compartilha memória e cache entre tabs, e precisa isolar processos maliciosos de dados sensíveis. Cada header de segurança e política de isolamento existe por causa de um ataque real que foi explorado em produção.

Engenheiros que entendem o modelo de segurança do browser escrevem aplicações que não dependem só de "o usuário não vai fazer isso".

## Como Funciona

### Same-Origin Policy (SOP)

A política fundamental: scripts de `https://app.com` não podem ler respostas de `https://api.bank.com`. Origem = protocolo + host + porta.

```
https://app.com/page  →  https://app.com/api    ✅ mesma origem
https://app.com/page  →  https://api.app.com    ❌ host diferente
https://app.com/page  →  http://app.com/api     ❌ protocolo diferente
https://app.com/page  →  https://app.com:8080   ❌ porta diferente
```

**SOP não bloqueia:** envio de requests (POST, forms) — só leitura da resposta. CSRF explora isso.

### CORS — Cross-Origin Resource Sharing

CORS permite exceções controladas à SOP via headers do servidor.

```typescript
// Express — configuração correta
import cors from "cors";

app.use(cors({
  origin: ["https://app.com", "https://admin.app.com"],  // lista explícita
  methods: ["GET", "POST", "PUT", "DELETE"],
  allowedHeaders: ["Content-Type", "Authorization"],
  credentials: true,   // permite cookies cross-origin
  maxAge: 86400        // pre-flight cache em segundos
}));

// NUNCA fazer isso:
// origin: "*" com credentials: true → o browser rejeita, mas indica config errada
// origin: true → espelha qualquer origem → CORS inútil
```

**Pre-flight request:** para métodos não-simples (PUT, DELETE, custom headers), o browser envia `OPTIONS` primeiro. Servidor responde com headers CORS. Só então o request real é enviado.

### Content Security Policy (CSP)

CSP define de onde recursos podem ser carregados, mitigando XSS — mesmo que código malicioso seja injetado, o browser bloqueia execução se não estiver na policy.

```http
# CSP restritiva para SPA
Content-Security-Policy:
  default-src 'none';
  script-src 'self' 'nonce-{random}';
  style-src 'self' 'unsafe-inline';
  img-src 'self' data: https://cdn.app.com;
  font-src 'self' https://fonts.gstatic.com;
  connect-src 'self' https://api.app.com;
  frame-ancestors 'none';
  base-uri 'self';
  form-action 'self';
```

**`strict-dynamic`:** substitui allowlists de URLs por nonces — mais robusto porque nonces mudam por request.

```http
Content-Security-Policy:
  script-src 'nonce-abc123' 'strict-dynamic';
```

```html
<!-- Apenas scripts com nonce correto executam -->
<script nonce="abc123" src="/app.js"></script>
```

**CSP Report-Only:** mode de teste antes de enforçar.
```http
Content-Security-Policy-Report-Only: default-src 'self'; report-uri /csp-report
```

### Fetch Metadata & Isolation Headers

Trio de headers que implementam isolamento de processo entre origens:

```http
# Impede que sua página seja embarcada em iframe de outro domínio
Cross-Origin-Opener-Policy: same-origin

# Impede que sua página carregue recursos de outras origens sem CORS explícito
Cross-Origin-Embedder-Policy: require-corp

# Impede que seu recurso seja lembarcado por outras origens sem permissão explícita
Cross-Origin-Resource-Policy: same-site
```

**Por que importam (Spectre):** com COEP + COOP ativos, o browser habilita `SharedArrayBuffer` e timers de alta precisão — necessários para WebAssembly, mas também para explorar timing side-channels como Spectre. Sem esses headers, o browser desabilita os recursos para proteção.

**Fetch Metadata — defense no servidor:**
```typescript
// Bloquear requests que não parecem legítimos
app.use((req, res, next) => {
  const dest = req.headers["sec-fetch-dest"];
  const site = req.headers["sec-fetch-site"];
  const mode = req.headers["sec-fetch-mode"];

  // Bloquear requests de outras origens para endpoints internos
  if (site && site !== "same-origin" && site !== "same-site" && site !== "none") {
    if (req.path.startsWith("/internal/")) {
      return res.status(403).json({ error: "Forbidden" });
    }
  }

  next();
});
```

### Spectre / Meltdown — Impacto no Browser

```
Spectre (CVE-2017-5753/5715):
  Exploita execução especulativa do CPU para ler memória de outros processos.
  Em browsers: JavaScript pode ler memória de outras tabs (mesma origem é irrelevante).

Mitigações implementadas pelos browsers:
  - Redução de precisão de timers (performance.now(), Date.now())
  - Desabilitação de SharedArrayBuffer por padrão
  - Site Isolation: cada origem em processo separado do OS
  - Requer COEP + COOP para reabilitar features de alta precisão
```

### Outros Headers Importantes

```http
# Forçar HTTPS (1 ano, incluir subdomínios, preload)
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

# Bloquear MIME type sniffing
X-Content-Type-Options: nosniff

# Controlar informações no Referer
Referrer-Policy: strict-origin-when-cross-origin

# Bloquear clickjacking (substituído por frame-ancestors no CSP)
X-Frame-Options: DENY

# Permissões de APIs do browser
Permissions-Policy: camera=(), microphone=(), geolocation=(self)
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| CSP strict | Elimina XSS mesmo com injection | Complexidade de manutenção de nonces/hashes |
| COEP/COOP | Habilita recursos de alta performance | Quebra embeds de terceiros (iframes, pixels) |
| SameSite=Strict | Bloqueia CSRF completamente | Quebra fluxos de login via link externo |
| CORS restritivo | Bloqueia requests não autorizados | Pode quebrar integrações legítimas |

## Quando Usar / Quando Evitar

**CSP:** todo app com usuários. Começar com `Report-Only` para medir violações antes de enforçar.

**COEP/COOP:** apps que usam `SharedArrayBuffer` (WebAssembly intensivo, colaboração em tempo real). Verificar se embed de terceiros (analytics, suporte) vai quebrar antes de ativar.

**HSTS Preload:** domínios em produção com HTTPS permanente. Irreversível — uma vez no preload list, não tem como remover rapidamente.

## Conceitos Relacionados

[[owasp-top10]] · [[api-security]] · [[autenticacao-segura]] · [[input-validation-output-encoding]] · [[secure-design-patterns]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-23*
