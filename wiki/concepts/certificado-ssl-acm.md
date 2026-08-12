---
type: concept
title: "Certificado SSL / AWS Certificate Manager (ACM)"
aliases: ["certificado SSL", "SSL certificate", "ACM", "AWS Certificate Manager", "validação de domínio"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
tags: [aws, ssl, tls, acm, certificado, https, seguranca]
skill: tech-mentor-networking
status: stub
---

# Certificado SSL / AWS Certificate Manager (ACM)

Um **certificado SSL** é um certificado digital que habilita [[wiki/concepts/http-vs-https|HTTPS]] e prova que quem responde a uma requisição é o **dono daquele [[wiki/concepts/dominio|domínio]]** (não que é a marca esperada — ver [[wiki/concepts/http-vs-https]]). É apresentado durante o [[wiki/concepts/tls-handshake|TLS handshake]].

## ACM na prática (validação por CNAME)

O **AWS Certificate Manager** emite certificados para domínios. Fluxo demonstrado:

1. Solicitar um certificado para o domínio (ex.: `kdev.xyz`).
2. O ACM devolve um par **nome + valor CNAME** de validação.
3. Cadastrar esse **registro CNAME** no [[wiki/concepts/aws-route-53|Route 53]] (na hosted zone do domínio).
4. Quando o ACM consulta o domínio e encontra o valor esperado, conclui que o solicitante controla o domínio e **emite o certificado** (status: emitido / êxito).

A lógica da validação: "se o domínio é seu, coloque este valor no DNS dele" — só o dono consegue editar o DNS, então a presença do valor prova a propriedade.

O certificado emitido é depois anexado à distribuição [[wiki/concepts/aws-cloudfront|CloudFront]] como **Custom SSL certificate**, habilitando conexões HTTPS para o site estático servido do [[wiki/concepts/amazon-s3|S3]].

## Key sources
- [[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] — solicitação no ACM, validação por CNAME no Route 53, uso do cert no CloudFront
