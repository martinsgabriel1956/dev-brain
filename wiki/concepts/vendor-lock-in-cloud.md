---
type: concept
title: "Vendor Lock-in em Cloud"
aliases: ["vendor lock-in", "lock-in de nuvem", "aprisionamento a provedor"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
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

## Relação com outros conceitos

- [[wiki/concepts/finops-para-ia]] — mesmo tipo de trade-off "conveniência vs. dependência de fornecedor" no domínio de custo de IA
- [[wiki/concepts/camada-de-aplicacao-vs-modelo]] — mesma lógica estrutural aplicada a modelos de IA em vez de serviços de cloud

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
