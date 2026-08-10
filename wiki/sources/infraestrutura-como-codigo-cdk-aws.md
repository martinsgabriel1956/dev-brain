---
type: source
title: "Infrastructure as Code — Por Que Parar de Clicar no Console da AWS (com Demo em AWS CDK)"
aliases: ["iac aws cdk", "infra as code demo cdk", "esquema illuminati" ]
date_created: 2026-08-05
date_updated: 2026-08-05
source_count: 0
tags: [tech-mentor-infra, iac, aws, cdk, cloudformation, terraform, devops, lambda, api-gateway]
skill: tech-mentor-infra
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/infraestrutura-como-codigo-cdk-aws.md
source_url:
author: "desconhecido no áudio; forte coincidência de padrão com [[wiki/entities/augusto-galego]] (curso próprio de System Design cobrindo API Gateway/Lambda/banco de dados, reembolso integral sem questionamento em um mês) — não confirmado por nome"
date_published:
date_ingested: 2026-08-05
---

# Infrastructure as Code — Por Que Parar de Clicar no Console da AWS (com Demo em AWS CDK)

## TL;DR

Vídeo argumentando que configurar infraestrutura manualmente pelo console da AWS (ou de qualquer cloud) não é reproduzível nem documentado, e que empresas maduras deveriam adotar [[wiki/concepts/infraestrutura-como-codigo|Infrastructure as Code]] (IaC) — tratar infraestrutura como código versionado, revisável e reproduzível. Apresenta um panorama de ferramentas de IaC (Terraform/OpenTofu, AWS CloudFormation, [[wiki/concepts/aws-cdk|AWS CDK]], Pulumi, Ansible, Bicep, e — de forma mais ampla — Kubernetes) e demonstra na prática, com [[wiki/concepts/aws-cdk|AWS CDK]] em TypeScript, o deploy de uma stack simples (um bucket S3 e uma função [[wiki/concepts/aws-lambda|Lambda]] com permissão de escrita no bucket), incluindo `cdk deploy`, verificação no console AWS e `cdk destroy`. Fecha com pitch do curso pago de System Design do autor.

## Key Claims

1. **Configuração manual via console não é reproduzível nem documentada.** Alterar uma configuração de banco de dados (ex.: RDS/Aurora) direto no console não deixa rastro visível para o time — pode ser feita em staging e esquecida em produção (ou vice-versa) sem que ninguém perceba.
   **Confiança:** alta (afirmação de razoabilidade prática, consistente com a literatura de IaC referenciada pela skill `tech-mentor-infra`).

2. **IaC = tratar infraestrutura como código de mesma categoria que código de aplicação** — com versionamento, revisão, auditabilidade, replicabilidade e automação como os quatro benefícios centrais citados.
   **Evidência:** contraste explícito entre criar recursos clicando no console vs. commitar um arquivo de configuração no GitHub, revisável por pull request.
   **Confiança:** alta.

3. **Caminho de maturidade recomendado é começar manual, migrar para IaC.** Para aprender qualquer provedor (AWS, GCP, Azure), o autor recomenda começar manualmente seguindo documentação/tutoriais oficiais; para um projeto robusto/empresa madura, IaC é o padrão esperado.
   **Confiança:** média-alta — é uma recomendação pedagógica pessoal do autor, não uma citação de fonte externa.

4. **Terraform é citado como a ferramenta de IaC mais popular**, tendo fechado sua licença open-source em algum momento, o que gerou o fork gratuito OpenTofu.
   **Confiança:** alta — consistente com `references/terraform.md` da skill `tech-mentor-infra`, que documenta o OpenTofu como fork surgido após a mudança para BSL em 2023.
   [skill: tech-mentor-infra]

5. **AWS CDK escreve TypeScript e sintetiza para CloudFormation** — o CDK não é uma alternativa ao CloudFormation, é uma camada de abstração sobre ele; o artefato de fato aplicado na AWS é o CloudFormation gerado.
   **Evidência:** demonstração ao vivo — `npx cdk deploy` sintetiza a stack, lista as mudanças, aplica; internamente gera um template de CloudFormation descrito como difícil de ler diretamente.
   **Confiança:** alta.

6. **TypeScript de propósito geral permite lógica condicional real na definição de infraestrutura** (ex.: `environment` dev vs. prod alterando política de backup do banco), algo que uma DSL puramente declarativa (YAML/HCL) expressa com mais dificuldade.
   **Evidência:** exemplo pessoal do autor — banco de produção com backups mais resilientes que o de dev numa empresa anterior, configurado dinamicamente via essa lógica condicional.
   **Confiança:** média — anedota de uma experiência profissional específica, não uma comparação sistemática de linguagens declarativas vs. imperativas para IaC.

7. **Escolha de ferramenta de IaC depende do escopo: só-AWS favorece CDK/CloudFormation; multi-cloud favorece Terraform/OpenTofu.**
   **Confiança:** alta — consistente com a árvore de decisão explícita em `references/terraform.md` da skill (`"Só AWS → CDK ou CloudFormation pode ser mais natural"`). [skill: tech-mentor-infra]

8. **Erro comum: região AWS padrão mal configurada.** Na própria demonstração, o autor esperava que o recurso fosse deployado em US East 1 (Virginia) e ele foi parar na Irlanda — o autor reconhece que isso "já aconteceu muitas vezes" com ele.
   **Confiança:** alta (observado ao vivo na fonte).

## Entidades Mencionadas

- [[wiki/entities/amazon-web-services]] — provedor cloud usado em toda a demonstração (console, CDK, Lambda, S3, CloudFormation).
- [[wiki/entities/augusto-galego]] — autoria inferida com evidência de padrão de conteúdo (curso próprio de System Design cobrindo os mesmos tópicos citados no fechamento — API Gateway, Lambda, network, banco de dados —, política de reembolso integral em um mês sem questionamento), não confirmada por nome no áudio.

## Conceitos Tocados

- [[wiki/concepts/infraestrutura-como-codigo]] *(novo)*
- [[wiki/concepts/aws-cdk]] *(novo)*
- [[wiki/concepts/aws-cloudformation]] *(novo)*
- [[wiki/concepts/aws-lambda]]
- [[wiki/concepts/api-gateway]]
- [[wiki/concepts/postgresql]]
- Terraform/OpenTofu — ver [[wiki/sources/terraform]]

## Open Questions

- Autoria não confirmada por nome no áudio. A inferência para [[wiki/entities/augusto-galego]] se apoia no conteúdo do fechamento (curso próprio de System Design cobrindo exatamente API Gateway, Lambda, network e banco de dados, com a mesma política de reembolso integral em um mês sem questionamento já documentada na entidade) — mas o sponsor deste vídeo (AmaX, infraestrutura de pagamentos) é diferente dos sponsors já associados a essa entidade em fontes anteriores (HostGator/Hostinger), então a evidência é de conteúdo, não de padrão de patrocínio. Se uma fonte futura confirmar (ou refutar) o nome, esta página e a entidade precisam ser corrigidas.
- A fonte não detalha como o CDK decide nomes de recursos por padrão, nem como lidar com múltiplas contas/ambientes AWS de forma mais estruturada do que o `if (environment === ...)` mostrado — fica como lacuna para uma fonte futura mais aprofundada de CDK.
- Não fica claro no vídeo qual mecanismo exato causou o deploy ter ido para a região errada (configuração de perfil da AWS CLI? variável de ambiente? default do CDK?) — tratado como observação anedótica, não como causa raiz explicada.

## Raw Quotes

> "Quando a gente entra no console da AWS e a gente manipula o console da AWS manualmente, a gente vai tá fazendo algo que talvez não seja facilmente reproduzível, e com certeza não vai tá bem documentado."

> "Infrastructure as Code é tratar infraestrutura da mesma maneira que a gente trata o código — como um cidadão de mesma categoria, com controle de versionamento, documentação clara e de maneira reproduzível e revisável."

> "Toda vez que eu altero esse código aqui e eu rodo o meu CDK de novo, ele vai atualizando o código que tá lá no CDK, lá na AWS — e a gente consegue também lidar com as permissões."

> "Infrastructure as Code não é o futuro, é o presente — e se sua empresa não faz isso, ela tá presa no passado."
