---
type: concept
title: "API Economy"
aliases: ["economia das APIs", "API como produto", "API-as-a-product"]
date_created: 2026-08-18
date_updated: 2026-08-24
source_count: 2
tags: [api-economy, modelo-de-negocio, api, historia-da-computacao]
skill: tech-mentor-backend
status: stub
---

# API Economy

Termo para o momento em que a API deixa de ser apenas uma ferramenta técnica interna e passa a ser **estratégia de negócio** — seja expondo dados/serviços de uma empresa para terceiros construírem em cima, seja vendendo a própria API como produto.

## Duas ondas, segundo a fonte

1. **Anos 2000 — grandes players abrem APIs públicas.** eBay, Amazon e Salesforce são citadas como pioneiras, seguidas por Google, Facebook e Twitter — empresas passam a disponibilizar dados/serviços para desenvolvedores terceiros construírem em cima. [[wiki/sources/historia-oauth2-antipadrao-senha-bernardo-lobato]] cita especificamente Salesforce, Google Maps, Amazon e [[wiki/entities/flickr|Flickr]] como pioneiras de 2006, situando o nascimento da API Economy no mesmo momento histórico em que o [[wiki/concepts/antipadrao-da-senha|antipadrão da senha]] (compartilhar senha para dar acesso a terceiros) se tornou insustentável.
2. **Anos 2010 — API vira o produto em si, não só um canal de distribuição.** Stripe, Twilio e SendGrid citadas como empresas que se tornaram bilionárias vendendo API diretamente (pagamento, mensageria, e-mail). No mesmo período, [[wiki/entities/amazon-web-services]], Google Cloud e Azure expandem oferecendo centenas de APIs de infraestrutura como produto.

## Relação com o Antipadrão da Senha e o OAuth

A API Economy é o pano de fundo direto da criação do [[wiki/concepts/oauth2|OAuth]]: conforme mais empresas expunham dados via API, o único mecanismo de acesso disponível — o [[wiki/concepts/antipadrao-da-senha|antipadrão da senha]] — se tornou insustentável em escala, motivando o grupo de discussão OAuth de 2007. Ver [[wiki/sources/historia-oauth2-antipadrao-senha-bernardo-lobato]].

## Relação com [[wiki/concepts/api-gateway]]

O crescimento do consumo massivo de APIs públicas/comerciais é uma das forças que empurra a necessidade de padrões de segurança e governança (OAuth, OpenID Connect, API Gateway) nos anos seguintes — sem eles, expor API como produto em escala vira risco de abuso e falta de controle de acesso.

## Key Sources

- [[wiki/sources/historia-e-evolucao-das-apis-bernardo-lobato]] — as duas ondas de API economy (anos 2000 abertura pública, anos 2010 API como produto), e a pressão resultante por segurança/governança nos anos 2020
- [[wiki/sources/historia-oauth2-antipadrao-senha-bernardo-lobato]] — 2006 como o momento em que o antipadrão da senha se tornou insustentável frente ao crescimento da API Economy, motivando a criação do OAuth
