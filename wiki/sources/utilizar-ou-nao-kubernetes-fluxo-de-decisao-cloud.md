---
type: source
title: "Utilizar ou Não Kubernetes: Como Decidir Onde Rodar Sua Aplicação na Nuvem"
aliases: ["utilizar ou não kubernetes", "kubernetes não é a única opção", "fluxo de decisão de compute azure", "fabrício kubernetes ou não"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/utilizar-ou-nao-kubernetes-fluxo-de-decisao-cloud.md
source_url: ""
author: "Fabrício (sobrenome não aparece na transcrição; identificado por inferência como Fabrício Veronez)"
date_published: ""
date_ingested: 2026-11-03
source_count: 0
tags: [kubernetes, docker, conteineres, cloud, azure, aws, gcp, vendor-lock-in, decisao-arquitetural, tech-mentor-infra]
skill: tech-mentor-infra
status: stable
---

# Utilizar ou Não Kubernetes: Como Decidir Onde Rodar Sua Aplicação na Nuvem

## TL;DR

[[wiki/entities/fabricio-veronez|Fabrício]] responde a quem acha que precisa de [[wiki/concepts/kubernetes]] para rodar em nuvem de forma escalável. A resposta dele: **Kubernetes é opcional; [[wiki/concepts/conteinerizacao|contêineres]] quase não são.**

Para mostrar isso, ele percorre o fluxograma de escolha de compute da documentação do Azure ([[wiki/concepts/arvore-de-decisao-de-computacao-em-nuvem]]). O caminho termina em serviços que rodam contêiner sem exigir Kubernetes, como o Azure Container Apps ([[wiki/concepts/conteineres-gerenciados-sem-kubernetes]]). Depois, um de-para leva a escolha para AWS e Google. Por fim, ele apresenta os quatro critérios que usa para decidir ([[wiki/concepts/criterios-de-adocao-de-servico-cloud]]): requisitos do projeto, adoção de mercado, conhecimento da equipe e custo.

O preço de sair do Kubernetes é [[wiki/concepts/vendor-lock-in-cloud|lock-in]], atenuado pela portabilidade do contêiner.

**Datado:** dois serviços citados como opção mudaram de status. O Azure Spring Apps está em aposentadoria e o AWS App Runner fechou para novos clientes. Ver "Verificação externa".

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| Kubernetes é orquestrador: escala horizontal por réplicas, balanceamento de carga, gerenciamento de configuração, todos os componentes num único lugar | Definição do autor; consistente com [[wiki/sources/kubernetes-core]] | Alta |
| Aprender contêineres e Docker é pré-requisito para aprender Kubernetes | Opinião do autor, baseada na estrutura do curso dele (1 módulo de Docker, 2 de Kubernetes). Há conflito de interesse leve: o vídeo vende esse curso | Alta como ordem de estudo |
| Docker serve para monolito; dizer que não serve é "balela" | Experiência do autor em projetos; nenhum caso citado | Alta (contêiner não impõe arquitetura) |
| Docker pode ir para produção sem Kubernetes | Ver [[wiki/concepts/conteineres-gerenciados-sem-kubernetes]]; `[skill: tech-mentor-infra]` confirma com Fargate, Cloud Run, Container Apps e Swarm | Alta |
| Contêineres facilitam setup de desenvolvimento e migração entre ambientes | Afirmação do autor (baixar o código, executar um comando) | Alta |
| Decisão começa em migrar vs. criar algo novo; migrar legado dá mais trabalho | `[external]` A página da Microsoft confirma a divisão migrar vs. construir | Alta |
| Aplicação não conteinerizada reduz bastante o leque de opções | Leitura do autor sobre o fluxo | Média-alta |
| VM é o ambiente mais parecido com data center; dá controle total, mas você gerencia SO e runtime "no braço" | Afirmação do autor; só o hardware sai da sua responsabilidade | Alta |
| Azure Container Instances é difícil de escalar | `[external]` Confirmado: autoscaling "Not supported", sem load balancer embutido, sem orquestração completa. O autor diz "um único contêiner", o que é simplificação: a unidade é o *container group* | Alta |
| Service Fabric tem pouca adoção no mercado | Percepção do autor, que admite nunca ter usado. `[external]` A Microsoft hoje o lista apenas em "Specialty workloads", o que é compatível, mas não mede adoção | Média |
| Todos os grandes provedores têm serviço de Kubernetes e serviço de contêiner gerenciado | Afirmação do autor; a tabela não aparece na transcrição | Alta |
| Não existe serviço OpenShift no Google | **Incorreto hoje.** `[external]` A Red Hat oferece OpenShift Dedicated no Google Cloud (lançado em 2016). O autor só disse que não achou e pediu ajuda | Baixa |
| Em Kubernetes "não há" lock-in, porque é padrão entre provedores | **Exagero.** O próprio autor fala em portabilidade "mais fácil". Inferência: a API é comum, mas identidade, ingress, storage e add-ons continuam específicos de cada provedor | Média |
| Fora do Kubernetes, a migração é menos transparente, mas "não vai ser um mistério" se você usa contêineres | Argumento do autor | Média-alta |
| Projeto sem alta escalabilidade, que tolera downtime, ou que precisa de custo inicial baixo talvez não precise de Kubernetes | Critério do autor; converge com [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]] (VPS sem Kubernetes) | Alta |

## O caminho pelo fluxograma

Conforme narrado pelo autor. A versão atual do diagrama pode diferir.

**Cenário ruim** (migração, sem contêiner):

1. Já está otimizada para cloud? Se sim, volta ao fluxo de aplicação nova.
2. Lift and shift? ([[wiki/concepts/lift-and-shift]])
3. Está conteinerizada? Não.
4. É produto de prateleira? Se sim, VM.
5. Se não: Azure Spring Apps ou Azure App Service.

**Caminho feliz** (aplicação web nova):

| Pergunta | Se sim | O autor segue porque |
|---|---|---|
| Controle total? | VM | não quer gerenciar SO e runtime |
| Batch? | Azure Batch | é web |
| Spring Boot? | Azure Spring Apps | hipótese de não usar |
| Evento com processamento curto? | Azure Functions | tem regras de negócio e precisa escalar |
| Plataforma gerenciada para web? | Azure App Service | quer contêineres (o App Service também suporta) |
| Ambiente simples, sem orquestração? | Azure Container Instances | difícil de escalar |
| Service Fabric ou .NET Framework antigo? | Azure Service Fabric | pouca adoção |
| OpenShift? | Azure Red Hat OpenShift | não é o caso |
| Quer acessar as APIs do Kubernetes? | AKS | ainda não conhece Kubernetes |
| Nenhuma das anteriores | **Azure Container Apps** | fim do caminho |

Na pergunta do Container Instances, a transcrição diz literalmente "totalmente gerenciado, totalmente orquestrado". O texto da Microsoft não confirma essa redação (a pergunta exata fica na imagem), então a tabela usa uma paráfrase.

## De-para citado no vídeo

| Azure | AWS | Google |
|---|---|---|
| App Service | Elastic Beanstalk, App Runner | App Engine |
| Máquina virtual | EC2 | Compute Engine |

O autor menciona também comparativos para Spring Apps, Kubernetes e contêineres gerenciados, mas a transcrição não nomeia esses serviços. A tabela ficou só na tela e na descrição do vídeo.

## Verificação externa

`[external]` Consultado em 2026-11-03:

- **Fluxograma:** é a página [Choose an Azure compute service](https://learn.microsoft.com/azure/architecture/guide/technology-choices/compute-decision-tree). O diagrama é uma imagem e não foi inspecionado: só o texto e o texto alternativo foram lidos. A redação exata das perguntas não foi conferida.
- **Azure Spring Apps:** não aparece mais nessa página. Não aceita novos clientes desde 17/mar/2025 e será aposentado em [31/mar/2028](https://learn.microsoft.com/en-my/azure/spring-apps/basic-standard/retirement-announcement). A Microsoft recomenda migrar para Azure Container Apps.
- **AWS App Runner:** [fechado para novos clientes desde 30/abr/2026](https://docs.aws.amazon.com/ja_jp/apprunner/latest/dg/apprunner-availability-change.html), segundo a busca (a leitura direta da página falhou). Quem já é cliente continua usando, sem novos recursos previstos. A AWS sugere ECS Express Mode.
- **OpenShift no Google:** [OpenShift Dedicated no Google Cloud](https://www.redhat.com/en/technologies/cloud-computing/openshift/dedicated), oferta atual da Red Hat.
- **Autor:** [Fabricio Veronez](https://www.docker.com/captains/fabricio-veronez/) é Docker Captain e dono da Formação DevOps Pro. A identificação é uma inferência a partir do primeiro nome e do curso.

## Entities

[[wiki/entities/fabricio-veronez]] · [[wiki/entities/microsoft]] · [[wiki/entities/amazon-web-services]] · [[wiki/entities/google-cloud-platform]]

## Concepts

[[wiki/concepts/kubernetes]] · [[wiki/concepts/conteinerizacao]] · [[wiki/concepts/conteineres-gerenciados-sem-kubernetes]] · [[wiki/concepts/arvore-de-decisao-de-computacao-em-nuvem]] · [[wiki/concepts/criterios-de-adocao-de-servico-cloud]] · [[wiki/concepts/lift-and-shift]] · [[wiki/concepts/vendor-lock-in-cloud]] · [[wiki/concepts/virtualizacao]] · [[wiki/concepts/ec2]] · [[wiki/concepts/ecs]] · [[wiki/concepts/aws-fargate]] · [[wiki/concepts/elastic-beanstalk]] · [[wiki/concepts/escalabilidade-horizontal]] · [[wiki/concepts/monolito]] · [[wiki/concepts/escolha-de-stack]] · [[wiki/concepts/avaliar-hype-tecnologico]]

## Open Questions

- O diagrama atual da Microsoft ainda leva a Container Apps quando se responde "não" às APIs do Kubernetes? O texto da página não permite confirmar.
- Qual é o tamanho real do lock-in em Kubernetes gerenciado, comparado a Container Apps ou ECS? A fonte não quantifica.
- A partir de que porte Kubernetes passa a compensar? O autor dá critérios qualitativos, sem números.

## Conexão com outras fontes

Complementa [[wiki/sources/kubernetes-core]] (como funciona) com a pergunta anterior: se é preciso usar. Na AWS, [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] faz a mesma comparação de simplicidade entre ECS e EKS.

[skill: tech-mentor-infra] Calibrado com `containers/serverless-containers.md`, `containers/docker-runtime.md` (produção sem K8s) e `cloud/cloud-agnostic.md` (7Rs).
