---
type: entity
title: "Renato Augusto"
aliases: ["Renato Augusto"]
date_created: 2026-06-05
date_updated: 2026-08-19
source_count: 13
tags: [design-patterns, oop, arquitetura, criador-de-conteudo, youtube, carreira, soft-skills, system-design, pos-graduacao]
skill: tech-mentor-backend
status: stub
---

# Renato Augusto

Desenvolvedor e criador de conteúdo brasileiro. Publica vídeos sobre padrões de projeto GoF e orientação a objetos, com foco em exemplos agnósticos de linguagem e framework aplicados a contextos web reais, além de conteúdo de carreira/soft skills e de system design (escalabilidade, load balancers) para programadores. Menciona o "Mapa do Arquiteto", seu produto de mentoria/roadmap de carreira para arquitetos de software.

## Key Sources

- [[sources/design-pattern-proxy]]
- [[wiki/sources/3-soft-skills-que-poucos-programadores-dominam]] — comunicação persuasiva, imagem profissional e habilidade de lidar com pessoas
- [[wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos]] — escalabilidade horizontal, tipos de load balancer, camadas OSI e algoritmos de balanceamento com demonstração prática em Nginx
- [[wiki/sources/design-pattern-adapter]] — Adapter Pattern com exemplo de troca de biblioteca de PDF (DomPDF → TCPDF), acoplamento, SRP e testabilidade
- [[wiki/sources/pos-graduacao-arquitetura-software-vale-a-pena]] — se vale a pena fazer pós-graduação em arquitetura de software; primeira menção explícita do "Mapa do Arquiteto" como produto próprio dentro de uma fonte
- [[wiki/sources/design-pattern-facade-renato-augusto]] — Facade Pattern com exemplo de OrderController/OrderFacade num e-commerce; defende que a Facade não fere o SRP por operar num nível de abstração diferente das classes de serviço que orquestra
- [[wiki/sources/full-text-search-mysql-postgresql]] — Full-Text Search em MySQL e PostgreSQL, demonstração prática de `LIKE` vs. índice invertido com DBeaver
- [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] — continuação da playlist de System Design: sharding/fragmentação de bancos de dados, shard key, hash-based vs. range-based, consistent hashing, problema da celebridade, Saga pattern e relação com DDD/microsserviços
- [[wiki/sources/design-pattern-decorator-renato-augusto]] — Decorator Pattern com pipeline de `ImageProcessor` (básico → marca d'água → resize); ensina composição recursiva, ancora no Open/Closed Principle e contrasta com Chain of Responsibility
- [[wiki/sources/como-nunca-mais-esquecer-o-que-voce-estuda-programacao]] — por que se esquece o que se estuda (homeostase sináptica), necessidade como gatilho de aprendizado, o conceito de "projeto impossível" e a regra dos 80% de tempo em fundamentos; primeira fonte de conteúdo de carreira/aprendizado (não técnico-específico) deste autor na wiki
- [[wiki/sources/microsservicos-monolito-first-renato-augusto]] — por que não começar um projeto com microsserviços (complexidade sistêmica, escala de times, falta de conhecimento de domínio), DDD/bounded context como resposta, princípio Monolith First de Fowler, caso Amazon Prime Video; primeira fonte deste autor cruzando DDD + monolito modular + microsserviços de forma integrada
- [[wiki/sources/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto]] — autoria inferida (não confirmada explicitamente na transcrição, ver open questions da fonte); arquitetura de placar de futebol em tempo real estilo Google com event sourcing, fundamentos de Kafka (partições, consumer groups, hash murmur, offset commit, rebalance), cache pré-computado no Redis e tempo real via SSE + Redis Pub/Sub; fonte mais tecnicamente densa deste autor na wiki até agora
- [[wiki/sources/world-cup-system-design]] — slide deck (PDF exportado de board Miro) da mesma aula acima, mesma inferência de autoria; contratos de API, taxonomia de eventos, schemas JSON e SQL concretos que a transcrição não capturava, e um quinto gatilho de escala (atender todos os campeonatos do mundo)
