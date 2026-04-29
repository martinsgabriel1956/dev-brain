---
date: 2026-03-27
tags: [tech-mentor, system-design, infraestrutura, dns, rede]
skill: tech-mentor-system-design/references/architecture-ops.md
level: fundamento
---

# DNS — Domain Name System

## Contexto

DNS traduz nomes legíveis (`api.empresa.com`) em endereços IP (`192.168.1.1`). Parece trivial, mas tem armadilhas reais em migrações, failover e email deliverability. É o primeiro componente que qualquer requisição atravessa.

## Como Funciona

### Fluxo de Resolução

```
Browser digita "api.empresa.com"
        │
        ▼
1. Cache local (browser → OS → /etc/hosts)
        │ miss
        ▼
2. Recursive Resolver (8.8.8.8, 1.1.1.1 ou ISP)
        │ não sabe
        ▼
3. Root Name Server → "quem cuida de .com?" → TLD Server
        │
        ▼
4. TLD Name Server (.com) → "quem cuida de empresa.com?" → Authoritative NS
        │
        ▼
5. Authoritative Name Server (Route 53, Cloudflare DNS...)
   "api.empresa.com = 192.168.1.1" → resposta final
        │
        ▼
6. Recursive Resolver cacheia por TTL → entrega ao cliente
```

Percorre todo o caminho só na primeira vez. Depois fica cacheado em cada nível pelo TTL configurado.

## Código de Referência

### TTL — A Variável Mais Importante

```
TTL alto (86.400s = 1 dia):
  ✅ Menos queries aos DNS servers
  ❌ Mudança de IP demora até 24h para propagar

TTL baixo (300s = 5min):
  ✅ Mudanças propagam em minutos
  ❌ Mais carga nos DNS servers
```

**Estratégia correta para trocar IP sem downtime:**
```
7 dias antes:  reduza TTL para 300s
               (aguarde os caches antigos expirarem com o TTL alto anterior)
No momento:    mude o registro A para o novo IP
Aguarde:       5 minutos para propagação
Depois:        restaure TTL para valor alto (3600s+)
```

### Tipos de Registro

| Registro | Para que serve | Exemplo |
|---|---|---|
| `A` | Domínio → IPv4 | `api.empresa.com → 192.168.1.1` |
| `AAAA` | Domínio → IPv6 | `api.empresa.com → 2001:db8::1` |
| `CNAME` | Domínio → outro domínio (alias) | `www → empresa.com` |
| `ALIAS/ANAME` | CNAME mas permitido na raiz | `empresa.com → elb.amazonaws.com` |
| `MX` | Servidores de email | `empresa.com → mail.google.com` |
| `TXT` | Verificação, SPF, DKIM | Autenticação de email |
| `NS` | Aponta para o Authoritative NS | `empresa.com → ns1.route53.com` |

**Por que CNAME não funciona na raiz (`@`)?** O padrão DNS proíbe CNAME coexistir com outros registros. Na raiz sempre há `NS` e `SOA` — logo, CNAME é inválido. Use `ALIAS`/`ANAME` para apontar o apex para uma hostname.

### DNS como Ferramenta de Arquitetura (Route 53)

**Failover automático:**
```
Primary:   192.168.1.1  (health check ativo)
Secondary: 192.168.1.2  (assume se primary falhar)
Tempo de failover: ~60s (depende do TTL e intervalo de health check)
```

**Weighted routing — canary via DNS:**
```
70% → servidor A (versão atual)
30% → servidor B (nova versão)
```

**Latency-based routing:**
```
Usuário em São Paulo → us-east-1
Usuário em Tóquio   → ap-northeast-1
```

**Geolocation routing:**
```
Usuários do Brasil → conteúdo em português
Usuários da UE    → servidor na Europa (GDPR)
```

### SPF, DKIM, DMARC — Email via DNS

```dns
# SPF — autoriza quais servidores enviam email pelo domínio
TXT @ "v=spf1 include:_spf.sendgrid.net include:amazonses.com -all"

# DKIM — assina o email com chave privada
TXT s1._domainkey "v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBA..."

# DMARC — política quando SPF/DKIM falham
TXT _dmarc "v=DMARC1; p=quarantine; rua=mailto:dmarc@empresa.com"
# p=none → só monitora | p=quarantine → spam | p=reject → rejeita
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| **TTL alto** | Menos carga no DNS | Propagação lenta em mudanças |
| **TTL baixo** | Failover rápido | Mais queries, mais custo |
| **DNS como LB** | Zero infra extra | Sem health check — IP morto continua sendo retornado |
| **Weighted routing** | Canary sem infraestrutura extra | Granularidade baixa (não é por request) |

## Quando Usar / Quando Evitar

**Armadilhas comuns:**
- Propagação não é instantânea — ISPs podem ignorar TTL e cachear mais tempo
- CNAME na raiz do domínio quebra o MX — email para de funcionar
- DNS não é load balancer confiável — sem health check nativo
- Negative caching: `NXDOMAIN` também é cacheado — registro novo pode demorar a aparecer

## Conceitos Relacionados

[[fase-1-fundamentos-infraestrutura]] · [[load-balancer]] · [[cdn]] · [[email-deliverability]]
