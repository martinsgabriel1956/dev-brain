---
type: entity
title: "Hostinger"
aliases: ["Hostinger VPS"]
date_created: 2026-07-21
date_updated: 2026-08-19
source_count: 7
tags: [tech-mentor-infra, vps, hosting, patrocinio, coolify]
skill: tech-mentor-ai
status: stub
---

# Hostinger

Provedora de VPS citada em bloco patrocinado de [[wiki/sources/hermes-agent-open-claw-learning-loop]]: permite configurar o servidor virtual livremente (instanciar com Debian, Open Claw, Claude Code etc., com ou sem painel), enquanto o servidor físico — proteção DDoS, firewall com IA, snapshots e backups semanais gratuitos, servidores distribuídos globalmente — fica a cargo da própria Hostinger. Tratado como conteúdo patrocinado, não como avaliação técnica independente; sem comparação com outras provedoras de VPS nesta fonte.

Também citada (novamente em bloco patrocinado) em [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]]: o autor usou o instalador de [[wiki/concepts/coolify]] com um clique da Hostinger tanto no servidor original quanto na VPS nova provisionada após o incidente de [[wiki/concepts/ddos-syn-flood|SYN flood]] — sem que isso implique que a Hostinger tenha alguma responsabilidade técnica no incidente (o bug era do Traefik/Coolify, na camada de software, não da VPS em si).

Citada também como **registrador de domínios** em [[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]]: é onde [[wiki/entities/fernanda-kipper]] mantém seus domínios mais novos (os antigos estão na [[wiki/entities/godaddy]]), e serve na fonte para mostrar a busca/compra de um [[wiki/concepts/dominio|domínio]] e a checagem de disponibilidade por TLD.

*Nota de desambiguação:* não confundir com [[wiki/entities/hostgator]], outra provedora de VPS brasileira patrocinadora de conteúdo técnico na wiki (ver [[wiki/sources/continuous-integration-delivery-deploy-vs-release]] e [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]]) — nomes parecidos, empresas diferentes.

Também citada (terceiro bloco patrocinado) em [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]]: usada para o deploy "com um clique" de um [[wiki/concepts/ai-gateway-llm-router|AI Gateway]] self-hosted (o "Nine Router", nome não confirmado) — mesmo padrão de "implantação com um clique" já citado como diferencial da Hostinger nas fontes anteriores, aplicado a uma ferramenta de proxy multi-provider de LLM em vez de a um app genérico.

Também citada (quarto bloco patrocinado, cronologicamente anterior ao incidente de SYN flood) em [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]]: nos primeiros 15 dias do Find My SaaS, a VPS Hostinger usada tinha apenas 1 vCPU, 4GB de RAM e 50GB de armazenamento — suficiente para sustentar 230 mil+ requisições, incluindo tentativas de ataque bloqueadas pelo Cloudflare, sem downtime nesse período.

Também citada (quinto bloco patrocinado) em [[wiki/sources/code-review-morreu-uncle-bob-push-force-prod-lucas-montano]], por [[wiki/entities/lucas-montano]]: plano **KVM2** (2 vCPU, 8 GB RAM, SSD, backups semanais grátis, firewall gerenciado), com o mesmo diferencial de "implantação com um clique" já citado nas fontes anteriores — aqui aplicado a [[wiki/entities/claude-code]], Codex CLI, N8N e Docker — além de instalar só o SO (Debian, Ubuntu, Alma/Arch Linux) e testar Odysseus/Hermes com um clique. Cupom "Lucas Montano". Conteúdo patrocinado, não avaliação técnica independente.

Também citada (sexto bloco patrocinado) em [[wiki/sources/ia-2026-nao-e-so-prompt-nem-so-agente-codigo-fonte-tv]]: reforça o padrão de deploy de um clique já documentado (Claude Code 24x7, Codex, n8n, Docker) e acrescenta produtos ainda não citados na wiki para a Hostinger — **Horizons** (criação de MVP com IA, com banco de dados, usado pelo canal num hackathon) e um **serviço de GPU em lista de espera** (treino/inferência de modelos). Cita também "openla" (nome provavelmente mal transcrito) e **Hermes Agent** como agentes disponíveis, e o **Dokploy** (não confundir com o Coolify já citado em fontes anteriores — são PaaS self-hosted distintos, ambos com deploy de um clique na Hostinger) como ferramenta usada pelo próprio canal para gerenciar containers.

## Key Sources

- [[wiki/sources/hermes-agent-open-claw-learning-loop]]
- [[wiki/sources/code-review-morreu-uncle-bob-push-force-prod-lucas-montano]] — plano KVM2, deploy de um clique de Claude Code/Codex CLI/N8N/Docker, cupom "Lucas Montano"
- [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]]
- [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]] — deploy de um clique de AI Gateway self-hosted (proxy multi-provider de LLM)
- [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]] — VPS mínima (1 vCPU/4GB/50GB) sustentando 230 mil+ requisições nos primeiros 15 dias do Find My SaaS
- [[wiki/sources/ia-2026-nao-e-so-prompt-nem-so-agente-codigo-fonte-tv]] — Horizons (MVP com IA), serviço de GPU em lista de espera, Hermes Agent, Dokploy
