---
type: concept
title: "AWS Lambda"
aliases: ["Lambda", "AWS Lambda Function"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
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

## Relação com outros conceitos

- [[wiki/concepts/api-gateway]] — forma mais comum de rotear requests HTTP até Lambdas
- [[wiki/concepts/aws-fargate]] — outra forma serverless, unidade de container em vez de função
- [[wiki/concepts/ec2]] — contraste direto de modelo de custo (tempo alocado vs. tempo de execução)
- [[wiki/concepts/step-functions]] — coordena múltiplos Lambdas como máquina de estados

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
