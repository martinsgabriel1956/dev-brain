---
date: 2026-03-30
tags: [tech-mentor, security, criptografia, aes, tls, kms, envelope-encryption, pki]
skill: tech-mentor-security/references/crypto
level: fundamento
---

# Criptografia — Fundamentos

## Contexto

Criptografia para arquitetos não é sobre implementar algoritmos — é sobre tomar decisões corretas: qual algoritmo usar, onde armazenar chaves, como estruturar a proteção de dados em repouso e em trânsito. **Nunca implemente seu próprio algoritmo de criptografia.** Use bibliotecas auditadas.

---

## Conceitos Base

### Hash vs Encryption

```
Hash:       one-way. Não dá para reverter.
            Use para: senhas, integridade de dados, identificadores.
            Exemplos: bcrypt, Argon2, SHA-256 (para integridade, não senhas)

Encryption: two-way. Cifra e decifra com chave.
            Use para: dados que precisam ser recuperados.
            Exemplos: AES-256-GCM, RSA, ChaCha20
```

### Simétrica vs Assimétrica

| Critério | Simétrica (AES) | Assimétrica (RSA/EC) |
|---|---|---|
| **Velocidade** | Muito rápida (GB/s) | Lenta (KB/s — 1000× mais lenta) |
| **Chave** | Mesma para cifrar/decifrar | Par pública/privada |
| **Problema** | Como distribuir a chave? | Pública pode ser compartilhada livremente |
| **Uso típico** | Dados em repouso, bulk encryption | Troca de chaves, assinaturas, TLS handshake |

**Regra prática**: use assimétrica para *trocar* a chave simétrica. Use simétrica para *cifrar* os dados. Isso é **hybrid encryption** — e é o que TLS faz.

---

## AES-256-GCM — O Padrão

**AES** (Advanced Encryption Standard): cifra simétrica de bloco. 256 bits = tamanho da chave.

**GCM** (Galois/Counter Mode): modo de operação que adiciona autenticação (AEAD — Authenticated Encryption with Associated Data). Garante **confidencialidade + integridade** em uma operação.

```typescript
import { createCipheriv, createDecipheriv, randomBytes } from "crypto";

function encrypt(plaintext: string, key: Buffer): { ciphertext: string; iv: string; tag: string } {
  const iv = randomBytes(12);  // 96 bits — obrigatório para GCM, único por mensagem
  const cipher = createCipheriv("aes-256-gcm", key, iv);

  const encrypted = Buffer.concat([
    cipher.update(plaintext, "utf8"),
    cipher.final()
  ]);

  return {
    ciphertext: encrypted.toString("base64"),
    iv: iv.toString("base64"),
    tag: cipher.getAuthTag().toString("base64")  // autenticação — NUNCA omita
  };
}

function decrypt(ciphertext: string, iv: string, tag: string, key: Buffer): string {
  const decipher = createDecipheriv("aes-256-gcm", key, Buffer.from(iv, "base64"));
  decipher.setAuthTag(Buffer.from(tag, "base64"));  // valida integridade antes de decifrar

  return Buffer.concat([
    decipher.update(Buffer.from(ciphertext, "base64")),
    decipher.final()
  ]).toString("utf8");
}
```

### Gotchas críticos do AES-GCM

**IV (nonce) deve ser único por mensagem com a mesma chave.** Reutilizar `(key, nonce)` em GCM quebra toda a segurança — o atacante consegue recuperar a chave. Sempre gere com `randomBytes(12)`.

**Nunca use ECB mode** — sem IV, blocos idênticos geram ciphertext idêntico. Padrões ficam visíveis no dado cifrado.

**Sempre verifique o auth tag** — sem ele, não detecta tampering (bit-flipping attack).

**Por que GCM e não CBC?** CBC não autentica — um atacante pode modificar o ciphertext sem você detectar.

---

## Envelope Encryption — O Padrão de Produção

Cifrar dados diretamente com uma chave mestra tem dois problemas: rotação de chave exige re-cifrar tudo, e a chave fica exposta na memória por mais tempo. Envelope encryption resolve isso com dois níveis de chaves.

```
┌─────────────────────────────────────────────┐
│  Key Management Service (KMS)               │
│  Master Key (CMK/KEK) — NUNCA sai do KMS    │
└──────────────────┬──────────────────────────┘
                   │ gera e cifra DEK
                   ▼
         Data Encryption Key (DEK)  ← única por documento/registro
         Cifrada com CMK → armazenada junto com os dados
                   │ usada para
                   ▼
              Dados cifrados (AES-256-GCM)
```

**Fluxo para cifrar**:
1. KMS gera DEK → retorna `plaintext_DEK` + `encrypted_DEK`
2. Cifrar dados com `plaintext_DEK` (AES-256-GCM)
3. Descartar `plaintext_DEK` da memória imediatamente
4. Armazenar: dados cifrados + `encrypted_DEK`

**Fluxo para decifrar**:
1. Chamar KMS para decifrar `encrypted_DEK` (KMS autentica o caller via IAM)
2. Usar DEK resultante para decifrar os dados
3. Descartar DEK

**Por que usar envelope encryption**:
- Rotação de CMK = re-cifrar apenas as DEKs (pequenas), não terabytes de dados
- Comprometimento de uma DEK afeta apenas um registro
- CMK nunca toca os dados — KMS é o árbitro de quem pode decifrar

AWS KMS, GCP Cloud KMS e Azure Key Vault implementam nativamente.

---

## KDFs — Key Derivation Functions

Senhas têm baixa entropia. Não dá para usá-las diretamente como chave criptográfica. KDF transforma senha (baixa entropia) em chave segura, sendo computacionalmente cara para dificultar brute force.

| KDF | Uso recomendado | Resistência GPU | Observação |
|---|---|---|---|
| **Argon2id** | Senhas — novos sistemas | Alta (memory-hard) | Vencedor PHC 2015 |
| **bcrypt** | Senhas — sistemas legados | Moderada | Battle-tested, amplamente suportado |
| **PBKDF2-SHA256** | Compliance FIPS/NIST | Baixa | Mínimo 310k iterações (NIST 2023) |
| **scrypt** | Chaves + senhas | Alta (memory-hard) | Alternativa ao Argon2 |

```typescript
import argon2 from "argon2";

// Hash de senha — Argon2id para novos sistemas
const hash = await argon2.hash(password, {
  type: argon2.argon2id,
  memoryCost: 65536,  // 64MB — eleva custo de ataque por GPU
  timeCost: 3,
  parallelism: 4
});

// Verificação — timing-safe por padrão
const valid = await argon2.verify(hash, password);

// re-hash automático se os parâmetros mudaram
if (argon2.needsRehash(hash)) {
  const newHash = await argon2.hash(password, { ... });
  await db.users.updateHash(userId, newHash);
}
```

**Nunca use para senhas**: MD5, SHA-1, SHA-256 diretamente — são fast hashes, reversíveis em segundos com GPU moderna.

---

## TLS — Transport Layer Security

TLS é o protocolo que protege dados em trânsito. O que acontece no handshake:

```
1. ClientHello: versões TLS suportadas, cipher suites, random
2. ServerHello: versão e cipher suite escolhidos
3. Certificado: servidor envia seu certificado X.509
4. Key Exchange: troca de chave via ECDHE (Diffie-Hellman efêmero)
                 → forward secrecy: comprometer a chave privada hoje
                   não decripta tráfego passado
5. ChangeCipherSpec: "de agora em diante, tudo cifrado"
6. Handshake completo — dados fluem com AES-GCM

TLS 1.3 (use sempre):
  - Handshake mais rápido (1 RTT vs 2 RTT)
  - Cipher suites inseguras removidas (sem RC4, DES, 3DES)
  - Forward secrecy obrigatório
```

**HSTS — HTTP Strict Transport Security**:
```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

Diz ao browser: "nunca tente HTTP — vá direto para HTTPS por 1 ano"
Preload: incluído na lista hard-coded dos browsers (proteção desde o primeiro acesso)
```

**Minimum TLS version**:
```typescript
// Node.js — forçar TLS 1.2+ em servidores e clientes
const server = https.createServer({
  minVersion: "TLSv1.2",
  ciphers: [
    "TLS_AES_256_GCM_SHA384",      // TLS 1.3
    "TLS_CHACHA20_POLY1305_SHA256", // TLS 1.3
    "ECDHE-RSA-AES256-GCM-SHA384"  // TLS 1.2
  ].join(":")
});
```

---

## PKI — Public Key Infrastructure

PKI é o sistema que gerencia certificados digitais — base do HTTPS, mTLS e assinatura de código.

### Hierarquia de CAs

```
Root CA (offline, protegida fisicamente — não assina certificados finais)
    └── Intermediate CA (online — assina certificados)
            ├── api.exemplo.com
            ├── db.exemplo.com
            └── service-a (certificado de cliente para mTLS)
```

**Por que hierarquia?** Root CA comprometida = tudo comprometido. Intermediate CA comprometida = revoga o intermediate, emite novo. Root CA pode ficar offline, reduzindo superfície de ataque.

### Certificado X.509 — campos importantes

```bash
openssl x509 -in cert.pem -text -noout

# Subject:    CN=api.exemplo.com, O=Minha Empresa
# Issuer:     CN=Intermediate CA, O=Minha Empresa
# SAN:        DNS:api.exemplo.com, DNS:*.exemplo.com
# Valid:      Not Before / Not After
# Key Usage:  Digital Signature, Key Encipherment
# Ext Key:    TLS Web Server Authentication
```

**SAN (Subject Alternative Names) é obrigatório** — Common Name (CN) foi depreciado para validação de hostname pelos browsers.

### Revogação: OCSP Stapling

```
CRL (Certificate Revocation List):
  CA publica lista de seriais revogados periodicamente
  Problema: pode estar desatualizada, arquivo grande

OCSP (Online Certificate Status Protocol):
  Cliente consulta CA em tempo real para cada certificado
  Mais atual, mas adiciona latência

OCSP Stapling (recomendado):
  Servidor consulta OCSP periodicamente, inclui resposta assinada no handshake TLS
  Zero latência adicional para o cliente
```

---

## Assinaturas Digitais

Provam autenticidade e integridade — "este dado foi gerado por quem tem a chave privada".

```
Assinar:   hash(dado) + cifrar com chave PRIVADA → assinatura
Verificar: decifrar assinatura com chave PÚBLICA + comparar com hash(dado)
```

### HMAC vs Assinatura Assimétrica

| | HMAC | RSA/ECDSA/Ed25519 |
|---|---|---|
| **Chave** | Simétrica (compartilhada) | Par pública/privada |
| **Não-repúdio** | ❌ (ambos podem forjar) | ✅ (só quem tem privada assina) |
| **Velocidade** | Muito rápido | Mais lento |
| **Uso típico** | JWT HS256, webhooks, APIs internas | Code signing, documentos, JWT RS256/ES256 |

### Ed25519 — algoritmo recomendado

Estado da arte. Resistente a side-channel, não depende de randomness externo (ECDSA pode vazar chave privada se PRNG for ruim). Chaves de 32 bytes, assinaturas de 64 bytes.

```typescript
import { generateKeyPairSync, sign, verify } from "crypto";

const { privateKey, publicKey } = generateKeyPairSync("ed25519");

// Assinar
const signature = sign(null, Buffer.from(message), privateKey);

// Verificar
const valid = verify(null, Buffer.from(message), publicKey, signature);
```

---

## Criptografia em Repouso

### TDE — Transparent Data Encryption

Cifra os arquivos do banco de dados no nível de storage. Transparente para a aplicação — dados são decifrados antes de chegar na query.

**Protege contra**: acesso físico ao disco, backup roubado.

**Não protege contra**: SQL injection (dados já estão decifrados na query), DBA malicioso com acesso ao banco.

AWS RDS: habilitado por padrão com KMS. PostgreSQL: encryption via EBS.

### Column-Level Encryption

Colunas específicas cifradas — banco não vê o plaintext.

```sql
-- PostgreSQL com pgcrypto
INSERT INTO users (nome, cpf_encrypted)
VALUES ('João', pgp_sym_encrypt('123.456.789-00', current_setting('app.encryption_key')));

-- Decifrar
SELECT nome, pgp_sym_decrypt(cpf_encrypted::bytea, current_setting('app.encryption_key'))
FROM users WHERE id = 1;
```

### Application-Level Encryption

A aplicação cifra antes de persistir — banco nunca vê o plaintext.

```typescript
// CPF nunca persiste em plaintext
const cpfEncrypted = encrypt(user.cpf, await getDataKey());
await db.query("INSERT INTO users (cpf_encrypted) VALUES ($1)", [cpfEncrypted]);
```

### Trade-offs

| Abordagem | Protege contra | Busca | Custo operacional |
|---|---|---|---|
| TDE | Disco físico | ✅ Full index | Baixo |
| Column-level (DB) | Disco + DBA | ❌ Sem index | Médio |
| App-level | Disco + DBA + query layer | ❌ (blind index para igualdade) | Alto |

**Blind index** — busca por igualdade sem expor plaintext:

```sql
-- Coluna adicional com hash do valor + salt fixo por tenant
SELECT * FROM users WHERE cpf_hash = digest('123.456.789-00' || $salt, 'sha256');
```

---

## Rotação de Chaves

Chaves devem ser rotacionadas periodicamente. Implicação arquitetural: dados cifrados com chave antiga precisam ser re-cifrados ou você mantém múltiplas versões.

```
Incluir key_version no dado cifrado:
{
  "key_version": "v3",
  "iv": "...",
  "tag": "...",
  "ciphertext": "..."
}

Ao decifrar: usar versão indicada
Ao re-cifrar: migrar para versão atual em background job
```

Com envelope encryption: rotação de CMK = apenas re-cifrar as DEKs (KB de dados, não TB).

---

## Guia de Decisão Rápido

```
Precisa armazenar senha?
  → Argon2id (ou bcrypt se limitado pela lib)

Precisa cifrar dado para recuperar depois?
  → AES-256-GCM + envelope encryption via KMS

Precisa provar que mensagem não foi adulterada (serviços internos)?
  → HMAC-SHA256 com timingSafeEqual na verificação

Precisa provar autoria com não-repúdio (documentos, code signing)?
  → Ed25519 ou RSA-PSS 4096

Precisa proteger dados em repouso no banco?
  → TDE mínimo + column-level para PII + app-level para dados críticos

Precisa proteger dados em trânsito?
  → TLS 1.3 + HSTS + certificados com SAN válido
```

---

## Conceitos Relacionados

[[autenticacao-segura]] · [[secrets-management]] · [[data-privacy]] · [[owasp-top10]] · [[zero-trust]]

---

*Fonte: tech-mentor skill · tech-mentor-security · 2026-03-30*
