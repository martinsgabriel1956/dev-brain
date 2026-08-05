---
type: concept
title: "Microsserviços"
aliases: ["microsservicos", "microservices", "arquitetura de microsserviços", "decomposição por domínio"]
date_created: 2026-07-24
date_updated: 2026-08-04
source_count: 9
tags: [microsservicos, arquitetura, bounded-context, distributed-monolith, circuit-breaker, resiliencia]
skill: tech-mentor-backend
status: draft
---

# Microsserviços

Estilo arquitetural em que o sistema é dividido em serviços pequenos e independentes, cada um responsável por uma parte específica do negócio (ex.: pagamentos, usuário, notificações). Cada microsserviço roda isolado, tem seu próprio banco de dados se bem implementado, e pode ser desenvolvido, implantado e escalado independentemente dos demais. A comunicação entre serviços acontece via API (REST, RPC) ou mensageria assíncrona (filas, eventos).

Raízes em arquitetura orientada a serviços do início dos anos 2000; popularizou-se a partir de 2014 com o artigo de Martin Fowler e James Lewis, e virou hype ao longo da década seguinte — inclusive como efeito manada, com projetos adotando o estilo desde o início sem necessidade real de escala ou de times separados. Ver [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]].

## O Artigo Original de 2014 (Fowler & Lewis)

[[wiki/sources/microsservicos-martin-fowler-james-lewis]] é o artigo-fonte que cunhou a definição hoje citada universalmente: um estilo de desenvolver uma aplicação única como um conjunto de pequenos serviços, cada um rodando no próprio processo, comunicando-se via mecanismos leves (tipicamente API HTTP), construídos em torno de **capacidades de negócio**, implantáveis por esteira totalmente automatizada, com o mínimo de gerenciamento centralizado. Os autores enumeram nove características comuns (não uma definição formal e obrigatória, já que nem toda arquitetura de microsserviços tem todas): Componentização via Serviços, Organização em Torno de Capacidades de Negócio, Produtos não Projetos, Endpoints Inteligentes e Tubos Burros ("smart endpoints, dumb pipes" — em oposição a ESBs, citando a frase de Jim Webber de que ESB significa "Erroneous Spaghetti Box"), Governança Descentralizada, Gerenciamento de Dados Descentralizado ([[wiki/concepts/circuit-breaker|Polyglot Persistence]]), Automação de Infraestrutura, Design for Failure e Design Evolutivo.

Ponto frequentemente perdido em resumos populares do artigo: os próprios autores **não** afirmam que microsserviços sejam definitivamente "o futuro" da arquitetura de software — encerram com "otimismo cauteloso", reconhecendo que fronteiras de serviço mal definidas são caras de refatorar entre processos (ao contrário de bibliotecas em processo), que complexidade pode simplesmente se deslocar do interior de um componente para as conexões confusas entre eles, e que um time pouco habilidoso constrói um sistema ruim independentemente do estilo escolhido — as verdadeiras consequências de uma decisão arquitetural, segundo eles, só ficam evidentes anos depois.

## Origem no Debate sobre SOA e a Lei de Conway

O artigo posiciona a decomposição por capacidade de negócio como reação direta à [[wiki/concepts/contexto-organizacional-para-arquitetura|Lei de Conway]] em ação: quando a gestão divide o time por camada técnica (times de UI, de lógica de servidor, de banco), cada mudança simples vira um projeto entre times, e a lógica de negócio acaba forçada para dentro de qualquer camada com acesso mais fácil — "lógica em todo lugar". A citação central de Melvin Conway (1968) — "qualquer organização que projeta um sistema produzirá um design cuja estrutura é uma cópia da estrutura de comunicação da organização" — é o mesmo argumento que, em outro artigo de Fowler de 2003, já aparecia aplicado à própria noção de fronteira de aplicação; ver [[wiki/concepts/application-boundary]].

Quanto a SOA: o artigo reconhece mérito na comparação (microsserviços é próximo do que "advocates de SOA" já defendiam), mas argumenta que o rótulo "SOA" acumulou significados contraditórios demais — na prática, a maioria das implementações chamadas de "SOA" tinha foco em ESBs integrando monolitos, com governança centralizada que ativamente inibia mudança. Daí a necessidade de um termo mais preciso.

## Decomposição Correta

O critério correto é decompor por **[[wiki/concepts/ddd-strategic|bounded context]]** (domínio de negócio), não por camada técnica. "Serviço de dados" + "Serviço de API" é um [[wiki/concepts/distributed-monolith|distributed monolith]] técnico disfarçado de microsserviços; "Orders Service" + "Payments Service" é decomposição real por domínio, com dados isolados e deploy independente.

## O Percurso Didático de Problemas: Deadlock → 2PC → Saga → CQRS

Uma aula constrói, problema por problema, o percurso que leva um microsserviço de banco compartilhado a uma arquitetura madura: banco compartilhado entre serviços causa [[wiki/concepts/deadlock]] → isolar banco por serviço ([[wiki/concepts/database-per-service]]) resolve o deadlock mas quebra atomicidade entre serviços (o "A" do [[wiki/concepts/acid]]) → [[wiki/concepts/two-phase-commit]] resolve a atomicidade mas não escala além de poucos serviços → [[wiki/concepts/saga-pattern]] via fila ([[wiki/entities/rabbitmq]]) e [[wiki/concepts/event-driven-architecture]] resolve o gargalo ao custo de compensação manual → escalar o banco separando leitura e escrita ([[wiki/concepts/cqrs]] com [[wiki/concepts/read-replicas]]) introduz replication lag. Reforça o argumento central desta página de que microsserviços trazem complexidade operacional real (consistência distribuída, latência de rede) que precisa ser resolvida com padrões específicos, não é "só separar em serviços menores". Ver [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]].

## Custo-Benefício

**Benefícios:** escalabilidade seletiva (escalar só o serviço que precisa), times menores e autônomos trabalhando em paralelo, maior resiliência (falha de um serviço não derruba necessariamente o sistema inteiro).

**Custos:** complexidade operacional bem maior — consistência de dados distribuída, latência de rede entre serviços, observabilidade sobre múltiplos serviços, orquestração de deploy, e padrões de resiliência obrigatórios ([[wiki/concepts/circuit-breaker]], retry, timeout) para lidar com falhas parciais que não existiam num processo único.

Segundo `references/architecture-foundations.md` da skill `tech-mentor-backend`, monolito modular é o ponto de partida correto para ~90% dos casos — o caminho arquitetural saudável é monolito bem modularizado → extrair microsserviço quando há necessidade real (escala diferente, time separado, deploy independente), não o inverso.

## Microsserviços como Eixo de Aprendizado (Não Só Estilo Arquitetural)

[[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]] argumenta que o valor de estudar microsserviços vai além de saber implementá-los em produção: o estudo funciona como um eixo unificado que amarra, de forma organizada e com propósito definido, uma dezena de conceitos avançados e dispersos de arquitetura — [[wiki/concepts/circuit-breaker|circuit breaker/retry/timeout]], [[wiki/concepts/observabilidade]], [[wiki/concepts/saga-pattern|saga pattern/consistência eventual]], [[wiki/concepts/mensageria|comunicação assíncrona]], contratos de API versionados, e cultura de times autônomos. Cada um desses conceitos se aplica integralmente dentro de um monólito ou backend único — não são exclusividade de sistemas distribuídos. O relato de primeira mão do autor: usar o hype de microsserviços de 2014 como norte de estudo, vindo de uma bagagem de sistemas distribuídos, foi o que o trouxe de volta ao mercado depois de quase 10 anos preso a monólitos legados.

## Reaproveitando Peças Prontas do Ecossistema

Mesmo fora de uma arquitetura de microsserviços completa, dá para reaproveitar componentes prontos desse ecossistema — ex.: Keycloak como serviço de autenticação/autorização (incluindo federação), evitando reinvestir tempo em um requisito já resolvido por software livre estabelecido. Ver [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]].

## Opinião Estável ao Longo da Carreira: Microsserviços Exigem Justificativa

[[wiki/sources/topicos-desenvolvimento-software-mudei-de-ideia-6-anos]] (Chris Kiehl) lista, entre as opiniões que **não** mudaram em 6 anos de carreira, que "monólitos são pretty good na maioria das circunstâncias" e "microsserviços exigem justificativa" — reforço direto e independente do argumento central já documentado nesta página (monolito modular como ponto de partida correto, extração só com necessidade real).

## Decisão Atribuída a Sênior-Plus

[[wiki/concepts/niveis-de-senioridade-system-design]] situa a decisão monolito vs. microsserviços — junto de SQL vs. NoSQL e serverless vs. servidor dedicado — como tipicamente atribuída a "sênior plus" (tech lead/CTO/staff), no contexto de desenvolver um sistema inteiro do zero para uma equipe trabalhar em cima. Em entrevista, essa mesma decisão aparece como um dos principais focos de discussão de tradeoffs no nível sênior.

## O Mesmo Princípio de Extração Tardia no Frontend

[[wiki/sources/arquitetura-frontend-microfrontends-monolito-modular-vertical-slice]] reforça, do lado frontend, a mesma tese de ponto de partida: [[wiki/concepts/monolito-modular-frontend|monolito modular]] com fronteiras por domínio é a base, [[wiki/concepts/vertical-slice-architecture|vertical slice]] isola funcionalidades complexas dentro do módulo, e só se migra para [[wiki/concepts/microfrontend-baseado-em-rotas|builds separados]] ou [[wiki/concepts/microfrontends-parciais|microfrontends distribuídos]] com necessidade real — nunca por hype ou pela imagem "arquitetura distribuída = madura" vendida em posts de LinkedIn.

## Sharding de Banco Como Consequência, Não Ponto de Partida

[[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] fecha o argumento pelo lado da persistência: não faz sentido tentar fazer [[wiki/concepts/sharding]] de um monolito inteiro com centenas de tabelas, porque não existe uma única entidade central óbvia para servir de shard key. A ordem correta é decompor primeiro por [[wiki/concepts/ddd|DDD]]/bounded context, e só então shardear o banco de dados de um microsserviço específico (onde a entidade principal — usuário, pedido, paciente — já está isolada). Reforça, de um ângulo de banco de dados, a mesma tese já central desta página: decomposição primeiro, escala de infraestrutura depois.

## O ESB Como o "Antigo Barramento Central" Que "Smart Endpoints, Dumb Pipes" Rejeita

[[wiki/concepts/esb-enterprise-service-bus|ESB]] não é só uma referência histórica dentro do artigo de Fowler/Lewis — é a peça concreta que a filosofia de microsserviços rejeitava na prática: em vez de concentrar transformação de mensagens e orquestração num barramento central, cada serviço vira responsável pela própria lógica, comunicando-se por mecanismos leves. Isso não significa que o ESB tenha desaparecido: em empresas com grande legado tecnológico, ele continua sendo a peça que integra sistemas de épocas diferentes enquanto a migração para uma arquitetura mais distribuída acontece de forma incremental.

## Key Sources

- [[wiki/sources/tecnologias-hype-passado-soap-xml-esb-jquery-cobol]] — ESB como contraponto histórico direto ao "smart endpoints, dumb pipes"; por que ESBs continuam essenciais em empresas com grande legado mesmo perdendo espaço em projetos novos
- [[wiki/sources/microsservicos-martin-fowler-james-lewis]] — artigo original de 2014 (James Lewis e Martin Fowler) que cunhou a definição do termo; nove características comuns, "smart endpoints and dumb pipes", Lei de Conway, Design for Failure, e a postura de "otimismo cauteloso" dos próprios autores
- [[wiki/sources/microsservicos]] — decomposição por bounded context, distributed monolith como anti-pattern, padrões de resiliência obrigatórios
- [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]] — microsserviços como guia/eixo de aprendizado de arquitetura, hype de 2014 em perspectiva histórica, relato pessoal de carreira, Keycloak como peça pronta reaproveitável
- [[wiki/sources/topicos-desenvolvimento-software-mudei-de-ideia-6-anos]] — "microsserviços exigem justificativa" como opinião estável (não mudou em 6 anos), reforçando a mesma tese por um ângulo independente
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]] — monolito vs. microsserviços como decisão de sênior-plus, e como tópico de tradeoff cobrado em entrevista sênior
- [[wiki/sources/arquitetura-frontend-microfrontends-monolito-modular-vertical-slice]] — mesmo princípio de extração tardia (monolito modular → vertical slice → builds separados) aplicado à arquitetura frontend
- [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]] — percurso didático incremental deadlock → database-per-service → 2PC → Saga Pattern → CQRS, construindo problema por problema
- [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] — sharding de banco como consequência da decomposição por DDD, não como técnica aplicável a um monolito inteiro
