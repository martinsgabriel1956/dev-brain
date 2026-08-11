---
type: concept
title: "Sticky Session"
aliases: ["session affinity", "afinidade de sessão", "session stickiness"]
date_created: 2026-06-26
date_updated: 2026-08-10
source_count: 3
tags: [system-design, load-balancer, sessao, stateful, escalabilidade]
skill: tech-mentor-system-design
status: draft
---

# Sticky Session

Configuração do [[load-balancer]] que garante que **todas as requisições de um mesmo usuário sempre vão para o mesmo servidor**. Usada como solução paliativa quando o servidor é stateful (guarda sessão em memória).

## Como funciona

O Load Balancer usa um cookie ou IP hash para identificar o usuário e roteá-lo sempre para a mesma instância.

```
Usuário A → sempre Servidor 1
Usuário B → sempre Servidor 2
Usuário C → sempre Servidor 1
```

## O Problema

Sticky session é uma **solução paliativa** que carrega custos sérios:

1. **Desequilíbrio de carga** — um servidor pode ficar sobrecarregado enquanto outros ficam ociosos
2. **Perda de sessão em falha** — se o Servidor 1 cair, todos os usuários nele perdem a sessão
3. **Dificulta escalabilidade** — novas instâncias não recebem usuários existentes automaticamente
4. **Limita Auto Scaling** — remover uma instância destrói sessões ativas

## Por que não é a solução certa

Sticky session trata o sintoma (sessão em memória) sem resolver a causa. A solução correta é tornar o servidor [[stateless]] — mover o estado para fora (Redis, banco) para que qualquer servidor possa atender qualquer usuário.

## Quando é aceitável

- Migração gradual de sistema legado stateful
- Aplicações com sessão de curta duração e baixo risco de perda
- Ambientes com carga previsível e uniforme entre usuários

## Relação com outros conceitos

- [[stateless]] — a solução correta que elimina a necessidade de sticky sessions
- [[load-balancer]] — quem implementa a afinidade de sessão
- [[escalabilidade-horizontal]] — sticky session limita os benefícios da horizontal

## Key sources

- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
- [[wiki/sources/reacao-artigo-visual-algoritmos-load-balancing]] — contraste implícito: Round Robin, Weighted Round Robin, Least Connections e PEWMA pressupõem servidores intercambiáveis (sem afinidade), o cenário que sticky session existe para contornar quando essa premissa não é atendida
- [[wiki/sources/escalar-para-um-milhao-de-usuarios]] — sticky sessions e preferências do usuário como caso de uso do NoSQL externo; esse store é compartilhado inclusive entre data centers na etapa multi-região
