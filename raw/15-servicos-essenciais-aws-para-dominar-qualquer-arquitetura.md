# 15 Serviços Essenciais da AWS Para Dominar Qualquer Arquitetura

> Transcrição de vídeo em português (áudio original em pt-BR, sem tradução necessária). ASR bruto sem pontuação, limpo e organizado em seções temáticas por serviço para leitura. Conteúdo técnico preservado integralmente; apenas pontuação, quebras de parágrafo e subtítulos foram adicionados.

## Gancho / Contexto

A AWS tem 200 serviços — um monte de siglas que assustam qualquer um que tá aprendendo. Mas 90% das aplicações usam os mesmos 15 serviços, e se você dominar eles, constrói qualquer coisa. Hoje a gente passa por cada um deles: o que cada um faz, quando usar, e como se conectam.

## IAM — Identity and Access Management

Antes de qualquer serviço você precisa entender o IAM, o sistema de segurança da AWS: quem pode fazer o quê, onde e quando.

Quatro conceitos principais:
- **Users** — pessoas.
- **Groups** — agrupam users e herdam permissões.
- **Roles** — identidades temporárias que serviços assumem.
- **Policies** — JSONs que definem o que pode e o que não pode.

O princípio mais importante é o **least privilege** (menor privilégio): você dá o mínimo necessário para cada coisa funcionar. Se uma instância precisa ler do S3, crie uma role com exatamente essa permissão — se a instância for comprometida, o dano é limitado.

Ative MFA (multi-factor) na conta root e nunca use a conta root para tarefas do dia a dia. É segurança básica, mas ainda muita gente ignora.

## VPC — Virtual Private Cloud

Com a segurança configurada, antes de subir qualquer coisa você precisa de uma rede. O VPC é sua rede isolada dentro da AWS: você define um range de IPs, cria subnets e controla quem entra e quem sai.

Existem dois tipos de subnets:
- **Públicas** — têm rota pro Internet Gateway, recebem tráfego da internet.
- **Privadas** — isoladas, só saem pela internet via NAT Gateway.

**Security Groups** são os firewalls: você define regras de entrada e saída no nível da instância.

Arquitetura mais típica: load balancer na subnet pública, aplicação na subnet privada, banco em subnet privada ainda mais isolada — três camadas de defesa.

## EC2 — Elastic Compute Cloud

Com a rede pronta, agora sim: subir os servidores. EC2 é o servidor virtual na nuvem. Você escolhe o tipo de instância, o sistema operacional, e em minutos tem um servidor rodando.

Famílias mais comuns:
- **T** — workloads variáveis, ambientes de dev/teste.
- **M** — uso geral em produção.
- **C** — computação mais pesada.
- **R** — quando exige muita memória.

O que realmente importa são os **modelos de preço**:
- **On-Demand** — paga pelo uso, sem compromisso, mais caro.
- **Reserved** — compromissos de 1 a 3 anos, desconto de até 70%.
- **Spot** — usa capacidade ociosa, desconto de até 90%, mas pode ser interrompido a qualquer momento.

Na prática: produção estável em Reserved, picos em On-Demand, batch em Spot.

**EBS** é o armazenamento de bloco, os discos das instâncias. Regra geral: use GP3 para quase tudo, e io2 quando precisa de IOPS garantido em bancos exigentes.

## Auto Scaling Groups + Application Load Balancer

Com um EC2 rodando, e quando o tráfego aumenta? EC2 sozinho não escala — precisa de Auto Scaling Groups e Load Balancers.

O **Auto Scaling Group (ASG)** mantém instâncias EC2 saudáveis rodando. Você define o mínimo, o desejado e o máximo. Se a CPU passar de, digamos, 70%, escala para cima; se cair, escala para baixo.

O **Application Load Balancer (ALB)** distribui tráfego entre as instâncias. Opera na camada HTTP, pode rotear por path, host e headers, e faz health checks constantes — se uma instância falha, remove do pool automaticamente.

Arquitetura mais clássica: ALB na frente, ASG atrás. Tráfego aumenta, ASG escala, ALB distribui. Tráfego cai, ASG reduz e você economiza.

## S3 — Simple Storage Service

Com computação e escalabilidade resolvidos: e os arquivos, imagens, vídeos e backups? S3 é o armazenamento de objetos da AWS. Você guarda qualquer coisa dentro de buckets: imagens, vídeos, backups, logs, etc. Objetos podem ter até 5 TB, com durabilidade de 11 noves.

**Storage classes**:
- **Standard** — dados acessados frequentemente.
- **Standard-IA** — dados raramente acessados, mas que precisam estar disponíveis rápido.
- **Glacier** — arquivos de longo prazo, recuperação em minutos a horas.

**Lifecycle policies** movem objetos entre classes automaticamente (ex: depois de 30 dias vai para IA, depois de 90 para Glacier).

**Versioning** protege contra deleção acidental. **Block Public Access** bloqueia acesso público mesmo que você configure errado.

**S3 Event Notifications** são poderosos: upload de um arquivo pode disparar uma Lambda; deleção pode mandar mensagem pro SQS. É a cola de muitas arquiteturas event-driven.

## RDS — Relational Database Service

Agora sabemos como armazenar objetos, mas e os dados estruturados? Para isso você precisa de um banco. RDS é o banco de dados relacional gerenciado da AWS. Você escolhe a engine (Postgres, MySQL, MariaDB, Oracle, SQL Server). A AWS cuida do patching, backups e failover; você cuida do esquema, queries e índices.

### Availability Zones e Multi-AZ

Cada região da AWS (ex: São Paulo) tem múltiplas AZs. Cada AZ é um data center físico separado, com energia, rede e refrigeração independentes — perto o suficiente para latência baixa entre elas, distante o bastante para que um desastre numa AZ não afete a outra.

**Multi-AZ** usa isso para dar alta disponibilidade: instância primária numa AZ, standby em outra AZ, replicação síncrona entre elas. Se a primária cai (falha de hardware, rede, ou a AZ inteira), o failover é automático — o DNS aponta pro standby e a aplicação continua rodando. Detalhe importante: a standby não recebe tráfego de leitura, é só para disponibilidade.

**Read replicas** escalam leitura: escritas vão pro primário, leituras vão pras réplicas — dá para ter até cinco.

## Aurora

Aurora é o banco nativo da nuvem da AWS, compatível com Postgres e MySQL, mas com armazenamento distribuído em três AZs. Cresce automaticamente até 128 TB, suporta até 15 réplicas compartilhando o mesmo armazenamento, e o failover leva menos de 30 segundos.

**Aurora Serverless**: pago por uso, escala automaticamente, pode até pausar quando não tem tráfego — ideal para dev/teste e workloads imprevisíveis.

Regra de escolha: workload pequeno ou ambiente de dev → RDS. Precisa de performance/escala → Aurora.

## Lambda

Com bancos relacionais cobertos, agora o serverless. Lambda é computação sem servidor: você escreve código e a AWS executa, sem servidor para você gerenciar. Você faz deploy de uma função, define triggers, e o código roda quando esses eventos acontecem (API Gateway para HTTP, S3 para upload, SQS para filas, EventBridge para schedules).

Quando o evento chega, a AWS cria um contêiner e executa — com milhares de eventos simultâneos, milhares de contêineres paralelos são criados.

**Cold start** é a latência de primeira execução; depois o contêiner fica quente e é reutilizado. Se o cold start incomoda, **Provisioned Concurrency** mantém contêineres prontos.

Modelo de preço: por execução e tempo de processamento (primeiro milhão de requests/mês é grátis, no momento desta transcrição).

Padrões mais comuns: API Gateway + Lambda para backend; upload no S3 disparando Lambda para processar; EventBridge agendando Lambda para tarefas periódicas.

Ponto importante: timeout máximo de 15 minutos. Para tráfego constante e previsível, EC2 geralmente é mais barato.

## DynamoDB

DynamoDB é o banco NoSQL da AWS. Escala praticamente ilimitada, latência de milissegundos de forma consistente. A diferença importante: você projeta pro padrão de acesso, não pro modelo de dados normalizado.

A **partition key** distribui e localiza dados; a **sort key** permite queries por range (ex: partition key = customer ID, sort key = order date → busca todos os pedidos de um cliente ordenados por data).

Dois modos de capacidade: **Provisioned** (quando você sabe o padrão) e **On-Demand** (quando não sabe — mais caro por request, menos preocupação).

**DynamoDB Streams** captura mudanças na tabela em tempo real; uma Lambda consome para sincronizar, reagir e auditar.

Casos ideais: sessões, leaderboards, IoT, carrinhos de compras, metadata. Não ideal para analytics complexos ou dados relacionais.

## API Gateway

Já sabemos como guardar dados, mas como o mundo exterior acessa? API Gateway é como você expõe suas APIs pro mundo. Duas opções: **REST API** (mais features) e **HTTP API** (mais simples, mais barato). Comece com HTTP API e migre pra REST se precisar.

Integração mais comum: com Lambda (a request chega no gateway, invoca a Lambda, retorna a resposta), mas também pode fazer proxy para EC2, ECS, ou escrever direto no DynamoDB sem Lambda no meio.

Para autorização: IAM para chamada service-to-service, Cognito para validação de JWT, Lambda Authorizers para lógica customizada.

**Throttling** protege seu backend de sobrecarga. Dá para usar domínios customizados com certificado SSL via ACM.

## CloudFront

A API tá respondendo, mas com usuários espalhados pelo mundo, para resolver latência você precisa de CDN. CloudFront é a CDN da AWS, com mais de 400 pontos pelo mundo. Sem CDN, cada request de um usuário distante precisa viajar pelo mundo todo; com CloudFront, o Edge Location mais próximo responde em milissegundos.

Origins podem ser S3, Load Balancer, API Gateway, qualquer servidor HTTP. **Cache behaviors** definem como cachear por path (ex: `/api/*` com cache curto, `/static/*` com cache longo).

HTTPS vem com certificado gratuito pelo **ACM** (AWS Certificate Manager): você registra seu domínio, o ACM emite e renova o certificado automaticamente.

**Origin Access Control** garante que só o CloudFront acessa seu S3, não o usuário diretamente. O **WAF** protege contra SQL Injection, cross-site scripting e bots maliciosos.

## CloudWatch

Tudo servido e cacheado, mas como saber se tá funcionando? CloudWatch é o hub de observabilidade da AWS, baseado em três pilares: **métricas, logs e alarmes**.

Os serviços da AWS publicam métricas automaticamente (CPU, latência, erros, número de requests); você pode publicar métricas customizadas da sua aplicação também. Logs vão para **Log Groups** — configure a retention, senão acumula infinitamente e fica cada vez mais caro. **Logs Insights** deixa você pesquisar e agregar logs com uma query language própria.

**Alarmes** monitoram métricas e disparam ações (ex: CPU passa de 80%, o alarme dispara, SNS notifica, ASG escala).

**X-Ray** é tracing distribuído: cada request tem um trace ID que mostra o caminho completo (ex: API Gateway → Lambda → DynamoDB), identificando gargalos e erros por componente.

## Mensageria: SQS, SNS e EventBridge

Quando serviços precisam conversar entre si, a AWS oferece três serviços de mensageria, cada um com seu propósito.

**SQS** é a fila: o produtor manda mensagem, o consumidor processa quando puder. Se o consumidor cai, a mensagem espera — ajuda a desacoplar sistemas e absorver picos de tráfego. Dois tipos: **Standard** (throughput ilimitado, entrega pelo menos uma vez) e **FIFO** (ordem garantida, processamento exactly-once). A **Dead Letter Queue** captura mensagens que falharam várias vezes, para análise posterior.

**SNS** é pub/sub: você publica num tópico, todos os inscritos recebem. SQS entrega para um; SNS entrega para todos. Padrão mais comum: SNS publica e múltiplas filas SQS consomem em paralelo, cada fila processando de forma independente.

**EventBridge** é a evolução do SNS para arquiteturas event-driven: recebe eventos de serviços AWS, da sua aplicação e até de SaaS externos. Filtragem mais detalhada, e a feature principal é o **replay** de eventos.

Regra geral: SQS para desacoplamento simples, SNS para notificar vários consumidores, EventBridge para eventos mais complexos.

## ECS, EKS e ECR

ECS é a orquestração de contêineres gerenciada da AWS: se você usa Docker, o ECS roda seus containers em escala. Você define **task definitions** (imagem, CPU, memória); **services** mantêm N tasks rodando e integram com load balancer.

Dois launch types: **EC2** (você gerencia a instância) e **Fargate** (serverless). Fargate é mais simples; EC2 faz sentido quando precisa de GPU ou controle mais fino.

**ECR** armazena suas imagens Docker — privado, integrado com IAM, com scan de vulnerabilidades.

Diferença entre ECS e EKS: ECS é mais simples, integrado nativamente com AWS. EKS é Kubernetes gerenciado — mais portátil, mas muito mais complexo.

## Serviços Adicionais (visão rápida)

- **Route 53** — DNS da AWS: traduz domínios em IPs, com roteamento inteligente (por latência, localização, ou failover automático se um endpoint cair).
- **Cognito** — autenticação gerenciada: cadastro, MFA, login social (Google, Apple), retorna token JWT que o API Gateway valida automaticamente.
- **Secrets Manager** — armazena credenciais e chaves de API, com rotação automática. **Parameter Store** é alternativa gratuita para configurações mais simples.
- **Step Functions** — orquestração de workflows: quando várias Lambdas precisam coordenar em sequência, com retry e tratamento de erros.
- **ElastiCache** — Redis ou Memcached gerenciado: cache em memória com latência de sub-milissegundo, para sessões, cache de queries, leaderboards.
- **Kinesis** — streaming de dados em tempo real, para logs, clickstream e IoT. Diferença pro SQS: Kinesis permite múltiplos consumidores lendo o mesmo dado simultaneamente, com replay.

## Arquitetura de Referência (juntando tudo)

Route 53 recebe o DNS e aponta pro CloudFront. CloudFront serve assets estáticos do S3 e roteia requests de API pro API Gateway. O Gateway autentica via Cognito e invoca a Lambda. A Lambda consulta o DynamoDB, faz cache no ElastiCache, manda mensagem pro SQS para processar de forma assíncrona. Um worker consome o SQS e atualiza o RDS. Enquanto isso, o CloudWatch monitora tudo.

Cada bloco é substituível: EC2 no lugar de Lambda, ECS no lugar de EC2, SNS no lugar de SQS — você escolhe baseado no seu caso de uso.

## Resumo por Categoria

- **Fundação**: VPC dá rede, IAM controla acesso.
- **Computação**: EC2, Lambda.
- **Armazenamento**: S3, EBS.
- **Banco de dados**: RDS e Aurora (relacional), DynamoDB (NoSQL).
- **Cache**: ElastiCache.
- **Rede**: Route 53, CloudFront, API Gateway.
- **Integração**: SQS, SNS, EventBridge.
- **Observabilidade**: CloudWatch, X-Ray.
