---
type: concept
title: "Defense in Depth"
aliases: ["defense in depth", "defesa em profundidade", "camadas de segurança", "layered security"]
date_created: 2026-06-05
date_updated: 2026-07-20
source_count: 3
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

## Exemplo: Três Camadas Contra Agente de IA Comprometido

[[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] aplica defense in depth a um domínio diferente da pilha de aplicação acima: contenção de agentes de codificação de IA.

```
Sessão (AI Jail / [[wiki/concepts/agent-containment]])  → isola o processo em execução agora
Código (Git, push manual)                                 → reverte dano ao filesystem do projeto
Sistema operacional ([[wiki/concepts/sistema-operacional-imutavel]]) → reverte dano ao próprio SO no reboot
```

Cada camada assume que a anterior pode falhar: mesmo que o agente escape da cela do [[wiki/entities/bubblewrap]], o dano ao código é revertido por `git checkout`; mesmo que corrompa arquivos fora do controle do Git, um SO imutável descarta a mudança no próximo boot.

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
- [[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] — modelo de três camadas (sessão/AI Jail, código/Git, SO imutável) contra agentes de IA comprometidos
