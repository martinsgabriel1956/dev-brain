---
type: concept
title: "Soberania Digital"
aliases: ["Digital Sovereignty", "Residência de Dados", "Data Residency"]
date_created: 2026-05-06
date_updated: 2026-07-29
source_count: 3
tags: ["soberania-digital", "compliance", "regulação", "dados", "cloud"]
skill: tech-mentor-infra
status: stub
---

# Soberania Digital

Capacidade de uma organização ou governo de manter controle total sobre seus dados, aplicações e infraestrutura dentro de fronteiras nacionais ou jurisdicionais definidas. No contexto de cloud pública, implica garantir que dados não saiam de um território específico e que a infraestrutura esteja sujeita às leis locais.

## Dimensões

| Dimensão | Descrição |
|---|---|
| **Residência de dados** | Dados armazenados e processados apenas em território específico |
| **Portabilidade** | Capacidade de migrar dados sem dependência de fornecedor (vendor lock-in) |
| **Controle operacional** | Quem tem acesso ao hardware/software que processa os dados |
| **Conformidade regulatória** | Aderência a leis locais (LGPD, GDPR, CLOUD Act) |

## Soluções AWS para Soberania Digital

- **[[zona-local-dedicada|Dedicated Local Zones]]** — infraestrutura dedicada e isolada, operada pela AWS
- **[[aws-outposts|AWS Outposts]]** — hardware AWS dentro das instalações do cliente
- **AWS GovCloud** — regiões isoladas para governo dos EUA (FedRAMP/ITAR)
- **Controles de região** — políticas IAM que impedem workloads de cruzar fronteiras

## Regulações Relevantes

| Regulação | Jurisdição | Impacto |
|---|---|---|
| LGPD | Brasil | Dados de brasileiros devem ter proteção equivalente |
| GDPR | União Europeia | Transferência de dados fora da UE é restrita |
| CLOUD Act (EUA) | EUA | Governo americano pode exigir acesso a dados em provedores dos EUA |
| ITAR | EUA | Dados de defesa/armamento com controles rígidos |

## Tensão: Soberania vs. Escala Cloud

O modelo multi-tenant da cloud pública por natureza compartilha infraestrutura. Soberania plena exige isolamento que aumenta custo e reduz elasticidade — é um trade-off arquitetural explícito.

## Nova Dimensão: Soberania Sobre o Próprio Modelo de IA

[[wiki/sources/modelo-openai-escapa-sandbox-benchmark-cyberseguranca]] adiciona uma dimensão à tabela acima que não é sobre dados, mas sobre **controle do próprio modelo de IA**: durante um incidente de segurança real, modelos com [[wiki/concepts/agent-containment|guardrails]] padrão (acessados via API de terceiros) se recusaram a ajudar a investigar um ataque em andamento, e a solução só foi possível hospedando um modelo (GLM 5.2) na própria infraestrutura, sem depender do comportamento decidido por um provedor externo. A fonte argumenta que esse é um exemplo concreto de por que empresas podem precisar de "soberania" não só sobre onde os dados residem, mas sobre qual modelo processa esses dados e sob quais regras — hoje uma opção cara e restrita a poucas organizações, mas com demanda crescente à medida que ataques e defesas passam a depender do mesmo tipo de ferramenta.

## Nota Lateral: Internacionalização de Domínio como Soberania de Identidade

[[wiki/sources/email-address]] cita a aprovação do domínio ".bharat" pela Índia em sete escritas locais (Devanágari entre elas) como exemplo de EAI (Email Address Internationalization). É uma dimensão diferente das listadas acima — não é sobre onde o dado reside, mas sobre quem controla o espaço de nomes/identidade da internet num idioma nacional, puxado por decisão de governo. Conexão mais fraca que as demais fontes desta página; citada aqui como referência lateral, não como caso central.

## Key Sources

- [[wiki/sources/aws-infraestrutura-global]]
- [[wiki/sources/modelo-openai-escapa-sandbox-benchmark-cyberseguranca]] — soberania sobre o próprio modelo de IA (self-hosting sem guardrails) como caso limite durante resposta a incidente
- [[wiki/sources/email-address]] — internacionalização de domínio (.bharat, EAI) como nota lateral de soberania de identidade/namespace
