---
date: 2026-04-23
tags: [tech-mentor, security, criptografia, post-quantum, pqc, nist]
skill: tech-mentor-security/references/post-quantum-crypto
level: arquiteto
---

# Post-Quantum Cryptography (PQC)

## Contexto

Computadores quânticos com escala suficiente quebram RSA, ECDSA e ECDH em tempo polinomial via algoritmo de Shor. A criptografia simétrica (AES-256) sobrevive com ajuste de tamanho de chave. TLS, certificados X.509, assinaturas digitais, VPNs e SSH — toda a infraestrutura de segurança moderna depende de algoritmos vulneráveis a quântico.

O NIST finalizou os primeiros padrões PQC em 2024. A migração é necessária agora por causa do ataque **harvest-now-decrypt-later**: adversários estão coletando tráfego criptografado hoje para decriptar quando tiverem computadores quânticos suficientes. Dados com longa confidencialidade (segredos de estado, médicos, financeiros) são os mais urgentes.

## Como Funciona

### Por Que RSA/ECC Quebra com Quântico

```
RSA segurança:  fatorar n = p × q com p, q primos grandes
ECDSA segurança: resolver problema do logaritmo discreto em curva elíptica

Algoritmo de Shor (quântico):
  Fatoração de n em O((log n)³) — tempo polinomial
  Logaritmo discreto em O((log n)³)

RSA-2048: computador clássico → 300 trilhões de anos
          computador quântico com ~4000 qubits lógicos → horas

Estimativa de timeline: 2030-2035 para quântico criptograficamente relevante
(incerteza alta — pode ser antes ou depois)
```

### AES e Hash — O Que Sobrevive

```
AES-128: Grover's algorithm reduz para equivalente 64-bit → INSEGURO pós-quântico
AES-256: Grover's algorithm reduz para equivalente 128-bit → SEGURO (dobrar tamanho é suficiente)
SHA-256: levemente enfraquecido → migrar para SHA-384/SHA-512
SHA-3:   projetado para resistência quântica → SEGURO
```

### NIST PQC Standards (2024)

O NIST padronizou três algoritmos após 7 anos de processo:

| Algoritmo | Padrão NIST | Tipo | Uso Principal |
|---|---|---|---|
| **CRYSTALS-Kyber** | FIPS 203 (ML-KEM) | KEM (troca de chave) | Substituição de ECDH / RSA encrypt |
| **CRYSTALS-Dilithium** | FIPS 204 (ML-DSA) | Assinatura digital | Substituição de ECDSA / RSA sign |
| **SPHINCS+** | FIPS 205 (SLH-DSA) | Assinatura (hash-based) | Backup stateless, mais conservador |

**Falcon** (FIPS 206 / FN-DSA) — também padronizado, menor tamanho de assinatura mas implementação mais complexa.

### CRYSTALS-Kyber (ML-KEM) — Como Funciona

Baseado no problema **Learning With Errors (LWE)** sobre reticulados (lattices) — dificuldade acreditada resistente a quântico.

```
Key Exchange com Kyber (simplificado):
1. Alice gera chave pública/privada
2. Bob encapsula segredo usando chave pública de Alice → ciphertext
3. Alice decapsula ciphertext com chave privada → mesmo segredo
4. Ambos têm shared secret para derivar chave simétrica (AES)

Tamanhos (Kyber-768, nível de segurança AES-192 equivalente):
  Chave pública:    1184 bytes  (vs 32 bytes ECDH P-256)
  Chave privada:    2400 bytes
  Ciphertext:       1088 bytes
  Performance: comparável ao ECDH para operações cripto
```

### Estratégia de Migração

**Hybrid approach** — combinar algoritmo clássico + PQC durante transição:

```
TLS com hybrid key exchange:
  X25519 (ECDH clássico) + Kyber-768 (PQC)
  → shared secret = KDF(ECDH_secret || Kyber_secret)
  → Seguro se QUALQUER UM dos dois for seguro
  → Proteção contra: quântico (Kyber) + side-channels novos em PQC (X25519)
```

**Suporte atual:**
- **OpenSSL 3.x:** suporte experimental via OQS (Open Quantum Safe)
- **Cloudflare:** X25519Kyber768 em TLS 1.3 desde 2023
- **AWS:** KMS suporte a Kyber, s2n-tls com híbrido
- **Google Chrome:** X25519Kyber768 desde versão 116

```go
// Go — usando liboqs via wrapper
import "github.com/open-quantum-safe/liboqs-go/oqs"

// Geração de par de chaves Kyber-768
kem := oqs.KeyEncapsulation{}
kem.Init("Kyber768", nil)
defer kem.Clean()

publicKey, err := kem.GenerateKeyPair()

// Encapsulação (lado do cliente)
ciphertext, sharedSecretClient, err := kem.EncapSecret(serverPublicKey)

// Decapsulação (lado do servidor)
sharedSecretServer, err := kem.DecapSecret(ciphertext)
// sharedSecretClient == sharedSecretServer
```

### Harvest-Now-Decrypt-Later

```
Adversários (nation-state) já estão coletando:
  - Tráfego TLS de alvos de alto valor
  - Chaves públicas de certificados
  - Dados criptografados em repouso

Quando quântico estiver disponível:
  - Quebram a troca de chave registrada
  - Decriptam todo o tráfego histórico

Dados com confidencialidade longa (> 10 anos) são risco AGORA:
  - Segredos governamentais e militares
  - Propriedade intelectual sensível
  - Dados médicos e financeiros de longo prazo
  - Chaves mestras de PKI

Ação: migrar para PQC híbrido em sistemas com esses dados antes de 2027
```

### Timeline de Migração Recomendada

```
2024-2025 (agora):
  ✓ Inventário de algoritmos criptográficos em uso
  ✓ Identificar dados com longa confidencialidade
  ✓ Testar hybrid TLS em ambiente staging
  ✓ Atualizar dependências (OpenSSL, BoringSSL, libraries)

2025-2027:
  ✓ Hybrid TLS em produção para dados sensíveis
  ✓ Assinaturas PQC em code signing e certificados internos
  ✓ PKI interna migrada para algoritmos híbridos

2027-2030:
  ✓ Migração completa para PQC puro
  ✓ Deprecar RSA/ECDSA onde PQC estiver maduro
  ✓ Certificados públicos com PQC (requer browser/CA ecosystem)
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Hybrid approach | Seguro contra clássico E quântico | Overhead de tamanho e latência |
| Kyber vs RSA | Resistente a quântico | Chaves maiores (3-10x), impacto em handshake |
| Migração agora | Proteção contra harvest-now | Ecossistema ainda amadurecendo |
| Esperar standards maduros | Evitar retrabalho | Dados sensíveis coletados agora |
| Dilithium vs SPHINCS+ | Dilithium é mais rápido | SPHINCS+ é mais conservador (stateless, mais confiante) |

## Quando Usar / Quando Evitar

**Migrar agora (alta prioridade):**
- Dados com confidencialidade > 10 anos
- Sistemas governamentais, defesa, financeiro de longo prazo
- Infraestrutura PKI interna (pode migrar sem dependência do ecosystem externo)

**Hybrid como padrão (2025+):**
- Qualquer novo sistema com requisito de segurança elevado
- TLS interno entre serviços onde você controla ambos os lados

**Aguardar (baixa prioridade):**
- Certificados TLS públicos — depende de suporte de browsers e CAs, em evolução
- Dados com curto prazo de sensibilidade (< 5 anos)

## Conceitos Relacionados

[[criptografia-fundamentos]] · [[tls-mtls-vpn]] · [[secrets-management]] · [[compliance-soc2-pci]] · [[zero-trust]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-23*
