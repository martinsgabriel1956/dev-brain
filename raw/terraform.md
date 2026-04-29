---
date: 2026-04-17
tags: [tech-mentor, infra, devops, terraform, iac, gitops, modules, state, terragrunt]
skill: tech-mentor-infra/references/devops
level: intermediário
---

# Terraform — IaC, State, Módulos, Terragrunt e Drift Detection

## Contexto

Terraform é a linguagem franca de Infrastructure as Code — declara recursos cloud em HCL (HashiCorp Configuration Language) e reconcilia a infraestrutura real com o estado desejado. O diferencial sobre scripts de shell ou AWS CloudFormation é o plan/apply workflow: você vê exatamente o que vai mudar antes de mudar. State é o coração e o ponto de risco central do Terraform.

---

## Estrutura de Projeto

```
infra/
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   └── terraform.tfvars
│   ├── staging/
│   └── production/
├── modules/
│   ├── vpc/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── ecs-service/
│   └── rds/
└── .terraform.lock.hcl    # lock de versões de providers
```

---

## Fundamentos HCL

```hcl
# terraform block — versões e providers
terraform {
  required_version = ">= 1.7.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"   # ~> = pessimistic: 5.x mas não 6.x
    }
  }

  # Backend remoto — state compartilhado e locking
  backend "s3" {
    bucket         = "mycompany-terraform-state"
    key            = "production/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"  # DynamoDB para distributed locking
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy   = "terraform"
      Project     = var.project_name
    }
  }
}

# Variables
variable "aws_region" {
  description = "AWS region para deploy"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Ambiente: dev, staging ou production"
  type        = string
  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "Environment deve ser dev, staging ou production."
  }
}

variable "db_config" {
  description = "Configuração do banco de dados"
  type = object({
    instance_class    = string
    allocated_storage = number
    multi_az          = bool
  })
  sensitive = false
}

# Locals — valores computados, sem prompt ao usuário
locals {
  name_prefix = "${var.project_name}-${var.environment}"
  common_tags = {
    Environment = var.environment
    Project     = var.project_name
  }
  is_production = var.environment == "production"
}

# Resources
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = merge(local.common_tags, {
    Name = "${local.name_prefix}-vpc"
  })
}

resource "aws_subnet" "private" {
  count             = 3
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.${count.index}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]

  tags = {
    Name = "${local.name_prefix}-private-${count.index + 1}"
    Type = "private"
  }
}

# Data sources — ler recursos existentes não gerenciados pelo Terraform
data "aws_availability_zones" "available" {
  state = "available"
}

data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

# Outputs — valores exportados para outros módulos ou usuários
output "vpc_id" {
  description = "ID da VPC criada"
  value       = aws_vpc.main.id
}

output "private_subnet_ids" {
  description = "IDs das subnets privadas"
  value       = aws_subnet.private[*].id
}
```

---

## Módulos — Reutilização de Infraestrutura

```hcl
# modules/ecs-service/variables.tf
variable "service_name" { type = string }
variable "container_image" { type = string }
variable "container_port" { type = number; default = 3000 }
variable "desired_count" { type = number; default = 2 }
variable "cpu" { type = number; default = 256 }
variable "memory" { type = number; default = 512 }
variable "vpc_id" { type = string }
variable "subnet_ids" { type = list(string) }
variable "environment_variables" {
  type    = map(string)
  default = {}
}

# modules/ecs-service/main.tf
resource "aws_ecs_task_definition" "this" {
  family                   = var.service_name
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = var.cpu
  memory                   = var.memory
  execution_role_arn       = aws_iam_role.ecs_execution.arn
  task_role_arn            = aws_iam_role.ecs_task.arn

  container_definitions = jsonencode([{
    name  = var.service_name
    image = var.container_image
    portMappings = [{
      containerPort = var.container_port
      protocol      = "tcp"
    }]
    environment = [
      for k, v in var.environment_variables : { name = k, value = v }
    ]
    logConfiguration = {
      logDriver = "awslogs"
      options = {
        "awslogs-group"         = "/ecs/${var.service_name}"
        "awslogs-region"        = data.aws_region.current.name
        "awslogs-stream-prefix" = "ecs"
      }
    }
  }])
}

resource "aws_ecs_service" "this" {
  name            = var.service_name
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.this.arn
  desired_count   = var.desired_count
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = var.subnet_ids
    security_groups  = [aws_security_group.service.id]
    assign_public_ip = false
  }

  deployment_circuit_breaker {
    enable   = true    # rollback automático se deploy falhar
    rollback = true
  }

  lifecycle {
    ignore_changes = [desired_count]  # permitir autoscaling externo sem drift
  }
}

# modules/ecs-service/outputs.tf
output "service_arn" { value = aws_ecs_service.this.id }
output "task_definition_arn" { value = aws_ecs_task_definition.this.arn }

# Usar o módulo em environments/production/main.tf
module "order_service" {
  source = "../../modules/ecs-service"

  service_name    = "order-service"
  container_image = "123456789.dkr.ecr.us-east-1.amazonaws.com/order-service:${var.image_tag}"
  desired_count   = 3
  cpu             = 512
  memory          = 1024
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_subnet_ids

  environment_variables = {
    NODE_ENV     = "production"
    LOG_LEVEL    = "info"
    DATABASE_URL = aws_ssm_parameter.db_url.value
  }
}
```

---

## State — O Coração do Terraform

```bash
# State remoto — NUNCA usar state local em produção
# Configurar backend S3 + DynamoDB para locking

# Criar a infraestrutura de state manualmente (chicken-and-egg problem)
aws s3 mb s3://mycompany-terraform-state --region us-east-1
aws s3api put-bucket-versioning \
  --bucket mycompany-terraform-state \
  --versioning-configuration Status=Enabled

aws dynamodb create-table \
  --table-name terraform-state-lock \
  --attribute-definitions AttributeName=LockID,AttributeType=S \
  --key-schema AttributeName=LockID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST

# Comandos de state management
terraform state list                              # listar todos os resources no state
terraform state show aws_ecs_service.order        # ver detalhes de um resource
terraform state mv aws_instance.old aws_instance.new  # renomear sem recriar
terraform state rm aws_ecs_service.legacy         # remover do state (não destroi o recurso real)
terraform import aws_ecs_service.existing "cluster/service"  # importar recurso existente

# Drift detection — infraestrutura mudou fora do Terraform?
terraform plan -refresh-only                      # só refresh, não calcula mudanças de config
terraform apply -refresh-only                     # atualizar state com o estado real atual
```

---

## Fluxo Plan / Apply / Destroy

```bash
# Inicializar — baixar providers e configurar backend
terraform init

# Validar HCL sem conectar ao provider
terraform validate

# Ver o que vai mudar
terraform plan -out=tfplan                        # salvar o plan
terraform plan -target=module.order_service       # plan específico
terraform plan -var="image_tag=v1.2.3"           # override de variável

# Aplicar (com o plan salvo — garante que apply é exatamente o plan aprovado)
terraform apply tfplan

# Destruir (CUIDADO — irreversível)
terraform plan -destroy                           # ver o que será destruído
terraform destroy -target=aws_ecs_service.legacy  # destruir recurso específico

# Variáveis — ordem de precedência (maior prioridade primeiro)
# 1. -var="key=value" na linha de comando
# 2. terraform.tfvars (auto-carregado)
# 3. *.auto.tfvars (auto-carregados em ordem alfabética)
# 4. Variáveis de ambiente TF_VAR_name
# 5. default no bloco variable
```

---

## Terragrunt — DRY para Múltiplos Ambientes

```hcl
# Estrutura com Terragrunt:
# environments/
# ├── terragrunt.hcl          (root — configs compartilhadas)
# ├── dev/
# │   ├── terragrunt.hcl
# │   └── order-service/
# │       └── terragrunt.hcl
# └── production/
#     └── order-service/
#         └── terragrunt.hcl

# environments/terragrunt.hcl — configuração raiz
remote_state {
  backend = "s3"
  generate = {
    path      = "backend.tf"
    if_exists = "overwrite"
  }
  config = {
    bucket         = "mycompany-terraform-state"
    key            = "${path_relative_to_include()}/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}

# Inputs compartilhados para todos os módulos
inputs = {
  aws_region   = "us-east-1"
  project_name = "mycompany"
}

# environments/production/terragrunt.hcl
include "root" {
  path = find_in_parent_folders()
}

inputs = {
  environment = "production"
}

# environments/production/order-service/terragrunt.hcl
include "root" {
  path = find_in_parent_folders()
}

terraform {
  source = "../../../modules//ecs-service"
}

# Dependência explícita — aguarda VPC estar criada
dependency "vpc" {
  config_path = "../vpc"
  mock_outputs = {
    vpc_id          = "vpc-mock"
    private_subnet_ids = ["subnet-mock-1", "subnet-mock-2"]
  }
}

inputs = {
  service_name    = "order-service"
  container_image = "123456.dkr.ecr.us-east-1.amazonaws.com/order-service:${get_env("IMAGE_TAG")}"
  vpc_id          = dependency.vpc.outputs.vpc_id
  subnet_ids      = dependency.vpc.outputs.private_subnet_ids
}
```

---

## Trade-offs

| Ferramenta | Vantagem | Limitação |
|---|---|---|
| **Terraform** | Multi-cloud, ecossistema maduro | State lock, HCL verboso para lógica |
| **Terragrunt** | DRY para multi-env, dependency management | Camada adicional, curva de aprendizado |
| **Pulumi** | IaC em TypeScript/Python (loops, condicionais reais) | Menor ecossistema que Terraform |
| **Crossplane** | K8s-native, GitOps nativo | Complexidade operacional alta |
| **CDK** | IaC em linguagem de programação, abstração alta | Lock-in no CloudFormation/AWS |

## Quando Usar / Quando Evitar

**State remoto sempre:** state local é apenas para aprendizado. Em equipe, state local causa conflitos imediatamente.

**lifecycle.ignore_changes:** use para recursos gerenciados por autoscaling ou outros sistemas fora do Terraform (desired_count de ECS, por exemplo).

**Terraform para mudanças raras de infra, não para config frequente:** deployr uma nova versão de container via Terraform a cada commit é anti-pattern. Use variáveis de ambiente ou parâmetros, e CI/CD para o deploy. Terraform para a infraestrutura, não para o código da aplicação.

**Módulos versionados:** em monorepos, versione os módulos com Git tags para evitar que mudanças em módulos quebrem todos os ambientes simultaneamente.

## Conceitos Relacionados

[[argocd]] · [[github-actions-avancado]] · [[kubernetes-core]] · [[finops]] · [[secrets-management]]

---
*Fonte: tech-mentor skill · tech-mentor-infra · 2026-04-17*
