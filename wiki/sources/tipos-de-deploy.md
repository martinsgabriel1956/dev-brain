---
type: source
title: "Tipos de Deploy"
aliases: ["deploy vs release", "recreate rolling blue green canary shadow"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [devops, deploy, cicd, infra, feature-flags]
skill: tech-mentor-infra
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/tipos-de-deploy.md
source_url: ""
author: "canal de tecnologia (patrocinado por HostGator)"
date_published: 2026-07-09
date_ingested: 2026-07-09
status: stable
---

# Tipos de Deploy

## TL;DR

Deploy (código na máquina) é diferente de release (código visível/ativo para o usuário) — a distinção central do vídeo. Cobre deploy manual vs. automático (a diferença é o gatilho, não a ação), e seis estratégias de deploy: Recreate (downtime, shutdown+start), Rolling (substituição gradual, tráfego misto), Blue/Green (dois ambientes, troca atômica, rollback instantâneo), Canary (percentual gradual de tráfego, reduz risco técnico), A/B (percentual de tráfego, mas para validar hipótese de negócio, não risco técnico) e Shadow (tráfego real duplicado para v2 sem que nenhum usuário veja, validação com dados reais de produção). Fecha com Continuous Deployment como conceito ortogonal às estratégias, e uma nota sobre deploy em serverless (a cloud administra o "recreate instantâneo" ou blue/green por baixo dos panos).

## Key Claims

- **Deploy ≠ Release** — deploy é colocar o binário na máquina; release é o código afetar o usuário. Possível fazer deploy sem release via feature flag ou via duas instâncias com tráfego só na antiga. → [[concepts/deploy-vs-release]]
- **Deploy manual vs. automático** — a diferença não é o que é executado (pode ser o mesmo SSH + git pull + npm start), é o gatilho: manual é decisão humana pontual, automático é uma pipeline "triggada" por regra (ex.: merge na main). → [[concepts/ci-cd]]
- **Recreate** — desliga a instância antiga, sobe a nova na mesma porta; downtime inevitável na janela entre shutdown e start. Era a origem da "janela de manutenção". → [[concepts/recreate-deployment]]
- **Rolling** — substitui instâncias uma a uma; tráfego misto exige compatibilidade de API e de banco de dados entre v1 e v2. → [[concepts/rolling-update]]
- **Blue/Green** — vantagem central é rollback instantâneo porque a versão antiga continua rodando em paralelo; custo é manter as duas versões de pé. → [[concepts/blue-green-deploy]]
- **Canary** — percentual pequeno de usuários vê a versão nova para reduzir risco técnico; setup complexo e debugging fica obscuro quando só uma fração relata bug. → [[concepts/canary-release]]
- **A/B deployment** — mecanicamente parecido com Canary (split de tráfego), mas o objetivo é validar hipótese de negócio (ex.: qual checkout vende mais), não reduzir risco técnico. → [[concepts/ab-testing-deployment]]
- **Shadow deployment** — 100% do tráfego real é duplicado/replicado para v2, que processa em paralelo sem responder ao usuário; usado para validar a nova versão com tráfego de produção real antes do cutover. Complicado quando há side effects (envio de e-mail) ou escrita em banco de dados. → [[concepts/shadow-deployment]]
- **Continuous Deployment é ortogonal às estratégias** — toda mudança que passa nos testes é deployada continuamente, mas qual estratégia (Recreate/Rolling/Blue-Green/Canary) é usada para isso é uma decisão separada. → [[concepts/ci-cd]]
- **Serverless tende a Recreate/Blue-Green invisível** — a cloud troca o roteamento por baixo dos panos; nada impede configurar Canary/A/B manualmente, mas serviços simples geralmente ficam no padrão da plataforma.

## Entities

(nenhuma entidade nova — canal e patrocinador não promovidos a página própria por serem conteúdo publicitário pontual)

## Concepts

[[concepts/deploy-vs-release]] · [[concepts/recreate-deployment]] · [[concepts/rolling-update]] · [[concepts/blue-green-deploy]] · [[concepts/canary-release]] · [[concepts/ab-testing-deployment]] · [[concepts/shadow-deployment]] · [[concepts/feature-flags]] · [[concepts/ci-cd]] · [[concepts/deploy-strategies]] · [[concepts/zero-downtime-deploy]]

## Open Questions

- Shadow deployment com side effects (e-mail, escrita em banco) — o vídeo levanta o problema mas não resolve: duplicar o banco? mockar escrita? Fica em aberto.
- Como Canary com múltiplos serviços dependentes coordena percentual entre eles — mesma questão já aberta em [[sources/blue-green-canary-rolling]], reforçada aqui.

## Raw Quotes

> "Você consegue fazer um deploy sem fazer um release: você consegue lançar o código pra máquina sem que esse código afete os usuários."

> "A diferença entre um deploy manual e um automático não é o que está sendo feito — a diferença é qual o trigger, qual o gatilho para causar esse deploy."

> "Canary é sobre reduzir risco... o AB é sobre ver se, de repente, a gente implementou um checkout novo, esse checkout novo vende mais."

> "Você tá validando o seu V2 com clones do tráfego real."

## Notas de Ingestão

Transcrição em português, sem necessidade de tradução — texto de origem já veio em pt-BR (fala de um canal brasileiro de tecnologia). Bloco publicitário do patrocinador (HostGator/VPS) preservado de forma resumida no `raw/` por fazer parte do fluxo natural da fala, mas não gerou entidade nem claim técnico na wiki — tratado como ruído comercial, não conteúdo técnico. Vídeo é uma aula introdutória sem fontes primárias citadas (nenhum paper, nenhuma doc oficial referenciada) — tratado como conteúdo de referência prática/didática, complementando (não substituindo) [[sources/blue-green-canary-rolling]], que já cobria Blue/Green, Canary e Rolling com profundidade técnica de Kubernetes/Argo Rollouts. Esta fonte contribui principalmente com: a distinção deploy vs. release (não coberta antes), Recreate como estratégia própria (não coberta antes), A/B deployment como conceito distinto de Canary (não coberto antes), e Shadow deployment (não coberto antes). Sem contradições com o conteúdo técnico já existente — os claims sobre Rolling/Blue-Green/Canary aqui são consistentes com (e menos aprofundados tecnicamente do que) os já registrados em [[concepts/rolling-update]], [[concepts/blue-green-deploy]] e [[concepts/canary-release]].
