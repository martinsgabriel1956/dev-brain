---
type: entity
title: "Flickr"
aliases: ["flickr"]
date_created: 2026-07-30
date_updated: 2026-08-24
source_count: 2
tags: [devops, devsecops, origem-do-devops, oauth2, api-economy]
skill: tech-mentor-security
status: stub
---

# Flickr

Serviço de hospedagem de fotos cuja palestra na conferência Velocity de 2009 — "10+ Deploys por Dia: Cooperação entre Desenvolvedores e Operações no Flickr", apresentada por dois de seus funcionários — é citada como o ponto de virada que deu tração à ideia de [[wiki/concepts/devsecops|DevOps]] proposta por [[wiki/entities/patrick-debois]]. A palestra demonstrava deploys frequentes viabilizados por cooperação direta entre desenvolvimento e operações, em vez dos silos tradicionais entre as duas áreas.

## Exemplo Canônico do Antipadrão da Senha (Pré-OAuth)

Em 2006, antes do [[wiki/concepts/oauth2|OAuth]] existir, o Flickr é citado como exemplo direto do [[wiki/concepts/antipadrao-da-senha|antipadrão da senha]]: para um serviço terceiro acessar suas fotos, você tinha que fornecer sua própria senha do Flickr, e ele se conectava como se fosse você. Também citado, ao lado de Salesforce, Google Maps e Amazon, como um dos serviços pioneiros em disponibilizar recursos via API na origem da [[wiki/concepts/api-economy|API Economy]].

## Key Sources

- [[wiki/sources/devsecops-origem-cultura-manifesto]] — palestra na Velocity 2009 como catalisador do movimento DevOps
- [[wiki/sources/historia-oauth2-antipadrao-senha-bernardo-lobato]] — exemplo canônico do antipadrão da senha em 2006, e pioneiro citado da API Economy
