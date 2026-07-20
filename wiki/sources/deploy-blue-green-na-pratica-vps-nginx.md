---
type: source
title: "Deploy Blue/Green na Prática — VPS + Nginx (Demo)"
aliases: ["blue green na prática", "deploy blue green vps hostgator", "demo blue green nginx"]
date_created: 2026-07-20
date_updated: 2026-07-20
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/deploy-blue-green-na-pratica-vps-nginx.md
source_url: ""
author: "Augusto Galego"
date_published: ""
date_ingested: 2026-07-20
source_count: 0
tags: [blue-green, deploy, nginx, reverse-proxy, vps, ssh, systemd, ci-cd, hostgator]
skill: tech-mentor-infra
status: stable
---

# Deploy Blue/Green na Prática — VPS + Nginx (Demo)

## TL;DR

Demo prática (patrocinada pela [[wiki/entities/hostgator|HostGator]]) de deploy [[wiki/concepts/blue-green-deploy|blue/green]] manual, de ponta a ponta, numa única VPS: [[wiki/concepts/reverse-proxy|Nginx como reverse proxy]] na porta 80 roteando para duas instâncias Node rodando em paralelo (portas 3001/3002), trocadas via um script que só altera a config do Nginx — nenhuma instância é derrubada na troca. Continuação de uma aula anterior sobre tipos de deploy, feita deliberadamente à mão (sem pipeline) para depois automatizar com confiança.

## Key Claims

- **Blue/Green na prática é só uma seta de roteamento** — ambas as versões (v1 e v2) já estão rodando em paralelo, em portas diferentes, na mesma máquina; "trocar" não sobe nem derruba nada, apenas reconfigura para onde o [[wiki/concepts/reverse-proxy|Nginx]] direciona o tráfego do usuário. → [[wiki/concepts/blue-green-deploy]]
- **O nome da cor não importa, só o papel.** O apresentador confunde ao vivo qual branch Git (`blue`/`green`) corresponde a qual papel do deploy (a versão live vs. a nova) — e usa o próprio erro para reforçar que blue/green é convenção de rótulo, não uma regra semântica fixa.
- **Fluxo recomendado antes de expor ao usuário**: subir a instância nova numa porta que o usuário não acessa, testar direto nessa porta (bypass do proxy), só então "flipar" o roteamento do proxy — e manter a instância antiga de pé por um tempo para rollback instantâneo.
- **Nginx = web server / reverse proxy**, fazendo a ponte entre o usuário externo e o processo Node local; ambos (proxy e app) rodam na mesma VPS, sem necessidade de máquinas separadas — replicável localmente sem nenhuma infraestrutura extra. → [[wiki/concepts/reverse-proxy]]
- **Deploy manual como etapa pedagógica antes de automatizar**: a sequência inteira (clonar, instalar dependências, subir instância, trocar roteamento) é feita com ~4 scripts bash rodados manualmente via SSH, não uma pipeline — a tese do apresentador é que entender o processo manual primeiro facilita confiar depois numa pipeline (GitHub Actions) que faz a mesma coisa automaticamente. → [[wiki/concepts/ci-cd]]
- **A única diferença de configuração entre blue e green é a porta** — tanto no script de deploy quanto no bloco de `proxy_pass` do Nginx, com bastante redundância proposital do número de porta em vários pontos do arquivo, para tolerar erro de edição.
- **systemd é usado para administrar os processos** (subir, manter vivo, reiniciar) das instâncias Node na VPS, mas o apresentador não detalha a configuração das unidades — trata como ferramental de suporte, não o foco da demo.
- **Custo/infra**: VPS mais barata da HostGator (menor plano) foi suficiente para rodar Nginx + duas instâncias Node simultâneas; o apresentador recomenda esse tipo de VPS para SaaS/site próprio real, mas reconhece que rodar localmente também é válido para aprendizado.

## Entities

[[wiki/entities/augusto-galego]] · [[wiki/entities/hostgator]]

## Concepts

[[wiki/concepts/blue-green-deploy]] · [[wiki/concepts/reverse-proxy]] · [[wiki/concepts/load-balancer]] · [[wiki/concepts/ci-cd]] · [[wiki/concepts/systemd]] · [[wiki/concepts/deploy-strategies]]

## Conexão com fontes existentes

Esta fonte é o complemento **prático** de [[wiki/sources/blue-green-canary-rolling]] e [[wiki/sources/tipos-de-deploy]] (ambas mais conceituais/comparativas, já citadas em [[wiki/concepts/blue-green-deploy]] e [[wiki/concepts/deploy-strategies]]): mostra o "por baixo do capô" de como a troca de tráfego é implementada de fato num único host, sem Kubernetes — reverse proxy + múltiplas portas + script de swap, em vez de `Service.selector` no cluster. Também conecta com a distinção já registrada em [[wiki/concepts/ci-cd]] entre deploy manual e automático ("a diferença não é o que é executado, é o que dispara a execução") — esta fonte é um exemplo concreto de deploy 100% manual disparado por SSH.

## Open Questions

- Configuração exata das unidades systemd (arquivos `.service`, restart policy) não foi mostrada na demo — apenas mencionada como instalada.
- O apresentador é explícito sobre não ser especialista em Nginx/DevOps ("não sou a melhor pessoa para explicar isso"); os detalhes de configuração do Nginx foram tratados como caixa-preta replicada de tutorial, sem explicação profunda das diretivas.
- Nenhum dado de latência/downtime real foi medido durante a troca — a demonstração é qualitativa (F5 no navegador), não instrumentada.

## Raw Quotes

> "A blue tá rodando na 3001 tá e a green é a V2, é que tá rodando no 3002 [...] mas tradicionalmente quando a gente fala de blue green na prática não muda nada qual cor e qual não."

> "Ele tá apenas mudando essa setinha aqui — pra onde as requisições do usuário vão ser direcionadas, se vai ser pro blue ou pro green."

> "Eu vou subir uma instância green, eu vou testar ali a minha instância green [...] quando eu garantir que tá funcionando eu vou flipar minha Nginx: 'pode mudar o tráfego, tá tudo certo, tá funcionando, vira o tráfego pra cá e deleta essa instância aqui.'"

*(Transcrição completa em `raw/deploy-blue-green-na-pratica-vps-nginx.md`.)*
