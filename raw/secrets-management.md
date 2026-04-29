---
date: 2026-03-30
tags: [tech-mentor, security, secrets, vault, aws-secrets-manager, dynamic-secrets, rotation]
skill: tech-mentor-security/references/secrets-management
level: fundamento
---

# Secrets Management

## Contexto

Secrets — credenciais de banco, chaves de API, tokens de serviços, certificados — são o alvo mais fácil em breaches de cloud. A maioria dos incidentes começa não por exploração sofisticada, mas por um `.env` commitado, uma variável de ambiente impressa em log, ou uma chave estática que nunca foi rotacionada.

**Regra zero**: secrets nunca existem em código-fonte, Dockerfiles, logs ou manifests de versão.

---

## O Problema com .env e Variáveis de Ambiente

```bash
# ❌ Problemas encadeados
DATABASE_URL=postgres://admin:senha123@prod-db.internal/app
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
STRIPE_SECRET_KEY=sk_live_...
```

- Git history retém secrets mesmo após remoção do arquivo — `git filter-branch` é necessário
- CI/CD logs podem imprimir variáveis de ambiente em falhas (`env: true` no GitHub Actions)
- Rotação exige redeploy completo
- Auditoria impossível: quem acessou qual secret, quando?

Variáveis de ambiente em containers têm o mesmo problema: aparecem em `docker inspect`, em dumps de crash e em `/proc/environ` — qualquer processo no container pode ler.

---

## Ferramentas de Secrets Management

| Ferramenta | Quando usar | Diferenciais |
|---|---|---|
| **HashiCorp Vault** | Multi-cloud, on-premise, controle máximo | Dynamic secrets, PKI, SSH CA, audit log completo |
| **AWS Secrets Manager** | Stack AWS, menor operacional | Rotação automática com RDS, integração IAM nativa |
| **GCP Secret Manager** | Stack GCP | Simples, integrado com Workload Identity |
| **Azure Key Vault** | Stack Azure | Certificados, chaves BYOK, HSM gerenciado |
| **External Secrets Operator** | Kubernetes + qualquer backend | Sincroniza secrets externos com K8s Secrets |

### HashiCorp Vault

```bash
# Armazenar e ler secrets (CLI)
vault kv put secret/myapp/db password="senha-segura" username="app_user"
vault kv get -field=password secret/myapp/db
```

```typescript
import vault from "node-vault";

const client = vault({ endpoint: process.env.VAULT_ADDR });

// AppRole — autenticação para serviços (sem credencial humana)
await client.approleLogin({
  role_id: process.env.VAULT_ROLE_ID,
  secret_id: process.env.VAULT_SECRET_ID
});

const { data } = await client.read("secret/data/myapp/db");
const dbPassword = data.data.password;
```

**Features que importam para arquitetos**:
- **Dynamic secrets**: Vault gera credenciais temporárias diretamente no PostgreSQL/MySQL/MongoDB
- **Lease com TTL**: credenciais expiram automaticamente, nenhuma revogação manual necessária
- **Audit log completo**: cada acesso registrado com identity, IP, timestamp, operação
- **PKI engine**: Vault como CA interna para emitir certificados mTLS com TTL de horas

### AWS Secrets Manager

```typescript
import { SecretsManagerClient, GetSecretValueCommand } from "@aws-sdk/client-secrets-manager";

const client = new SecretsManagerClient({ region: "us-east-1" });

const response = await client.send(
  new GetSecretValueCommand({ SecretId: "prod/myapp/database" })
);
const secret = JSON.parse(response.SecretString);
// { username: "app_user", password: "...", host: "..." }
```

Rotação automática: AWS Lambda rotaciona credenciais RDS sem downtime — nova senha criada no banco antes de atualizar o secret, versão `AWSPREVIOUS` mantida como fallback durante o processo.

---

## Dynamic Secrets — O Padrão Ideal

Credenciais estáticas são o problema: uma chave de banco criada há 3 anos e nunca rotacionada. Dynamic secrets invertem o modelo — credenciais criadas sob demanda, expiram automaticamente.

```
Aplicação → Vault → cria user temporário no PostgreSQL
                  → retorna credenciais com TTL de 1h
                  → após 1h, Vault revoga automaticamente via DROP ROLE
```

```hcl
# Vault: PostgreSQL dynamic secrets
resource "vault_database_secret_backend_role" "app" {
  name    = "app-role"
  backend = vault_database_secrets_mount.postgres.path
  db_name = "postgres"

  creation_statements = [
    "CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}';",
    "GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO \"{{name}}\";"
  ]

  default_ttl = "1h"
  max_ttl     = "24h"
}
```

Resultado: se uma credencial vazar, ela expira em no máximo 1 hora. Sem revogação manual, sem incidente prolongado.

Vault suporta dynamic secrets para: PostgreSQL, MySQL, MongoDB, Cassandra, Redis, AWS IAM, SSH, certificados PKI.

---

## Zero-Trust: Autenticação sem Secrets Estáticos

O objetivo final é eliminar completamente secrets estáticos — a aplicação autentica pela sua identidade, não por uma senha.

### Workload Identity no Kubernetes (IRSA na AWS)

```yaml
# Service Account com anotação para assumir IAM Role
apiVersion: v1
kind: ServiceAccount
metadata:
  name: myapp
  namespace: production
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::123456789:role/myapp-prod-role
```

O pod usa o token do Service Account para obter credenciais temporárias AWS via STS — sem nenhuma `AWS_ACCESS_KEY_ID` no código ou no ambiente. O SDK AWS faz o exchange automaticamente.

### EC2 Instance Profile

```typescript
// Na EC2 com Instance Profile configurado:
const s3 = new S3Client({ region: "us-east-1" });
// SDK usa http://169.254.169.254/latest/meta-data/iam/... automaticamente
// Nenhuma credencial hardcoded necessária
```

---

## Injeção de Secrets em Kubernetes

### Vault Agent Sidecar (recomendado para Vault)

```yaml
annotations:
  vault.hashicorp.com/agent-inject: "true"
  vault.hashicorp.com/agent-inject-secret-db: "secret/data/myapp/db"
  vault.hashicorp.com/agent-inject-template-db: |
    {{- with secret "secret/data/myapp/db" -}}
    DATABASE_URL=postgres://{{ .Data.data.username }}:{{ .Data.data.password }}@db:5432/app
    {{- end }}
```

O Vault Agent monta `/vault/secrets/db` como arquivo no container — nunca como variável de ambiente. A aplicação lê o arquivo, que é renovado automaticamente antes do TTL expirar.

### External Secrets Operator (multi-cloud)

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: myapp-db-secret
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secretsmanager
    kind: ClusterSecretStore
  target:
    name: myapp-db-secret       # K8s Secret criado automaticamente
  data:
    - secretKey: DATABASE_URL
      remoteRef:
        key: prod/myapp/database
        property: url
```

Sincroniza o secret externo como K8s Secret, com refresh automático a cada hora. Funciona com AWS Secrets Manager, GCP Secret Manager, Vault, Azure Key Vault e outros.

---

## Rotação de Secrets

### Rotação automatizada com AWS (4 passos)

```
createSecret  → criar nova versão no secrets manager
setSecret     → atualizar o recurso (banco, API) com a nova credencial
testSecret    → verificar que a nova credencial funciona
finishSecret  → promover nova versão para AWSCURRENT, antiga para AWSPREVIOUS
```

Durante o processo, `AWSPREVIOUS` permite fallback sem downtime — conexões existentes usam a versão antiga até expirar.

### Versionamento de secrets

```
AWSCURRENT  → versão ativa
AWSPREVIOUS → versão anterior (mantida durante rotação para conexões em andamento)
AWSPENDING  → nova versão em processo de rotação
```

Ao ler um secret durante rotação, a aplicação deve tentar `AWSCURRENT` e, em caso de falha de autenticação, tentar `AWSPREVIOUS` — isso elimina downtime em sistemas com connection pools.

---

## Auditoria

Todo secrets manager em produção deve ter audit log. O que cada acesso deve registrar:

```json
{
  "time": "2026-03-30T10:30:00Z",
  "type": "secret_access",
  "secret": "prod/myapp/database",
  "accessor": "k8s-serviceaccount/production/myapp",
  "operation": "read",
  "client_ip": "10.0.1.45",
  "lease_ttl": "3600"
}
```

**Alertas que devem existir**:
- Acesso a secrets fora do horário normal de operação
- Volume anômalo de acessos (possível exfiltração)
- Acesso de IP não registrado para aquela workload
- Identity desconhecida tentando ler secret de produção

---

## Armadilhas de Produção

**Secrets em URLs de conexão em logs**: `postgres://user:SENHA@host` aparece em stack traces. Sanitize connection strings antes de logar — ou use logging que nunca imprime a URL completa.

**Service account única para tudo**: se comprometida, acessa todos os secrets. Least privilege por serviço — cada workload tem sua própria identity com acesso apenas ao que precisa.

**Caching sem respeitar TTL**: aplicação cacheia o secret e não detecta rotação. Implemente refresh antes do TTL expirar (Vault Agent faz isso automaticamente).

**Secrets de dev/staging iguais aos de produção**: vazamento de credencial de dev = acesso a prod. Ambientes completamente isolados, sem credenciais compartilhadas.

**`git log` retém tudo**: remover um secret do código e fazer commit não resolve — está no histórico. Use `git filter-repo` ou `BFG Repo-Cleaner`, e invalide a credencial imediatamente.

---

## Secret Scanning no Pipeline

Bloquear o vazamento antes de chegar no repositório:

```yaml
# GitHub Actions — Gitleaks no PR
- name: Scan for secrets
  uses: gitleaks/gitleaks-action@v2
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

```bash
# Pre-commit hook local
pip install detect-secrets
detect-secrets scan > .secrets.baseline
# detecta: API keys, tokens AWS, chaves privadas, senhas em strings
```

GitHub Advanced Security escaneia automaticamente o histórico completo quando habilitado — e notifica quando um secret é encontrado, incluindo em commits antigos.

---

## Checklist de Produção

```
[ ] Nenhum secret em código-fonte ou git history
[ ] Secret scanning no CI (Gitleaks, TruffleHog ou GH Advanced Security)
[ ] Pre-commit hook bloqueando commits com secrets
[ ] Todos os secrets têm TTL definido
[ ] Dynamic secrets onde possível (banco, nuvem)
[ ] Rotação automatizada configurada
[ ] Auditoria habilitada com alertas
[ ] Least privilege: uma identity por workload
[ ] Secrets de dev/staging isolados de produção
[ ] Playbook documentado para secret comprometido
```

---

## Conceitos Relacionados

[[criptografia-fundamentos]] · [[autenticacao-segura]] · [[owasp-top10]] · [[zero-trust]] · [[devsecops-pipeline]]

---

*Fonte: tech-mentor skill · tech-mentor-security · 2026-03-30*
