---
type: concept
title: "Busca booleana de vagas"
aliases: ["boolean search de vagas", "busca booleana no LinkedIn", "Google dorks para vagas"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [carreira, busca-de-vagas, logica-booleana, linkedin, google]
skill: tech-mentor-leadership
status: stub
---

# Busca booleana de vagas

Usar os operadores da [[wiki/concepts/logica-booleana]] na busca, como os recrutadores fazem para achar candidatos, para achar vagas do seu perfil em vez de digitar "desenvolvedor Python" e receber anúncios genéricos ([[wiki/sources/onde-procurar-vagas-guia-definitivo]]).

## Operadores

- **AND, OR, NOT, aspas e parênteses**: `"desenvolvedor backend" AND (Python OR Go) AND (remoto OR remote)`.
- **No Google**: `site:` (domínio), `intitle:`, `inurl:`, `-` (exclui), `filetype:`. O Google indexa os sites das empresas, Gupy, Glassdoor e Indeed, cobrindo o que não está no [[wiki/entities/linkedin]].

## Práticas

- Aspas em cargos compostos; variações em inglês com OR.
- No LinkedIn, rodar a busca e afunilar com os filtros (Emprego, última semana, modo, nível, empresa).
- Mirar um site: `site:indeed.com` ou `site:linkedin.com` + (remote OR Latin America) + (Python OR Django OR FastAPI), demo de [[wiki/entities/augusto-galego]] ([[wiki/sources/onde-encontrar-vagas-workshop-roadmap-emprego-galego]]). O [[wiki/entities/lever]] é ruim de buscar no próprio site e bom via Google.
- Buscar **posts** em vez de vagas no LinkedIn (últimas 24 h) para chegar ao recrutador que postou, e falar com ele ([[wiki/concepts/networking-de-carreira]]).
- Google for Jobs: bloco agregador ativado por buscas como "vagas desenvolvedor fullstack remoto".

A variante voltada para os domínios dos ATS (Ashby, Greenhouse, Lever) está em [[wiki/concepts/busca-de-vagas-direto-no-ats]].

## Key Sources

- [[wiki/sources/onde-procurar-vagas-guia-definitivo]]: tabela de operadores, modelos para LinkedIn e Google
- [[wiki/sources/onde-encontrar-vagas-workshop-roadmap-emprego-galego]]: demo no Google com Indeed e LinkedIn, posts de recrutadores, Lever
