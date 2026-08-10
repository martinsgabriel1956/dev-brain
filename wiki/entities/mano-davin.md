---
type: entity
title: "Mano Davin (Find My SaaS)"
aliases: ["davin", "mano davin", "find my saas", "manodeivin"]
date_created: 2026-07-31
date_updated: 2026-08-06
source_count: 2
tags: [criador-conteudo, youtube, saas, seguranca, devops, indie-hacker, lean-startup]
skill: tech-mentor-security
status: draft
---

# Mano Davin (Find My SaaS)

Criador de conteúdo de tecnologia no YouTube (canal descrito como "o canal mais chorume de tecnologia do YouTube", com lives regulares terças e quintas 10h; Instagram @manodeivin), autor e operador do SaaS "Find My SaaS" (findmysas.com — marketplace de upvote/boost para outros SaaS, "mercadão de Madureira do SaaS"). Trata conteúdo técnico com forte foco recente em segurança — vazamentos de empresas, vulnerabilidades em ferramentas populares — descrito como "novo hiperfoco" do canal.

## 15 dias após o lançamento

Em [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]] — cronologicamente anterior ao incidente de SYN flood abaixo — narra o balanço dos primeiros 15 dias do Find My SaaS: 12 mil usuários via Google Analytics, 646 SaaS cadastrados organicamente, R$ 4.819 de faturamento (via boost pago, sem tráfego pago), 230 mil+ requisições recebidas contra uma VPS [[wiki/entities/hostinger|Hostinger]] de 1 vCPU/4GB rodando um monolito sem [[wiki/concepts/over-engineering|Kubernetes ou microsserviços]], e 157 tentativas maliciosas bloqueadas pelo [[wiki/concepts/waf|Cloudflare]] — sem incidente grave nesse momento. Um pentest voluntário de um inscrito (Márcio Mendes) encontrou 12 vulnerabilidades, incluindo uma falha crítica de [[wiki/concepts/oauth2|OAuth]] (parâmetros de escopo/permissão aceitos sem validação via URL no login com Google). Declara seguir a metodologia [[wiki/concepts/lean-startup|Lean Startup]] (build-measure-learn) e rejeita pressão de "especialistas de PowerPoint" para adicionar features ou trocar de stack sem justificativa técnica — ver [[wiki/concepts/especialista-de-powerpoint]].

## Incidente relatado (SYN flood)

Em [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]], narra em primeira pessoa um ataque de [[wiki/concepts/ddos-syn-flood|SYN flood]] de 260 milhões de requests em um dia contra o próprio Find My SaaS — 6 horas de indisponibilidade, servidor não recuperado (reconstruído do zero), causado pela combinação de modo Under Attack desativado no [[wiki/concepts/waf|Cloudflare]] com um bug de CPU/memory leak no Traefik (auto-atualizado pelo [[wiki/concepts/coolify]]). Usou [[wiki/entities/hostinger]] como provedora de VPS antes e depois do incidente — este incidente ocorre depois do modo Under Attack já ter sido eficaz na fonte anterior, indicando que a configuração de segurança do Cloudflare pode ter sido desativada ou mudada em algum ponto entre as duas fontes (não esclarecido em nenhuma das duas transcrições).

## Key Sources

- [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]]
- [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]]
