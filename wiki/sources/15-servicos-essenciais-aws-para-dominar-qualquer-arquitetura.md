---
type: source
title: "15 Serviços Essenciais da AWS Para Dominar Qualquer Arquitetura"
aliases: ["200 serviços AWS 15 que importam", "guia essencial de serviços AWS"]
date_created: 2026-08-17
date_updated: 2026-08-17
source_count: 0
tags: [aws, cloud, infraestrutura, arquitetura, iam, vpc, ec2, s3, rds, aurora, lambda, dynamodb, api-gateway, cloudfront, cloudwatch, sqs, sns, eventbridge, ecs, ecr, eks]
skill: tech-mentor-infra
status: stable
source_file: "raw/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura.md"
source_url: ""
author: "não identificado (vídeo educacional em pt-BR, canal não referenciado na transcrição)"
date_published: ""
date_ingested: "2026-08-17"
---

## TL;DR

A AWS tem ~200 serviços, mas 90% das aplicações usam os mesmos ~15. A fonte percorre esses serviços em ordem de dependência lógica (não alfabética): IAM (segurança) → VPC (rede) → EC2 (computação) → Auto Scaling + ALB (elasticidade) → S3 (objetos) → RDS/Aurora (relacional) → Lambda (serverless) → DynamoDB (NoSQL) → API Gateway (exposição) → CloudFront (CDN) → CloudWatch (observabilidade) → SQS/SNS/EventBridge (mensageria) → ECS/EKS/ECR (containers), fechando com uma visão rápida de Route 53, Cognito, Secrets Manager, Step Functions, ElastiCache e Kinesis, e uma arquitetura de referência que encadeia todos os blocos centrais. O fio condutor é sempre prático: o que o serviço resolve, quando usar, e como se conecta ao próximo bloco da pilha — sem aprofundar em nenhum deles além do necessário para montar o mapa mental completo.

---

## Reivindicações Principais

**Claim:** O princípio de least privilege no IAM deve ser aplicado de forma granular — uma role deve ter exatamente a permissão necessária (ex: `s3:GetObject` num bucket específico), nunca acesso amplo, porque limita o dano em caso de comprometimento.
**Evidência:** Exemplo direto da fonte: "se precisa ler do S3, crie uma row com exatamente essa permissão; se a instância for comprometida, o dano é limitado."
**Confiança:** Alta — consistente com a prática documentada em detalhe em [[wiki/concepts/aws-iam]] e com o exemplo JSON de policy já presente na referência de skill carregada (`tech-mentor-infra/references/cloud/aws.md`).

**Claim:** A arquitetura de rede mais típica em produção usa três camadas de isolamento: load balancer em subnet pública, aplicação em subnet privada, banco em subnet privada ainda mais isolada.
**Evidência:** Descrição direta da fonte da arquitetura "clássica" de VPC com subnets públicas/privadas e Security Groups como firewall por instância.
**Confiança:** Alta como padrão de mercado amplamente documentado; a fonte não cita caso real, é uma generalização didática.

**Claim:** O modelo de preço de EC2 deve ser escolhido por perfil de carga: Reserved para produção estável (desconto até 70%), On-Demand para picos, Spot para batch (desconto até 90%, mas sujeito a interrupção).
**Evidência:** Regra prática apresentada como conclusão direta dos três modelos de preço descritos.
**Confiança:** Alta — regra padrão da indústria, mas a fonte não detalha graceful shutdown para Spot (ver [[wiki/concepts/auto-scaling]] e a referência de skill sobre Spot Interruption Handling para o detalhe que falta aqui).

**Claim:** Aurora deve ser preferido a RDS quando o SLA não tolera 1-2 minutos de failover, quando o storage cresce de forma imprevisível, ou quando é necessário mais de 5 read replicas; RDS continua fazendo sentido para workloads pequenos/dev ou quando custo é prioridade.
**Evidência:** A fonte já apresenta a heurística de forma direta ("workload pequeno ou dev → RDS; performance/escala → Aurora"), mas sem números.
**Confiança:** Alta — os números específicos (failover <30s Aurora vs Multi-AZ RDS, até 15 réplicas Aurora vs 5 RDS) vêm da referência de skill `tech-mentor-infra/references/cloud/aws.md`, que confirma e detalha a heurística qualitativa da fonte.

**Claim:** Lambda não é adequado para tráfego constante e previsível — nesse regime, EC2 costuma ser mais barato — e tem um teto rígido de 15 minutos de execução.
**Evidência:** Afirmação direta da fonte ao final da seção de Lambda.
**Confiança:** Alta — confirmado pela seção "Lambda Limitations que quebram o plano" da referência de skill (15min timeout, 10GB memória máx, cold start em VPC ~1s).

**Claim:** DynamoDB exige modelagem por padrão de acesso (não normalizado) — partition key para distribuição/localização, sort key para queries por range — e não é adequado para analytics complexos ou dados fortemente relacionais.
**Evidência:** Exemplo direto: partition key = customer ID, sort key = order date, para buscar pedidos de um cliente ordenados por data.
**Confiança:** Alta — modelagem por access pattern é o princípio fundamental documentado de DynamoDB, sem contradição com o restante da wiki.

**Claim:** SQS, SNS e EventBridge têm papéis distintos e não intercambiáveis: SQS para desacoplamento simples (fila, um consumidor por mensagem), SNS para notificar múltiplos consumidores (fan-out), EventBridge para arquiteturas event-driven mais complexas com filtragem detalhada e replay de eventos.
**Evidência:** Definições e regra de decisão apresentadas de forma direta pela fonte.
**Confiança:** Alta — consistente com a tabela de mensageria já presente na referência de skill (`tech-mentor-infra/references/cloud/aws.md`, seção "Mensageria & Eventos"), que aponta a mesma divisão de papéis.

**Claim:** ECS é mais simples e mais integrado nativamente com a AWS; EKS é mais portátil (multi-cloud) mas significativamente mais complexo operacionalmente — a escolha depende do quanto o time já conhece Kubernetes e da necessidade real de portabilidade.
**Evidência:** Comparação direta apresentada como conclusão da seção ECS/EKS/ECR.
**Confiança:** Alta — árvore de decisão detalhada na referência de skill (`ECS vs EKS — Decisão Detalhada`) converge integralmente com a heurística da fonte, incluindo a recomendação de que ECS Fargate é frequentemente a escolha certa para times pequenos.

---

## Entidades

Nenhuma entidade (pessoa, empresa, produto de terceiros) foi identificada na transcrição além da própria AWS/Amazon. Não há autor citado, canal identificado ou patrocinador — a transcrição bruta fornecida não trazia esses metadados.

- [[wiki/entities/amazon-web-services]] — sujeito central de toda a fonte; os 15 serviços descritos são todos produtos AWS

## Conceitos

- [[wiki/concepts/aws-iam]] — seção de abertura da fonte; reforça least privilege e MFA na conta root com exemplo prático de escopo mínimo de permissão
- [[wiki/concepts/ec2]] — famílias de instância (T/M/C/R) e os três modelos de preço (On-Demand/Reserved/Spot) com regra de uso por perfil de carga
- [[wiki/concepts/auto-scaling]] — ASG com min/desejado/máximo e gatilho por métrica (ex: CPU 70%), sempre acoplado ao ALB na arquitetura de referência
- [[wiki/concepts/amazon-s3]] — storage classes (Standard/IA/Glacier), lifecycle policies, versioning, Block Public Access e Event Notifications como gatilho de arquiteturas event-driven
- [[wiki/concepts/rds]] — Multi-AZ, failover automático, read replicas (até 5), engine gerenciada
- [[wiki/concepts/aws-lambda]] — cold start, Provisioned Concurrency, timeout de 15min, padrões de trigger (API Gateway, S3, EventBridge)
- [[wiki/concepts/dynamodb]] — partition key + sort key, modos Provisioned/On-Demand, DynamoDB Streams, casos ideais vs. não ideais
- [[wiki/concepts/api-gateway]] — REST vs HTTP API, integração com Lambda/EC2/ECS/DynamoDB direto, autorização via IAM/Cognito/Lambda Authorizer
- [[wiki/concepts/aws-cloudfront]] — Edge Locations, cache behaviors por path, Origin Access Control, integração com ACM e WAF
- [[wiki/concepts/aws-route-53]] — DNS com roteamento por latência, localização e failover automático
- [[wiki/concepts/ecs]] — task definitions, services, launch types EC2 vs Fargate
- [[wiki/concepts/aws-fargate]] — launch type serverless do ECS, mais simples que gerenciar EC2 diretamente
- [[wiki/concepts/escalabilidade-horizontal]] — ASG + ALB como mecanismo concreto de escalabilidade horizontal sob demanda

- [[wiki/concepts/load-balancer]] — ALB (camada 7) com roteamento por path/host/headers e health checks constantes, sempre acoplado ao ASG na arquitetura de referência

### Conceitos novos (stubs criados por esta fonte)

- [[wiki/concepts/vpc]] — rede isolada da AWS, subnets públicas/privadas, Security Groups; fundação de rede citada antes de qualquer serviço de computação
- [[wiki/concepts/aws-elasticache]] — Redis/Memcached gerenciado, cache sub-milissegundo, papel de cache na arquitetura de referência (entre Lambda e RDS)
- [[wiki/concepts/aws-sqs]] — fila (Standard vs FIFO), Dead Letter Queue, desacoplamento simples
- [[wiki/concepts/aws-sns]] — pub/sub, fan-out para múltiplas filas SQS
- [[wiki/concepts/aws-cloudwatch]] — métricas/logs/alarmes, Log Groups com retention, Logs Insights, X-Ray para tracing distribuído

---

## Ver também

- Nenhuma outra fonte da wiki cobre AWS com esta amplitude (visão panorâmica de 15 serviços); fontes existentes tendem a ser específicas por conceito (ver `wiki/concepts/aws-*` e `wiki/concepts/ec2.md`, `rds.md`, `ecs.md`, `dynamodb.md`, `api-gateway.md` individualmente).

---

## Perguntas Abertas

- **Autoria não identificada.** A transcrição bruta fornecida não incluía nome de canal, autor ou qualquer metadado de origem. Diferente de outras fontes recentes da wiki (ex: Augusto Galego, Erick Wendel), não há padrão de fala, patrocínio ou autorreferência que permita inferir autoria com confiança. Tratado como fonte anônima.
- **Nenhuma menção a custo real ou benchmark quantitativo** — toda a fonte é qualitativa/didática (percentuais de desconto Spot/Reserved e limites técnicos como 5TB/objeto S3 ou 128TB Aurora são specs públicas da AWS, não medições da fonte).
- **EventBridge, Cognito, Secrets Manager, Step Functions, Kinesis** foram cobertos na fonte apenas na seção final "visão rápida", com uma frase cada — não geraram stubs de concept-page dedicados nesta ingestão por não terem profundidade suficiente na fonte; podem ser criados quando uma fonte futura os aprofundar.

---

## Citações

> "200 serviços, um monte de siglas que assustam qualquer um que tá aprendendo, mas 90% das aplicações usam os mesmos 15 serviços — e se você dominar eles, constrói qualquer coisa."

> "Se a instância for comprometida, o dano é limitado." (sobre least privilege no IAM)

> "Produção estável em reserved, picos em on demand, batch em spot."

> "Você projeta pro padrão de acesso, e não pro modelo de dados normalizado." (sobre DynamoDB)

> "SQS entrega para um, SNS entrega para todos."

> "Cada bloco é substituível — você vai escolhendo baseado no seu caso de uso." (sobre a arquitetura de referência)
