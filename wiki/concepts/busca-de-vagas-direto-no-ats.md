---
type: concept
title: "Busca de vagas direto no ATS"
aliases: ["hunting de vagas","job hunting fora do LinkedIn","site: ashby greenhouse lever","busca booleana"]
date_created: 2026-10-07
date_updated: 2026-11-16
source_count: 3
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

## Três categorias de vaga (Mapeando Vagas)

[[wiki/sources/introducao-mapeando-vagas]] divide a busca em buscadores (LinkedIn e outros), outsourcing e Big Techs, e manda buscar as Big Techs direto no site delas porque muitas não postam no LinkedIn. Converge com esta página: a vaga nasce no site/ATS da empresa.

## Key Sources

- [[wiki/sources/novos-cargos-ia-e-hunting-de-vagas-fora-do-linkedin]]
- [[wiki/sources/introducao-mapeando-vagas]] — Big Techs no próprio site; três categorias de vaga

## Complemento: busca por país (adição 2026-11-16)

[[wiki/sources/quais-paises-podem-fazer-sentido-vagas-internacionais-galego]] propõe outra alavanca contra a concorrência: em vez de sair do LinkedIn, filtrar países pouco procurados (Luxemburgo) e usar job boards nacionais de imigração (Work in Estonia, Work in Lithuania). Confirma que "Remote" costuma ser restrito ([[wiki/concepts/remoto-com-restricao-de-residencia]]) e acrescenta buscar o termo "contractor". As duas estratégias se somam.

- [[wiki/sources/quais-paises-podem-fazer-sentido-vagas-internacionais-galego]]

## Mesma técnica como "busca booleana"

[[wiki/sources/buscadores-e-outsourcing-galego]] chama de "busca booleana" o método para achar vagas no [[wiki/entities/lever]] fora do Brasil (a aula de busca booleana do curso não está na wiki). Ver também [[wiki/concepts/job-board]].

## Key sources (adição 2026-11-16)

- [[wiki/sources/buscadores-e-outsourcing-galego]]

## Mesma tática numa segunda fonte

[[wiki/sources/onde-encontrar-vagas-workshop-roadmap-emprego-galego]] chega ao mesmo método por outro caminho: busca booleana no Google com `site:` (Indeed, LinkedIn, `lever.co`), sem passar pela busca de cada plataforma. O PDF [[wiki/sources/onde-procurar-vagas-guia-definitivo]] acrescenta `intitle:`, `inurl:`, `filetype:` e o Google for Jobs. Ver [[wiki/concepts/busca-booleana-de-vagas]].

## Key sources (adição 2026-11-16)

- [[wiki/sources/onde-encontrar-vagas-workshop-roadmap-emprego-galego]]
- [[wiki/sources/onde-procurar-vagas-guia-definitivo]]
- [[wiki/sources/big-techs-salarios-vagas-processo-de-aplicacao]] — página de carreiras: filtro por país, várias vagas

## Página de carreiras da Big Tech (2026-11-16)

[[wiki/sources/big-techs-salarios-vagas-processo-de-aplicacao]]: buscar "<empresa> Careers" leva à página de vagas (Google Careers, jobs.netflix); filtrar por cargo e país (Software Engineer Brasil: 18 vagas na gravação) e ler qualificações mínimas e preferidas antes de aplicar para várias vagas ([[wiki/concepts/contratacao-por-time-em-big-tech]]).
