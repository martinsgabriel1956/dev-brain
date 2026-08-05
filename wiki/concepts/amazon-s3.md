---
type: concept
title: "Amazon S3"
aliases: ["S3", "Simple Storage Service"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
tags: ["aws", "s3", "storage", "cdn", "infra", "cloud"]
skill: tech-mentor-infra
status: stub
---

# Amazon S3 (Simple Storage Service)

Serviço de object storage da AWS — um "bucket" para armazenar dados de forma durável e altamente escalável. Casos de uso típicos: documentos, backups (inclusive de banco de dados), dados arquivados (archive), hospedagem de sites estáticos (um `index.html`, opcionalmente combinado com [[wiki/concepts/aws-cloudfront]] para CDN) e assets estáticos (imagens, logos).

## Prós

- Custo de armazenamento relativamente baixo para a maioria das utilizações.
- Escalabilidade praticamente sem limite prático de volume de dados.

## Contras

- **Não é banco de dados.** Existe latência que o torna inadequado para acesso transacional de baixa latência.
- **Custo por acesso** pode tornar o S3 caro para dados acessados com muita frequência — um backup de banco de dados acessado constantemente pode sair mais caro no S3 do que manter um banco de dados de verdade rodando.
- Não tem compute nativo nem file system nativo — não é possível "rodar um servidor" dentro de um bucket.

## Relação com outros conceitos

- [[wiki/concepts/aws-cloudfront]] — CDN comumente usada junto ao S3 para servir sites estáticos com baixa latência
- [[wiki/concepts/cache]] — trade-off custo/latência parecido com o de qualquer camada de armazenamento intermediária

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
