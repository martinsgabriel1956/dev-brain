# Toolkit da AWS — Serviços Essenciais para Aplicações Escaláveis

**Formato:** transcrição de vídeo (idioma original: português — sem necessidade de tradução), limpa de erros de reconhecimento de fala, pontuada e organizada em seções por serviço.

## Abertura

Hoje a gente vai ver o nosso toolkit da AWS: quais são os serviços que a AWS nos dá para aprender, como a gente pode usar esses serviços, o que vai ser útil para a gente e como a gente vai construir aplicações que escalam utilizando a cloud.

A gente não vai abrir o console da AWS — o console da AWS é uma bagunça interminável e, se eu começar a abrir o console, esse vídeo vai demorar 35 horas e não a meia hora que eu quero que demore. A gente também não vai deployar nada em produção nesse vídeo. Planejo fazer outros vídeos em que eu utilizo essas coisas na prática, mostrando como configurar um ambiente que vai deployar automaticamente do GitHub para a AWS, do jeito que eu uso isso nas empresas em que trabalho.

Uma vez que você aprendeu a usar a AWS, uma vez que você aprendeu os serviços que ela oferece, você vai poder escolher alguma das ferramentas para fazer o deploy. Eu conheço e tenho experiência com CDK (Cloud Development Kit), um pouco de experiência com Serverless Framework e com CloudFormation. Existem outras maneiras de fazer isso: você pode usar Terraform, algum CI customizado no GitHub Actions e fazer algo mais manual (SSH para as máquinas da AWS puxando o código do Git), ou você pode usar Kubernetes de alguma forma. Mas esse vídeo não é sobre essas maneiras de fazer deploy — é sobre o ferramental da AWS em si.

## S3 (Simple Storage Service)

S3 é um bucket — um "balde", como o próprio nome diz — utilizado para armazenar vários tipos de informação. Você pode armazenar:

- Documentos e backups (inclusive backup de banco de dados)
- Dados arquivados (archive)
- Sites estáticos (um `index.html`, ou até sites um pouco mais complicados, principalmente combinado com CloudFront e algum tipo de CDN)
- Assets estáticos (imagens de um site, logos, coisas que não mudam)

**Prós:**
- Relativamente barato — não sai caro para a maioria das utilizações.
- Escalabilidade: dá para armazenar praticamente a quantidade de dados que você quiser, é muito difícil bater nos limites do S3.

**Contras:**
- Não é para ser usado como banco de dados — para alguns casos de uso não faz sentido, existe latência que incomoda.
- Não é barato se você acessa os dados com muita frequência. Ex.: um backup de banco de dados no S3, se acessado o tempo todo, sai mais caro do que usar um banco de dados de verdade. Embora o armazenamento em si seja barato, geralmente existe custo por acesso.
- (Observação: a forma de cobrança da AWS muda com o tempo — a AWS adiciona formas diferentes de cobrar, então isso pode não ser sempre verdade.)

Se você entender as limitações do S3 — não tem compute nativo, não tem file system nativo, você não vai rodar um servidor nele — ele é uma ferramenta fantástica para o que se propõe.

## EC2 (Elastic Compute Cloud)

EC2 é o building block básico da AWS — o "servidor" entre aspas. Você escolhe um tamanho de máquina (instância) com uma certa especificação e tem aquela máquina alocada. É usado para servidores no sentido amplo — geralmente web, mas não só: dá para rodar qualquer tipo de processamento em background numa EC2.

O EC2 é um serviço-base da AWS; outros serviços se utilizam dele. O grande pró de uma EC2 é a versatilidade: você tem basicamente o que você quiser. O grande contra é que você paga pelo **tempo em que tem a máquina**, não pela computação em si. Se você alugar uma máquina, deixá-la rodando um mês sem fazer nada, o custo é o mesmo. Isso também é vantagem: se você usar 100% da máquina o tempo todo, você está pagando exatamente pelo que alugou. (De novo, isso depende de como a AWS decide cobrar, que pode mudar.)

Quando a gente deploya uma aplicação para produção, a gente não pensa em deployar um único servidor — é bem difícil subir em produção uma única máquina EC2 e lidar com todo o tráfego de uma aplicação com ela. O que acontece se essa máquina cair? Por isso geralmente existe alguma forma de orquestração em cima do EC2.

## ECS (Elastic Container Service)

ECS serve para fazer orquestração de servidores em cima do EC2. Ela dá suporte a containers Docker e permite clusterização — ao invés de subir um único EC2, você sobe um cluster de EC2s. Permite deployar aplicações num cluster. Também dá para usar Fargate junto com ECS.

Dado o que se propõe, o ECS simplifica escalar servidores/aplicações, porque é mais fácil usar várias EC2 através do ECS do que provisionar EC2 manualmente uma por uma. É um serviço de orquestração de containers geralmente usado em cima de EC2, mas não é obrigatório — dá para usar ECS sem EC2, embora seja o mais comum.

**Vantagem:** permite escalar baseado na demanda — um serviço de orquestração de containers pode provisionar instâncias a mais para acompanhar a demanda, permitindo otimização de recursos (ex.: menos servidores de madrugada, mais no horário de pico).

**Contras:**
- Mais complexo de configurar do que um único servidor grande.
- Vendor locking: quanto mais serviços específicos da AWS você usa, mais difícil fica sair da AWS depois.
- Escalar automaticamente também escala o seu custo — se o app explodir em uso (configurado de forma serverless com Fargate) e você não conseguir monetizar em cima disso, pode gerar custo excessivo.

## Load Balancer (ALB — Application Load Balancer)

Load Balancer distribui a carga (load) da aplicação — geralmente requests — entre diferentes destinos. Um usuário faz um request para o Load Balancer, e o Load Balancer direciona esse request para diferentes servidores (podem ser instâncias EC2, clusters diferentes, ou até destinos heterogêneos — parte do tráfego para um cluster EC2, parte para Lambdas). O propósito é não sobrecarregar um único servidor e fazer uma distribuição decente baseada em regras configuradas.

A regra de distribuição não precisa ser um-a-um sequencial (isso seria um algoritmo de round robin) — existem outros algoritmos de distribuição de tráfego.

O ALB (Amazon Load Balancer) permite distribuir tráfego baseado em rotas: por exemplo, requests para `/produtos` vão para um cluster de servidores, requests para `/admin` vão para outra máquina. Isso é possível porque o ALB é um load balancer de camada 7 (aplicação/HTTP) do modelo OSI — se não fosse, não daria para balancear com base em rotas.

**Contras:** custo pode ser maior do que load balancers mais clássicos/baratos, e dificuldade de configuração.

**Prós:** routing avançado (baseado em rotas), SSL termination, suporte a WebSockets, suporte a health checks — é um load balancer bastante completo.

Nota geral: a dificuldade de configuração parece quase proposital na AWS — quanto mais difícil configurar, mais difícil configurar um setup barato.

## Fargate

Fargate é um serverless compute engine. Isso significa que você não vai precisar gerenciar as instâncias do seu servidor — você talvez nem saiba qual é a infra rodando por baixo. O propósito do Fargate é eliminar a necessidade de provisionar, configurar e escalar clusters ou lidar com máquinas virtuais e containers diretamente. Você define e deploya containers, e a AWS lida com infraestrutura, escalabilidade e patching.

**Prós:** reduz complexidade; custo que escala com o uso/demanda real.

**Contras:** custo pode ficar elevado dependendo do workload — dependendo do caso, pode ser mais barato rodar em Lambda ou em EC2 tradicional do que em Fargate.

## Elastic Beanstalk

Elastic Beanstalk é um platform as a service (PaaS). Permite deployar aplicações sem se preocupar muito com a infraestrutura — ele cuida de provisionar infra e escalabilidade. Também permite customizar essa infra: dá para configurar load balancers, EC2, RDS, S3, etc., por trás dele.

**Prós:** configuração relativamente simples (na opinião de quem fala) e custo mais atrativo do que outras opções para aplicações web mais simples (front-end + back-end, sem muita complexidade, em qualquer framework — Django, Spring Boot, Rails, Go etc.), porque o Beanstalk tende a ser mais eficiente em alocar exatamente o quanto de infra é necessário. Como não é serverless (a infra por baixo costuma ser EC2), o custo tende a ser atrativo para aplicações de baixo tráfego.

**Contras:**
- Vendor lock-in: difícil migrar de Elastic Beanstalk para outra infra.
- Simples para casos de uso básicos, mas casos de uso mais avançados têm complexidade adicional para configurar corretamente.
- Como o Fargate, é um pouco "caixa preta" — às vezes é difícil entender o que deu certo ou errado.

## Lambda

Lambda é a menor unidade de serverless da AWS — permite rodar código sem provisionar servidores. A grande sacada é o modelo pay-per-use: dá para ver quanto custa, por exemplo, 1 milhão de requests no Lambda, ou quanto custa cada request que dura 10 segundos. Em aplicações web reais, o Lambda geralmente é usado numa pegada de "um endpoint, uma invocação de Lambda".

**Prós:** relativamente barato (muito dependente do caso de uso — se o caso de uso é adequado para Lambda, é barato; se não é, fica caro); escalabilidade praticamente infinita, e rápida.

**Contras:**
- Escalabilidade infinita pode gerar custo infinito: se um usuário malicioso fizer um trilhão de requests e nada prevenir isso, o custo é proporcional. Um servidor tradicional que recebe 1 trilhão de requests provavelmente cai (crash); um Lambda provavelmente vai tentar executar todos.
- Timeout: se um request demora muito para processar, dá timeout e o Lambda não retorna.
- Lambda geralmente tem pouca memória RAM alocada por padrão; dá para aumentar, mas o custo sobe proporcionalmente.
- Cold start: o primeiro request depois de um período sem uso (ex.: ~15 minutos de inatividade) é lento, porque a AWS precisa provisionar a infra antes de o código ficar pronto para receber requests. Requests subsequentes são rápidos.
- **Ponto pouco discutido:** você paga pelo tempo total que o Lambda fica ativo resolvendo um request, mesmo que boa parte desse tempo seja gasto esperando I/O (uma API externa, um banco de dados), e não computando de fato. Exemplo dado: um request de 15 segundos onde só ~30ms são processamento de fato (10ms no início, 20ms no fim) e os ~14s do meio são espera por uma API externa e por um banco de dados. Você paga pelos 15 segundos inteiros. Num servidor tradicional (não serverless), esse tempo de espera por I/O é tempo em que o servidor poderia estar atendendo outras requests — não necessariamente é tempo morto. Então um dos contras do serverless em Lambda é que você pode acabar pagando mais caro por tempo ocioso (waiting on I/O) do que pagaria num servidor que consegue reaproveitar esse tempo para outras requisições.

Mesmo assim, quem fala gosta bastante de Lambda — usou em duas das últimas três empresas em que trabalhou.

## API Gateway

A forma mais comum de encaminhar requests até um Lambda num contexto web é através de um API Gateway — a "porta da frente" das APIs. O usuário/frontend envia o request para o API Gateway, e o API Gateway decide para onde ele vai: pode encaminhar para um Lambda específico baseado na rota (ex.: `/user` vai para o Lambda de usuário, `/produtos` vai para o Lambda de produtos), ou para uma EC2. Nesse sentido, o API Gateway acaba sendo um pouco parecido com o Load Balancer, mas o intuito principal não é balancear carga.

**Prós:** ótimo suporte de integração com o ecossistema AWS (Lambda, Cognito, IAM, autorizers customizados para autorizar ou não um request).

**Contras:** custo por request; adiciona uma certa latência a cada request resolvido (pequena, mas existe); tem timeout (como fica entre usuário e servidor, o próprio API Gateway tem um timeout); mais vendor lock-in.

## Step Functions

Step Functions permite coordenar workflows complexos — o modelo mental é uma máquina de estados. Você tem uma porta de entrada que invoca, por exemplo, um Lambda de processamento de imagem; dependendo do resultado (sucesso ou falha), o fluxo segue por caminhos diferentes — falha pode ir para uma dead letter queue, sucesso pode seguir para outro processamento (metadados, IA na imagem) e depois cair num banco de dados. É possível montar uma máquina de estados que executa diferentes passos formando um workflow customizado.

Step Functions encorajam modularidade — quebrar tarefas que tradicionalmente seriam únicas em pedaços menores — e têm suporte de integração para retries e filas. O preço é baseado em transições de estado.

**Contra principal:** é uma solução com bastante vendor lock-in, e para a maioria das empresas, na maioria dos casos, é complexidade demais. Dentro da lógica interna do seu próprio servidor você provavelmente já tem coisas que se assemelham a máquinas de estado, resolvidas de outras formas (ex.: eventos emitidos pelo banco de dados, um Kafka para troca de mensagens). Acaba sendo um caso de uso bem específico para fazer sentido — arquiteturas orientadas a eventos.

## RDS (Relational Database Service)

RDS é uma máquina que você aluga/provisiona para rodar um banco de dados relacional. Dá suporte aos bancos relacionais mais usados (SQL). Não dá suporte a NoSQL (não foi visto sendo usado para isso). O nome já diz: **r**elational **d**atabase **s**ervice.

Se você está no ecossistema AWS, você provavelmente vai usar RDS; se não está, provavelmente não vai. Preço é adequado, features são as esperadas: observabilidade, escalar se quiser, backups — tudo isso tem custo.

## DynamoDB

DynamoDB é o banco de dados NoSQL da AWS, e é o banco NoSQL que, em termos de funcionalidade, quem fala mais gosta. O modelo mental é o de um key-value store — como um hash map, com uma **hash key** e uma **sort key** (duas chaves para acessar um item, usadas para dar mais performance — teoricamente só uma seria necessária). Dá para guardar documentos, com esquema flexível — as vantagens e desvantagens usuais de NoSQL.

**Por que gosta tanto:**
- Escalabilidade "do zero à escala global" — Global Tables permitem escalabilidade global e distribuída de forma bem robusta.
- Latência muito baixa, principalmente com muitos dados, comparado a outros tipos de serviço.
- Bom suporte a eventos: o Dynamo reage a eventos e também emite eventos.

**Contra:** custo. Geralmente é pay-per-use por request, e esse custo pode ficar muito alto para workloads com muitas requisições. Também existe uma certa curva de aprendizado para usar com eficiência.

## Serviços cobertos rapidamente

- **SQS (Simple Queue Service):** serviço de filas — o que você esperaria de um serviço de fila. Útil, por exemplo, quando um servidor gera itens que vão para uma fila de processamento para serem processados depois.
- **SNS (Simple Notification Service):** parecido com o SQS, usado para aplicações no modelo pub/sub (publisher/subscriber), ideia de troca de mensagens.
- **CloudWatch:** usado principalmente para logs — inclusive erros dentro do servidor, consultáveis pelo console. Usado para quase tudo por conveniência: é fácil ver para onde o request foi e acessar os logs.
- **Secrets Manager:** armazena segredos — chaves de API, credenciais de banco de dados etc.
- **CloudFront:** CDN — distribuição de conteúdo. Pode ser usada em conjunto com S3 para entregar um site inteiro só com o arquivo estático no S3 (ex.: um `index.html`). Serve para entregar HTML, imagens, vídeo, áudio, com baixa latência para o usuário.
- **Amplify:** hospedagem de aplicações full-stack, funciona bem com frameworks como Next.js. Usado, por exemplo, para hospedar uma single-page application em React: um front-end relativamente simples, sem custo muito alto, configurando o domínio (a configuração de domínio em si é feita em outro serviço, provavelmente Route 53). Bom para MVPs e aplicações pequenas sem um backend muito complexo; quando o backend fica mais complexo, geralmente vale sair do Amplify.

## Fechamento

Isso é o essencial do toolkit da AWS coberto no vídeo — os "20% dos serviços que compõem efetivamente 80%" do que é usado na prática. A AWS tem centenas de serviços; esse vídeo cobriu o subconjunto mais recorrente para quem constrói aplicações web que precisam escalar. Promessa (não garantida) de um vídeo futuro fazendo um exemplo prático: um API Gateway com CDK ou SAM direcionando requests para Lambdas diferentes (ex.: `users.js`, `products.js`), mostrando o roteamento configurado via infraestrutura como código.

**Nota:** o vídeo contém um bloco de patrocínio de uma empresa de contabilidade online (Agilize) no meio do conteúdo, sem relação técnica com o tema — omitido desta transcrição por não ser conteúdo técnico.
