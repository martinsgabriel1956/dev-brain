---
type: concept
title: "Contrato de API"
aliases: ["API contract", "contrato de interface", "interface contract"]
date_created: 2026-07-09
date_updated: 2026-07-27
source_count: 4
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
- [[wiki/concepts/entrevista-system-design]] — modelar endpoints, request/response e protocolo (HTTP vs. gRPC) é etapa avaliada em entrevista de arquitetura
- [[wiki/concepts/must-ignore-pattern]] — técnica de extensibilidade de schema para evoluir um contrato sem quebrar consumidores existentes
- [[wiki/concepts/contract-testing]] — como verificar automaticamente que um contrato continua sendo respeitado
- Ver também tratamento mais aprofundado de versionamento e breaking changes em `references/api-versioning-lifecycle.md` (tech-mentor-backend)

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-backend]]
- [[wiki/sources/5-dicas-entrevistas-lousa-branca-system-design]]
- [[wiki/sources/consumer-driven-contracts-martin-fowler]] — Must Ignore pattern e o modelo Provider/Consumer/Consumer-Driven Contract
- [[wiki/sources/anatomia-entrevista-system-design-bigtech]] — contraste entre API trivial (`POST /urls`) e API que exige multipart upload, autenticação e presigned URL (upload de vídeo) como demonstração de repertório real de design de API
