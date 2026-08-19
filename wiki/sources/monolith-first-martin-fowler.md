---
type: source
title: "Monolith First (Martin Fowler)"
aliases: ["monolith first bliki", "monolith first original", "martinfowler.com/bliki/monolithfirst"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/monolith-first-martin-fowler.md
source_url: "https://martinfowler.com/bliki/MonolithFirst.html"
author: "Martin Fowler"
date_published: 2015-06-03
date_ingested: 2026-08-18
source_count: 0
tags: [monolito, monolito-modular, microsservicos, martin-fowler, arquitetura, yagni, bounded-context, sacrificial-architecture]
skill: tech-mentor-backend
status: stable
---

# Monolith First (Martin Fowler)

## TL;DR

Fonte primária do bliki de 2015 em que Fowler nomeia o princípio **Monolith First**: não comece um projeto novo com microsserviços, mesmo com certeza de que ele vai crescer o suficiente para justificar essa arquitetura mais tarde. A tese parte de um padrão observado — quase toda história de microsserviços bem-sucedida começou como monolito que cresceu e foi quebrado; quase todo sistema que nasceu já distribuído teve sérios problemas — e a sustenta com dois argumentos: [[wiki/concepts/yagni|YAGNI]] (você ainda não sabe se a aplicação será útil, e o "MicroservicePremium" é um peso desnecessário nessa fase) e a dificuldade de acertar [[wiki/concepts/bounded-context|BoundedContexts]] logo no início, mesmo para arquitetos experientes. Esta ingestão confirma e substitui, como fonte primária, o relato de segunda mão que já estava registrado via [[wiki/sources/microsservicos-monolito-first-renato-augusto]].

## Key Claims

- **Padrão observado por Fowler**: quase todas as histórias de sucesso com microsserviços começaram com um monolito que cresceu e foi quebrado depois; quase todos os sistemas construídos como microsserviços desde o zero, dos quais ele ouviu falar, acabaram em sérios problemas. É a base empírica (anedotal, o próprio Fowler admite isso no fechamento do artigo) de todo o argumento.
- **MicroservicePremium**: mesmo defensores de microsserviços reconhecem um "prêmio" — o custo de gerenciar um conjunto de serviços — que só compensa em sistemas mais complexos; para aplicações simples, esse prêmio favorece o monolito.
- **Argumento 1 — YAGNI**: no início de uma aplicação nova, não há certeza de que ela será útil; a melhor forma de descobrir isso costuma ser construir uma versão simples e testar. Nessa fase prioriza-se velocidade de ciclo de feedback, e o prêmio de microsserviços é um peso a evitar. → [[wiki/concepts/yagni]]
- **Argumento 2 — dificuldade de BoundedContexts**: microsserviços só funcionam bem com fronteiras de serviço boas e estáveis; refatorar funcionalidade entre serviços é muito mais difícil do que num monolito. Mesmo arquitetos experientes em domínios familiares erram as fronteiras no início. Construir o monolito primeiro dá tempo de descobrir as fronteiras certas antes de "uma camada de piche" (o design distribuído) travá-las, e de desenvolver os "MicroservicePrerequisites" necessários para serviços mais granulares. → [[wiki/concepts/bounded-context]]
- **Quatro caminhos práticos de execução da estratégia**, citados por Fowler como observação de campo, não como receita única: (1) desenhar um monolito modular com cuidado desde o início e migrar depois — ele diz explicitamente que confiaria mais nisso se tivesse ouvido mais histórias de sucesso reais; (2) começar com monolito e ir descascando microsserviços nas bordas gradualmente, deixando um monolito residual relativamente quieto no centro; (3) tratar o monolito como [[wiki/concepts/arquitetura-de-sacrificio|SacrificialArchitecture]] — construí-lo sabendo que será substituído por inteiro, sem vergonha nisso, se ele acelerar a chegada ao mercado; (4) começar com poucos serviços de granulação grossa (o "duolith" da nota de rodapé), maiores do que os serviços finais esperados, para reduzir refatoração entre serviços enquanto as fronteiras ainda não estão estáveis.
- **Contra-argumento reconhecido explicitamente**: começar direto com microsserviços acostuma o time ao ritmo de desenvolvimento distribuído desde cedo e facilita escalar o esforço com times separados por fronteira de serviço — especialmente viável em substituições de sistemas existentes, onde as fronteiras já são mais conhecidas. Fowler qualifica isso com uma condição: só faz sentido começar direto com microsserviços se o time já tem experiência razoável construindo sistemas de microsserviços.
- **Postura epistêmica do próprio autor**: Fowler encerra o artigo dizendo que não tinha, em 2015, anedotas suficientes para uma posição firme — "dias iniciais em microsserviços" — e que qualquer conselho sobre o tema deveria ser visto como tentativo, por mais confiante que soe o argumento.

## Entities

[[wiki/entities/martin-fowler]]

## Concepts

[[wiki/concepts/monolith-first]] · [[wiki/concepts/yagni]] · [[wiki/concepts/bounded-context]] · [[wiki/concepts/arquitetura-de-sacrificio]] · [[wiki/concepts/monolito]] · [[wiki/concepts/monolito-modular]] · [[wiki/concepts/microsservicos]] · [[wiki/concepts/microservice-premium]]

## Relação com a fonte secundária já ingerida

[[wiki/sources/microsservicos-monolito-first-renato-augusto]] já havia parafraseado este artigo (incluindo a imagem dos "dois caminhos" com dragões) sem link direto, e sua open question #3 sinalizava explicitamente a falta da fonte primária. Esta ingestão confirma a paráfrase como fiel ao original em todos os pontos centrais (as duas percepções, YAGNI, dificuldade de bounded contexts, a imagem dos dois caminhos) e acrescenta conteúdo que a fonte secundária não cobria: o termo formal **MicroservicePremium**, os quatro caminhos práticos de execução (a fonte secundária só descrevia o "monolito modular" como caminho), o "duolith" da nota de rodapé, e o contra-argumento a favor de começar direto com microsserviços em substituições de sistema — nenhum desses aparecia na transcrição de Renato Augusto.

## Open Questions

- O artigo cita "Sam Newman describes a case study" como leitura adicional, com link para `samnewman.io` — não seguido nesta ingestão; candidato a fonte própria se o case study for relevante o suficiente para justificar ingestão isolada.
- Os termos `MicroservicePrerequisites` e o "duolith" da nota de rodapé 2 são mencionados de forma breve no artigo original e não têm página própria na wiki — tratados aqui apenas como menção dentro desta fonte, não como stubs, por falta de profundidade suficiente para justificar uma página isolada.

## Raw Quotes

> "Almost all the successful microservice stories have started with a monolith that got too big and was broken up."

> "you shouldn't start a new project with microservices, even if you're sure your application will be big enough to make it worthwhile."

> "By building a monolith first, you can figure out what the right boundaries are, before a microservices design brushes a layer of treacle over them."

*(Tradução completa em `raw/monolith-first-martin-fowler.md`; para o texto exato em inglês, ver `source_url`.)*
