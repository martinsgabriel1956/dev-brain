---
type: concept
title: "Contrato de API"
aliases: ["API contract", "contrato de interface", "interface contract"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [api, contrato, backend, arquitetura, desacoplamento]
skill: tech-mentor-backend
status: stub
---

# Contrato de API

A API é um contrato entre quem pede e quem responde. O consumidor (frontend, outro serviço) não precisa saber como a tabela do banco foi montada nem qual framework o servidor usa — só precisa saber qual rota chamar, quais dados mandar e qual resposta esperar.

## Por que importa

É o contrato estável que permite ao backend mudar por dentro sem quebrar quem consome:

- Trocar o banco de dados
- Dividir um serviço em vários
- Mudar a regra interna de processamento

Enquanto o contrato não muda, o cliente continua funcionando. Um contrato bem feito deixa claro **o que pode entrar**, **o que pode sair**, e **como o sistema se comporta quando algo dá errado**.

## Relação com outros conceitos

- [[wiki/concepts/requisicao-resposta]] — o contrato formaliza o formato dessas mensagens
- [[wiki/concepts/validacao-de-entrada]] — o contrato define o que é uma entrada válida; a validação garante em runtime
- Ver também tratamento mais aprofundado de versionamento e breaking changes em `references/api-versioning-lifecycle.md` (tech-mentor-backend)

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-backend]]
