---
type: source
title: "Comunicação Assíncrona — Arquiteturas Distribuídas (Bernardo Lobato)"
aliases: ["comunicacao assincrona bernardo lobato", "async vs sync bernardo lobato", "comunicação assíncrona arquiteturas distribuídas"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 0
tags: [comunicacao-assincrona, comunicacao-sincrona, mensageria, polling, webhook, consistencia-eventual, acoplamento, resiliencia, arquiteturas-distribuidas]
skill: tech-mentor-backend
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato.md"
source_url: ""
author: "Bernardo Lobato"
date_published: ""
date_ingested: "2026-09-30"
---

## TL;DR

Vídeo introdutório de [[wiki/entities/bernardo-lobato]] que prepara o terreno para a série de arquiteturas distribuídas. Contrasta [[wiki/concepts/comunicacao-sincrona]] (chamada bloqueante, resposta imediata, acoplamento forte, baixa resiliência — exemplo: serviço externo de autenticação/autorização devolvendo JWT) com [[wiki/concepts/comunicacao-assincrona]] (emissor não espera a resposta; receptor processa em background; acoplamento fraco). Lista três formas de implementá-la: **polling por ID de operação** ([[wiki/concepts/async-request-reply]]), **[[wiki/concepts/webhook]]/callback** e **[[wiki/concepts/mensageria]]** por broker (Kafka, RabbitMQ). Exemplo central: serviço de Pedidos publica um evento "pedido criado" que Estoque e Faturamento consomem de forma independente — ganho em escalabilidade, desempenho, autonomia de times e absorção de picos (Black Friday). Reconhece que a complexidade é maior e nomeia três desafios: **debug** (rastreabilidade → [[wiki/concepts/observabilidade]]), **garantia de entrega** ([[wiki/concepts/garantia-de-entrega]]) e **[[wiki/concepts/eventual-consistency|consistência eventual]]**. Avisa contra "emular síncrono sobre assíncrono" e contra adotar por moda; aponta [[wiki/concepts/cqrs]], [[wiki/concepts/event-sourcing]], [[wiki/concepts/event-driven-architecture]] e [[wiki/concepts/microsservicos]] como os próximos passos.

---

## Reivindicações Principais

**Claim:** Comunicação síncrona bloqueia o fluxo do chamador até a resposta, é simples e intuitiva, mas esconde dois problemas: alto acoplamento (mudança em um lado afeta o outro) e baixa resiliência (se o serviço chamado cai ou fica lento, o sistema todo pode ficar inviável).
**Evidência:** Exemplo de um serviço externo de autenticação/autorização consultado a cada requisição, devolvendo JWT; sem medição, argumento do autor.
**Confiança:** Alta — coincide com a definição de [[wiki/concepts/temporal-coupling]] (A precisa que B esteja disponível *agora*) [skill: tech-mentor-backend, `references/architecture-resilience-patterns.md`]. Nota de inferência: a dependência pode ser atenuada sem trocar o modelo (timeout, [[wiki/concepts/circuit-breaker]], cache de chaves públicas para validar JWT localmente); o vídeo não discute isso e adia o tratamento justo da síncrona para vídeo futuro.

**Claim:** Na assíncrona, o emissor não espera a resposta; o receptor processa em background e o emissor é notificado depois, ou consulta o status periodicamente. Analogia: áudio no grupo de WhatsApp.
**Evidência:** Definição do autor.
**Confiança:** Alta — definição padrão.

**Claim:** Síncrona: resposta imediata e acoplamento forte; assíncrona: resposta não imediata e acoplamento fraco (uma API lenta não compromete necessariamente o resto do sistema).
**Evidência:** Tabela comparativa do vídeo (exemplos: REST entre microsserviços vs. mensageria via broker).
**Confiança:** Média-alta — "acoplamento fraco" é verdadeiro no eixo **temporal**; acoplamento de contrato (schema da mensagem) continua existindo ([external]/[skill] [[wiki/concepts/temporal-coupling]] distingue temporal de espacial). O vídeo não faz essa distinção.

**Claim:** Assíncrono não exige broker. Duas alternativas simples: (1) devolver um ID da operação e o cliente fazer polling de um endpoint de status/resultado; (2) devolver só um OK e o processador chamar um webhook/callback cadastrado no solicitante. Ambas servem quando não se controla todos os sistemas (ex.: API externa em produção).
**Evidência:** Descrição do autor, sem código.
**Confiança:** Alta — corresponde ao padrão request-reply assíncrono (`202 Accepted` + `jobId`) [skill: tech-mentor-backend, `references/architecture-eda-patterns.md`]; ver [[wiki/concepts/async-request-reply]] e [[wiki/concepts/webhook]].

**Claim:** Publicar um evento "pedido criado" em fila/tópico, consumido independentemente por Estoque e Faturamento, evita dependência de resposta imediata e melhora escalabilidade, desempenho, autonomia e manutenibilidade (times menores focados num serviço).
**Evidência:** Exemplo de e-commerce simplificado, sem código ou números.
**Confiança:** Média-alta — padrão clássico de pub/sub/EDA ([[wiki/concepts/event-driven-architecture]], [[wiki/concepts/mensageria]]). Não discute o risco de a publicação não ser atômica com o commit no banco (ver [[wiki/concepts/outbox-pattern]]) nem idempotência dos consumidores ([[wiki/concepts/idempotencia]]).

**Claim:** Tolerância a falhas e picos: se um consumidor cai, ao voltar relê as mensagens perdidas e continua "como se nada tivesse acontecido"; num pico (Black Friday) não é preciso escalar a solução inteira, só os serviços sob pressão.
**Evidência:** Raciocínio do autor.
**Confiança:** Média — verdadeiro quando o broker retém mensagens de forma durável e o consumidor é idempotente; "como se nada tivesse acontecido" omite reprocessamento e duplicatas. A absorção de pico é o papel de [[wiki/concepts/buffer]] (a fila desacopla a velocidade de produção da de consumo); a fila tem limite físico (ver [[wiki/sources/back-pressure-producer-consumer-filas-bounded-admission-control]]).

**Claim:** Não se deve emular comunicação síncrona sobre o modelo assíncrono; é preciso aprender as boas práticas do modelo e adotá-lo por necessidade, não "por usar". A complexidade é maior e exige capacitação do time.
**Evidência:** Observação do autor sobre times vindos de REST/HTTP.
**Confiança:** Média — experiência declarada, sem caso documentado. Converge com [[wiki/sources/microsservicos-historia-soa-esb-bernardo-lobato]] (mesmo autor: capacitação do time como desafio central pouco discutido).

**Claim:** Três desafios: (1) debug sem passo a passo linear, mitigado por rastreabilidade/observabilidade; (2) garantia de entrega — muitos brokers não vêm configurados por padrão para garantir entrega a todos os receptores; (3) consistência eventual — leituras podem devolver dado desatualizado entre serviços; isso precisa ser "vendido" à liderança/cliente.
**Evidência:** Lista do autor, com exemplo pedido/pagamento para a consistência.
**Confiança:** Média-alta — alinhado a [[wiki/concepts/distributed-tracing]], [[wiki/concepts/eventual-consistency]] e [[wiki/concepts/mensageria]] (at-least-once + DLQ). A afirmação sobre "padrão dos brokers" é genérica: varia por broker e configuração (acks/replicação no Kafka, durabilidade/confirmações no RabbitMQ) [skill: tech-mentor-backend, `references/brokers-comparison.md`; não consultado em detalhe nesta sessão].

**Claim:** A comunicação assíncrona é base para estilos mais complexos: CQRS, Event Sourcing, arquitetura orientada a eventos e microsserviços — temas dos próximos vídeos.
**Evidência:** Fecho do vídeo.
**Confiança:** Alta — ver [[wiki/concepts/cqrs]], [[wiki/concepts/event-sourcing]], [[wiki/concepts/event-driven-architecture]], [[wiki/concepts/microsservicos]].

---

## Entidades e Conceitos Tocados

- [[wiki/entities/bernardo-lobato]] — autor
- [[wiki/concepts/comunicacao-sincrona]] — novo (stub)
- [[wiki/concepts/comunicacao-assincrona]] — novo (conceito central)
- [[wiki/concepts/async-request-reply]] — novo (stub): polling por ID de operação
- [[wiki/concepts/webhook]] — novo (stub): callback
- [[wiki/concepts/garantia-de-entrega]] — novo (stub)
- [[wiki/concepts/processamento-assincrono]] — stub promovido a draft
- [[wiki/concepts/mensageria]], [[wiki/entities/rabbitmq]], [[wiki/concepts/kafka]] — broker como forma principal
- [[wiki/concepts/temporal-coupling]], [[wiki/concepts/acoplamento]], [[wiki/concepts/tolerancia-a-falha]] — acoplamento e resiliência
- [[wiki/concepts/eventual-consistency]], [[wiki/concepts/event-driven-architecture]], [[wiki/concepts/cqrs]], [[wiki/concepts/event-sourcing]], [[wiki/concepts/microsservicos]] — estilos que dependem do modelo
- [[wiki/concepts/observabilidade]], [[wiki/concepts/distributed-tracing]] — resposta ao desafio de debug
- [[wiki/concepts/buffer]], [[wiki/concepts/websocket-vs-polling]] — fila como buffer de picos; polling como técnica

---

## Perguntas em Aberto

- O vídeo prometido sobre comunicação síncrona (benefícios e melhor aproveitamento) e o sobre mensageria ainda não estão na wiki.
- Como escolher entre polling, webhook e broker por critério (controle dos dois lados, latência, volume)? O vídeo só diz que polling/webhook são comuns quando não se controla todos os sistemas.
- Como tratar a experiência do usuário quando o resultado não é imediato (UI otimista, notificação, status)? Não abordado.

---

## Citações Preservadas

> "Quando a gente utiliza a comunicação assíncrona de uma maneira adequada, a gente percebe benefícios que podem salvar a sua arquitetura, que podem salvar o seu projeto."

> "É muito comum em times que estão adotando esse modelo [...] tentar emular como funcionaria uma comunicação síncrona com o modelo assíncrono. Isso não funciona."

> "Eventualmente ela vai ser atualizada, mas não necessariamente agora."
