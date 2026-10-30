---
title: "Introdução ao Terraform — o que é, para que serve e como funciona (com prática)"
source_type: transcrição de vídeo (PT-BR, legenda automática)
author: "não identificado (canal de DevOps; menciona o 'Laboratório DevOps' e 14.000 inscritos)"
date_ingested: 2026-10-26
---

# Introdução ao Terraform — o que é, para que serve e como funciona

> Transcrição limpa (pontuação, parágrafos e termos corrigidos). Já em português; sem tradução. Correções de ASR: "Terraformer"/"Terraforme"/"Terraforming" → Terraform; "Terraformit"/"Terraform in" → Terraform init; "Terraform Plane" → Terraform plan; "WS"/"a WS" → AWS; "E2"/"S2"/"C2" → EC2; "MI" → AMI; "Gitab" → GitLab; "Terraformistry"/"register" → Terraform Registry; "ptf" → .tf; "Cubernets" → Kubernetes; "Asure"/"Ager" → Azure; "research"/"ressarces" → resource; "ridm" → README; "S1" → us-east-1 (dito "US East 1"); "Ubunto 26 22" mantido como "Ubuntu" (versão ilegível no ASR; o apresentador diz "26.04" depois); "Local Stack" → LocalStack. "Maria" é o apresentador se dirigindo ao espectador e foi mantido. Nome do apresentador não identificado.

## Abertura

Bem-vindo a mais um vídeo do canal. Hoje: **Terraform**, ferramenta fundamental para quem quer atuar como engenheiro de DevOps — "é muito, muito utilizada"; a dica é aprender Terraform. O vídeo é um "geralzão", uma introdução, parte de uma série para quem está tendo o primeiro contato com a ferramenta. Roteiro: o que é, para que serve, como funciona, e uma parte prática para fixar.

## O que é o Terraform

É uma ferramenta de **código aberto** (a comunidade pode contribuir com o desenvolvimento) e de **infraestrutura como código**.

Exemplo: uma aplicação que precisa de um banco de dados. A infraestrutura que ela precisa para rodar é o banco, o servidor (a máquina onde a aplicação roda) e a rede (para o servidor falar com o banco e para os clientes acessarem a aplicação via web).

**Infraestrutura como código:** para subir um servidor na AWS — a máquina virtual da AWS se chama **EC2** (Elastic Compute Cloud) —, o jeito padrão seria entrar na AWS, clicar em "criar instância", escolher sistema operacional, nome e os demais parâmetros. Com infraestrutura como código, em vez de clicar nos botões, **escreve-se um código que descreve exatamente o que se quer criar** ("quero uma instância EC2 com tal sistema operacional, de tal tipo e família") e o Terraform conversa com a **API da AWS** e cria o recurso.

Existem outras ferramentas que seguem o mesmo princípio (o apresentador pode trazê-las em vídeos futuros), mas o Terraform é uma das mais usadas porque se conecta a **diversas nuvens e tipos de provedores**.

## Para que serve

Serve para **provisionar, gerenciar e versionar a infraestrutura de forma segura e eficiente**. Três palavras-chave:

1. **Automação.** Escrever código automatiza o processo manual. Exemplo: surge a demanda de criar cinco instâncias EC2. Sem Terraform, seria criar a primeira, depois a segunda, repetindo o processo manual cinco vezes — repetitivo e desnecessário. Com Terraform, escreve-se o código uma vez e ele pode ser reutilizado quantas vezes for preciso.
2. **Versionamento.** Como é um arquivo, pode ser versionado (Git, GitHub, GitLab): dá para acompanhar o progresso da infraestrutura, ver o histórico de cada mudança e **quem do time alterou determinada configuração**. Problema comum quando não se versiona: criar uma instância com um padrão e outra com padrão/nome diferente; alguém esquece de colocar uma tag obrigatória; perde-se o padrão. Se for preciso aumentar a máquina (de 2 CPUs para 4), fazendo manualmente no console **não fica registrado** o valor anterior; como código, dá para saber que em determinado momento eram 2 CPUs e depois mudou.
3. **Multi-provedor.** O Terraform funciona para diversos provedores. Exemplo: instância EC2 na AWS, banco de dados no GCP, bucket no Microsoft Azure. Sem Terraform, seria preciso ir manualmente em cada nuvem, clicar e configurar. Com Terraform, escreve-se **um único código**, na linguagem do Terraform, que conversa com todas essas nuvens/provedores.

## Como funciona

O Terraform funciona de forma **declarativa**: você declara **o que quer** (o estado final/desejado) e ele faz o necessário para chegar lá. Ele **compara o que já existe com o que foi declarado**. Exemplo: já existe um servidor e o código declara três; o Terraform cria só **dois**, porque um já existia.

### Três pilares

1. **HCL** — a linguagem de programação do Terraform (assim como aplicações são escritas em Java ou Python, a infraestrutura é escrita em HCL). Os arquivos têm extensão **`.tf`**. É "extremamente fácil e simples de entender".
2. **Providers** — plugins que dizem ao Terraform **como se comunicar com a nuvem**. O provider da AWS conversa com a API da AWS para criar recursos na AWS. O apresentador gosta de dizer: "o provider é onde você vai criar". Para criar uma rede no Google Cloud, usa-se o provider da GCP, e assim por diante.
3. **State** — o **arquivo de estado** (`terraform.tfstate`, "TF State"). É um arquivo extremamente importante: nele o Terraform guarda **tudo o que já criou**. Ao criar uma instância na AWS, o Terraform cria um arquivo no diretório; quando se criam novos recursos ou se editam os existentes, ele **sempre olha para o state e compara com o novo estado**, aplicando as diferenças entre o state e o que foi declarado. "Toda vez que roda, o Terraform compara o state para saber o que vai alterar."

### Principais comandos e o fluxo

Fluxo: escrever o código → rodar no terminal.

- **`terraform init`** — baixa todos os providers declarados (ex.: o da AWS, o do Google, conforme o código) e **inicializa o diretório de trabalho**, criando arquivos de que o Terraform precisa para funcionar.
- **`terraform plan`** — "planejar": gera um **plano de execução** como saída no terminal, listando tudo o que vai criar ("vou criar uma máquina com dois CPUs, da família tal, com o nome tal, na AWS, com todos os parâmetros"). Olhando o plano, decide-se se aplica ou se muda algo no código; mudando, é preciso rodar o `plan` de novo. Nessa etapa o Terraform **compara o que está no state com o que está no código** para gerar o plano.
- **`terraform apply`** — **aplica** o plano de execução; é aí que de fato os recursos são criados no provedor (AWS, Google, tanto faz). Ao final, a infraestrutura está provisionada.

### Sintaxe básica

O Terraform trabalha com **blocos**: `tipo-do-bloco "tipo-específico" "nome" { argumentos }`. Abre-se chaves, inserem-se os argumentos e fecha-se; ao fechar a chave, o bloco termina. Cada tipo de bloco tem seus parâmetros e especificações. Exemplos mostrados:

- **`provider`** — o tipo específico é o provider. Exemplo com o provider **Google**: dentro do bloco, informa-se o projeto do Google e a região. Exemplo com o provider **AWS**: parâmetros específicos como região, conta, credenciais.
- **`resource`** — recursos a criar. Exemplo: `resource "aws_vpc" "exemplo" { ... }` cria uma **rede (VPC)** na AWS; `aws_vpc` é o tipo do recurso e `exemplo` o nome do bloco; dentro, parâmetros específicos do recurso.
- **`variable`** — exemplo: variável `instance_type`, com tipo `string`, descrição ("tipo da instância EC2") e **valor padrão** (`t2.micro`) caso não seja definida. Um `resource "aws_instance" "web"` pode então referenciar a variável em vez de um valor fixo; se nenhuma variável específica for definida, usa o padrão `t2.micro`. O apresentador diz que é um pouco mais complexo e que vai deixar o link da documentação oficial para aprofundar.

## Prática

### As duas documentações fundamentais

**1. Terraform Registry** (registry.terraform.io): onde está a documentação de **todos os providers**. Pensa-se sempre "com qual API/provedor quero me comunicar". Há providers da AWS, Azure, Google e também do **Kubernetes** — dá para criar pods, service accounts e clusters com Terraform (o apresentador oferece um vídeo/laboratório sobre isso se pedirem nos comentários).

Seguindo o exemplo da instância EC2 na AWS: a página do provider AWS mostra que é um **provedor oficial** — "muito importante que você veja isso, porque há muitos providers; é interessante usar os oficiais, que são mais seguros". Há também exemplos de **módulos** (que ele não detalha, mas recomenda estudar). Na documentação, a versão do provider (no momento, **6.54**) e o exemplo de uso do bloco `provider`. Mostra também como **autenticar**: é preciso ter conta na AWS, gerar credenciais e dar permissão ao Terraform para criar coisas na conta; pode-se passar Access Key e Secret Key direto no código, "obviamente não é uma boa prática, mas dá para fazer"; há várias outras formas, não detalhadas.

Pesquisando "instance" na seção EC2 → Resources → **`aws_instance`**. Toda página de resource segue o padrão: **exemplo de uso**; **Argumentos** (inputs: parâmetros que se podem inserir no bloco, obrigatórios e opcionais — por exemplo `region` é opcional e, se omitido, usa a região definida no provider; também `ami`, opções de CPU, zona de disponibilidade etc.); e **Atributos** (outputs: informações disponíveis depois que o recurso é criado, como o **ARN** — ID global do recurso na conta —, o DNS público etc.). Atributos podem ser usados como parâmetro de outros recursos.

**2. Documentação da linguagem Terraform**: ensina o HCL em detalhe — como configurar um bloco de recurso, providers, variáveis e vários outros blocos: **module, output, backend, data sources** etc. "É muito extenso e interessante que você veja e aprenda melhor sobre a linguagem."

### Laboratório (sandbox)

Dá para instalar o Terraform na máquina e usar o VS Code, mas como é só uma introdução ele usa o **sandbox interativo fornecido pelo próprio Terraform** (link na descrição). O ambiente dura **uma hora** e já vem com **Terraform instalado, Docker, LocalStack e a CLI da AWS configurada**: não se acessa a console da AWS diretamente, mas pela linha de comando da AWS se vê se os recursos foram criados. Passos: "Launch sandbox" → "Launch" → esperar alguns minutos → "Start". O ambiente tem terminal e um editor de código (como um VS Code) com alguns arquivos (`main.tf`, `terraform.tf`, README, limitations, LocalStack, arquitetura). O foco é `terraform.tf` e `main.tf`; o restante pode ser ignorado.

**Passo 1 — o provider (`terraform.tf`).** Já vem com o bloco `terraform` e a lista de provedores (`required_providers`) com a versão. Como o provider já está em versão mais recente (6.54), ele apaga o conteúdo e recria do zero: copia da documentação do Registry (botão "Use provider") o bloco `terraform { required_providers { aws = { source = ..., version = ... } } }` e o bloco `provider "aws" {}`. Para saber que parâmetros o bloco `provider` aceita, consulta a documentação do AWS Provider; no sandbox não precisa de credenciais (já configuradas), mas na máquina própria seria preciso. Insere somente a **região: `us-east-1`** (Norte da Virgínia).

**Por que vários arquivos `.tf`?** Por convenção, separa-se um arquivo para providers (`terraform.tf`, também comum `provider.tf`) e o `main.tf` para os recursos ("main" = principal). **Não é obrigatório**: pode haver vários arquivos, um para a EC2, outro para a rede etc., com qualquer nome — o importante é a extensão `.tf`. `main.tf` e `terraform.tf` são convenções.

**Passo 2 — o recurso (`main.tf`).** Apaga o exemplo que veio e, na documentação, pesquisa "instance" → `aws_instance` → copia **somente o bloco `resource`** do exemplo (não o bloco `data` que aparece junto, que ele diz que não vai explicar agora). Pontos importantes:

- O **tipo do recurso** (`aws_instance`) tem de ser **exatamente** o nome do recurso: o Terraform procura esse tipo específico no provider AWS; não se pode escrever, por exemplo, "instancia". É imutável.
- O **nome do bloco** (segundo rótulo) é livre — ex.: `minha_primeira_ec2`. Ele **não** é o nome da máquina na AWS; é apenas o nome do recurso dentro do código.
- O **nome da instância na AWS** vem da **tag `Name`** — no exemplo, `Hello World`.
- Para saber que parâmetros pode inserir: documentação → Argument Reference. Ele mantém simples: `instance_type` = **`t3.micro`** (família T3: 2 vCPU e 1 GB de RAM, "uma máquina bem pequenininha") e `tags`; remove a `ami` do exemplo (o que causará um erro de propósito).

**Passo 3 — `terraform init`.** No terminal, `ls` mostra `main.tf` e `terraform.tf`. Ao rodar `terraform init`, ele inicializa o backend, procura e instala o provider da AWS na versão especificada e informa que a configuração foi inicializada: "você pode agora começar a trabalhar com Terraform; comece rodando `terraform plan`".

**Antes do plan: verificar que não há nada na AWS.** Usa a CLI da AWS: `aws ec2 describe-instances` — a saída vem **vazia**, ou seja, nenhuma instância existe ainda.

**Passo 4 — `terraform plan` (com erro proposital).** O apresentador **simula um erro** ("nem sempre tudo são flores"): o plan falha dizendo que, para criar uma EC2, é preciso especificar **uma AMI ou um launch template**. Explicação: **AMI** (Amazon Machine Image) é o **sistema operacional** da máquina; na console da AWS não se cria uma máquina virtual sem escolher a AMI, e no Terraform é igual. Na documentação o parâmetro `ami` aparece como "opcional", mas o texto explica que é **obrigatório a não ser que se passe um `launch_template`** — "tem uma pegadinha, tem que ler". Correção: adicionar o parâmetro `ami` no `main.tf`. Como o ambiente é simulado, poderia ser qualquer valor (ex.: "teste"); para parecer código real, ele pega na console da AWS o ID de uma AMI elegível ao nível gratuito (Ubuntu Server 26.04, segundo ele) e cola.

**Por que não rodar `init` de novo?** Porque nenhum provider novo foi adicionado; só seria necessário se, por exemplo, declarasse um provider do Google.

**Passo 5 — `terraform plan` (agora funcionando).** O plano mostra que o Terraform vai **criar um recurso do tipo `aws_instance`** chamado `minha_primeira_ec2`, listando tudo o que será criado. Valores como ARN, IP público etc. só são conhecidos **depois** da criação ("known after apply"). Mostra o tipo `t3.micro`, a região `us-east-1` (vinda do provider) e o nome `Hello World`. O resumo final: **1 a adicionar, 0 a alterar, 0 a destruir**.

**Passo 6 — `terraform apply`.** Mostra o plano novamente e pergunta se tem certeza ("Terraform vai fazer o que foi descrito acima; digite `yes` para aceitar"). Ao digitar `yes`, cria a instância — **cerca de 10 segundos** — e retorna o ID da instância.

**Verificação.** Rodando `aws ec2 describe-instances` de novo, agora retorna uma instância, com tipo T3, a **tag Name = Hello World**, a rede, o status, e a AMI com final `7D99`, a mesma colocada no código. "A nossa máquina foi provisionada na AWS usando Terraform." E "o céu é o limite": para provisionar 10 máquinas, declaram-se as 10 e **um `plan` + um `apply`** criam tudo automaticamente.

## Encerramento

Este é o poder do Terraform; o vídeo é só uma introdução. Para aprofundar, o apresentador recomenda o seu **Laboratório DevOps** (série de vídeos gratuita no YouTube, link na descrição), onde se monta uma infraestrutura completa com Terraform na AWS — primeiro de forma manual, depois automatizando, indo além com uma **pipeline** que faz tudo automaticamente. Pede inscrição no canal (14.000 inscritos), comentários e compartilhamento do vídeo.
