---
type: source
title: "Novos cargos pós-IA e hunting de vagas fora do LinkedIn"
aliases: ["hunting de vagas ATS","vagas na gringa Ashby Greenhouse Lever","novos cargos IA"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_count: 1
tags: [tech-mentor-leadership, tech-mentor-ai, carreira, mercado-de-trabalho, busca-de-vagas, ats, forward-deployed-engineer, agent-engineer, ai-engineer, design-engineer]
skill: tech-mentor-leadership
status: draft
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/novos-cargos-ia-e-hunting-de-vagas-fora-do-linkedin.md
source_url:
author: "Ana (sobrenome e canal não identificados na transcrição)"
date_published:
date_ingested: 2026-10-07
---

## TL;DR

Vídeo em duas partes. (1) Mapa dos cargos que "se ramificaram" do software engineer com a IA — [[wiki/concepts/forward-deployed-engineer]], [[wiki/concepts/ai-engineer]], [[wiki/concepts/agent-engineer]] e [[wiki/concepts/design-engineer]] — contra o "dev genérico" (vagas em queda) e o dev que resolve problemas ponta a ponta (vagas em alta). (2) Método prático de busca: o [[wiki/entities/linkedin]] é o último lugar onde a vaga chega e o primeiro onde a concorrência chega; a vaga nasce no [[wiki/concepts/applicant-tracking-system]] ([[wiki/entities/ashby]], [[wiki/entities/greenhouse]], [[wiki/entities/lever]]), então busque direto lá com `site:` e APIs JSON públicas — ver [[wiki/concepts/busca-de-vagas-direto-no-ats]], [[wiki/concepts/cacar-a-empresa-nao-a-vaga]], [[wiki/concepts/sinais-de-vaga-real-vs-fantasma]] e [[wiki/concepts/fragmentacao-de-titulos-de-cargos-ia]].

Contexto: a autora trabalha há ~2 anos com clientes americanos. Tudo abaixo é relato dela `[external, não verificado]` — os percentuais não trazem fonte na transcrição.

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| Vagas de "dev genérico" (ecossistema único, ticket de uma camada) caíram ~50%; vagas de dev que usa IA e resolve problemas cresceram ~59% | Números ditos sem fonte (link "na descrição", ausente) | Baixa |
| Forward Deployed Engineer foi o cargo que mais cresceu, sobretudo em 2026 | Pesquisa própria, sem dado na transcrição | Baixa — **conflita** com [[wiki/questions/forward-deployed-engineer-demanda-crescendo-vs-pequena]] |
| Agent Engineer cresceu >280% | Idem | Baixa |
| AI Engineer (produtos/modelos) exige aprofundamento em ML | Opinião | Média (concorda parcialmente com [[wiki/sources/ai-engineer-forward-deployed-engineer-mercado-vagas-2026]] sobre o escopo) |
| Design não acabou: vira design system + código; front especialista monta o ecossistema (Storybook) para o design prototipar com IA | Opinião/experiência | Média |
| A vaga nasce no ATS e só depois chega ao LinkedIn (atraso, volume, vagas fantasmas, filtro `remote` = remoto nos EUA) | Experiência; mecanismo plausível | Média |
| Ashby, Greenhouse e Lever têm APIs públicas sem autenticação com JSON; `includeCompensation=true` no Ashby traz a faixa salarial | Demonstrado ao vivo no vídeo | Média-alta (verificável) |
| Faixa salarial publicada ⇒ vaga real/recente (leis dos EUA obrigam a exibir) | Afirmação dela | Média — a obrigação varia por estado `[external, não verificado]` |

## Conceitos

- [[wiki/concepts/busca-de-vagas-direto-no-ats]] — método `site:` + APIs + agente
- [[wiki/concepts/applicant-tracking-system]]
- [[wiki/concepts/cacar-a-empresa-nao-a-vaga]] — 30–50 empresas-alvo, 3–4 currículos
- [[wiki/concepts/sinais-de-vaga-real-vs-fantasma]]
- [[wiki/concepts/fragmentacao-de-titulos-de-cargos-ia]]
- [[wiki/concepts/autonomia-de-sugerir-vs-pegar-para-si]] — resolver ponta a ponta sem invadir escopo
- [[wiki/concepts/forward-deployed-engineer]], [[wiki/concepts/ai-engineer]], [[wiki/concepts/agent-engineer]], [[wiki/concepts/design-engineer]], [[wiki/concepts/product-engineer]]
- [[wiki/concepts/novo-perfil-dev-ia]], [[wiki/concepts/ciclo-de-mercado-tech]] (defasagem EUA → Brasil), [[wiki/concepts/curriculo-vs-portfolio]], [[wiki/concepts/networking-de-carreira]], [[wiki/concepts/model-context-protocol]], [[wiki/concepts/skills-agente]]

## Entidades

[[wiki/entities/ashby]], [[wiki/entities/greenhouse]], [[wiki/entities/lever]], [[wiki/entities/y-combinator]], [[wiki/entities/linkedin]], [[wiki/entities/figma]], [[wiki/entities/claude-code]], [[wiki/entities/openai]]. Também citados sem página: Coders (mentoria patrocinadora do vídeo), Codex, Google Alerts, n8n, Storybook, Claude Design.

## Open Questions

- Fonte dos percentuais (-50%, +59%, +280%) e do "crescimento absurdo" de FDE em 2026 — ver [[wiki/questions/forward-deployed-engineer-demanda-crescendo-vs-pequena]].
- Endpoints exatos das APIs (só descritos oralmente; Lever "um pouco diferente") — validar nas docs oficiais antes de automatizar `[external]`.
- Termos ASR incertos: "Laurer" (empresa do exemplo, possivelmente Lever?), "Scally Draw" (provavelmente Excalidraw), "dearremote.com" (possivelmente Deel/Remote.com).
- Aplicar em massa nos ATS ignora o risco de ser filtrado pelo próprio ATS e a ética/limites de scraping — não discutido.

## Quotes

> "O LinkedIn é o último lugar onde a vaga chega e o primeiro onde a concorrência chega."

> "Quando você caça a empresa, você sabe onde a vaga vai nascer antes dela existir."

> "Você não é uma pessoa que executa um ticket de uma camada só" (paráfrase do contraste dev genérico × dev que resolve o problema).
