---
type: concept
title: "Extração de Slice para Serviço"
aliases: ["slice como passo antes do microsserviço", "isolar antes de extrair"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_count: 1
tags: [vertical-slice, microsservicos, extracao, migracao, autenticacao]
skill: tech-mentor-backend
status: draft
---

# Extração de Slice para Serviço

## TL;DR

Receita de [[wiki/sources/vertical-slice-organizar-codigo-por-funcionalidade-bernardo-lobato]] para extrair uma funcionalidade: (1) criar a slice **dentro** do projeto e isolar todo o comportamento nela; (2) provar o isolamento por uso e testes automatizados; (3) só então recriá-la como serviço externo. Exemplo: autenticação/autorização movida para um serviço externo de autenticação. Por isso o autor chama o [[wiki/concepts/vertical-slice-architecture]] de "caminho intermediário" rumo a [[wiki/concepts/microsservicos]].

## Relações

- Mesma lógica de extração tardia de [[wiki/concepts/monolito-modular]] e, nas migrações, de [[wiki/concepts/strangler-fig-pattern]]; a slice faz o papel de módulo no nível de funcionalidade.
- Requisito: slice sem dependência de modelo compartilhado ([[wiki/concepts/dominio-centralizado-vs-modelo-por-slice]]) e sem acoplamento escondido ([[wiki/concepts/acoplamento-entre-slices]]); dados compartilhados continuam sendo o ponto difícil (ver armadilhas em [[wiki/concepts/strangler-fig-pattern]]).

## Key sources

- [[wiki/sources/vertical-slice-organizar-codigo-por-funcionalidade-bernardo-lobato]]
