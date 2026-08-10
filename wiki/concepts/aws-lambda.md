---
type: concept
title: "AWS Lambda"
aliases: ["Lambda", "AWS Lambda Function"]
date_created: 2026-08-04
date_updated: 2026-08-05
source_count: 2
tags: ["aws", "lambda", "serverless", "faas", "infra", "cloud"]
skill: tech-mentor-infra
status: stub
---

# AWS Lambda

Menor unidade de serverless da AWS (Function as a Service) — roda código sob demanda sem provisionamento explícito de servidor. Modelo de custo pay-per-use (por invocação/tempo de execução), em vez de pay-per-tempo-alocado como [[wiki/concepts/ec2]]. Em aplicações web, o padrão mais comum é "um endpoint, uma invocação de Lambda", geralmente atrás de um [[wiki/concepts/api-gateway]].

## Prós

- Custo relativamente baixo quando o caso de uso é adequado (tráfego irregular, event-driven).
- Escalabilidade praticamente infinita e rápida.

## Contras

1. **Escalabilidade infinita = exposição a custo infinito.** Sem limites configurados, um pico anômalo de tráfego (ex.: ataque) é executado (e cobrado) integralmente — ao contrário de um servidor tradicional, que tende a cair sob carga excessiva em vez de processar (e cobrar) tudo.
2. **Timeout.** Requests que demoram demais não retornam.
3. **Memória limitada por padrão**; aumentar RAM aumenta custo proporcionalmente.
4. **Cold start.** O primeiro request após um período de inatividade (a fonte cita ~15 minutos) é lento — a AWS precisa provisionar a infra antes do código ficar pronto para receber tráfego. Requests subsequentes são rápidos.
5. **Paga-se pelo tempo total de execução, incluindo espera por I/O** (chamadas a APIs externas, banco de dados) — não só pelo processamento de CPU efetivo. Num servidor tradicional, esse tempo de espera por I/O pode ser reaproveitado para atender outras requisições em paralelo; num Lambda isolado por invocação, esse tempo ocioso é pago integralmente como se fosse computação.

## Provisionamento via Infrastructure as Code

Numa demonstração com [[wiki/concepts/aws-cdk|AWS CDK]], um Lambda é instanciado como um construto TypeScript apontando para um handler local (ex.: `index.handler`); permissões (ex.: escrita num bucket S3) são concedidas via chamada de método em vez de policy JSON manual. A cada novo `cdk deploy`, o código publicado no Lambda é atualizado automaticamente a partir do código-fonte local — reforçando reprodutibilidade em vez de editar a função direto pelo console. Ver [[wiki/concepts/infraestrutura-como-codigo]].

## Relação com outros conceitos

- [[wiki/concepts/api-gateway]] — forma mais comum de rotear requests HTTP até Lambdas
- [[wiki/concepts/aws-fargate]] — outra forma serverless, unidade de container em vez de função
- [[wiki/concepts/ec2]] — contraste direto de modelo de custo (tempo alocado vs. tempo de execução)
- [[wiki/concepts/step-functions]] — coordena múltiplos Lambdas como máquina de estados
- [[wiki/concepts/aws-cdk]] — ferramenta de IaC usada para provisionar e atualizar Lambdas de forma reproduzível

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
- [[wiki/sources/infraestrutura-como-codigo-cdk-aws]] — deploy e atualização de um Lambda via AWS CDK, incluindo concessão de permissão de escrita num bucket S3
