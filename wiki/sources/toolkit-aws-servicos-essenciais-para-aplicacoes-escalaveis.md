---
type: source
title: "Toolkit da AWS — Serviços Essenciais para Aplicações Escaláveis"
aliases: ["toolkit AWS", "80/20 da AWS", "serviços essenciais AWS"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 0
tags: ["aws", "cloud", "ec2", "s3", "lambda", "ecs", "fargate", "elastic-beanstalk", "rds", "dynamodb", "api-gateway", "load-balancer", "vendor-lock-in", "serverless", "arquitetura"]
skill: tech-mentor-infra
status: stable
source_file: "raw/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis.md"
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-08-04
---

# Toolkit da AWS — Serviços Essenciais para Aplicações Escaláveis

## TL;DR

Vídeo em português (transcrição, sem necessidade de tradução) que percorre o "80/20" da AWS — os serviços que, segundo quem fala, compõem a maior parte do uso real em aplicações web escaláveis, sem abrir o console. Cobre três formas concretas de computação (EC2 servidor tradicional, Fargate serverless-de-container, Lambda serverless-de-função), duas formas de orquestrar/simplificar deploy em cima delas (ECS e Elastic Beanstalk), roteamento de tráfego (ALB e API Gateway), coordenação de workflow (Step Functions), dois bancos gerenciados (RDS relacional, DynamoDB NoSQL) e uma passagem rápida por SQS, SNS, CloudWatch, Secrets Manager, CloudFront e Amplify. O fio condutor é sempre prós/contras de cada serviço, com ênfase recorrente em dois eixos: **custo por tempo alocado vs. custo por uso real** (a distinção central entre EC2 e Lambda) e **vendor lock-in** (quanto mais serviços proprietários da AWS um sistema usa, mais caro fica migrar depois).

## Key Claims

1. **EC2 cobra por tempo de máquina alugada, não por computação realizada** — uma instância ociosa custa o mesmo que uma sob 100% de carga.
   - Evidência: *"o grande contra da EC2 vai ser que você vai tá pagando pelo tempo em que você tem a máquina e não pela computação [...] se você alugar ali uma máquina, deixar a máquina um mês rodando e não fizer absolutamente nada nessa máquina, o seu custo vai ser o mesmo."*

2. **Lambda paga pelo tempo total de execução do request, incluindo tempo de espera por I/O (rede, banco de dados), não só pelo processamento de CPU efetivo** — um contraste direto com um servidor tradicional, onde esse tempo ocioso de I/O pode ser reaproveitado para atender outras requisições em paralelo.
   - Evidência: exemplo detalhado de um Lambda de 15 segundos onde ~30ms são processamento real (10ms início + 20ms fim) e ~14s são espera por API externa e banco de dados: *"você pagou aqui por sei lá 10 milissegundos no início, 20 milissegundos de processamento no final e 14 segundos em que nada estava sendo computado no Lambda [...] você efetivamente pagou por uma quantidade infinitamente maior do que o processamento que de fato ocorreu."*

3. **Escalabilidade "infinita" de serviços serverless (Lambda, Fargate) é também exposição a custo "infinito"** sem limites de uso configurados — ao contrário de um servidor tradicional, que tende a cair (crash) sob carga excessiva em vez de continuar processando e cobrando indefinidamente.
   - Evidência: *"se algum usuário malicioso fizer um trilhão de requests pro seu servidor [...] você pediu para a AWS executar um trilhão de computações ali, a AWS vai fazer [...] existe um custo aqui, porque se o seu servidor receber um trilhão de requests ele vai crashar. Se o seu Lambda receber um trilhão de requests, provavelmente um trilhão de requests vão ser executados."*

4. **ALB é um load balancer de camada 7 (aplicação), o que é o que permite roteamento baseado em rota HTTP** (ex.: `/produtos` vs. `/admin` para destinos diferentes) — um load balancer de camada mais baixa não teria essa capacidade.
   - Evidência: *"consegue fazer routing mais avançado [...] eu acho que se não seria possível fazer esse balanceamento baseado em rotas [...] esse aqui é um load balancer de camada 7 da OSI."*

5. **Quanto mais serviços proprietários da AWS um sistema adota (ECS, Elastic Beanstalk, API Gateway, Step Functions), maior o vendor lock-in** — migrar para outro provedor ou para infraestrutura própria fica progressivamente mais difícil e caro. Step Functions é citado como o caso mais extremo de lock-in entre os serviços cobertos, e por isso descartado pelo autor em empresas onde trabalhou.
   - Evidência: *"quanto mais coisas da AWS a gente usa, mais difícil é sair da AWS no futuro [...] [Step Functions] preciso falar aqui que é super lock-in, muito lock-in, muito preso na AWS. Eu não utilizei nas empresas que eu trabalhei porque a gente pensou que era lock-in demais."*

6. **DynamoDB usa duas chaves (hash key + sort key) para indexar itens, embora uma só bastasse em teoria** — a segunda chave existe para ganho de performance, não por necessidade estrutural do modelo de dados.
   - Evidência: *"você vai ter duas keys para acessar algum item no Dynamo. Essas chaves são utilizadas para dar mais performance. Teoricamente você só precisaria de uma aqui."*

7. **Elastic Beanstalk (PaaS) tende a ter custo mais atrativo que orquestração manual via ECS para aplicações web simples**, porque aloca infraestrutura de forma mais próxima da necessidade real — mas cai em complexidade adicional de configuração assim que o caso de uso foge do básico.
   - Evidência: *"eu acho que a configuração é relativamente simples e eu acho que o custo acaba sendo um pouco mais atrativo do que as outras opções [...] casos de uso mais avançados vão ter uma complexidade adicional."*

## Entities

- [[wiki/entities/amazon-web-services]]

## Concepts

- [[wiki/concepts/ec2]] (novo)
- [[wiki/concepts/amazon-s3]] (novo)
- [[wiki/concepts/ecs]] (novo)
- [[wiki/concepts/aws-fargate]] (novo)
- [[wiki/concepts/elastic-beanstalk]] (novo)
- [[wiki/concepts/aws-lambda]] (novo)
- [[wiki/concepts/step-functions]] (novo)
- [[wiki/concepts/rds]] (novo)
- [[wiki/concepts/dynamodb]] (novo)
- [[wiki/concepts/load-balancer]]
- [[wiki/concepts/api-gateway]]
- [[wiki/concepts/secrets-management]]
- [[wiki/concepts/aws-cloudfront]]
- [[wiki/concepts/vendor-lock-in-cloud]]
- [[wiki/concepts/serverless]] (mencionado, sem página própria — ver open question)

Mencionados sem página dedicada (cobertura breve na fonte, não central): SQS, SNS, CloudWatch, Amplify.

## Open Questions

- A fonte afirma que RDS "não dá suporte a NoSQL" com baixa confiança do próprio autor ("vamos presumir que não [...] não sei também") — isso é tecnicamente correto (RDS é só para engines relacionais: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server; NoSQL gerenciado na AWS é DynamoDB/DocumentDB/Keyspaces), mas vale registrar que a fonte não afirma isso com certeza.
- A wiki ainda não tem uma página `wiki/concepts/serverless.md` central que unifique Lambda, Fargate e Aurora Serverless sob o mesmo trade-off (pay-per-use vs. cold start vs. custo de tempo ocioso de I/O) — esta fonte é a primeira a articular claramente o argumento de "custo de tempo ocioso em I/O" como contra específico do modelo serverless de função (Lambda), que pode valer a pena promover a uma página própria quando houver mais fontes sobre o tema.
- A fonte não entra em detalhes de EKS (Kubernetes gerenciado na AWS) — cobre EC2, ECS e Fargate como as três formas de computação em container/servidor, mas não posiciona EKS na mesma árvore de decisão. Fica como gap explícito, já coberto de forma mais completa na referência da skill (`tech-mentor-infra/references/cloud/aws.md`, seção "EKS vs ECS vs Lambda — Árvore de Decisão") mas não na wiki-fonte ainda.
- Comparação de custo entre Fargate, Lambda e EC2 é qualitativa ("depende do workload") em toda a fonte — nenhum número concreto é dado, ao contrário de, por exemplo, [[wiki/sources/aws-infraestrutura-global]] que tem métricas concretas de infraestrutura.

## Raw Quotes

> "Você pediu para a AWS executar um trilhão de computações ali, a AWS vai fazer."

> "A dificuldade de configuração parece até proposital, porque quanto mais difícil configurar o negócio, mais difícil você configurar um negócio barato."

> "RDS é onde fica o banco de dados. Tipo, é isso."

> "O legal do Dynamo é que eles têm uma global table [...] você consegue ter uma escalabilidade global e distribuída de maneira muito muito bizarra."

> "Dentro da sua própria lógica interna do servidor [...] você provavelmente já tem coisas que se assemelham a máquinas de estado, e você provavelmente já fez isso de maneiras diferentes."

## Key Sources (páginas que citam esta fonte)

—
