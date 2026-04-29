---
date: 2026-04-01
tags: [tech-mentor, security, secret-scanning, gitleaks, trufflehog, ghas, credential-leak]
skill: tech-mentor-security/references/secret-scanning
level: fundamento
---

# Secret Scanning

## Contexto

Uma credencial no GitHub pode ser explorada em **menos de 5 minutos** por bots automatizados. O histórico do git guarda para sempre — mesmo que você delete o arquivo, o commit ainda existe.

90% das breaches envolvem credenciais expostas. O custo de resposta a um vazamento (rotação, auditoria, notificação regulatória) supera muito o custo de prevenção.

## Como Funciona

Três camadas de defesa, cada uma cobrindo o que a anterior deixa passar:

```
Camada 1 — Pre-commit (local):    bloqueia antes do commit
Camada 2 — CI/CD:                 bloqueia antes do merge
Camada 3 — GHAS / monitoramento:  detecta no histórico e em repos já publicados
```

## Código de Referência

### Camada 1 — Pre-commit com Gitleaks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.4
    hooks:
      - id: gitleaks
        name: "Detect hardcoded secrets"

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: detect-private-key
      - id: detect-aws-credentials

  - repo: local
    hooks:
      - id: no-env-files
        name: "Prevent .env files from being committed"
        entry: bash -c 'if git diff --cached --name-only | grep -q "\.env$"; then echo "ERROR: .env file detected!"; exit 1; fi'
        language: system
        pass_filenames: false
```

```bash
pip install pre-commit
pre-commit install  # instala os hooks no repo local
```

**Customizar regras para tokens internos:**

```toml
# .gitleaks.toml
[extend]
useDefault = true

[[rules]]
id = "internal-api-key"
description = "Internal API Key"
regex = '''INTERNAL-[A-Z0-9]{32}'''

[allowlist]
regexes = [
  '''EXAMPLE_KEY_DO_NOT_USE''',  # exemplos em docs são ok
]
```

### Camada 2 — CI/CD

```yaml
# GitHub Actions — escaneia todo PR
jobs:
  secret-scan:
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # histórico completo — não só o último commit

      - name: Gitleaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: TruffleHog
        uses: trufflesecurity/trufflehog@main
        with:
          base: ${{ github.event.repository.default_branch }}
          head: HEAD
          extra_args: --only-verified  # reduz falsos positivos
```

### Camada 3 — GitHub Advanced Security (GHAS)

Detecta automaticamente 200+ padrões: AWS Keys, GitHub PAT, Google API Keys, Stripe, Twilio, JWT secrets, SSH private keys...

```bash
# Habilitar para toda a organização
curl -X PATCH https://api.github.com/orgs/my-org \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -d '{
    "secret_scanning_enabled_for_new_repositories": true,
    "secret_scanning_push_protection_enabled_for_new_repositories": true
  }'
```

**Custom patterns para tokens internos:**
```
Name: Internal Service Token
Pattern: IST_[0-9a-f]{40}
```

### O que nunca deve ir para o código

```
❌ API keys (AWS, GitHub, Google, Stripe, etc.)
❌ Senhas de banco de dados
❌ JWT secrets / signing keys
❌ SSH private keys
❌ OAuth client secrets
❌ Tokens de acesso (PAT, service tokens)
❌ Chaves de criptografia

✅ Nomes de hosts de dev/staging
✅ Configurações não-sensíveis (timeouts, feature flags)
✅ Chaves PÚBLICAS (de um par RSA)
✅ Exemplos claramente marcados (EXAMPLE_KEY_DO_NOT_USE)
```

### Alternativas ao hardcode

```typescript
// ❌ NUNCA
const AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY";

// ✅ IAM Role (melhor para EC2/Lambda/ECS) — sem credencial alguma no código
// A SDK pega automaticamente as credenciais da role da instância

// ✅ Secrets Manager
import { SecretsManagerClient, GetSecretValueCommand } from "@aws-sdk/client-secrets-manager";

async function getSecret(secretName: string) {
  const client = new SecretsManagerClient({ region: "us-east-1" });
  const response = await client.send(new GetSecretValueCommand({ SecretId: secretName }));
  return JSON.parse(response.SecretString!);
}

const dbCreds = await getSecret("prod/orders-service/postgres");

// ✅ Variável de ambiente (mínimo aceitável — injetado pelo sistema de deploy)
const API_KEY = process.env.PAYMENT_API_KEY!;
```

## Se um Secret Vazar

```
1. REVOGAR imediatamente no provider (< 15 min)
   → Não espere confirmar o impacto. Revogar é reversível, vazamento não é.

2. INVESTIGAR
   → CloudTrail, audit logs: houve acesso indevido?
   → Por quanto tempo a credencial esteve exposta?

3. ROTACIONAR todas as credenciais do mesmo sistema

4. REMOVER do histórico git (somente após revogar)
   git filter-repo --replace-text <(echo "AKIA_KEY==>REMOVED")
   git push origin --force --all
   → Avisar o time para re-clonar

5. NOTIFICAR
   → Time de segurança
   → Se dados de usuários expostos → LGPD/GDPR tem prazo de 72h

6. POST-MORTEM
   → Como chegou até aqui? Qual controle falhou?
   → Melhoria nos controles preventivos
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Pre-commit hooks | Bloqueia antes de chegar no repo | Dev pode desinstalar localmente (não é enforcement) |
| CI scanning | Enforcement garantido, histórico completo | Não evita o commit, só bloqueia o merge |
| GHAS | 200+ padrões sem configuração | Requer GitHub Enterprise em repos privados |
| `--only-verified` no TruffleHog | Reduz falsos positivos | Pode deixar passar credenciais não verificáveis |

## Quando Usar / Quando Evitar

**Sempre use:** pre-commit hooks + CI scanning são custo zero e bloqueiam o vetor mais comum de breach. Não há justificativa para não ter.

**GHAS vale quando:** organização com muitos repos e times — monitoramento centralizado compensa o custo.

## Conceitos Relacionados

[[secrets-management]] · [[devsecops-pipeline]] · [[supply-chain-security]] · [[autenticacao-segura]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-01*
