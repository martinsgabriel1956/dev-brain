---
type: source
title: "15 Dias Depois de Lançar Meu SaaS: Números, Ataques e Vulnerabilidades"
aliases: ["find my saas 15 dias", "pentest márcio mendes find my saas", "oauth google scope injection find my saas"]
date_created: 2026-08-06
date_updated: 2026-08-06
source_count: 0
tags: [saas, indie-hacker, lean-startup, mvp, vps, oauth2, open-redirect, pentest, ddos, waf, over-engineering, marketing-organico, monetizacao, google-analytics]
skill: tech-mentor-security
status: stable
source_file: raw/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades.md
source_url: ""
author: "Davin (canal Mano Davin / Mano Deivin, Find My SaaS)"
date_published: "vídeo gravado em 6 de abril (ano não confirmado na transcrição)"
date_ingested: 2026-08-06
---

## TL;DR

Vlog em primeira pessoa, 15 dias após o lançamento público do Find My SaaS (marketplace de upvote para outros SaaS, findmysas.com), cobrindo quatro frentes: (1) métricas de tráfego e cadastro via Google Analytics — 12 mil usuários, 178 mil eventos, 646 SaaS cadastrados organicamente, tráfego majoritariamente orgânico via YouTube; (2) faturamento de R$ 4.819 em 15 dias via boost pago, sem tráfego pago nem funil; (3) 230 mil+ requisições recebidas, incluindo 157 tentativas maliciosas bloqueadas pelo Cloudflare, contra uma VPS Hostinger de 1 núcleo/4GB rodando um monolito Ruby sem Kubernetes nem microsserviços; (4) pentest voluntário de um inscrito (Márcio Mendes) que encontrou 12 vulnerabilidades, incluindo uma crítica — o fluxo de login via Google OAuth aceitava parâmetros de escopo/permissão extra pela URL sem validação, permitindo um ataque de engenharia social para captura de token via link malicioso. O autor também narra pressão de "especialistas de PowerPoint" sugerindo features e troca de stack (ex.: reescrever em TypeScript) sem experiência prévia de lançamento própria.

**Nota de continuidade:** esta fonte antecede cronologicamente [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]] (mesmo projeto, mesmo autor). Nesta fonte, o autor descreve o Cloudflare bloqueando 157 tentativas maliciosas sem incidente grave; no incidente posterior, um SYN flood de 260 milhões de requests derruba o servidor por 6h justamente porque o modo Under Attack do Cloudflare estava desativado — não há contradição factual (são eventos em momentos diferentes), mas marca uma progressão de maturidade de segurança que vale registrar como continuidade narrativa, não como fato isolado desta fonte.

## Key Claims

1. **Um MVP em VPS única (1 vCPU, 4GB RAM, 50GB disco), monolito sem Kubernetes/microsserviços/arquitetura event-driven, sustentou 230 mil+ requisições em 15 dias, incluindo ataques.** *Evidência: relato direto do autor com números do Cloudflare/infra; sem verificação externa de logs brutos nesta ingestão — number self-reported.* Ver [[wiki/concepts/over-engineering]] e [[wiki/concepts/mvp]].
2. **157 tentativas maliciosas foram bloqueadas pelo Cloudflare no período**, parte de um total de 230-234 mil requisições. *Evidência: dashboard do Cloudflare, citado mas não capturado em screenshot na transcrição.* Ver [[wiki/concepts/waf]] e [[wiki/concepts/ddos-syn-flood]].
3. **Vulnerabilidade crítica de OAuth: o fluxo de login via Google aceitava parâmetros extras (escopo/permissão) via URL sem validação server-side, permitindo que um atacante montasse um link malicioso pedindo permissões além do escopo padrão (e-mail, nome, foto) e capturasse o token de autenticação quando a vítima aceitava.** *Evidência: relato do autor sobre o achado do pentester Márcio Mendes; mecanismo descrito é consistente com falha de validação de parâmetros do Authorization Request (`scope`, possivelmente `redirect_uri`) descrita em `references/appsec-authn-authz.md` do skill tech-mentor-security — a claim do autor de que "o erro não era da aplicação, era confiar no input do usuário" é imprecisa: falta de validação server-side de parâmetros de autorização é, por definição, uma falha da aplicação/Authorization Server, não do usuário.* Confidence: média — mecanismo plausível e nomeado corretamente como classe de vulnerabilidade, mas sem relatório técnico do pentest disponível para verificação de detalhes (ex.: se era `scope` puro, `redirect_uri`, ou ambos). Ver [[wiki/concepts/oauth2]] e [[wiki/concepts/open-redirect]].
4. **Faturamento de R$ 4.819 em 15 dias via monetização de boost pago (destaque temporário na home), sem tráfego pago, funil ou copy de vendas — atribuído por hipótese do autor à visibilidade do canal (efeito novidade) mais que a growth hacking.** *Evidência: dashboard do List MRR (produto de terceiro, conectado via chave de leitura do Stripe), citado ao vivo no vídeo.* Ver [[wiki/concepts/produto-vendivel-desde-o-dia-zero]] e [[wiki/concepts/dev-e-negocio]].
5. **Tráfego majoritariamente orgânico: ~46% via vídeo do YouTube, 19% direto, 14% busca orgânica, resto via referral e redes sociais (7,9%, a menor fatia apesar de posts em X/LinkedIn/Instagram).** *Evidência: Google Analytics compartilhado publicamente no vídeo (build in public).* Ver [[wiki/concepts/marketing-organico-viral]].
6. **Metodologia declarada: Lean Startup na prática (build-measure-learn), priorizando execução sobre arquitetura ou escolha de stack "elegante".** Rejeitou sugestão não solicitada de reescrever o projeto em TypeScript, defendendo que trocar de stack por preferência alheia — sem justificativa técnica sólida — é um risco à execução. Ver [[wiki/concepts/lean-startup]] e [[wiki/concepts/escolha-de-stack]].
7. **Recomendação: para quem faz vibe coding sem saber programar, contratar um pentester antes de lançar é mais acessível que contratar um dev — cita o caso do Abraham (Cinema Hub), que deixou o `.env` exposto publicamente e teve a base de dados exportada por terceiros.**

## Entidades

- [[wiki/entities/mano-davin]] — autor, mesmo projeto (Find My SaaS) já coberto por [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]]
- [[wiki/entities/hostinger]] — provedora da VPS (1 vCPU/4GB/50GB)

## Conceitos

- [[wiki/concepts/mvp]] — VPS mínima como teste de resiliência do MVP
- [[wiki/concepts/over-engineering]] — recusa explícita de Kubernetes/microsserviços/event-driven para um projeto neste estágio
- [[wiki/concepts/lean-startup]] — build-measure-learn citado nominalmente
- [[wiki/concepts/waf]] — Cloudflare bloqueando tentativas maliciosas
- [[wiki/concepts/ddos-syn-flood]] — precursor ao incidente relatado em fonte posterior
- [[wiki/concepts/oauth2]] — vulnerabilidade central do pentest
- [[wiki/concepts/open-redirect]] — classe de vulnerabilidade adjacente (parâmetros de autorização não validados)
- [[wiki/concepts/marketing-organico-viral]] — breakdown de tráfego orgânico via Google Analytics
- [[wiki/concepts/produto-vendivel-desde-o-dia-zero]] — monetização via boost desde o lançamento
- [[wiki/concepts/hacker-mindset]] — "sempre vai ter alguém tentando hackear o que você faz"
- [[wiki/concepts/escolha-de-stack]] — recusa de reescrever em TypeScript por pressão externa
- [[wiki/concepts/especialista-de-powerpoint]] — feedback de quem nunca lançou nada, tratado como ruído

## Open Questions

- Detalhes técnicos exatos da vulnerabilidade de OAuth (qual parâmetro exato — `scope`, `redirect_uri`, ambos — e se PKCE estava em uso) não foram verificados contra um relatório de pentest formal; a explicação do autor é de segunda mão (repassada por quem encontrou a falha) e simplificada.
- Ano de gravação do vídeo não confirmado na transcrição (menção apenas a "dia 6 de abril").
- Não há confirmação externa (ex. logs brutos do Cloudflare) para os números de 230-234 mil requisições e 157 tentativas maliciosas — tratados como self-reported.
- Relação temporal exata entre esta fonte e [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]] (qual veio primeiro) inferida por contexto interno (esta fonte é "15 dias após o lançamento"; a outra descreve reconstrução total do servidor após incidente posterior), não por data de publicação confirmada — sinalizado para revisão se uma fonte futura esclarecer a ordem cronológica real.

## Quotes

> "Sempre vai ter alguém tentando hackear o que você faz. E eu falo sempre, é sempre."

> "A gente tem que tomar cuidado com esses especialistas em PowerPoint."

> "Pô, às vezes uma VPS bem configurada resolve o seu problema."

> "Feedback é um presente — você aceita ou não."

## Raw Source

[[raw/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]]
