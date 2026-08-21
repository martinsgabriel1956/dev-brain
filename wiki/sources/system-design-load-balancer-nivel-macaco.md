---
type: source
title: "System Design — Load Balancer Explicado do Zero (Aula \"Nível Macaco\")"
aliases: ["aula load balancer fiascão", "load balancer nível macaco", "DNS decide a mesa, load balancer decide o garçom"]
date_created: 2026-08-19
date_updated: 2026-08-19
source_count: 0
tags: [load-balancer, dns, l4, l7, global-load-balancer, gateway-load-balancer, over-engineering, polyglot-persistence, system-design, infra]
skill: tech-mentor-infra
status: draft
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/system-design-load-balancer-nivel-macaco.md
source_url:
author:
date_published:
date_ingested: 2026-08-19
---

# System Design — Load Balancer Explicado do Zero (Aula "Nível Macaco")

## TL;DR

Aula introdutória de um curso de System Design, apresentada por um instrutor que se identifica como "Horácio Fiasco"/"Fiascão" (convidado por "Mateus Leandro"), demonstrando load balancer num simulador de servidor ao vivo. Progressão em três níveis: (1) poucos usuários, servidor único, sem necessidade de load balancer — introduzi-lo aqui seria over-engineering; (2) carga cresce, servidor único satura e falha ~30% das requisições, resolvido inserindo um load balancer com round robin na frente de múltiplos servidores; (3) taxonomia de tipos — L4 (cego ao conteúdo) vs. L7 (lê headers/cookies, roteia por rota autenticada), Global Load Balancer (roteia por geolocalização), Application Load Balancer vs. Gateway Load Balancer (políticas de segurança/firewall, ex. Cloudflare), e menção ao Ingress do Kubernetes. Fecha com um bloco de perguntas frequentes, com destaque para a distinção didática entre load balancer e DNS via analogia de restaurante.

## Key Claims

| Claim | Evidência |
|---|---|
| Com baixa complexidade, poucos usuários e latência baixa, não há necessidade de load balancer — introduzi-lo nesse cenário é over-engineering | Simulação nível 1: 200 usuários, 1 servidor, 1 banco, zero falhas, latência baixa |
| Um servidor único satura sob carga alta o suficiente, gerando falhas em cascata proporcionais ao excesso de carga | Simulação nível 2: 2.000 usuários contra 1 servidor único, ~30% de falha |
| Load balancer com round robin distribui requisições entre múltiplos servidores, eliminando as falhas observadas com servidor único, desde que haja servidores suficientes atrás dele | Simulação nível 2: 1→4 servidores atrás do LB elimina falhas; reduzir para 2 servidores as reintroduz |
| L4 roteia sem inspecionar conteúdo da requisição ("rota menos engarrafada"); L7 lê headers/cookies e roteia por tipo de requisição (ex.: rota autenticada) | Exemplos numéricos dados na aula (50/50 para L4; 99/1 para L7 com rota admin) |
| Global Load Balancer roteia por geolocalização do cliente, explicando tanto bloqueio de conteúdo por região (Netflix/YouTube) quanto variação de ping em jogos online por proximidade do servidor físico | Explicação dada com exemplos de VPN e servidores por capital/país |
| Gateway Load Balancer aplica políticas de segurança/firewall sobre o tráfego, com a Cloudflare citada como exemplo real desse tipo de comportamento | Afirmação do instrutor sem demonstração técnica no simulador |
| Load balancer e DNS não são a mesma coisa: DNS decide a rota (resolve nome → IP, sem saber se o destino está saudável); load balancer decide quem atende dentro da rota, verificando a saúde dos servidores (health check) antes de rotear | Analogia de restaurante ("DNS decide a mesa, load balancer decide o garçom") e explicação técnica dada na seção de perguntas frequentes |
| Múltiplos bancos de dados por sistema (leitura/escrita/consolidado, ou por tipo de dado — busca, eventos, cache) é prática comum em sistemas distribuídos — citado sob o termo "polyglot persistence" | Resposta à pergunta frequente 3, com exemplos (Elasticsearch para busca, Cassandra para eventos, Redis para cache) |
| Escalar não significa apenas adicionar mais servidores — cache é citada como técnica alternativa que evita bater repetidamente no servidor/banco de dados | Resposta à pergunta frequente 1 |
| Ter múltiplos load balancers é tecnicamente possível, mas o instrutor afirma nunca ter visto essa prática aplicada — opinião pessoal, não uma negação técnica fundamentada | Resposta à pergunta frequente 2 (confiança baixa, sem justificativa técnica dada) |

## Entidades

- Instrutor identificado apenas pelo apelido "Horácio Fiasco"/"Fiascão" — sem sobrenome, canal ou identidade confirmada na transcrição; nenhuma entidade de autoria foi criada nesta ingestão para não forçar atribuição não verificada (mesmo critério já aplicado em outras fontes sem autoria confirmada, ex. [[wiki/sources/unit-of-work-padrao-de-design]]).
- "Mateus Leandro", citado como quem convidou o instrutor para o curso — sem mais contexto na fonte para justificar página própria.

## Conceitos

- [[wiki/concepts/load-balancer]] — já cobre L4/L7, algoritmos e tipos com profundidade maior; esta fonte contribui a demonstração pedagógica em simulador nível a nível e a taxonomia Global/Gateway Load Balancer + Ingress citados de passagem
- [[wiki/concepts/dns]] — nova contribuição: a distinção didática LB vs. DNS via analogia de restaurante, com foco no health check como diferencial do load balancer
- [[wiki/concepts/over-engineering]] — nova contribuição: heurística concreta de "quando NÃO introduzir load balancer" (baixa complexidade, poucos usuários, latência baixa)
- [[wiki/concepts/escalabilidade-horizontal]] — já cobre extensivamente a mecânica de escalar com load balancer; esta fonte reforça com demonstração visual de saturação e recuperação passo a passo
- [[wiki/concepts/database-per-service]] — nova contribuição: exemplos concretos de polyglot persistence (leitura/escrita/consolidado; Elasticsearch/Cassandra/Redis)
- [[wiki/concepts/cache]] — cache citado como técnica alternativa a "só adicionar mais servidor" para escalar
- [[wiki/concepts/reverse-proxy]] — Nginx citado como ferramenta real de load balancer, sem detalhar a distinção reverse-proxy vs. load-balancer (já coberta em profundidade na página do conceito)

## Open Questions

- Afirmação "nunca vi múltiplos load balancers na prática" é opinião pessoal do instrutor, sem exemplo técnico contrário ou a favor — não é uma negação categórica e não deveria ser tratada como fato consolidado.
- Não há confirmação de identidade (nome completo, canal, curso) do instrutor nem de "Mateus Leandro" — impede checar se este é o mesmo "Mateus" citado alhures no wiki (ex. Mateus Guimarães, Mateus Castiglioni) ou uma pessoa distinta; tratado como pessoa não identificada.
- Gateway Load Balancer e Cloudflare são mencionados apenas como afirmação, sem demonstração técnica ou detalhamento de mecanismo — fica como lacuna a preencher com uma fonte futura mais técnica sobre Gateway Load Balancer especificamente.

## Key Sources

_Este é o documento primário._
