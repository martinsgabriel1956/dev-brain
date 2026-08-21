---
type: concept
title: "Arquitetura de Sacrifício"
aliases: ["sacrificial architecture", "arquitetura sacrificial", "arquitetura de sacrificio", "código descartável deliberado"]
date_created: 2026-08-10
date_updated: 2026-08-10
date_updated: 2026-08-18
source_count: 2
tags: [arquitetura, evolutionary-design, monolito, microsservicos, tech-debt, refatoracao, martin-fowler]
skill: tech-mentor-backend
status: draft
---

# Arquitetura de Sacrifício

## Definição

Uma **arquitetura de sacrifício** (termo de [[wiki/sources/arquitetura-de-sacrificio|Martin Fowler]], 2014) é aquela que você escolhe **deliberadamente** sabendo que, se o produto der certo, você vai **jogá-la fora** em alguns anos. A tese central inverte o instinto comum: descartar uma base de código **não é fracasso** — "frequentemente o melhor código que você consegue escrever hoje é um código que você vai descartar daqui a alguns anos". Software de vida curta ainda entrega muito valor; o sucesso pode ser construído sobre código já enviado ao `/dev/null`.

O motor por trás disso é o **crescimento exponencial**: a arquitetura certa para uma escala não é a certa para outra ordem de grandeza. A do eBay de 1996 (scripts Perl) não aguentaria 2006; a de 2006 seria complexa demais para as necessidades de 1996.

## Como se decide sacrificar

- **Cedo, priorize flexibilidade** sobre performance/escala. Você ainda não sabe o que o sistema precisa fazer — ter usuários demais numa base pouco performática é um problema melhor que o inverso. "Performance é uma feature" (Jeff Atwood) é trade-off, não prioridade absoluta.
- **Regra do "10×" (Google):** projete para 10× a necessidade atual; se ultrapassar uma ordem de grandeza, planeje reescrever do zero. Subsistemas são descartados a cada poucos anos.
- **Não sacrifique a qualidade interna.** Sacrificar qualidade interna morde antes da hora da substituição. Boa **modularidade** ([[wiki/concepts/monolito-modular]]) é o que permite, com o tempo, sacrificar **módulos individuais** em vez do sistema inteiro — só possível com boas fronteiras de módulo.
- **Cuidado com a contabilidade.** Amortização da base de código pode travar a substituição de um sistema inviável (problema típico de grandes empresas).
- **Features também podem ser sacrificiais.** Construa uma feature de forma descartável e libere-a a um subconjunto via [[wiki/concepts/feature-flag]] para validar antes de investir o esforço total.

## Monolito como arquitetura de sacrifício

Substituibilidade modular é argumento pró-[[wiki/concepts/microsservicos|microsserviços]], mas Fowler **desaconselha** microsserviços para uma arquitetura de sacrifício: eles implicam distribuição e assincronia — amplificadores de complexidade que desaceleram o pipeline de features quando adotados sem necessidade. O padrão recomendado é **[[wiki/concepts/monolito|monolito]] primeiro**, com microsserviços introduzidos depois para desmontá-lo gradualmente — essencialmente o [[wiki/concepts/strangler-fig-pattern]].

## Quem tem o direito de sacrificar

"O time que escreve a arquitetura de sacrifício é o time que decide que chegou a hora de sacrificá-la." É uma dinâmica muito diferente de um time novo que chega, **odeia** o código herdado e quer reescrevê-lo sem entender o contexto em que foi escrito. Sacrificar conscientemente o próprio código ≠ desprezar código alheio. Isso conecta com o risco de perda de contexto e reescrita big-bang descrito em [[wiki/concepts/ciclo-da-desgraca-software]].

## Relações

- [[wiki/concepts/tech-debt-como-ferramenta]] — sacrifício deliberado é dívida assumida com intenção, não negligência.
- [[wiki/concepts/over-engineering]] — priorizar flexibilidade cedo evita otimização prematura.
- [[wiki/concepts/refatoracao]] — substituição incremental de módulos como alternativa ao descarte total.
- [[wiki/concepts/ciclo-de-mudanca-de-arquitetura]] — o processo (AS-IS → TO-BE → POC → coexistência) pelo qual o sacrifício acontece sem virar reescrita big-bang.
- [[wiki/concepts/escalabilidade-horizontal]] — a escala que invalida a arquitetura inicial.
- [[wiki/concepts/application-boundary]] — fronteiras como construção social e técnica.

## Citada em Monolith First como um dos Caminhos Práticos

[[wiki/sources/monolith-first-martin-fowler]] cita explicitamente esta mesma ideia (`SacrificialArchitecture`) como um dos quatro caminhos práticos para executar a estratégia [[wiki/concepts/monolith-first]]: tratar o monolito inicial como descartável por inteiro, sem culpa nisso, se ele acelerar a chegada ao mercado — mesma tese central já registrada acima, aplicada especificamente à escolha monolito-vs-microsserviços do dia 1 de um projeto.

## Key Sources

- [[wiki/sources/monolith-first-martin-fowler]] — SacrificialArchitecture citada como um dos caminhos práticos do princípio Monolith First
- [[wiki/sources/arquitetura-de-sacrificio]] — artigo original de Martin Fowler (2014), com os casos eBay e Google.
