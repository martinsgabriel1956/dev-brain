---
type: concept
title: "Amazon S3"
aliases: ["S3", "Simple Storage Service"]
date_created: 2026-08-04
date_updated: 2026-08-17
source_count: 3
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

## Storage Classes, Lifecycle e Event Notifications

Objetos podem ter até 5 TB, durabilidade de 11 noves. Três storage classes principais: **Standard** (acesso frequente), **Standard-IA** (raramente acessado, mas precisa estar disponível rápido), **Glacier** (arquivo de longo prazo, recuperação em minutos a horas). **Lifecycle policies** movem objetos entre classes automaticamente (ex: 30 dias → IA, 90 dias → Glacier) sem intervenção manual — mitiga o contra de "custo por acesso" já registrado acima ao migrar dados frios automaticamente. **Versioning** protege contra deleção acidental; **Block Public Access** bloqueia acesso público mesmo com configuração errada. **S3 Event Notifications** disparam Lambda (upload) ou mandam mensagem para [[wiki/concepts/aws-sqs|SQS]] (deleção) — cola comum de arquiteturas event-driven. Ver [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]].

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — storage classes, lifecycle policies, versioning, Block Public Access e Event Notifications como gatilho de arquiteturas event-driven
- [[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] — bucket S3 público hospedando site estático; o **endpoint de site estático é HTTP puro** (sem SSL → navegador marca "not secure"), motivando a camada [[wiki/concepts/aws-cloudfront|CloudFront]] + [[wiki/concepts/certificado-ssl-acm|ACM]] para obter HTTPS
