---
type: concept
title: "TLS Handshake"
aliases: ["negociação TLS", "SSL handshake"]
date_created: 2026-07-28
date_updated: 2026-08-12
source_count: 2
tags: [rede, tls, https, handshake, browser, critical-rendering-path]
skill: tech-mentor-frontend
status: draft
---
# TLS Handshake

Etapa executada apenas quando o site usa HTTPS, imediatamente após o [[wiki/concepts/tcp-three-way-handshake]]. Browser e servidor negociam a criptografia da conexão trocando certificados e chaves, o que adiciona round trips extras antes do primeiro request HTTP conseguir ser enviado.

Faz parte da fase de rede do [[wiki/concepts/critical-rendering-path]] — é uma das razões pelas quais HTTPS tem latência inicial maior que HTTP puro (mitigável com TLS 1.3, session resumption, ou `<link rel="preconnect">`, este último documentado na skill `tech-mentor-frontend`).

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
- [[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] — a "troca de chaves entre navegador e servidor" do [[wiki/concepts/http-vs-https|HTTPS]], apresentando o [[wiki/concepts/certificado-ssl-acm|certificado SSL]] como prova de que quem responde é dono do domínio (mitigando Man-in-the-Middle)
