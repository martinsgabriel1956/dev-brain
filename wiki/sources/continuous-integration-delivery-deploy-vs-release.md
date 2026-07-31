---
type: source
title: "CI, CD (Delivery) e CD (Deploy) — e a Diferença entre Deploy e Release"
aliases: ["os dois CDs", "ci cd delivery deploy", "deploy vs release na prática github actions"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/continuous-integration-delivery-deploy-vs-release.md
source_url: ""
author: "não identificado no vídeo (autoria inferida: possivelmente Augusto Galego — ver open question)"
date_published: ""
date_ingested: 2026-07-31
source_count: 0
tags: [ci-cd, deploy, deploy-vs-release, feature-flags, github-actions, secrets-management, staging, vps, infra]
skill: tech-mentor-infra
status: stable
---

# CI, CD (Delivery) e CD (Deploy) — e a Diferença entre Deploy e Release

## TL;DR

Transcrição de aula em português (sem necessidade de tradução) que didaticamente separa os "dois CDs" — Continuous Delivery vs. Continuous Deployment — dentro de Continuous Integration/Continuous Delivery, e reforça a distinção deploy vs. release já documentada na wiki. Demonstra na prática, com GitHub Actions, um pipeline de dois jobs (CI: lint/test/build; CD: deploy via SSH para uma VPS da HostGator) e o fluxo de secrets write-only do GitHub. Também descreve o fluxo de branches feature → dev/staging → main com clonagem anonimizada do banco de produção para testes em staging.

## Key Claims

- **CI, Continuous Delivery e Continuous Deployment são três níveis distintos, mas a maioria das empresas médias não distingue delivery de deploy na prática** — só empresas em escala massiva (cita a Meta) fazem essa distinção de forma explícita, com um gate humano entre "pronto para lançar" e "lançado". Consistente com a tabela dos "Três Níveis" já documentada em [[wiki/concepts/ci-cd]].
- **A distinção técnica entre deploy e release é reforçada com dois mecanismos concretos**: feature flag (código escondido atrás de flag desligada) e tráfego direcionado (duas instâncias, 100% do tráfego ainda na antiga) — mesma dualidade já registrada em [[wiki/concepts/deploy-vs-release]].
- **Recomendação de mover scripts de deploy para dentro da codebase** ("tudo que você faz via script manual, você consegue fazer via script codado, sujeito às mesmas revisões da codebase") como forma de reduzir erro humano — ideia já presente em [[wiki/concepts/ci-cd]] ("deploy automático reduz erro humano"), aqui com a justificativa adicional de que o script fica sujeito a code review.
- **Fluxo de branches com ambiente intermediário**: `feature → dev/staging → main`, com QA testando em staging antes do merge para main. Ponto não coberto anteriormente na wiki com este nível de detalhe de fluxo de branch (a wiki já tinha a ideia de sequência dev → homologação → PR em [[wiki/concepts/paridade-local-producao]], mas não a nomenclatura de branch específica).
- **Clonagem do banco de dados de produção para staging, com anonimização seletiva** (senhas, nomes, dados de pagamento) preservando a estrutura e dispersão dos dados — reforça concretamente a recomendação genérica de "dados reais anonimizados" já citada em [[wiki/concepts/paridade-local-producao]], com exemplos explícitos do que se anonimiza.
- **Demonstração concreta de GitHub Secrets como write-only**: uma vez salvo, nem o dono do repositório consegue visualizar o valor — só atualizar. Acessado no workflow via `secrets.NOME_DO_SECRET`. Reforça, com uma demonstração ao vivo, a propriedade já documentada em [[wiki/concepts/secrets-management]] ("secrets configurados não são mais visíveis — nem ao próprio configurador").
- **Deploy via SSH direto para uma VPS**, sem Kubernetes/plataforma de deploy gerenciada — instalar dependências e subir a aplicação manualmente dentro do job de CD. Caso simples, de baixo nível de abstração, coerente com a tabela "Estratégias de deploy" da skill `tech-mentor-infra` (Rolling/Blue-Green/Canary não entram em jogo aqui — é um deploy de instância única, mais próximo de "Recreate").
- **Bloco patrocinado da HostGator**: planos a partir de R$ 21,70/mês, VPS em São Paulo, opções de OS (Ubuntu, Alma Linux, Rocky Linux, com/sem cPanel) e ofertas prontas para N8N, WordPress, Docker — e uma oferta de VPS com **Claude Code pré-instalado**, promovida como alternativa a rodar localmente (não precisa deixar o computador ligado; dá pra usar do celular). Não há comparação independente com outros provedores — tratado como conteúdo patrocinado, não avaliação técnica. → [[wiki/entities/hostgator]], [[wiki/entities/claude-code]]

## Entities

[[wiki/entities/meta]] · [[wiki/entities/hostgator]] · [[wiki/entities/claude-code]] · [[wiki/entities/augusto-galego]] (autoria inferida)

## Concepts

[[wiki/concepts/ci-cd]] · [[wiki/concepts/deploy-vs-release]] · [[wiki/concepts/feature-flags]] · [[wiki/concepts/github-actions]] · [[wiki/concepts/secrets-management]] · [[wiki/concepts/paridade-local-producao]] · [[wiki/concepts/canary-release]]

## Conexão com Fontes Existentes

Esta fonte não traz um caso novo — ela é essencialmente didática, reforçando e demonstrando na prática conceitos já bem documentados via [[wiki/sources/rapid-release-at-massive-scale-facebook]] (o exemplo da Meta é citado de segunda mão aqui, sem novo dado além do que já está em [[wiki/concepts/canary-release]] e [[wiki/entities/meta]]) e [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]] (mesmo padrão de demo em VPS com HostGator, mesmo estilo de conteúdo, reforçando a hipótese de mesma autoria — ver open question abaixo). O valor incremental real está na demonstração concreta de GitHub Secrets write-only e no detalhamento do fluxo de branch feature/dev-staging/main com anonimização de banco.

## Open Questions

- **Autoria não confirmada.** O vídeo não identifica o autor por nome. O estilo (demo prática de deploy em VPS, patrocínio da HostGator, série sobre "tipos de deploy") é consistente com [[wiki/entities/augusto-galego]], que já tem uma fonte irmã ([[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]]) com o mesmo padrão de patrocínio e o mesmo tema declarado como continuação de uma aula anterior sobre "tipos de deploy" — esta fonte pode ser, na verdade, a própria "aula anterior" referenciada lá, ou uma aula irmã da mesma série. Não há confirmação direta (nome, site, ou voz) na transcrição para fechar essa atribuição.
- **"HostGator" vs. "Hostinger".** A transcrição contém a palavra "Host Gator" (grafada separada, possível artefato de transcrição automática de áudio). Já existe uma entidade [[wiki/entities/hostgator]] (grafia unida, sem espaço) documentada a partir de [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]] — tratada aqui como a mesma empresa, dado o contexto idêntico (VPS patrocinada, Brasil, São Paulo). Distinta da empresa **Hostinger** ([[wiki/entities/hostinger]]), que é uma provedora de VPS diferente, já documentada em outras duas fontes da wiki — risco real de confusão de nomes entre as duas empresas, mantido como nota de desambiguação nas duas entidades.
- O vídeo não detalha como a etapa de aprovação/gate de Continuous Delivery é implementada tecnicamente quando há interação humana (menciona "environments com aprovação manual" apenas de forma abstrata) — [[wiki/concepts/github-actions]] já documenta o recurso concreto do GitHub Actions (`environment: production` exigindo aprovação), sem contradição, apenas sem o vídeo ter entrado nesse nível de detalhe.

## Raw Quotes

- "Deploy e release não são a mesma coisa. Eu posso subir uma feature e ter o meu código pronto dentro do meu servidor sem lançar esse código."
- "Tudo que você consegue fazer através de um script manual, você consegue fazer através de um script codado dentro da codebase, sujeito aos mesmos padrões e reviews da codebase."
- "Mesmo que eu clique para editar aqui, você não consegue ver o valor que tá atualmente — é impossível eu ler esse valor, eu consigo fazer um update nesse valor, mas eu não consigo ler ele."
