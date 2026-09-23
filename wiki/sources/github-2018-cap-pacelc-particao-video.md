---
type: source
title: "GitHub 2018, CAP e PACELC (vídeo)"
aliases: ["github 2018 cap pacelc video", "incidente github 2018 video"]
date_created: 2026-09-23
date_updated: 2026-09-23
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/github-2018-cap-pacelc-video.md
source_url: ""
author: "não identificado (canal não citado na transcrição)"
date_published: ""
date_ingested: 2026-09-23
source_count: 0
tags: [system-design, sistemas-distribuidos, cap-theorem, pacelc, github, particao-de-rede, consistencia, latencia]
skill: tech-mentor-system-design
status: draft
---

# GitHub 2018, CAP e PACELC (vídeo)

## TL;DR

Vídeo de system design que usa o incidente do [[wiki/entities/github]] de outubro de 2018 ([[wiki/concepts/github-incidente-2018-particao-de-rede]]) para explicar o [[wiki/concepts/cap-theorem]]: a rede voltou em 43 s, mas o serviço só normalizou após mais de 24 h, porque os dois data centers aceitaram escritas divergentes ([[wiki/concepts/split-brain]]). Redefine "disponibilidade" como "todo nó vivo responde sem erro" ([[wiki/concepts/disponibilidade-no-teorema-cap]]), ilustra o dilema com agências de banco ([[wiki/concepts/analogia-agencias-bancarias-cap]]), mede localmente o custo de leitura local vs. forte ([[wiki/concepts/custo-da-leitura-forte-vs-local]]) e apresenta o [[wiki/concepts/pacelc]] como a escolha latência vs. consistência que existe *sem* partição. Cita duas [[wiki/concepts/falacias-da-computacao-distribuida]].

## Key Claims

- **A rede voltou em 43 s, o serviço em mais de 24 h.** Evidência: relato do autor sobre o incidente; a demora vem de reconciliar dados que existiam só de um lado. → [[wiki/concepts/github-incidente-2018-particao-de-rede]]
- **No CAP, "disponível" não é "no ar": é todo nó não-falho responder sem erro, inclusive o isolado.** Por essa definição o GitHub ficou disponível nas 24 h. → [[wiki/concepts/disponibilidade-no-teorema-cap]]
- **O dilema recusar vs. pagar com caixa local só existe com o canal fechado**, e o nó não distingue outro nó caído, lento ou incomunicável: tudo chega como silêncio. → [[wiki/concepts/analogia-agencias-bancarias-cap]]
- **Teste local (3 nós, 1 isolado):** escrita = 5 s de timeout e falha; leitura forte = falha; leitura local = resposta imediata com dado pré-partição. Sem partição: leitura local ≈ 0,05 ms; leitura forte ≈ +0,19 ms de round trip ao quórum. → [[wiki/concepts/custo-da-leitura-forte-vs-local]]
- **P não é opcional; na partição escolhe-se C ou A.** → [[wiki/concepts/cap-theorem]]
- **Sem partição ainda há escolha: latência ou consistência (PACELC), e é o caso comum.** O PACELC não invalida o CAP, adiciona uma camada. → [[wiki/concepts/pacelc]]
- **Falácias:** "a rede é confiável" e "a latência é zero". → [[wiki/concepts/falacias-da-computacao-distribuida]]
- **Ressalva do autor:** não reproduziu o cenário leste/oeste do GitHub (3 nós não formam maioria dos dois lados) e não mediu latência entre zonas/regiões.

## Entities

[[wiki/entities/github]]

## Concepts

[[wiki/concepts/cap-theorem]] · [[wiki/concepts/pacelc]] · [[wiki/concepts/split-brain]] · [[wiki/concepts/consistency-models]] · [[wiki/concepts/eventual-consistency]] · [[wiki/concepts/raft-paxos]] · [[wiki/concepts/alta-disponibilidade]] · [[wiki/concepts/github-incidente-2018-particao-de-rede]] · [[wiki/concepts/disponibilidade-no-teorema-cap]] · [[wiki/concepts/analogia-agencias-bancarias-cap]] · [[wiki/concepts/custo-da-leitura-forte-vs-local]] · [[wiki/concepts/falacias-da-computacao-distribuida]]

## Open Questions

- O relato do incidente é simplificado. [external] O post-mortem do GitHub descreve um failover automático de topologia MySQL (Orchestrator) para a costa oeste após ~43 s de perda de conectividade; **não foi verificado nesta sessão** (ver https://github.blog/news-insights/company-news/oct21-post-incident-analysis/).
- O autor diz que o GitHub "ficou no ar" e portanto "disponível" no sentido do CAP; na prática o serviço operou degradado (dados defasados, atrasos), o que mostra o quanto a definição formal difere da percepção do usuário.
- Os números (0,05 ms e 0,19 ms) vêm de um teste local sem rede real entre zonas; o próprio autor ressalva que não mediu zonas/regiões. Não generalizam.
- Qual banco/sistema foi usado no experimento não é dito na transcrição.
- Autor, canal e data desconhecidos.

## Raw Quotes

> "todo nó que não caiu ele precisa responder sem erro inclusive o nó ficou sozinho, do lado errado da partição"

> "a rede ela voltou em 43 segundos porém o serviço só voltou ao normal mais de 24 horas depois"

> "mesmo quando não há partição de rede ainda assim a gente tem um tradeoff que é justamente escolher entre latência e consistência"
