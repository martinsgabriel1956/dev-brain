---
type: entity
title: "Mercado Livre"
aliases: ["MELI", "Mercado Pago", "Mercado Livre/Mercado Pago"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 2
tags: [mercado-livre, mercado-pago, fintech, e-commerce, iso-27001, pci-dss, zero-trust, golang]
skill: tech-mentor-security
status: draft
---

# Mercado Livre

## TL;DR

Maior plataforma de e-commerce e pagamentos da América Latina (via Mercado Pago). Opera pagamentos, logística e varejo simultaneamente, o que gera uma superfície de ataque grande. Combina certificação [[wiki/concepts/iso-27001]] com PCI-DSS e aplica Zero Trust (ver [[wiki/sources/zero-trust]]) — nada é confiável por padrão, tudo é verificado. Também é citada como referência de adoção madura de Go em produção no mercado brasileiro.

## Perfil

- **Domínio:** e-commerce + fintech (Mercado Pago) + logística
- **Região:** América Latina, sede no Brasil/Argentina

## Postura de segurança

- Certificação ISO 27001, recertificada e destacada no relatório anual de 2024 como pilar de confiança do ecossistema
- Combina ISO 27001 com **PCI-DSS** (padrão de segurança para dados de cartão de crédito) — necessário pela operação de pagamentos via Mercado Pago
- Aplica **Zero Trust**: nenhum acesso é confiável por padrão, tudo deve ser verificado — alinhado aos controles reorganizados da ISO 27001:2022

## Decisões técnicas

- Uma das empresas brasileiras citadas como adotante consolidada de **Go** em produção (junto com Mercado Pago e Stone), evidência de que a linguagem já superou a fase de "tendência passageira" no mercado local

## Key Sources

- [[wiki/sources/iso-27001-dicionario-programador]] — postura de segurança: ISO 27001 + PCI-DSS + Zero Trust
- [[wiki/sources/golang-mercado-trabalho-frontend-para-backend]] — adoção consolidada de Go em produção
