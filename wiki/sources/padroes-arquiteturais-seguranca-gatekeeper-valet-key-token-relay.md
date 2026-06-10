---
type: source
title: "Padrões Arquiteturais de Segurança: Gatekeeper, Valet Key e Token Relay"
aliases: ["gatekeeper pattern", "valet key pattern", "token relay pattern", "segurança arquitetural api"]
date_created: 2026-06-05
date_updated: 2026-06-05
source_file: /home/nemomartins/Documentos/new/dev-study/raw/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay.md
source_url: ""
author: "Bernardo Lobato"
date_published: ""
date_ingested: 2026-06-05
source_count: 0
tags: [gatekeeper, valet-key, token-relay, attack-surface, api-security, waf, api-gateway, defense-in-depth, arquitetura-seguranca, presigned-url]
skill: tech-mentor-security
status: stable
---

## TL;DR

Três padrões arquiteturais de segurança que agem no nível do design, não do código. Gatekeeper centraliza todo tráfego externo em um único ponto de entrada, reduzindo superfície de ataque. Valet Key emite credenciais temporárias de escopo mínimo para acesso direto a recursos pesados (ex: S3 presigned URL). Token Relay propaga a identidade do usuário por todos os saltos internos da arquitetura, permitindo autorização fina em cada serviço.

## Key Claims

**Claim:** A maioria dos problemas de segurança em APIs tem origem arquitetural, não de código.
**Evidence:** Validar tokens, adicionar headers e middlewares cria falsa sensação de segurança se a arquitetura permite caminhos que nunca deveriam existir. O problema é quantos pontos de entrada existem e quem pode falar com quem.
**Confidence:** alta — alinhado com princípio de minimização de superfície de ataque.

**Claim:** Gatekeeper reduz superfície de ataque ao centralizar todo acesso externo em um único ponto.
**Evidence:** Serviços internos deixam de se preocupar com autenticação/autorização de borda — toda chamada já chega filtrada pelo componente único de entrada. API Gateway e BFF são implementações comuns.
**Confidence:** alta

**Claim:** WAF opera em nível mais baixo que Gatekeeper e não substitui um.
**Evidence:** WAF não sabe quem é o usuário, não conhece os serviços internos e não aplica autorização contextual. Atua em padrões de ataque HTTP conhecidos (OWASP Top 10, DDoS). O Gatekeeper atua em identidade e roteamento de negócio.
**Confidence:** alta

**Claim:** Valet Key evita que a API vire proxy de alto tráfego.
**Evidence:** Em vez de receber o arquivo do cliente e repassar ao storage, a API só gera a credencial temporária. O cliente faz upload/download diretamente. Mesmo que o token seja interceptado, o dano é limitado em tempo e escopo.
**Confidence:** alta — padrão documentado no Azure Architecture Center como "Valet Key pattern".

**Claim:** Token Relay garante que autorização aconteça em cada serviço, não só na borda.
**Evidence:** Em arquiteturas com múltiplos serviços, é comum validar autenticação na borda mas não verificar se aquele usuário pode acessar aquele recurso específico lá dentro. Com Token Relay, a identidade viaja junto — cada serviço pode aplicar suas próprias regras de autorização.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/gatekeeper-pattern]]
- [[concepts/valet-key-pattern]]
- [[concepts/token-relay-pattern]]
- [[concepts/attack-surface]]
- [[concepts/waf]]
- [[concepts/defense-in-depth]]
- [[concepts/rate-limiting]]
- [[concepts/media-upload-pattern]]
- [[entities/bernardo-lobato]]

## Open Questions

- Em arquiteturas serverless (Lambda/Functions), como aplicar o Gatekeeper pattern sem API Gateway gerenciado?
- Token Relay com tokens opacos (por referência) vs. tokens auto-contidos (JWT): qual a trade-off de segurança em cada salto?
- Como o Valet Key pattern interage com arquiteturas multi-tenant onde o mesmo storage serve múltiplos clientes?
