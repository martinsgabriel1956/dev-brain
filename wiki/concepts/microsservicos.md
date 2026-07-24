---
type: concept
title: "Microsserviços"
aliases: ["microsservicos", "microservices", "arquitetura de microsserviços", "decomposição por domínio"]
date_created: 2026-07-24
date_updated: 2026-07-24
source_count: 2
tags: [microsservicos, arquitetura, bounded-context, distributed-monolith, circuit-breaker, resiliencia]
skill: tech-mentor-backend
status: draft
---

# Microsserviços

Estilo arquitetural em que o sistema é dividido em serviços pequenos e independentes, cada um responsável por uma parte específica do negócio (ex.: pagamentos, usuário, notificações). Cada microsserviço roda isolado, tem seu próprio banco de dados se bem implementado, e pode ser desenvolvido, implantado e escalado independentemente dos demais. A comunicação entre serviços acontece via API (REST, RPC) ou mensageria assíncrona (filas, eventos).

Raízes em arquitetura orientada a serviços do início dos anos 2000; popularizou-se a partir de 2014 com o artigo de Martin Fowler e James Lewis, e virou hype ao longo da década seguinte — inclusive como efeito manada, com projetos adotando o estilo desde o início sem necessidade real de escala ou de times separados. Ver [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]].

## Decomposição Correta

O critério correto é decompor por **[[wiki/concepts/ddd-strategic|bounded context]]** (domínio de negócio), não por camada técnica. "Serviço de dados" + "Serviço de API" é um [[wiki/concepts/distributed-monolith|distributed monolith]] técnico disfarçado de microsserviços; "Orders Service" + "Payments Service" é decomposição real por domínio, com dados isolados e deploy independente.

## Custo-Benefício

**Benefícios:** escalabilidade seletiva (escalar só o serviço que precisa), times menores e autônomos trabalhando em paralelo, maior resiliência (falha de um serviço não derruba necessariamente o sistema inteiro).

**Custos:** complexidade operacional bem maior — consistência de dados distribuída, latência de rede entre serviços, observabilidade sobre múltiplos serviços, orquestração de deploy, e padrões de resiliência obrigatórios ([[wiki/concepts/circuit-breaker]], retry, timeout) para lidar com falhas parciais que não existiam num processo único.

Segundo `references/architecture-foundations.md` da skill `tech-mentor-backend`, monolito modular é o ponto de partida correto para ~90% dos casos — o caminho arquitetural saudável é monolito bem modularizado → extrair microsserviço quando há necessidade real (escala diferente, time separado, deploy independente), não o inverso.

## Microsserviços como Eixo de Aprendizado (Não Só Estilo Arquitetural)

[[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]] argumenta que o valor de estudar microsserviços vai além de saber implementá-los em produção: o estudo funciona como um eixo unificado que amarra, de forma organizada e com propósito definido, uma dezena de conceitos avançados e dispersos de arquitetura — [[wiki/concepts/circuit-breaker|circuit breaker/retry/timeout]], [[wiki/concepts/observabilidade]], [[wiki/concepts/saga-pattern|saga pattern/consistência eventual]], [[wiki/concepts/mensageria|comunicação assíncrona]], contratos de API versionados, e cultura de times autônomos. Cada um desses conceitos se aplica integralmente dentro de um monólito ou backend único — não são exclusividade de sistemas distribuídos. O relato de primeira mão do autor: usar o hype de microsserviços de 2014 como norte de estudo, vindo de uma bagagem de sistemas distribuídos, foi o que o trouxe de volta ao mercado depois de quase 10 anos preso a monólitos legados.

## Reaproveitando Peças Prontas do Ecossistema

Mesmo fora de uma arquitetura de microsserviços completa, dá para reaproveitar componentes prontos desse ecossistema — ex.: Keycloak como serviço de autenticação/autorização (incluindo federação), evitando reinvestir tempo em um requisito já resolvido por software livre estabelecido. Ver [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]].

## Key Sources

- [[wiki/sources/microsservicos]] — decomposição por bounded context, distributed monolith como anti-pattern, padrões de resiliência obrigatórios
- [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]] — microsserviços como guia/eixo de aprendizado de arquitetura, hype de 2014 em perspectiva histórica, relato pessoal de carreira, Keycloak como peça pronta reaproveitável
