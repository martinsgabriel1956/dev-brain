---
type: concept
title: "Monolito"
aliases: ["monolito", "monolith", "monolito tradicional"]
date_created: 2026-08-10
date_updated: 2026-09-03
source_count: 6
tags: [monolito, arquitetura, deploy, mvp, backend]
skill: tech-mentor-backend
status: stub
---

# Monolito

Aplicação entregue como **um único artefato**, com deploy único, geralmente um repositório, uma versão e (tradicionalmente) uma equipe. Módulos e domínios (produtos, users, pagamentos, hotéis...) coexistem no mesmo processo e comunicam-se por **chamadas de função** diretas.

## Vantagens

Simplicidade: sem APIs entre serviços, sem comunicação via protocolos de rede (que adicionam latência e complexidade), sem orquestração mirabolante de deploys. Um deploy só — não há o problema de versões divergentes entre serviços.

## Deploy Único: Cadência Cai Conforme o Time Cresce

[[wiki/sources/arquitetura-monolitica-vantagens-desvantagens]] detalha um mecanismo pouco explorado nas outras fontes: o artefato único não é só "mais simples de atualizar" — ele também **limita a frequência** de deploy conforme o número de desenvolvedores cresce (a fonte cita >15 devs como ponto de dor). Como não dá pra fazer deploy de um módulo isolado, times acabam amarrados a uma esteira coordenada (ex.: um dia fixo por semana) mesmo usando ferramentas ágeis (sprints). É o mesmo trade-off que justifica extrair um módulo para [[wiki/concepts/microsservicos|microsserviço]] quando ele precisa de deploy independente — ver critério em [[wiki/concepts/microsservicos]].

## SPOF de Módulo, Não Só de Servidor

Além do servidor único ser [[wiki/concepts/single-point-of-failure|SPOF]] físico, [[wiki/sources/arquitetura-monolitica-vantagens-desvantagens]] nomeia o caso de **falha lógica**: um bug numa nova versão de um módulo (ex.: estoque) pode derrubar toda a aplicação, incluindo módulos não relacionados (vendas) — porque todos compartilham processo e deploy. É o mesmo conceito de SPOF aplicado à camada de código, não à infraestrutura.

## Risco

Sem disciplina de fronteiras, o monolito cresce de forma desorganizada — uma função chamando outra em cadeia — e degenera em [[wiki/concepts/code-espaguete]] / projeto legado. As saídas discutidas são melhorar o monolito, evoluir para [[wiki/concepts/monolito-modular]], ou migrar para [[wiki/concepts/microsservicos]].

## Quando basta

Monolitos levam MVPs muito longe. Exemplo citado: produtos solo do Pieter Levels, todos monolitos, faturando milhões — com ~1M de usuários basta rodar em 3-4 máquinas com load balancer e réplica de banco ([[wiki/concepts/escalabilidade-horizontal]]). Ver [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]].

## Caso Real: Amazon Prime Video

[[wiki/sources/microsservicos-monolito-first-renato-augusto]] cita a migração (reportada publicamente, sem link primário nesta fonte) de parte do sistema do Amazon Prime Video de microsserviços/serverless distribuído de volta para um monolito, reduzindo custos de infraestrutura AWS em mais de 90%, com menor complexidade sistêmica e mais eficiência operacional. É o exemplo concreto usado para argumentar que mesmo empresas do porte da Amazon reavaliam microsserviços quando o custo operacional supera o benefício de escalabilidade seletiva — reforça, com um case real de "big tech", o mesmo argumento central de [[wiki/concepts/microsservicos]] sobre o custo-benefício da decomposição prematura. Fica registrado como fato **[external]** não verificado diretamente (a fonte não linka o post técnico original da Amazon) — candidato a fonte própria se uma transcrição mais detalhada do caso for ingerida depois.

## Monolith First (Martin Fowler)

[[wiki/concepts/monolith-first]] é a formalização de Fowler do princípio "não comece um projeto novo com microsserviços": quase toda história de microsserviços bem-sucedida começou como monolito, quase todo sistema que nasceu já distribuído teve sérios problemas. A fonte primária, [[wiki/sources/monolith-first-martin-fowler]], sustenta isso com dois argumentos — [[wiki/concepts/yagni|YAGNI]] (o monolito evita o [[wiki/concepts/microservice-premium|MicroservicePremium]] enquanto ainda não se sabe se a aplicação será útil) e a dificuldade de acertar [[wiki/concepts/bounded-context|bounded contexts]] logo no início. Ver também [[wiki/sources/microsservicos-monolito-first-renato-augusto]].

## A Analogia do Canivete Suíço

[[wiki/sources/como-projetar-sistemas-encurtador-de-urls-passo-a-passo]] usa a imagem do canivete suíço para o monolito (uma unidade única concentrando tudo) contra a caixa de ferramentas dos microsserviços (peças especializadas e independentes) — aplicada a um encurtador de URL com proporção leitura:escrita de 100:1, onde a limitação central do monolito é não conseguir escalar seletivamente só o serviço de redirect. Ver [[wiki/concepts/microsservicos]] para o critério de decisão completo.

## Key sources

- [[wiki/sources/como-projetar-sistemas-encurtador-de-urls-passo-a-passo]] — analogia do canivete suíço (monolito) vs. caixa de ferramentas (microsserviços), aplicada à decisão prática de escalabilidade seletiva
- [[wiki/sources/monolith-first-martin-fowler]] — fonte primária: MicroservicePremium, YAGNI, dificuldade de bounded contexts, quatro caminhos práticos
- [[wiki/sources/microsservicos-monolito-first-renato-augusto]] — caso Amazon Prime Video, princípio Monolith First de Fowler
- [[wiki/sources/arquitetura-de-sacrificio]] — Fowler recomenda o monolito como a melhor *arquitetura de sacrifício* por padrão (microsserviços adicionam distribuição/assincronia cedo demais)
- [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]]
- [[wiki/sources/arquitetura-monolitica-vantagens-desvantagens]] — fonte introdutória: cadência de deploy caindo conforme o time cresce, SPOF de módulo (bug em estoque derruba vendas), reuso de código via classe compartilhada, custo operacional de escalar verticalmente um servidor único
