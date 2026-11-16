---
type: entity
title: "IBGE (API de localidades)"
aliases: ["IBGE", "Instituto Brasileiro de Geografia e Estatística", "servicodados.ibge.gov.br"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [orgao-publico, api, dados-abertos, brasil]
skill: tech-mentor-frontend
status: stub
---

# IBGE (API de localidades)

Instituto Brasileiro de Geografia e Estatística. Publica APIs abertas em servicodados.ibge.gov.br; a de localidades lista regiões, estados e municípios.

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa `/api/v1/localidades/estados` (27 objetos com id, sigla, nome e região) para preencher o select de UF do Ecoleta e `/api/v1/localidades/estados/{UF}/municipios` para as cidades, com o id do estado (33 é o Rio de Janeiro, 11 Rondônia). Escolheu usar "um serviço que já existe na internet" para não preencher à mão. Ver [[wiki/concepts/fetch-api]] e [[wiki/concepts/json]].

## Key sources

- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: estados e municípios para o formulário do Ecoleta
