---
date: 2026-03-27
tags: [tech-mentor, system-design, infraestrutura, cdn, cache, edge, performance]
skill: tech-mentor-system-design/references/architecture-ops.md
level: fundamento
---

# CDN — Content Delivery Network

## Contexto

CDN é uma rede de servidores distribuídos geograficamente (PoPs — Points of Presence) que cacheiam e servem conteúdo próximo ao usuário. O objetivo é reduzir latência eliminando a distância física entre usuário e dados. Para assets estáticos, transforma latências de 120ms em 5ms.

## Como Funciona

```
Sem CDN:
Usuário (São Paulo) → origin (us-east-1) → ~120ms

Com CDN:
Usuário (São Paulo)
        │
[PoP: GRU — Cloudflare/Fastly/CloudFront]
        │
        ├── Cache HIT  → ~5-10ms
        └── Cache MISS → origin (~120ms) → cacheia → responde
```

### O que Cachear (e por quanto tempo)

**Assets estáticos com hash** — TTL máximo:
```
bundle.a1b2c3.js  → Cache-Control: public, max-age=31536000, immutable
style.x9y8z7.css  → Cache-Control: public, max-age=31536000, immutable
```
Hash no nome garante que URL nova = conteúdo novo. Zero problema de stale.

**HTML** — sem cache:
```
index.html → Cache-Control: no-cache
```
HTML referencia assets pelo hash. Se cachear HTML, usuário recebe HTML velho apontando para assets que não existem mais.

**APIs públicas** — TTL médio:
```
GET /products   → Cache-Control: public, s-maxage=300
GET /categories → Cache-Control: public, s-maxage=3600
GET /users/me   → Cache-Control: private, no-store
```
`s-maxage` controla o CDN especificamente — sobrescreve `max-age` para proxies, não para o browser.

## Código de Referência

### HTTP Headers de Cache

```
Cache-Control: max-age=3600               → cacheia 1h (browser + CDN)
Cache-Control: s-maxage=86400             → 1 dia só no CDN
Cache-Control: no-cache                   → pode cachear, mas revalida antes de servir
Cache-Control: no-store                   → nunca cacheia (dados sensíveis)
Cache-Control: private                    → só no browser, CDN não cacheia
Cache-Control: immutable                  → nunca revalida (assets com hash)
Cache-Control: stale-while-revalidate=60  → serve stale por 60s enquanto revalida
```

### ETag — Revalidação Eficiente

```
1. Servidor responde:           ETag: "abc123"
2. Browser/CDN guarda o ETag

3. Próxima request:             If-None-Match: "abc123"
4. Servidor responde:
   → 304 Not Modified (sem body) — usa o cacheado
   → 200 OK com novo ETag        — conteúdo mudou, baixa novamente
```

Economiza bandwidth — valida sem transferir bytes.

### Cache Invalidation

**Purge por URL via API:**
```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "Authorization: Bearer {token}" \
  -d '{"files": ["https://exemplo.com/api/products"]}'
```

**Surrogate Keys / Cache Tags (Cloudflare, Fastly):**
```
# Ao servir, tag a resposta:
Surrogate-Key: product-123 category-electronics

# Ao atualizar, invalida pelo tag:
curl -X POST purge -H "Surrogate-Key: product-123"
# Invalida tudo taggeado com product-123
```

### Edge Computing — Lógica no CDN

```
Usuário → Edge Node (Cloudflare Worker / Lambda@Edge / Vercel Edge)
              │
              ├── Executa lógica (auth, A/B, redirect)
              └── Cache miss → origin
```

| Caso | Benefício | Trade-off |
|---|---|---|
| A/B testing | Sem roundtrip ao origin | Difícil debugar no edge |
| JWT validation | Rejeita inválidos antes do origin | JWT precisa ser stateless |
| Geolocation routing | Usuário → servidor mais próximo | Replicação cross-region |
| Bot detection | Bloqueia antes da infra | Modelos ML simples |
| Image optimization | Resize/format on demand | Custo de CPU no edge |

**Limitações do edge runtime:**
- CPU ~50ms por request
- Sem filesystem, sem processos filhos
- Cold start ~0ms (V8 isolates)

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| **Assets estáticos** | Hit rate ~100%, latência mínima | Setup de cache busting necessário |
| **APIs cacheáveis** | Reduz carga no origin drasticamente | Dados podem ficar stale até o TTL |
| **Purge** | Invalida imediatamente | Custo de API calls, complexidade |
| **Edge functions** | Latência ~5ms para lógica | CPU limitada, debugging difícil |
| **Proteção DDoS** | Absorve volumétrico antes do origin | Origin exposto se IP vazar |

## Quando Usar / Quando Evitar

**CDN não ajuda com:**
- ❌ Dados personalizados por usuário → use `Cache-Control: private`
- ❌ Mutações (POST/PUT/DELETE) → não fazem sentido em cache
- ❌ WebSocket/SSE → conexões persistentes (suporte parcial em CDNs modernos)
- ❌ Consistência forte → dado precisa estar atualizado ao milissegundo

**CDN como proteção:**
- WAF (Web Application Firewall) no edge — bloqueia OWASP Top 10 antes do origin
- Rate limiting antes de chegar à aplicação
- DDoS absorption — volumétrico absorvido pela rede do CDN
- Origin "escondido" — ninguém sabe o IP real do servidor

## Conceitos Relacionados

[[fase-1-fundamentos-infraestrutura]] · [[dns]] · [[load-balancer]] · [[cache]] · [[http-caching]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
