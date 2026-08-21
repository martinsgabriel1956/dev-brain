---
type: entity
title: "HostGator"
aliases: ["HostGator", "HostGator VPS"]
date_created: 2026-07-20
date_updated: 2026-08-17
source_count: 3
tags: [empresa, hosting, vps, infra, patrocinio]
skill: tech-mentor-infra
status: stub
---

# HostGator

Provedora de hospedagem/VPS, patrocinadora da demo de [[wiki/concepts/blue-green-deploy|deploy blue/green]] de [[wiki/entities/augusto-galego]]. Oferece planos de VPS com servidores localizados no Brasil (latência menor para público local) e terminal web integrado além de acesso via SSH.

## Contexto de uso na demo

- Plano de VPS mais barato usado como ambiente de teste — suficiente para rodar [[wiki/concepts/reverse-proxy|Nginx]] + duas instâncias Node em paralelo.
- Apresentado como opção viável tanto para aprendizado quanto para produção real (SaaS/site próprio), com upgrade de plano disponível se a carga crescer.

## Segunda Aparição: Deploy Contínuo via SSH e VPS com Claude Code Pré-instalado

Citada novamente (bloco patrocinado) em [[wiki/sources/continuous-integration-delivery-deploy-vs-release]], desta vez como alvo de deploy contínuo via GitHub Actions + SSH, não deploy manual blue/green. Planos a partir de R$ 21,70/mês, servidores em São Paulo, opções de OS (Ubuntu, Alma Linux, Rocky Linux, com/sem cPanel) e instaladores prontos para N8N, WordPress, Docker. Destaque adicional: oferta de VPS com [[wiki/entities/claude-code]] pré-instalado, promovida como alternativa a manter o computador local sempre ligado. *Nota de desambiguação:* não confundir com [[wiki/entities/hostinger]], provedora de VPS diferente já documentada em outras fontes da wiki — risco de confusão de nome, já que a transcrição desta fonte grafa o nome como "Host Gator" (dois termos), possível artefato de transcrição automática.

## Terceira Aparição: "Allstack" — Agregador de Assinaturas de IA

Citada em [[wiki/sources/leetcode-system-design-entrevista-versus-trabalho-real-na-era-da-ia]] como patrocinadora de um produto novo, "Allstack" (nome falado, grafia não confirmada): passe único que centraliza várias assinaturas de IA (chat com roteamento entre modelos como Claude, GPT, Gemini, Grok, e agentes pré-configurados ou customizáveis), com planos diferenciados incluindo um foco em privacidade/modo anônimo. Proposta de valor: reduzir troca de contexto e custo agregando assinaturas num único lugar.

## Key Sources

- [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]]
- [[wiki/sources/continuous-integration-delivery-deploy-vs-release]] — segunda aparição, agora como alvo de deploy contínuo via GitHub Actions; oferta de VPS com Claude Code pré-instalado
- [[wiki/sources/leetcode-system-design-entrevista-versus-trabalho-real-na-era-da-ia]] — terceira aparição, produto "Allstack" de agregação de assinaturas de IA
