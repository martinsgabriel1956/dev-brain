---
type: concept
title: "Defense in Depth"
aliases: ["defense in depth", "defesa em profundidade", "camadas de segurança", "layered security"]
date_created: 2026-06-05
date_updated: 2026-07-10
source_count: 2
tags: [defense-in-depth, security, arquitetura-seguranca, least-privilege, gatekeeper, waf]
skill: tech-mentor-security
status: stable
---

# Defense in Depth

Princípio de segurança que defende um sistema com múltiplas camadas de controle independentes. Se uma falha, as outras contêm o dano. Nenhuma camada assume que a anterior é perfeita.

## Camadas Típicas (Fora → Dentro)

```
CDN / WAF           → bloqueia ataques HTTP, DDoS
API Gateway         → autenticação, rate limiting, roteamento
Service Mesh / mTLS → autenticação entre serviços (L4/L7)
Aplicação           → validação de input, autorização por recurso
Banco de dados      → Row Level Security, column encryption
Storage             → encryption at rest, KMS
```

Cada camada é independente: um serviço interno ainda valida input mesmo que venha de outro serviço interno.

## Anti-pattern

"Nosso serviço só é chamado internamente, não precisa validar." — Lateral movement em um incidente começa exatamente aqui.

## Relação com os Padrões de Segurança

- [[concepts/gatekeeper-pattern]] — implementa a camada de borda (API Gateway)
- [[concepts/waf]] — camada antes do gateway (borda de rede)
- [[concepts/token-relay-pattern]] — garante que identidade e autorização persistam em todas as camadas internas
- [[concepts/valet-key-pattern]] — aplica least privilege na camada de credenciais
- [[wiki/concepts/hardening-de-servidor]] — camada de infraestrutura (SO/serviço), fora da pilha de aplicação listada acima

## Key Sources

- [[sources/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay]]
- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — as 5 práticas do Pragmatic Programmer como instâncias de camadas de defense in depth
- [[wiki/sources/ssh-chaves-como-funcionam]] — hardening de SSH como exemplo de camada de infraestrutura
