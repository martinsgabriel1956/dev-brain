---
type: concept
title: "Conteinerização"
aliases: ["contêiner", "container", "docker", "contêineres", "containers"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 1
tags: [conteineres, docker, portabilidade, infra]
skill: tech-mentor-infra
status: stub
---

# Conteinerização

Executar processos de forma isolada dentro de contêineres, sendo o Docker a ferramenta mais citada. A tese da fonte: Kubernetes é opcional, mas o uso de contêineres é "quase que obrigatório". [[wiki/sources/utilizar-ou-nao-kubernetes-fluxo-de-decisao-cloud]]

## O que a fonte defende

- **Pré-requisito:** aprender Docker e os conceitos de contêiner vem antes de [[wiki/concepts/kubernetes]].
- **Serve para [[wiki/concepts/monolito]]:** dizer que Docker não serve para monolito é "balela".
- **Não depende de Kubernetes:** dá para ir a produção com [[wiki/concepts/conteineres-gerenciados-sem-kubernetes]].
- **Facilita o desenvolvimento:** banco e mensageria sobem em contêineres, sem instalar dependências na máquina.
- **Dá portabilidade:** reduz o custo de trocar de ambiente ou de provedor, atenuando [[wiki/concepts/vendor-lock-in-cloud]].
- **Abre opções:** aplicação não conteinerizada encontra bem menos caminhos em [[wiki/concepts/arvore-de-decisao-de-computacao-em-nuvem]].

Rodar sem contêiner continua possível: o App Service aceita código direto, por exemplo. O autor apenas não recomenda.

## Key Sources

- [[wiki/sources/utilizar-ou-nao-kubernetes-fluxo-de-decisao-cloud]]
