---
type: concept
title: "AWS CDK"
aliases: ["CDK", "Cloud Development Kit"]
date_created: 2026-08-05
date_updated: 2026-08-05
source_count: 1
tags: ["aws", "cdk", "iac", "typescript", "cloudformation", "infra"]
skill: tech-mentor-infra
status: stub
---

# AWS CDK (Cloud Development Kit)

Ferramenta de [[wiki/concepts/infraestrutura-como-codigo|Infrastructure as Code]] da AWS que permite descrever infraestrutura em uma linguagem de propósito geral (TypeScript, no exemplo demonstrado — mas também suporta outras linguagens) em vez de uma DSL declarativa pura. O CDK interpreta esse código e sintetiza um template de [[wiki/concepts/aws-cloudformation|CloudFormation]], que é o que efetivamente é aplicado na conta AWS.

## Modelo mental

- Um `App` (aplicativo CDK) contém uma ou mais `Stack`s.
- Dentro de uma stack, construtos (ex.: `Bucket`, uma função Lambda) são instanciados como classes/objetos TypeScript.
- Como é código de propósito geral, é possível usar lógica condicional real (`if (environment === 'dev') {...}`) para variar configuração entre ambientes a partir do mesmo código-fonte — ex.: banco de produção com backups mais resilientes que o de dev.
- Permissões entre recursos (ex.: dar a um Lambda permissão de escrita num bucket S3) são expressas como chamadas de método, não como blocos de policy manual.

## Fluxo de trabalho

1. `npx cdk deploy` — sintetiza a stack, mostra a lista de mudanças que serão aplicadas (criação/atualização de recursos) para aprovação, e então aplica de fato via CloudFormation.
2. `npx cdk destroy` — destrói todos os recursos criados pela stack.
3. Toda vez que o código-fonte de um Lambda muda e o deploy roda de novo, o código publicado na AWS é atualizado — sempre reproduzindo exatamente a mesma stack a partir do mesmo código.

## Risco / cuidado prático citado

É tecnicamente possível usar qualquer lógica arbitrária dentro do código do CDK (ex.: bater numa API externa para decidir dinamicamente o nome de um recurso) — mas isso compromete a reprodutibilidade, que é justamente o benefício central de IaC. A recomendação é manter a definição de infraestrutura o mais determinística possível.

Região padrão mal configurada é um erro comum e fácil de cometer (recurso deployado numa região diferente da esperada) — vale sempre conferir explicitamente a região configurada antes do deploy.

## Relação com outros conceitos

- [[wiki/concepts/infraestrutura-como-codigo]] — categoria geral à qual o CDK pertence
- [[wiki/concepts/aws-cloudformation]] — formato para o qual o CDK compila/sintetiza
- [[wiki/concepts/aws-lambda]] — recurso provisionado no exemplo demonstrado (função + permissões + código-fonte)

## Key Sources

- [[wiki/sources/infraestrutura-como-codigo-cdk-aws]]
