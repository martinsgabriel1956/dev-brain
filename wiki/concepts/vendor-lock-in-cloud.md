---
type: concept
title: "Vendor Lock-in em Cloud"
aliases: ["vendor lock-in", "lock-in de nuvem", "aprisionamento a provedor"]
date_created: 2026-08-04
date_updated: 2026-08-05
source_count: 2
tags: ["vendor-lock-in", "aws", "cloud", "arquitetura", "infra", "custo"]
skill: tech-mentor-infra
status: stub
---

# Vendor Lock-in em Cloud

Risco de dependência crescente de serviços proprietários de um provedor de cloud (ex.: AWS): quanto mais serviços específicos de um único fornecedor uma aplicação usa — [[wiki/concepts/ecs]], [[wiki/concepts/elastic-beanstalk]], [[wiki/concepts/api-gateway]], [[wiki/concepts/step-functions]] —, mais caro e complexo fica migrar essa aplicação para outro provedor ou para infraestrutura própria depois.

## Gradiente de lock-in

Nem todo serviço gerenciado tem o mesmo grau de aprisionamento. Numa mesma fonte sobre o toolkit essencial da AWS, o gradiente citado (do mais portável ao mais preso) é aproximadamente:

- [[wiki/concepts/ec2]] — baixo lock-in; é essencialmente uma VM, portável para praticamente qualquer provedor.
- [[wiki/concepts/aws-lambda]], [[wiki/concepts/aws-fargate]] — modelo conceitual (FaaS, containers serverless) existe em outros provedores, mas a API e o tooling são específicos da AWS.
- [[wiki/concepts/ecs]], [[wiki/concepts/elastic-beanstalk]], [[wiki/concepts/api-gateway]] — lock-in médio-alto: orquestração e configuração deeply integradas ao ecossistema AWS.
- [[wiki/concepts/step-functions]] — citado como o caso mais extremo entre os serviços cobertos: a lógica do workflow em si (máquina de estados) vive dentro do serviço proprietário, não no código da aplicação.

## Por que existe apesar do risco

Serviços mais integrados ao ecossistema de um provedor tendem a ser mais simples de configurar e operar (menos peças para montar manualmente) — o trade-off de lock-in é trocado por velocidade e menor complexidade operacional. Times avaliam esse trade-off caso a caso: um serviço como Step Functions pode ser descartado justamente por lock-in excessivo em favor de uma alternativa mais portátil (ex.: fila + lógica de estado no próprio código).

## Variante: Lock-in de Ferramenta de IA a um Único Vendor de Modelo

[[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]] descreve uma forma de lock-in fora do domínio de cloud infra tradicional: uma ferramenta cliente (ex.: [[wiki/entities/claude-code]]) só aceita, nativamente, modelos de um único provider (Anthropic). O autor descreve o uso de um [[wiki/concepts/ai-gateway-llm-router|AI Gateway]] como forma de contornar esse lockin — a ferramenta continua funcionando normalmente, mas o modelo real por trás pode ser de qualquer outro provider. É a mesma lógica de dependência de fornecedor da tabela acima (trocar de "vendor" depois é mais caro/complexo quanto mais a ferramenta for feita para um único formato), só que aplicada à camada de modelo de IA, não a serviços de infraestrutura cloud.

## Relação com outros conceitos

- [[wiki/concepts/finops-para-ia]] — mesmo tipo de trade-off "conveniência vs. dependência de fornecedor" no domínio de custo de IA
- [[wiki/concepts/camada-de-aplicacao-vs-modelo]] — mesma lógica estrutural aplicada a modelos de IA em vez de serviços de cloud
- [[wiki/concepts/ai-gateway-llm-router]] — mecanismo concreto usado para contornar lock-in de modelo numa ferramenta de IA

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
- [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]] — lock-in de ferramenta de IA a um único provider de modelo, contornado via AI Gateway
