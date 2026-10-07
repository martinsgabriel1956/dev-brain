---
type: concept
title: "Busca de vagas direto no ATS"
aliases: ["hunting de vagas","job hunting fora do LinkedIn","site: ashby greenhouse lever"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_count: 1
tags: [carreira, busca-de-vagas, ats, mercado-internacional, automacao]
skill: tech-mentor-leadership
status: draft
---

# Busca de vagas direto no ATS

Em vez de esperar a vaga aparecer no [[wiki/entities/linkedin]], buscar no [[wiki/concepts/applicant-tracking-system]] onde ela nasce. Segundo [[wiki/sources/novos-cargos-ia-e-hunting-de-vagas-fora-do-linkedin]]:

1. **Por que não só LinkedIn:** atraso de republicação, centenas de candidatos quando chega ao feed (candidatura fácil), vagas fantasmas que ninguém fechou, e filtro `remote` que costuma significar "remoto nos EUA".
2. **Google com `site:`** nos domínios de [[wiki/entities/ashby]], [[wiki/entities/greenhouse]] e [[wiki/entities/lever]] + título do cargo entre aspas, filtrando a última semana; combinar os três com `OR`; ignorar resultados patrocinados. Operador negativo/positivo com frases como `"must be authorized to work in"` serve para excluir (ou localizar) vagas só-EUA.
3. **APIs públicas sem autenticação** devolvem JSON — fácil de consumir por agente. No Ashby, `includeCompensation=true` traz a faixa salarial. `[external]` Endpoints exatos devem ser conferidos nas docs de cada ATS.
4. **Agente especialista** com os objetivos de carreira rodando a query diariamente (ou Google Alerts) e avisando quando surgir vaga do perfil.
5. **Títulos fragmentados:** buscar um nome por vez — ver [[wiki/concepts/fragmentacao-de-titulos-de-cargos-ia]].
6. **Depois da vaga:** achar o recruiter no LinkedIn e mandar mensagem ([[wiki/concepts/networking-de-carreira]]); triagem pelos [[wiki/concepts/sinais-de-vaga-real-vs-fantasma]].

Estratégia mais ampla: [[wiki/concepts/cacar-a-empresa-nao-a-vaga]].

## Key Sources

- [[wiki/sources/novos-cargos-ia-e-hunting-de-vagas-fora-do-linkedin]]
