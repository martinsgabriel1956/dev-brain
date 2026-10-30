---
type: entity
title: "GitHub"
aliases: ["github.com"]
date_created: 2026-09-23
date_updated: 2026-10-30
source_count: 4
tags: [plataforma, git, incidente, sistemas-distribuidos, security]
skill: tech-mentor-system-design
status: stub
---

# GitHub

Plataforma de hospedagem de código. Na wiki aparece como estudo de caso de falha distribuída (o incidente de outubro de 2018, [[wiki/concepts/github-incidente-2018-particao-de-rede]]) e, mais recentemente, como alvo e ferramenta de segurança: a API de busca de código tem limites de indexação relevantes para secret scanning ([[wiki/concepts/github-search-api-limites]]), e a plataforma oferece defesas nativas contra vazamento de credenciais (push protection, GitHub Advanced Security — ver [[wiki/concepts/secret-scanning]]).

## Key sources

- [[wiki/sources/github-2018-cap-pacelc-particao-video]] — incidente de 2018 usado para explicar CAP/PACELC
- [[wiki/sources/dev-na-era-da-ia-qualidade-esteira-e-novas-preocupacoes]] — citado como ferramenta a aprender junto com a IA
- [[wiki/sources/secrets-vazadas-no-github-conceitos-e-riscos]] — limites técnicos da API de busca de código (indexação, teto de resultados) relevantes para a descoberta de secrets vazadas

## Key sources (adição 2026-10-30)

- [[wiki/sources/spec2cobolrot-envelhecer-cobol-com-ia-complexidade-vs-entropia-historica]] — hospeda os samples públicos do Spec2COBOLRot (jbespi/spec2cobolrot-samples)
